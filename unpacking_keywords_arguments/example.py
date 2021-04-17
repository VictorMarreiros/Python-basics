def named(**kwargs):  # receive data unpackage to print one-by-one
    print(kwargs)

def print_nicely(**kwargs): # receive
    named(**kwargs) # unpacking
    for arg, value in kwargs.items(): # pick arg="value" from each item in kwargs  --> kwargs.items()
        print(f"{arg}: {value}")


details = {"name": "John", "age": 20, "school": "Computing"}
print_nicely(**details)     # unpacking