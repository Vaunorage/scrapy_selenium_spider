from tunisie import announce

# you can pass all other arguments as well.
# pass recurrence 60 to run it every hour
from tunisie.parameters import Country, Sort

announce.get(country=Country.TUNISIE.name, gouvernerat=Country.TUNISIE.NABEUL.name,
             sort=Sort.MODICATION_DT_ASC,
             save=True, with_photos=True, headless=True)

# because no records exist against these arguments on the website.

# %%
