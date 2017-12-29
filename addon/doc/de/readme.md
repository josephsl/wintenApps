# Windows 10 App Essentials #

* Autors: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version][1] herunterladen
* [Entwicklerversion][2] herunterladen

This add-on is a collection of app modules for various Windows 10 apps, as
well as enhancements and fixes for certain windows 10 controls.

Die folgenden App-Module oder unterstützten Module für Windows-10-Apps sind
inbegriffen (siehe weiter unten jeden App-Bereich für mehr Details)

* Wecker und Uhr
* Kalender
* Rechner (modern)
* Cortana
* Spieleleiste
* Mail
* Karten
* Microsoft Edge
* Unterstützung für Eingabevorschläge für Emoticons bei modernen virtuellen
  Tastaturen mit Emoticon-Eingabe, (gilt für Windowsversionen ab Build 1709)
* Kontakte
* Einstellungen (Systemeinstellungen, Windows+I)
* Skype (universal app)
* Store
* Wetter
* Diverse Steuermodule wie beispielsweise die Startmenübereiche

Note: this add-on requires Windows 10 Version 1703 (build 15063) or later
and NVDA 2017.3 or later. For best results, use the add-on with latest
Windows 10 stable build (build 16299) and latest stable version of
NVDA. Also, after changing update settings for the add-on, be sure to save
NVDA settings.

## Allgemein

* Untermenüs werden im Kontextmenü von Kacheln korrekt erkannt
* Certain dialogs are now recognized as proper dialogs, including Insider
  Preview dialog (settings app).
* NVDA kann die Anzahl der Vorschläge bei der Suche in den meisten Fällen
  bekannt geben. Diese Option wird gesteuert durch Meldung von
  Objektpositionsdaten im Dialog der Objektpräsentation.
* In bestimmten Kontextmenüs (z.B. in Edge) werden Positionsinformationen
  (z.B. 1 von 2) nicht mehr angesagt.
* Folgende UIA-Ereignisse werden erkannt: Controller für Live-Region Change,
  Systemalarm, Element ausgewählt, Fenster geöffnet. Wenn NVDA so
  eingestellt ist, dass es mit aktiviertem Debug-Logging läuft, werden diese
  Ereignisse protokolliert.
* Added ability to check for add-on updates (automatic or manual) via
  Windows 10 App Essentials dialog found in NvDA Preferences menu. By
  default, stable and development versions will check for new updates
  automatically on a weekly or daily basis, respectively.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases.

## Wecker und Uhr

* Die Werte für den Zeitbalken werden nun angezeigt. Dies macht sich beim
  Verschieben des Fokus auf die Balkensteuerung bemerkbar. Es betrifft auch
  das Steuerelement für die Festlegung des Neustarts nach einer erfolgreich
  abgeschlossenen Aktualisierung.

## Rechner

* NVDA sagt die Rechenergebnisse beim Drücken der Eingabe- oder Escape-Taste
  an.
* Für Berechnungen wie im Einheitenumrechner und Währungsumrechner gibt NVDA
  die Ergebnisse bekannt, sobald die Berechnungen eingegeben wurden.

## Kalender

* NVDA sagt nicht mehr "bearbeiten" oder"schreibgeschützt" im
  Nachrichtentext und in anderen Feldern an.

## Cortana

* Textuelle Antworten von Cortana werden in den meisten Fällen
  angezeigt. Falls nicht, öffnen Sie das StartMenü und starten Sie die Suche
  erneut.
* NVDA will be silent when talking to Cortana via voice.
* NVDA wird nun eine Erinnerungsbestätigung anzeigen, nachdem Sie eine
  eingestellt haben.

## Spieleleiste

* NVDA wird das Erscheinen des Fensters mit der Spieleleiste
  ansagen. Aufgrund technischer Einschränkungen kann NVDA nicht vollständig
  mit der Spieleleiste interagieren.

## Mail

* Beim Navigieren durch Elemente in der Nachrichtenliste können Sie nun
  Tabellen-Navigationsbefehle verwenden, um Betreffzeilen zu überprüfen.
* Wenn Sie eine Nachricht schreiben, wird das Erscheinen von Vorschlägen
  durch Töne angezeigt.

## Karten

* NVDA spielt einen Ortungston für Kartenstandorte ab.
* Wenn Sie die Straßenseitenansicht verwenden und die Option"Tastatur
  verwenden" aktiviert ist, wird NVDA Straßenadressen ankündigen, während
  Sie mit den Pfeiltasten durch die Karte navigieren.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts are
  announced.

## moderne viertuelle Tastaturen

* Unterstützung für das schwebende Emoji-Eingabefeld in der Windowsversion
  1709 (Fall Creators Update). Für beste Erfahrungen beim Lesen von Emojis
  verwenden Sie Windows-OneCore-Sprachausgaben.
* Unterstützung für Eingabevorschläge bei Hardware-Tastaturen (gilt für
  Windowsversionen ab Build 17040)

## Kontakte

* Wenn die Suche nach Kontakten erfolgreich war, wird ein Signalton
  abgespielt.

## Einstellungen

* Certain information such as Windows Update progress is reported
  automatically.
* Werte in Fortschrittsbalken und andere Informationen werden nicht mehr
  zweimal angesagt.
* Einstellungsgruppen werden erkannt, wenn Objektnavigation zur Navigation
  zwischen Controllern angewendet wird.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes.
* Fortschrittsbalken in Lautstärke-Reglern werden nicht mehr ausgegeben
  (gilt für Windowsversionen ab Build 17035)

## Skype

* Die Eingabe des Indikatortextes wird wie bei Skype für Desktop-Client
  angekündigt.
* STRG+NVDA+Zahlen aus der Zahlenreihe zum Lesen des letzten Chatverlaufs
  und zum Verschieben des Navigator-Objekts in Chat-Einträgen wie bei Skype
  für Desktop.
* Sie können nun die Alt+Zahlen aus der Zahlenreihe  drücken, um Gespräche
  (1), Kontaktliste (2), Bots (3) und Chat-Eingabefeld zu suchen und zu
  verschieben, falls sichtbar (4). Beachten Sie, dass diese Befehle
  ordnungsgemäß funktionieren, wenn das im März 2017 veröffentlichte
  Skype-Update installiert ist.
* Die Beschriftungen für Ausklapplisten für die Skype-Vorschau-App, welche
  in November 2016 veröffentlich wurde, werden erkannt.
* NVDA wird beim Navigieren durch die Nachrichteneinträge in den meisten
  Fällen nicht mehr "Skype-Nachricht" ansagen.
* Verschiedene Probleme bei der Verwendung von Skype mit Braillezeilen
  wurden behoben, einschließlich Darstellungsprobleme von
  Nachrichtenprotokollen in Braille.
* Wenn Sie in der Liste des Nachrichtenverlaufs auf einem Nachrichteneintrag
  NVDA+D drücken, kann NVDA nun detaillierte Informationen zu einer
  Nachricht wie z.B. Kanaltyp, Versanddatum, Uhrzeit usw. ansagen.

## Store

* Nach der Suche nach App-Aktualisierungen werden die App-Namen in der Liste
  der zu aktualisierenden Apps korrekt beschriftet.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

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
