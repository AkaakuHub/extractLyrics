import sys
from bs4 import BeautifulSoup

with open("input.txt", "r", encoding="utf-8") as i0:
    i1 = i0.read().replace("</span>", "\n")
s = BeautifulSoup(i1, "html.parser")
o1 = s.get_text()
with open("output.txt", "w") as f:
    f.write(o1)
