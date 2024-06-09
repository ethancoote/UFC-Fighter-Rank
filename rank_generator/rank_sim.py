# Takes all UFC fights in order and give each fighter a ranking
import os

peak_rank = ['0', '']
current_path = os.path.dirname(os.path.abspath(__file__))

def rank_sim(fight_list_filename, fighter_rank_filename):
    ordered_list = []
    all_fights = get_fights_data(fight_list_filename)
    all_ranks = get_ranks_data(fighter_rank_filename)
    get_stats(current_path + "/rank_data/rank_data.txt")
    # get_ordered_list(current_path + "/rank_data/ordered_list.txt")
    all_ranks = update_ranks(all_fights, all_ranks)
    ordered_list = init_list_from_dict(ordered_list, all_ranks)
    ordered_list = set_ordered_list(ordered_list)
    save_data(ordered_list)
    # print(all_ranks)
    # print(peak_rank)

def get_fights_data(filename):
    all_data = []
    try:
        f = open(filename, "r")
    except:
        print("File not found...")
        return([])
    
    for line in f:
        line = line.strip()
        split_line = line.split("---")
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
        split_line = line.split("---")
        name = split_line[0]
        split_line.pop(0)
        all_data[name] = split_line
    
    f.close()
    return all_data

def get_stats(filename):
    try:
        f = open(filename, "r")
    except:
        print("File not found...")
        return -1
    
    for line in f:
        line = line.strip()
        split_line = line.split("1")
        if split_line[0] == "Peak":
            peak_rank[0] = split_line[1]
            peak_rank[1] = split_line[2]

    f.close()
    return 0

def get_ordered_list(filename):
    ordered_list = []
    try:
        f = open(filename, "r")
    except:
        print("File not found...")
        return -1
    
    for line in f:
        line = line.strip()
        split_line = line.split("---")
        ordered_list.append(split_line)
    
    return ordered_list

def update_ranks(all_fights, all_ranks):
    k = 64 # this is arbitrary, and can be changed
    for fight in reversed(all_fights):
        # fight[3] is not needed (result of opponent, which can be determined by result of the fighter_one)
        fighter_one = fight[0]
        fight_result = fight[1]
        fighter_two = fight[2]
        weight_class = fight[4]

        # checking if fighter has already fought
        if fighter_one in all_ranks:
            fighter_one_data = all_ranks.get(fighter_one)
            if not weight_class in fighter_one_data:
                fighter_one_data.append(weight_class)
        else:
            # fighter_one_pos = update_ordered_list_position(-1, 1000, fighter_one)
            fighter_one_data = ["1000", weight_class]
            all_ranks[fighter_one] = fighter_one_data

        if fighter_two in all_ranks:
            fighter_two_data = all_ranks.get(fighter_two)
            if not weight_class in fighter_two_data:
                fighter_two_data.append(weight_class)
        else:
            # fighter_two_pos = update_ordered_list_position(-1, 1000, fighter_two)
            fighter_two_data = ["1000", weight_class]
            all_ranks[fighter_two] = fighter_two_data

        # rank change formula
        fighter_one_win_prob = round(1 / (1 + (10 ** ((int(fighter_two_data[0]) - int(fighter_one_data[0])) / 400))), 2)
        fighter_two_win_prob = round(1 / (1 + (10 ** ((int(fighter_one_data[0]) - int(fighter_two_data[0])) / 400))), 2)

        if fight_result == "WIN":
            fighter_one_new_rank = int(fighter_one_data[0]) + (k * (1 - fighter_one_win_prob))
            fighter_two_new_rank = int(fighter_two_data[0]) + (k * (0 - fighter_two_win_prob))
        elif fight_result == "DRAW":
            fighter_one_new_rank = int(fighter_one_data[0]) + (k * (0.5 - fighter_one_win_prob))
            fighter_two_new_rank = int(fighter_two_data[0]) + (k * (0.5 - fighter_two_win_prob))
        else:
            fighter_one_new_rank = int(fighter_one_data[0])
            fighter_two_new_rank = int(fighter_two_data[0])

        fighter_one_new_rank = round(fighter_one_new_rank)
        fighter_two_new_rank = round(fighter_two_new_rank)

        all_ranks[fighter_one][0] = str(fighter_one_new_rank)
        all_ranks[fighter_two][0] = str(fighter_two_new_rank)

        # updating rank peak
        if fighter_one_new_rank > int(peak_rank[0]):
            peak_rank[0] = str(fighter_one_new_rank)
            peak_rank[1] = fighter_one

    return all_ranks

def set_ordered_list(list):
    low = 0
    high = len(list) - 1
    list = quick_sort(list, low, high)
    return list

def partition(list, low, high):
    pivot = int(list[high][1])
    i = low - 1
    for j in range(low, high):
        if int(list[j][1]) < pivot:
            i = i + 1
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    
    i = i + 1
    temp = list[i]
    list[i] = list[high]
    list[high] = temp

    return i, list

def quick_sort(list, low, high):
    if low < high:
        pi, list = partition(list, low, high)

        list = quick_sort(list, low, pi - 1)

        list = quick_sort(list, pi + 1, high)

    return list

def init_list_from_dict(list, dict):
    for item in dict:
        list.append([item, dict[item][0]])

    return list

def save_data(ordered_list):
    f = open(current_path + "/rank_data/rank_data.txt", "w")
    f.write(f"Peak---{peak_rank[0]}---{peak_rank[1]}")
    f.close()

    f = open(current_path + "/rank_data/ordered_list.txt", "w")
    for fighter in reversed(ordered_list):
        f.write(f"{fighter[0]}---{fighter[1]}\n")

    f.close()

