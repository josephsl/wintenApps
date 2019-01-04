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
* Spieleleiste
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

* Diese Erweiterung erfordert Windows 10 Version 1709 (Build 16299) oder
  höher und NVDA 2018.3 oder höher. Für beste Ergebnisse verwenden Sie die
  Erweiterung mit der neuesten stabilen Version von Windows 10 (Build 17134)
  und der neuesten stabilen Version von NVDA.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* Für Einträge, die unten nicht aufgeführt sind, können Sie davon ausgehen,
  dass diese Funktionen Teil von NVDA selbst sind und nicht mehr anwendbar
  sind, da die Erweiterung alte Windows 10-Versionen nicht unterstützt oder
  Änderungen an Anwendungen vorgenommen wurden, die Einträge nicht mehr
  anwendbar machen.
* Standalone update check from this add-on will be removed in version
  19.02. For future add-on updates, please use Add-on Updater add-on.

Eine Liste aller Änderungen in den einzlnen Versionen der Erweiterung finden
Sie im Dokument [Changelogs der Erweiterungen][3].

## Allgemein

* Interne Änderungen, um die Erweiterung mit zukünftigen NVDA-Versionen
  kompatibel zu machen.
* Wenn die Erweiterung Zusatz-Updater installiert ist, wird diese
  Erweiterung nach Updates für Windows 10 App Essentials suchen.
* Das standardmäßige Prüfintervall für Aktualisierungen wurde auf
  wöchentliche Prüfungen sowohl für stabile als auch für
  Entwicklungsversionen geändert. Dies gilt, wenn die Erweiterung Windows 10
  App Essentials selbst nach Updates sucht.
* Eine Fehlermeldung wird während der Aktualisierung dieser Erweiterung
  ausgegeben, wenn die neue Erweiterungsversion eine neuere NVDA-Version
  erfordert. Dies gilt auch dann, wenn die Erweiterung selbst nach
  Aktualisierungen sucht.
* Kleine Änderungen an der Darstellung einiger Benachrichtigungen in anderen
  Sprachen als Englisch.
* Untermenüs werden in verschiedenen Anwendungen richtig erkannt,
  einschließlich des Kontextmenüs für Startmenükacheln und des
  Anwendungsmenüs von Microsoft Edge (Redstone 5).
* Bestimmte Dialoge werden nun als richtige Dialoge erkannt und als solche
  gemeldet, einschließlich des Insider-Vorschau-Dialogs (in den
  Windows-Einstellungen). Diese Funktion ist nun auch Teil des NVDA selbst.
* NVDA kann die Anzahl der Vorschläge bei der Suche in den meisten Fällen
  bekannt geben. Diese Option wird gesteuert durch Meldung von
  Objektpositionsdaten im Dialog der Objektpräsentation.
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
* Benachrichtigungen von neueren App-Releases auf Windows 10 Version 1709
  (Build 16299) und neuer werden mitgeteilt.
* Tooltips von Edge und Universal Apps werden erkannt und angekündigt.
* Beim Öffnen, Schließen oder Wechseln zwischen virtuellen Desktops gibt
  NVDA die aktuelle Desktop-ID (z.B. Desktop 2) bekannt.
* NVDA sagt den Text für die Größe des Startmenüs nicht mehr an, wenn die
  Bildschirmauflösung oder Ausrichtung geändert wird.

## Einstellungscenter für Benachrichtigungen und Aktionen

* Die schnelle Aktion für Helligkeit ist nun eine Schaltfläche anstelle
  einer Umschalttaste.
* Verschiedene Statusänderungen wie Focus Assist und Helligkeit werden nun
  angesagt.

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

## Spieleleiste

* NVDA wird das Erscheinen der Spieleleiste ankündigen. Auf Grund
  technischer Einschränkungen kann NVDA vor dem Build 17723 nicht
  vollständig mit der Spieleleiste interagieren.

## Mail

* Beim Navigieren durch Elemente in der Nachrichtenliste können Sie nun
  Tabellen-Navigationsbefehle verwenden, um Betreffzeilen zu überprüfen. Die
  Navigation zwischen Zeilen (Nachrichten) wird noch nicht unterstützt.
* Wenn Sie eine Nachricht schreiben, wird das Erscheinen von Vorschlägen
  durch Töne angezeigt.

## Karten

* NVDA spielt einen Ortungston für Kartenstandorte ab.
* Wenn Sie die Straßenseitenansicht verwenden und die Option"Tastatur
  verwenden" aktiviert ist, wird NVDA Straßenadressen ankündigen, während
  Sie mit den Pfeiltasten durch die Karte navigieren.

## Microsoft Edge

* Benachrichtigungen wie Datei-Downloads und verschiedene Webseiten-Alarme
  sowie die Verfügbarkeit der Leseansicht (ab Version 1709) werden
  mitgeteilt.
* Die automatische Vervollständigung beim Tippen wird verfolgt und in der
  Adress-Omnibar ordnungsgemäß angesagt.

## Moderne virtuelle Tastaturen

Hinweis: Die meisten der unten aufgeführten Funktionen sind nun Teil von
NVDA 2018.3.

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
  panel in more recent 19H1 Insider Preview builds.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search
  results for emojis if possible.

## Kontakte

* Bei der Suche nach Kontakten wird der erste Vorschlag angekündigt,
  insbesondere bei Verwendung aktueller App-Veröffentlichungen.

## Einstellungen

* Bestimmte Informationen wie z.B. der Fortschritt von Windows Update,
  Widget zur Bereinigung und Defragmentierung von Speicher und Festplatten
  werden in echtzeit gemeldet.
* Werte in Fortschrittsbalken und andere Informationen werden nicht mehr
  zweimal angesagt.
* Einstellungsgruppen werden erkannt, wenn Objektnavigation zur Navigation
  zwischen Elementen angewendet wird.
* Bei einigen Kombinationsfeldern und Kontrollfeldern wird NVDA nun die
  Beschriftung erkennen und/oder Wertänderungen ankündigen.
* Lautstärke-Fortschrittsbalken werden nicht mehr ausgegeben (gilt für
  Windowsversionen ab Build 1803)
* Weitere Meldungen über den Status von Windows Update werden angezeigt,
  insbesondere wenn im Windows Update Fehler auftreten.
* NVDA wird nun ordnungsgemäß reagieren und keine Fehlertöne mehr während
  der Objektnavigation abspielen.
* Verschiedene neue Links, die im Build 18282 hinzugefügt wurden, haben
  jetzt entsprechende Beschriftungen.
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
