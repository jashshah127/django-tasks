from reportlab.pdfgen import canvas
from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
c = canvas.Canvas("samples.pdf")
c.drawString(10,50,"Hello this is Jash and This is my pdf at :"+str(today)+str(now))
c.save()
