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
import os

def save_character(character, filename):
    """
    Save the character to a text file in the exact required format.
    Returns True on success, False otherwise.
    """
    # Basic checks (use simple equality checks rather than "if not")
    if filename == "":
        return False

    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for k in required_keys:
        if k not in character:
            return False

    file = open(filename, "w")
    file.write("Character Name: " + str(character["name"]) + "\n")
    file.write("Class: " + str(character["class"]) + "\n")
    file.write("Level: " + str(int(character["level"])) + "\n")
    file.write("Strength: " + str(int(character["strength"])) + "\n")
    file.write("Magic: " + str(int(character["magic"])) + "\n")
    file.write("Health: " + str(int(character["health"])) + "\n")
    file.write("Gold: " + str(int(character["gold"])) + "\n")
    file.close()

    # Confirm file exists now
    created = os.path.exists(filename)
    if created == True:
        return True
    return False


def load_character(filename):
    """
    Load a character from a file saved with save_character.
    Returns the character dict on success, or None if file missing or incomplete.
    """
    if os.path.exists(filename) == False:
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    data = {}
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(": ", 1)
        if len(parts) == 2:
            key_label = parts[0].strip()
            value = parts[1].strip()
            data[key_label] = value

    required_labels = ["Character Name", "Class", "Level", "Strength", "Magic", "Health", "Gold"]
    for lbl in required_labels:
        if lbl not in data:
            return None

    # Create dict manually (not using update or conversion)
    character = {}
    character["name"] = data["Character Name"]
    character["class"] = data["Class"]
    character["level"] = int(data["Level"])
    character["strength"] = int(data["Strength"])
    character["magic"] = int(data["Magic"])
    character["health"] = int(data["Health"])
    character["gold"] = int(data["Gold"])

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
