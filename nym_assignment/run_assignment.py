import pdfplumber
from nym_assignment import pdf_to_dict, populate_chart, pdf_to_extra_dict

def main():

    with pdfplumber.open("samples/chart1.pdf") as pdf:
        # to run bonus 1:
        pdf_path = "samples/chart1.pdf"
        pages_to_extra_words = pdf_to_extra_dict(pdf_path)
        
        for page_num, words in pages_to_extra_words.items():
            print(f"Page {page_num + 1}:")
            for word in words:
                print(f"Text: {word.text}, Font: {word.fontname}, Size: {word.size}, Is Bold: {word.is_bold}")

        
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
