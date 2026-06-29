#In built functions
#Function -> Repeat a task - You can use a function
#print(), input(), type(), format(), max(), min(), id(), sum(), avg()

name= "aaysha"
print(name)
print(type(name))
print(id(name)) #id -> memory address where it is stored
print(len(name)) # lenght of string start with 1
name = name.upper()
print(name)
name = name.lower()
print(name)
name = name.casefold()
print(name)
a=name.count('a')
#print(a)
#print(name[6]) # IndexError: string index out of range
#Immutable - that can't be changed
name[0]= "X"  # TypeError: 'str' object does not support item assignment
print(name)