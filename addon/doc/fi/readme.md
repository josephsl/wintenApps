# Windows App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut
* Lataa [vakaa versio][1]
* Lataa [beetaversio][2]
* Lataa [kehitysversio][3]
* Yhteensopivuus: NVDA 2023.3.4 ja uudemmat

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
* Asetukset (järjestelmän asetukset, Windows+I)

Huomautukset:

* Tämä lisäosa edellyttää Windows 10:n versiota 22H2 (koontiversio 19045),
  11:n versiota 22H2 (koontiversio 22621) tai uudempaa.
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
[lisäosajulkaisujen muutoslokit][4] -dokumentista.

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

## Asetukset

* NVDA ilmoittaa Windows Updaten tilan päivitysten latauksen ja asennuksen
  edistyessä. Tästä voi olla seurauksena puheen keskeytyminen navigoitaessa
  Asetukset-sovelluksessa päivitysten lataamisen ja asennuksen
  aikana. Mikäli käytetään Windows 11:tä ja UIA-tapahtumien rekisteröinti on
  määritetty valikoivaksi NVDA:n Lisäasetukset-paneelissa, kohdistus on
  siirrettävä päivitysten luetteloon heti niiden ilmestyessä, jotta NVDA voi
  ilmoittaa päivityksen edistymisen.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
