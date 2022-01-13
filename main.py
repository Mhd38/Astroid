import core
import pygame
import creep
import ennemis
from avatar import Avatar
from creep import Creep
from ennemis import Ennemis


def setup():
    print("-----setup------start")
    core.WINDOW_SIZE = [1000, 1000]
    core.fps = 30
    core.memory("A", Avatar())
    core.memory("B", Ennemis())
    core.memory("nbrcreep", 30)
    core.memory("listcreep", [])
    core.memory("nbrEnnemis", 25)
    core.memory("listEnnemis", [])

    for i in range(0, core.memory("nbrcreep")):
        core.memory("listcreep").append(creep.Creep())

    for i in range(0, core.memory("nbrEnnemis")):
        core.memory("listEnnemis").append(ennemis.Ennemis())

    print("-----setup------End--")


def run():
    core.cleanScreen()
    core.memory("A").show()
    core.memory("A").edge(core.WINDOW_SIZE)

    for c in core.memory("listcreep"):
        c.edge(core.WINDOW_SIZE)
        c.show()
        c.move()

    for p in core.memory("listEnnemis"):
        p.edge(core.WINDOW_SIZE)
        p.show()
        p.move("listcreep")

    for p in core.memory("listEnnemis"):
        p.manger(core.memory("listcreep"))

    if core.getMouseLeftClick():
        core.memory("A").move()


core.main(setup, run)
