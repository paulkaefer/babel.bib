
import os # os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
import random

# available characters
# for now, more spaces makes spaces more likely to appear
# in the future, consider giving spaces more likely random chance (can we do that without increasing complexity?)
bookChars  = 'abcdefghijklmnopqrstuvwxyz     ,.'
titleChars = 'abcdefghijklmnopqrstuvwxyz     '

#os.mkdir("/tmp/book/")
#book = open("/tmp/book/book.tex", 'w')
book = open("book.tex", 'w')
os.mkdir("tmp")

def randomChar(charSet, n):
    l = len(charSet)
    s = ""
    for i in xrange(0,n):
        thisChar = charSet[random.randrange(l)]
        s = s + thisChar
    return s

bookTitle = randomChar(titleChars, random.randrange(48)+2)
book.write("\\documentclass{article}\n\n")
book.write("\\title{" + bookTitle + "}\n\n")
book.write("\\begin{document}\n\n")
book.write("\\maketitle\n\n")

#\input{Chapters/chapter_1}
#% each chapter may have \begin{singlespace}
#% which may require Assets/doublespace.sty from thesis

book.write("\\end{document}\n\n")

# bookTitle in large font on first page

book.close()

# will be handled by book.php
#os.rmdir("tmp")

