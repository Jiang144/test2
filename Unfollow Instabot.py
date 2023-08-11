from instabot import Bot
#import os 
#import glob
#cookie_del = glob.glob("config/*cookie.json")
#os.remove(cookie_del[0])
bot = Bot(unfollow_delay=2, max_unfollows_per_day=1000)
bot.login(username= "tyrantmonocle", password="PURPLE992599")
bot.unfollow_non_followers()
