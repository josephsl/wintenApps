# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* Yhteensopivuus: NVDA 2019.3 ja uudemmat
* Lataa [vanhempi versio,][4] joka on yhteensopiva NVDA 2019.2.1:n ja sitä
  vanhempien kanssa

Tämä lisäosa sisältää kokoelman sovellusmoduuleja Windows 10:n mukana
tuleville sovelluksille sekä laajennuksia ja korjauksia tietyille
säätimille.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Laskin (moderni)
* Kalenteri
* Cortana (keskustelut)
* Sähköposti
* Kartat
* Microsoft Store
* Moderni näppäimistö (emojipaneeli/sanelu/fyysisen näppäimistösyötteen
  ehdotukset/pilvileikepöydän historia/modernin syöttömenetelmän editorit)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* Tämä lisäosa edellyttää Windows 10:n versiota 1903 (koontiversio 18362)
  tai uudempaa. Käytä parhaan käyttökokemuksen varmistamiseksi Windows 10:n
  viimeisintä vakaata versiota (koontiversio 18363).
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue vanhoja
  Windows 10 -versioita tai eivät ole enää käyttökelpoisia Windows 10:een ja
  sovelluksiin tehtyjen muutosten vuoksi.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

* NVDA ei toista enää virheääniä tai tee mitään, mikäli tämä lisäosa
  aktivoituu Windows 7:ssä, 8.1:ssä tai sellaisissa Windows 10:n versioissa,
  joita ei enää tueta.
* Entistä enemmän valintaikkunoita tunnistetaan ja ilmoitetaan nyt
  asianmukaisesti valintaikkunoina, mukaan lukien Insider-esiversion
  valintaikkuna (Asetukset-sovellus). Tämä sisältyy nyt NVDA 2018.3:een.
* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa. Tätä toimintoa hallitaan "Lue objektien sijaintitiedot"
  -asetuksella Objektien lukeminen -paneelista NVDA:n asetuksista.
* NVDA puhuu nyt etsittäessä vähemmän hakutuloksia kahdesti
  Käynnistä-valikossa tai Resurssienhallinnassa versiossa 1909 (November
  2019 -päivitys) ja uudemmissa, mikä tekee lisäksi
  pistekirjoitustulosteesta yhdenmukaisempaa kohteita tarkasteltaessa.
* Seuraavat UIA-tapahtumat tunnistetaan: ohjain kohteelle, vetämisen
  aloitus, vetämisen peruutus, vetäminen suoritettu, vetämisen kohteeseen
  siirtyminen, vetämisen kohteesta poistuminen, vetämisen kohde pudotettu,
  elementti valittu, kohteen tila, aktiivisen alueen muutos, ilmoitus,
  järjestelmän ilmoitus, työkaluvihje avattu, ikkuna avattu. Näitä
  tapahtumia seurataan, kun NVDA:n lokitasoksi on määritetty
  "virheenkorjaus", ja UIA-ilmoitustapahtuma ilmaistaan virheäänellä, mikäli
  ilmoitukset tulevat muualta kuin aktiivisesta sovelluksesta.
* On mahdollista seurata vain tiettyjä tapahtumia ja/tai tietyistä
  sovelluksista tulevia tapahtumia.
* NVDA ilmoittaa nykyisen työpöydän tunnisteen (esim. työpöytä 2) avattaessa
  ja suljettaessa virtuaalityöpöytiä tai siirryttäessä niiden välillä.
* NVDA ei enää ilmoita Käynnistä-valikon kokoa  näytön resoluutiota tai
  suuntaa vaihdettaessa.
* Kun Käynnistä-valikon ruutuja tai Toimintokeskuksen pikatoimintoja
  järjestellään Alt+Vaihto+nuolinäppäimillä, NVDA puhuu raahattujen
  kohteiden tiedot tai raahatun kohteen uuden sijainnin.

## Laskin

