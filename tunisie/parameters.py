import dataclasses
from enum import Enum


@dataclasses.dataclass
class CountryBase:
    pass


@dataclasses.dataclass
class GouverneratBase:
    pass


class Ariana(GouverneratBase):
    name = 'Ariana'

    ARIANAVILLE = 'Ariana Ville'
    ETTADHAMEN = 'Ettadhamen'
    KALAATLANDLOUS = 'Kalaat Landlous'
    LASOUKRA = 'La Soukra'
    MNIHLA = 'Mnihla'
    RAOUED = 'Raoued'
    SIDITHABET = 'Sidi Thabet'


class Beja(GouverneratBase):
    name = 'Beja'

    AMDOUN = 'Amdoun'
    BEJA_NORD = 'Beja Nord'
    BEJA_SUD = 'Beja Sud'
    GOUBELLAT = 'Goubellat'
    MEJEZ_EL_BAB = 'Mejez El Bab'
    NEFZA = 'Nefza'
    TEBOURSOUK = 'Teboursouk'
    TESTOUR = 'Testour'
    THIBAR = 'Thibar'


class BenArous(GouverneratBase):
    name = 'Ben Arous'

    BEN_AROUS = 'Ben Arous'
    BOU_MHEL_EL_BASSATINE = 'Bou Mhel El Bassatine'
    EL_MOUROUJ = 'El Mourouj'
    EZZAHRA = 'Ezzahra'
    FOUCHANA = 'Fouchana'
    HAMMAM_CHATT = 'Hammam Chatt'
    HAMMAM_LIF = 'Hammam Lif'
    MEGRINE = 'Megrine'
    MOHAMADIA = 'Mohamadia'
    MORNAG = 'Mornag'
    NOUVELLE_MEDINA = 'Nouvelle Medina'
    RADES = 'Rades'


class Bizerte(GouverneratBase):
    name = 'Bizerte'

    BIZERTE_NORD = 'Bizerte Nord'
    BIZERTE_SUD = 'Bizerte Sud'
    EL_ALIA = 'El Alia'
    GHAR_EL_MELH = 'Ghar El Melh'
    GHEZALA = 'Ghezala'
    JARZOUNA = 'Jarzouna'
    JOUMINE = 'Joumine'
    MATEUR = 'Mateur'
    MENZEL_BOURGUIBA = 'Menzel Bourguiba'
    MENZEL_JEMIL = 'Menzel Jemil'
    RAS_JEBEL = 'Ras Jebel'
    SEJNANE = 'Sejnane'
    TINJA = 'Tinja'
    UTIQUE = 'Utique'


class Gabes(GouverneratBase):
    name = 'Gabes'

    EL_HAMMA = 'El Hamma'
    EL_METOUIA = 'El Metouia'
    GABES_MEDINA = 'Gabes Medina'
    GABES_OUEST = 'Gabes Ouest'
    GABES_SUD = 'Gabes Sud'
    GHANNOUCHE = 'Ghannouche'
    MARETH = 'Mareth'
    MATMATA = 'Matmata'
    MENZEL_HABIB = 'Menzel Habib'
    NOUVELLE_MATMATA = 'Nouvelle Matmata'


class Gafsa(GouverneratBase):
    name = 'Jendouba'

    BELKHIR = 'Belkhir'
    EL_GUETTAR = 'El Guettar'
    EL_KSAR = 'El Ksar'
    EL_MDHILLA = 'El Mdhilla'
    GAFSA_NORD = 'Gafsa Nord'
    GAFSA_SUD = 'Gafsa Sud'
    METLAOUI = 'Metlaoui'
    MOULARES = 'Moulares'
    REDEYEF = 'Redeyef'
    SIDI_AICH = 'Sidi Aich'
    SNED = 'Sned'


class Jendouba(GouverneratBase):
    name = 'Kairouan'

    AIN_DRAHAM = 'Ain Draham'
    BALTA_BOU_AOUENE = 'Balta Bou Aouene'
    BOU_SALEM = 'Bou Salem'
    FERNANA = 'Fernana'
    GHARDIMAOU = 'Ghardimaou'
    JENDOUBA = 'Jendouba'
    JENDOUBA_NORD = 'Jendouba Nord'
    OUED_MLIZ = 'Oued Mliz'
    TABARKA = 'Tabarka'


