from deepeval.metrics import BaseMetric

# You are creating a custom evaluation metric that inherits from BaseMetric.
# Why inherit?
# Because DeepEval expects metrics to follow a specific structure:
# Must define measure()
# Must set self.score
# Must set self.passed
# By inheriting, you plug into the framework correctly.

class ToolUsageMetrics(BaseMetric):

    def measure(self,test_case):
        trace=test_case.metadata["trace"]
        spans=trace.get("spans",[])

        used_tools=[s["name"] for s in spans]

        if len(used_tools)>0:
            self.score=1.0
        else:
            self.score=0.0

        # >=0.5 this is a boolean comparision
        # It asks:
        # Is the score greater than or equal to 0.5?
        self.passed = self.score >=0.5
        return self.score

