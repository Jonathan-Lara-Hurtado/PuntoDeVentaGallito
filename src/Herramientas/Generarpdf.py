from reportlab.pdfgen import canvas

c = canvas.Canvas("gato.pdf")
c.drawString(50,50,"!hOLA MUNDO")
c.save()
