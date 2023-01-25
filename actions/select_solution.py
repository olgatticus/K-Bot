import random 

def find_solutions(solutions, group, valence, energy, danceability):

    if group != "none":
        solutions = [s for s in solutions if (s["group"] == group)]

    # Filter out solutions that do not satisfy the given constraints
    sol1 = [s for s in solutions if (s["variables"]["valence"] == valence or valence == "all")]
    sol2 = [s for s in solutions if (s["variables"]["energy"] == energy or energy == "all")]
    sol3 = [s for s in solutions if (s["variables"]["danceability"] == danceability or danceability == "all")]

    set1 = {(s["name"], s["group"]) for s in sol1}
    set2 = {(s["name"], s["group"]) for s in sol2}
    set3 = {(s["name"], s["group"]) for s in sol3}

    common_elements = find_common_elements(set1, set2, set3)
    if not common_elements:
        return set1
    return common_elements

def find_common_elements(set1, set2, set3):
   
    # Find the intersection of the three sets
    common_elements = set1 & set2 & set3
    
    # If the intersection is not empty, return it
    if common_elements:
        return common_elements
    
    # Otherwise, find the intersection of the two sets with the largest overlap
    if set1 & set2:
        return set1 & set2
    if set1 & set3:
        return set1 & set3
    if set2 & set3:
        return set2 & set3
    
    # If there is no overlap between any pairs of sets, return the empty set
    return set()


