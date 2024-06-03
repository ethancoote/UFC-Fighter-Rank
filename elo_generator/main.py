# main file
import stat_scraper
import os

current_path = os.path.dirname(os.path.abspath(__file__))
# results = stat_scraper.init_dataset()
results = stat_scraper.get_event_results("http://www.ufcstats.com/event-details/8fa2b06572365321")

f = open(current_path + "/fighter_data/fighter.data.txt", "w")
for fight in results:
    f.write(f"{fight[0]}-{fight[1]}-{fight[2]}-{fight[3]}-{fight[4]}\n")

