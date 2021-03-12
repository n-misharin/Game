class GameSettings:
    MAX_UNIT_COUNT_ON_FIELD = 3


class UnitType:
    TYPES_COUNT = 4
    WORKER = 0
    TRANSPORT = 1
    KAMIKAZE = 2
    SECURITY = 3


class FieldType:
    TYPES_COUNT = 6
    SOIL = 0
    OIL = 1
    GOLD = 2
    DIAMOND = 3
    WATER = 4
    ROCK = 5


class Unit:
    def __init__(self, energy=0, position=None, unit_type=0, health=1):
        self.type = unit_type
        # position on game board
        self.position = position
        # cells per step
        self.energy = energy
        self.health = health

    def set_position(self, field):
        pass

    def is_can_move(self, new_position=(0, 0)):
        if self.energy <= 0 or self.health <= 0:
            return False
        return True


class Worker(Unit):
    def __init__(self, position=None):
        super().__init__(energy=3, unit_type=UnitType.WORKER, position=position)


class Field:
    def __init__(self, field_type=FieldType.SOIL, units=None):
        self.type = field_type
        self.units = units
        if self.units is None:
            self.units = []
        self.__max_unit_count = GameSettings.MAX_UNIT_COUNT_ON_FIELD

    def is_busy(self):
        return len(self.units) >= self.__max_unit_count

    def add_unit(self, unit):



class Board:
    def __init__(self, size=(1, 1), fields=None):
        if fields is None:
            self.__fields = [[Field()]]
        self.size = self[:]


