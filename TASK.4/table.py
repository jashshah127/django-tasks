from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

data = [
    ['Sequence Number','Name', 'Surname', 'Likes Python or Not'],
    ['001','Jash ', 'Shah', 'Yes'],
    ['002','Naitik ', 'Gala', 'Yes'],
    ['003','Moxi ', 'Sanghvi', 'No'],
    ['004','Harshil ', 'Mehta', 'Yes'],
    ['null','null ', 'null', 'null']
]

fileName = 'table.pdf'


pdf = SimpleDocTemplate(
    fileName,
    pagesize = letter
)


table =Table(data)

style = TableStyle([
    ('BACKGROUND',(0,0),(3,0), colors.orange),
    ('TEXTCOLOR',(0,0),(-1,0), colors.whitesmoke),

    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME',(0,0),(-1,0), 'Courier-Bold'),
    ('FONTSIZE',(0,0),(-1,0), 14),

    ('BOTTOMPADDING',(0,0),(-1,0), 12),
    ('BACKGROUND',(0,1),(-1,-1), colors.beige),
])

table.setStyle(style)

ts = TableStyle(
    [
    ('BOX',(0,0),(-1,-1), 2, colors.beige),    
    ('LINEABOVE',(0,2),(-1,-2), 2, colors.orange),
    ('LINEABOVE',(0,3),(-1,-1), 2, colors.orange),
    ('LINEABOVE',(0,4),(-1,-1), 2, colors.orange),
    ('GRID',(0,1),(-1,-1), 2, colors.black)
    ]
)
table.setStyle(ts)

elems = []
elems.append(table)

pdf.build(elems)
