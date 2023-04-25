def metre_to_yard(value):
	yard = 0.0
	return yard

def yard_to_metre(value):
	metre = 0.0
	return metre

def mille_to_kilometre(value):
	kilometre = 0.0
	return kilometre

def kilometre_to_mille(value):
	mille = 0.0
	return mille

def feet_to_metre(value):
	metre = 0.0
	return metre

def metre_to_feet(value):
	feet = 0.0
	return feet

def kilo_to_pound(value):
	pound = 0.0
	return pound

def pound_to_kilo(value):
	kilo = 0.0
	return  kilo

def ounce_to_gram(value):
	gram = 0.0
	return gram

def gram_to_ounce(value):
	ounce = 0.0
	return ounce

def celsius_to_fahrenheit(value):
	fahrenheit = 0.0
	return fahrenheit

def celsius_to_kelvin(value):
	kelvin = 0.0
	return kelvin

def fahrenheit_to_celsius(value):
	celsius = 0.0
	return celsius

def fahrenheit_to_kelvin(value):
	kelvin = 0.0
	return kelvin

def kelvin_to_celsius(value):
	celsius = 0.0
	return celsius

def kelvin_to_fahrenheit(value):
	fahrenheit = 0.0
	return fahrenheit

op = ""
one_value = "Ingrese un valor: "

if op == "metro a yarda":
    metre_value = int(input(one_value))
    metre_to_yard(metre_value)
elif op == "yarda a metro":
    yard_value = int(input(one_value))
    yard_to_metre(yard_value)
elif op == "km a milla":
    kilometre_value = int(input(one_value))
    kilometre_to_mille(kilometre_value)
elif op == "milla a km":
    mille_value = int(input(one_value))
    mille_to_kilometre(mille_value)
elif op == "metre":
    kilo_value = int(input(one_value))
elif op == "c a f":
    celsius_value = int(input(one_value))
    celsius_to_fahrenheit(celsius_value)
elif op == "f a c":
    fahrenheit_value = int(input(one_value))
    fahrenheit_to_celsius(fahrenheit_value)
elif op == "f a k":
    fahrenheit_value = int(input(one_value))
    fahrenheit_to_kelvin(fahrenheit_value)
elif op == "k a f":
    kelvin_value = int(input(one_value))
    kelvin_to_fahrenheit(kelvin_value)
elif op == "k a c":
    kelvin_value = int(input(one_value))
    kelvin_to_celsius(kelvin_value)
else:
    print("Opción no soportada")