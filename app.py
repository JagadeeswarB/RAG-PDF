import faiss
from sentence_transformers import SentenceTransformer
import PyPDF2
import gradio as gr

# Step 1: Extract Knowledge Base from PDF
def extract_text_from_pdf(pdf_path):
    """
    Extract and clean text from a PDF file.
    """
    knowledge = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                # Replace newlines with spaces for better readability
                text = text.replace("\n", " ")
                # Split the text into meaningful sentences
                knowledge.extend(text.split(". "))
    # Clean up each sentence and remove empty strings
    return [sentence.strip() for sentence in knowledge if sentence.strip()]

# Step 2: Create the Retriever
embedder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')  # Embedding model for document similarity

index = None  # Global variable to store FAISS index
knowledge_base = []  # Global variable to store the knowledge base

def upload_and_query(pdf_file, query):
    """
    Handle PDF upload and process queries.
    """
    global index, knowledge_base

    if not pdf_file:
        return "Please upload a valid PDF file."

    # Process the uploaded PDF
    if not knowledge_base:  # Only process if the knowledge base is empty
        knowledge_base = extract_text_from_pdf(pdf_file)
        if not knowledge_base:
            return "The uploaded PDF does not contain any readable text."

        document_embeddings = embedder.encode(knowledge_base)
        dimension = document_embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)
        index.add(document_embeddings)

        return "PDF uploaded successfully. Now ask your query."

    # Handle queries
    if not query:
        return "Please enter a query after uploading a PDF."

    if index is None or not knowledge_base:
        return "Please upload a PDF document before asking a query."

    # Generate query embeddings and perform retrieval
    query_embedding = embedder.encode([query])
    distances, indices = index.search(query_embedding, 5)  # Retrieve top 5 results
    retrieved_docs = [knowledge_base[idx] for idx in indices[0]]

    # Clean up and format the retrieved context
    context = " ".join(retrieved_docs).replace("\n", " ").strip()
    return context

# Step 3: Create Gradio Interface
interface = gr.Interface(
    fn=upload_and_query,
    inputs=[
        gr.File(label="Upload a PDF document", type="filepath"),
        gr.Textbox(label="Enter your query"),
    ],
    outputs="text",
    title="PDF Knowledge Base Query",
    description="Upload a PDF document and ask questions based on its content."
)

# Launch the Interface
if __name__ == "__main__":
    interface.launch()
