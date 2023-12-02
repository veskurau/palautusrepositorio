class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._arvo_historia = [0]

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._arvo_historia.append(self._arvo)

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._arvo_historia.append(self._arvo)

    def nollaa(self):
        self._arvo = 0
        self._arvo_historia.append(self._arvo)

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        self._arvo = self._arvo_historia.pop()
