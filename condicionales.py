import os

name = os.getenv("NAME")
age = int(os.getenv("EDAD"))

print("Hello " + name)

if age >= 18:
    print("Eres mayor de edad")
else:
    print("menor de edad")