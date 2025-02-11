# Bonus 1

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
from dataclasses import dataclass
import re

@dataclass
class ExtraTextualWord:
    text: str
    fontname: str
    size: float
    is_bold: bool

def pdf_to_extra_dict(pdf_path: str) -> dict:
    pages_to_extra_words = {}

    for page_num, page_layout in enumerate(extract_pages(pdf_path)):
        page_words = []
        
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    current_word = ""
                    fontname = None
                    size = None
                    is_bold = False
                    
                    for character in text_line:
                        if isinstance(character, LTChar):
                            if re.match(r'\s', character.get_text()):
                                if current_word: 
                                    page_words.append(ExtraTextualWord(current_word, fontname, size, is_bold))
                                    current_word = ""
                                
                            else:
                                current_word += character.get_text()
                                if fontname is None:
                                    fontname = character.fontname
                                    size = character.size
                                    is_bold = 'Bold' in fontname

                    if current_word:
                        page_words.append(ExtraTextualWord(current_word, fontname, size, is_bold))
        
        pages_to_extra_words[page_num + 1] = page_words
    
    return pages_to_extra_words
