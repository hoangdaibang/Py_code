import pyttsx3
import PyPDF2

sach=open(r'SE.pdf', 'rb')
pdfReader=PyPDF2.PdfFileReader(sach)
pages=pdfReader.numPages
print(pages)


bot=pyttsx3.init()
voice= bot.getProperty('voices')
voice= bot.setProperty('voice',voice[1].id)
for num in range (8,pages):
    page=pdfReader.getPage(8)
    text=page.extractText()
    bot.say(text)
    bot.runAndWait()