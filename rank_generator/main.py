# main file
import stat_scraper
import rank_sim
import os

current_path = os.path.dirname(os.path.abspath(__file__))

def run_init():
    # results = stat_scraper.init_dataset()
    results = stat_scraper.get_event_results("http://ufcstats.com/event-details/c11036da9162cb5f")

    # write new fights to temp file
    f = open(current_path + "/fighter_data/fighter_data.txt", "w")
    for fight in results:
        f.write(f"{fight[0]}---{fight[1]}---{fight[2]}---{fight[3]}---{fight[4]}\n")

    # read data from all previously saved fights
    f2 = open(current_path + "/fighter_data/fighter_data_saved.txt", "r")

    f.write(f2.read())

    f.close()
    f2.close()

    # rename file and remove temp file
    os.remove(current_path + "/fighter_data/fighter_data_saved.txt")
    os.rename(current_path + "/fighter_data/fighter_data.txt", current_path + "/fighter_data/fighter_data_saved.txt")


def run_rank_sim():
    rank_sim.rank_sim(current_path + "/fighter_data/fighter_data_saved.txt", current_path + "/rank_data/fighter_rank.txt")
    

run_init()
#run_rank_sim()

