import os, PyPDF2

userpdflocation = str(input('Your Folder Location: '))
os.chdir(userpdflocation)

userfilename = input('What should i call the file?: ')
From_Page_No = int(input("Starting Page no: "))
To_Page_No + int(input("Till page no: "))
pdf2merge = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf2merge.append(filename)

pdfWriter = PyPDF2.PdfFileWriter()


for filename in pdf2merge:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #for pageNum in range(1, pdfReader.numPages):
	for pageNum in range(From_Page_No, To_Page_No):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)


pdfOutput = open(userfilename+'.pdf', 'wb')

pdfWriter.write(pdfOutput)

pdfOutput.close()

print("I have saved your file," +userfilename)