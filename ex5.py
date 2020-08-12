name = 'Zed A. Shaw'
one_inches_into_centimetres = 2.54
one_pound_into_kilogram =  0.45
zeds_inches_into_centimetres = 180 * 2.54 
age = 35  
height = 74 * one_inches_into_centimetres
weight = 180 * one_pound_into_kilogram
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print (f"Let's talk about {name}.")
print (f"He's {height} inches tall.")
print (f"He's {weight} pounds heavy.")
print ("Actually that's not too heavy.")
print (f"He's got {eyes} eyes and {hair} hair.")
print (f"His teeth are usually {teeth} depending on coffee.")

# this line is tricky, try to get is exactly right

total = age + height + weight
print (f" If I add {age}, {height}, and {weight} I get {total}.")