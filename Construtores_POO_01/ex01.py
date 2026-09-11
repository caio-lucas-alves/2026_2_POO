class retangulo:
    def __init__(self, b, h):
        if b <= 0:
            print("A base deve ser positiva")

        if h <= 0:
            print("A altura deve ser positiva")

        else:
            self.b = b
            self.h = h

    def SetBase(self, nova_base):
        if nova_base <= 0:
            print ("A nova base precisa ser positiva")

        self.b = nova_base

    def SetAltura(self, nova_altura):
        if nova_altura <= 0:
            print ("A altura precisa ser positiva")

        self.a = nova_altura

    def GetBase(self):
        return self.b
        
    def GetAltura(self):
        return self.h

    def CalcArea(self):
        return self.b * self.h

    def CalcDiagonal(self):
        return math.sqrt(self.b**2 + self.h**2)

    def ToString(self):
        return f"Base: {self.b}, Altura: {self.h}"

