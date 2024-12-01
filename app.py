import streamlit as st
import os
from openai import OpenAI
from pinecone import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer





# Initialize pinecone
pinecone_api_key = st.secrets["PINECONE_API_KEY"]
pc = Pinecone(api_key=pinecone_api_key)
# Connect to pinecone database
pinecone_index = pc.Index("codebase-rag")

# Load the 


# Create openai client via GROQ
client = OpenAI(
    base_url = "https://api.groq.com/openai/v1",
    api_key = st.secrets["GROQ_API_KEY"]
)

# Load model globally
embedding_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")




# Create huggingface embeddings
def get_huggingface_embeddings(text):
    return embedding_model.encode(text)

# Retrieve relevant documents from Pinecone
def retrieve_relevant_docs(query):
        # create embeddings based on user query
        query_embedding = get_huggingface_embeddings(query)

        # query pinecone index
        top_matches = pinecone_index.query(vector=query_embedding.tolist(), top_k=5, include_metadata=True, namespace="https://github.com/CoderAgent/SecureAgent")

        if not top_matches["matches"]:
                return "No relevant documents found."

        # Get the list of retrieved text and decode the text with better formatting
        contexts = [item["metadata"]["text"] for item in top_matches["matches"]]
        augmented_query = "<CONTEXT>\n" + "\n\n-------\n\n".join(contexts[ : 10]) + "\n-------\n</CONTEXT>\n\n\n\nMY QUESTION:\n" + query

        return augmented_query



# Streamlit UI
all_messages = []
def chatbot():
        st.title("Codebase chatbot")
        st.subheader("This is a chatbot that can help you with your codebase questions")

        st.warning ("Codebase used for this project: https://github.com/CoderAgent/SecureAgent")
        # Initialize chat history in session state
        if "messages" not in st.session_state:
                st.session_state.messages = [
                       {"role": "system", "content": "You are a software engineer with 20 years of experience"},
                       {"role": "assistant", "content": "Hi! I'm the codebase chatbot assitant. How can I help you today?"}
                       ]  

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
               # chat message for the role: user, etc
               if message["role"] != "system":
                      with st.chat_message(message["role"]):
                              st.markdown(message["content"])
     
        # Chat input     
        user_input = st.chat_input("Ask anything about the codebase")

        if user_input:
                # Display user message in chat
                with st.chat_message("user"):
                        st.markdown(user_input)

                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": user_input})

                augmented_user_input = retrieve_relevant_docs(user_input)
                all_messages.append(augmented_user_input)

                # Display assistant message in chat
                with st.chat_message("assistant"):
                        chat = client.chat.completions.create(
                               model="llama-3.1-8b-instant",
                               messages=[
                                       {"role": "system", "content": "You are a software engineer with 20 years of experience"},
                                       {"role": "user", "content": all_messages[-1]}
                                ],                                   
                        )
                        response = chat.choices[0].message.content
                        st.markdown(response)
                
                # Add chatbot response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
                       


                # In case, want to create stream, so give a better user experience
                
                # # Display assistant message in chat
                # with st.chat_message("assistant"):
                #         stream = client.chat.completions.create(
                #                 model="llama-3.1-8b-instant",
                #                 messages=[
                #                         {"role": message["role"], "content": message["content"]}
                #                 ],
                #                 stream = True,
                #         )
                #         response = st.write_stream(stream)

                # Add chatbot response to chat history

                # st.session_state.messages.append({"role": "assistant", "content": response})


        



if __name__ == "__main__":
    chatbot()