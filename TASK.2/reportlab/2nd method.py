from reportlab.pdfgen import canvas


def Title(filename):
    
   # filename = 'Mydoc.pdf'
    documentTitle = 'Document Title!'
    title = 'ABC'
    subtitle = 'Normal ReportLab Execution'

    textlines = [
        'trying reportlab for the first time',
        'it seems easy, lets hope'
    ]

    pdf = canvas.Canvas(filename)

    pdf.save()


Title('jashshah.pdf')