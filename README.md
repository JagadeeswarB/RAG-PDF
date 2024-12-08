# 📚 PDF Knowledge Base Query App

Welcome to the **PDF Knowledge Base Query App**! This application allows you to upload a PDF document, extract its content, and ask questions based on the extracted knowledge using a Retrieval-Augmented Generation (RAG) pipeline. 🚀

---

## 💡 Features
- **Upload PDF**: Upload any PDF document containing text.
- **Question Answering**: Ask questions based on the uploaded PDF's content.
- **Dynamic Retrieval**: Uses FAISS and SentenceTransformers to efficiently retrieve relevant sections from the document.

---

## 🛠️ How It Works
1. **Upload**: Select a PDF file using the upload button.
2. **Process**: The app extracts text from the PDF and builds an index for querying.
3. **Ask**: Enter your question, and the app will return the most relevant information from the PDF.

---

## 🚀 Usage
1. Click on **Upload a PDF document** and select a file from your computer.
2. Wait for the app to process the document. You will see a message: *"PDF uploaded successfully. Now you can ask your query."*
3. Enter your question in the query box and hit enter.
4. Get your response instantly based on the document content.

---

## 🖥️ Technologies Used
- **[Gradio](https://gradio.app/)**: For creating the interactive web interface.
- **[FAISS](https://github.com/facebookresearch/faiss)**: For efficient similarity search and clustering.
- **[SentenceTransformers](https://www.sbert.net/)**: For embedding sentences into vector space.
- **[PyPDF2](https://pypdf2.readthedocs.io/)**: For reading and extracting text from PDF files.

---

## 📋 Example
### Query:
> What is active listening?

### Response:
> Active listening is an essential skill counselors can exploit to develop a positive and healthy interaction with a client. "Active listening intentionally focuses on who you are listening to, whether in a group or one-on-one, in order to understand what he or she is saying." Key aspects of listening: 1. Receiving 2. Understanding 3. Evaluating 4. Remembering 5. Responding. Active and empathetic listening is important in all communication.

---

## ⚙️ Setup for Local Development
To run the app locally:
1. Clone the repository:
   ```bash
   https://github.com/JagadeeswarB/RAG-PDF
   cd RAG-PDF
