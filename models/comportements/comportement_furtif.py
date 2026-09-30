from models.comportement import Comportement

class ComportementFurtif:

    def __init__(self):
        self._tour = 0
    
    def agir(self, ennemi):
        self._tour += 1

        if self._tour % 2 == 0:

            return "defend"

        return "attaque"


