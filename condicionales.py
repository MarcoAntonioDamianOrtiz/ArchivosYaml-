import os

name = os.getenv("NAME")
age = int(os.getenv("EDAD"))

print("Hello " + name)
print ("Tu edad es: " + str(age))

if age >= 18:
    print("Eres mayor de edad")
else:
    print("menor de edad")