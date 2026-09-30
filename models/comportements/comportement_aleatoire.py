from models.comportement import Comportement
import random 

class ComportementAleatoire:

    def agir(self, ennemi) -> str:
        return random.choice[("defend", "attaque")]
