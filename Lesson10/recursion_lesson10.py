def add_one(num):
    if(num >= 9):
        return num + 1
    total = num + 1
    print(total)
    
    # Now the function calls itself
    #However this result can also be achieve with loop
    return add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)