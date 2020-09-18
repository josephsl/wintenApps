# Zugänglichkeitsverbesserungen für Windows 10 Apps #

* Autoren: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA compatibility: 2020.1 to 2020.3

Diese Erweiterung bietet eine Sammlung von Anwendungsmodulen für
verschiedene Windows 10 Anwendungen sowie Korrekturen in einigen Windows 10
Elementen.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Rechner (modern)
* Kalender
* Cortana (Unterhaltungen)
* Mail
* Karten
* Microsoft Solitaire Collection
* Microsoft Store
* Moderne Tastatur (Emoji-Panel- / Diktier- / Hardware-Eingabevorschläge /
  Cloud-Zwischenablage-Elemente in Version 1709 und höher)
* Kontakte
* Einstellungen (System-Einstellungen, Windows+I)
* Wetter.
* Diverse Steuermodule wie beispielsweise die Startmenübereiche.

Hinweise:

* Diese Erweiterung benötigt Windows 10 Version 1909 (Build 18363) oder
  neuer. Für beste Ergebnisse verwenden Sie die Erweiterung mit der neuesten
  stabilen Version von Windows 10 Version 2004 (Build 19041).
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
* Zusätzlich zu den von der NVDA erkannten Dialogen werden nun mehr Dialoge
  als richtige Dialoge erkannt und als solche gemeldet, einschließlich des
  Dialogs Insider-Vorschau (Einstellungsanwendung).
* NVDA kann in den meisten Fällen die Anzahl der Vorschläge bei der
  Durchführung einer Suche bekannt geben. Diese Option wird durch
  "Objekt-Positionsinformationen mitteilen" im Objektpräsentationsfenster in
  den NVDA-Einstellungen gesteuert.
* Bei der Suche im Startmenü oder im Datei-Explorer der Version 1909 (Update
  November 2019) und neuer sind Fälle von NVDA, in denen Suchergebnisse bei
  der Überprüfung von Ergebnissen zweimal angekündigt werden, weniger
  auffällig, was auch die Brailleausgabe bei der Überprüfung von Elementen
  einheitlicher macht.
* Die folgenden UIA-Ereignisse werden erkannt: Controller für, Drag Start,
  Drag Abbrechen, Drag Vollständig, Drag Ziel eingeben, Drag Ziel verlassen,
  Drag Ziel fallenlassen, Element ausgewählt, Elementstatus,
  Live-Regionsänderung, Benachrichtigung, Systemalarm, Textänderung, Tooltip
  geöffnet, Fenster geöffnet. Wenn NVDA so eingestellt ist, dass es mit
  aktivierter Debug-Protokollierung läuft, werden diese Ereignisse verfolgt,
  und für das UIA-Benachrichtigungsereignis wird ein Debug-Ton ausgegeben,
  wenn die Benachrichtigungen von einer anderen als der derzeit aktiven
  Anwendung kommen. Einige Ereignisse liefern zusätzliche Informationen wie
  die Elementanzahl im Controller für das Ereignis, den Zustand des Elements
  für das Zustandsänderungsereignis und den Elementtext für das
  Elementstatusereignis.
* Es ist möglich, nur bestimmte Ereignisse bzw. Ereignisse aus bestimmten
  Anwendungen zu verfolgen.
* NVDA verstummt nicht länger mehr oder Fehlertöne wiederzugeben, wenn die
  UIA-Automatisierungskennung für ein Element bei der Verfolgung von
  Ereignissen nicht aufgezeichnet werden konnte.
* Beim Öffnen, Schließen oder Umschalten virtueller Desktops meldet NVDA den
  aktuellen Desktop-Namen (z. B. Desktop 2).
* NVDA sagt den Text für die Größe des Startmenüs nicht mehr an, wenn die
  Bildschirmauflösung oder Ausrichtung geändert wird.
* Beim Anordnen von Startmenükacheln oder Action-Center-Schnellaktionen mit
  Alt+Umschalt+Pfeiltasten gibt NVDA Informationen zu gezogenen Elementen
  oder zur neuen Position des gezogenen Elements an.
* In den letzten Versionen von Word 365 meldet NVDA nicht mehr, dass beim
  Drücken der Tastenkombination Strg+Rücktaste das Wort "Vorheriges Wort
  löschen" gelöscht wird.
* Rückmeldungen wie z. B. Lautstärke-/Helligkeitsänderungen im
  Datei-Explorer und App-Update-Benachrichtigungen aus dem Microsoft Store
  können unterdrückt werden, indem die Benachrichtigung über Berichte in den
  Objektpräsentationseinstellungen von NVDA deaktiviert wird.
* Das Dialogfeld "Öffnen mit" in Version 2004 (Update Mai 2020) und neuer
  wird nun angesagt.

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

Die meisten Punkte sind ab der Version 1903 nicht mehr verwendbar, es sei
denn, Cortana (Version 2004 und neuer) wird verwendet.

* Rückmeldungstexte von Cortana werden in den meisten Situationen
  angekündigt.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.
* In der Version 1909 (Update November 2019) und neuer wird die moderne
  Suche im Datei-Explorer mit der Benutzeroberfläche der Windows-Suche
  unterstützt.

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

## Microsoft Solitaire Collection

* NVDA sagt nun die Karten und den Kartenstapel an.

## Microsoft Store

* Nach der Suche nach App-Aktualisierungen werden die App-Namen in der Liste
  der zu aktualisierenden Apps korrekt beschriftet.
* Beim Herunterladen von Inhalten wie Apps und Filmen wird NVDA den
  Produktnamen und den Fortschritt des Downloads bekannt geben.

## Moderne virtuelle Tastaturen

Dazu gehören Emoji-Panel, Verlauf der Zwischenablage, Diktat,
Hardware-Eingabevorschläge und moderne Eingabemethoden-Editoren für
bestimmte Sprachen. Wenn Sie Emojis betrachten, aktivieren Sie am besten die
Unicode-Konsortium-Einstellung in den Spracheinstellungen von NVDA und
setzen Sie die Symbol-Stufe auf "Einige" oder höher.

* Beim Öffnen des Verlauf der Zwischenablage wird NVDA unter Umständen nicht
  mehr das Wort "Zwischenablage" mitteilen, wenn sich Elemente in der
  Zwischenablage befinden.
* Auf einigen Systemen, auf denen die Version 1903 (Update Mai 2019) und
  neuer läuft, wird NVDA beim Öffnen des Emoji-Panels nichts mehr zu tun
  haben.
* Unterstützung für die moderne IME-Kandidaten-Schnittstelle für Chinesisch,
  Japanisch und Koreanisch (CJK) wurde in Version 2004 (Build 18965 und
  neuer) eingeführt.
* Wenn eine Emoji-Gruppe (einschließlich kaomoji und Symbolgruppe in Version
  1903 oder später) ausgewählt wird, verschiebt NVDA das Navigator-Objekt
  nicht mehr zu bestimmten Emojis.

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
