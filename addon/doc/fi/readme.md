# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa sisältää kokoelman sovellusmoduuleja Windows 10:n mukana
tuleville sovelluksille sekä laajennuksia ja korjauksia tietyille
säätimille.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Hälytykset ja kello
* Kalenteri
* Laskin (moderni)
* Cortana
* Palautekeskus
* Pelipalkki
* Sähköposti
* Kartat
* Microsoft Edge
* Moderni näppäimistö (emojipaneelin/fyysisen näppäimistösyötteen ehdotukset
  versiossa 1709 ja uudemmissa)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Skype (universaali sovellus)
* Kauppa
* Sää
* Sekalaisia moduuleita sellaisille säätimille kuin Käynnistä-valikon
  tiilet.

Huom: Tämä lisäosa edellyttää Windows 10:n versiota 1703 (koontiversio
15063) tai uudempaa ja NVDA 2017.3:a tai uudempaa. Käytä parhaan
käyttökokemuksen varmistamiseksi Windows 10:n viimeisimpiä vakaita versioita
(koontiversio 16299 tai 17134) sekä uusinta NVDA:ta. Varmista myös, että
tallennat NVDA:n asetukset muutettuasi lisäosan päivitysasetuksia.

## Yleistä

* Alavalikot tunnistetaan oikein Käynnistä-valikon tiilien pikavalikoissa.
* Tietyt valintaikkunat tunnistetaan nyt asianmukaisesti valintaikkunoiksi,
  mukaan lukien Insider-esiversion valintaikkuna (Asetukset-sovellus).
* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa. Tätä toimintoa hallitaan "Lue objektien sijaintitiedot"
  -asetuksella Objektien lukuasetukset -valintaikkunasta.
* Sijaintitietoja (esim. 1 / 2) ei enää lueta tietyissä pikavalikoissa
  (kuten Edgessä).
* Seuraavat UIA-tapahtumat tunnistetaan: Ohjain kohteelle, vetämisen
  aloitus, vetämisen peruutus, vetäminen suoritettu, elementti valittu,
  aktiivisen alueen muutos, ilmoitus, järjestelmän ilmoitus, työkaluvihje
  avattu, ikkuna avattu. Näitä tapahtumia seurataan ja UIA-ilmoitustapahtuma
  ilmaistaan virheäänellä, kun NVDA:n lokitasoksi on määritetty
  "virheenkorjaus".
* Lisätty mahdollisuus päivitysten tarkistamiseen (automaattinen tai
  manuaalinen) NVDA:n Asetukset-valikosta löytyvän uuden Windows 10 App
  Essentials -valintaikkunan kautta. Vakaat ja kehitysversiot suorittavat
  oletuksena automaattisen päivitystarkistuksen viikoittain tai päivittäin.
* Joidenkin sovellusten Aktiivisen alueen teksti luetaan. Näitä ovat
  mm. Edgen ilmoitukset ja laskutoimitusten tulokset Laskimessa sekä
  muut. Huomaa, että tämä saattaa johtaa joissakin tapauksissa ilmoitusten
  kahdesti puhumiseen.
* Uusien sovellusversioiden ilmoitukset puhutaan Windows 10:n versiossa 1709
  (koontiversio 16299) ja uudemmissa. Teknisten rajoitusten vuoksi tämä
  ominaisuus toimii asianmukaisesti vain NVDA 2018.1:ssä tai
  uudemmissa. NVDA 2018.2 tulee sisältämään tämän toiminnallisuuden
  sisäänrakennettuna.
* Edgen ja universaalien sovellusten työkaluvihjeet tunnistetaan ja
  ilmoitetaan.
* NVDA ei enää ilmoita "tuntematon" pikalinkkivalikkoa (Windows+X)
  avattaessa. Tämä korjaus tulee sisältymään NVDA 2018.2:een.
* Kun koontiversiossa 17627 ja uudemmissa avataan uusi Sets-välilehti
  (Ctrl+Windows+T), NVDA ilmoittaa hakutulokset etsittäessä kohteita
  upotetussa Cortana-IKKUNASSA.
