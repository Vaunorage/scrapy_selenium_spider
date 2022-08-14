
import announce

# you can pass all other arguments as well. 
# pass recurrence 60 to run it every hour
announce.get(Country='Tunisie',Gouvernorat='Beja',price_min=500, price_max=600,save=False,with_photos=True,headless=False)

# will run every 1 min. just for demo.