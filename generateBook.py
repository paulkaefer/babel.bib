
import os # os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
import random

# available characters
# for now, more spaces makes spaces more likely to appear
# in the future, consider giving spaces more likely random chance (can we do that without increasing complexity?)
bookChars  = 'abcdefghijklmnopqrstuvwxyz     ,.'
titleChars = 'abcdefghijklmnopqrstuvwxyz     '

nPages = 410
nLinesPerPage = 20
nCharsPerLine = 80

totalChars = nCharsPerLine * nLinesPerPage * nPages
# (in theory, you can also have it print out, or include as a footnote,
#   "this is one of N possible/available books in our library)
#
# could we generate the hash and assign it a number, based on 00000...0 being 0 and fffff...f being N?
# or are hash collisions common in the large number of possible books?
#
# how does libraryofbabel.info do a "library catalogue"?

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

bookText = randomChar(bookChars, totalChars)

bookTitle = randomChar(titleChars, random.randrange(48)+2)
book.write("\\documentclass{article}\n\n")
book.write("\\title{" + bookTitle + "}\n\n")
book.write("\\author{ }\n\n")
book.write("\\begin{document}\n\n")
book.write("\\maketitle\n\n")

book.write("\\newpage\n\n")

ptr = 0
for iPage in xrange(nPages):
    for iLine in xrange(nLinesPerPage):
        book.write(bookText[ptr:ptr+nCharsPerLine])
        ptr = ptr + nCharsPerLine
        book.write("\n\n")
    book.write("\\newpage\n\n")

#book.write(bookText)

# separate the book onto individual pages... use the following:
#\input{Chapters/chapter_1}
#% each chapter may have \begin{singlespace}
#% which may require Assets/doublespace.sty from thesis

book.write("\\newpage\n\n")

book.write("\\end{document}\n\n")

# bookTitle in large font on first page

book.close()

# will be handled by book.php
#os.rmdir("tmp")

