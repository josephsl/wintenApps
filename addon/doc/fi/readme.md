# Windows App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut
* Lataa [vakaa versio][1]
* Lataa [beetaversio][2]
* Lataa [kehitysversio][3]
* Yhteensopivuus: NVDA 2023.1 ja uudemmat

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

Huomautukset:

* Tämä lisäosa edellyttää Windows 10:n versiota 22H2 (koontiversio 19045),
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
* Jotkin lisäosan ominaisuudet sisältyvät tai tulevat sisältymään NVDA:han.
* Saat parhaan kokemuksen verkkotekniikoita ja -sisältöä hyödyntävistä
  sovelluksista, kuten Käynnistä-valikosta ja sen pikavalikosta, ottamalla
  käyttöön "Automaattinen vuorovaikutustila kohdistuksen muuttuessa"
  -asetuksen NVDA:n Selaustila-asetuspaneelista.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokit][4] -dokumentista.

## Yleistä

* NVDA ilmoittaa aktiivisen virtuaalityöpöydän nimen (esim. työpöytä 2)
  avattaessa, suljettaessa tai siirryttäessä virtuaalityöpöytien välillä.
* Paranneltu Windows 10:n ja 11:n tehtäväpalkin kokemusta, mukaan lukien
  kuvakkeiden uudelleenjärjestämisen tulosten puhuminen painettaessa
  Alt+Vaihto+Vasen/Oikea nuolinäppäin (Windows 11) ja kohteen sijainnin
  ilmoittaminen tehtäväpalkin kuvakkeiden välillä liikuttaessa (Windows 10
  ja 11).
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

* NVDA ilmoittaa ehdotetut toiminnot Windows 11 22H2:ssa ja uudemmissa, kun
  leikepöydälle kopioidaan yhteensopivaa dataa, kuten puhelinnumeroita.

## Asetukset

* NVDA puhuu valinnaisen laatupäivityksen säätimen nimen (Lataa ja asenna
  nyt -linkki Windows 10:ssä, Lataa-painike Windows 11:ssä), mikäli
  sellainen on näkyvissä.
* Navigointipolkupalkin kohteet tunnistetaan oikein Windows 11:ssä.
* NVDA ilmoittaa Windows Updaten tilan päivitysten latauksen ja asennuksen
  edistyessä. Tästä voi olla seurauksena puheen keskeytyminen navigoitaessa
  Asetukset-sovelluksessa päivitysten lataamisen ja asennuksen
  aikana. Mikäli käytetään Windows 11:tä ja valikoiva UIA-tapahtumien
  rekisteröinti on käytössä tai määritetty valikoivaksi, kohdistus on
  siirrettävä päivitysluetteloon heti niiden ilmestyessä, jotta NVDA voi
  ilmoittaa päivityksen edistymisen.

## Puhekäyttö

Tämä viittaa Puhekäyttö-ominaisuuteen, joka esiteltiin Windows 11:n
versiossa 22H2.

* NVDA ilmoittaa mikrofonin tilan, kun sitä muutetaan Puhekäytön
  käyttöliittymästä.

## Sää

* Sellaiset välilehdet kuten "ennuste" ja "kartat" tunnistetaan oikeiksi
  välilehdiksi (korjauksen tehnyt Derek Riemer).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