class Kairouan(GouverneratBase):
    name = 'Kasserine'

    BOU_HAJLA = 'Bou Hajla'
    CHEBIKA = 'Chebika'
    CHERARDA = 'Cherarda'
    EL_ALA = 'El Ala'
    HAFFOUZ = 'Haffouz'
    HAJEB_EL_AYOUN = 'Hajeb El Ayoun'
    KAIROUAN_NORD = 'Kairouan Nord'
    KAIROUAN_SUD = 'Kairouan Sud'
    NASRALLAH = 'Nasrallah'
    OUESLATIA = 'Oueslatia'
    SBIKHA = 'Sbikha'


class Kasserine(GouverneratBase):
    name = 'Kasserine'

    EL_AYOUN = 'El Ayoun'
    EZZOUHOUR = 'Ezzouhour (Kasserine)'
    FERIANA = 'Feriana'
    FOUSSANA = 'Foussana'
    HAIDRA = 'Haidra'
    HASSI_EL_FRID = 'Hassi El Frid'
    JEDILIANE = 'Jediliane'
    KASSERINE_NORD = 'Kasserine Nord'
    KASSERINE_SUD = 'Kasserine Sud'
    MEJEL_BEL_ABBES = 'Mejel Bel Abbes'
    SBEITLA = 'Sbeitla'
    SBIBA = 'Sbiba'
    THALA = 'Thala'


class Kebili(GouverneratBase):
    name = 'Kebili'

    DOUZ = 'Douz'
    EL_FAOUAR = 'El Faouar'
    KEBILI_NORD = 'Kebili Nord'
    KEBILI_SUD = 'Kebili Sud'
    SOUK_EL_AHAD = 'Souk El Ahad'


class LeKef(GouverneratBase):
    name = 'Le Kef'

    DAHMANI = 'Dahmani'
    EL_KSOUR = 'El Ksour'
    JERISSA = 'Jerissa'
    KALAA_EL_KHASBA = 'Kalaa El Khasba'
    KALAAT_SINANE = 'Kalaat Sinane'
    LE_KEF_EST = 'Le Kef Est'
    LE_KEF_OUEST = 'Le Kef Ouest'
    LE_SERS = 'Le Sers'
    NEBEUR = 'Nebeur'
    SAKIET_SIDI_YOUSSEF = 'Sakiet Sidi Youssef'
    TAJEROUINE = 'Tajerouine'
    TOUIREF = 'Touiref'


class Mahdia(GouverneratBase):
    name = 'Mahdia'

    BOU_MERDES = 'Bou Merdes'
    CHORBANE = 'Chorbane'
    EL_JEM = 'El Jem'
    HBIRA = 'Hbira'
    KSOUR_ESSAF = 'Ksour Essaf'
    LA_CHEBBA = 'La Chebba'
    MAHDIA = 'Mahdia'
    MELLOULECH = 'Melloulech'
    OULED_CHAMAKH = 'Ouled Chamakh'
    SIDI_ALOUENE = 'Sidi Alouene'
    SOUASSI = 'Souassi'


class Manouba(GouverneratBase):
    name = 'Manouba'

    BORJEL_AMRI = 'Borj El Amri'
    DOUAR_HICHER = 'Douar Hicher'
    EL_BATTAN = 'El Battan'
    JEDAIDA = 'Jedaida'
    MANNOUBA = 'Mannouba'
    MORNAGUIA = 'Mornaguia'
    OUED_ELLIL = 'Oued Ellil'
    TEBOURBA = 'Tebourba'


class Medenine(GouverneratBase):
    name = 'Medenine'

    AJIM = 'Ajim'
    BEN_GUERDANE = 'Ben Guerdane'
    BENI_KHEDACHE = 'Beni Khedache'
    DJERBA_HOUMET_ESSOUK = 'Djerba - Houmet Essouk'
    DJERBA_MIDOUN = 'Djerba - Midoun'
    MEDENINE_NORD = 'Medenine Nord'
    MEDENINE_SUD = 'Medenine Sud'
    SIDI_MAKHLOUF = 'Sidi Makhlouf'
    ZARZIS = 'Zarzis'


class Monastir(GouverneratBase):
    name = 'Monastir'

    BEKALTA = 'Bekalta'
    BEMBLA = 'Bembla'
    BENI_HASSEN = 'Beni Hassen'
    JEMMAL = 'Jemmal'
    KSAR_HELAL = 'Ksar Helal'
    KSIBET_EL_MEDIOUNI = 'Ksibet El Mediouni'
    MOKNINE = 'Moknine'
    MONASTIR = 'Monastir'
    OUERDANINE = 'Ouerdanine'
    SAHLINE = 'Sahline'
    SAYADA_LAMTA_BOU_HAJAR = 'Sayada Lamta Bou Hajar'
    TEBOULBA = 'Teboulba'
    ZERAMDINE = 'Zeramdine'


