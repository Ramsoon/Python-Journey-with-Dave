from random import choice
capital = "Ikeja"
bird = "Owl"
flower = "Sunflower"
song = "Home of Commerce"

def randomfunfact():
    funfact = [
        "Lagos is considered flat, but it does not have a mountain",
        "Ikeja is the lagest city in the state",
        "A considerable porrtion of Lagos City is actually a sea",
        "Most Lagosians are annoyed by the daily traffic on the road."
    ]
    
    index = choice("0123")
    print(funfact[int(index)])
    
if  __name__ == "__main__":
    randomfunfact()