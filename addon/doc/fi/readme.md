# Windows App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut

Huom: Tämä lisäosa (alkuperäiseltä nimeltään Windows 10 App Essentials) on
nimetty uudelleen Windows App Essentialsiksi vuonna 2021 tukemaan Windows
10:tä sekä tulevia versioita, kuten Windows 11:tä. Lisäosassa viitataan
vielä osittain vanhaan nimeen.

Tämä lisäosa on kokoelma sovellusmoduuleita moderneille
Windows-sovelluksille sekä laajennuksia ja korjauksia tietyille säätimille
Windows 10:ssä ja uudemmissa.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Moderni näppäimistö
* Asetukset (Windows+I)

Huomautukset:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* Ominaisuuspäivityksen tuen kesto on sidoksissa kuluttajatuen kestoon
  (Home, Pro, Pro Education, Pro for Workstations -versiot), ja lisäosa
  saattaa lopettaa tuen ominaisuuspäivitykselle jo ennen kuluttajatuen
  päättymistä. Katso lisätietoja ja tukipäivämäärät osoitteesta
  <https://aka.ms/WindowsTargetVersioninfo>.
* Tämä lisäosa ei tue Windows 10 Enterprise LTSC:tä (Long-Term Servicing
  Channel) eikä Windows Server -versioita, vaikka asennus onkin mahdollista.
* Kaikkia Windowsin Insider-esikoontiversioiden ominaisuuksia ei tueta,
  varsinkaan sellaisia, jotka esitellään vain osalle canary- ja
  dev-kanavilla olevista käyttäjistä.
* Lisäosa saattaa jäljitellä Insider-esiversioihin sisällytettyjä
  korjauksia, jotka poistetaan myöhemmin. Näihin muutoksiin liittyen
  korjaukset saatetaan poistaa lisäosan tulevissa versioissa.
* Lisäosan dev-kanava sisältää muutoksia, mukaan lukien kokeellinen sisältö,
  joka saatetaan sisällyttää beeta- ja vakaisiin versioihin, ja beta-kanava
  sisältää tuleviin vakaisiin versioihin suunniteltuja muutoksia.
* Jotkin lisäosan ominaisuudet sisältyvät tai tulevat sisältymään NVDA:han.
* Saat parhaan kokemuksen verkkotekniikoita ja -sisältöä hyödyntävistä
  sovelluksista, kuten Käynnistä-valikosta ja sen pikavalikosta, ottamalla
  käyttöön "Automaattinen vuorovaikutustila kohdistuksen muuttuessa"
  -asetuksen NVDA:n Selaustila-asetuspaneelista.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokit][1] -dokumentista.

## Moderni näppäimistö

Näitä ovat emojipaneeli, leikepöydän historia, kosketusnäppäimistö,
sanelu/puhekirjoitus, ehdotukset syötettäessä tekstiä fyysisellä
näppäimistöllä, ehdotetut toiminnot sekä modernin syöttömenetelmän editorit
tietyille kielille Windows 10:ssä ja 11:ssä. Ota käyttöön emojeita
tarkasteltaessa Unicode-konsortion datan asetus NVDA:n puheasetuksista
parhaan kokemuksen saamiseksi, ja aseta symbolitasoksi "jotain" tai
korkeampi. Kun liität leikepöydän historiasta, liitä valittu kohde
painamalla Välilyönti-näppäintä Enterin sijaan.

* NVDA ilmoittaa ehdotetut toiminnot Windows 11:ssä, kun leikepöydälle
  kopioidaan yhteensopivaa dataa, kuten puhelinnumeroita. Tämä sisältyy NVDA
  2024.2:een.

## Asetukset (Windows+I)

* NVDA will report updates to Windows Update status as download and install
  progresses. In Windows 10, this may result in speech interruption when
  navigating Settings app while updates are being downloaded and
  installed. In Windows 11, object navigation can be used in updates list to
  review update status for individual entries.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
