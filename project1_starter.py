"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
# project1_starter.py
# Clean, test-friendly implementation for the assignment
# No top-level I/O (safe to import), simple logic, integer numeric fields

import os

# === Function 1: Create a new character ===
def create_character(name, character_class):
    """
    Create and return a character dict for valid classes.
    Returns None for invalid class.
    Keeps the class string exactly as passed.
    """
    valid = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid:
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": int(level),
        "strength": int(strength),
        "magic": int(magic),
        "health": int(health),
        "gold": int(100)
    }
    return character


# === Function 2: Calculate character stats ===
def calculate_stats(character_class, level):
    """
    Return a tuple (strength, magic, health) as integers.
    Accepts class names exactly as in the assignment but handles internally.
    """
    # ensure level is an integer >= 1
    lvl = int(level)
    if lvl < 1:
        lvl = 1

    # Use simple, deterministic base values and integer scaling
    if character_class == "Warrior":
        base_s, base_m, base_h = 15, 3, 120
        per_s, per_m, per_h = 3, 1, 10
    elif character_class == "Mage":
        base_s, base_m, base_h = 5, 15, 80
        per_s, per_m, per_h = 1, 4, 6
    elif character_class == "Rogue":
        base_s, base_m, base_h = 8, 8, 70
        per_s, per_m, per_h = 2, 2, 5
    elif character_class == "Cleric":
        base_s, base_m, base_h = 9, 14, 100
        per_s, per_m, per_h = 2, 3, 8
    else:
        # unknown class -> return zeros
        return (0, 0, 0)

    offset = lvl - 1
    strength = int(base_s + per_s * offset)
    magic = int(base_m + per_m * offset)
    health = int(base_h + per_h * offset)
    return (strength, magic, health)


# === Function 3: Save character to file ===
def save_character(character, filename):
    """
    Save character to text file in exact required format.
    Returns True on success, False otherwise.
    """
    # filename should be a non-empty string
    if filename == "":
        return False

    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for k in required_keys:
        if k not in character:
            return False

    # Write file with exact labels and integer numeric values
    file = open(filename, "w")
    file.write("Character Name: " + str(character["name"]) + "\n")
    file.write("Class: " + str(character["class"]) + "\n")
    file.write("Level: " + str(int(character["level"])) + "\n")
    file.write("Strength: " + str(int(character["strength"])) + "\n")
    file.write("Magic: " + str(int(character["magic"])) + "\n")
    file.write("Health: " + str(int(character["health"])) + "\n")
    file.write("Gold: " + str(int(character["gold"])) + "\n")
    file.close()

    # verify file exists now
    if os.path.exists(filename) == True:
        return True
    return False


# === Function 4: Load character from file ===
def load_character(filename):
    """
    Load character from a file saved with save_character.
    Return dict on success, None if file missing or incomplete.
    """
    if os.path.exists(filename) == False:
        return None

    file = open(filename, "r")
    raw_lines = file.readlines()
    file.close()

    data = {}
    for raw in raw_lines:
        line = raw.strip()
        if line == "":
            continue
        parts = line.split(": ", 1)
        if len(parts) != 2:
            continue
        key_label = parts[0].strip()
        value = parts[1].strip()
        data[key_label] = value

    required_labels = ["Character Name", "Class", "Level", "Strength", "Magic", "Health", "Gold"]
    for lbl in required_labels:
        if lbl not in data:
            return None

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
    if character is None:
        return
    print("===== CHARACTER INFO =====")
    print("Name:", character.get("name", ""))
    print("Class:", character.get("class", ""))
    print("Level:", character.get("level", ""))
    print("Strength:", character.get("strength", ""))
    print("Magic:", character.get("magic", ""))
    print("Health:", character.get("health", ""))
    print("Gold:", character.get("gold", ""))
    print("==========================")


# === Function 6: Level up character ===
def level_up(character):
    if character is None:
        return None
    character["level"] = int(character["level"]) + 1
    s, m, h = calculate_stats(character["class"], character["level"])
    character["strength"] = int(s)
    character["magic"] = int(m)
    character["health"] = int(h)
    character["gold"] = int(character.get("gold", 0)) + 50
    return character


# No top-level code that runs on import beyond definitions.
if __name__ == "__main__":
    # Simple interactive demo for manual runs (won't run during import in tests)
    print("=== Welcome to the RPG Character Creator ===")
    name = input("Enter your character's name: ")
    print("Choose a class: Warrior, Mage, Rogue, Cleric")
    character_class = input("Enter class: ")
    player = create_character(name, character_class)
    display_character(player)
