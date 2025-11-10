# Nom i cognoms: Victor Girones De Asix
# Data: 06/11/2025
# Descripció:
# Crea un mòdul conversions.py amb funcions

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

print("0 °C =", celsius_a_fahrenheit(0), "°F")
print("100 °C =", celsius_a_fahrenheit(100), "°F")
print("32 °F =", fahrenheit_a_celsius(32), "°C")
print("212 °F =", fahrenheit_a_celsius(212), "°C")