# Zugänglichkeitsverbesserungen für Windows 10 Apps #

* Autoren: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA compatibility: 2019.2

Diese Erweiterung bietet eine Sammlung von Anwendungsmodulen für
verschiedene Windows 10 Anwendungen sowie Korrekturen in einigen Windows 10
Elementen.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Rechner (modern)
* Kalender
* Cortana (Klassik und Unterhaltungen)
* Feedback Hub
* E-Mail
* Karten
* Microsoft Edge
* Microsoft Store
* Moderne Tastatur (Emoji-Panel- / Diktat- / Hardware-Eingabevorschläge /
  Cloud-Zwischenablage-Elemente in Version 1709 und höher)
* Kontakte
* Einstellungen (Systemeinstellungen, Windows+I)
* Wetter.
* Diverse Steuermodule wie beispielsweise die Startmenübereiche.

Hinweise:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18362) and latest stable version of NVDA.
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
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu in Version 1809
  (October 2018 Update).
* Zusätzlich zu den von der NVDA erkannten Dialogen werden nun mehr Dialoge
  als richtige Dialoge erkannt und als solche gemeldet, einschließlich des
  Dialogs Insider-Vorschau (Einstellungsanwendung).
* NVDA kann in den meisten Fällen die Anzahl der Vorschläge bei der
  Durchführung einer Suche bekannt geben. Diese Option wird durch
  "Objekt-Positionsinformationen mitteilen" im Objektpräsentationsfenster in
  den NVDA-Einstellungen gesteuert.
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu. This will be part of NVDA 2019.3.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
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
* Anwendungsname und -Version für verschiedene universelle Apps werden nun
  korrekt angezeigt. Dies wird Bestandteil von NVDA 2019.3.

## Rechner

* NVDA sagt die Rechenergebnisse beim Drücken der Eingabe- oder Escape-Taste
  an.
* Für Berechnungen wie Umrechnungen von Einheiten und Währungen gibt NVDA
  das Ergebnis Ergebnisse bekannt, sobald die Berechnung eingegeben wird.
* NVDA nennt bei Berechnungsergebnissen nicht mehr "Überschriftebenen".
* NVDA meldet, wenn die maximale Anzahl der Ziffern während der Eingabe von
  Ausdrücken erreicht wurde.
* Added support for always on mode in Calculator version 10.1908 and later.

## Kalender

* NVDA sagt nicht mehr "bearbeiten" oder"schreibgeschützt" im
  Nachrichtentext und in anderen Feldern an.

## Cortana

Most items are no longer applicable on Version 1903 and later. Classic
Cortana refers to older Cortana interface which was part of Start menu.

* Textuelle Antworten von Cortana werden in den meisten Fällen
  angezeigt. Falls nicht, öffnen Sie das StartMenü und starten Sie die Suche
  erneut.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.
* NVDA wird nun eine Erinnerungsbestätigung anzeigen, nachdem Sie eine
  eingestellt haben.
* In Version 1909 (November 2019 Update) and 20H1 build 18945 and later,
  modern search experience in File Explorer powered by Windows Search user
  interface is supported.

## Feedback Hub

* Feedback-Kathegorien werden in neueren App-Versionen nicht mehr zweimal
  angesagt.

## E-Mail

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

Dies bezieht sich auf den klassischen Edge (HTML-basierter Microsoft Edge).

* Die automatische Vervollständigung beim Tippen wird verfolgt und in der
  Adresszeile ordnungsgemäß angesagt. Dies wird Bestandteil von NVDA 2019.3.
* NVDA gibt keinen Vorschlags-Ton mehr wieder, wenn F11 für den
  Vollbildmodus gedrückt wird. Dies wird Bestandteil von NVDA 2019.3.
* Vorschlags Ton  für kombinierte Adress-Leiste entfernt. Dies wird
  Bestandteil von NVDA 2019.3.

## Microsoft Store

* Nach der Suche nach App-Aktualisierungen werden die App-Namen in der Liste
  der zu aktualisierenden Apps korrekt beschriftet.
* Beim Herunterladen von Inhalten wie Apps und Filmen wird NVDA den
  Produktnamen und den Fortschritt des Downloads bekannt geben.

## Moderne virtuelle Tastaturen

Die meisten unten aufgeführten Funktionen sind jetzt Teil von NVDA 2018.3
oder neuer.

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
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in 20H1 build 18965 and later.

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
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later. This will be part of NVDA 2019.3.
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
