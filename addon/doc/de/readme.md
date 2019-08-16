# Zugänglichkeitsverbesserungen für Windows 10 Apps #

* Autoren: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2019.1 bis 2019.2

Diese Erweiterung bietet eine Sammlung von Anwendungsmodulen für
verschiedene Windows 10 Anwendungen sowie Korrekturen in einigen Windows 10
Elementen.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Rechner (modern)
* Kalender
* Cortana
* Feedback Hub
* E-Mail
* Karten
* Microsoft Edge
* Moderne Tastatur (Emoji-Panel- / Diktat- / Hardware-Eingabevorschläge /
  Cloud-Zwischenablage-Elemente in Version 1709 und höher)
* Kontakte
* Einstellungen (Systemeinstellungen, Windows+I)
* Store
* Wetter.
* Diverse Steuermodule wie beispielsweise die Startmenübereiche.

Hinweise:

* Diese Erweiterung erfordert Windows 10 Version 1809 (Build 17763) oder
  höher und NVDA 2019.1 oder höher. Für beste Ergebnisse verwenden Sie die
  Erweiterung mit der neuesten stabilen Version von Windows 10 und der
  neuesten stabilen Version von NVDA.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* Für Einträge, die im Folgenden nicht aufgeführt sind, können Sie davon
  ausgehen, dass Funktionen Teil von NVDA sind, die nicht mehr benötigt
  werden, da die Erweiterung alte Windows 10-Versionen nicht unterstützt
  oder Änderungen an Windows 10 und Anwendungen vorgenommen wurden, die
  Einträge nicht mehr notwendig sind.

Eine Liste aller Änderungen in den einzelnen Versionen der Erweiterung
finden Sie im Dokument [Änderungsprotokolle  der veröffentlichten
Versionen][3].

## Allgemein

* NVDA wird keine Fehlertöne mehr abspielen oder nichts tun, wenn diese
  Erweiterung unter Windows 7, Windows 8.1 und nicht unterstützten Versionen
  von Windows 10 benutzt wird.
* Untermenüs werden in verschiedenen Anwendungen richtig erkannt,
  einschließlich des Kontextmenüs für Startmenükacheln und des
  Anwendungsmenüs von Microsoft Edge (Redstone 5).
* Zusätzlich zu den von der NVDA erkannten Dialogen werden nun mehr Dialoge
  als richtige Dialoge erkannt und als solche gemeldet, einschließlich des
  Dialogs Insider-Vorschau (Einstellungsanwendung).
* NVDA kann in den meisten Fällen die Anzahl der Vorschläge bei der
  Durchführung einer Suche bekannt geben. Diese Option wird durch
  "Objekt-Positionsinformationen mitteilen" im Objektpräsentationsfenster in
  den NVDA-Einstellungen gesteuert.
* In bestimmten Kontextmenüs (z.B. in Edge) werden Positionsinformationen
  (z.B. 1 von 2) nicht mehr angesagt.
* Die folgenden Ereignisse für die Benutzeroberflächenautomatisierung werden
  erkannt: Steuerung für, Drag Start, Drag Cancel, Drag Complete, Element
  ausgewählt, Elementstatus, Änderung der Live-Region, Benachrichtigung,
  Systemalarm, Textänderung, Tooltipp geöffnet, Fenster geöffnet. Wenn NVDA
  so eingestellt ist, dass es mit aktivierter Debug-Protokollierung läuft,
  werden diese Ereignisse verfolgt und für das Benachrichtigungsereignis der
  Benutzeroberflächenautomatisierung wird ein Debug-Ton ausgegeben, wenn
  Benachrichtigungen von einem anderen Ort als der aktuell aktiven Anwendung
  stammen.
* Es ist möglich, nur bestimmte Ereignisse bzw. Ereignisse aus bestimmten
  Anwendungen zu verfolgen.
* Tooltips von Edge und Universal Apps werden erkannt und angekündigt. Dies
  wird in NVDA 2019.3 standardmäßig implementiert.
* Beim Öffnen, Schließen oder Umschalten virtueller Desktops meldet NVDA den
  aktuellen Desktop-Namen (z. B. Desktop 2).
* NVDA sagt den Text für die Größe des Startmenüs nicht mehr an, wenn die
  Bildschirmauflösung oder Ausrichtung geändert wird.
* In der Version 1903 (Mai 2019 Update) wird NVDA Änderungen bei der
  Lautstärke und Helligkeit sofort zurückmelden. Dies ist nun eine Neuerung
  in NVDA 2019.2.

## Rechner

* NVDA sagt die Rechenergebnisse beim Drücken der Eingabe- oder Escape-Taste
  an.
* Für Berechnungen wie Umrechnungen von Einheiten und Währungen gibt NVDA
  das Ergebnis Ergebnisse bekannt, sobald die Berechnung eingegeben wird.
