class Pokemon:
    def __init__(self, poke_num, name, types, desc, evol):
        '''
        Name=string, pokedex number=int, type=list, description=string, evolution(s)=list
        '''
        self.poke_num = poke_num
        self.name = name
        self.types = types
        self.desc = desc
        self.evol = evol
        
    def __str__(self):
        '''
        1.  Bulbasaur
            Grass / Poison
            It can go for days without eating a single morsel. In the bulb on its back, it stores energy.
            Bulbasaur -> Ivysaur -> Venusaur
        '''

        # to join elements of lists with a character(s), use list.join() function
        type_str = " / ".join(self.types).title()
        evo_str = None
        if (len(self.evol)) > 1:
            evo_str = " -> ".join(self.evol).title()
        else:
            evo_str = "Does not evolve."
        
        output = f"{self.poke_num}.\t{self.name}\n"
        output += f"\t{type_str}\n"
        output += f"\t{self.desc}\n"
        output += f"\t{evo_str}\n"

        return output


'''
# -------- TEST ----------
poke_num = 1
name = "Bulbasaur"
types = ["Grass", "Poison"]
desc = "It can go for days without eating a single morsel. In the bulb on its back, it stores energy."
evol = ["Bulbasaur","Ivysaur","Venusaur"]

# To make a new Pokemon object, we do something like:
# pokemon_example = Pokemon(poke_num, name, types, desc, evol)
# Then we can test the __str__ function by simply calling print(pokemon_example)

pokemon_bulbasaur = Pokemon(poke_num, name, types, desc, evol)
print(pokemon_bulbasaur)
'''