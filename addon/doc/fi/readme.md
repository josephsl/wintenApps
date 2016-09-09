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
* Insider-/Palautekeskus (vain Windows Insider -ohjelmaan liittyneillä).
* Sähköposti
* Kartat
* Microsoft Edge
* Asetukset (järjestelmän asetukset, Windows+I).
* Skypen esiversio
* Twitter
* TeamViewer Touch
* Sää
* Sekalaisia moduuleita sellaisille säätimille kuin Käynnistä-valikon
  tiilet.

Huom: Tämä lisäosa edellyttää Windows 10:n versiota 1507 (koontiversio
10240) tai uudempaa ja NVDA:n 2015.4-versiota tai uudempaa.

## Yleistä

* Alavalikot tunnistetaan oikein Käynnistä-valikon tiilien pikavalikoissa.
* Ikkunoita pienennettäessä (Windows+M) ei enää sanota "ruutu"
  (havaittavissa Insider-esiversioita käytettäessä).
* Tietyt valintaikkunat tunnistetaan nyt oikeiksi
  valintaikkunoiksi. Tällaisia ovat esim. Insider-esiversioiden
  valintaikkuna (Asetukset-sovelluksessa) sekä uudentyylinen Käyttäjätilien
  valvonnan valintaikkuna koontiversiossa 14328 ja uudemmissa NVDA
  2016.2.1:ssä tai vanhemmassa.
* Ajanvalitsimen lukeminen toimii muillakin kuin englannin kielialueilla.
* Tiettyjen hakukenttien ehdotusten ilmestyminen/loppuminen (varsinkin
  Asetukset-sovelluksessa) ilmaistaan nyt äänimerkeillä ja/tai
  pistekirjoituksella.

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
* Cortanalle puhuttaessa saadaan parempi kokemus painamalla Cortanan
  kuuntelutilan pikanäppäintä (Windows+C versioissa 1507 ja 1511,
  Windows+Shift+C versiossa 1607).

## Insider-/Palautekeskus ja TeamViewer Touch

* Vain Insider-keskus (Palautekeskus Anniversary Update -versiossa):
  Tarkoitettu Windows Insider -ohjelmaan liittyneiden käyttöön, joilla on
  asennettuna Windowsin Insider-versio.
* Valintapainikkeiden nimet luetaan.
* TeamViewer Touch: Painikkeiden nimet luetaan.

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

## Skypen esiversio

* Kirjoitusilmaisimen teksti puhutaan kuten Skypen työpöytäversiossa.
* Osittainen Control+NVDA+numero-komentojen paluu tuoreen
  keskusteluhistorian lukemiseen sekä navigointiobjektin siirtämiseen
  keskustelukohteisiin kuten Skypen työpöytäversiossa.

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
