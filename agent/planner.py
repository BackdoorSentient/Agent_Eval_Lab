import json
import ollama
from tenacity import retry,stop_after_attempt,wait_exponential

MODEL_NAME="llama3"

SYSTEM_PROMPT = """
You are a reasoning agent with access to tools.

Available tools:
1. calculator(expression: str)
2. unit_converter(value: float, from_unit: str, to_unit: str)

You must respond ONLY with valid JSON.

Format:

{
  "action": "tool" | "final",
  "tool_name": "...",
  "tool_input": {...},
  "final_answer": "..."
}
"""

@retry(stop=stop_after_attempt(3),wait=wait_exponential())
def plan(user_input:str, scratchpad:str):
    response=ollama.chat(
        model=MODEL_NAME,
        host="http://host.docker.internal:11434",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":f"Questions: {user_input}\nScratchpad: {scratchpad}"
            }
        ],
        options={"temperature":0}
    )
    content=response["message"]["content"]
    content=content.replace("```json","").replace("```","").strip()
    try:
        return json.loads(content)
    except:
        start=content.find("{")
        end=content.rfind("}")+1
        return json.loads(content[start:end])