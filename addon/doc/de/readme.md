# Zugänglichkeitsverbesserungen für Windows 10 Apps #

* Autoren: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][4] compatible with NVDA 2019.2.1 and earlier

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
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Kontakte
* Einstellungen (Systemeinstellungen, Windows+I)
* Wetter.
* Diverse Steuermodule wie beispielsweise die Startmenübereiche.

Hinweise:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18363) and latest stable version of NVDA.
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
* Untermenü-Einträge werden in verschiedenen Anwendungen richtig erkannt,
  darunter das Kontextmenü für die Kachel-Ansicht im Startmenü und das
  App-Menü in Microsoft Edge in der Version 1809 (Update Oktober 2018).
* Zusätzlich zu den von der NVDA erkannten Dialogen werden nun mehr Dialoge
  als richtige Dialoge erkannt und als solche gemeldet, einschließlich des
  Dialogs Insider-Vorschau (Einstellungsanwendung).
* NVDA kann in den meisten Fällen die Anzahl der Vorschläge bei der
  Durchführung einer Suche bekannt geben. Diese Option wird durch
  "Objekt-Positionsinformationen mitteilen" im Objektpräsentationsfenster in
  den NVDA-Einstellungen gesteuert.
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu. This is now part of NVDA 2019.3.
* Bei der Suche im Startmenü oder im Datei-Explorer der Version 1909 (Update
  November 2019) und neuer sind Fälle von NVDA, in denen Suchergebnisse bei
  der Überprüfung von Ergebnissen zweimal angekündigt werden, weniger
  auffällig, was auch die Brailleausgabe bei der Überprüfung von Elementen
  einheitlicher macht.
* In bestimmten Kontextmenüs (z.B. in Edge) werden Positionsinformationen
  (z.B. 1 von 2) nicht mehr angesagt.
* Die folgenden Ereignisse für die Benutzeroberflächenautomatisierung werden
  erkannt: Steuerung für, Drag Start, Drag Cancel, Drag Complete, drag
  target enter, drag target leave, drag target dropped, Element ausgewählt,
  Elementstatus, Änderung der Live-Region, Benachrichtigung, Systemalarm,
  Textänderung, Tooltipp geöffnet, Fenster geöffnet. Wenn NVDA so
  eingestellt ist, dass es mit aktivierter Debug-Protokollierung läuft,
  werden diese Ereignisse verfolgt und für das Benachrichtigungsereignis der
  Benutzeroberflächenautomatisierung wird ein Fehler-Ton ausgegeben, wenn
  Benachrichtigungen von einem anderen Ort als der aktuell aktiven Anwendung
  stammen.
* Es ist möglich, nur bestimmte Ereignisse bzw. Ereignisse aus bestimmten
  Anwendungen zu verfolgen.
* Tooltips from Edge and universal apps are recognized and will be
  announced. This is now part of NVDA 2019.3.
* Beim Öffnen, Schließen oder Umschalten virtueller Desktops meldet NVDA den
  aktuellen Desktop-Namen (z. B. Desktop 2).
* NVDA sagt den Text für die Größe des Startmenüs nicht mehr an, wenn die
  Bildschirmauflösung oder Ausrichtung geändert wird.
* App name and version for various Microsoft Store apps are now shown
  correctly. This is now part of NVDA 2019.3.
* Beim Anordnen von Startmenükacheln oder Action-Center-Schnellaktionen mit
  Alt+Umschalt+Pfeiltasten gibt NVDA Informationen zu gezogenen Elementen
  oder zur neuen Position des gezogenen Elements an.

## Rechner

* NVDA sagt die Rechenergebnisse beim Drücken der Eingabe- oder Escape-Taste
  an.
* Für Berechnungen wie Umrechnungen von Einheiten und Währungen gibt NVDA
  das Ergebnis Ergebnisse bekannt, sobald die Berechnung eingegeben wird.
* NVDA nennt bei Berechnungsergebnissen nicht mehr "Überschriftebenen".
* NVDA meldet, wenn die maximale Anzahl der Ziffern während der Eingabe von
  Ausdrücken erreicht wurde.
* Unterstützung für den Always-On-Modus in Calculator Version 10.1908 und
  neuer hinzugefügt.

## Kalender

* NVDA sagt nicht mehr "bearbeiten" oder"schreibgeschützt" im
  Nachrichtentext und in anderen Feldern an.

## Cortana

Die meisten Punkte sind ab der Version 1903 nicht mehr anwendbar. Classic
Cortana bezieht sich auf eine ältere Cortana-Schnittstelle, die Teil des
Startmenüs war.

* Textuelle Antworten von Cortana werden in den meisten Fällen
  angezeigt. Falls nicht, öffnen Sie das StartMenü und starten Sie die Suche
  erneut.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.
* NVDA wird nun eine Erinnerungsbestätigung anzeigen, nachdem Sie eine
  eingestellt haben.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

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

* Text auto-complete will be tracked and announced in address omnibar. This
  is now part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This is now part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This is now part
  of NVDA 2019.3.

## Microsoft Store

* Nach der Suche nach App-Aktualisierungen werden die App-Namen in der Liste
  der zu aktualisierenden Apps korrekt beschriftet.
* Beim Herunterladen von Inhalten wie Apps und Filmen wird NVDA den
  Produktnamen und den Fortschritt des Downloads bekannt geben.

## Moderne virtuelle Tastaturen

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including redesigned panel in Version 1809 (build 17661 and later)
  and changes made in Version 1903 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in Version
  2004 (build 18963 and later) as the app has been renamed. All of these
  changes are now part of NVDA 2019.3.
* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* Auf einigen Systemen, auf denen die Version 1903 (Update Mai 2019) und
  neuer läuft, wird NVDA beim Öffnen des Emoji-Panels nichts mehr zu tun
  haben.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

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
  later. This is now part of NVDA 2019.3.
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

[4]: https://addons.nvda-project.org/files/get.php?file=w10-2019
