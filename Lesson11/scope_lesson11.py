name = "Sadiq"
count = 1

def anotherfun():
    color = "blue"
    global count 
    count += 2
    print(count)
    def greeting(name):
        nonlocal color
        color = "Red"
        print(color)
        print(name)
        
    greeting("Sadiq")
    
anotherfun()
