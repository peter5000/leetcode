from string import Template

age = 10
name = "Peter"

print("Hi my name is %s and I am %s years old" % (name, age))
print(f"Hi my name is {name} and I am {age} years old")
print("Hi my name is {name} and I am {age} years old".format(name = name, age = age))
print("Hi my name is {} and I am {} years old".format(name, age))
print("Hi my name is {1} and I am {0} years old".format(name, age))
print(Template("Hi my name is $name and I am $age years old").substitute(name=name,age=age))