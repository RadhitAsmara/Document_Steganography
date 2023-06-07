import docx


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    paragraph = doc.paragraphs[-1]
    hidden_text = paragraph.text
    return hidden_text


extracted_text = extract_text_from_docx("modified.docx")
print(f"Extracted hidden text: {extracted_text}")
