# Casting in python is therefore done using constructor functions
# Integers
x = int(1)  # x will be 1
score = int(2.8) # score will be 2
character = int("3") # character will be 3
print(score)

#Floats
number = float(1)  # number will be 1.0
decimalNumber = float("3")   # decimalNumber will be 3.0
age = float("4.2") # age will be 4.2
print(age)

#Strings
word = str("s1") # word will be 's1'
number1 = str(2)    # number1 will be '2'
decimalNumber1 = str(3.0)  # decimalNumber1 will be '3.0'
print(decimalNumber1)

#Multiline Strings
text = """Python es un lenguaje de alto nivel de programación
 interpretado cuya filosofía hace hincapié en la 
 legibilidad de su código."""
print(text)

#String Length
message = "Hello, World!"
print(len(message))

#Substrings
string = "Python Fundamentals"
print(string[0:6]) # Obtener los primeros n caracteres de una cadena

string1 = "Multi Paradigm!"
print(string1[2:7]) # Obtener los caracteres de en medio de una cadena

string2 = "Guido Van Rossum"
print(string2[-6:]) # Obtener los últimos n caracteres de una cadena

#Upper Case
string3 = "FSF Award for the Advancement of Free Software"
print(string3.upper())

#Lower Case
string4 = "FSF Award for the Advancement of Free Software"
print(string4.lower())

#Remove Whitespace strip()
name = " Luis Vejarano "
print(name.strip()) # returns "Luis Vejarano"

#Replace String
text1 = "github"
print(text1.replace("g", "G")) # replaces a string with another string

#Split String
text2 = "Popayán, Timbio"
#returns a list where the text between the specified separator becomes the list items
print(text2.split(",")) # returns ['Popayán', ' Timbio']

#F-Strings
age = 36
city = "Popayán"
text3 = f"Mi nombre es Luis Vejarano, tengo {age} años y vivo en {city}"
print(text3)