* NVDA ilmoittaa laskutoimituksen tuloksen Enteriä tai Esciä painettaessa.
* NVDA puhuu laskutoimitusten tulokset (esim. yksikkö- ja
  valuuttamuuntimessa) heti laskukaavoja syötettäessä.
* NVDA ei enää sano "otsikkotaso" tarkasteltaessa laskutoimitusten tuloksia
  laskimessa.
* NVDA ilmoittaa, jos lukujen enimmäismäärä saavutetaan ilmaisuja
  kirjoitettaessa.
* Lisätty tuki Laskin-sovelluksen version 10.1908 ja uudempien aina käytössä
  -tilalle.

## Kalenteri

* NVDA ei sano enää "muokattava" tai "vain luku" viestisisällössä ja muissa
  kentissä.

## Cortana

Useimmat kohdat eivät enää koske versiota 1903 ja uudempia, ellei
Cortana-keskustelut (versio 2004 ja uudemmat) ole käytössä.

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa.
* NVDA on hiljaa puhuttaessa Cortanalle mikrofonin välityksellä.
* Windows-haun käyttöliittymän voimalla toimivaa Resurssienhallinnan
  modernia hakukokemusta tuetaan versiossa 1909 (marraskuun 2019 päivitys)
  sekä 20H1:ssä (koontiversio 18945) ja uudemmissa.

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

## Microsoft Store

* Sovellusten nimet näytetään oikein päivitettävien sovellusten luettelossa
  päivitystarkistuksen jälkeen.
* NVDA ilmoittaa tuotteen nimen ja latauksen edistymisen sisältöä, kuten
  sovelluksia ja elokuvia ladattaessa.

## Moderni näppäimistö

Näitä ovat emojipaneeli, leikepöydän historia, sanelu, ehdotukset
syötettäessä tekstiä fyysisellä näppäimistöllä sekä modernin
syöttömenetelmän editorit tietyille kielille. Ota käyttöön emojeita
tarkasteltaessa parhaan kokemuksen saamiseksi Unicode-konsortion datan
asetus NVDA:n puheasetuksista ja aseta symbolitasoksi "jotain" tai
korkeampi.

* NVDA ei enää sano leikepöydän historiaa avattaessa joissakin tilanteissa
  "leikepöytä", kun leikepöydällä on kohteita.
* Emojipaneelin avautuessa ei enää näytä siltä, että NVDA  ei tee mitään
  joissakin järjestelmissä, joissa on asennettuna Windows 10:n versio 1903
  (May 2019 -päivitys) tai uudempi.
* Lisätty tuki modernille kiinan, japanin ja korean (CJK) IME-ehdotusten
  liittymälle, joka esiteltiin versiossa 2004 (koontiversio 18965 ja
  uudemmat).

## Ihmiset

* Ensimmäinen ehdotus puhutaan kontakteja etsittäessä, erityisesti uusimpia
  sovellusversioita käytettäessä.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  mukaan lukien Tallennusseurannan/Levynsiivouksen pienoisohjelma sekä
  Windows Updaten virheet, puhutaan nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* NVDA ei enää epäonnistu joidenkin yhdistelmäruutujen ja
  valintapainikkeiden selitteiden tunnistamisessa ja/tai arvomuutosten
  ilmoittamisessa.
* NVDA ei tee enää mitään tai toista virheääniä, mikäli
  objektinavigointikomentoja käytetään tietyissä tilanteissa.
* Windows Updaten muistutusvalintaikkuna tunnistetaan asianmukaisesti
  valintaikkunaksi.
* Joissakin Windows-asennuksissa näkyvät erikoiset säädinten nimet on
  korjattu.
* Windows Update -prosessiin ominaisuuspäivitysten osalta tehtyjen muutosten
  vuoksi uudempiin 1803:n versioihin ja sitä tuoreempiin  on lisätty Lataa
  ja asenna nyt -linkki. Jos uusi päivitys on saatavilla, NVDA puhuu nyt sen
  nimen.

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

[4]: https://addons.nvda-project.org/files/get.php?file=w10-2019
