example = "hello world" # global

def local_ex():
    example = "this is a string" # local
    return example
    
print(example)
print(local_ex())

# In local reassigning global variable form local
def local_ex2():
    global fruit
    fruit = "pear"
    print(fruit)

fruit = "apple"
local_ex2()
print(fruit)

