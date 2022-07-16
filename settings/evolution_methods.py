#--------------------------------------------------------------------
# linoone: evolution_methods.py
#
# Project settings for evolution methods.
#--------------------------------------------------------------------
from enum import Enum

EvolutionParamTypes = Enum("EvolutionParamTypes", "none level item gt_number move type mapsec mon map")

# Evolution methods metadata settings that can't be automatically
# determined from source files inspection.
class EvolutionMethodSettings:
    def __init__(self):
        self.evolution_methods = {
            "1": {
                "id": "EVO_FRIENDSHIP",
                "description": "High friendship",
                "param_type": EvolutionParamTypes.none,
            },
            "2": {
                "id": "EVO_FRIENDSHIP_DAY",
                "description": "High friendship during day",
                "param_type": EvolutionParamTypes.none,
            },
            "3": {
                "id": "EVO_FRIENDSHIP_NIGHT",
                "description": "High friendship during night",
                "param_type": EvolutionParamTypes.none,
            },
            "4": {
                "id": "EVO_LEVEL",
                "description": "Level up",
                "param_type": EvolutionParamTypes.level,
            },
            "5": {
                "id": "EVO_TRADE",
                "description": "Trade",
                "param_type": EvolutionParamTypes.none,
            },
            "6": {
                "id": "EVO_TRADE_ITEM",
                "description": "Trade with item",
                "param_type": EvolutionParamTypes.item,
            },
            "7": {
                "id": "EVO_ITEM",
                "description": "Use item",
                "param_type": EvolutionParamTypes.item,
            },
            "8": {
                "id": "EVO_LEVEL_ATK_GT_DEF",
                "description": "Attack > Defense on level up",
                "param_type": EvolutionParamTypes.level,
            },
            "9": {
                "id": "EVO_LEVEL_ATK_EQ_DEF",
                "description": "Attack == Defense on level up",
                "param_type": EvolutionParamTypes.level,
            },
            "10": {
                "id": "EVO_LEVEL_ATK_LT_DEF",
                "description": "Attack < Defense on level up",
                "param_type": EvolutionParamTypes.level,
            },
            "11": {
                "id": "EVO_LEVEL_SILCOON",
                "description": "Silcoon personality on level up",
                "param_type": EvolutionParamTypes.level,
            },
            "12": {
                "id": "EVO_LEVEL_CASCOON",
                "description": "Cascoon personality on level up",
                "param_type": EvolutionParamTypes.level,
            },
            "13": {
                "id": "EVO_LEVEL_NINJASK",
                "description": "Ninjask",
                "param_type": EvolutionParamTypes.level,
            },
            "14": {
                "id": "EVO_LEVEL_SHEDINJA",
                "description": "Shedinja",
                "param_type": EvolutionParamTypes.level,
            },
            "15": {
                "id": "EVO_BEAUTY",
                "description": "Beauty",
                "param_type": EvolutionParamTypes.gt_number,
            },
            "16": {
                "id": "EVO_LEVEL_FEMALE",
                "description": "Level up (Female)",
                "param_type": EvolutionParamTypes.level,
            },
            "17": {
                "id": "EVO_LEVEL_MALE",
                "description": "Level up (Male)",
                "param_type": EvolutionParamTypes.level,
            },
            "18": {
                "id": "EVO_LEVEL_NIGHT",
                "description": "Level up (Night)",
                "param_type": EvolutionParamTypes.level,
            },
            "19": {
                "id": "EVO_LEVEL_DAY",
                "description": "Level up (Day)",
                "param_type": EvolutionParamTypes.level,
            },
            "20": {
                "id": "EVO_LEVEL_DUSK",
                "description": "Level up (Dusk)",
                "param_type": EvolutionParamTypes.level,
            },
            "21": {
                "id": "EVO_ITEM_HOLD_DAY",
                "description": "Level up (Holding item during the day)",
                "param_type": EvolutionParamTypes.item,
            },
            "22": {
                "id": "EVO_ITEM_HOLD_NIGHT",
                "description": "Level up (Holding item during the night)",
                "param_type": EvolutionParamTypes.item,
            },
            "23": {
                "id": "EVO_MOVE",
                "description": "Level up (Knowing a specific move)",
                "param_type": EvolutionParamTypes.move,
            },
            "24": {
                "id": "EVO_MOVE_TYPE",
                "description": "Level up (Knowing a move of a specific type)",
                "param_type": EvolutionParamTypes.type,
            },
            "25": {
                "id": "EVO_MAPSEC",
                "description": "Level up (In a specified map)",
                "param_type": EvolutionParamTypes.mapsec,
            },
            "26": {
                "id": "EVO_ITEM_MALE",
                "description": "Use item (Male)",
                "param_type": EvolutionParamTypes.item,
            },
            "27": {
                "id": "EVO_ITEM_FEMALE",
                "description": "Use item (Female)",
                "param_type": EvolutionParamTypes.item,
            },
            "28": {
                "id": "EVO_LEVEL_RAIN",
                "description": "Level up (While it's raining)",
                "param_type": EvolutionParamTypes.level,
            },
            "29": {
                "id": "EVO_SPECIFIC_MON_IN_PARTY",
                "description": "Level up (With specified mon in party)",
                "param_type": EvolutionParamTypes.mon,
            },
            "30": {
                "id": "EVO_LEVEL_DARK_TYPE_MON_IN_PARTY",
                "description": "Level up (With Dark-type in party)",
                "param_type": EvolutionParamTypes.level,
            },
            "31": {
                "id": "EVO_TRADE_SPECIFIC_MON",
                "description": "Trade for a specific mon",
                "param_type": EvolutionParamTypes.mon,
            },
            "32": {
                "id": "EVO_SPECIFIC_MAP",
                "description": "Level up on a specific map",
                "param_type": EvolutionParamTypes.map,
            },
            "33": {
                "id": "EVO_LEVEL_NATURE_AMPED",
                "description": "Level up (Amped nature)",
                "param_type": EvolutionParamTypes.level,
            },
            "34": {
                "id": "EVO_LEVEL_NATURE_LOW_KEY",
                "description": "Level up (Low Key nature)",
                "param_type": EvolutionParamTypes.level,
            },
            "35": {
                "id": "EVO_CRITICAL_HITS",
                "description": "Lands enough critical hits",
                "param_type": EvolutionParamTypes.gt_number,
            },
            "36": {
                "id": "EVO_SCRIPT_TRIGGER_DMG",
                "description": "Pokémon has specified HP below max, then player interacts trigger",
                "param_type": EvolutionParamTypes.none,
            },
            "37": {
                "id": "EVO_DARK_SCROLL",
                "description": "Interacts with Scroll of Darkness",
                "param_type": EvolutionParamTypes.none,
            },
            "38": {
                "id": "EVO_WATER_SCROLL",
                "description": "Interacts with Scroll of Water",
                "param_type": EvolutionParamTypes.none,
            },
            "65533": {
                "id": "EVO_PRIMAL_REVERSION",
                "description": "Primal Reversion",
                "param_type": EvolutionParamTypes.none,
            },
            "65534": {
                "id": "EVO_MOVE_MEGA_EVOLUTION",
                "description": "Mega Evolution with a move",
                "param_type": EvolutionParamTypes.move,
            },
            "65535": {
                "id": "EVO_MEGA_EVOLUTION",
                "description": "Mega Evolution",
                "param_type": EvolutionParamTypes.item,
            },
        }


    def get_label(self, method, param, items):
        """
        Builds the human-friendly label of the evolution method.
        """
        evo_method = self.evolution_methods[method]
        if evo_method["param_type"] == EvolutionParamTypes.none:
            return evo_method["description"]
        elif evo_method["param_type"] == EvolutionParamTypes.level:
            return "%s (%s)" % (evo_method["description"], param)
        elif evo_method["param_type"] == EvolutionParamTypes.item:
            return "%s %s" % (evo_method["description"], items[param]["name"])
        elif evo_method["param_type"] == EvolutionParamTypes.gt_number:
            return "%s > %s" % (evo_method["description"], param)
        else:
            return "UNKNOWN EVOLUTION METHOD"


evolution_methods = EvolutionMethodSettings()
