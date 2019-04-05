# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* NVDA compatibility: 2018.4 to 2019.1

Tämä lisäosa sisältää kokoelman sovellusmoduuleja Windows 10:n mukana
tuleville sovelluksille sekä laajennuksia ja korjauksia tietyille
säätimille.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Toimintokeskus
* Hälytykset ja kello
* Kalenteri
* Laskin (moderni)
* Cortana
* Palautekeskus
* Sähköposti
* Kartat
* Microsoft Edge
* Moderni näppäimistö (emojipaneeli/fyysisen näppäimistösyötteen
  ehdotukset/pilvileikepöydän kohteet versiossa 1709 ja uudemmissa)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Kauppa
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* This add-on requires Windows 10 Version 1803 (build 17134) or later and
  NVDA 2018.4 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17763) and latest stable version of NVDA.
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue vanhoja
  Windows 10 -versioita tai eivät ole enää käyttökelpoisia Windows 10:een ja
  sovelluksiin tehtyjen muutosten vuoksi.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7, Windows 8.1, and unsupported releases of Windows
  10.
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
* Seuraavat UIA-tapahtumat tunnistetaan: sijainnin muutos aktiivisessa
  tekstissä, ohjain kohteelle, vetämisen aloitus, vetämisen peruutus,
  vetäminen suoritettu, elementti valittu, kohteen tila, aktiivisen alueen
  muutos, ilmoitus, järjestelmän ilmoitus, työkaluvihje avattu, ikkuna
  avattu. Näitä tapahtumia seurataan, kun NVDA:n lokitasoksi on määritetty
  "virheenkorjaus", ja UIA-ilmoitustapahtuma ilmaistaan virheäänellä, mikäli
  ilmoitukset tulevat muualta kuin aktiivisesta sovelluksesta.
* Edgen ja universaalien sovellusten työkaluvihjeet tunnistetaan ja
  ilmoitetaan.
* NVDA ilmoittaa nykyisen työpöydän tunnisteen (esim. työpöytä 2)
  avattaessa, suljettaessa tai vaihdettaessa virtuaalityöpöytien välillä.
* NVDA ei enää ilmoita Käynnistä-valikon kokoa  näytön resoluutiota tai
  suuntaa vaihdettaessa.
* NVDA ilmoittaa nyt äänenvoimakkuuden ja kirkkauden muutokset
  koontiversiossa 18323 ja uudemmissa.

## Toimintokeskus

* Brightness quick action is now a button instead of a toggle button. This
  is now part of NVDA 2019.1.
* Various status changes such as Focus Assist and Brightness will be
  reported. This is now part of NVDA 2019.1.

## Hälytykset ja kello

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates. This is now part of NVDA
  2019.1.

## Laskin

* NVDA ilmoittaa laskutoimituksen tuloksen Enteriä tai Esciä painettaessa.
* NVDA puhuu laskutoimitusten tulokset (esim. yksikkö- ja
  valuuttamuuntimessa) heti laskukaavoja syötettäessä.
* NVDA ei enää sano "otsikkotaso" tarkasteltaessa laskutoimitusten tuloksia
  laskimessa.

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
* NVDA will no longer do anything or play error tones after closing this
  app. This is now part of NVDA 2019.1.

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

## Ihmiset

* Ensimmäinen ehdotus puhutaan kontakteja etsittäessä, erityisesti uusimpia
  sovellusversioita käytettäessä.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  mukaan lukien Tallennusseurannan/Levynsiivouksen pienoisohjelma, puhutaan
  nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* NVDA ei enää epäonnistu joidenkin yhdistelmäruutujen ja
  valintapainikkeiden selitteiden tunnistamisessa ja/tai arvomuutosten
  ilmoittamisessa.
* Edistymispalkkien äänimerkkejä ei enää kuulu muutettaessa
  äänenvoimakkuutta versiossa 1803 ja uudemmissa.
* Windows Updaten tilailmoituksia puhutaan enemmän etenkin virheitä
  havaittaessa.
* NVDA ei tee enää mitään tai toista virheääniä, mikäli
  objektinavigointikomentoja käytetään tietyissä tilanteissa.
* Windows Updaten muistutusvalintaikkuna tunnistetaan asianmukaisesti
  valintaikkunaksi.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.

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