* NVDA ilmoittaa nykyisen työpöydän tunnisteen (esim. työpöytä 2)
  avattaessa, suljettaessa tai vaihdettaessa virtuaalityöpöytien välillä.

## Hälytykset ja kello

* Ajanvalitsimen arvot puhutaan - havaittavissa siirrettäessä kohdistusta
  valitsimen säätimiin. Tämä vaikuttaa myös säätimeen, jolla valitaan,
  milloin Windows käynnistetään uudelleen päivitysten asentamisen
  viimeistelemiseksi.

## Laskin

* NVDA ilmoittaa laskutoimituksen tuloksen Enteriä tai Esciä painettaessa.
* NVDA puhuu laskutoimitusten tulokset (esim. yksikkö- ja
  valuuttamuuntimessa) heti laskukaavoja syötettäessä.

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
  johtuen NVDA ei voi olla täysin vuorovaikutuksessa pelipalkin kanssa.

## Sähköposti

* Voit nyt käyttää viestiluettelon kohteita tarkastellessasi
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen.
* Ät-maininnan ehdotukset ilmaistaan äänimerkeillä viestiä kirjoitettaessa.

## Kartat

* NVDA soittaa äänimerkin karttasijainneille.
* NVDA ilmoittaa katuosoitteet käyttäessäsi nuolinäppäimiä kartalla
  liikkumiseen oltaessa street side -näkymässä ja mikäli "use keyboard"
  -vaihtoehto on otettu käyttöön.

## Microsoft Edge

* Ilmoitukset, kuten tiedostojen lataukset ja verkkosivujen näyttämät,
  luetaan.

## Moderni näppäimistö

* Tuki version 1709 (Fall Creators -päivitys) kelluvalle
  emojinsyöttöpaneelille. Käytä parhaan kokemuksen saamiseksi Windows
  OneCore -syntetisaattoria.
* Tuki fyysisen näppäimistösyötteen ehdotuksille versiossa 1803
  (koontiversio 17040) ja uudemmissa.
* NVDA ilmoittaa 1709:ää uudemmissa koontiversioissa ensimmäisen valitun
  emojin, kun emojipaneeli avautuu.

## Ihmiset

* Kontakteja etsittäessä toistetaan ääni, mikäli hakutuloksia on.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  puhutaan nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* Asetusryhmät tunnistetaan säätimien välillä liikuttaessa
  objektinavigointia käyttäen.
* NVDA ei enää epäonnistu joidenkin yhdistelmäruutujen selitteiden
  tunnistamisessa ja/tai arvomuutosten ilmoittamisessa.
* Edistymispalkkien äänimerkkejä ei enää kuulu muutettaessa
  äänenvoimakkuutta versiossa 1803 (koontiversio 17035) ja uudemmissa.

## Skype

* Kirjoitusilmaisimen teksti puhutaan kuten Skypen työpöytäversiossa.
* Osittainen Control+NVDA+numero-komentojen paluu tuoreen
  keskusteluhistorian lukemiseen sekä navigointiobjektin siirtämiseen
  keskustelukohteisiin kuten Skypen työpöytäversiossa.
* Voit nyt painaa Alt+numerorivin numeroita etsiäksesi kontaktiluettelon
  (1), keskustelut (2), botit (3) ja keskustelumuokkauskentän, mikäli se on
  näkyvissä (4) sekä siirtyäksesi niihin. Huomaa, että nämä komennot
  toimivat oikein, jos maaliskuussa 2017 julkistettu Skype-päivitys on
  asennettu.
* Marraskuussa 2016 julkaistun Skype-sovelluksen esiversion
  yhdistelmäruutujen selitteet puhutaan.
* NVDA ei enää sano "Skype-viesti" useimmissa tapauksissa viestejä
  tarkasteltaessa.
* Korjattu useita ongelmia, joita ilmeni käytettäessä Skypeä pistenäytön
  kanssa, mukaan lukien kyvyttömyys lukea viestihistorian kohteita
  pistekirjoituksella.
* NVDA kertoo nyt viestin tarkat tiedot, kuten kanavatyypin ja
  lähetyspäivämäärän sekä -kellonajan jne., painettaessa NVDA+D
  viestihistorialuettelon kohteen kohdalla.

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
