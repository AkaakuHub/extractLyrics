import sys
from bs4 import BeautifulSoup

with open("input.txt", "r", encoding="utf-8") as i0:
    l = i0.read()

if '<div jsname="WbKHeb">' in l:
    # google
    i1 = l.replace("</span>", "\n")
else:
    # uta-net, j-lyrics, kkboxは対応
    i1 = l.replace("<br>", "\n")

s = BeautifulSoup(i1, "html.parser")
o1 = s.get_text()
with open("output.txt", "w") as f:
    f.write(o1)
