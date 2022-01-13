from pygame.math import Vector2
import random
import core


class Avatar:

    def __init__(self):
        self.vel = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.m = 0.05
        self.k = 0.001
        self.Vmax = 5
        self.AccMax = 3
        self.taille = 40
        self.color = [255, 255, 255]
        self.position = Vector2(random.randint(0, 1000), random.randint(0,1000))
        self.Speed = Vector2(0, 0)
        self.ACC = Vector2(0, 0)

    def show(self):
        a = 0 - self.vel.angle_to(Vector2(0, 1))

        p1 = self.position + Vector2(-5, 0).rotate(a)
        p2 = self.position + Vector2(0, 15).rotate(a)
        p3 = self.position + Vector2(5, 0).rotate(a)

        core.Draw.polygon(self.color, ((p1), (p2), (p3)))

    def edge(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.x > fenetre[1]:
            self.position.x = 0

    def move(self):
        '''Bilan des forces'''
        x = Vector2(core.getMouseLeftClick())
        v = Vector2((x - self.position))
        u = v.normalize()
        l = v.length()
        fr = Vector2(self.k * (l - self.m) * u)

        '''Vecteur Vitesse'''
        self.Speed = self.Speed + fr
        fr = Vector2(0, 0)

        '''deplacement'''
        self.position = self.position + self.Speed


