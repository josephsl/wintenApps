# Windows 10:n keskeiset sovellukset #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa sisältää kokoelman sovellusmoduuleja Windows 10:n mukana
tuleville sovelluksille sekä korjauksia tietyille säätimille.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Hälytykset ja kello
* Bank of America
* Kalenteri
* Laskin (moderni)
* Cortana
* Sähköposti
* Kartat
* Microsoft Edge
* Asetukset (järjestelmän asetukset, Windows+I).
* Skypen esiversio
* Kauppa
* Twitter
* TeamViewer Touch
* Sää
* Sekalaisia moduuleita sellaisille säätimille kuin Käynnistä-valikon
  tiilet.

Huom: Tämä lisäosa edellyttää Windows 10:n versiota 1507 (koontiversio
10240) tai uudempaa ja NVDA:n 2016.3-versiota tai uudempaa. Käytä parhaiden
tulosten saamiseksi viimeisintä vakaata koontiversiota (14393).

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
  Asetukset-sovelluksessa) ilmaistaan nyt äänimerkeillä ja/tai
  pistekirjoituksella.
* Sijaintitietoja (esim. 1 / 2) ei enää lueta tietyissä pikavalikoissa
  (kuten Edgessä).
* Seuraavat UIA-tapahtumat tunnistetaan: Ohjain kohteelle, aktiivinen alue
  muuttunut (nimenmuutostapahtuman käsittelemänä).

## Hälytykset ja kello

* Ajanvalitsimen arvot luetaan. Tämä vaikuttaa myös säätimeen, josta
  valitaan, milloin Windows käynnistetään uudelleen päivitysten asennuksen
  viimeistelemiseksi.

## Kalenteri ja Sähköposti

* NVDA ei enää ilmoita "vain luku" Kalenterissa tapaamisen aiheen kohdalla
  ja Sähköpostin viestisisällössä.

## Laskin

* NVDA ilmoittaa laskutoimituksen tuloksen Enter-näppäintä painettaessa.

## Cortana

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa
  (mikäli näin ei ole, avaa Käynnistä-valikko uudelleen ja yritä hakua
  toistamiseen).
* NVDA on hiljaa puhuessasi Cortanalle mikrofonin välityksellä.
* NVDA puhuu nyt vahvistuksen muistutusta lisättäessä.

## Sähköposti ja kalenteri

* NVDA ei enää ilmoita "muokattava" tai "vain luku" viestisisällössä ja
  muissa kentissä.

## Kartat

* NVDA soittaa äänimerkin karttasijainneille.

## Microsoft Edge

* Ilmoitukset, kuten tiedostojen lataukset, luetaan.
* Huomaa, että yleistuki on tällä hetkellä kokeellinen (Edgeä ei tulisi
  käyttää vielä vähään aikaan ensisijaisena selaimena).

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  puhutaan nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* Mikäli asetusten etsiminen kestää jonkin aikaa, NVDA ilmoittaa "etsitään"
  sekä hakutulosten tilan, kuten sen, jos asetusta ei löydy.

## Skypen esiversio

* Kirjoitusilmaisimen teksti puhutaan kuten Skypen työpöytäversiossa.
* Osittainen Control+NVDA+numero-komentojen paluu tuoreen
  keskusteluhistorian lukemiseen sekä navigointiobjektin siirtämiseen
  keskustelukohteisiin kuten Skypen työpöytäversiossa.
* Voit painaa nyt Alt+numerorivin numeroita etsiäksesi kontaktiluettelon
  (1), keskustelut (2) ja keskustelumuokkauskentän (3) sekä siirtyäksesi
  niihin. Huomaa, että nämä välilehdet on aktivoitava haluttuun osioon
  siirtymiseksi.

## Kauppa

* Sovellusten nimet näytetään oikein päivitettävien sovellusten luettelossa
  päivitystarkistuksen jälkeen.

## TeamViewer Touch

* Valintapainikkeiden nimet luetaan.
* Painikkeiden nimet luetaan.

## Bank of America/Twitter

* Painikkeiden nimet luetaan.

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

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
