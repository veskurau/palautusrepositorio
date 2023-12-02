class KomentoLuokka:

    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

    def __init__(self, sovelluslogiikka, komento, arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._komento = komento
        self._arvo = arvo

    def suorita(self):
        if self._komento == KomentoLuokka.SUMMA:
            self._sovelluslogiikka.plus(self._arvo)
        elif self._komento == KomentoLuokka.EROTUS:
            self._sovelluslogiikka.miinus(self._arvo)
        elif self._komento == KomentoLuokka.NOLLAUS:
            self._sovelluslogiikka.nollaa()
        elif self._komento == KomentoLuokka.KUMOA:
            pass