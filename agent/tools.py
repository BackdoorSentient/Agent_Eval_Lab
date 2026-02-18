import math

def claculator(expression:str):
    try:
        result=eval(expression,{"__builtins__":None},{"math":math})
        return str(result)
    except Exception as e:
        return f"Error:{str(e)}"
    
def unit_converter(value:float, from_unit:str, to_unit: str):
    conversions={
        ("km","m"):lambda x:x * 1000,
        ("m","km"):lambda x:x / 1000,
        ("c","f"):lambda x: (x*9/5) + 32,
        ("f","c"): lambda x : (x -32) * 5/9,
    }

    key=(from_unit.lower(),to_unit.lower())

    if key in conversions:
        return str(conversions[key](value))

    return "Conversion not supported"
