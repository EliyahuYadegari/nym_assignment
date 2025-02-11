import pdfplumber
from pdf_utils import pdf_to_dict
from chart import populate_chart

def main():

    with pdfplumber.open("samples/chart3.pdf") as pdf:
        page_to_words = pdf_to_dict(pdf)
        chart = populate_chart(page_to_words)
        print(f"Age: {chart.age:.2f}")
        if chart.dob:
            print(f"Dob: {chart.dob.strftime('%d/%m/%Y')}")
        else:
            print("Dob: Not Available")
        print(f"has_valid_ekg: {chart.has_valid_ekg}")
        print(f"Name: {chart.name}")

if __name__ == "__main__":
    main()
