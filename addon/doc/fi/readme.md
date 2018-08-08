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
  16299) tai uudempaa ja NVDA 2018.2:ta tai uudempaa. Käytä parhaan
  käyttökokemuksen varmistamiseksi Windows 10:n viimeisintä vakaata versiota
  (koontiversio 17134) sekä uusinta NVDA:ta.
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue vanhoja
  Windows 10 -versioita tai eivät ole enää käytettävissä sovelluksiin
  tehtyjen muutosten vuoksi.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

* Alavalikot tunnistetaan asianmukaisesti useissa sovelluksissa, mukaan
  lukien Käynnistä-valikon ruutujen tilannekohtaiset valikot ja microsoft
  Edgen sovellusvalikko (Redstone 5).
* Tietyt valintaikkunat tunnistetaan ja puhutaan nyt asianmukaisesti
  valintaikkunoina, mukaan lukien Insider-esiversion valintaikkuna
  (Asetukset-sovellus).
* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa. Tätä toimintoa hallitaan "Lue objektien sijaintitiedot"
  -asetuksella Objektien lukuasetukset -valintaikkunasta/paneelista.
* Sijaintitietoja (esim. 1 / 2) ei enää lueta tietyissä pikavalikoissa
  (kuten Edgessä).
* Seuraavat UIA-tapahtumat tunnistetaan: sijainnin muutos aktiivisessa
  tekstissä, ohjain kohteelle, vetämisen aloitus, vetämisen peruutus,
  vetäminen suoritettu, elementti valittu, aktiivisen alueen muutos,
  ilmoitus, järjestelmän ilmoitus, työkaluvihje avattu, ikkuna avattu. Näitä
  tapahtumia seurataan ja UIA-ilmoitustapahtuma ilmaistaan virheäänellä, kun
  NVDA:n lokitasoksi on määritetty "virheenkorjaus".
* Lisätty mahdollisuus päivitysten tarkistamiseen (automaattinen tai
  manuaalinen) NVDA:n Asetukset-valikosta löytyvän uuden Windows 10 App
  Essentials -valintaikkunan kautta. Vakaat ja kehitysversiot suorittavat
  oletuksena automaattisen päivitystarkistuksen viikoittain tai päivittäin.
* Joidenkin sovellusten Aktiivisen alueen teksti luetaan. Näitä ovat
  mm. Edgen ilmoitukset (mukaan lukien elementit, jotka on merkitty
  aria-role=alert-ominaisuudella) ja laskutoimitusten tulokset Laskimessa
  sekä muut. Huomaa, että tämä saattaa johtaa joissakin tapauksissa
  ilmoitusten kahdesti puhumiseen.
* Uusien sovellusversioiden ilmoitukset puhutaan Windows 10:n versiossa 1709
  (koontiversio 16299) ja uudemmissa.
* Edgen ja universaalien sovellusten työkaluvihjeet tunnistetaan ja
  ilmoitetaan.
* Kun Sets on otettu käyttöön (koontiversiot 17627-17692 joillakin Windows
  Insider -ohjelmaan liittyneillä), NVDA ilmoittaa uutta välilehteä
  avattaessa (Ctrl+Win+T) hakutulokset etsittäessä kohteita upotetussa
  Cortana-IKKUNASSA.
* Kun Sets on otettu käyttöön, NVDA ilmoittaa välilehteä vaihdettaessa sen
  nimen ja sijainnin, johon olet siirtymässä.
* NVDA ilmoittaa nykyisen työpöydän tunnisteen (esim. työpöytä 2)
  avattaessa, suljettaessa tai vaihdettaessa virtuaalityöpöytien välillä.
* NVDA ei enää ilmoita Käynnistä-valikon kokoa  näytön resoluutiota tai
  suuntaa vaihdettaessa.

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
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen.
* Ät-maininnan ehdotukset ilmaistaan äänimerkeillä viestiä kirjoitettaessa.

## Kartat

* NVDA soittaa äänimerkin karttasijainneille.
* NVDA ilmoittaa katuosoitteet käyttäessäsi nuolinäppäimiä kartalla
  liikkumiseen oltaessa street side -näkymässä ja mikäli "use keyboard"
  -vaihtoehto on otettu käyttöön.

## Microsoft Edge

* Ilmoitukset, kuten tiedostojen lataukset ja verkkosivujen näyttämät, sekä
  lukunäkymän saatavuus (mikäli käytetään versiota 1709) puhutaan.

## Moderni näppäimistö

* Tuki version 1709 (Fall Creators -päivitys) ja uudempien kelluvalle
  emojinsyöttöpaneelille, mukaan lukien koontiversion 17661 ja uudempien
  uudelleensuunniteltu paneeli. Käytä parhaan kokemuksen saamiseksi Windows
  OneCore -syntetisaattoria.
* Tuki fyysisen näppäimistösyötteen ehdotuksille versiossa 1803 (April 2018
  -päivitys) ja uudemmissa.
* NVDA ilmoittaa 1709:ää uudemmissa koontiversioissa ensimmäisen valitun
  emojin, kun emojipaneeli avautuu.
* Tuki pilvileikepöydän kohteiden ilmoittamiselle koontiversiossa 17666
  (Redstone 5) ja uudemmissa.
* Puheliaisuutta vähennetty modernia näppäimistöä ja sen ominaisuuksia
  käytettäessä. Fyysisen näppäimistön syöttöehdotuksia avattaessa ei enää
  sanota "Microsoft Candidate UI" sekä ollaan hiljaa tilanteessa, jossa
  tietyt kosketusnäppäimistön näppäimet aiheuttavat joissakin järjestelmissä
  muuttuneen nimitapahtuman.

## Ihmiset

* Ensimmäinen ehdotus puhutaan kontakteja etsittäessä, erityisesti uusimpia
  sovellusversioita käytettäessä.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  puhutaan nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* Asetusryhmät tunnistetaan säätimien välillä liikuttaessa
  objektinavigointia käyttäen.
* NVDA ei enää epäonnistu joidenkin yhdistelmäruutujen selitteiden
  tunnistamisessa ja/tai arvomuutosten ilmoittamisessa.
* Edistymispalkkien äänimerkkejä ei enää kuulu muutettaessa
  äänenvoimakkuutta versiossa 1803 ja uudemmissa.
* Windows Updaten tilailmoituksia puhutaan enemmän etenkin virheitä
  havaittaessa.

## Skype

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
