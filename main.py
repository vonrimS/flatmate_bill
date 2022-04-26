import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period



class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    Creates a PDF file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A5')
        pdf.add_page()

        # Add icon
        pdf.image(name='files/house.png', w=50, h=50)

        # Insert title
        pdf.set_font(family='Times', size=30, style='B')
        pdf.cell(w=0, h=40, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=150, h=40, txt='Period:', border=1, align='C')
        pdf.cell(w=0, h=40, txt=bill.period, border=1, align='C', ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=10, style='' )
        pdf.cell(w=150, h=40, txt=flatmate1.name, border=1, align='C')
        pdf.cell(w=0, h=40, txt=flatmate1_pay, border=1, align='C', ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=150, h=40, txt=flatmate2.name, border=1, align='C')
        pdf.cell(w=0, h=40, txt=flatmate2_pay, border=1, align='C', ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


bill = Bill(amount=120, period='April 2022')
john = Flatmate(name='John', days_in_house=20)
marry = Flatmate(name='Marry', days_in_house=25)

print('John pays: ', john.pays(bill=bill, flatmate2=marry))
print('Marry pays: ', marry.pays(bill=bill, flatmate2=john))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=bill)