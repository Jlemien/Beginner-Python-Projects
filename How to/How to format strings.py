"""
sub1 = "python string!"
sub2 = "an arg"

a = "i am a %s" % sub1
b = "i am a {0}".format(sub1)

c = "with %(kwarg)s!" % {'kwarg':sub2}
d = "with {kwarg}!".format(kwarg=sub2)

print(a)    # "i am a python string!"
print(b)   # "i am a python string!"
print(c)   # "with an arg!"
print(d)   # "with an arg!"
"""



print("This is our %s" % "string")
print("Is this a tuple with %s %s" % ("Python", "3"))
print("This is a dictionary. It will use the key such as lang to find the value, then print the value. We are learning %(lang)s %(ver)s" % {"lang": "Python", "ver": "3"})