import re
def metre_to_yard(value):
	yard = round(value * 1.0936, 2)
	print(f"{value} metro/s ----> {yard} yarda/s")

def yard_to_metre(value):
	metre = round(value / 1.0936, 2) 
	print(f"{value} yarda/s ----> {metre} metro/s")

def mille_to_kilometre(value):
	kilometre = round(value * 1.60934, 2) 
	print(f"{value} milla/s ----> {kilometre} kilómetro/s")

def kilometre_to_mille(value):
	mille = round(value / 1.60934, 2)
	print(f"{value} kilómetro/s ----> {mille} milla/s")

def feet_to_metre(value):
	metre = round(value * 3.28084, 2)
	print(f"{value} pie/s ----> {metre} metro/s")

def metre_to_feet(value):
	feet = round(value / 3.28084, 2)
	print(f"{value} metro/s ----> {feet} pie/s")

def kilo_to_pound(value):
	pound = round(value * 2.20462, 2)
	print(f"{value} kilogramo/s ----> {pound} libra/s")

def pound_to_kilo(value):
	kilo = round(value / 2.20462, 2)
	print(f"{value} libra/s ----> {kilo} kilogramo/s")

def ounce_to_gram(value):
	gram = round(value * 28.3495, 2)
	print(f"{value} onza/s ----> {gram} gramo/s")

def gram_to_ounce(value):
	ounce = round(value / 28.3495, 2)
	print(f"{value} gramo/s ----> {ounce} onza/s")

def celsius_to_fahrenheit(value):
	fahrenheit = round((value * 9/5) + 32, 2)
	print(f"{value} °C ----> {fahrenheit} °F")

def celsius_to_kelvin(value):
	kelvin = round(value + 273.15, 2)
	print(f"{value} °C ----> {kelvin} °K")

def fahrenheit_to_celsius(value):
	celsius = round((value - 32) * 5/9, 2)
	print(f"{value} °F ----> {celsius} °C")

def fahrenheit_to_kelvin(value):
	kelvin = round((value -32) * 5/9 + 273.15, 2)
	print(f"{value} °F ----> {kelvin} °K")

def kelvin_to_celsius(value):
	celsius = round(value - 273.15, 2)
	print(f"{value} °K ----> {celsius} °C")

def kelvin_to_fahrenheit(value):
	fahrenheit = round((value - 273.15) * 9/5 + 32, 2)
	print(f"{value} °K ----> {fahrenheit} °F")
 
one_value = int(input("Ingresa un valor: "))

print("\nCONVERSOR DE MEDIDAS (LONGITUD)")
metre_to_yard(one_value)
yard_to_metre(one_value)
kilometre_to_mille(one_value)
mille_to_kilometre(one_value)
metre_to_feet(one_value)
feet_to_metre(one_value)

print("\nCONVERSOR DE MEDIDAS (MASA)")
kilo_to_pound(one_value)
pound_to_kilo(one_value)
ounce_to_gram(one_value)
gram_to_ounce(one_value)

print("\nCONVERSOR DE MEDIDAS (TEMPERATURA)")
celsius_to_fahrenheit(one_value)
celsius_to_kelvin(one_value)
fahrenheit_to_celsius(one_value)
fahrenheit_to_kelvin(one_value)
kelvin_to_fahrenheit(one_value)
kelvin_to_celsius(one_value)