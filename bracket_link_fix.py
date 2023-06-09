# ASSUMPTION: There are no bracket errors in the document, so all unequal brackets are VALID ie. The number of open brackets in the document matches the number of closed brackets

""" Use Case: Allows TexSoup to correctly parse LaTeX documents that contain mismatched brackets and/or links containing '%' signs
- NOTE: for links, the relevant command must be included in the 'LINK_COMMANDS' constant, and the link must be the FIRST ARGUMENT of the relevant command (can fix for this in future if required)

The output '.tex' file will have '_fixed' appended to the filename and the document itself will be changed, but it will render the same as before. There is no change in rendered content. 
The only effect is allowing TexSoup to parse without error.
 """

import re

# List of commands that pass links as arguments, feel free to add to, link must be FIRST ARGUMENT in this version
LINK_COMMANDS = ['href', 'url']


def fix_brackets(filename, encoder = "utf-8"):
    r"""Takes a provided relative filepath 'filename' for a text file (.tex intended). Fixes unmatched brackets by encompassing in curly brackets and fixes links that include '%' characters
    by prepending an escape character '\'.

    Args:
        filename (str): filename of file to be 'fixed', include relative path from current working directory
        encoder (str): encoding type passed to file reader and writer ie: "utf-8", "ascii"

    Example Unmatched Brackets:
        Input Text: $(0, 32)]$
        Output Text: ${(0,32]}$

    Example Link:
        Input Text: \href{https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory}{ZFC Axioms}
        Output Text: \href{https://en.wikipedia.org/wiki/Zermelo\%E2\%80\%93Fraenkel_set_theory}{ZFC Axioms}

        Input Text:\url{https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory}
        Output Text:\url{https://en.wikipedia.org/wiki/Zermelo\%E2\%80\%93Fraenkel_set_theory}

    Example Complex:
        Input Text:
                \url{https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory}
                $[ 0 \text{ random mismatched in tex [3, 4)} [\inf, 4 ( 45, \inf) 32)]$
                \href{https://en.wikipedia.org/wiki/Construction_of_the_real_numbers}{ZFC Axioms}
        Output Text: 
                \url{https://en.wikipedia.org/wiki/Zermelo\%E2\%80\%93Fraenkel_set_theory}
                $[ 0 \text{ random mismatched in tex {[3, 4)}} {[\inf, 4 ( 45, \inf) 32)}]$
                \href{https://en.wikipedia.org/wiki/Construction_of_the_real_numbers}{ZFC Axioms}"""

    # Ensure list of relevant link commands is sorted by length
    LINK_COMMANDS.sort(key = len)

    extension = "." + filename.split(".")[-1]
    filenamelist = filename.split(".")[0:-1]

    fileroot = ""

    for i in filenamelist:
        fileroot += i

    brackets = "[("
    f = open(filename,'r', encoding = encoder) # assuming other languages will be supported in TexSoup
    w = open(fileroot+'_fixed'+extension, 'w', encoding = encoder)

    while True:
        k = f.read(1)
        if not k:
            break
        if (k in brackets):
            w.write(__encapsulate_bad_brackets(file = f, brack = k))

        # To catch and fix 'href' link errors (percentage sign in link)
        elif k == "\\":
            w.write(k)
            linkcheck_string = __link_check_fix(file = f)
            split_str = ""

            # accounting for when characters read by link_check_fix include brackets
            for i in linkcheck_string:
                if i in brackets:
                    chck = "(\\" + i + ")"
                    split_str = re.split(chck, linkcheck_string)
                    break
                
            if type(split_str) == str:
                w.write(linkcheck_string)
            else:
                w.write(split_str[0])
                aft_brack = "".join(split_str[1:])
                w.write(__encapsulate_bad_brackets(file = f, chk_str=aft_brack))
        
        else:
            w.write(k)

    f.close()
    w.close()
        

