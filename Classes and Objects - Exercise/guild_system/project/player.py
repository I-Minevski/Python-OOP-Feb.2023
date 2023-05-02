class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        result = f"""Name: {self.name}
Guild: {self.guild}
HP: {self.hp}
MP: {self.mp}\n"""
        result += '\n'.join(f"==={k} - {v}" for k, v in self.skills.items())

        return result

