# url = 'http://www.tunisie-annonce.com/AnnoncesImmobilier.asp?rech_cod_cat=1&rech_cod_rub=&rech_cod_typ=&rech_cod_sou_typ=&rech_cod_pay=TN&rech_cod_reg=102&rech_cod_vil=10204&rech_cod_loc=&rech_prix_min=&rech_prix_max=&rech_surf_min=&rech_surf_max=&rech_age=&rech_photo=&rech_typ_cli=&rech_order_by=31&rech_page_num=1'
# from urllib.parse import parse_qs,urlparse

# q = urlparse(url)
# q_dict = parse_qs(q.query)
# page = q_dict.get("rech_page_num")[0]
# print(page)
# import re

# # raw = re.search("(?:\[)(.*)(?:\])",'[Réf:3103437] Appartement parking residence gardée à nord hilton').group().split()
# # ref = "".join([l for l in raw if l.isdigit()])
# # print(ref)
# raw = re.search("\s[A-Z a-z].*","[Réf:3103437] Appartement parking residence gardée à nord hilton").group().strip()
# print(raw)

# import os
# p = os.path.exists('firefoxdriver/geckodriver')
# print(p)