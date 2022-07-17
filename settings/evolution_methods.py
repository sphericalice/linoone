#--------------------------------------------------------------------
# linoone: evolution_methods.py
#
# Project settings for evolution methods.
#--------------------------------------------------------------------
from enum import Enum

EvolutionParamTypes = Enum("EvolutionParamTypes", "none level item gt_number lt_number move type mapsec mon map")

# Evolution methods metadata settings that can't be automatically
# determined from source files inspection.
class EvolutionMethodSettings:
    def __init__(self):
        self.evolution_methods = {
            "1": {
                "id": "EVO_FRIENDSHIP",
                "description": "Level up with high friendship",
                "param_type": EvolutionParamTypes.none,
            },
            "2": {
                "id": "EVO_FRIENDSHIP_DAY",
                "description": "(Day) Level up with high friendship",
                "param_type": EvolutionParamTypes.none,
            },
            "3": {
                "id": "EVO_FRIENDSHIP_NIGHT",
                "description": "(Night) Level up with high friendship",
                "param_type": EvolutionParamTypes.none,
            },
            "4": {
                "id": "EVO_LEVEL",
                "description": "Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "5": {
                "id": "EVO_TRADE",
                "description": "Trade",
                "param_type": EvolutionParamTypes.none,
            },
            "6": {
                "id": "EVO_TRADE_ITEM",
                "description": "Trade while holding",
                "param_type": EvolutionParamTypes.item,
            },
            "7": {
                "id": "EVO_ITEM",
                "description": "Use",
                "param_type": EvolutionParamTypes.item,
            },
            "8": {
                "id": "EVO_LEVEL_ATK_GT_DEF",
                "description": "(Attack > Defense) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "9": {
                "id": "EVO_LEVEL_ATK_EQ_DEF",
                "description": "(Attack == Defense) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "10": {
                "id": "EVO_LEVEL_ATK_LT_DEF",
                "description": "(Attack < Defense) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "11": {
                "id": "EVO_LEVEL_SILCOON",
                "description": "(Silcoon personality) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "12": {
                "id": "EVO_LEVEL_CASCOON",
                "description": "(Cascoon personality) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "13": {
                "id": "EVO_LEVEL_NINJASK",
                "description": "Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "14": {
                "id": "EVO_LEVEL_SHEDINJA",
                "description": "(With space in party) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "15": {
                "id": "EVO_BEAUTY",
                "description": "Level up with Beauty stat",
                "param_type": EvolutionParamTypes.gt_number,
            },
            "16": {
                "id": "EVO_LEVEL_FEMALE",
                "description": "(Female) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "17": {
                "id": "EVO_LEVEL_MALE",
                "description": "(Male) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "18": {
                "id": "EVO_LEVEL_NIGHT",
                "description": "(Night) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "19": {
                "id": "EVO_LEVEL_DAY",
                "description": "(Day) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "20": {
                "id": "EVO_LEVEL_DUSK",
                "description": "(Dusk) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "21": {
                "id": "EVO_ITEM_HOLD_DAY",
                "description": "(Day) Level up holding",
                "param_type": EvolutionParamTypes.item,
            },
            "22": {
                "id": "EVO_ITEM_HOLD_NIGHT",
                "description": "(Night) Level up holding",
                "param_type": EvolutionParamTypes.item,
            },
            "23": {
                "id": "EVO_MOVE",
                "description": "Level up while knowing",
                "param_type": EvolutionParamTypes.move,
            },
            "24": {
                "id": "EVO_MOVE_TYPE",
                "description": "Level up while knowing a",
                "param_type": EvolutionParamTypes.type,
            },
            "25": {
                "id": "EVO_MAPSEC",
                "description": "Level up in",
                "param_type": EvolutionParamTypes.mapsec,
            },
            "26": {
                "id": "EVO_ITEM_MALE",
                "description": "(Male) Use",
                "param_type": EvolutionParamTypes.item,
            },
            "27": {
                "id": "EVO_ITEM_FEMALE",
                "description": "(Female) Use",
                "param_type": EvolutionParamTypes.item,
            },
            "28": {
                "id": "EVO_LEVEL_RAIN",
                "description": "(Rain) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "29": {
                "id": "EVO_SPECIFIC_MON_IN_PARTY",
                "description": "Level up when your party has a",
                "param_type": EvolutionParamTypes.mon,
            },
            "30": {
                "id": "EVO_LEVEL_DARK_TYPE_MON_IN_PARTY",
                "description": "(Dark-type Pokémon in party) Level up at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "31": {
                "id": "EVO_TRADE_SPECIFIC_MON",
                "description": "Trade for a",
                "param_type": EvolutionParamTypes.mon,
            },
            "32": {
                "id": "EVO_SPECIFIC_MAP",
                "description": "Level up in",
                "param_type": EvolutionParamTypes.map,
            },
            "33": {
                "id": "EVO_LEVEL_NATURE_AMPED",
                "description": "Level up (Amped Nature) at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "34": {
                "id": "EVO_LEVEL_NATURE_LOW_KEY",
                "description": "Level up (Low Key Nature) at Lv.",
                "param_type": EvolutionParamTypes.level,
            },
            "35": {
                "id": "EVO_CRITICAL_HITS",
                "description": "# of critical hits in a battle",
                "param_type": EvolutionParamTypes.gt_number,
            },
            "36": {
                "id": "EVO_SCRIPT_TRIGGER_DMG",
                "description": "Interact with trigger while HP",
                "param_type": EvolutionParamTypes.lt_number,
            },
            "37": {
                "id": "EVO_DARK_SCROLL",
                "description": "Interact with Scroll of Darkness",
                "param_type": EvolutionParamTypes.none,
            },
            "38": {
                "id": "EVO_WATER_SCROLL",
                "description": "Interact with Scroll of Water",
                "param_type": EvolutionParamTypes.none,
            },
            "65533": {
                "id": "EVO_PRIMAL_REVERSION",
                "description": "Primal Revert",
                "param_type": EvolutionParamTypes.none,
            },
            "65534": {
                "id": "EVO_MOVE_MEGA_EVOLUTION",
                "description": "Mega Evolve while knowing",
                "param_type": EvolutionParamTypes.move,
            },
            "65535": {
                "id": "EVO_MEGA_EVOLUTION",
                "description": "Mega Evolve while holding",
                "param_type": EvolutionParamTypes.item,
            },
        }


    def get_label(self, method, param, items, move_names, region_map_sections, region_map_section_ids, mon_species_names, maps, map_ids, type_names):
        """
        Builds the human-friendly label of the evolution method.
        """
        try:
            evo_method = self.evolution_methods[method]
            if evo_method["param_type"] == EvolutionParamTypes.none:
                return evo_method["description"]
            elif evo_method["param_type"] == EvolutionParamTypes.level:
                return "%s %s" % (evo_method["description"], param)
            elif evo_method["param_type"] == EvolutionParamTypes.item:
                return "%s %s" % (evo_method["description"], items[param]["name"])
            elif evo_method["param_type"] == EvolutionParamTypes.gt_number:
                return "%s > %s" % (evo_method["description"], param)
            elif evo_method["param_type"] == EvolutionParamTypes.lt_number:
                return "%s < %s" % (evo_method["description"], param)
            elif evo_method["param_type"] == EvolutionParamTypes.move:
                return "%s %s" % (evo_method["description"], move_names[param])
            elif evo_method["param_type"] == EvolutionParamTypes.type:
                return "%s %s-type move" % (evo_method["description"], type_names[param])
            elif evo_method["param_type"] == EvolutionParamTypes.mapsec:
                return "%s %s" % (evo_method["description"], region_map_sections[region_map_section_ids[param]]["name"])
            elif evo_method["param_type"] == EvolutionParamTypes.mon:
                return "%s %s" % (evo_method["description"], mon_species_names[param])
            elif evo_method["param_type"] == EvolutionParamTypes.map:
                return "%s %s" % (evo_method["description"], map_ids[int(param)])
            else:
                return "UNKNOWN EVOLUTION METHOD"
        except:
            raise Exception(f"Could not read evo method {evo_method}")


evolution_methods = EvolutionMethodSettings()
