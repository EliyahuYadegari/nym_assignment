import pdfplumber
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class TextualWord:
    x0: float
    x1: float
    text: str

PagesToWords = Dict[int, List[TextualWord]]

def pdf_to_dict(pdfplumber_pdf: pdfplumber.PDF) -> PagesToWords:
    pages_words = {}
    
    for page_num, page in enumerate(pdfplumber_pdf.pages):
        words = []
        
        for word in page.extract_words():
            x0 = round(word['x0'], 3)
            x1 = round(word['x1'], 3)
            text = word['text']
            
            words.append(TextualWord(x0=x0, x1=x1, text=text))
        
        pages_words[page_num] = words
    
    return pages_words
