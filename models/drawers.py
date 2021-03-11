class Drawer:
    def draw(self):
        pass


class UnitPrinter:
    def __init__(self, unit):
        self.unit = unit

    def draw(self):
        print(self.unit.type[0], end='')


class FieldPrinter(Drawer):
    def __init__(self, field):
        self.field = field

    def draw(self):
        print('|', self.field.getType(), end='')
        for unit in self.field.getUnits():
            unit.drawer.draw()
            print(',', end='')
        no_print_unit_count = self.field.MAX_UNITS_ON_FIELD - len(self.field.getUnits())
        print((2 * no_print_unit_count) * ' ', '|', end='')


class BoardPrinter(Drawer):
    def __init__(self, board):
        self.board = board

    def draw(self):
        fields = self.board.getFields()
        for _line in fields:
            print(('-' * 7) * len(fields))
            for _field in _line:
                _field.drawer.draw()
            print()
