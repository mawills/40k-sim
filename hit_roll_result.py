class HitRollResult:
    hits = 0
    lethal_hits = 0

    def __init__(self, hits: int = 0, lethal_hits: int = 0):
        self.hits = hits
        self.lethal_hits = lethal_hits

    def add_hits(self, n: int):
        self.hits += n

    def add_lethal_hits(self, n: int):
        self.lethal_hits += n
