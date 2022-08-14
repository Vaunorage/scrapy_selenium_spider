
import announce

# you can pass all other arguments as well. 
# pass recurrence 60 to run it every hour
announce.get(Country='Tunisie',Gouvernorat='Beja',save=False,with_photos=True,headless=True)

# because no records exist against these arguments on the website.
