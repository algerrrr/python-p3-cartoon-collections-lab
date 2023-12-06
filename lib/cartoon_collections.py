def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        print(f"{num}. {dwarf}")
        num += 1
    return

def summon_captain_planet(elems):
    summon = []
    for elem in elems:
        summon.append(f"{elem.title()}!")
    return summon

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True

    return False

def find_the_cheese(calls):
    for call in calls:
        if call == "cheddar":
            return call
    
