class Auto():
    def __init__(self, color , marca , peso) :
        self.color = color
        self.marca = marca
        self.peso = peso
    def cambiar_color(self):
        self.color="Negro"
    def __str__(self):
        return "El auto es de color {}  de marca {} y pesa {}".format(self.color,self.marca,self.peso)

auto = Auto("Verde","Toyota","200 kg")
print(auto)
auto.cambiar_color()
print(auto)