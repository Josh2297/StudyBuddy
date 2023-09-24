import requests
import pdfplumber
import nltk
import unicodedata
import os
from dotenv import load_dotenv
load_dotenv()
nltk.download('punkt')


API_TOKEN = os.environ.get("SUMMARY_API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def handle_page(text):
    return text


class Summary:
    """ 
    Extract and summarize extracted text.
     
    parameters:
    ---------- 
    pdf_file_path: str
            Full path to pdf file, can be constructed from os.path
            
    pages: list, optional
            Number of pages to extract.
    """

    def __init__(self, pdf_file_path: str, pages: list = None) -> None:
        self.pdf_file_path = pdf_file_path
        if pages:
            self.pages = pages
        else:
            self.pages = []

    def text_extractor(self) -> list:
        """
        Extract text from pdf file.

        returns:
        --------
        list
        """
        with pdfplumber.open(self.pdf_file_path) as pdf:
            if self.pages:
                self.pages = [int(i) for i in self.pages]
                page_extract_list = [0] * len(self.pages)
                for p, i in enumerate(self.pages):
                    page = pdf.pages[i]
                    page_extract_list[p] = page.extract_text()
            else:
                self.pages = pdf.pages
                page_extract_list = [0] * len(self.pages)
                for i, page in enumerate(self.pages):
                    page_extract_list[i] = page.extract_text()

        page_extract_list = " ".join(page_extract_list)

        tokens = nltk.sent_tokenize(page_extract_list)

        new_set = []
        empty = []
        for i in range(len(tokens)):
            if (i + 1) % 6 == 0:
                new_set.append(str_empty)
                str_empty = ""
                empty = []
                empty.append(tokens[i])
            else:
                empty.append(tokens[i])
                str_empty = " ".join(empty)

        new_set.append(str_empty)

        return new_set

    def _query(self, payload):
        response = requests.post(
            os.environ.get("SUMMARY_API_URL"),
            headers=headers,
            json=payload)
        return response.json()

    def summarize(self) -> list:
        """
        Summarize extracted text.

        returns:
        --------
        list
        """
        text = self.text_extractor()
        new_tuple = []
        n = 0
        for i in text:
            n += 1
            output = self._query({"inputs": i})
            summary = output[0]['summary_text']
            new_tuple.append(unicodedata.normalize('NFKD', summary))

        return new_tuple
