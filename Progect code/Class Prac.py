from tkinter import *
from PIL import Image ,ImageTk
import csv
import random

class Character():
    def __init__(self,health,atack,defense,speed):
        self.health = health
        self.atack = atack
        self.defense = defense
        self.speed = speed

    def run(self):
        distance = self.speed + self.health
        print(distance)

    def kill(self):
        if self.health <= 0:
            print("breaking news \n \n \n im dead")


    def damage(self,dmg):
        nhealth = self.health - (dmg - self.defense )
        if nhealth > self.health:
            nhealth = self.health
        print(nhealth)
        self.health = nhealth


x = 0
man1 = Character(10,6,3,5)
man2 = Character(20,4,3,2)
while True:
    char = input("1. Man1\n2. Man2\n")
    if int(char) == 1:
        im = int(input("1. Run\n2. Attack\n"))
        if im == 1:
            man1.run()
        elif im == 2:
            man1.damage(1)
        man1.kill()
        man2.kill()
    elif int(char) == 2:
        im = int(input("1. Run\n2. Attack\n"))
        if im == 1:
            man2.run()
        elif im == 2:
            man2.damage(6)
        man1.kill()
        man2.kill()