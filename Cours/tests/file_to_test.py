from random import uniform


# Test introduction:

def add(a,b):
    return a+b


def divide(a,b):
    return a/b

def add_integer(a,b):
    if isinstance(a,int) and isinstance(b,int):    
        return a+b
    else:
        raise(TypeError("Parameters should be integers"))

def alea_uniform(a,b):
    return uniform(a,b)

# Adavance test:

def input_function():
    return input("Que voulez vous renvoyer?")

def create_file(file_path,content):
    with open(file_path, "w") as fichier:
        fichier.write(content)

def print_hello():
    print("hello")


def several_input_function():
    count = 1
    my_input = input("Qu'avez-vous à déclarer?")
    while my_input != "Rien Monsieur":
        my_input = input("Qu'avez-vous à déclarer?")
        count+=1
    return count
    
def randomize():
    return uniform(0,1)

