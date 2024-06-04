# Takes all UFC fights in order and give each fighter an elo rating
def rank_sim(filename):
    all_fights = get_fights_data(filename)
    print(all_fights)


def get_fights_data(filename):
    all_fights = []
    try:
        f = open(filename, "r")
    except:
        print("File not found...")
        return([])
    
    for line in f:
        fight = line.split("-")
        all_fights.append(fight)

    return all_fights