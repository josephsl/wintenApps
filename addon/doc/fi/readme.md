# Windows App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut
* Lataa [vakaa versio][1]
* Lataa [beetaversio][2]
* Lataa [kehitysversio][3]
* Yhteensopivuus: NVDA 2022.4 ja uudemmat

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
* Moderni näppäimistö
  (emojipaneeli/kosketusnäppäimistö/sanelu/puhekirjoitus/fyysisen
  näppäimistösyötteen ehdotukset/leikepöydän historia/ehdotetut
  toiminnot/modernin syöttömenetelmän muokkaimet)
* Asetukset (järjestelmän asetukset, Windows+I)
* Puhekäyttö (Windows 11 22H2)
* Sää
* Sekalaisia moduuleita säätimille ja ominaisuuksille, kuten
  virtuaalityöpöytien ilmoitukset.

Huomautuksia:

* Tämä lisäosa edellyttää Windows 10:n versiota 21H2 (koontiversio 19044),
  11:n versiota 21H2 (koontiversio 22000) tai uudempaa.
* Ominaisuuspäivityksen tuen kesto on sidottu kuluttajatuen kestoon (Home,
  Pro, Pro Education, Pro for Workstations -versiot), ja lisäosa saattaa
  lopettaa tuen ominaisuuspäivitykselle jo ennen kuluttajatuen
  päättymistä. Katso lisätietoja ja tukipäivämäärät osoitteesta
  aka.ms/WindowsTargetVersioninfo.
* Tämä lisäosa ei tue Windows 10 Enterprise LTSC:tä (Long-Term Servicing
  Channel) eikä Windows Server -versioita, vaikka asennus onkin mahdollista.
* Windows App Essentials ei asennu ei-tuetuissa Windows-versioissa, jos
  Lisäosien päivittäjä on asennettuna ja lisäosien taustapäivitykset ovat
  käytössä.
* Kaikkia Windowsin Insider-esikoontiversioiden ominaisuuksia ei tueta,
  varsinkaan sellaisia, jotka esitellään vain osalle canary- ja
  dev-kanavilla olevista käyttäjistä.
* Lisäosan dev-kanava sisältää muutoksia, mukaan lukien kokeellinen sisältö,
  joka saatetaan sisällyttää beeta- ja vakaisiin versioihin, ja beta-kanava
  sisältää tuleviin vakaisiin versioihin suunniteltuja muutoksia.
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Saat parhaan kokemuksen verkkotekniikoita ja -sisältöä hyödyntävistä
  sovelluksista, kuten Käynnistä-valikosta ja sen pikavalikosta, ottamalla
  käyttöön "Automaattinen vuorovaikutustila kohdistuksen muuttuessa"
  -asetuksen NVDA:n Selaustila-asetuspaneelista.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokit][4] -dokumentista.

## Yleistä

* NVDA ilmoittaa aktiivisen virtuaalityöpöydän nimen (esim. työpöytä 2)
  avattaessa, suljettaessa tai siirryttäessä virtuaalityöpöytien välillä.
* NVDA ilmoittaa Windows 11:ssä haun kohokohdat Käynnistä-valikossa sen
  avautuessa. Tämä sisältyy NVDA 2023.1:een.
* Windows 11 22H2:ssa ja uudemmissa voidaan nyt käyttää hiirtä ja/tai
  kosketuseleitä vuorovaikutuksessa uudelleensuunnitellun ilmaisinalueen
  ylivuotoikkunan ja Avaa sovelluksessa -valintaikkunan kanssa. Tämä
  sisältyy NVDA 2023.1:een.
* NVDA tallentaa käynnistyessään nykyisen Windows-asennuksen
  suoritinarkkitehtuurin (x86/32-bittinen, AMD64, ARM64). Tämä sisältyy NVDA
  2023.1:een.
* Paranneltu Windows 10:n ja 11:n tehtäväpalkin kokemusta, mukaan lukien
  kuvakkeiden uudelleenjärjestämisen tulosten puhuminen painettaessa
  Alt+Vaihto+Vasen/Oikea nuolinäppäin (Windows 11 ennen koontiversiota
  25267) ja kohteen sijainnin ilmoittaminen tehtäväpalkin kuvakkeiden
  välillä liikuttaessa (Windows 10 ja 11 ennen koontiversiota 25281).
* NVDA ilmoittaa tyhjästä kansiosta, kun sellainen avataan
  Resurssienhallinnassa.
* NVDA puhuu välilehtien nimen ja sijainnin niiden välillä vaihdettaessa
  sellaisissa sovelluksissa, joissa välilehti-ikkunoita tuetaan
  (esim. Resurssienhallinta ja Muistio). Tämä sisältyy NVDA 2023.2:een.

## Cortana

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa.

## Kartat

* NVDA ei enää keskeytä puhetta joissakin tapauksissa, kun kohdistus on
  muissa kohteissa kuin karttasäätimessä.

## Moderni näppäimistö

Näitä ovat emojipaneeli, leikepöydän historia, kosketusnäppäimistö,
sanelu/puhekirjoitus, ehdotukset syötettäessä tekstiä fyysisellä
näppäimistöllä, ehdotetut toiminnot sekä modernin syöttömenetelmän editorit
tietyille kielille Windows 10:ssä ja 11:ssä. Ota käyttöön emojeita
tarkasteltaessa Unicode-konsortion datan asetus NVDA:n puheasetuksista
parhaan kokemuksen saamiseksi, ja aseta symbolitasoksi "jotain" tai
korkeampi. Kun liität leikepöydän historiasta, liitä valittu kohde
painamalla Välilyönti-näppäintä Enterin sijaan.

* Kun emojiryhmä (kaomoji ja symboliryhmä mukaan lukien) valitaan Windows
  10:n emojipaneelissa, NVDA ei enää siirrä navigointiobjektia tiettyihin
  emojeihin.
* Selaustila poistetaan käytöstä oletusarvoisesti Windows 11:n leikepöydän
  historiassa, minkä tarkoituksena on mahdollistaa NVDA:lle historian
  valikkokohteiden lukeminen. Tämä sisältyy NVDA 2023.1:een.
* NVDA ilmoittaa ehdotetut toiminnot Windows 11 22H2:ssa ja uudemmissa, kun
  leikepöydälle kopioidaan yhteensopivaa dataa, kuten puhelinnumeroita.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
