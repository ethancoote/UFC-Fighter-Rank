# temp test file to run other programs
import stat_scraper

#stat_scraper.init_dataset()
results = stat_scraper.get_event_results("http://www.ufcstats.com/event-details/6e4acc2c115215b5")
print(results)
