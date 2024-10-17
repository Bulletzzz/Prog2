class computadores:
    def __init__(self, so, cpu, ram):
        self.so = so
        self.cpu = cpu
        self.ram = ram

    def ligar(self):
        self.sit = 'ligado'

    def desligar(self):
        self.sit = 'desligado'
         
    def sobre(self):
          print(f"O SO é: {self.so}, CPU é: {self.cpu}, ram é: {self.ram} e está {self.sit}.")

class Desktop(computadores):
    def sobre (self):
        print("Desktop.")
        super().sobre()

class Notebook(Desktop):
    def sobre(self):
        print("Notebook")
        super().sobre()

desktop = Desktop('Windows', 'Intel i3', '8gb')
notebook = Notebook('Linux', 'Ryzen 5500', '16gb')

desktop.ligar()
notebook.ligar()
desktop.sobre()
notebook.sobre()