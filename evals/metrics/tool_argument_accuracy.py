from deepeval.metrics import BaseMetric

class ToolArgumentAccuracy(BaseMetric):

    def measure(self,test_case):
        trace=test_case.metadata["trace"]
        spans=trace.get("spans",[])

        if not spans:
            self.score=0
        else:
            self.score=1

        self.passed=self.score>=0.5
        return self.score