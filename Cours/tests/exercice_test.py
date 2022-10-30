import random as rd

##### Ecrire les tests pour les fonctions suivantes:


def multiply_by_42_then_pow(x,y):
    return (42 * x)**y


# Tester le cas de la division par 0 et le cas ou la liste n'est pas une liste numérique
def min_divide(ma_liste,y):
    return y/ min(ma_liste)

def pick_a_letter(word):
    return word[rd.randint(0,len(word)-1)]

def create_file(file_path,content):
    with open(file_path, "w") as fichier:
        fichier.write(content)

