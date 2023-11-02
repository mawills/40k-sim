class WoundRollResult:
    wounds = 0
    devastating_wounds = 0

    def __init__(self, wounds: int = 0, devastating_wounds: int = 0):
        self.wounds = wounds
        self.devastating_wounds = devastating_wounds

    def add_wounds(self, n: int):
        self.wounds += n

    def add_devastating_wounds(self, n: int):
        self.devastating_wounds += n
