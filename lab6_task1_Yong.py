import click
from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
import time

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 


def welcome():
    displayText('etch a skech',lcd,20,10)
    time.sleep(1.2)
    clearScreen(lcd)


welcome()
x=64
y=32
while 1:  
    c = click.getchar()  
    if c=='\x1b[A':
       y-=1
       while y<0:y=63
       lcd.set_pixel(x,y,1)
       lcd.show()
    elif c=='\x1b[B':
       y+=1
       while y>63:y=0
       lcd.set_pixel(x,y,1)
       lcd.show()
    elif c=='\x1b[C':
       x+=1
       while x>127:x=0
       lcd.set_pixel(x,y,1)
       lcd.show()
    elif c=='\x1b[D':
       x-=1
       while x<0:x=127
       lcd.set_pixel(x,y,1)
       lcd.show()
    elif c== 'q':
        displayText('goodbye',lcd,25,15)
        break
    elif c== 's':      
        welcome()
        displayText('Draw wite arrow',lcd,5,10) 
        time.sleep(1.5)     
        clearScreen(lcd)
        x=64
        y=32
        lcd.set_pixel(x,y,1)
        lcd.show()
    else:
        pass
        welcome()
        displayText('press s to start',lcd,10,15)
        time.sleep(1)
        clearScreen(lcd)

