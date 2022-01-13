import core
import pygame
from avatar import Avatar
from pygame.math import Vector2
import random


class Creep:

    def __init__(self):
        self.position = Vector2(random.randint(0, 1000), random.randint(0, 1000))
        self.vitesse = Vector2(0, 0)
        self.Acc = Vector2(0, 0)
        self.vivante = True
        self.couleur = (0, 255, 0)
        self.taille = 10
        self.maxV = 5
        self.maxAcc = 1

    def show(self):
        if self.vivante:
            core.Draw.circle(self.couleur, self.position, self.taille)

    def edge(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.x > fenetre[1]:
            self.position.x = 0

    def move(self):
        if self.vivante:
            self.Acc = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

            if self.Acc.length() > self.maxAcc:
                self.Acc.scale_to_length(self.maxAcc)

            self.vitesse = self.vitesse + self.Acc

            if self.vitesse.length() > self.maxV:
                self.vitesse.scale_to_length(self.maxV)

            self.position = self.position + self.vitesse

            self.Acc = Vector2(0, 0)
