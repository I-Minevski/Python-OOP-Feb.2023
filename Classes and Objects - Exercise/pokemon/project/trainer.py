from pokemon.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemon_names = [p.name for p in self.pokemons]
        if pokemon_name in pokemon_names:
            for p in self.pokemons:
                if p.name == pokemon_name:
                    self.pokemons.remove(p)
                    return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        pokemon_data = [p.pokemon_details() for p in self.pokemons]
        result = ""
        result += f"Pokemon trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for data in pokemon_data:
            result += f"- {data}\n"
        return result
