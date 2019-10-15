Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("\tCONVERSOR DE UNIDADES.")
print("1. Convertir Fahrenheit a 
Celsius.")
print("2. Convertir Celsius a Fahrenheit.")
print("3. 
Convertir Kelvin a Celsius.")
print("4. Salir.")

print()
opc = int
(input("Ingrese un opcion del menu: "))

print()

if opc==1:
    med1 = 
float(input("ingrese la medida de °F: ")) #(°F − 32) × 5/9 = °C
    
print("su medida es de "+str((med1-32)*5/9)+" °C")

elif opc==2:
    
med2 = float(input("ingrese la medida de °C: ")) #(°C × 9/5) + 32 
= °F
    print("su medida es de " + str((med2*9/5)+32)+" °F")
    
elif opc==3:
    med3 = float(input("ingrese la medida de °K: ")) 
#K − 273.15 = °C
    print("su medida es de " + str(med3-273.15)+" 
°C")
    
elif opc==4:
    print("Hasta pronto.")
    
else:
    print
("ingrese una opcion valida.")
