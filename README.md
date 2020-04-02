# Sporttireissu

## Kuvaus

Ohjelman avulla voi järjestää ja osallistua urheilumatkoille. Käyttäjä voi toimia sekä matkanjärjestäjänä että osallistujana. Käyttäjäprofiilissa ilmoitetaan harrastetut lajit sekä taitotaso kyseisissä lajeissa. Järjestäminen tapahtuu luomalla matka, jolle määritellään nimi, paikka, alkamis- ja päättymispäivät, hinta, kuvaus viimeinen ilmoittautumispäivä sekä enimmäisosallistujamäärä. Lisäksi jokaiseen matkaan liittyy yksi tai useampi urheilulaji sekä yksi tai useampi vaatimustaso. Käyttäjät voivat hakea luotuja matkoja niiden attribuuttien perusteella sekä ilmoittautua haluamilleen matkoille. Ajankohdaltaan päällekkäisille matkoille ei voi osallistua. Omaa ilmoitettua taitotasoa vastaamattomille matkoille on mahdollista osallistua, mutta ohjelma varoittaa käyttäjää tässä tapauksessa. Järjestäjä näkee listan hänen matkalleen ilmoittautuneista.

## Toimintoja

* Kirjautuminen
* Julkinen käyttäjäprofiili
* Matkan luominen ja peruutus
* Matkatarjonnan katselu eri rajauksilla
* Matkalle ilmoittautuminen (ja peruminen)
* Ilmoittautuneiden luettelo

Mahdollisia lisätoimintoja (jos aikaa)

* Osallistumiskutsun lähettäminen tietyn taitotason käyttäjille
* Laskun lähettäminen ilmoittautuneille

## Käyttäjätapaukset

Pyöräilyvalmentaja haluaa järjestää viikonlopun kestävän pyöräilyreissun Porvooseen. Sporttireissu-tunnuksellaan hän voi helposti luoda matkan, joka näkyy kaikille palvelun käyttäjille. Ajankohdan lisäksi hän voi määrittää matkalla hinnan sekä maksimiosallistujamäärän. Hän voi myös määrittää, että reissu on tarkoitettu vain aloitteleville pyöräilijöille.

Aloitteleva pyöräilijä etsii edullista viikonlopun kestävää pyöräilyreissua rennoissa merkeissä. Sporttireissu-tunnuksellaan hän voi hakea itselleen sopivaan ajankohtaan sijoittuvaa pyöräilyreissua, joka on nimenomaan aloittelijoille suunnattu. Haulleen hän voi määrittää myös hintahaitarin. Jos kyseisenlainen matka löytyy ja ilmoittautumiskiintiö ei ole täysi, hän voi ilmoittautua matkalle.

## Tietokantakaavio

![Tietokantakaavio](https://github.com/kafenoir/sporttireissu/blob/master/documentation/images/sporttireissu_tkk.png)

## Heroku

https://sporttireissu.herokuapp.com/

### Testitunnukset

käyttäjänimi: teppot
salasana: portableram
