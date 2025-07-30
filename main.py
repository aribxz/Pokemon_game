import time
import random
import json

player_pokemons = []

# List of Pokémon names
pokemon_names = pokemon_names = [
    "Pikachu",
    "Charmander",
    "Bulbasaur",
    "Squirtle",
    "Eevee",
    "Jigglypuff",
    "Meowth",
    "Psyduck",
    "Machop",
    "Growlithe",
    "Poliwag",
    "Abra",
    "Geodude",
    "Ponyta",
    "Magnemite",
    "Doduo",
    "Seel",
    "Gastly",
    "Onix",
    "Cubone"
]


def load_game():
    try:
        with open("save.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_game(pokemons):
    with open("save.json", "w") as f:
        json.dump(pokemons, f)

player_pokemons = load_game() 
print(f"📂 Loaded {len(player_pokemons)} Pokémon from your Pokédex.\n")

while True:
    print("🚶 Walking...")
    time.sleep(2)  # pause for 2 seconds

    chance_appearing = random.randint(1,11)

    if chance_appearing > 3:
        name = random.choice(pokemon_names)
        power = random.randint(1, 100)
        print(f"⚡ A wild {name} (Power: {power}) appeared!")
        
    
        secret_number = random.randint(1, 100)
        caught = False
        has_hint_power = any(p['power'] > 50 for p in player_pokemons)

        for attempt in range(10):

            guess = int(input(f"🎯 Guess the number (1–100) [Attempt {attempt+1}/10]: "))
            
            if guess == secret_number:
                print("✅ You caught the Pokémon!")
                caught = True
                break

            elif guess < secret_number:
                print("❌ Too low!")

                if has_hint_power:

                    if abs(secret_number - guess) <= 5:
                        print("🔥 You're very close!")

                    elif abs(secret_number - guess) >= 25:
                        print("🥶 You're way off...")

            elif guess > secret_number:
                print("❌ Too high!")
                
                if has_hint_power:

                    if abs(secret_number - guess) <= 5:
                        print("🔥 You're very close!")

                    elif abs(secret_number - guess) >= 25:
                        print("🥶 You're way off...")



        if caught:
            player_pokemons.append({"name": name, "power": power})
            save_game(player_pokemons)
            print(f"🎒 You now have {len(player_pokemons)} Pokémon(s)!\n")

        else:
            print("💀 The Pokémon ran away... Game Over.")
            print("\n📘 Your Pokédex:")

            if player_pokemons:
                for i, p in enumerate(player_pokemons, start=1):
                    print(f"{i}. {p['name']} — Power: {p['power']}")
                print(f"\n⭐ You caught {len(player_pokemons)} Pokémon in total!")

            else:
                print("You didn't catch any Pokémon.")

            break
                

                        

            



