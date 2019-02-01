# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* NVDA-yhteensopivuus: 2018.3-2019.1

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
* Skype (universaali sovellus)
* Kauppa
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* Huom: Tämä lisäosa edellyttää Windows 10:n versiota 1803 (koontiversio
  17134) tai uudempaa ja NVDA 2018.3:a tai uudempaa. Käytä parhaan
  käyttökokemuksen varmistamiseksi Windows 10:n viimeisintä vakaata versiota
  (koontiversio 17763) sekä uusinta vakaata NVDA:n versiota.
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue vanhoja
  Windows 10 -versioita tai eivät ole enää käyttökelpoisia Windows 10:een ja
  sovelluksiin tehtyjen muutosten vuoksi.
* Tämän lisäosan sisäänrakennettu päivitystarkistustoiminto on
  poistettu. Käytä päivitysten tarkistamiseen Lisäosien päivittäjä
  -lisäosaa.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

* Sisäisiä muutoksia, jotka tekevät lisäosasta yhteensopivan tulevien
  NVDA-versioiden kanssa.
* Pieniä muutoksia siihen, miten jotkin muun kuin englanninkieliset
  ilmoitukset näytetään.
* Alavalikot tunnistetaan asianmukaisesti useissa sovelluksissa, mukaan
  lukien Käynnistä-valikon ruutujen tilannekohtaiset valikot ja microsoft
  Edgen sovellusvalikko (Redstone 5).
* ½Tietyt valintaikkunat tunnistetaan ja puhutaan nyt asianmukaisesti
  valintaikkunoina, mukaan lukien Insider-esiversion valintaikkuna
  (Asetukset-sovellus). Tämä sisältyy nyt NVDA 2018.3:een.
* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa. Tätä toimintoa hallitaan "Lue objektien sijaintitiedot"
  -asetuksella Objektien lukuasetukset -valintaikkunasta/paneelista.
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

## Toimintokeskus

* Kirkkaus-pikatoiminto on nyt vipupainikkeen sijasta painike. Tämä tulee
  sisältymään NVDA 2019.1:een.
* Useat tilojen, kuten Keskittymisavustajan ja kirkkauden, muutokset
  ilmoitetaan. Tämä tulee sisältymään NVDA 2019.1:een.

## Hälytykset ja kello

* Ajanvalitsimen arvot puhutaan - havaittavissa siirrettäessä kohdistusta
  valitsimen säätimiin. Tämä vaikuttaa myös säätimeen, jolla valitaan,
  milloin Windows käynnistetään uudelleen päivitysten asentamisen
  viimeistelemiseksi. Tämä tulee sisältymään NVDA 2019.1:een.

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
2018.3:een.

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
* NVDA ei toista enää virheääniä tai ole tekemättä mitään emojipaneelia
  suljettaessa uudemmissa 19H1-Insider-esiversioissa.
* NVDA ilmoittaa versiossa 1809 (October 2018 -päivitys) ja uudemmissa
  emojien hakutulokset, mikäli mahdollista.

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
* NVDA ei näytä enää tekevän mitään tai toista virheääniä, mikäli
  objektinavigointikomentoja käytetään tietyissä tilanteissa.
* Windows Updaten muistutusvalintaikkuna tunnistetaan asianmukaisesti
  valintaikkunaksi.

## Skype

Huom: alla mainitut kohdat eivät toimi oikein Skype 14:n universaalissa
sovelluksessa.

* Kirjoitusilmaisimen teksti puhutaan kuten Skypen työpöytäversiossa.
* Ctrl+NVDA+numero-komennot, joita käytetään uusimman keskusteluhistorian
  lukemiseen sekä navigointiobjektin siirtämiseen keskustelukohteisiin
  Skypen työpöytäversiossa, ovat käytettävissä myös Skypen UWP-versiossa.
* Voit nyt painaa Alt+numerorivin numeroita etsiäksesi kontaktiluettelon
  (1), keskustelut (2), botit (3) ja keskustelumuokkauskentän, mikäli se on
  näkyvissä (4) sekä siirtyäksesi niihin. Huomaa, että nämä komennot
  toimivat oikein vain, jos maaliskuussa 2017 julkistettu Skype-päivitys on
  asennettu.
* NVDA ei enää sano "Skype-viesti" useimmissa tapauksissa viestejä
  tarkasteltaessa.
* NVDA kertoo nyt viestin tarkat tiedot, kuten kanavatyypin ja
  lähetyspäivämäärän sekä -kellonajan jne., kun sen kohdalla
  viestihistorialuettelossa painetaan NVDA+D.

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
