# Codebase Chatbot Assistant 🤖

This project is a **Codebase Chatbot Assistant** designed to help developers and users interact with a codebase repository more effectively. Built with **Streamlit**, **Pinecone**, **LangChain** and **GROQ**, this chatbot leverages advanced embeddings and natural language processing to retrieve relevant documents and answer queries about the codebase.

---

## 🚀 Features
- **Natural Language Understanding:** Users can ask questions in plain English about the codebase.
- **Intelligent Document Retrieval:** Uses **Pinecone** and **HuggingFace Embeddings** to fetch relevant code snippets and documentation.
- **AI-Powered Conversations:** Provides accurate and user-friendly answers using Groq and llama models.
- **Interactive UI:** Built with Streamlit, enabling real-time conversations.

---

## 🛠️ Technologies Used
- **[Streamlit](https://streamlit.io/):** For building the chatbot interface.
- **[Pinecone](https://www.pinecone.io/):** For vector database management and retrieval.
- **[Groq](https://groq.com/):** For language processing and generating responses.
- **[SentenceTransformers](https://huggingface.co/sentence-transformers):** For embedding queries into vector space.

---

## 📂 Folder Structure
- ├── app.py # Main Streamlit application 
- ├── requirements.txt # Dependencies for the project
- ├── README.md # Project documentation
- ├── .gitignore
- ├── venv
- ├── .streamlit
-      ├── secrets.toml



---

## ⚙️ Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- [Pinecone account and API key](https://www.pinecone.io/start/)
- [GROQ account and API key](https://console.groq.com/keys)
- Streamlit Cloud (optional, for deployment)

### Steps
1. **Clone this repository:**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   
2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Add secrets: Create a .streamlit/secrets.toml file and include the following:**
   ```toml
   [secrets]
   PINECONE_API_KEY = "your-pinecone-api-key"
   GROQ_API_KEY = "your-openai-api-key"

5. **Run the application:**
   ```bash
   streamlit run app.py
   
7. **Access the app: Open the URL displayed in your terminal (usually http://localhost:8501).**

## 🧪 Example Usage
1. Open the chatbot UI.
2. Type a question about the codebase, such as:
-       "How does the authentication function work in the codebase?"
3. Receive intelligent responses, along with contextual snippets from the repository.

## 📦 Deployment on Streamlit Cloud
Push the repository to GitHub.
Go to Streamlit Cloud and connect your GitHub repository.
Set environment variables in the Streamlit Cloud dashboard for your API keys.
Deploy and share your chatbot with others!

## 🛡️ License
This project is licensed under the MIT License.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (feature/my-feature).
3. Commit your changes and open a pull request.

## 🙌 Acknowledgments
- Streamlit Community for providing a simple yet powerful platform for building data apps.
- Pinecone for seamless vector search.
- OpenAI for enabling advanced conversational capabilities.

## 📧 Contact
For any questions, feel free to reach out via:

Email: your-email@example.com
GitHub: your-username

## Enjoy coding! ✨

### Steps to Use:
1. Replace placeholders (`<your-username>`, `<repo-name>`, and API keys) with your actual details.
2. Update the **Contact** section with your preferred communication methods.
