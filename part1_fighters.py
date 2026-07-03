# part1_fighters.py
import os
import pandas as pd

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()

CSV_PATH = os.path.join(SCRIPT_DIR, "fighters.csv")
SPRITE_DIR = os.path.join(SCRIPT_DIR, "sprites")
os.makedirs(SPRITE_DIR, exist_ok=True)

CLASS_MODIFIERS = {
    "Beast": {"health": +80, "strength": +50, "defense": -30, "speed": 20, "stamina": +15, "evasion": 0.02, "stamina_regen": 3, "stamina_light": 6, "stamina_heavy": 11},
    "Crazy": {"health": -20, "strength": +50, "defense": +0, "speed": 35, "stamina": +20, "evasion": 0.03, "stamina_regen": 5, "stamina_light": 6, "stamina_heavy": 9},
    "Tank": {"health": +0, "strength": + 30, "defense": + 100, "speed": 10, "stamina": -15, "evasion": 0.005, "stamina_regen": 2, "stamina_light": 12, "stamina_heavy": 25},
    "Genius": {"health": +30, "strength": +40, "defense": -20, "speed": 30, "stamina": +15, "evasion": 0.0625, "stamina_regen": 5, "stamina_light": 1, "stamina_heavy": 2},
    "Special: Z": {"health": +0, "strength": +0, "defense": -0, "speed": 20, "stamina": +0, "evasion": 0.0, "stamina_regen": 10, "stamina_light": 1, "stamina_heavy": 1}
}

def apply_class_modifiers(fighter):
    class_name = fighter.get("class","")
    modifiers = CLASS_MODIFIERS.get(class_name, {})
    for stat_name, class_value in modifiers.items():
        special_stats = ("crit_chance", "crit_bonus", "attacks")
        if stat_name in special_stats:
            fighter[stat_name] = class_value
        else:
            base_value = fighter.get(stat_name, 0)
            new_value = base_value + class_value
            fighter[stat_name] = new_value


FIGHTERS = [
    {
        "name": "Mike Tyson",
        "class": "Beast",
        "health": 1220,
        "strength": 280,
        "defense": 50,
        "stamina": 135,
        "critchance": 0.01,
        "critmult": 3.275,
        "sprite": "tyson.png",
        "sprite_scale": 1.0,
    },
    {
        "name": "Reze",
        "class": "Crazy",
        "health": 1065,
        "strength": 245,
        "defense": 90,
        "stamina": 120,
        "critchance": 0.055,
        "critmult": 2.6825,
        "sprite": "reze.webp",
        "sprite_scale": 1.0,
    },
    {
        "name": "Banana Brute",
        "class": "Tank",
        "health": 2000,
        "strength": 375,
        "defense": 140,
        "stamina": 65,
        "critchance": 0.0065,
        "critmult": 5.5,
        "sprite": "bananabrute.webp",
        "sprite_scale": 1.0,
    },
    {
        "name": "Monster Garou",
        "class": "Genius",
        "health": 1575,
        "strength": 230,
        "defense": 115,
        "stamina": 180,
        "critchance": 0.09,
        "critmult": 2.45,
        "sprite": "monstergarou.png",
        "sprite_scale": 1.0,
    },
    {
        "name": "Grimlock",
        "class": "Beast",
        "health": 1100,
        "strength": 300,
        "defense": 45,
        "stamina": 190,
        "critchance": 0.0925,
        "critmult": 1.55,
        "sprite": "grimlock.webp",
        "sprite_scale": 2.0,
    },
    {
        "name": "Dr. Edgar Zomboss",
        "class": "Speical: Z",
        "health": 50000,
        "strength": 1200,
        "defense": 185,
        "stamina": 999999,
        "critchance": 0.0,
        "critmult": 1.0,
        "sprite": "edgar.png",
        "sprite_scale": 2.0,
    },
]

fighters = [f.copy() for f in FIGHTERS]
for fighter in fighters:
    apply_class_modifiers(fighter)
    
df = pd.DataFrame(fighters)
df.to_csv(CSV_PATH, index=False)
print(f"Saved {len(fighters)} fighters to {CSV_PATH}")