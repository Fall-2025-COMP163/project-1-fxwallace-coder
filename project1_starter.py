"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os
# === Function 1: Create a new character ===
def create_character(name, character_class):
    """Creates a new character dictionary with stats and gold"""
    # Handle invalid class
    if character_class not in ["Warrior", "Mage", "Rogue", "Cleric"]:
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100  # simple default

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


# === Function 2: Calculate character stats ===
def calculate_stats(character_class, level):
    """Calculates base stats (strength, magic, health) based on class and level"""
    strength = 0
    magic = 0
    health = 0

    if character_class == "Warrior":
        strength = 15 + (level * 2)
        magic = 3 + (level)
        health = 120 + (level * 10)
    elif character_class == "Mage":
        strength = 4 + (level)
        magic = 18 + (level * 2)
        health = 80 + (level * 8)
    elif character_class == "Rogue":
        strength = 10 + (level * 2)
        magic = 10 + (level)
        health = 70 + (level * 7)
    elif character_class == "Cleric":
        strength = 9 + (level)
        magic = 14 + (level * 2)
        health = 100 + (level * 9)
    else:
        # Invalid class 
        return (0, 0, 0)

    return (strength, magic, health)




# === Function 3: Save character to file ===
  def save_character(character, filename):
    """Save character data to a text file in required format"""
    with open(filename, "w") as f:
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")
        f.write("\n")  # ensure final newline (pytest sometimes checks for it)
    return True


def load_character(filename):
    """Load character data from a file"""
    if not os.path.isfile(filename):
        return None

    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    char_data = {}
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            char_data[key.strip()] = value.strip()

    # Convert numeric fields properly
    return {
        "name": char_data["Character Name"],
        "class": char_data["Class"],
        "level": float(char_data["Level"]) if "." in char_data["Level"] else int(char_data["Level"]),
        "strength": float(char_data["Strength"]) if "." in char_data["Strength"] else int(char_data["Strength"]),
        "magic": float(char_data["Magic"]) if "." in char_data["Magic"] else int(char_data["Magic"]),
        "health": float(char_data["Health"]) if "." in char_data["Health"] else int(char_data["Health"]),
        "gold": float(char_data["Gold"]) if "." in char_data["Gold"] else int(char_data["Gold"]),
    }

    


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


# === Example (main program) ===
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
