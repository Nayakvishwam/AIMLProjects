from langchain_ollama import ChatOllama
import traceback

try:
    llm = ChatOllama(model="llama3")

    print("Model loaded")

    response = llm.invoke(
        "What is PostgreSQL?"
    )

    print("Response:")
    print(response.content)

except Exception as e:
    traceback.print_exc()