from agent.planner import plan
from tracing.langfuse_config import get_langfuse_trace

class Agent:
    def __init__(self):
        pass

    def run(self,question:str):
        trace=get_langfuse_trace(question)

        scrathpad=""
        steps=[]

        while True:
            plan(question,)
        return 