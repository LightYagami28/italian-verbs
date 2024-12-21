#!/usr/bin/python

import random


class Verbo:
    def __init__(self, nome, ausiliare, presente, participio, imperfetto, futuro):
        self.nome = nome
        self.ausiliare = ausiliare
        self.presente = presente
        self.participio = participio
        self.imperfetto = imperfetto
        self.futuro = futuro

        self.tempi = [
            ("presente", self.presente, presente == "[regolare]"),
            ("passato prossimo", self.passato_prossimo, participio == "[regolare]"),
            ("imperfetto", self.imperfetto, imperfetto == "[regolare]"),
            ("trapassato prossimo", self.trapassato_prossimo, participio == "[regolare]"),
            ("futuro", self.futuro, futuro == "[regolare]"),
            ("condizionale presente", self.condizionale_presente, futuro == "[regolare]"),
            ("condizionale passato", self.condizionale_passato, participio == "[regolare]")
        ]

    def il_participio(self):
        if self.participio == "[regolare]":
            prefisso = self.nome[:-3]
            suffisso = self.nome[-3:]

            if suffisso == "are":
                return prefisso + "ato"
            elif suffisso == "ere":
                return prefisso + "uto"
            elif suffisso == "ire":
                return prefisso + "ito"
        else:
            return self.participio

    def _formare_coniugazione(self, radice, suffissi):
        return [radice + suffisso for suffisso in suffissi]

    def _conjugazione_regolare(self, suffisso, radice, tempi):
        if suffisso == "are":
            return self._formare_coniugazione(radice, ["o", "i", "a", "iamo", "ate", "ano"])
        elif suffisso == "ere":
            return self._formare_coniugazione(radice, ["o", "i", "e", "iamo", "ete", "ono"])
        elif suffisso == "ire":
            return self._formare_coniugazione(radice, ["o", "i", "e", "iamo", "ite", "ono"])

    def presente(self):
        if self.presente == "[regolare]":
            radice = self.nome[:-3]
            suffisso = self.nome[-3:]
            return self._conjugazione_regolare(suffisso, radice, self.tempi)
        else:
            return self.presente.split(", ")

    def passato_prossimo(self):
        participio = self.il_participio()

        if self.ausiliare == "avere":
            return [f"ho {participio}", f"hai {participio}", f"ha {participio}", f"abbiamo {participio}",
                    f"avete {participio}", f"hanno {participio}"]
        elif self.ausiliare == "essere":
            return [f"sono {participio[:-1]}o", f"sei {participio[:-1]}o", f"è {participio[:-1]}o",
                    f"siamo {participio[:-1]}i", f"siete {participio[:-1]}i", f"sono {participio[:-1]}i"]

    def imperfetto(self):
        if self.imperfetto == "[regolare]":
            radice = self.nome[:-2]
            return self._formare_coniugazione(radice, ["vo", "vi", "va", "vamo", "vate", "vano"])
        else:
            return self.imperfetto.split(", ")

    def trapassato_prossimo(self):
        participio = self.il_participio()

        if self.ausiliare == "avere":
            return [f"avevo {participio}", f"avevi {participio}", f"aveva {participio}", f"avevamo {participio}",
                    f"avevate {participio}", f"avevano {participio}"]
        elif self.ausiliare == "essere":
            return [f"ero {participio[:-1]}o", f"eri {participio[:-1]}o", f"era {participio[:-1]}o",
                    f"eravamo {participio[:-1]}i", f"eravate {participio[:-1]}i", f"erano {participio[:-1]}i"]

    def futuro(self):
        radice = self.nome[:-3] if self.nome[-3:] == "are" else self.nome[:-1]
        return self._formare_coniugazione(radice, ["o", "ai", "a", "emo", "ete", "anno"])

    def condizionale_presente(self):
        radice = self.nome[:-3] if self.nome[-3:] == "are" else self.nome[:-1]
        return self._formare_coniugazione(radice, ["ei", "esti", "ebbe", "emmo", "este", "ebbero"])

    def condizionale_passato(self):
        participio = self.il_participio()

        if self.ausiliare == "avere":
            return [f"avrei {participio}", f"avresti {participio}", f"avrebbe {participio}", f"avremmo {participio}",
                    f"avreste {participio}", f"avrebbero {participio}"]
        elif self.ausiliare == "essere":
            return [f"sarei {participio[:-1]}o", f"saresti {participio[:-1]}o", f"sarebbe {participio[:-1]}o",
                    f"saremmo {participio[:-1]}i", f"sareste {participio[:-1]}i", f"sarebbero {participio[:-1]}i"]