class Nabeul(GouverneratBase):
    name = 'Nabeul'

    BENI_KHALLED = 'Beni Khalled'
    BENI_KHIAR = 'Beni Khiar'
    BOU_ARGOUB = 'Bou Argoub'
    DARCHAABANE_ELFEHRI = 'Dar Chaabane Elfehri'
    EL_HAOUARIA = 'El Haouaria'
    EL_MIDA = 'El Mida'
    GROMBALIA = 'Grombalia'
    HAMMAM_EL_GHEZAZ = 'Hammam El Ghezaz'
    HAMMAMET = 'Hammamet'
    KELIBIA = 'Kelibia'
    KORBA = 'Korba'
    MENZEL_BOUZELFA = 'Menzel Bouzelfa'
    MENZEL_TEMIME = 'Menzel Temime'
    NABEUL = 'Nabeul'
    SOLIMAN = 'Soliman'
    TAKELSA = 'Takelsa'


class Sfax(GouverneratBase):
    name = 'Sfax'

    AGAREB = 'Agareb'
    BIR_ALI_BEN_KHELIFA = 'Bir Ali Ben Khelifa'
    EL_AMRA = 'El Amra'
    EL_HENCHA = 'El Hencha'
    ESSKHIRA = 'Esskhira'
    GHRAIBA = 'Ghraiba'
    JEBENIANA = 'Jebeniana'
    KERKENAH = 'Kerkenah'
    MAHRAS = 'Mahras'
    MENZEL_CHAKER = 'Menzel Chaker'
    SAKIET_EDDAIER = 'Sakiet Eddaier'
    SAKIET_EZZIT = 'Sakiet Ezzit'
    SFAX_EST = 'Sfax Est'
    SFAX_SUD = 'Sfax Sud'
    SFAX_VILLE = 'Sfax Ville'


class SidiBouzid(GouverneratBase):
    name = 'Sidi bouzid'

    BEN_OUN = 'Ben Oun'
    BIR_EL_HAFFEY = 'Bir El Haffey'
    CEBBALA = 'Cebbala'
    JILMA = 'Jilma'
    MAKNASSY = 'Maknassy'
    MENZEL_BOUZAIENE = 'Menzel Bouzaiene'
    MEZZOUNA = 'Mezzouna'
    OULED_HAFFOUZ = 'Ouled Haffouz'
    REGUEB = 'Regueb'
    SIDI_BOUZID_EST = 'Sidi Bouzid Est'
    SIDI_BOUZID_OUEST = 'Sidi Bouzid Ouest'
    SOUK_JEDID = 'Souk Jedid'


class Siliana(GouverneratBase):
    name = 'Siliana'

    BARGOU = 'Bargou'
    BOU_ARADA = 'Bou Arada'
    EL_AROUSSA = 'El Aroussa'
    GAAFOUR = 'Gaafour'
    KESRA = 'Kesra'
    LE_KRIB = 'Le Krib'
    MAKTHAR = 'Makthar'
    ROHIA = 'Rohia'
    SIDI_BOU_ROUIS = 'Sidi Bou Rouis'
    SILIANA_NORD = 'Siliana Nord'
    SILIANA_SUD = 'Siliana Sud'


class Sousse(GouverneratBase):
    name = 'Sousse'

    AKOUDA = 'Akouda'
    BOU_FICHA = 'Bou Ficha'
    ENFIDHA = 'Enfidha'
    HAMMAM_SOUSSE = 'Hammam Sousse'
    HERGLA = 'Hergla'
    KALAA_EL_KEBIRA = 'Kalaa El Kebira'
    KALAA_ESSGHIRA = 'Kalaa Essghira'
    KONDAR = 'Kondar'
    MSAKEN = 'Msaken'
    SIDI_BOU_ALI = 'Sidi Bou Ali'
    SIDI_EL_HENI = 'Sidi El Heni'
    SOUSSE_JAOUHARA = 'Sousse Jaouhara'
    SOUSSE_RIADH = 'Sousse Riadh'
    SOUSSE_VILLE = 'Sousse Ville'


class Tataouine(GouverneratBase):
    name = 'Tataouine'

    BIR_LAHMAR = 'Bir Lahmar'
    DHEHIBA = 'Dhehiba'
    GHOMRASSEN = 'Ghomrassen'
    REMADA = 'Remada'
    SMAR = 'Smar'
    TATAOUINE_NORD = 'Tataouine Nord'
    TATAOUINE_SUD = 'Tataouine Sud'


