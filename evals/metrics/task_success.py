from deepeval.metrics import AnswerRelevancyMetric
from deepeval.models import OllamaModel

def task_sucess_metric():
    model=OllamaModel(model="llama3")

    return AnswerRelevancyMetric(
        model=model,
        threshold=0.7
    )