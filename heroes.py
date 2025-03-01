import json

class Hero:
    def __init__(self, id: int, name: str, localized_name: str, primary_attr: str, attack_type: str, roles: list, legs: int, 
                 img: str = None, icon: str = None, base_health: int = None, base_health_regen: float = None,
                 base_mana: int = None, base_mana_regen: float = None, base_armor: float = None, base_mr: int = None,
                 base_attack_min: int = None, base_attack_max: int = None, base_str: int = None, base_agi: int = None,
                 base_int: int = None, str_gain: float = None, agi_gain: float = None, int_gain: float = None,
                 attack_range: int = None, projectile_speed: int = None, attack_rate: float = None,
                 base_attack_time: int = None, attack_point: float = None, move_speed: int = None,
                 turn_rate: float = None, cm_enabled: bool = None, day_vision: int = None, night_vision: int = None):
        self.id = id
        self.name = name
        self.localized_name = localized_name
        self.primary_attr = primary_attr
        self.attack_type = attack_type
        self.roles = roles
        self.legs = legs
        self.img = img
        self.icon = icon
        self.base_health = base_health
        self.base_health_regen = base_health_regen
        self.base_mana = base_mana
        self.base_mana_regen = base_mana_regen
        self.base_armor = base_armor
        self.base_mr = base_mr
        self.base_attack_min = base_attack_min
        self.base_attack_max = base_attack_max
        self.base_str = base_str
        self.base_agi = base_agi
        self.base_int = base_int
        self.str_gain = str_gain
        self.agi_gain = agi_gain
        self.int_gain = int_gain
        self.attack_range = attack_range
        self.projectile_speed = projectile_speed
        self.attack_rate = attack_rate
        self.base_attack_time = base_attack_time
        self.attack_point = attack_point
        self.move_speed = move_speed
        self.turn_rate = turn_rate
        self.cm_enabled = cm_enabled
        self.day_vision = day_vision
        self.night_vision = night_vision

    def __str__(self):
        return self.to_message()
    
    def to_message(self) -> str:
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Localized Name: {self.localized_name}\n"
                f"Primary Attribute: {self.primary_attr}\n"
                f"Attack Type: {self.attack_type}\n"
                f"Roles: {', '.join(self.roles)}\n")
    def to_long_message(self) -> str:
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Localized Name: {self.localized_name}\n"
                f"Primary Attribute: {self.primary_attr}\n"
                f"Attack Type: {self.attack_type}\n"
                f"Roles: {', '.join(self.roles)}\n"
                f"Legs: {self.legs}\n"
                f"Base Health: {self.base_health}\n"
                f"Base Health Regen: {self.base_health_regen}\n"
                f"Base Mana: {self.base_mana}\n"
                f"Base Mana Regen: {self.base_mana_regen}\n"
                f"Base Armor: {self.base_armor}\n"
                f"Base Magic Resistance: {self.base_mr}\n"
                f"Base Attack Min: {self.base_attack_min}\n"
                f"Base Attack Max: {self.base_attack_max}\n"
                f"Base Strength: {self.base_str}\n"
                f"Base Agility: {self.base_agi}\n"
                f"Base Intelligence: {self.base_int}\n"
                f"Strength Gain: {self.str_gain}\n"
                f"Agility Gain: {self.agi_gain}\n"
                f"Intelligence Gain: {self.int_gain}\n"
                f"Attack Range: {self.attack_range}\n"
                f"Projectile Speed: {self.projectile_speed}\n"
                f"Attack Rate: {self.attack_rate}\n"
                f"Base Attack Time: {self.base_attack_time}\n"
                f"Attack Point: {self.attack_point}\n"
                f"Move Speed: {self.move_speed}\n"
                f"Turn Rate: {self.turn_rate}\n"
                f"Captains Mode Enabled: {self.cm_enabled}\n"
                f"Day Vision: {self.day_vision}\n"
                f"Night Vision: {self.night_vision}\n")

heroes = []
with open("dotaconstants/build/heroes.json") as file:
    data = json.load(file)
    for hero_id, hero_data in data.items():
        hero = Hero(
            id=hero_data["id"],
            name=hero_data["name"],
            localized_name=hero_data["localized_name"],
            primary_attr=hero_data["primary_attr"],
            attack_type=hero_data["attack_type"],
            roles=hero_data["roles"],
            legs=hero_data["legs"],
            img=hero_data.get("img"),
            icon=hero_data.get("icon"),
            base_health=hero_data.get("base_health"),
            base_health_regen=hero_data.get("base_health_regen"),
            base_mana=hero_data.get("base_mana"),
            base_mana_regen=hero_data.get("base_mana_regen"),
            base_armor=hero_data.get("base_armor"),
            base_mr=hero_data.get("base_mr"),
            base_attack_min=hero_data.get("base_attack_min"),
            base_attack_max=hero_data.get("base_attack_max"),
            base_str=hero_data.get("base_str"),
            base_agi=hero_data.get("base_agi"),
            base_int=hero_data.get("base_int"),
            str_gain=hero_data.get("str_gain"),
            agi_gain=hero_data.get("agi_gain"),
            int_gain=hero_data.get("int_gain"),
            attack_range=hero_data.get("attack_range"),
            projectile_speed=hero_data.get("projectile_speed"),
            attack_rate=hero_data.get("attack_rate"),
            base_attack_time=hero_data.get("base_attack_time"),
            attack_point=hero_data.get("attack_point"),
            move_speed=hero_data.get("move_speed"),
            turn_rate=hero_data.get("turn_rate"),
            cm_enabled=hero_data.get("cm_enabled"),
            day_vision=hero_data.get("day_vision"),
            night_vision=hero_data.get("night_vision")
        )
        heroes.append(hero)

def get_hero(id: int) -> Hero | None:
    for hero in heroes:
        if hero.id == id:
            return hero
    return None
