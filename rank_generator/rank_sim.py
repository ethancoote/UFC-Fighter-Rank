# Takes all UFC fights in order and give each fighter an elo rating
def rank_sim(fight_list_filename, fighter_rank_filename):
    all_fights = get_fights_data(fight_list_filename)
    all_ranks = get_ranks_data(fighter_rank_filename)
    # update_ranks(all_fights, all_ranks)

def get_fights_data(filename):
    all_data = []
    try:
        f = open(filename, "r")
    except:
        print("File not found...")
        return([])
    
    for line in f:
        line = line.strip()
        split_line = line.split("-")
        all_data.append(split_line)

    return all_data

def get_ranks_data(filename):
    all_data = {}
    try:
        f = open(filename, "r")
    except:
        print("File not found...")
        return({})
    
    for line in f:
        line = line.strip()
        split_line = line.split("-")
        name = split_line[0]
        split_line.pop(0)
        all_data[name] = split_line

    return all_data



#def update_ranks(all_fights, all_ranks):
#    for fight in all_fights: