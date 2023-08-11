from PyPDF2 import PdfMerger

AllPDF = ['1.pdf.pdf', '2.pdf.pdf']

OurMerger = PdfMerger()

for NewPDF in AllPDF:
    OurMerger.append(NewPDF)

OurMerger.write('Nasim.pdf')
OurMerger.close()