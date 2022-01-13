from pygame.math import Vector2
import random
import core


class Ennemis:

    def __init__(self):
        self.vel = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.m = 0.05
        self.k = 0.001
        self.Vmax = 5
        self.AccMax = 3
        self.taille = 20
        self.color = [255, 0, 0]
        self.position = Vector2(random.randint(0, 1000), random.randint(0, 1000))
        self.Speed = Vector2(0, 0)
        self.ACC = Vector2(0, 0)
        self.creep = None

    def show(self):
        a = 0 - self.vel.angle_to(Vector2(0, 1))

        p1 = self.position + Vector2(-5, 0).rotate(a)
        p2 = self.position + Vector2(0, 15).rotate(a)
        p3 = self.position + Vector2(5, 0).rotate(a)

        core.Draw.polygon(self.color, ((p1), (p2), (p3)), self.taille)

    def edge(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.x > fenetre[1]:
            self.position.x = 0

    def move(self, creep):
        self.ACC = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        if self.ACC.length() > self.AccMax:
            self.ACC.scale_to_length(self.AccMax)

        self.Speed = self.Speed + self.ACC

        if self.Speed.length() > self.Vmax:
            self.Speed.scale_to_length(self.Vmax)

        self.position = self.position + self.Speed

        self.ACC = Vector2(0, 0)

    def manger(self, creep):
        for p in creep:
            if p.position.distance_to(self.position) < self.taille + p.taille:
                p.vivante = False
