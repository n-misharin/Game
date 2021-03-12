import models.drawers
import random


class Player:
    def __init__(self, name="undefined"):
        self.name = name


class Unit:
    def __init__(self, unit_type):
        self.type = unit_type
        self.drawer = models.drawers.UnitPrinter(self)


class UnitTypes:
    WORKER = "WORKER"
    TRANSPORT = "TRANSPORT"
    DEFENDER = "DEFENDER"
    KAMIKAZE = "KAMIKAZE"


class FieldsTypes:
    FIELD_TYPES_COUNT = 6
    TUNNEL = 0
    SOIL = 1
    ROCK = 2
    GOLD = 3
    DIAMOND = 4
    WATER = 5
    OIL = 6


class Field:
    MAX_UNITS_ON_FIELD = 3

    def __init__(self, field_type=None, player=None, units=None):
        self.__type = None
        self.__player = None

        if units is None:
            units = list()
        self.__units = [self.addUnit(units) for unit in units]
        self.setType(field_type)
        self.setPlayer(player)

        self.drawer = models.drawers.FieldPrinter(self)

    def isBusy(self):
        return len(self.__units) >= self.MAX_UNITS_ON_FIELD

    def setPlayer(self, player):
        if player is None:
            self.__player = Player()
        else:
            self.__player = player

    def getPlayer(self):
        return self.__player

    def getType(self):
        return self.__type

    def setType(self, field_type=FieldsTypes.SOIL):
        self.__type = field_type

    def addUnit(self, unit):
        if not self.isBusy():
            self.__units.append(unit)
        else:
            raise Exception("max units on field = " + str(Field.MAX_UNITS_ON_FIELD))

    def getUnits(self):
        return self.__units[:]


class Board:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__fields = []
        for i in range(height):
            self.__fields.append([])
            for j in range(width):
                self.__fields[i].append(FieldFactory.getRandomField())

        self.drawer = models.drawers.BoardPrinter(self)

    def getSize(self):
        return self.__width, self.__height

    def getFields(self):
        return self.__fields[:][:]

    def addUnit(self, position=(0, 0), unit=None):
        x, y = position[0], position[1]
        self.__fields[y][x].addUnit(unit)


class FieldFactory:
    @staticmethod
    def getRandomField():
        field_type = random.randint(0, FieldsTypes.FIELD_TYPES_COUNT)
        return Field(field_type=field_type)
