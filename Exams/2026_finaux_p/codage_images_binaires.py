import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

class Image_binaire:
    def __init__(self, image:np.ndarray):
        self.set_image(image)


    def set_image(self, image:np.ndarray):
        if not isinstance(image, np.ndarray):
            raise TypeError("Image must be an np.ndarray.")
        if image.ndim == 3:
            image = self.couleur_vers_niveau_de_gris(image)
        if image.ndim == 2:
            image = self.niveau_de_gris_vers_binaire(image)
        self._data = image


    def get_image(self):
        return self._data


    def couleur_vers_niveau_de_gris(self, image:np.ndarray) -> np.ndarray:
        return  (image[:,:,0]*0.299 + image[:,:,1]*0.587 + image[:,:,2]*0.114).astype(int)


    def niveau_de_gris_vers_binaire(self, image:np.ndarray) -> np.ndarray:
        return np.where(image >=128,255,0).astype(np.uint8)

    def est_divisible(self):
        ligne,colonne = self._data.shape
        return ligne > 1 and colonne > 1

    def est_unicolor(self):
        return len(np.unique(self._data)) == 1

    def diviser(self):
        nb_ligne, nb_colonne = self._data.shape
        return [self._data[0:nb_ligne//2,0:nb_colonne//2], self._data[0:nb_ligne//2,nb_colonne//2:],self._data[nb_ligne//2:,0:nb_colonne//2], self._data[nb_ligne//2:,nb_colonne//2:]]

    def affiche(self):
        plt.imshow(self.get_image())
        plt.show()

class NoeudBinaire(Image_binaire):
    nb_noeuds:int = 0

    def __init__(self,image:np.ndarray, profondeur=0):
        super().__init__(image)
        self._prof = profondeur
        NoeudBinaire.nb_noeuds +=1
        self._fils:list = []

        if not self.est_unicolor() and self.est_divisible():
            im1,im2,im3,im4 = self.diviser()
            self._fils.append(NoeudBinaire(im1))
            self._fils.append(NoeudBinaire(im2))
            self._fils.append(NoeudBinaire(im3))
            self._fils.append(NoeudBinaire(im4))
            NoeudBinaire.nb_noeuds +=4


    def max_prof(self):
        if len(self._fils) == 0:
            return 1
        return 1 + self._fils[0].max_prof()



def main():
    im = plt.imread("fleurs.jpg")

    im_binaire= Image_binaire(im)
    im_binaire.affiche()


    im1,im2,im3,im4 = im_binaire.diviser()

    fig, axes = plt.subplots(2,2,figsize=(5,5))
    axes[0,0].imshow(im1)
    axes[0, 0].axis('off')
    axes[0,1].imshow(im2)
    axes[0, 1].axis('off')
    axes[1,0].imshow(im3)
    axes[1, 0].axis('off')
    axes[1,1].imshow(im4)
    axes[1, 1].axis('off')

    plt.tight_layout()
    plt.show()


    plt.show()

    noeud_binaire = NoeudBinaire(im)

    print(f"Nb de noeuds : {NoeudBinaire.nb_noeuds}")
    print(f"Profondeur max : {noeud_binaire.max_prof()}")

if __name__ == "__main__":
    main()