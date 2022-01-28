# Windows App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* Yhteensopivuus: NVDA 2021.2 ja uudemmat

Huom: Tämä lisäosa (alkuperäiseltä nimeltään Windows 10 App Essentials) on
nimetty uudelleen Windows App Essentialsiksi vuonna 2021 tukemaan Windows
10:tä sekä tulevia versioita, kuten Windows 11:tä. Lisäosassa viitataan
vielä osittain vanhaan nimeen.

Tämä lisäosa on kokoelma sovellusmoduuleita moderneille
Windows-sovelluksille sekä laajennuksia ja korjauksia tietyille säätimille
Windows 10:ssä ja uudemmissa.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Laskin
* Cortana
* Sähköposti
* Kartat
* Microsoft Solitaire -kokoelma
* Moderni näppäimistö (emojipaneeli/sanelu/puhekirjoitus/fyysisen
  näppäimistösyötteen ehdotukset/pilvileikepöydän historia/modernin
  syöttömenetelmän muokkaimet)
* Muistio (Windows 11)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* Tämä lisäosa edellyttää Windows 10:n versiota 21H1 (koontiversio 19043)
  tai uudempaa ja on yhteensopiva Windows 11:n kanssa.
* Tämä lisäosa ei tue Windows 10 Enterprise LTSC:tä (Long-Term Servicing
  Channel) eikä Windows Server -versioita, vaikka asennus onkin mahdollista.
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue tuen
  piiristä poistuneita Windowseja, kuten vanhoja 10:n versioita, tai eivät
  ole enää käyttökelpoisia Windowsiin ja sovelluksiin tehtyjen muutosten
  vuoksi.
* Jotkin sovellukset tukevat kompaktia peitetilaa (esim. Laskimessa Aina
  päällimmäisenä), joka ei toimi oikein NVDA:n massamuistiversion kanssa.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa, mukaan lukien tilanteet, joissa ehdotusten määrä muuttuu
  haun edistyessä. Tämä sisältyy NVDA 2021.3:een.
* Seuraavat UIA-tapahtumat tunnistetaan NVDA:n tarjoamien
  UIA-tapahtumakäsittelijöiden lisäksi: vetäminen suoritettu, vetämisen
  kohde pudotettu, asettelu mitätöity. Näitä tapahtumia seurataan, kun
  NVDA:n lokitasoksi on määritetty "virheenkorjaus", ja
  UIA-ilmoitustapahtuma ilmaistaan virheäänellä, mikäli ilmoitukset tulevat
  muualta kuin aktiivisesta sovelluksesta. NVDA:han sisäänrakennettuja
  tapahtumia, kuten nimen muutos ja ohjain tapahtumille seurataan Event
  Tracker -nimisestä lisäosasta.
* NVDA ilmoittaa aktiivisen virtuaalityöpöydän nimen (esim. työpöytä 2)
  avattaessa, suljettaessa, uudelleenjärjestettäessä (Windows 11) tai
  siirryttäessä niiden välillä.
* NVDA ei enää ilmoita Käynnistä-valikon kokoa  näytön resoluutiota tai
  suuntaa vaihdettaessa.
* Kun Käynnistä-valikon ruutuja tai Toimintokeskuksen pikatoimintoja
  järjestellään Alt+Vaihto+nuolinäppäimillä, NVDA puhuu raahattujen
  kohteiden tiedot tai raahatun kohteen uuden sijainnin.
* Ilmoitukset, kuten äänenvoimakkuuden/kirkkauden muutokset
  resurssienhallinnassa sekä sovellusten päivitysilmoitukset Microsoft
  Storesta voidaan estää poistamalla käytöstä Lue ilmoitukset -asetus NVDA:n
  objektien lukemisen asetuksista.

## Laskin

* NVDA ei enää sano graafisen laskinnäytön ilmoitusta kahdesti.
* Historia- ja muistiluettelon kohteet nimetään oikein Windows 10:ssä.

## Cortana

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa.
* NVDA on hiljaa puhuttaessa Cortanalle mikrofonin välityksellä.

## Sähköposti

* Voit nyt käyttää viestiluettelon kohteita tarkastellessasi
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen. Huomaa, että
  rivien (viestien) välillä liikkumista ei tueta.

## Kartat

* NVDA toistaa äänimerkin karttasijainneille.
* NVDA ilmoittaa katuosoitteet käyttäessäsi nuolinäppäimiä kartalla
  liikkumiseen oltaessa katunäkymässä ja mikäli "käytä näppäimistöä"
  -vaihtoehto on otettu käyttöön.

## Microsoft Solitaire -kokoelma

* NVDA sanoo korttien ja korttipakkojen nimet.

## Moderni näppäimistö

Näitä ovat emojipaneeli, leikepöydän historia, sanelu/puhekirjoitus,
ehdotukset syötettäessä tekstiä fyysisellä näppäimistöllä sekä modernin
syöttömenetelmän editorit tietyille kielille. Ota käyttöön emojeita
tarkasteltaessa Unicode-konsortion datan asetus NVDA:n puheasetuksista
parhaan kokemuksen saamiseksi, ja aseta symbolitasoksi "jotain" tai
korkeampi. Kun liität leikepöydän historiasta, liitä valittu kohde
painamalla välilyöntinäppäintä Enterin sijaan. NVDA tukee lisäksi
päivitettyä syöttökokemuksen paneelia Windows 11:ssä.

* Kun emojiryhmä (kaomoji ja symboliryhmä mukaan lukien) valitaan Windows
  10:ssä, NVDA ei enää siirrä navigointiobjektia tiettyihin emojeihin.
* Lisätty tuki Windows 11:n päivitetylle syöttökokemuksen paneelille
  (yhdistetty emojipaneeli ja leikepöydän historia).
* Windows 11:ssä on jälleen mahdollista käyttää nuolinäppäimiä emojien
  tarkasteluun, kun emojipaneeli avautuu.

## Muistio

Tämä viittaa Windows 11:n Muistion versioon 11 tai sitä uudempiin.

* NVDA puhuu tilakohteet, kuten rivin ja sarakkeen tiedot, kun Puhu tilarivi
  -komento (NVDA+End pöytäkoneissa, NVDA+Vaihto+End kannettavissa)
  suoritetaan.
* NVDA ei enää puhu kirjoitettua tekstiä, kun asiakirjassa painetaan
  Enter-näppäintä.

## Ihmiset

* Ensimmäinen ehdotus puhutaan kontakteja etsittäessä, erityisesti uusimpia
  sovellusversioita käytettäessä.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  mukaan lukien Tallennusseurannan/Levynsiivouksen pienoisohjelma sekä
  Windows Updaten virheet, puhutaan nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* Joissakin Windows-asennuksissa näkyvät erikoiset säädinten nimet on
  korjattu.
* NVDA puhuu valinnaisen laatupäivityksen säätimen nimen (Lataa ja asenna
  nyt -linkki Windows 10:ssä, Lataa-painike Windows 11:ssä), mikäli
  sellainen on näkyvissä.
* Navigointipolkupalkin kohteet tunnistetaan oikein Windows 11:ssä.

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
