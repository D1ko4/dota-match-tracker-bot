import json

class Hero:
    def __init__(self, id: int, name: str, localized_name: str, primary_attr: str, attack_type: str, roles: list, legs: int):
        self.id = id
        self.name = name
        self.localized_name = localized_name
        self.primary_attr = primary_attr
        self.attack_type = attack_type
        self.roles = roles
        self.legs = legs

    def __str__(self):
        return self.toMessage()
    
    def to_message(self) -> str:
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Localized Name: {self.localized_name}\n"
                f"Primary Attribute: {self.primary_attr}\n"
                f"Attack Type: {self.attack_type}\n"
                f"Roles: {', '.join(self.roles)}\n")

def get_hero(id: int) -> Hero | None:
    for hero in heroes:
        if hero.id == id:
            return hero
    return None



heroes = []
with open("data/heroes.json") as file:
    data = json.load(file)
    for hero in data:
        heroes.append(Hero(hero["id"], hero["name"], hero["localized_name"], hero["primary_attr"], hero["attack_type"], hero["roles"], hero["legs"]))
