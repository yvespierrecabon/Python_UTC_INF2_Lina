import os
import PIL.Image as img
from openpyxl.chart import series_factory


class Note:
    nb_notes = 0
    def __init__(self, titre:str):
        self._titre = titre
        Note.nb_notes += 1

    def __del__(self):
        Note.nb_notes -= 1


    def get_titre(self)->str:
        return self._titre

    def set_titre(self, titre):
        self._titre = titre

    def __str__(self):
        return self._titre


class Article(Note):
    def __init__(self, titre:str, texte:str):
        super().__init__(titre)
        self._texte = texte

    def get_texte(self)->str:
        return self._texte

    def set_texte(self, texte):
        self._texte = texte

    def __str__(self):
        return f"{self._titre} : {self._texte}"

class Image(Note):
    def __init__(self, titre:str, description:str, url:str):
        super().__init__(titre)
        self._description = description
        self._url = url

    def get_description(self)->str:
        return self._description

    def set_description(self, description):
        self._description = description


    def __str__(self)->str:
        return f"{self._titre} : {self._description}"

    def get_url(self)->str:
        return self._url


    def set_url(self, url):
        if os.path.isfile(url):
            self._url = url

    def print(self):
        print( f"{self._titre} : {self._description}")
        image = img.open(str(self._url))
        img._show(image)



class Document(Note):
    def __init__(self, titre:str):
        super().__init__(titre)
        self._liste = []

    def ajouter(self, note:Note)->None:
        self._liste.append(note)

    def supprimer_note(self, note:Note)->None:
        self._liste.remove(note)

    def print(self):
        print( f"{self._titre}")
        for note in self._liste:
            print(note)


###########################################

image1 = Image("image1", "une image",'/home/yves/Documents/Images/20230416_001.jpg')
image1.print()
note1 = Note("note1")
article_1 = Article("article_1", "texte de l'article1")
article_2 = Article("article_2", "texte de l'article2")

document_1 = Document("document_1")
document_1.ajouter(note1)
document_1.ajouter(article_1)
document_1.ajouter(image1)
document_1.ajouter(article_2)
document_1.print()
print(f"Nombre de notes : {Note.nb_notes}")

