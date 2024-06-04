# main file
import stat_scraper
import rank_sim
import os

current_path = os.path.dirname(os.path.abspath(__file__))

def run_init():
    # results = stat_scraper.init_dataset()
    results = stat_scraper.get_event_results("http://www.ufcstats.com/event-details/6420efac0578988b")

    f = open(current_path + "/fighter_data/fighter_data.txt", "w")
    for fight in results:
        f.write(f"{fight[0]}-{fight[1]}-{fight[2]}-{fight[3]}-{fight[4]}\n")

def run_rank_sim():
    rank_sim.rank_sim(current_path + "/fighter_data/fighter_data_test_sample.txt")
    

# run_init()
run_rank_sim()

