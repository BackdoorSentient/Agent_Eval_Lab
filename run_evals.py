from agent.agent import Agent
from evals.dataset import DATASET
from deepeval.test_case import LLMTestCase
from deepeval import evaluate

from evals.metrics.tool_usage import ToolUsageMetrics
from evals.metrics.tool_argument_accuracy import ToolArgumentAccuracy
from evals.metrics.reasoning_quality import reasoning_metric
from evals.metrics.task_success import task_sucess_metric

def run():
    agent=Agent()
    test_cases=[]
    

    for item in DATASET:
        output=agent.run(item["input"])

        test_case=LLMTestCase(
        input=item["input"],
        actual_output=output,
        expected_output=item["expected_output"],
        metadata={}
        )
        test_cases.append(test_case)
    
    evaluate(
        test_cases=test_cases,
        metrics=[
            ToolUsageMetrics(),
            ToolArgumentAccuracy(),
            reasoning_metric(),
            task_sucess_metric()

        ]
    )

if __name__=="__main__":
    run()
