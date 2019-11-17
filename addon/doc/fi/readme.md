# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* NVDA compatibility: 2019.2 to 2019.3

Tämä lisäosa sisältää kokoelman sovellusmoduuleja Windows 10:n mukana
tuleville sovelluksille sekä laajennuksia ja korjauksia tietyille
säätimille.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Laskin (moderni)
* Kalenteri
* Cortana (perinteinen ja keskustelut)
* Palautekeskus
* Sähköposti
* Kartat
* Microsoft Edge
* Microsoft Store
* Moderni näppäimistö (emojipaneeli/sanelu/fyysisen näppäimistösyötteen
  ehdotukset/pilvileikepöydän kohteet versiossa 1709 ja uudemmissa)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18363) and latest stable version of NVDA.
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
* Alivalikot tunnistetaan asianmukaisesti useissa sovelluksissa, mukaan
  lukien Käynnistä-valikon ruutujen tilannekohtaiset valikot ja microsoft
  Edgen sovellusvalikko versiossa 1809 (October 2018 -päivitys).
* Entistä enemmän valintaikkunoita tunnistetaan ja ilmoitetaan nyt
  asianmukaisesti valintaikkunoina, mukaan lukien Insider-esiversion
  valintaikkuna (Asetukset-sovellus). Tämä sisältyy nyt NVDA 2018.3:een.
* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa. Tätä toimintoa hallitaan "Lue objektien sijaintitiedot"
  -asetuksella Objektien lukeminen -paneelista NVDA:n asetuksista.
* NVDA ei enää sano "tyhjä" painettaessa ylä- tai alanuolta kaikki
  sovellukset -näkymän avaamiseksi Käynnistä-valikossa. Tämä sisältyy NVDA
  2019.3:een.
* NVDA puhuu nyt etsittäessä vähemmän hakutuloksia kahdesti
  Käynnistä-valikossa tai Resurssienhallinnassa versiossa 1909 (November
  2019 -päivitys) ja uudemmissa, mikä tekee lisäksi
  pistekirjoitustulosteesta yhdenmukaisempaa kohteita tarkasteltaessa.
* Sijaintitietoja (esim. 1 / 2) ei enää lueta tietyissä pikavalikoissa
  (kuten Edgessä).
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app.
* On mahdollista seurata vain tiettyjä tapahtumia ja/tai tietyistä
  sovelluksista tulevia tapahtumia.
* Edgen ja universaalien sovellusten työkaluvihjeet tunnistetaan ja
  ilmoitetaan. Tämä sisältyy NVDA 2019.3:een.
* NVDA ilmoittaa nykyisen työpöydän tunnisteen (esim. työpöytä 2) avattaessa
  ja suljettaessa virtuaalityöpöytiä tai siirryttäessä niiden välillä.
* NVDA ei enää ilmoita Käynnistä-valikon kokoa  näytön resoluutiota tai
  suuntaa vaihdettaessa.
* Useiden Microsoft Store -sovellusten nimi ja versio näytetään nyt
  asianmukaisesti. Tämä tulee sisältymään NVDA 2019.3:een.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.

## Laskin

* NVDA ilmoittaa laskutoimituksen tuloksen Enteriä tai Esciä painettaessa.
* NVDA puhuu laskutoimitusten tulokset (esim. yksikkö- ja
  valuuttamuuntimessa) heti laskukaavoja syötettäessä.
* NVDA ei enää sano "otsikkotaso" tarkasteltaessa laskutoimitusten tuloksia
  laskimessa.
* NVDA ilmoittaa, jos lukujen enimmäismäärä saavutetaan ilmaisuja
  kirjoitettaessa.
* Lisätty tuki Laskin-sovelluksen version 10.1908 ja uudempien aina käytössä
  -tilalle.

## Kalenteri

* NVDA ei sano enää "muokattava" tai "vain luku" viestisisällössä ja muissa
  kentissä.

## Cortana

Useimmat kohdat eivät enää koske versiota 1903 ja uudempia. Perinteinen
Cortana viittaa vanhempaan Cortana-liittymään, joka oli osa
Käynnistä-valikkoa.

* Cortanan (sekä perinteisen että keskustelut-käyttöliittymän)
  tekstimuotoiset vastaukset puhutaan useimmissa tapauksissa (mikäli käytät
  perinteistä Cortanaa eikä vastauksia puhuta, avaa Käynnistä-valikko
  uudelleen ja yritä hakua toistamiseen).
* NVDA on hiljaa puhuttaessa Cortanalle mikrofonin välityksellä.
* NVDA puhuu nyt vahvistuksen muistutusta lisättäessä perinteisessä
  Cortanassa.
