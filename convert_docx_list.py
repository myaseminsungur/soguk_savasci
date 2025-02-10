from docx import Document

def convert_doc_to_list(doc_path):
    """
    Extracts question-answer pairs from a correctly formatted Word document.

    Args:
        doc_path (str): Path to the Word document.

    Returns:
        list: A list of strings in the format "question: answer".
    """
    document = Document(doc_path)
    qa_list = []
    
    # Iterate through paragraphs in steps of 2 (Q: and A: pairs)
    paragraphs = document.paragraphs
    for i in range(0, len(paragraphs), 2):
        question = paragraphs[i].text[2:].strip()  # Remove "Q:" and strip whitespace
        answer = paragraphs[i + 1].text[2:].strip()  # Remove "A:" and strip whitespace
        qa_list.append(f"{question}: {answer}")
    
    return qa_list 


# Example usage
qa_list = convert_doc_to_list("data/soguk_savas_soruları.docx")

# save as JSON
import json
with open('data/qa_list.json', 'w', encoding='utf-8') as f:
    json.dump(qa_list, f, ensure_ascii=False, indent=2)

# Print the list
print(qa_list[:2])