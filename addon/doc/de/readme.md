# Zugänglichkeitsverbesserungen für Windows 10 Apps #

* Autoren: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2020.4 und neuer

Diese Erweiterung bietet eine Sammlung von Anwendungsmodulen für
verschiedene Windows 10 Anwendungen sowie Korrekturen in einigen Windows 10
Elementen.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Taschenrechner (modern)
* Kalender
* Cortana (Unterhaltungen)
* Mail
* Karten
* Microsoft Solitaire Collection
* Microsoft Store
* Moderne Tastatur (Emoji-Panel / Diktat / Hardware-Eingabevorschläge /
  Zwischenablage-Verlauf / Editoren für moderne Eingabemethoden)
* Kontakte
* Einstellungen (System-Einstellungen, Windows+I)
* Wetter
* Verschiedene Module für Bedienelemente wie Startmenü-Kacheln

Hinweise:

* This add-on requires Windows 10 Version 2004 (build 19041) or later. For
  best results, use the add-on with latest Windows release (Windows 10
  Version 21H1/build 19043).
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support older Windows
  releases, or changes were made to Windows and apps that makes entries no
  longer applicable.
* Einige Apps unterstützen den kompakten Overlay-Modus (z. B. im
  Taschenrechner immer ganz oben). Dieser Modus funktioniert mit der
  portablen NVDA-Version nicht ordnungsgemäß.

Eine Liste aller Änderungen in den einzelnen Versionen der Erweiterung
finden Sie im Dokument [Änderungsprotokolle  der veröffentlichten
Versionen][3].

## Allgemein

* NVDA kann in den meisten Fällen die Anzahl der Vorschläge bei der
  Durchführung einer Suche bekannt geben. Diese Option wird durch
  "Objekt-Positionsinformationen mitteilen" im Objektpräsentationsfenster in
  den NVDA-Einstellungen gesteuert.
* Bei der Suche im Startmenü oder im Datei-Explorer der Version 1909 (Update
  November 2019) und neuer sind Fälle von NVDA, in denen Suchergebnisse bei
  der Überprüfung von Ergebnissen zweimal angekündigt werden, weniger
  auffällig, was auch die Brailleausgabe bei der Überprüfung von Elementen
  einheitlicher macht.
* Zusätzlich zu den von NVDA bereitgestellten UIA-Ereignishandlern werden
  die folgenden UIA-Ereignisse erkannt: Start starten, Abbruch ziehen,
  Abschluss ziehen, Ziel ziehen ziehen lassen, Ziel ziehen lassen, Ziel
  fallen lassen. Wenn die Protokollstufe von NVDA auf Debug eingestellt ist,
  werden diese Ereignisse verfolgt, und bei UIA-Benachrichtigungsereignissen
  ertönt ein Debug-Ton, wenn Benachrichtigungen von einem anderen Ort als
  der derzeit aktiven App stammen. Einige Ereignisse enthalten zusätzliche
  Informationen, z. B. die Anzahl der Elemente in der Steuerung für das
  Ereignis, den Status des Elements für das Statusänderungsereignis und den
  Elementtext für das Ereignis des Elementstatus.
* Es ist möglich, nur bestimmte Ereignisse bzw. Ereignisse aus bestimmten
  Anwendungen zu verfolgen.
* Beim Öffnen, Schließen, Neuordnen (Build 21337 oder neuer) oder Wechseln
  zwischen virtuellen Desktops gibt NVDA den Namen des aktiven virtuellen
  Desktops bekannt (z. B. Desktop 2).
* NVDA gibt beim Ändern der Bildschirmauflösung oder -ausrichtung keinen
  Text in der Startmenügröße mehr aus.
* Beim Anordnen von Startmenükacheln oder Action-Center-Schnellaktionen mit
  Alt+Umschalt+Pfeiltasten gibt NVDA Informationen zu gezogenen Elementen
  oder zur neuen Position des gezogenen Elements an.
* Rückmeldungen wie z. B. Lautstärke-/Helligkeitsänderungen im
  Datei-Explorer und App-Update-Benachrichtigungen aus dem Microsoft Store
  können unterdrückt werden, indem die Benachrichtigung über Berichte in den
  Objektpräsentationseinstellungen von NVDA deaktiviert wird.

## Rechner

* NVDA liest die Bildschirmmeldung des Grafikrechners nicht mehr doppelt
  vor.

## Kalender

* NVDA sagt nicht mehr "bearbeiten" oder"schreibgeschützt" im
  Nachrichtentext und in anderen Feldern an.

## Cortana

Die meisten Elemente gelten für die Verwendung von Cortana-Unterhaltungen
(Version 2004 und neuer).

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

Dies umfasst das Emoji-Bedienfeld, den Verlauf der Zwischenablage, die
Diktierfunktion, Vorschläge für Hardware-Eingaben und moderne Editoren für
Eingabemethoden für bestimmte Sprachen. Aktivieren Sie beim Anzeigen von
Emojis die Unicode Consortium-Einstellung in den Spracheinstellungen von
NVDA und stellen Sie die Symbolstufe auf "Einige" oder höher ein. Außerdem
unterstützt NVDA das aktualisierte Input Experience Panel in Build 21296 und
neuer.

* Beim Öffnen des Verlauf der Zwischenablage wird NVDA unter Umständen nicht
  mehr das Wort "Zwischenablage" mitteilen, wenn sich Elemente in der
  Zwischenablage befinden.
* Auf einigen Systemen, auf denen die Version 1903 (Update Mai 2019) und
  neuer läuft, wird NVDA beim Öffnen des Emoji-Panels nichts mehr zu tun
  haben.
* Wenn eine Emoji-Gruppe (einschließlich kaomoji und Symbolgruppe in Version
  1903 oder später) ausgewählt wird, verschiebt NVDA das Navigator-Objekt
  nicht mehr zu bestimmten Emojis.
* Unterstützung für das aktualisierte Input Experience Panel (kombiniertes
  Emoji-Bedienfeld und Zwischenablageverlauf) in Build 21296 und neuer
  hinzugefügt.

## Kontakte

* Bei der Suche nach Kontakten wird der erste Vorschlag angekündigt,
  insbesondere bei Verwendung aktueller App-Veröffentlichungen.

## Einstellungen

* Bestimmte Informationen, wie z. B. der Fortschritt von Windows Update,
  werden automatisch gemeldet, einschließlich des Widgets für die Speicher-
  und Festplattenbereinigung und der Fehler von Windows Update.
* Werte in Fortschrittsbalken und andere Informationen werden nicht mehr
  zweimal angesagt.
* Das Erinnerungsdialogfeld von Windows Update wird als richtiger Dialog
  erkannt.
* Odd control labels seen in certain Windows installations has been
  corrected.
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