* Windows-haun käyttöliittymän voimalla toimivaa Resurssienhallinnan
  modernia hakukokemusta tuetaan versiossa 1909 (November 2019 -päivitys)
  sekä 20H1:ssä (koontiversio 18945) ja uudemmissa.

## Palautekeskus

* NVDA ei enää puhu palauteluokkia kahdesti sovelluksen uudemmissa
  versioissa.

## Sähköposti

* Voit nyt käyttää viestiluettelon kohteita tarkastellessasi
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen. Huomaa, että
  rivien (viestien) välillä liikkumista ei tueta.
* Ät-maininnan ehdotukset ilmaistaan äänimerkeillä viestiä kirjoitettaessa.

## Kartat

* NVDA toistaa äänimerkin karttasijainneille.
* NVDA ilmoittaa katuosoitteet käyttäessäsi nuolinäppäimiä kartalla
  liikkumiseen oltaessa katunäkymässä ja mikäli "käytä näppäimistöä"
  -vaihtoehto on otettu käyttöön.

## Microsoft Edge

Tämä viittaa perinteiseen EdgeHTML-pohjaiseen Microsoft Edgeen.

* Tekstin automaattista täydennystä seurataan ja siitä ilmoitetaan
  osoitepalkissa. Tämä tulee sisältymään NVDA 2019.3:een.
* NVDA ei enää toista ehdotusten ääntä vaihdettaessa koko näytön tilaa
  F11:tä painamalla. Tämä tulee sisältymään NVDA 2019.3:een.
* Ehdotusääntä ei enää toisteta osoitepalkissa. Tämä tulee sisältymään NVDA
  2019.3:een.

## Microsoft Store

* Sovellusten nimet näytetään oikein päivitettävien sovellusten luettelossa
  päivitystarkistuksen jälkeen.
* NVDA ilmoittaa tuotteen nimen ja latauksen edistymisen sisältöä, kuten
  sovelluksia ja elokuvia ladattaessa.

## Moderni näppäimistö

Suurin osa alla luetelluista ominaisuuksista sisältyy nyt NVDA 2018.3:een
tai sitä uudempiin versioihin.

* Tuki version 1709 (Fall Creators -päivitys) ja uudempien kelluvalle
  emojinsyöttöpaneelille, mukaan lukien version 1809 (koontiversio 17661 ja
  uudemmat) uudelleensuunniteltu paneeli sekä versioon 19H1 (koontiversio
  18262 ja uudemmat) tehdyt muutokset, mukaan lukien kaomoji sekä
  koontiversion 18305 symbolikategoriat. Tämä koskee myös koontiversiota
  18963 ja uudempia, sillä sovellus on nimetty uudelleen. Mikäli käytetään
  NVDA 2018.4:ää vanhempia versioita, tulee parhaan kokemuksen saamiseksi
  käyttää Windows OneCore -syntetisaattoria. Jos käytössä on versio 2018.4
  tai uudempi, tulee NVDA:n puheasetuksista ottaa käyttöön
  Unicode-konsortion datan käyttäminen ja symbolitasoksi asetta "jotain" tai
  korkeampi.
* NVDA ei enää sano joissakin tilanteissa "leikepöytä", kun leikepöydällä on
  kohteita.
* Emojipaneelin avautuessa ei enää näytä siltä, että NVDA  ei tee mitään
  joissakin järjestelmissä, joissa on asennettuna Windows 10:n versio 1903
  (May 2019 -päivitys) tai uudempi.
* Lisätty tuki modernille kiinan, japanin ja korean (CJK)
  IME-ehdotusliittymälle, joka esiteltiin 20H1:n koontiversiossa 18965 ja
  uudemmissa.

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
  äänenvoimakkuutta versiossa 1803 ja uudemmissa. Tämä sisältyy NVDA
  2019.3:een.
* NVDA ei tee enää mitään tai toista virheääniä, mikäli
  objektinavigointikomentoja käytetään tietyissä tilanteissa.
* Windows Updaten muistutusvalintaikkuna tunnistetaan asianmukaisesti
  valintaikkunaksi.
* Joissakin Windows-asennuksissa näkyvät erikoiset säädinten nimet on
  korjattu.
* Windows Update -prosessiin ominaisuuspäivitysten osalta tehtyjen muutosten
  vuoksi uudempiin 1803:n versioihin ja sitä tuoreempiin  on lisätty Lataa
  ja asenna nyt -linkki. Jos uusi päivitys on saatavilla, NVDA puhuu nyt sen
  nimen.

## Sää

* Sellaiset välilehdet kuten "ennuste" ja "kartat" tunnistetaan oikeiksi
  välilehdiksi (korjauksen tehnyt Derek Riemer).
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
