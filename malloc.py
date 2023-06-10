"""
def malloc():

    val = ""

    current_val = input("Current Name/Value? ")
    val = current_val
    print("The current value of your variable is: ", val)
    
    new_val = input("New Value? ")

    val = new_val
    print(val)

malloc()    
"""

# useless library i made lol

def malloc(variable_name, new_value):
    globals()[variable_name] = new_value
    print("The current value of your variable", variable_name, "is:", globals()[variable_name])

# Example usage
malloc("my_variable", 42)

# i accidentally found out what 8j is lol
# balls = 7 + 8j
# print(balls)     prints: (7+8j)  
