import os
# from langfuse import Langfuse
from dotenv import load_dotenv
from langfuse import get_client

load_dotenv()

# langfuse=Langfuse(
#     public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
#     secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
#     host=os.getenv("LANGFUSE_HOST")

# )

# def get_langfuse_trace(user_input:str):
#     return langfuse.trace(
#         name="agent-run",
#         input=user_input
#     )
langfuse = get_client(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST", "http://localhost:3000")
)

def get_langfuse_trace(user_input: str):
    return langfuse.start_trace(
        name="agent-run",
        input=user_input
    )