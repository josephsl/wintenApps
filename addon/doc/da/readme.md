# Vigtige forbedringer til Windows apps (Windows App Essentials) #

* Forfattere: Joseph Lee, Derek Riemer og andre
* Download [stabil version][1]
* Download [betaversion][2]
* Download [udviklingsversion][3]
* NVDA-kompatibilitet: 2023.3.3 og nyere

Bemærk: Denne tilføjelse hed Windows 10 App Essentials, men er blevet omdøbt
til Windows App Essentials i 2021 for at understøtte Windows 10 og
fremtidige udgivelser som Windows 11. Dele af dette tilføjelsesprogram vil
stadig henvise til det originale navn for tilføjelsen.

Denne tilføjelse er en samling af app-moduler til forskellige Windows-apps,
samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Moderne tastatur
* Indstillinger (systemindstillinger, Windows+I)

Bemærkninger:

* Denne tilføjelse kræver Windows 10 22H2 (build 19045), 11 22H2 (build
  22621) eller nyere udgivelser.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  <https://aka.ms/WindowsTargetVersioninfo> for more information and support
  dates.
* Selvom installation er mulig, understøtter denne tilføjelse ikke Windows
  Enterprise LTSC (Long-Term Servicing Channel) og Windows
  Server-udgivelser.
* Ikke alle funktioner fra Windows Insider Preview-builds vil blive
  understøttet. Dette er yderligere tilfældet for funktioner introduceret i
  en undergruppe af Windows Insiders i udviklerkanalen.
* The add-on may emulate changes included in Insider Preview builds which
  are subsequently removed, and for these changes, the add-on may remove
  them in future releases.
* Tilføjelsesudviklerkanal vil inkludere ændringer, herunder eksperimentelt
  indhold, der muligvis er inkluderet i beta- og stabile versioner, og
  betakanalen vil komme med ændringer, der er planlagt for fremtidige
  stabile versioner.
* Nogle funktioner tilføjelsespakken indeholder er eller bliver en del af
  NVDA skærmlæser.
* For at få den bedste oplevelse med apps, der integrerer webteknologier og
  indhold som f.eks. Start-menuen og dens kontekstmenu, skal du aktivere
  indstillingen "Automatisk fokustilstand ved ændring af fokus" fra NVDAs
  indstillingspanel under "Gennemsynstilstand".

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][4].

## Moderne tastatur

Dette inkluderer emoji-panelet, historik for udklipsholderen,
berøringstastatur, diktering, forslag i forhold til hardwareinput og moderne
Input Methodf Editor for visse sprog. Når du ser emojier, skal du for at få
den bedste oplevelse aktivere Unicode Consortium-indstillingen fra NvDAs
taleindstillinger og indstille tegnsætningsniveauet til "nogle" eller
højere. Når du skal indstille fra historikken i Windows 10, skal du bruge
mellemrumstasten i stedet for enter.

* In Windows 11, NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard. This is now part of NVDA
  2024.2.

## Indstillinger

* NVDA vil afbryde talen og oplyse status for opdateringer til Windows
  Update, efterhånden som download og installation skrider frem. Dette kan
  resultere i afbrydelse af talen, når du navigerer i appen Indstillinger,
  mens opdateringer downloades og installeres. Hvis du bruger Windows 11
  22H2 og nyere med indstillingen "Registrer hændelser fra UI Automation
  samt egenskabsændringer" slået til, skal du flytte fokus til listen
  opdateringer, så NVDA kan oplyse status for opdateringerne.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
