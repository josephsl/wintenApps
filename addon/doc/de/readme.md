# Windows 10 App Essentials #

* Autors: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version herunterladen][1]
* [Entwicklungsversion herunterladen][2]
* NVDA-Kompatibilität: 2018.3 bis 2019.1

Diese Erweiterung bringt ein Paket von Anwendungsmodulen für diverse Windows
10 Apps sowie Korrekturen in einigen Windows 10 Elementen mit.

Die folgenden App-Module oder unterstützten Module für Windows-10-Apps sind
inbegriffen (siehe weiter unten jeden App-Bereich für mehr Details)

* Einstellungscenter für Benachrichtigungen und Aktionen
* Wecker und Uhr.
* Kalender
* Rechner (modern)
* Cortana
* Feedback Hub
* Mail
* Karten
* Microsoft Edge
* Moderne Tastatur (Emoji-Panel / Hardware-Eingabevorschläge /
  Cloud-Zwischenablage ab Version 1709)
* Kontakte
* Einstellungen (Systemeinstellungen, Windows+I)
* Skype (universal app)
* Store
* Wetter.
* Diverse Steuermodule wie beispielsweise die Startmenübereiche.

Hinweise:

* Diese Erweiterung erfordert Windows 10 Version 1803 (Build 17134) oder
  neuer und NVDA 2018.3 oder neuer. Für beste Ergebnisse verwenden Sie die
  Erweiterung mit der neuesten stabilen Version von Windows 10 (Build 17763)
  und der neuesten stabilen Version von NVDA.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to Windows 10 and apps that makes entries
  no longer applicable.

Eine Liste aller Änderungen in den einzelnen Versionen der Erweiterung
finden Sie im Dokument [Änderungsprotokolle  der veröffentlichten
Versionen][3].

## Allgemein

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7 and 8.1.
* Untermenüs werden in verschiedenen Anwendungen richtig erkannt,
  einschließlich des Kontextmenüs für Startmenükacheln und des
  Anwendungsmenüs von Microsoft Edge (Redstone 5).
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* In bestimmten Kontextmenüs (z.B. in Edge) werden Positionsinformationen
  (z.B. 1 von 2) nicht mehr angesagt.
* Folgende UIA-Ereignisse werden erkannt: aktive Textpositionsänderung,
  Steuerelement für, Ziehen Starten, Ziehen Abbrechen, Ziehen erfolgt,
  Element ausgewählt, Änderung der Live Region, Benachrichtigung,
  Systemalarm, Tooltip geöffnet, Fenster geöffnet. Wenn NVDA mit
  Debug-Protokollierungsstufe ausgeführt wird, werden diese Ereignisse
  verfolgt. Für UIA-Benachrichtigungsereignisse wird ein Debug-Ton
  ausgegeben, wenn Benachrichtigungen von einer anderen Anwendung als der
  aktuell aktiven Anwendung kommen.
* Tooltips von Edge und Universal Apps werden erkannt und angekündigt.
* Beim Öffnen, Schließen oder Wechseln zwischen virtuellen Desktops gibt
  NVDA die aktuelle Desktop-ID (z.B. Desktop 2) bekannt.
* NVDA sagt den Text für die Größe des Startmenüs nicht mehr an, wenn die
  Bildschirmauflösung oder Ausrichtung geändert wird.
* In build 18323 and later, NVDA will now announce audio volume and
  brightness changes.

## Einstellungscenter für Benachrichtigungen und Aktionen

* Brightness quick action is now a button instead of a toggle button. This
  will be part of NVDA 2019.1.
* Various status changes such as Focus Assist and Brightness will be
  reported. This will be part of NVDA 2019.1.

## Wecker und Uhr

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates. This will be part of NVDA
  2019.1.

## Rechner

* NVDA sagt die Rechenergebnisse beim Drücken der Eingabe- oder Escape-Taste
  an.
* Für Berechnungen wie im Einheitenumrechner und Währungsumrechner gibt NVDA
  die Ergebnisse bekannt, sobald die Berechnungen eingegeben wurden.
* NVDA wird nicht mehr "Überschriften" für Berechnungsergebnisse bekannt
  geben.

## Kalender

* NVDA sagt nicht mehr "bearbeiten" oder"schreibgeschützt" im
  Nachrichtentext und in anderen Feldern an.

## Cortana

* Textuelle Antworten von Cortana werden in den meisten Fällen
  angezeigt. Falls nicht, öffnen Sie das StartMenü und starten Sie die Suche
  erneut.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.
* NVDA wird nun eine Erinnerungsbestätigung anzeigen, nachdem Sie eine
  eingestellt haben.

## Feedback Hub

* Feedback-Kathegorien werden in neueren App-Versionen nicht mehr zweimal
  angesagt.

## Mail

* Beim Navigieren durch Elemente in der Nachrichtenliste können Sie nun
  Tabellen-Navigationsbefehle verwenden, um Betreffzeilen zu überprüfen. Die
  Navigation zwischen Zeilen (Nachrichten) wird noch nicht unterstützt.
* Wenn Sie eine Nachricht schreiben, wird das Erscheinen von Vorschlägen
  durch Töne angezeigt.
* NVDA will no longer do anything or play error tones after closing this
  app.

## Karten