* NVDA nennt bei Berechnungsergebnissen nicht mehr "Überschriftebenen".
* NVDA meldet, wenn die maximale Anzahl der Ziffern während der Eingabe von
  Ausdrücken erreicht wurde.

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
* Ab Windows 10 Build 18945 und neuer wird die moderne Suchfunktion der
  Cortana-Benutzeroberfläche im Dateiexplorer unterstützt.

## Feedback Hub

* Feedback-Kathegorien werden in neueren App-Versionen nicht mehr zweimal
  angesagt.

## E-Mail

* Beim Navigieren durch Elemente in der Nachrichtenliste können Sie nun
  Tabellen-Navigationsbefehle verwenden, um Betreffzeilen zu überprüfen. Die
  Navigation zwischen Zeilen (Nachrichten) wird noch nicht unterstützt.
* Wenn Sie eine Nachricht schreiben, wird das Erscheinen von Vorschlägen
  durch Töne angezeigt.
* NVDA wird nach dem Schließen dieser App nicht mehr unklare Ereignisse
  hervorrufen oder Fehlertöne wiedergeben. Dies ist nun in NVDA 2019.2
  bereits standardmäßig enthalten.

## Karten

* NVDA spielt einen Ortungston für Kartenstandorte ab.
* Wenn Sie die Straßenseitenansicht verwenden und die Option"Tastatur
  verwenden" aktiviert ist, wird NVDA Straßenadressen ankündigen, während
  Sie mit den Pfeiltasten durch die Karte navigieren.

## Microsoft Edge

* Die automatische Vervollständigung beim Tippen wird verfolgt und in der
  Adresszeile ordnungsgemäß angesagt.
* NVDA gibt keinen Vorschläge-Ton mehr wieder, wenn F11 für den
  Vollbildmodus gedrückt wird.

## Moderne virtuelle Tastaturen

Hinweis: Die meisten unten aufgeführten Funktionen sind jetzt Teil von NVDA
2018.3 oder neuer.

* Unterstützung für das Emoji-Eingabefeld in Version 1709 (Fall Creators
  Update) und später, einschließlich des neu gestalteten Panels in Version
  1809 (Build 17661 und später) und Änderungen in 19H1 (Build 18262 und
  später, einschließlich Kaomoji und Symbolkategorien in Build 18305). Wenn
  Sie NVDA-Versionen vor 2018.4 verwenden, verwenden Sie für ein optimales
  Erlebnis beim Lesen von Emojis die Windows OneCore-Sprachausgabe. Wenn
  2018.4 oder höher verwendet wird, aktivieren Sie die
  Unicode-Konsortiumseinstellung aus den Spracheinstellungen von NVDA und
  stellen Sie die Symbolstufe auf "Einige" oder höher ein.
* NVDA wird unter bestimmten Umständen keine "Zwischenablage" mehr
  ankündigen, wenn sich Elemente in der Zwischenablage befinden.
* Auf einigen Systemen, auf denen die Version 1903 (Update vom Mai 2019)
  läuft, wird NVDA beim Öffnen des Emoji-Panels nichts mehr zu tun haben.

## Kontakte

* Bei der Suche nach Kontakten wird der erste Vorschlag angekündigt,
  insbesondere bei Verwendung aktueller App-Veröffentlichungen.

## Einstellungen

* Bestimmte Informationen, wie z. B. der Fortschritt von Windows Update,
  werden automatisch gemeldet, einschließlich des Widgets für die Speicher-
  und Festplattenbereinigung und der Fehler von Windows Update.
* Werte in Fortschrittsbalken und andere Informationen werden nicht mehr
  zweimal angesagt.
* Bei einigen Kombinationsfeldern und Kontrollfeldern wird NVDA nun die
  Beschriftung erkennen und/oder Wertänderungen ankündigen.
* Lautstärke-Fortschrittsbalken werden nicht mehr ausgegeben (gilt für
  Windowsversionen ab Build 1803)
* NVDA wird nun ordnungsgemäß reagieren und keine Fehlertöne mehr während
  der Objektnavigation abspielen.
* Das Erinnerungsdialogfeld von Windows Update wird als richtiger Dialog
  erkannt.
* Unsaubere Kontrollbeschriftungen, die in bestimmten
  Windows-10-Installationen zu sehen sind, wurden korrigiert.
* In neueren Revisionen der Version 1803 und später wurde aufgrund von
  Änderungen am Windows Update-Verfahren für Feature-Updates ein Link "Jetzt
  herunterladen und installieren" hinzugefügt. NVDA wird nun den Titel für
  das neue Update bekannt geben, falls vorhanden.

## Store

* Nach der Suche nach App-Aktualisierungen werden die App-Namen in der Liste
  der zu aktualisierenden Apps korrekt beschriftet.
* Beim Herunterladen von Inhalten wie Apps und Filmen wird NVDA den
  Produktnamen und den Fortschritt des Downloads bekannt geben.

## Wetter

* Registerkarten wie"Prognose" und"Karten" werden als richtige
  Registerkarten erkannt (Patch von Derek Riemer).
* Beim Lesen einer Vorhersage können Sie mit den Pfeiltasten nach links und
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
