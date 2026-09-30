from models.comportement import Comportement

class Ennemi:
    def __init__(self, nom: str, hp: int, hp_max: int, attaque, comportement) -> None:
        self.nom = nom
        self.hp = hp
        self.hp_max = hp_max
        self.attaque = attaque
        self._comportement = comportement
    
    def agir(self):
        return self._comportement.agir(self)

    def set_comportement(self, comportement: Comportement):
        self._comportement = comportement

    def get_comportement(self):
        return self._comportement
    
    def recevoir_degats(self, degats: int):
        self.hp = max(0, hp_max - degats)
    
    def est_vivant(self) -> Bool:
        return self.hp > 0
    
    def __str__(self) -> str:
        return f"{self.nom} (HP: {self.hp}/{self.hp_max})"





