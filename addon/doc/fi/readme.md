# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa sisältää kokoelman sovellusmoduuleja Windows 10:n mukana
tuleville sovelluksille sekä korjauksia tietyille säätimille.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Hälytykset ja kello
* Kalenteri
* Laskin (moderni)
* Cortana
* Groove Music
* Sähköposti
* Kartat
* Microsoft Edge
* Asetukset (järjestelmän asetukset, Windows+I).
* Skypen esiversio
* Kauppa
* Sää
* Windows Defender -tietoturvakeskus (Creators Update ja uudemmat)
* Sekalaisia moduuleita sellaisille säätimille kuin Käynnistä-valikon
  tiilet.

Huom: Tämä lisäosa edellyttää Windows 10:n versiota 1511 (koontiversio
10586) tai uudempaa ja NVDA 2016.4:ää tai uudempaa. Käytä parhaiden tulosten
varmistamiseksi viimeisintä vakaata koontiversiota (14393) sekä viimeisintä
vakaata NVDA:n versiota.

## Yleistä

* Alavalikot tunnistetaan oikein Käynnistä-valikon tiilien pikavalikoissa.
* Ikkunoita pienennettäessä (Windows+M) ei enää sanota "ruutu"
  (havaittavissa Insider-esiversioita käytettäessä).
* Tietyt valintaikkunat tunnistetaan nyt oikeiksi
  valintaikkunoiksi. Tällaisia ovat esim. Insider-esiversioiden
  valintaikkuna (Asetukset-sovelluksessa) sekä uudentyylinen Käyttäjätilien
  valvonnan valintaikkuna koontiversiossa 14328 ja uudemmissa NVDA
  2016.2.1:ssä tai vanhemmassa.
* Tiettyjen hakukenttien ehdotusten ilmestyminen/sulkeutuminen (varsinkin
  Asetukset- ja Kauppa-sovelluksessa) ilmaistaan nyt äänimerkeillä ja
  pistekirjoituksella. Tämä koskee myös Käynnistä-valikon hakukenttää.
* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa. Tätä toimintoa hallitaan "Lue objektien sijaintitiedot"
  -asetuksella Objektien lukuasetukset -valintaikkunasta.
* Sijaintitietoja (esim. 1 / 2) ei enää lueta tietyissä pikavalikoissa
  (kuten Edgessä).
* Seuraavat UIA-tapahtumat tunnistetaan: Ohjain kohteelle, aktiivinen alue
  muuttunut (nimenmuutostapahtuman käsittelemänä).
* Lisätty lisäosan päivitysmahdollisuus (automaattinen tai manuaalinen)
  NVDA:n Asetukset-valikosta löytyvän uuden Windows 10 App Essentials
  -valintaikkunan kautta. Vakaat ja kehitysversiot suorittavat oletuksena
  automaattisen päivitystarkistuksen viikoittain tai päivittäin.
* Mahdollisuus Universal Windows Platform (UWP) -sovelluksista tulevien
  tapahtumien seuraamiseen, mikäli NVDA:ta käytetään
  virheenkorjaus-lokitasolla (2017.1 tai uudempi).

## Hälytykset ja kello

* Ajanvalitsimen arvot puhutaan - havaittavissa siirrettäessä kohdistusta
  valitsimen säätimiin. Tämä vaikuttaa myös säätimeen, jolla valitaan,
  milloin Windows käynnistetään uudelleen päivitysten asentamisen
  viimeistelemiseksi.

## Laskin

* NVDA ilmoittaa laskutoimituksen tuloksen Enter-näppäintä painettaessa.

## Kalenteri

* NVDA ei sano enää "muokattava" tai "vain luku" viestisisällössä ja muissa
  kentissä.

## Cortana

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa
  (mikäli näin ei ole, avaa Käynnistä-valikko uudelleen ja yritä hakua
  toistamiseen).
* NVDA on hiljaa puhuessasi Cortanalle mikrofonin välityksellä.
* NVDA puhuu nyt vahvistuksen muistutusta lisättäessä.

## Groove Music

* Ehdotusten ilmestyminen havaitaan nyt kappaleita etsittäessä.

## Sähköposti

* Voit nyt käyttää viestiluettelon kohteita tarkastellessasi
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen.

## Kartat

* NVDA soittaa äänimerkin karttasijainneille.
* NVDA ilmoittaa katuosoitteet käyttäessäsi nuolinäppäimiä kartalla
  liikkumiseen oltaessa street side -näkymässä ja mikäli "use keyboard"
  -vaihtoehto on otettu käyttöön.

## Microsoft Edge

* Ilmoitukset, kuten tiedostojen lataukset, luetaan.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  puhutaan nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* Mikäli asetusten etsiminen kestää jonkin aikaa, NVDA ilmoittaa "etsitään"
  sekä hakutulosten tilan, kuten sen, jos asetusta ei löydy.
* Asetusryhmät tunnistetaan säätimien välillä liikuttaessa
  objektinavigointia käyttäen.
* NVDA ei enää epäonnistu joidenkin yhdistelmäruutujen selitteiden
  tunnistamisessa ja/tai arvomuutosten ilmoittamisessa.

## Skypen esiversio

* Kirjoitusilmaisimen teksti puhutaan kuten Skypen työpöytäversiossa.
* Osittainen Control+NVDA+numero-komentojen paluu tuoreen
  keskusteluhistorian lukemiseen sekä navigointiobjektin siirtämiseen
  keskustelukohteisiin kuten Skypen työpöytäversiossa.
* Voit painaa nyt Alt+numerorivin numeroita etsiäksesi kontaktiluettelon
  (1), keskustelut (2) ja keskustelumuokkauskentän (3) sekä siirtyäksesi
  niihin. Huomaa, että nämä välilehdet on aktivoitava haluttuun osioon
  siirtymiseksi.
* Marraskuussa 2016 julkaistun Skype-sovelluksen esiversion
  yhdistelmäruutujen selitteet puhutaan.
* NVDA ei enää sano "Skype-viesti" useimmissa tapauksissa viestejä
  tarkasteltaessa.

## Kauppa

* Sovellusten nimet näytetään oikein päivitettävien sovellusten luettelossa
  päivitystarkistuksen jälkeen.
* Hakutulosehdotusten ilmestyminen ilmoitetaan.
* NVDA ilmoittaa tuotteen nimen ja latauksen edistymisen sisältöä, kuten
  sovelluksia ja elokuvia, ladattaessa.

## Sää

* Sellaiset välilehdet kuten "ennuste" ja "kartat" tunnistetaan oikeiksi
  välilehdiksi (korjauksen tehnyt Derek Riemer).
* Käytä ennustetta lukiessasi vasenta ja oikeaa nuolta kohteiden välillä
  liikkumiseen. Käytä nuolta ylös ja alas yksittäisten kohteiden
  lukemiseen. Esim.  oikeaa nuolta painettaessa saatetaan sanoa "Maanantai:
  26,1 astetta, puolipilvistä, ...", ja nuolta alas painettaessa
  "Maanantai". Uudelleen painaminen lukee seuraavan kohteen (kuten
  lämpötilan). Toimii tällä hetkellä päivittäisiin ja tunnin välein
  tehtäviin ennusteisiin.

## Windows Defender -tietoturvakeskus

* Painikkeiden selitteet puhutaan.
* Windows Defender -tietoturvakeskus (universaali sovellus) sisältyy
  koontiversioon 14986 ja sitä uudempiin, ja tämän lisäosan tuki
  ko. sovellukselle voi muuttua.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
