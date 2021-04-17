def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error, because "Bob" is not a dictionary
myfunction(**None)   # Error