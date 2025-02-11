from datetime import date, datetime
import re
from dataclasses import dataclass

@dataclass
class Chart:
    name: str
    dob: date
    has_valid_ekg: bool
    
    @property
    def age(self) -> float:
        if self.dob is None:
            return 0.0
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

def populate_chart(page_to_words: dict) -> Chart:
    name = ""
    dob = None
    has_valid_ekg = False
    
    text = " ".join([word.text for word in page_to_words[0]])
    if "Patient Name" in text:
        name_start_index = text.index("Patient Name: ") + len("Patient Name: ")
        name_parts = text[name_start_index:].split("DOB")[0].split("EKG")[0].strip()
        name = name_parts

    dob_match = re.search(r'DOB:\s*(\d{2}/\d{2}/\d{4})', text)
    if dob_match:
        dob_str = dob_match.group(1)
        dob = datetime.strptime(dob_str, "%d/%m/%Y")
    else:
        print("DOB not found")
    
    if "no valid" in text.lower() or "not valid" in text.lower():
        has_valid_ekg = False
    elif "EKG" in text:
        has_valid_ekg = True
    
    return Chart(name=name.strip(), dob=dob, has_valid_ekg=has_valid_ekg)