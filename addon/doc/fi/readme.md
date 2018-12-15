# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* NVDA compatibility: 2018.3 to 2019.1

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
* Pelipalkki
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
* Sekalaisia moduuleita sellaisille säätimille kuin Käynnistä-valikon
  tiilet.

Huomautuksia:

* Huom: Tämä lisäosa edellyttää Windows 10:n versiota 1709 (koontiversio
  16299) tai uudempaa ja NVDA 2018.3:a tai uudempaa. Käytä parhaan
  käyttökokemuksen varmistamiseksi Windows 10:n viimeisintä vakaata versiota
  (koontiversio 17763) sekä uusinta NVDA:ta.
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue vanhoja
  Windows 10 -versioita tai eivät ole enää käytettävissä sovelluksiin
  tehtyjen muutosten vuoksi.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

* Sisäisiä muutoksia, jotka tekevät lisäosasta yhteensopivan tulevien
  NVDA-versioiden kanssa.
* Jos Lisäosien päivittäjä -lisäosa on asennettuna, se tarkistaa Windows 10
  App Essentialsin päivitykset.
* Sekä vakaiden että kehitysversioiden päivitykset tarkistetaan nyt
  oletusarvoisesti viikon välein. Tämä pitää paikkansa vain, mikäli käytössä
  on lisäosan oma päivitystentarkistustoiminto.
* Jos lisäosa on määritetty tarkistamaan päivityksensä ja mikäli uusi versio
  vaatii päivitettäessä uudemman NVDA-version, siitä ilmoittava
  virheilmoitus näytetään.
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
* Uusien sovellusversioiden ilmoitukset puhutaan Windows 10:n versiossa 1709
  (koontiversio 16299) ja uudemmissa. NVDA 2018.2 ja uudemmat tukevat tätä,
  ja 2018.3 lisää tuen entistä useammille ilmoituksille.
* Edgen ja universaalien sovellusten työkaluvihjeet tunnistetaan ja
  ilmoitetaan.
* NVDA ilmoittaa nykyisen työpöydän tunnisteen (esim. työpöytä 2)
  avattaessa, suljettaessa tai vaihdettaessa virtuaalityöpöytien välillä.
* NVDA ei enää ilmoita Käynnistä-valikon kokoa  näytön resoluutiota tai
  suuntaa vaihdettaessa.

## Toimintokeskus

* Kirkkaus-pikatoiminto on nyt vipupainikkeen sijasta painike.
* Useat tilojen, kuten Keskittymisavustajan ja kirkkauden, muutokset
  ilmoitetaan.

## Hälytykset ja kello

* Ajanvalitsimen arvot puhutaan - havaittavissa siirrettäessä kohdistusta
  valitsimen säätimiin. Tämä vaikuttaa myös säätimeen, jolla valitaan,
  milloin Windows käynnistetään uudelleen päivitysten asentamisen
  viimeistelemiseksi.

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

## Pelipalkki

* NVDA ilmoittaa pelipalkki-ikkunan ilmestymisestä. Teknisistä rajoituksista
  johtuen NVDA ei voi olla täysin vuorovaikutuksessa pelipalkin kanssa ennen
  koontiversiota 17723.

## Sähköposti

* Voit nyt käyttää viestiluettelon kohteita tarkastellessasi
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen. Huomaa, että
  rivien (viestien) välillä liikkumista ei tueta.
* Ät-maininnan ehdotukset ilmaistaan äänimerkeillä viestiä kirjoitettaessa.

## Kartat

* NVDA soittaa äänimerkin karttasijainneille.
* NVDA ilmoittaa katuosoitteet käyttäessäsi nuolinäppäimiä kartalla
  liikkumiseen oltaessa street side -näkymässä ja mikäli "use keyboard"
  -vaihtoehto on otettu käyttöön.

## Microsoft Edge

* Ilmoitukset, kuten tiedostojen lataukset ja verkkosivujen näyttämät, sekä
  lukunäkymän saatavuus (mikäli käytetään versiota 1709) puhutaan.
* Tekstin automaattista täydennystä seurataan ja siitä ilmoitetaan
  osoitepalkissa.

## Moderni näppäimistö

Huom: suurin osa alla luetelluista ominaisuuksista sisältyy nyt NVDA
2018.3:een.

* Tuki version 1709 (Fall Creators -päivitys) ja uudempien kelluvalle
  emojinsyöttöpaneelille, mukaan lukien version 1809 (koontiversio 17661 ja
  uudemmat) uudelleensuunniteltu paneeli sekä versioon 19H1 (koontiversio
  18262) tehdyt muutokset. Käytä parhaan kokemuksen saamiseksi Windows
  OneCore -syntetisaattoria.
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
* NVDA ei enää toista virheääniä tai ole tekemättä mitään emojipaneelia
  suljettaessa uudemmissa Insider-esiversioissa.
* NVDA ilmoittaa emojien hakutulokset, mikäli mahdollista.

## Ihmiset

* Ensimmäinen ehdotus puhutaan kontakteja etsittäessä, erityisesti uusimpia
  sovellusversioita käytettäessä.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  mukaan lukien Tallennusseurannan/Levynsiivouksen pienoisohjelma, puhutaan
  nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* Asetusryhmät tunnistetaan säätimien välillä liikuttaessa
  objektinavigointia käyttäen.
* NVDA ei enää epäonnistu joidenkin yhdistelmäruutujen ja
  valintapainikkeiden selitteiden tunnistamisessa ja/tai arvomuutosten
  ilmoittamisessa.
* Edistymispalkkien äänimerkkejä ei enää kuulu muutettaessa
  äänenvoimakkuutta versiossa 1803 ja uudemmissa.
* Windows Updaten tilailmoituksia puhutaan enemmän etenkin virheitä
  havaittaessa.
* NVDA ei näytä enää tekevän mitään tai toista virheääniä, mikäli
  objektinavigointikomentoja käytetään tietyissä tilanteissa.
* Useilla koontiversioon 18282 lisätyillä linkeillä on nyt selitteet.
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