songs_solutions = [
    {"name": "Butter", "group": "BTS", "variables": {"valence": "high", "energy": "middle", "danceability": "high"}},
    {"name": "Permission to Dance", "group": "BTS", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Fake Love", "group": "BTS", "variables": {"valence": "low", "energy": "middle", "danceability": "medium"}},
    {"name": "DNA", "group": "BTS", "variables": {"valence": "medium", "energy": "middle", "danceability": "high"}},
    {"name": "Mic Drop", "group": "BTS", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "HOME", "group": "BTS", "variables": {"valence": "high", "energy": "middle", "danceability": "high"}},
    {"name": "Spring day", "group": "BTS", "variables": {"valence": "low", "energy": "low", "danceability": "low"}},
    {"name": "Intro:Persona", "group": "BTS", "variables": {"valence": "high", "energy": "high", "danceability": "middle"}},
    {"name": "Butter", "group": "BTS", "variables": {"valence": "high", "energy": "middle", "danceability": "high"}},
    {"name": "Run Bts", "group": "BTS", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Outro:Tear", "group": "BTS", "variables": {"valence": "low", "energy": "middle", "danceability": "low"}},
    {"name": "Pied piper", "group": "BTS", "variables": {"valence": "high", "energy": "middle", "danceability": "high"}},
    {"name": "Dimple", "group": "BTS", "variables": {"valence": "high", "energy": "middle", "danceability": "low"}},
    {"name": "Friends", "group": "BTS", "variables": {"valence": "high", "energy": "low", "danceability": "low"}},
    {"name": "UGH!", "group": "BTS", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "Hot Sauce", "group": "NCT", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Hello Future", "group": "NCT", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Life is Still Going On", "group": "NCT", "variables": {"valence": "low", "energy": "medium", "danceability": "low"}},
    {"name": "Beatbox", "group": "NCT", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Arcade", "group": "NCT", "variables": {"valence": "low", "energy": "high", "danceability": "medium"}},
    {"name": "Life is Still Going On", "group": "NCT", "variables": {"valence": "low", "energy": "medium", "danceability": "low"}},
    {"name": "Arcade", "group": "NCT", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "Chewing Gum", "group": "NCT", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "2 Baddies", "group": "NCT", "variables": {"valence": "low", "energy": "high", "danceability": "medium"}},
    {"name": "Limitless", "group": "NCT", "variables": {"valence": "medium", "energy": "medium", "danceability": "medium"}},
    {"name": "Angel", "group": "NCT", "variables": {"valence": "high", "energy": "low", "danceability": "medium"}},
    {"name": "Good Thing", "group": "NCT", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "MAD DOG", "group": "NCT", "variables": {"valence": "low", "energy": "high", "danceability": "low"}},
    {"name": "Fire Truck", "group": "NCT", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "Favorite", "group": "NCT", "variables": {"valence": "medium", "energy": "medium", "danceability": "high"}},
    {"name": "Sticker", "group": "NCT", "variables": {"valence": "medium", "energy": "high", "danceability": "medium"}},
    {"name": "Cherry Bomb", "group": "NCT", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Kick it", "group": "NCT", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "Road Trip", "group": "NCT", "variables": {"valence": "high", "energy": "low", "danceability": "low"}},
    {"name": "Paradise", "group": "NCT", "variables": {"valence": "high", "energy": "low", "danceability": "low"}},
    {"name": "Faster", "group": "NCT", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "No Rules", "group": "TXT", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Cat & Dog", "group": "TXT", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Magic", "group": "TXT", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Opening Sequence", "group": "TXT", "variables": {"valence": "low", "energy": "medium", "danceability": "low"}},
    {"name": "Good Boy Gone Mad", "group": "TXT", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "Blue Hour", "group": "TXT", "variables": {"valence": "high", "energy": "high", "danceability": "medium"}},
    {"name": "Loser Lover", "group": "TXT", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Anti Romantic", "group": "TXT", "variables": {"valence": "low", "energy": "low", "danceability": "low"}},
    {"name": "Thursday's Child Has Far To Go", "group": "TXT", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "2 minus 1", "group": "Seventeen", "variables": {"valence": "medium", "energy": "medium", "danceability": "high"}},
    {"name": "Anyone", "group": "Seventeen", "variables": {"valence": "low", "energy": "medium", "danceability": "medium"}},
    {"name": "Boomboom", "group": "Seventeen", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "HOME;RUN", "group": "Seventeen", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Pretty U", "group": "Seventeen", "variables": {"valence": "high", "energy": "medium", "danceability": "low"}},
    {"name": "Left & Right", "group": "Seventeen", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Snapshoot", "group": "Seventeen", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "VERY NICE", "group": "Seventeen", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "CLAP", "group": "Seventeen", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Mansae", "group": "Seventeen", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Adore U", "group": "Seventeen", "variables": {"valence": "high", "energy": "high", "danceability": "medium"}},
    {"name": "Trauma", "group": "Seventeen", "variables": {"valence": "low", "energy": "low", "danceability": "low"}},
    {"name": "MY I", "group": "Seventeen", "variables": {"valence": "low", "energy": "medium", "danceability": "low"}},
    {"name": "Flower", "group": "Seventeen", "variables": {"valence": "low", "energy": "medium", "danceability": "low"}},
    {"name": "HOT", "group": "Seventeen", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "Maniac", "group": "Stray Kids", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "Maknae on Top", "group": "Stray Kids", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "FAM", "group": "Stray Kids", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Case 143", "group": "Stray Kids", "variables": {"valence": "high", "energy": "medium", "danceability": "medium"}},
    {"name": "Slump", "group": "Stray Kids", "variables": {"valence": "low", "energy": "low", "danceability": "low"}},
    {"name": "God's Menu", "group": "Stray Kids", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "TA", "group": "Stray Kids", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "MIROH", "group": "Stray Kids", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Boxer", "group": "Stray Kids", "variables": {"valence": "high", "energy": "medium", "danceability": "low"}},
    {"name": "Christmas EveL", "group": "Stray Kids", "variables": {"valence": "medium", "energy": "medium", "danceability": "medium"}},
    {"name": "N/S", "group": "Stray Kids", "variables": {"valence": "high", "energy": "medium", "danceability": "high"}},
    {"name": "Domino", "group": "Stray Kids", "variables": {"valence": "low", "energy": "high", "danceability": "high"}},
    {"name": "Shutdown", "group": "Blackpink", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Boombayah", "group": "Blackpink", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "DDU-DU DDU-DU", "group": "Blackpink", "variables": {"valence": "low", "energy": "medium", "danceability": "medium"}},
    {"name": "How You Like That", "group": "Blackpink", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Whistle", "group": "Blackpink", "variables": {"valence": "high", "energy": "low", "danceability": "low"}},
    {"name": "Love shot", "group": "EXO", "variables": {"valence": "medium", "energy": "medium", "danceability": "medium"}},
    {"name": "Call Me Baby", "group": "EXO", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Monster", "group": "EXO", "variables": {"valence": "low", "energy": "medium", "danceability": "medium"}},
    {"name": "Lotto", "group": "EXO", "variables": {"valence": "medium", "energy": "high", "danceability": "high"}},
    {"name": "Growl", "group": "EXO", "variables": {"valence": "low", "energy": "low", "danceability": "low"}},
    {"name": "Power", "group": "EXO", "variables": {"valence": "high", "energy": "high", "danceability": "high"}},
    {"name": "Telephone", "group": "EXO", "variables": {"valence": "high", "energy": "low", "danceability": "low"}},
]

