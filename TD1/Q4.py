""" Q4 """
def nb_caracteres(texte:str)-> int:
    return len([c for c in list(texte) if c != " "])

def nb_lettres(texte:str)-> int:
    return len([c for c in list(texte.lower()) if 'a' <= c <= 'z'])

def nb_chiffres(texte:str)-> int:
    return len([c for c in list(texte.lower()) if '0' <= c < '9'])

texte_ = input("Entrez un texte :")

print(texte_)
print('Ce texte a',len(texte_),'caracteres avec les espaces')
print(f"Ce texte a {nb_caracteres(texte_)} caracteres")
print('Ce texte a',nb_lettres(texte_),'lettres')
print('Ce texte a',nb_chiffres(texte_),'chiffres')