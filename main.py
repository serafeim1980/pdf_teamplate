from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    #set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, text=row["Topic"], align="L",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    pdf.line(10, 21, 200, 21)

    # set the footer
    pdf.ln(267)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10,text=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, text=row["Topic"], align="R")
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)


pdf.output("output.pdf")
