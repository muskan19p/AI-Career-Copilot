from pypdf import PdfReader
from docx import Document
import tempfile


def extract_text(file):

    filename = file.filename.lower()

    if filename.endswith(".pdf"):

        with tempfile.NamedTemporaryFile(delete=False) as temp:

            temp.write(file.file.read())

            reader = PdfReader(temp.name)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            return text

    elif filename.endswith(".docx"):

        with tempfile.NamedTemporaryFile(delete=False) as temp:

            temp.write(file.file.read())

            document = Document(temp.name)

            text = "\n".join(
                para.text for para in document.paragraphs
            )

            return text

    return ""