# Windows App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* Yhteensopivuus: NVDA 2021.3 ja uudemmat

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
  näppäimistösyötteen ehdotukset/leikepöydän historia/ehdotetut toiminnot
  (esiversio)/modernin syöttömenetelmän muokkaimet)
* Muistio (Windows 11)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Puhekäyttö (Windows 11)
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* Tämä lisäosa edellyttää Windows 10:n versiota 21H1 (koontiversio 19043),
  Windows 11:n versiota 21H2 (koontiversio 22000) tai uudempaa.
* Tämä lisäosa ei tue Windows 10 Enterprise LTSC:tä (Long-Term Servicing
  Channel) eikä Windows Server -versioita, vaikka asennus onkin mahdollista.
* Kaikkia Windowsin Insider-esiversioiden ominaisuuksia ei tueta.
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue tuen
  piiristä poistuneita Windowseja, kuten vanhoja 10:n versioita, tai eivät
  ole enää käyttökelpoisia Windowsiin ja sovelluksiin tehtyjen muutosten
  vuoksi.
* Jotkin sovellukset tukevat kompaktia peitetilaa (esim. Laskimessa Aina
  päällimmäisenä), joka ei toimi oikein NVDA:n massamuistiversion kanssa.
* Saat parhaan kokemuksen verkkotekniikoita ja -sisältöä hyödyntävistä
  sovelluksista, kuten Käynnistä-valikosta ja sen pikavalikosta, ottamalla
  käyttöön "Automaattinen vuorovaikutustila kohdistuksen muuttuessa"
  -asetuksen NVDA:n Selaustila-asetuspaneelista.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

* NVDA:n tarjoamien UIA-tapahtumakäsittelijöiden lisäksi tunnistetaan
  seuraavat UIA-tapahtumat ja -ominaisuudet: pudotus suoritettu, vetäminen
  ja pudottaminen meneillään, pudotettu pudotuksen kohteeseen. Näitä
  tapahtumia seurataan ja ne tallennetaan lokiin, kun NVDA:n lokitasoksi on
  määritetty "virheenkorjaus".
* NVDA ilmoittaa aktiivisen virtuaalityöpöydän nimen (esim. työpöytä 2)
  avattaessa, suljettaessa, uudelleenjärjestettäessä (Windows 11) tai
  siirryttäessä niiden välillä.
* NVDA puhuu raahattujen kohteiden tiedot tai raahatun kohteen uuden
  sijainnin, kun Käynnistä-valikon kiinnitettyjä kohteita (ruutuja Windows
  10:ssä) tai Toimintokeskuksen pikatoimintoja järjestellään
  Alt+Vaihto+nuolinäppäimillä.
* Ilmoitukset, kuten äänenvoimakkuuden/kirkkauden muutokset
  resurssienhallinnassa sekä sovellusten päivitysilmoitukset Microsoft
  Storesta voidaan estää poistamalla käytöstä Lue ilmoitukset -asetus NVDA:n
  objektien lukemisen asetuksista.
* Mikrofonin mykistyksen (Win+Alt+K) tila ilmoitetaan nyt kaikkialta Windows
  11:n versiossa 22H2 ja sitä uudemmissa.
* NVDA ei enää toista tekstitulostetta Windows Terminal 1.12.10733:ssa ja
  uudemmissa. Tämä sisältyy nyt NVDA 2022.1:een.
* NVDA ilmoittaa jälleen hakutulosten tiedot Käynnistä-valikossa. Tämä
  sisältyy nyt NVDA 2022.2:een.
* Tehtäväpalkin kohteet ja muut käyttöliittymän säätimet tunnistetaan oikein
  Windows 11:ssä hiirtä ja/tai kosketusvuorovaikutusta käytettäessä. Tämä
  sisältyy nyt NVDA 2022.2:een.

## Laskin

* Historia- ja muistiluettelon kohteet nimetään oikein Windows 10:ssä. Tämä
  sisältyy NVDA 2022.1:een.
