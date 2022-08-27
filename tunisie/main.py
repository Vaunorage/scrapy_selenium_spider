from tunisie import announce

# you can pass all other arguments as well.
# pass recurrence 60 to run it every hour
from tunisie.parameters import Country

announce.get(country=Country.TUNISIE.name, gouvernerat=Country.TUNISIE.NABEUL.name,
             save=True, with_photos=True, headless=True)

# because no records exist against these arguments on the website.

# %%
