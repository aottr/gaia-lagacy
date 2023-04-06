from enum import IntEnum


class SubOrders(IntEnum):
    Lizard = 1
    Snake = 2
    WormLizard = 3
    Rodent = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
