# Unmatched Bracket and Link Fix for TexSoup

An optional fix for TexSoup parsing errors on documents with unmatched brackets:

- ie. [ x , y ) 

and hyperlinks containing '%' signs: 
- ie. href{https://random.domain.com/look%E2%80here}{Rendered Name}

---
Creates a new version of your LaTeX document that is both LaTeX render-safe and TexSoup parse-safe, without changing the rendered output.

---

This fix is intended for use with TexSoup, a fault-tolerant, Python3 package for searching, navigating, and modifying LaTeX documents created by [Alvin Wan](https://github.com/alvinwan). Check TexSoup out here:

- [TexSoup Website](https://texsoup.alvinwan.com)
- [TexSoup GitHub](https://github.com/alvinwan/TexSoup)