* NVDA ilmoittaa nyt laskimen näytön sisällön funktiotilan komentoja, kuten
  trigonometrisiä laskutoimituksia, suoritettaessa. Tämä sisältyy nyt NVDA
  2022.2:een.

## Cortana

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa.
* NVDA on hiljaa puhuttaessa Cortanalle mikrofonin välityksellä.

## Sähköposti

* Voit nyt käyttää viestiluettelon kohteita tarkastellessasi
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen. Huomaa, että
  rivien (viestien) välillä liikkumista ei tueta.

## Kartat

* NVDA toistaa äänimerkin karttasijainneille.

## Microsoft Solitaire -kokoelma

* NVDA sanoo korttien ja korttipakkojen nimet.

## Moderni näppäimistö

Näitä ovat emojipaneeli, leikepöydän historia, sanelu/puhekirjoitus,
ehdotukset syötettäessä tekstiä fyysisellä näppäimistöllä, ehdotetut
toiminnot (esiversio) sekä modernin syöttömenetelmän editorit tietyille
kielille. Ota käyttöön emojeita tarkasteltaessa Unicode-konsortion datan
asetus NVDA:n puheasetuksista parhaan kokemuksen saamiseksi, ja aseta
symbolitasoksi "jotain" tai korkeampi. Kun liität leikepöydän historiasta,
liitä valittu kohde painamalla välilyöntinäppäintä Enterin sijaan. NVDA
tukee lisäksi päivitettyä syöttökokemuksen paneelia Windows 11:ssä.

* Kun emojiryhmä (kaomoji ja symboliryhmä mukaan lukien) valitaan Windows
  10:ssä, NVDA ei enää siirrä navigointiobjektia tiettyihin emojeihin.
* Windows 11:ssä on jälleen mahdollista käyttää nuolinäppäimiä emojien
  tarkasteluun, kun emojipaneeli avautuu. Tämä sisältyy NVDA 2022.1:een.
* Selaustila poistetaan käytöstä oletusarvoisesti Windows 11:n leikepöydän
  historiassa, minkä tarkoituksena on mahdollistaa NVDA:lle historian
  valikkokohteiden lukeminen.
* Insider-esikoontiversiossa 25115 NVDA ilmoittaa ehdotetut toiminnot, kun
  leikepöydälle kopioidaan yhteensopivaa dataa, kuten puhelinnumeroita.

## Muistio

Tämä viittaa Windows 11:n Muistion versioon 11 tai sitä uudempiin.

* NVDA puhuu tilakohteet, kuten rivin ja sarakkeen tiedot, kun Puhu tilarivi
  -komento (NVDA+End pöytäkoneissa, NVDA+Vaihto+End kannettavissa)
  suoritetaan. Tämä sisältyy nyt NVDA 2022.2:een.

## Ihmiset

* Ensimmäinen ehdotus puhutaan kontakteja etsittäessä, erityisesti uusimpia
  sovellusversioita käytettäessä.

## Asetukset

* Joissakin Windows-asennuksissa näkyvät erikoiset säädinten nimet on
  korjattu.
* NVDA puhuu valinnaisen laatupäivityksen säätimen nimen (Lataa ja asenna
  nyt -linkki Windows 10:ssä, Lataa-painike Windows 11:ssä), mikäli
  sellainen on näkyvissä.
* Navigointipolkupalkin kohteet tunnistetaan oikein Windows 11:ssä.
* NVDA keskeyttää puheen ja ilmoittaa Windows 10:ssä Windows Updaten tilan
  päivitykset latauksen ja asennuksen edistyessä. Tämä voi aiheuttaa puheen
  keskeytymisen Asetukset-sovelluksessa navigoitaessa päivitysten lataamisen
  ja asennuksen aikana.

## Puhekäyttö

Tämä viittaa Puhekäyttö-ominaisuuteen, joka esiteltiin Windows 11:n
versiossa 22H2.

* NVDA ilmoittaa mikrofonin tilan, kun sitä muutetaan Puhekäytön
  käyttöliittymästä.

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
