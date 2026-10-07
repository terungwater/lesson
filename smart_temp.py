"""
Implement smart_temperature(value). Convert value to a Celsius number. 
If conversion fails, return Invalid temperature. 
Convert Celsius to Fahrenheit using the standard formula. 
Return a three-line report with labels Celsius, Fahrenheit, and Status. 
Status is freezing when Celsius is less than or equal to 0, cold when below 20, warm when from 20 through 30, and hot when above 30.
"""

def smart_temperature(value):
    celsius = 0
    try:
        celsius = float(value)
    except ValueError:
        return "Invalid temperature"
    fahrenheit = (celsius * 9/5) + 32
    if celsius <= 0:
        return f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: freezing"
    elif celsius < 20:
        return f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: code"
    elif celsius >=20 and celsius <=30:
        return f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: warm"
    elif celsius > 30:
        return f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: hot"
    else:
        return f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: hot"
print(smart_temperature(30))