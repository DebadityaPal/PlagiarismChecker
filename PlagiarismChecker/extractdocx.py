import docx

"""
This File opens a MS Word (.docx) file, fetches the text for
further processing.
"""


def extractDocx(docxfile):
    document = docx.Document(docxfile)

    # Fetch all the text out of the document
    # Make explicit unicode version
    unicode_text = []
    for para in document.paragraphs:
        unicode_text.append(para.text)

    # Print out text of document with two newlines under each paragraph
    return "\n".join(unicode_text)
