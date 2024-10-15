"""
tp4
Par Yul Kim
Groupe:405
plusieurs exercise de tp4
"""
import math
import random
from dataclasses import dataclass
exercise = int(input('Quel exercise voulez vous voir?:'))

if exercise == 1:
    class StringFoo:
        message = input('Quel est votre message?:')

    def set_string(message):
        StringFoo.message = str(message)

    def print_string(message):
        print(message.upper())
    set_string(StringFoo.message)
    print_string(StringFoo.message)

elif exercise == 2:
    class Rectangle:
        def __init__(self):
            self.longeur = int(input('Quel est votre longeur ?:'))
            self.largeur = int(input('Quel est votre largeur ?:'))
            self.aire = 0

        def calcule_aire(self):
            self.aire = self.longeur*self.largeur

        def afficher_info(self):
            print(f'Longeur:{self.longeur}\nLargeur:{self.largeur}\nAire:{self.aire}')
    a = Rectangle()
    a.calcule_aire()
    a.afficher_info()

elif exercise == 3:
    class Cercle:
        def __init__(self):
            self.rayon = int(input('Quel est votre rayon?:'))
            self.aire = 0
            self.circ = 0

        def calcule_aire(self):
            self.aire = self.rayon**2*math.pi

        def calcule_circonference(self):
            self.circ = 2*math.pi*self.rayon

        def afficher_info(self):
            print(f'Rayon:{self.rayon}\nAire:{self.aire}\nCirconference:{self.circ}')

    a = Cercle()
    a.calcule_aire()
    a.calcule_circonference()
    a.afficher_info()

elif exercise == 4:
    class Hero:
        def __init__(self):
            self.name = input('Quel est le nom de votre Hero?')
            self.hp = random.randint(1, 10)+random.randint(1, 10)
            self.atk = random.randint(1, 6)
            self.defense = random.randint(1, 6)
            self.qte_dommage = random.randint(1, 10)

        def attque(self):
            f_attaque = self.atk+random.randint(1, 6)
            print(f'Attaque:{f_attaque}')

        def dommage(self):
            self.hp -= self.qte_dommage - self.defense
            print(f'Dommage recu:{self.qte_dommage}')

        def est_vivant(self):
            if self.hp > 0:
                print('vivant')
            else:
                print('mort')

        def info(self):
            print(f'Nom:{self.name}\nHp:{self.hp}\nDefense{self.defense}')

    a = Hero()
    a.info()
    a.attque()
    a.dommage()
    a.est_vivant()
elif exercise == 5:
    @dataclass
    class HeroData:
        name: str
        constitution: int
        force: int
        defense: int
        intelligence: int
        dexterite: int
        charisme: int
        sagesse: int
        qte_dommage: int

    class HeroMain:
        def __init__(self):
            self.data = HeroData(str(input('Quel est le nom de votre Hero?')),
                                 random.randint(1, 20), random.randint(1, 20),
                                 random.randint(1, 20), random.randint(1, 20),
                                 random.randint(1, 20), random.randint(1, 20),
                                 random.randint(1, 20), random.randint(1, 10))

        def attque(self):
            f_attaque = self.data.force+random.randint(1, 6)
            print(f'Attaque:{f_attaque}')

        def dommage(self):
            self.data.constitution -= self.data.qte_dommage - self.data.defense
            print(f'Dommage recu:{self.data.qte_dommage}')

        def est_vivant(self):
            if self.data.constitution > 0:
                print('vivant')
            else:
                print('mort')

        def info(self):
            print(f'Nom:{self.data.name}\nConstitution:{self.data.constitution}\nDefense:{self.data.defense}'
                  f'\nIntelligence:{self.data.intelligence}'
                  f'\nDexterite:{self.data.dexterite}\nCharism:{self.data.charisme}\nSagesse:{self.data.sagesse}')

    hero = HeroMain()
    hero.info()
    hero.attque()
    hero.dommage()
    hero.est_vivant()
