""" Q4 """
def nb_caracteres(texte:str):
    return len([c for c in list(texte) if c != " "])

def nb_lettres(texte:str):
    return len([c for c in list(texte.lower()) if 97<= ord(c)<122])

def nb_chiffres(texte:str):
    return len([c for c in list(texte.lower()) if 48<= ord(c)<57])

texte = input("Entrez un texte :")

print(texte)
print('Ce texte a',len(texte),'caracteres avec les espaces')
print('Ce texte a',nb_caracteres(texte),'caracteres')
print('Ce texte a',nb_lettres(texte),'lettres')
print('Ce texte a',nb_chiffres(texte),'chiffres')