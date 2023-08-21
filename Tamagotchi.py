import random
import time


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # Nível de fome
        self.happiness = 50  # Nível de felicidade
        self.energy = 50  # Nível de energia
        self.is_alive = True

    def feed(self):
        if self.is_alive:
            print(f"{self.name} está sendo alimentado.")
            self.hunger -= 10
            self.happiness += 5
            self.energy += 5
        else:
            print(f"{self.name} não pode ser alimentado, ele está morto.")

    def play(self):
        if self.is_alive:
            print(f"{self.name} está brincando.")
            self.hunger += 5
            self.happiness += 10
            self.energy -= 5
        else:
            print(f"{self.name} não pode brincar, ele está morto.")

    def sleep(self):
        if self.is_alive:
            print(f"{self.name} está dormindo.")
            self.energy += 20
            self.hunger += 5
            self.happiness -= 5
        else:
            print(f"{self.name} não pode dormir, ele está morto.")

    def check_status(self):
        if self.is_alive:
            print(f"Nome: {self.name}")
            print(f"Fome: {self.hunger}")
            print(f"Felicidade: {self.happiness}")
            print(f"Energia: {self.energy}")
        else:
            print(f"{self.name} está morto.")

    def update(self):
        if self.is_alive:
            self.hunger += 5
            self.happiness -= 5
            self.energy -= 5
            if self.hunger >= 100 or self.happiness <= 0 or self.energy <= 0:
                self.is_alive = False
                print(f"{self.name} morreu devido à negligência.")


# Função para simular o tempo passando e atualizar o estado do Tamagotchi
def simulate_time(tamagotchi):
    while tamagotchi.is_alive:
        tamagotchi.update()
        time.sleep(5)  # Atualize a cada 5 segundos


# Função principal
def main():
    name = input("Escolha um nome para o seu Tamagotchi: ")
    tamagotchi = Tamagotchi(name)

    print(f"Seu Tamagotchi {name} nasceu!")

    # Inicie a simulação do tempo em segundo plano


    # Interface de linha de comando para interagir com o Tamagotchi
    while tamagotchi.is_alive:
        print("\nAções disponíveis:")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Dormir")
        print("4. Verificar status")
        print("5. Sair")
        choice = input("Escolha uma ação: ")

        if choice == '1':
            tamagotchi.feed()
        elif choice == '2':
            tamagotchi.play()
        elif choice == '3':
            tamagotchi.sleep()
        elif choice == '4':
            tamagotchi.check_status()
        elif choice == '5':
            tamagotchi.is_alive = False
        else:
            print("Escolha uma ação válida.")

    print("Obrigado por cuidar do seu Tamagotchi!")


if __name__ == "__main__":
    main()
