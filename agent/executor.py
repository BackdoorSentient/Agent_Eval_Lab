from agent.tools import claculator,unit_converter

TOOLS={
    "calculator":claculator,
    "unit_converter":unit_converter
}

def execute_tool(tool_name:str,tool_input:str):
    if tool_name not in TOOLS:
        return "Tool not found"

    return TOOLS[tool_name](**tool_input)