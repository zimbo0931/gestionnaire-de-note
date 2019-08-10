class etablissement():
    def __init__(self, dico=None):
        self.nom = dico["nom"]
        self.ListeClasse = []
        for e in dico["classes"]:
            # creation instance etablissement
            clas = Classe(e)
            self.listeClasse.append(clas)