
import announce

# you can pass all other arguments as well.
# pass recurrence 60 to run it every hour
from parameters import Country

announce.get(Country=Country.TUNISIE.name, Gouvernorat=Country.TUNISIE.NABEUL.name,
             save=True, with_photos=True, headless=True)

# because no records exist against these arguments on the website.