class Tozeur(GouverneratBase):
    name = 'Tozeur'

    DEGUECHE = 'Degueche'
    HEZOUA = 'Hezoua'
    NEFTA = 'Nefta'
    TAMEGHZA = 'Tameghza'
    TOZEUR = 'Tozeur'


class Tunis(GouverneratBase):
    name = 'Tunis'

    AIN_ZAGHOUAN = 'Ain Zaghouan'
    BAB_BHAR = 'Bab Bhar'
    BAB_SOUIKA = 'Bab Souika'
    CARTHAGE = 'Carthage'
    CITE_EL_KHADRA = 'Cite El Khadra'
    EL_HRAIRIA = 'El Hrairia'
    EL_KABBARIA = 'El Kabbaria'
    EL_KRAM = 'El Kram'
    EL_MENZAH = 'El Menzah'
    EL_OMRANE = 'El Omrane'
    EL_OMRANE_SUPERIEUR = 'El Omrane Superieur'
    EL_OUERDIA = 'El Ouerdia'
    ESSIJOUMI = 'Essijoumi'
    ETTAHRIR = 'Ettahrir'
    EZZOUHOUR_TUNIS = 'Ezzouhour (Tunis)'
    JEBEL_JELLOUD = 'Jebel Jelloud'
    LA_GOULETTE = 'La Goulette'
    LA_MARSA = 'La Marsa'
    LA_MEDINA = 'La Medina'
    LE_BARDO = 'Le Bardo'
    SIDI_EL_BECHIR = 'Sidi El Bechir'
    SIDI_HASSINE = 'Sidi Hassine'


class Zaghouan(GouverneratBase):
    name = 'Zaghouan'

    BIR_MCHERGA = 'Bir Mcherga'
    EL_FAHS = 'El Fahs'
    ENNADHOUR = 'Ennadhour'
    HAMMAM_ZRIBA = 'Hammam Zriba'
    SAOUEF = 'Saouef'
    ZAGHOUAN = 'Zaghouan'


class Tunisie(CountryBase):
    name = 'Tunisie'

    ARIANA: Ariana = Ariana
    BEJA: Beja = Beja
    BENAROUS: BenArous = BenArous
    BIZERTE: Bizerte = Bizerte
    GABES: Gabes = Gabes
    GAFSA: Gafsa = Gafsa
    JENDOUBA: Jendouba = Jendouba
    KAIROUAN: Kairouan = Kairouan
    KASSERINE: Kasserine = Kasserine
    KEBILI: Kebili = Kebili
    LEKEF: LeKef = LeKef
    MAHDIA: Mahdia = Mahdia
    MANOUBA: Manouba = Manouba
    MEDENINE: Medenine = Medenine
    MONASTIR: Monastir = Monastir
    NABEUL: Nabeul = Nabeul
    SFAX: Sfax = Sfax
    SIDIBOUZID: SidiBouzid = SidiBouzid
    SILIANA: Siliana = Siliana
    SOUSSE: Sousse = Sousse
    TATAOUINE: Tataouine = Tataouine
    TOZEUR: Tozeur = Tozeur
    TUNIS: Tunis = Tunis
    ZAGHOUAN: Zaghouan = Zaghouan


@dataclasses.dataclass
class Country:
    ALGERIE = 'Algerie'
    BELGIQUE = 'Belgique'
    CANADA = 'Canada'
    FRANCE = 'France'
    MAROC = 'Maroc'
    SENEGAL = 'Senegal'
    TUNISIE: Tunisie = Tunisie


class Localite(Enum):
    pass


class Nature(Enum):
    LOCATION = 'Location'
    VENTE = 'Vente'
    TERRAIN = 'Terrain'
    LOCATION_VACANCES = 'Location Vacances'
    BUREAUX_COMMERCES = 'Bureaux & Commerces'
    PARTAGE = 'Partage'


class Rubrique(Enum):
    OFFRES = 'Offres'
    DEMANDES = 'Demandes'


class Type(Enum):
    pass


@dataclasses.dataclass
class Sort:
    PRICE_ASC = "Prix de - à +"
    PRICE_DSC = "Prix de + à -"
    PUBLICATION_DT_ASC = "Publiée de - à +"
    PUBLICATION_DT_DSC = "Publiée de + à -"
    MODICATION_DT_ASC = "Modifiée de - à +"
    MODICATION_DT_DSC = "Modifiée de + à -"
