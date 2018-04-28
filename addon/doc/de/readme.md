# Ergänzungen für Windows 10 Apps #

* Autors: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version][1] herunterladen
* [Entwicklerversion][2] herunterladen

Diese Erweiterung bringt ein Paket von Anwendungsmodulen für diverse Windows
10 Apps sowie Korrekturen in einigen Windows 10 Elementen mit.

Die folgenden App-Module oder unterstützten Module für Windows-10-Apps sind
inbegriffen (siehe weiter unten jeden App-Bereich für mehr Details)

* Wecker und Uhr
* Kalender
* Rechner (modern)
* Cortana
* Feedback Hub
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
Windows 10 stable releases (build 16299 or 17134) and latest stable version
of NVDA. Also, after changing update settings for the add-on, be sure to
save NVDA settings.

## Allgemein

* Untermenüs werden im Kontextmenü von Kacheln korrekt erkannt
* Bestimmte Dialoge werden nun als richtige Dialogfelder erkannt. Dazu
  gehören das Dialogfeld"Insider-Vorschau" in der App für
  Windowseinstellungen.
* NVDA kann die Anzahl der Vorschläge bei der Suche in den meisten Fällen
  bekannt geben. Diese Option wird gesteuert durch Meldung von
  Objektpositionsdaten im Dialog der Objektpräsentation.
* In bestimmten Kontextmenüs (z.B. in Edge) werden Positionsinformationen
  (z.B. 1 von 2) nicht mehr angesagt.
* The following UIA events are recognized: Controller for, drag start, drag
  cancel, drag complete, element selected, live region change, notification,
  system alert, tooltip opened, window opened. With NVDA set to run with
  debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard.
* Möglichkeit hinzugefügt, über den neuen Dialog Windows 10 App Essentials
  im NVDA-Einstellungsmenü nach Aktualisierungen für diese Erweiterung
  (automatisch oder manuell) zu suchen. Standardmäßig werden stabile- und
  Entwicklerversionen wöchentlich bzw. täglich automatisch nach neuen
  Updates suchen.
* In einigen Apps wird Live-Region-Text angekündigt. Dazu gehören Meldungen
  in Edge, Ergebnisse im Windowsrechner und andere. Beachten Sie, dass dies
  in manchen Fällen zu einer doppelten Aussprache führen kann, da die
  meisten Szenarien nun Bestandteil von NVDA ab 2017.3 sind.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced. Due to technical limitations, this feature
  works properly with NVDA 2018.1 and later, and will be part of NVDA with
  2018.2 release.
* Tooltips from Edge and universal apps are recognized and will be
  announced.
* NVDA will no longer announce "unknown" when opening quick link menu
  (Windows+X). This fix will be part of NVDA 2018.2.
* In build 17627 and later, when opening a new Sets tab (Control+Windows+T),
  NVDA will announce search results when searching for items in the embedded
  Cortana window.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop ID (desktop 2, for example).

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
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.
* NVDA wird nun eine Erinnerungsbestätigung anzeigen, nachdem Sie eine
  eingestellt haben.

## Feedback Hub

* Feedback-Kathegorien werden in neueren App-Versionen nicht mehr zweimal
  angesagt.

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

* Benachrichtigungen wie Datei-Downloads und verschiedene
  Website-Benachrichtigungen werden nun angesagt. 

## moderne virtuelle Tastaturen

* Unterstützung für das schwebende Emoji-Eingabefeld in der Windowsversion
  1709 (Fall Creators Update). Für beste Erfahrungen beim Lesen von Emojis
  verwenden Sie Windows-OneCore-Sprachausgaben.
* Unterstützung für Eingabevorschläge bei Hardware-Tastaturen (gilt für
  Windowsversionen ab Build 17040)
* NVDA wird nun im Emoji-Fenster das erste ausgewählte Emoji ansagen. Dies
  gilt für Windows-Builds ab Build 1709.

## Kontakte

* Wenn die Suche nach Kontakten erfolgreich war, wird ein Signalton
  abgespielt.

## Einstellungen

* Bestimmte Informationen, wie z.B. der Fortschritt von Windows Update,
  werden nun automatisch gemeldet.
* Werte in Fortschrittsbalken und andere Informationen werden nicht mehr
  zweimal angesagt.
* Einstellungsgruppen werden erkannt, wenn Objektnavigation zur Navigation
  zwischen Elementen angewendet wird.
* Bei einigen Ausklapplisten wird NVDA nun die Beschriftung erkennen
  und/oder Wertänderungen ankündigen.
* Lautstärke-Fortschrittsbalken werden nicht mehr ausgegeben (gilt für
  Windowsversionen ab Build 17035)

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
