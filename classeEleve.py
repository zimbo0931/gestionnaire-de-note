class Eleve():
    def __init__(self, dico=None):
        self.nom = dico["nom"]
        self.listeMatiere = []
        for e in dico["matiere"]:
            # creation instance etablissement
            mati = Matiere(e)
            self.listeMatiere.append(mati)