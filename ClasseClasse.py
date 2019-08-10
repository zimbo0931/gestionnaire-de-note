class Classe():
    def __init__(self, dico=None):
        self.nom = dico["nom"]
        self.listeEleve = []
        for e in dico["eleves"]:
            # creation instance etablissement
            elev = Eleve(e)
            self.listeEleve.append(elev)

    def rechercheNom