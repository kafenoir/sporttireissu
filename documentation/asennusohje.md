# Asennusohje

Sovelluksen saa ladattua pakattuna osoitteesta:

https://github.com/kafenoir/sporttireissu/archive/master.zip

Pura pakattu sovellus ja mene terminaalilla sen juurikansioon `sporttireissu-master`.

## Asennus paikallisesti

Luo hakemistoon Python-virtuaaliympäristö komennolla `python3 -m venv venv`

Aktivoi virtuaaliympäristö komennolla `source venv/bin/activate`

Asenna sovelluksen riippuvuudet komennolla `pip install -r requirements.txt`

### Urheilulajien ja taitotasojen lisääminen

Avaa yhteys sovelluksen käyttämään tietokantaan komennolla sqlite3 `application/trips.db`

Urheilulajien lisääminen tapahtuu komennolla:

`INSERT INTO sport(name) VALUES(lajin_nimi)`

ESIM: `INSERT INTO sport(name) VALUES(Juoksu)`

Taitotasojen

`INSERT INTO level(name) VALUES(taitotason_nimi)`

ESIM: `INSERT INTO level(name) VALUES(Aloittelija)`

Kun olet valmis, voit sulkea yhteyden tietokantaan komennolla `.exit`

### Sovelluksen käynnistäminen

Käynnistä sovellus komennolla `python run.py`

Mene selaimella osoitteeseen `http://localhost:5000/`




