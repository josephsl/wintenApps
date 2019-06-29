# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* NVDA compatibility: 2018.4 to 2019.2

Tämä lisäosa sisältää kokoelman sovellusmoduuleja Windows 10:n mukana
tuleville sovelluksille sekä laajennuksia ja korjauksia tietyille
säätimille.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Toimintokeskus
* Hälytykset ja kello
* Laskin (moderni)
* Kalenteri
* Cortana
* Palautekeskus
* Sähköposti
* Kartat
* Microsoft Edge
* Moderni näppäimistö (emojipaneeli/sanelu/fyysisen näppäimistösyötteen
  ehdotukset/pilvileikepöydän kohteet versiossa 1709 ja uudemmissa)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Kauppa
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* Tämä lisäosa edellyttää Windows 10:n versiota 1803 (koontiversio 17134)
  tai uudempaa ja NVDA 2018.4:ää tai uudempaa. Käytä parhaan
  käyttökokemuksen varmistamiseksi Windows 10:n viimeisintä vakaata versiota
  (koontiversio 18362) sekä uusinta vakaata NVDA:n versiota.
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue vanhoja
  Windows 10 -versioita tai eivät ole enää käyttökelpoisia Windows 10:een ja
  sovelluksiin tehtyjen muutosten vuoksi.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

* NVDA ei toista enää virheääniä tai tee mitään, mikäli tämä lisäosa
  aktivoituu Windows 7:ssä, 8.1:ssä tai sellaisissa Windows 10:n versioissa,
  joita ei enää tueta.
* Alavalikot tunnistetaan asianmukaisesti useissa sovelluksissa, mukaan
  lukien Käynnistä-valikon ruutujen tilannekohtaiset valikot ja microsoft
  Edgen sovellusvalikko (Redstone 5).
* Entistä enemmän valintaikkunoita tunnistetaan ja ilmoitetaan nyt
  asianmukaisesti valintaikkunoina, mukaan lukien Insider-esiversion
  valintaikkuna (Asetukset-sovellus). Tämä sisältyy nyt NVDA 2018.3:een.
* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa. Tätä toimintoa hallitaan "Lue objektien sijaintitiedot"
  -asetuksella Objektien lukeminen -paneelista NVDA:n asetuksista.
* Sijaintitietoja (esim. 1 / 2) ei enää lueta tietyissä pikavalikoissa
  (kuten Edgessä).
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* Edgen ja universaalien sovellusten työkaluvihjeet tunnistetaan ja
  ilmoitetaan.
* NVDA ilmoittaa nykyisen työpöydän tunnisteen (esim. työpöytä 2) avattaessa
  ja suljettaessa virtuaalityöpöytiä tai siirryttäessä niiden välillä.
* NVDA ei enää ilmoita Käynnistä-valikon kokoa  näytön resoluutiota tai
  suuntaa vaihdettaessa.
* In Version 1903 (May 2019 Update), NVDA will announce volume and
  brightness changes immediately if focused on File Explorer. This is now
  part of NVDA 2019.2.

## Toimintokeskus

* Kirkkaus-pikatoiminto on nyt vipupainikkeen sijasta painike. Tämä sisältyy
  NVDA 2019.1:een.
* Useat tilojen, kuten Keskittymisavustajan ja kirkkauden, muutokset
  ilmoitetaan. Tämä sisältyy NVDA 2019.1:een.

## Hälytykset ja kello

* Ajanvalitsimen arvot puhutaan - havaittavissa siirrettäessä kohdistusta
  valitsimen säätimiin. Tämä vaikuttaa myös säätimeen, jolla valitaan,
  milloin Windows käynnistetään uudelleen päivitysten asentamisen
  viimeistelemiseksi. Tämä tulee sisältyy NVDA 2019.1:een.

## Laskin

* NVDA ilmoittaa laskutoimituksen tuloksen Enteriä tai Esciä painettaessa.
* NVDA puhuu laskutoimitusten tulokset (esim. yksikkö- ja
  valuuttamuuntimessa) heti laskukaavoja syötettäessä.
* NVDA ei enää sano "otsikkotaso" tarkasteltaessa laskutoimitusten tuloksia
  laskimessa.
* NVDA ilmoittaa, jos lukujen enimmäismäärä saavutetaan ilmaisuja
  kirjoitettaessa.

## Kalenteri

* NVDA ei sano enää "muokattava" tai "vain luku" viestisisällössä ja muissa
  kentissä.

## Cortana

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa
  (mikäli näin ei ole, avaa Käynnistä-valikko uudelleen ja yritä hakua
  toistamiseen).
* NVDA on hiljaa puhuttaessa Cortanalle mikrofonin välityksellä.
* NVDA puhuu nyt vahvistuksen muistutusta lisättäessä.

## Palautekeskus

* NVDA ei enää puhu palauteluokkia kahdesti sovelluksen uudemmissa
  versioissa.

## Sähköposti

* Voit nyt käyttää viestiluettelon kohteita tarkastellessasi
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen. Huomaa, että
  rivien (viestien) välillä liikkumista ei tueta.
