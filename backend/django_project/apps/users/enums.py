from enum import Enum

class Rank(Enum):
    BEGINNER = 0
    INTERMEDIATE = 1
    ADVANCED = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name.title()) for key in cls]