class Ita:
    def __init__(self):
        self.verbi = [
            Verbo("avere", "avere", "ho, hai, ha, abbiamo, avete, hanno", "[regolare]", "[regolare]", "avr"),
            Verbo("essere", "essere", "sono, sei, è, siamo, siete, sono", "stato",
                  "ero, eri, era, eravamo, eravate, erano", "sar"),
            Verbo("aiutare", "avere", "[regolare]", "[regolare]", "[regolare]", "[regolare]"),
            Verbo("andare", "essere", "vado, vai, va, andiamo, andate, vanno", "[regolare]", "[regolare]", "andr"),
            Verbo("cantare", "avere", "[regolare]", "[regolare]", "[regolare]", "[regolare]"),
            Verbo("dare", "avere", "do, dai, da, diamo, date, danno", "[regolare]", "[regolare]", "dar"),
            Verbo("dimenticare", "avere", "[regolare]", "[regolare]", "[regolare]", "dimenticher"),
            Verbo("fare", "avere", "faccio, fai, fa, facciamo, fate, fanno", "[regolare]",
                  "facevo, facevi, faceva, facevamo, facevate, facevano", "far"),
            Verbo("mangiare", "avere", "[regolare]", "[regolare]", "[regolare]", "manger"),
            Verbo("stare", "essere", "sto, stai, sta, stiamo, state, stanno", "[regolare]", "[regolare]", "star"),
            Verbo("bere", "avere", "bevo, bevi, beve, beviamo, bevete, bevono", "bevuto",
                  "bevevo, bevevi, beveva, bevevamo, bevevate, bevevano", "berr"),
            Verbo("cadere", "avere", "[regolare]", "[regolare]", "[regolare]", "cadr"),
            Verbo("chiudere", "avere", "[regolare]", "chiuso", "[regolare]", "[regolare]"),
            Verbo("conoscere", "avere", "[regolare]", "conosciuto", "[regolare]", "[regolare]"),
            Verbo("dovere", "avere", "devo, devi, deve, dobbiamo, dovete, devono", "[regolare]", "[regolare]", "dovr"),
            Verbo("leggere", "avere", "[regolare]", "letto", "[regolare]", "[regolare]"),
            Verbo("piacere", "essere", "piaccio, piaci, piace, piacciamo, piacete, piacciono", "piaciuto", "[regolare]",
                  "[regolare]"),
            Verbo("potere", "avere", "posso, puoi, può, possiamo, potete, possono", "[regolare]", "[regolare]", "potr"),
            Verbo("prendere", "avere", "[regolare]", "preso", "[regolare]", "[regolare]"),
            Verbo("scrivere", "avere", "[regolare]", "scritto", "[regolare]", "[regolare]"),
            Verbo("vedere", "avere", "[regolare]", "visto", "[regolare]", "[regolare]"),
            Verbo("vivere", "avere", "[regolare]", "vissuto", "[regolare]", "[regolare]"),
            Verbo("volere", "avere", "voglio, vuoi, vuole, vogliamo, volete, vogliono", "[regolare]", "[regolare]",
                  "vorr")
        ]

    def get_verbo(self, nome):
        return next((verbo for verbo in self.verbi if verbo.nome == nome), None)

    def coniuga_verbo(self, verbo_nome, tempo):
        verbo = self.get_verbo(verbo_nome)
        if verbo:
            method = getattr(verbo, tempo, None)
            if callable(method):
                return method()
            else:
                return f"Tempo {tempo} non trovato per il verbo {verbo_nome}"
        return f"Verbo {verbo_nome} non trovato."

    def lista_tempi(self, verbo_nome):
        verbo = self.get_verbo(verbo_nome)
        if verbo:
            return [tempo[0] for tempo in verbo.tempi]
        return f"Verbo {verbo_nome} non trovato."


if __name__ == "__main__":
    ita = Ita()

    # Esempio di utilizzo
    verbo_nome = "andare"
    tempi_disponibili = ita.lista_tempi(verbo_nome)
    print(f"Tempi disponibili per il verbo {verbo_nome}: {tempi_disponibili}")
    tempo_da_coniugare = "passato_prossimo"
    coniugazione = ita.coniuga_verbo(verbo_nome, tempo_da_coniugare)
    print(f"Coniugazione del verbo {verbo_nome} nel tempo {tempo_da_coniugare}: {coniugazione}")
