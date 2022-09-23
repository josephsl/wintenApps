# Windows App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* Yhteensopivuus: NVDA 2022.2 ja uudemmat

Huom: Tämä lisäosa (alkuperäiseltä nimeltään Windows 10 App Essentials) on
nimetty uudelleen Windows App Essentialsiksi vuonna 2021 tukemaan Windows
10:tä sekä tulevia versioita, kuten Windows 11:tä. Lisäosassa viitataan
vielä osittain vanhaan nimeen.

Tämä lisäosa on kokoelma sovellusmoduuleita moderneille
Windows-sovelluksille sekä laajennuksia ja korjauksia tietyille säätimille
Windows 10:ssä ja uudemmissa.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Cortana
* Kartat
* Moderni näppäimistö (emojipaneeli/sanelu/puhekirjoitus/fyysisen
  näppäimistösyötteen ehdotukset/leikepöydän historia/ehdotetut toiminnot
  (esiversio)/modernin syöttömenetelmän muokkaimet)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Puhekäyttö (Windows 11 22H2)
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* Tämä lisäosa edellyttää Windows 10:n versiota 21H2 (koontiversio 19044),
  11:n versiota 21H2 (koontiversio 22000) tai uudempaa.
* Tämä lisäosa ei tue Windows 10 Enterprise LTSC:tä (Long-Term Servicing
  Channel) eikä Windows Server -versioita, vaikka asennus onkin mahdollista.
* Windows App Essentials ei asennu ei-tuetuissa Windows-versioissa, jos
  Lisäosien päivittäjä 22.08 tai uudempi on asennettuna ja lisäosien
  taustapäivitykset ovat käytössä.
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

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect.
* NVDA ilmoittaa aktiivisen virtuaalityöpöydän nimen (esim. työpöytä 2)
  avattaessa, suljettaessa, uudelleenjärjestettäessä (Windows 11) tai
  siirryttäessä niiden välillä.
* Kun kohteita vedetään ja pudotetaan, esim. järjesteltäessä kiinnitettyjä
  kohteita (ruutuja Windows 10:ssä) Käynnistä-valikossa tai
  Toimintokeskuksen pikatoimintoja Alt+Vaihto+nuolinäppäimillä, NVDA sanoo
  "vedetään" ja/tai vetämisen ja pudottamisen  vaikutukset ennen kohteiden
  vetämistä ja sen aikana. Tämän ilmoituksen puhuminen sisältyy NVDA
  2022.4:ään.
* Ilmoitukset, kuten äänenvoimakkuuden/kirkkauden muutokset
  resurssienhallinnassa sekä sovellusten päivitysilmoitukset Microsoft
  Storesta voidaan estää poistamalla käytöstä Lue ilmoitukset -asetus NVDA:n
  objektien lukemisen asetuksista.
* Mikrofonin mykistyksen (Win+Alt+K) tila ilmoitetaan nyt kaikkialta Windows
  11:n versiossa 22H2 ja sitä uudemmissa.

## Cortana

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa.
* NVDA on hiljaa puhuttaessa Cortanalle mikrofonin välityksellä.

## Kartat

* NVDA toistaa äänimerkin karttasijainneille.

## Moderni näppäimistö

Näitä ovat emojipaneeli, leikepöydän historia, sanelu/puhekirjoitus,
ehdotukset syötettäessä tekstiä fyysisellä näppäimistöllä, ehdotetut
toiminnot (esiversio) sekä modernin syöttömenetelmän editorit tietyille
kielille. Ota käyttöön emojeita tarkasteltaessa Unicode-konsortion datan
asetus NVDA:n puheasetuksista parhaan kokemuksen saamiseksi, ja aseta
symbolitasoksi "jotain" tai korkeampi. Kun liität leikepöydän historiasta,
liitä valittu kohde painamalla välilyöntinäppäintä Enterin sijaan. NVDA
tukee lisäksi päivitettyä syöttökokemuksen paneelia Windows 11:ssä.

* In Windows 10 emoji panel, when an emoji group (including kaomoji and
  symbols group) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Selaustila poistetaan käytöstä oletusarvoisesti Windows 11:n leikepöydän
  historiassa, minkä tarkoituksena on mahdollistaa NVDA:lle historian
  valikkokohteiden lukeminen.
* Insider-esikoontiversiossa 25115 ja sitä uudemmissa (taaksepäin sovitettu
  Windows 11:n beeta-koontiversioon 22622) NVDA ilmoittaa ehdotetut
  toiminnot, kun leikepöydälle kopioidaan yhteensopivaa dataa, kuten
  puhelinnumeroita.

## Ihmiset

* When searching for contacts, first suggestion will be announced.

## Asetukset

* NVDA puhuu valinnaisen laatupäivityksen säätimen nimen (Lataa ja asenna
  nyt -linkki Windows 10:ssä, Lataa-painike Windows 11:ssä), mikäli
  sellainen on näkyvissä.
* Navigointipolkupalkin kohteet tunnistetaan oikein Windows 11:ssä.
* NVDA keskeyttää puheen ja ilmoittaa Windows 10 ja 11 22H2:ssa ja
  uudemmissa Windows Updaten tilan päivitysten latauksen ja asennuksen
  edistyessä. Tämä voi aiheuttaa puheen keskeytymisen
  Asetukset-sovelluksessa navigoitaessa päivitysten lataamisen ja asennuksen
  aikana. Mikäli käytetään Windows 11 22H2:ta tai sitä uudempaa ja
  valikoivan UIA-tapahtumien rekisteröinti on käytössä, kohdistus on
  siirrettävä päivitysten luetteloon heti niiden ilmestyessä, jotta NVDA voi
  ilmoittaa päivityksen edistymisen.

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
