class Teglalap:
    def terulet(self, a, b):
        t = a * b
        return t

    def kerulet(self, a, b):
        k = 2 * (a + b)
        return k

    def bekeres(self, a, b):
        global a_oldal, b_oldal
        a_oldal = a
        b_oldal = b
        while True:
            # a_oldal = input("Add meg az 'a' oldalt: ")
            try:
                a_oldal = int(a_oldal)
                break;
            except ValueError:
                try:
                    a_oldal = float(a_oldal)
                    break;
                except ValueError:
                    # print("Nem számot adott meg!")
                    pass
        while True:
            # b_oldal = input("Add meg az 'b' oldalt: ")
            try:
                b_oldal = int(b_oldal)
                break;
            except ValueError:
                try:
                    b_oldal = float(b_oldal)
                    break;
                except ValueError:
                    # print("Nem számot adott meg!")
                    pass

    def szamitas(self, mertekegyseg, mertekegyseg_szamitott):
        global a_oldal, b_oldal
        terulet_szamitott = 0
        if mertekegyseg == "cm" and mertekegyseg_szamitott == "cm":
            terulet_szamitott = self.terulet(a_oldal, b_oldal)
            kerulet_szamitott = self.kerulet(a_oldal, b_oldal)

        elif mertekegyseg == "cm" and mertekegyseg_szamitott == "dm":
            terulet_szamitott = self.terulet(a_oldal, b_oldal) / 10
            kerulet_szamitott = self.kerulet(a_oldal, b_oldal) / 10

        elif mertekegyseg == "dm" and mertekegyseg_szamitott == "dm":
            terulet_szamitott = self.terulet(a_oldal, b_oldal)
            kerulet_szamitott = self.kerulet(a_oldal, b_oldal)

        elif mertekegyseg == "dm" and mertekegyseg_szamitott == "cm":
            terulet_szamitott = self.terulet(a_oldal, b_oldal) * 10
            kerulet_szamitott = self.kerulet(a_oldal, b_oldal) * 10

        return terulet_szamitott, kerulet_szamitott

    # szamitas()
