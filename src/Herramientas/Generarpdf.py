import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class CrearTicket:
    def __init__(self):
        self.data = [("Id Compra", "fechaventa","Subtotal","iva", "total")]
        self.data2= [("producto","Cantidad","Precio")]

    def addData(self,v):
        self.data.append(v)

    def addData2(self,v):
        self.data2.append(v)

    def grouper(self,iterable, n):
        args = [iter(iterable)] * n
        return itertools.zip_longest(*args)

    def export_to_pdf(self,data,data2):
        c = canvas.Canvas("Ticket.pdf", pagesize=A4)
        w, h = A4
        max_rows_per_page = 45
        # Margin.
        x_offset = 30
        y_offset = 120
        # Space between rows.
        padding = 15
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 30)
        c.drawString(x_offset, 790, "Gallito Negro")

        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 20)
        c.drawString(x_offset, 730, "Compra")

        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 12)

        xlist = [x + x_offset for x in [0, 90, 250, 300, 350, 400]]
        ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]

        for rows in self.grouper(data, max_rows_per_page):
            rows = tuple(filter(bool, rows))
            c.grid(xlist, ylist[:len(rows) + 1])
            for y, row in zip(ylist[:-1], rows):
                for x, cell in zip(xlist, row):
                    c.drawString(x + 2, y - padding + 3, str(cell))

        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 20)
        c.drawString(x_offset, 640, "Articulos")


        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 12)


        y_offset = 100+120
        padding = 15

        xlist = [x + x_offset for x in [0, 90, 250, 300]]
        ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]


        for rows in self.grouper(data2, max_rows_per_page):
            rows = tuple(filter(bool, rows))
            c.grid(xlist, ylist[:len(rows) + 1])

            for y, row in zip(ylist[:-1], rows):
                for x, cell in zip(xlist, row):
                    c.drawString(x + 2, y - padding + 3, str(cell))
            c.showPage()


        c.save()

    def generar(self):
        self.export_to_pdf(self.data,self.data2)

"""
a = ("1","2","3","4","5")
b =("11","22","31")
c = CrearTicket()
c.addData(a)
c.addData2(b)
c.addData2(b)
c.addData2(b)
c.addData2(b)
c.generar()
"""