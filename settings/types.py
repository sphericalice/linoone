#--------------------------------------------------------------------
# linoone: types.py
#
# Project settings for Pokémon types.
#--------------------------------------------------------------------
from enum import Enum

# Pokémon types metadata that can't be automatically
# determined from source files inspection.
class TypesSettings:
    def __init__(self):
        self.coords = {
            "0": { # Normal
                "x": "0",
                "y": "0",
            },
            "1": { # Fighting
                "x": "1",
                "y": "2",
            },
            "2": { # Flying
                "x": "0",
                "y": "2",
            },
            "3": { # Poison
                "x": "0",
                "y": "3",
            },
            "4": { # Ground
                "x": "2",
                "y": "1",
            },
            "5": { # Rock
                "x": "1",
                "y": "1",
            },
            "6": { # Bug
                "x": "3",
                "y": "2",
            },
            "7": { # Ghost
                "x": "2",
                "y": "2",
            },
            "8": { # Steel
                "x": "2",
                "y": "3",
            },
            "9": { # Mystery
                "x": "1",
                "y": "4",
            },
            "10": { # Fire
                "x": "1",
                "y": "0",
            },
            "11": { # Water
                "x": "2",
                "y": "0",
            },
            "12": { # Grass
                "x": "3",
                "y": "0",
            },
            "13": { # Electric
                "x": "0",
                "y": "1",
            },
            "14": { # Psychic
                "x": "1",
                "y": "3",
            },
            "15": { # Ice
                "x": "3",
                "y": "1",
            },
            "16": { # Dragon
                "x": "0",
                "y": "4",
            },
            "17": { # Dark
                "x": "3",
                "y": "3",
            },
            "18": { # Fairy
                "x": "2",
                "y": "4",
            },
        }


types = TypesSettings()
