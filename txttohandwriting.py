from PIL import Image
from fpdf import FPDF
from PIL import Image
import os
BG = Image.open("myfont/bg.png")
sizeOfSheet = BG.width
pages,gap, _ = 0, 100, 250
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890:'


def writee(char):
    global gap, _
    if char == '\n':
        pass
    else:
        char.lower()
        cases = Image.open("myfont/%s.png" % char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases


def letterwrite(word):
    global gap, _
    if word == '*':
        gap = 100
        _ += 220
        writee('space')
    if gap > sizeOfSheet - 98 * (len(word)):
        gap = 100
        _ += 170
        writee('space')
    for letter in word:
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hiphen'
            elif letter == ':':
                letter = 'colon'
            writee(letter)


def worddd(Input):
    wordlist = Input.split(' ')
    for i in wordlist:
        if '*' in i:
            letterwrite(i)
        else:
            letterwrite(i)
            writee('space')
            
if __name__ == '__main__':
    try:
        with open('boom.txt', 'r') as file:
            data = file.read().replace('\n',' * \n')

        with open('final_output.pdf', 'w') as file:
            pass

        data = data.strip()
        data = data.split(" ")
        p = data
        writee('space')
        for i in range(0, len(p)-1):
            worddd(p[i])
            if _< 2800:
                continue
            pages += 1
            BG.save('%doutt.png' % pages)
            BG1 = Image.open("myfont/bg.png")
            BG = BG1
            gap = 100
            _ = 250
            writee('space')
            print(pages)
        if _ > 0 or gap > 0:
            pages += 1
            BG.save('%doutt.png' % pages)
            BG1 = Image.open("myfont/bg.png")
            BG = BG1
            gap = 100
            _ = 250
            writee('space')
            print(pages)
    except ValueError as E:
        print("{}\nTry again".format(E))

imagelist = []
for i in range(1, pages+1):
    imagelist.append('%doutt.png' % i)

#Converting images to pdf
#Source:https://datatofish.com/images-to-pdf-python/


def pdf_creation(PNG_FILE, flag=False):
    rgba = Image.open(PNG_FILE)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split()[3])  # paste using alpha channel as mask
    rgb.save('final_output.pdf',
             append=flag)  #Now save multiple images in same pdf file


#First create a pdf file if not created
pdf_creation(imagelist.pop(0))

#Now I am opening each images and converting them to pdf
#Appending them to pdfs
for PNG_FILE in imagelist:
    pdf_creation(PNG_FILE, flag=True)
