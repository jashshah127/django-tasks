import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter, inch
from reportlab.lib.pagesizes import A4

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, XPreformatted
from reportlab.rl_config import defaultPageSize
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import BaseDocTemplate


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline' #Conttent can be disposed as inline(open view in new tab), attachment)(downloaded)

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # p = BaseDocTemplate(p,showBoundary=1,leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0, pagesize=A4)
    # p.setPageSize( landscape(letter) )
    orient=request.GET.get('orient')
    if (orient=="00"):  #landscape
        height, width = 8.5*inch, 11*inch
    elif(orient=="01"): #portait
        height, width = 11*inch, 8.5*inch
    p.setPageSize( (width, height) )   
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # PAGE_HEIGHT = defaultPageSize[1]; PAGE_WIDTH = defaultPageSize[0]
    # BottomMargin = 0.4 * inch
    # TopMargin = 0.0 * inch
    # LeftMargin = .1 * inch  
    # RightMargin = .1 * inch
    # ContentBottomMargin = TopMargin + 0.25 * inch
    # ContentTopMargin = BottomMargin + 0.35 * inch
    # ContentLeftMargin = LeftMargin 
    # ContentRightMargin = RightMargin 

    # frameT = Frame(p.leftMargin, p.bottomMargin, p.width, p.height,topPadding=0, id='normal')
    
    frame = Frame(
                    0.1*inch,     # x
                    0.1*inch,     # y at bottom
                    width - 0.2*inch,     # width
                    height - 0.2*inch,     # height
                    showBoundary = 1  # helps us see what's going on
                    )
    
    frame.drawBoundary(p)

    data = [
    ['Sequence Number','Name', 'Surname', 'Likes Python or Not'],
    ['001','Jash ', 'Shah', 'Yes'],
    ['002','Naitik ', 'Gala', 'Yes'],
    ['003','Moxi ', 'Sanghvi', 'No'],
    ['004','Harshil ', 'Mehta', 'Yes'],
    ['null','null ', 'null', 'null']
    ]

    width = 400
    height = 100
    x = 100
    y = 500
    f = Table(data)

    style = TableStyle([
    ('BACKGROUND',(0,0),(3,0), colors.orange),
    ('TEXTCOLOR',(0,0),(-1,0), colors.whitesmoke),

    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME',(0,0),(-1,0), 'Courier-Bold'),
    ('FONTSIZE',(0,0),(-1,0), 14),

    ('BOTTOMPADDING',(0,0),(-1,0), 12),
    ('BACKGROUND',(0,1),(-1,-1), colors.beige),
    ])

    f.setStyle(style)

    ts = TableStyle(
        [
        ('BOX',(0,0),(-1,-1), 2, colors.beige),    
        ('LINEABOVE',(0,2),(-1,-2), 2, colors.orange),
        ('LINEABOVE',(0,3),(-1,-1), 2, colors.orange),
        ('LINEABOVE',(0,4),(-1,-1), 2, colors.orange),
        ('GRID',(0,1),(-1,-1), 2, colors.black)
        ]
    )
    f.setStyle(ts)
    f.wrapOn(p, width, height)
    f.drawOn(p, x,y)


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def border(request):
    return FileResponse