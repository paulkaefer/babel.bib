
import os # os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos' --> if Windows, system commands are different
import random

# available characters
# for now, more spaces makes spaces more likely to appear
# in the future, consider giving spaces more likely random chance (can we do that without increasing complexity?)
bookChars  = 'abcdefghijklmnopqrstuvwxyz      ,.'
titleChars = 'abcdefghijklmnopqrstuvwxyz      '

nPages = 410
nLinesPerPage = 40
nCharsPerLine = 80

totalChars = nCharsPerLine * nLinesPerPage * nPages
# (in theory, you can also have it print out, or include as a footnote,
#   "this is one of N possible/available books in our library")
#
# could we generate the hash and assign it a number, based on 00000...0 being 0 and fffff...f being N?
# or are hash collisions common in the large number of possible books?
#
# how does libraryofbabel.info do a "library catalogue"?

book = open("book.tex", 'w')

def randomChar(charSet, n):
    l = len(charSet)
    s = ""
    for i in xrange(0,n):
        thisChar = charSet[random.randrange(l)]
        s = s + thisChar
    return s

bookText = randomChar(bookChars, totalChars)

bookTitle = randomChar(titleChars, random.randrange(48)+2)
book.write("\\documentclass[12pt]{article}\n\n")

# "quickest" way to change margins, as per http://kb.mit.edu/confluence/pages/viewpage.action?pageId=3907057
# and "landscape" mode: landscape, 
#   http://texblog.org/2007/11/10/landscape-in-latex/
book.write("\\usepackage[margin=1in]{geometry}")
# for coloring single pages
# http://tex.stackexchange.com/questions/25137/how-to-change-the-background-color-only-for-the-current-page
book.write("\\usepackage{afterpage}")
book.write("\\usepackage[usenames,dvipsnames,svgnames]{xcolor}")

book.write("\\title{" + bookTitle + "}\n\n")
book.write("\\author{ }\n\n")
book.write("\\begin{document}\n\n")
book.write("\\maketitle\n\n")

book.write("\\pagecolor{ForestGreen}\\afterpage{\\nopagecolor}")

book.write("\\newpage\n\n")

ptr = 0
for iPage in xrange(nPages):
    for iLine in xrange(nLinesPerPage):
        book.write("\\noindent " + bookText[ptr:ptr+nCharsPerLine] + "\n\n")
        ptr = ptr + nCharsPerLine
    
    book.write("\n\n\\newpage\n\n")

# empty page http://www.kronto.org/thesis/tips/empty-pages.html
book.write("\\mbox{}")
book.write("\\pagecolor{ForestGreen}\\afterpage{\\nopagecolor}")

book.write("\\newpage\n\n")

book.write("\\end{document}\n\n")

book.close()


