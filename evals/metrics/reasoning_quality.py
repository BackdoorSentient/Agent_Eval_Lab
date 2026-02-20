from deepeval.metrics import GEval
from deepeval.models import OllamaModel

def reasoning_metric():
    model=OllamaModel(model="llama3")

    return GEval(
        name="Reasoning Quality",
        criteria="""
        Was the reasoning logical?
        Were tools used appropriately?
        Was the final answer justified?
        """,
        model=model,
        threshold=0.7
    )