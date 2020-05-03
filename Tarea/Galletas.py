class Galleta:
    def __init__(self,sabor,color):
        self.sabor = sabor
        self.color = color
    def aumentar_chispitas(self):
        return "chispas"
    def __str__(self):
        return "La galleta es de {} con un color {} ".format(self.sabor,self.color)

galleta = Galleta("Chocolate","Cafe")
print(galleta)
print ("y tiene "+galleta.aumentar_chispitas())