* Ät-maininnan ehdotukset ilmaistaan äänimerkeillä viestiä kirjoitettaessa.
* NVDA ei tee enää mitään tai toista virheääniä, kun tämä sovellus on
  suljettu. Tämä sisältyy NVDA 2019.1:een.

## Kartat

* NVDA toistaa äänimerkin karttasijainneille.
* NVDA ilmoittaa katuosoitteet käyttäessäsi nuolinäppäimiä kartalla
  liikkumiseen oltaessa katunäkymässä ja mikäli "käytä näppäimistöä"
  -vaihtoehto on otettu käyttöön.

## Microsoft Edge

* Tekstin automaattista täydennystä seurataan ja siitä ilmoitetaan
  osoitepalkissa.
* NVDA ei enää toista ehdotusten ääntä vaihdettaessa koko näytön tilaa
  F11:tä painamalla.

## Moderni näppäimistö

Huom: suurin osa alla luetelluista ominaisuuksista sisältyy nyt NVDA
2018.3:een tai uudempiin versioihin.

* Tuki version 1709 (Fall Creators -päivitys) ja uudempien kelluvalle
  emojinsyöttöpaneelille, mukaan lukien version 1809 (koontiversio 17661 ja
  uudemmat) uudelleensuunniteltu paneeli sekä versioon 19H1 (koontiversio
  18262 ja uudemmat) tehdyt muutokset, mukaan lukien kaomoji sekä
  koontiversion 18305 symbolikategoriat. Mikäli käytetään NVDA 2018.4:ää
  vanhempia versioita, tulee parhaan kokemuksen saamiseksi käyttää Windows
  OneCore -syntetisaattoria. Jos käytössä on versio 2018.4 tai uudempi,
  tulee NVDA:n puheasetuksista ottaa käyttöön Unicode-konsortion datan
  käyttäminen ja symbolitasoksi asetta "jotain" tai korkeampi.
* Tuki fyysisen näppäimistösyötteen ehdotuksille versiossa 1803 (April 2018
  -päivitys) ja uudemmissa.
* Kun emojipaneeli avautuu, NVDA ilmoittaa koontiversion 1709 jälkeisissä
  versioissa ensimmäisen valittuna olevan emojin. Tämä on näkyvämpää
  koontiversiossa 18262 ja uudemmissa, joissa emojipaneeli saattaa avautua
  viimeksi selattuun kategoriaan, kuten näyttäessään ihonvärimuuntimen
  Ihmiset-kategorian avauduttua.
* Tuki pilvileikepöydän kohteiden ilmoittamiselle versiossa 1809
  (koontiversio 17666 ja uudemmat).
* Puheliaisuutta vähennetty modernia näppäimistöä ja sen ominaisuuksia
  käytettäessä. Fyysisen näppäimistön syöttöehdotuksia avattaessa ei enää
  sanota "Microsoft Candidate UI" sekä ollaan hiljaa tilanteessa, jossa
  tietyt kosketusnäppäimistön näppäimet aiheuttavat joissakin järjestelmissä
  muuttuneen nimitapahtuman.
* NVDA ei toista enää virheääniä tai tee mitään emojipaneelia suljettaessa
  uudemmissa 19H1-Insider-esiversioissa. Tämä sisältyy NVDA 2019.1:een.
* NVDA ilmoittaa versiossa 1809 (October 2018 -päivitys) ja uudemmissa
  emojien hakutulokset, mikäli mahdollista. Tämä sisältyy NVDA 2019.1:een.
* NVDA ei enää sano joissakin tilanteissa "leikepöytä", kun leikepöydällä on
  kohteita.
* Emojipaneelin avautuessa ei enää näytä siltä, että NVDA  ei tee mitään
  joissakin järjestelmissä, joissa on asennettuna Windows 10:n versio 1903
  (May 2019 -päivitys).

## Ihmiset

* Ensimmäinen ehdotus puhutaan kontakteja etsittäessä, erityisesti uusimpia
  sovellusversioita käytettäessä.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  mukaan lukien Tallennusseurannan/Levynsiivouksen pienoisohjelma sekä
  Windows Updaten virheet, puhutaan nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* NVDA ei enää epäonnistu joidenkin yhdistelmäruutujen ja
  valintapainikkeiden selitteiden tunnistamisessa ja/tai arvomuutosten
  ilmoittamisessa.
* Edistymispalkkien äänimerkkejä ei enää kuulu muutettaessa
  äänenvoimakkuutta versiossa 1803 ja uudemmissa.
* NVDA ei tee enää mitään tai toista virheääniä, mikäli
  objektinavigointikomentoja käytetään tietyissä tilanteissa.
* Windows Updaten muistutusvalintaikkuna tunnistetaan asianmukaisesti
  valintaikkunaksi.
* Joissakin Windows-asennuksissa näkyvät erikoiset säädinten nimet on
  korjattu.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## Kauppa

* Sovellusten nimet näytetään oikein päivitettävien sovellusten luettelossa
  päivitystarkistuksen jälkeen.
* NVDA ilmoittaa tuotteen nimen ja latauksen edistymisen sisältöä, kuten
  sovelluksia ja elokuvia ladattaessa.

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

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
