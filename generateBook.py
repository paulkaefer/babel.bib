
import os # os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
import random

# available characters
# for now, more spaces makes spaces more likely to appear
# in the future, consider giving spaces more likely random chance (can we do that without increasing complexity?)
bookChars  = 'abcdefghijklmnopqrstuvwxyz     ,.'
titleChars = 'abcdefghijklmnopqrstuvwxyz     '

os.mkdir("tmp")
book = open("files/book.tex", 'w')

def randomChar(charSet, n):
    l = len(charSet)
    s = ""
    for i in xrange(0,n):
        thisChar = charSet[random.randrange(l)]
        s = s + thisChar
    return s

bookTitle = randomChar(titleChars, random.randrange(48)+2)

book.close()

os.rmdir("tmp")

