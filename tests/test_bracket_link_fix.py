import bracket_link_fix
import os


def test_fix_brackets():

    encoder = "utf-8"

    with open("sample\\brack_test1_exp.tex",'r', encoding = encoder) as f:
        expected1 = f.read()
    
    with open("sample\\brack_test2_exp.tex",'r', encoding = encoder) as f:
        expected2 = f.read()

    with open("sample\\brack_test3_exp.tex",'r', encoding = encoder) as f:
        expected3 = f.read()

    with open("sample\\brack_test4_exp.tex",'r', encoding = encoder) as f:
        expected4 = f.read()

    with open("sample\\brack_test5_exp.tex",'r', encoding = encoder) as f:
        expected5 = f.read()

    with open("sample\\brack_test6_exp.tex",'r', encoding = encoder) as f:
        expected6 = f.read()

    with open("sample\\brack_test7.tex",'r', encoding = encoder) as f:
        expected7 = f.read()

    with open("sample\\brack_test8_exp.tex",'r', encoding = encoder) as f:
        expected8 = f.read()

    with open("sample\\brack_test9_exp.tex",'r', encoding = encoder) as f:
        expected9 = f.read()
    
    with open("sample\\brack_test10_exp.tex",'r', encoding = encoder) as f:
        expected10 = f.read()

    with open("sample\\href_only_exp.tex", 'r', encoding = encoder) as f:
        expected11 = f.read()

    with open("sample\\url_only_exp.tex", 'r', encoding = encoder) as f:
        expected12 = f.read()

    with open("sample\\href_url_brackets_exp.tex", 'r', encoding = encoder) as f:
        expected13 = f.read()

    bracket_link_fix.fix_brackets("sample\\brack_test1.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test2.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test3.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test4.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test5.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test6.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test7.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test8.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test9.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\brack_test10.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\href_only.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\url_only.tex", encoder)
    bracket_link_fix.fix_brackets("sample\\href_url_brackets.tex", encoder)


    with open("sample\\brack_test1_fixed.tex",'r', encoding = encoder) as f:
        actual1 = f.read()

    os.remove("sample\\brack_test1_fixed.tex")

    with open("sample\\brack_test2_fixed.tex",'r', encoding = encoder) as f:
        actual2 = f.read()

    os.remove("sample\\brack_test2_fixed.tex")
    
    with open("sample\\brack_test3_fixed.tex",'r', encoding = encoder) as f:
        actual3 = f.read()

    os.remove("sample\\brack_test3_fixed.tex")
    
    with open("sample\\brack_test4_fixed.tex",'r', encoding = encoder) as f:
        actual4 = f.read()

    os.remove("sample\\brack_test4_fixed.tex")
    
    with open("sample\\brack_test5_fixed.tex",'r', encoding = encoder) as f:
        actual5 = f.read()

    os.remove("sample\\brack_test5_fixed.tex")
    
    with open("sample\\brack_test6_fixed.tex",'r', encoding = encoder) as f:
        actual6 = f.read()

    os.remove("sample\\brack_test6_fixed.tex")

    with open("sample\\brack_test7_fixed.tex",'r', encoding = encoder) as f:
        actual7 = f.read()

    os.remove("sample\\brack_test7_fixed.tex")
    
    with open("sample\\brack_test8_fixed.tex",'r', encoding = encoder) as f:
        actual8 = f.read()

    os.remove("sample\\brack_test8_fixed.tex")
    
    with open("sample\\brack_test9_fixed.tex",'r', encoding = encoder) as f:
        actual9 = f.read()

    os.remove("sample\\brack_test9_fixed.tex")

    with open("sample\\brack_test10_fixed.tex",'r', encoding = encoder) as f:
        actual10 = f.read()

    os.remove("sample\\brack_test10_fixed.tex")

    with open("sample\\href_only_fixed.tex",'r', encoding = encoder) as f:
        actual11 = f.read()

    os.remove("sample\\href_only_fixed.tex")

    with open("sample\\url_only_fixed.tex",'r', encoding = encoder) as f:
        actual12 = f.read()

    os.remove("sample\\url_only_fixed.tex")

    with open("sample\\href_url_brackets_fixed.tex",'r', encoding = encoder) as f:
        actual13 = f.read()

    os.remove("sample\\href_url_brackets_fixed.tex")

    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
    assert actual4 == expected4
    assert actual5 == expected5
    assert actual6 == expected6
    assert actual7 == expected7
    assert actual8 == expected8
    assert actual9 == expected9
    assert actual10 == expected10
    assert actual11 == expected11
    assert actual12 == expected12
    assert actual13 == expected13