* NVDA spielt einen Ortungston für Kartenstandorte ab.
* Wenn Sie die Straßenseitenansicht verwenden und die Option"Tastatur
  verwenden" aktiviert ist, wird NVDA Straßenadressen ankündigen, während
  Sie mit den Pfeiltasten durch die Karte navigieren.

## Microsoft Edge

* Die automatische Vervollständigung beim Tippen wird verfolgt und in der
  Adress-Omnibar ordnungsgemäß angesagt.
* NVDA gibt keinen Vorschläge-Ton mehr wieder, wenn F11 für den
  Vollbildmodus gedrückt wird.

## Moderne virtuelle Tastaturen

Note: most features below are now part of NVDA 2018.3 or later.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). If using NVDA releases earlier
  than 2018.4, for best experience when reading emojis, use Windows OneCore
  speech synthesizer. If 2018.4 or later is in use, enable Unicode
  Consortium setting from NvDA's speech settings and set symbol level to
  "some" or higher.
* Unterstützung für Eingabevorschläge bei Hardware-Tastaturen (gilt für
  Windowsversionen ab Build 1803)
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as displaying skin
  tone modifiers when opened to People category.
* Unterstützung für die Ansage der Einträge in der Cloud-basierten
  Zwischenablage in Build 17666 (Redstone 5) und höher.
* Unnötige Ausführlichkeit bei der Arbeit mit der modernen Tastatur und
  deren Funktionen reduziert. Dazu gehört, dass die "Microsoft Kandidat UI"
  beim Öffnen von Hardware-Tastatur-Eingabevorschlägen nicht mehr
  angekündigt wird, und dass es still bleibt, wenn bestimmte
  Berührungstasten auf manchen Systemen ein Namensänderungsereignis
  auslösen.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent 19H1 Insider Preview builds. This will be part of
  NVDA 2019.1.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search
  results for emojis if possible. This will be part of NVDA 2019.1.

## Kontakte

* Bei der Suche nach Kontakten wird der erste Vorschlag angekündigt,
  insbesondere bei Verwendung aktueller App-Veröffentlichungen.

## Einstellungen

* Bestimmte Informationen wie z.B. der Fortschritt von Windows Update,
  Widget zur Bereinigung und Defragmentierung von Speicher und Festplatten
  werden in echtzeit gemeldet.
* Werte in Fortschrittsbalken und andere Informationen werden nicht mehr
  zweimal angesagt.
* Bei einigen Kombinationsfeldern und Kontrollfeldern wird NVDA nun die
  Beschriftung erkennen und/oder Wertänderungen ankündigen.
* Lautstärke-Fortschrittsbalken werden nicht mehr ausgegeben (gilt für
  Windowsversionen ab Build 1803)
* Weitere Meldungen über den Status von Windows Update werden angezeigt,
  insbesondere wenn im Windows Update Fehler auftreten.
* NVDA wird nun ordnungsgemäß reagieren und keine Fehlertöne mehr während
  der Objektnavigation abspielen.
* Das Erinnerungsdialogfeld von Windows Update wird als richtiger Dialog
  erkannt.

## Skype

Hinweis: Die folgenden Einträge funktionieren in der universellen Skype 14
App nicht ordnungsgemäß.

* Die Eingabe des Indikatortextes wird wie bei Skype für Desktop-Client
  angekündigt.
* Strg+NVDA+1 bis 9, zum Lesen der letzten Chat-Meldungen und zum Ziehen des
  Navigator-Objects zum Chat-Eintrag in Skype für Desktop (auch verfügbar in
  Skype UWP).
* Sie können Alt+1 bis 9 drücken, um Gespräche (1), Kontaktliste (2), Bots
  (3) und Chat-Eingabefeld zu finden und zu verschieben, falls sichtbar
  (4). Beachten Sie dabei, dass diese Befehle nur dann funktionieren, wenn
  Sie das im März 2017 veröffentlichte Skype-Update installiert haben.
* NVDA wird beim Navigieren durch die Nachrichteneinträge in den meisten
  Fällen nicht mehr "Skype-Nachricht" ansagen.
* Durch Drücken von NVDA+D auf einem Nachrichtenelement kann NVDA
  detaillierte Informationen über eine Nachricht wie zum Beispiel Chat-ARt,
  gesendetes Datum und Uhrzeit, etc. anzeigen.

## Store

* Nach der Suche nach App-Aktualisierungen werden die App-Namen in der Liste
  der zu aktualisierenden Apps korrekt beschriftet.
* Beim Herunterladen von Inhalten wie Apps und Filmen wird NVDA den
  Produktnamen und den Fortschritt des Downloads bekannt geben.

## Wetter

* Registerkarten wie"Prognose" und"Karten" werden als richtige
  Registerkarten erkannt (Patch von Derek Riemer).
* Beim Lesen einer Prognose können Sie mit den Pfeiltasten nach links und
  rechts zwischen den Elementen wechseln. Verwenden Sie die Aufwärts- und
  Abwärtspfeile, um die einzelnen Teile eines Elements zu lesen. Zum
  Beispiel könnte ein Druck auf den Pfeil nach rechts den Bericht "Montag:
  33 Grad, teilweise bewölkt, ..." anzeigen. Wenn man den Pfeil nach unten
  drückt, heißt es"Montag", dann wird ein erneuter Druck auf den Pfeil den
  nächsten Punkt anzeigen (wie z.B. die Temperatur). Dies funktioniert
  derzeit für Tages- und Stundenvorhersagen.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
