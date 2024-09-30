class computadores:
    def __init__(self, so, cpu, ram):
        self.so = so
        self.cpu = cpu
        self.ram = ram

    def ligar(self):
        print("O computador está ligando...")


    def sobre(self):
        print(f"O SO é: {self.so} O CPU é: {self.cpu} A ram é:  {self.ram}")


    def desligar(self):
        print("O computador está desligando...")


classe = computadores(
    so='Linux',
    cpu='Ryzen 5',
    ram='16gb'
    )


classe2 = computadores(
    so ='Windows',
    cpu = 'Intel i3',
    ram = '8gb',
)


classe.ligar()
classe.sobre()
classe.desligar()

classe2.ligar()
classe2.sobre()
classe2.desligar()
