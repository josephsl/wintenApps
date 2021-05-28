# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* NVDA compatibility: 2020.4 and beyond

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
* Microsoft Solitaire -kokoelma
* Microsoft Store
* Moderni näppäimistö (emojipaneeli/sanelu/fyysisen näppäimistösyötteen
  ehdotukset/pilvileikepöydän historia/modernin syöttömenetelmän editorit)
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Sää
* Sekalaisia moduuleita säätimille, esim. Käynnistä-valikon ruuduille.

Huomautuksia:

* Tämä lisäosa edellyttää Windows 10:n versiota 2004 (koontiversio 19041)
  tai uudempaa. Käytä parhaan käyttökokemuksen varmistamiseksi Windows 10:n
  viimeisintä vakaata versiota (21H1/koontiversio 19043).
* Jotkin lisäosan ominaisuudet ovat tai tulevat olemaan osa NVDA:ta.
* Voidaan olettaa, että ominaisuudet, joita ei ole lueteltu alla, joko
  sisältyvät NVDA:han, eivät ole enää käytössä, koska lisäosa ei tue vanhoja
  Windows 10 -versioita tai eivät ole enää käyttökelpoisia Windows 10:een ja
  sovelluksiin tehtyjen muutosten vuoksi.
* Jotkin sovellukset tukevat kompaktia peitetilaa (esim. Laskimessa Aina
  päällimmäisenä), joka ei toimi oikein NVDA:n massamuistiversion kanssa.

Katso luettelo lisäosan kaikkiin versioihin tehdyistä muutoksista
[lisäosajulkaisujen muutoslokeista.][3]

## Yleistä

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
* Seuraavat UIA-tapahtumat tunnistetaan NVDA:n tarjoamien
  UIA-tapahtumakäsittelijöiden lisäksi: vetämisen aloitus, vetämisen
  peruutus, vetäminen suoritettu, vetämisen kohteeseen siirtyminen,
  vetämisen kohteesta poistuminen, vetämisen kohde pudotettu. Näitä
  tapahtumia seurataan, kun NVDA:n lokitasoksi on määritetty
  "virheenkorjaus", ja UIA-ilmoitustapahtuma ilmaistaan virheäänellä, mikäli
  ilmoitukset tulevat muualta kuin aktiivisesta sovelluksesta. Jotkin
  tapahtumat tarjoavat lisätietoja, kuten elementtien määrä ohjain kohteelle
  -tapahtumalla, elementin tila tilan muutos -tapahtumalla sekä kohteen
  teksti kohteen tila -tapahtumalla.
* On mahdollista seurata vain tiettyjä tapahtumia ja/tai tietyistä
  sovelluksista tulevia tapahtumia.
* When opening, closing, reordering (build 21337 or later), or switching
  between virtual desktops, NVDA will announce active virtual desktop name
  (desktop 2, for example).
* NVDA ei enää ilmoita Käynnistä-valikon kokoa  näytön resoluutiota tai
  suuntaa vaihdettaessa.
* Kun Käynnistä-valikon ruutuja tai Toimintokeskuksen pikatoimintoja
  järjestellään Alt+Vaihto+nuolinäppäimillä, NVDA puhuu raahattujen
  kohteiden tiedot tai raahatun kohteen uuden sijainnin.
* Ilmoitukset, kuten äänenvoimakkuuden/kirkkauden muutokset
  resurssienhallinnassa sekä sovellusten päivitysilmoitukset Microsoft
  Storesta voidaan estää poistamalla käytöstä Lue ilmoitukset -asetus NVDA:n
  objektien lukemisen asetuksista.

## Laskin

* NVDA ei enää sano graafisen laskinnäytön ilmoitusta kahdesti.

## Kalenteri

* NVDA ei sano enää "muokattava" tai "vain luku" viestisisällössä ja muissa
  kentissä.

## Cortana

Useimmat kohdat koskevat versiota 2004 ja uudempia Cortana-keskusteluja
käytettäessä.

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa.
* NVDA on hiljaa puhuttaessa Cortanalle mikrofonin välityksellä.
* Modernia Windows-haun käyttöliittymän voimalla toimivaa
  resurssienhallinnan hakukokemusta tuetaan versiossa 1909 (marraskuun 2019
  päivitys) ja uudemmassa.

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

## Microsoft Solitaire -kokoelma

* NVDA sanoo korttien ja korttipakkojen nimet.

## Microsoft Store

* Sovellusten nimet näytetään oikein päivitettävien sovellusten luettelossa
  päivitystarkistuksen jälkeen.
* NVDA ilmoittaa tuotteen nimen ja latauksen edistymisen sisältöä, kuten
  sovelluksia ja elokuvia ladattaessa.

## Moderni näppäimistö

Näitä ovat emojipaneeli, leikepöydän historia, sanelu, ehdotukset
syötettäessä tekstiä fyysisellä näppäimistöllä sekä modernin
syöttömenetelmän editorit tietyille kielille. Ota emojeita tarkasteltaessa
parhaan kokemuksen saamiseksi käyttöön Unicode-konsortion datan asetus
NVDA:n puheasetuksista ja aseta symbolitasoksi "jotain" tai korkeampi. NVDA
tukee lisäksi päivitettyä syöttökokemuksen paneelia koontiversiossa 21296 ja
uudemmissa.

* NVDA ei enää sano leikepöydän historiaa avattaessa joissakin tilanteissa
  "leikepöytä", kun leikepöydällä on kohteita.
* Emojipaneelin avautuessa ei enää näytä siltä, että NVDA  ei tee mitään
  joissakin järjestelmissä, joissa on asennettuna Windows 10:n versio 1903
  (May 2019 -päivitys) tai uudempi.
* Kun emojiryhmä (mukaan lukien kaomoji ja symboliryhmä versiossa 1903 tai
  uudemmissa) valitaan, NVDA ei enää siirrä navigointiobjektia tiettyihin
  emojeihin.
* Lisätty tuki päivitetylle syöttökokemuksen paneelille (yhdistetty
  emojipaneeli ja leikepöydän historia) koontiversiossa 21296 ja uudemmissa.

## Ihmiset

* Ensimmäinen ehdotus puhutaan kontakteja etsittäessä, erityisesti uusimpia
  sovellusversioita käytettäessä.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  mukaan lukien Tallennusseurannan/Levynsiivouksen pienoisohjelma sekä
  Windows Updaten virheet, puhutaan nyt automaattisesti.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
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
