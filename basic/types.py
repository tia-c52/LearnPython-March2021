a = 'Hello'
print("Repeating: \{0}\ {1} times: {2}". format(a, 4, a * 4))
print(a * 50)
print("Try the named index placeholder:")
print("Name: {name}, Age: {age}".format(age=100, name="Tia"))

b = "Hello\n\"World\"!"
#print(b + a)
c = """Hello
Line one "world"
line two
line 4
"""
#print("original: " + c)

#print("Title:" + c.title())
#print("Capitalize:" + c.capitalize())
#print("Upper cases:" + c.upper())
#print("lower case:" + c.lower())