def __encapsulate_bad_brackets(file, brack = "", chk_str = ""):
    r"""Identifies open brackets '[' or '(' and all characters read between them. If a bracket is closed by another bracket that does not match it, encapsulates the
    unmatched brackets statement with outer curly braces ie. [\inf, 3) -> {[\inf, 3)}

    Args:
        file (TextIOWrapper): Input stream reading from a given file
        brack (str): the last character read, a bracket either '[' or '('
        chk_str (str): previously read characters that aren't checked for brackets

    Returns:
        str: all text read from the input parameter open bracket 'brack' to the bracket that closes said statement, with any mismatched bracketed statements now
        enclosed in curly braces

    Example Unmatched Brackets:
        Input Text: $(0, 32)]$
        Output Text: ${(0,32]}$

    Example Nested Unmatched Brackets:
        Input Text: $[ [\inf, (,) 32) ]$
        Ouput Text: $[ {[\inf, (,) 32)} ]$
    """

    brackets = {"[":"]", "(":")"}
    stringlist = []

    if not brack:
        brack = chk_str[0]

    stack = [brack]
    index = 1
    stmp = brack

    while True:
        if index < len(chk_str):
            k = chk_str[index]
            index += 1
        else:
            k = file.read(1)
        
        if not k and True:
            break

        if len(stack) == 0: # detects if stack is empty therefore all brackets closed
            stmp += k
            break 
        elif k in "[(": 
            stack.append(k)
            stringlist.append(stmp)
            stmp = k
        elif k not in "])":
            stmp += k
        elif k == brackets[stack[-1]]:
            stack.pop()
            stmp += k
            if stringlist:
                stmp = stringlist.pop() + stmp 
                #append the current matched brackets to the prior unclosed string, store in the temporary string then remove final cell of list
            elif not stringlist: # as an else statement this gets skipped, negation elif statement used
                break 

        else: #unmatched brackets

            stmp = "{" + stmp + k + "}"
            stack.pop()  
            if stringlist:
                stmp = stringlist.pop() + stmp

    while index < len(chk_str):
        stmp += chk_str[index]
        index += 1
    
    return stmp


def __link_check_fix(file):
    r"""Identifies whether a command relates to a link, if so, checkes for any '%' characters within the link and prepends an escape character '%' to all found.

    Args:
        file (TextIOWrapper): Input stream reading from a given file

    Returns:
        str: all text read from file with any '%' sign in links prepending with an escape character

    Examples:
        Input Text: href{https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory}{ZFC Axioms}
        Output Text: href{https://en.wikipedia.org/wiki/Zermelo\%E2\%80\%93Fraenkel_set_theory}{ZFC Axioms}

        Input Text:url{https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory}
        Output Text:url{https://en.wikipedia.org/wiki/Zermelo\%E2\%80\%93Fraenkel_set_theory}

        Input Text:href{https://en.wikipedia.org/wiki/Construction_of_the_real_numbers}{Construction of Real Numbers}
        Output Text:href{https://en.wikipedia.org/wiki/Construction_of_the_real_numbers}{Construction of Real Numbers}

        Input Text: textbf
        Output Text: textbf
    """

    k = file.read(len(LINK_COMMANDS[0]))

    for i in LINK_COMMANDS:
        if len(i) == len(k):
            if k in LINK_COMMANDS:
                break
        elif len(i) > len(k):
            k += file.read(len(i)-len(k))
            print("\n"+repr(k))

            if k in LINK_COMMANDS:
                break
        
        #All relevant commands checked, none are for links, return all text read
        if i == LINK_COMMANDS[-1]:
            return k

    stmp = k
    while True:
        k = file.read(1)
        if not k and True:
            break

        if k == "%":
            stmp += "\\" + k

        elif k == "}":
            stmp += k
            break

        else:
            stmp +=k

    return stmp

### below here is not covered on tests
def main():
    fix_brackets("tests\\sample\\brack_test10.tex", "utf-8")

if __name__ == '__main__':
    main()