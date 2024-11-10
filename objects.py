import board

class Thing:
    def __init__(self, appearance, collision, pushable, coordinates, event = "none"):
        self.appearance = appearance
        self.collision = collision
        self.pushable = pushable
        self.coordinates = coordinates
        self.atop = "Don't look at this"
        self.event = event

    def check_atop(self):
        self.atop = board.board[self.coordinates]

    def collision(self, x_plus, y_plus, push):
        if push:
            ex_atop = self.atop
            self.atop.move(x_plus, y_plus)
            self.check_atop()
            if self.atop == ex_atop:
                self.coordinates[0] -= x_plus
                self.coordinates[1] -= y_plus
        else:
            self.coordinates[0] -= x_plus
            self.coordinates[1] -= y_plus

    def move(self, x_plus, y_plus):
        self.coordinates[0] += x_plus
        self.coordinates[1] += y_plus
        try:
            self.check_atop()
        except IndexError:
            self.collision(x_plus, y_plus, False)
            return
        if self.atop.collision:
            self.collision(x_plus, y_plus, self.atop.pushable)


class PlayerThing(Thing):
    def __init__(self, appearance, coordinates):
        super().__init__(appearance, True, True, coordinates)


class DirectionalThing(Thing):
    def __init__(self, appearance, collision, pushable, coordinates, direction):
        super().__init__(appearance, collision, pushable, coordinates)
        self.direction = direction


class SelfMovingThing(DirectionalThing):
    def __init__(self, appearance, coordinates, direction):
        super().__init__(appearance, True, True, coordinates, direction)


Box = Thing("+", True, True, (0, 0))
Player = PlayerThing("P", (0, 0))
