"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

# === Function 1: Create a new character ===
def create_character(name, character_class):
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "gold": 100
    }

    # Calculate base stats using helper function
    stats = calculate_stats(character_class, character["level"])
    character.update(stats)
    return character


# === Function 2: Calculate character stats ===
def calculate_stats(character_class, level):
    # Base stats
    if character_class.lower() == "warrior":
        strength = 10 + (level * 3)
        magic = 2 + (level * 1)
        health = 30 + (level * 5)
    elif character_class.lower() == "mage":
        strength = 3 + (level * 1)
        magic = 10 + (level * 3)
        health = 20 + (level * 3)
    elif character_class.lower() == "rogue":
        strength = 6 + (level * 2)
        magic = 5 + (level * 2)
        health = 15 + (level * 3)
    elif character_class.lower() == "cleric":
        strength = 5 + (level * 2)
        magic = 8 + (level * 3)
        health = 25 + (level * 4)
    else:
        raise ValueError("Unknown character class!")

    return {"strength": strength, "magic": magic, "health": health}


# === Function 3: Save character to file ===
def save_character(character, filename):
    with open(filename, "w") as f:
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")

# === Function 4: Load character from file ===
def load_character(filename):
    character = {}
    with open(filename, "r") as f:
        for line in f:
            # Split the line at ": " and clean up spaces
            key, value = line.strip().split(": ")
            key = key.lower().strip()
            value = value.strip()

            # Match the expected keys in the program
            if key == "character name":
                character["name"] = value
            elif key == "class":
                character["class"] = value
            elif key == "level":
                character["level"] = int(value)
            elif key == "strength":
                character["strength"] = int(value)
            elif key == "magic":
                character["magic"] = int(value)
            elif key == "health":
                character["health"] = int(value)
            elif key == "gold":
                character["gold"] = int(value)

    return character

    


# === Function 5: Display character info ===
def display_character(character):
    print("===== CHARACTER INFO =====")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("===========================")


# === Function 6: Level up character ===
def level_up(character):
    character["level"] += 1
    print(f"\n {character['name']} leveled up to Level {character['level']}!")
    stats = calculate_stats(character["class"], character["level"])
    character.update(stats)
    character["gold"] += 50
    return character


# === Example gameplay flow (main program) ===
if __name__ == "__main__":
    print("=== Welcome to the RPG Character Creator ===")
    name = input("Enter your character's name: ")
    print("Choose a class: Warrior, Mage, Rogue, Cleric")
    character_class = input("Enter class: ")

    # Create and show new character
    player = create_character(name, character_class)
    display_character(player)

    # Save to file
    filename = f"{name}_save.txt"
    save_character(player, filename)
    print(f"Character saved to '{filename}'.")

    # Level up example
    level_up(player)
    display_character(player)

    # Save again
    save_character(player, filename)
    print("Progress saved.\n")

    # Load and show from file
    print("Loading character from file...")
    loaded_player = load_character(filename)
    display_character(loaded_player)
