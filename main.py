import pyttsx3
import PyPDF2 
from tkinter.filedialog import *

the_book = askopenfilename()
pdfreader = PyPDF2.PdfReader(the_book)
pages = len(pdfreader.pages)

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
