'''
Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt,
shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs,
using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard,
with these specifications:

    The orientation of the PDF should be Portrait.
    The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    The shirt’s image should be centered horizontally.
    The user’s name should be on top of the shirt, in white text.

All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate
needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.
'''
from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", size=50)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='c')
        self._pdf.image("shirtificate.png", w = self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x= 42, y=140, txt=f"{name} took CS50" )

    def save(self, filename):
        self._pdf.output(filename)

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate1.pdf")