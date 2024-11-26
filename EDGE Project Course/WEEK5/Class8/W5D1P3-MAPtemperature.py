

def CelsiusToFahrenheit(temperatures):
    
    fahern=list(map(lambda t : (9*t/5)+32,temperatures))
    return fahern

Celsius=[i*3 for i in range(1,10)]

print(CelsiusToFahrenheit(Celsius))