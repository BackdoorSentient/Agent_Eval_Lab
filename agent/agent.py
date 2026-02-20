from agent.planner import plan
from tracing.langfuse_config import get_langfuse_trace
from agent.executor import execute_tool

class Agent:
    def __init__(self):
        pass

    def run(self,question:str):
        trace=get_langfuse_trace(question)

        scrathpad=""
        steps=[]

        while True:
            plan_output=plan(question,scrathpad)

            # if plan_output["action"]=="final":
            #     trace.update(output=plan_output["final_answer"])
            #     trace.end()
            #     return plan_output["final_answer"]
            if plan_output["action"] == "final":
                trace.end(output=plan_output["final_answer"])
                return plan_output["final_answer"]
            
            if plan_output["action"]=="tool":
                tool_name=plan_output["tool_name"]
                tool_input=plan_output["tool_input"]

                # span=trace.span(
                span = trace.start_span(
                    name=tool_name,
                    input=tool_input
                )

                result=execute_tool(tool_name,tool_input)

                # span.append({
                #     "tool":tool_name,
                #     "input":tool_input,
                #     "output":result
                # })
                span.end(output=result)

                scratchpad += f"\nTool {tool_name} returned: {result}"
