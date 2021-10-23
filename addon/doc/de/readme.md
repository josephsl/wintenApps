# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA compatibility: 2021.2 and beyond

Hinweis: Ursprünglich als Windows 10 App Essentials bezeichnet, wurde es
2021 in Windows App Essentials umbenannt, um Windows 10 und zukünftige
Versionen wie Windows 11 zu unterstützen. Teile dieser Erweiterung beziehen
sich weiterhin auf den ursprünglichen Namen der Erweiterung.

Diese Erweiterung ist eine Sammlung von App-Modulen für verschiedene moderne
Windows-Apps sowie Verbesserungen und Korrekturen für bestimmte
Steuerelemente in Windows 10 und neuer.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Taschenrechner (modern)
* Cortana (Unterhaltungen)
* Mail
* Karten
* Microsoft Solitaire Collection
* Microsoft Store
* Moderne Tastatur
  (Emoji-Panel/Diktat/Spracheingabe/Hardware-Eingabevorschläge/Zwischenablageverlauf/moderne
  Eingabemethoden-Editoren)
* Kontakte
* Einstellungen (System-Einstellungen, Windows+I)
* Wetter
* Verschiedene Module für Bedienelemente wie Startmenü-Kacheln

Hinweise:

* This add-on requires Windows 10 20H2 (build 19042) or later and is
  compatible with Windows 11.
* Obwohl eine Installation möglich ist, unterstützt diese Erweiterung keine
  Versionen von Windows Enterprise LTSC (Long-Term Servicing Channel) und
  Windows Server.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* Bei Einträgen, die unten nicht aufgeführt sind, können Sie davon ausgehen,
  dass Funktionen Teil von NVDA sind und nicht mehr nutzbar sind, da die
  Erweiterung nicht unterstützte Windows-Versionen wie alte Windows
  10-Versionen nicht unterstützt oder Änderungen an Windows und Apps
  vorgenommen wurden, die keine Einträge mehr vornehmen.
* Einige Apps unterstützen den kompakten Overlay-Modus (z. B. im
  Taschenrechner immer ganz oben). Dieser Modus funktioniert mit der
  portablen NVDA-Version nicht ordnungsgemäß.

Eine Liste aller Änderungen in den einzelnen Versionen der Erweiterung
finden Sie im Dokument [Änderungsprotokolle  der veröffentlichten
Versionen][3].

## Allgemein

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses.
* Zusätzlich zu den von NVDA bereitgestellten UIA-Ereignishandlern werden
  die folgenden UIA-Ereignisse erkannt: Drag Start, Drag Cancel, Drag
  Complete, Drop Target Drag Enter, Drop Target Drag Leave, Drop Target
  Drop, Layout ungültig gemacht. Wenn die Protokollebene von NVDA auf Debug
  eingestellt ist, werden diese Ereignisse nachverfolgt, und bei
  Benachrichtigungsereignissen der UIA ist ein Debugton zu hören, wenn
  Benachrichtigungen von einem anderen Ort als der derzeit aktiven App
  stammen. In NVDA integrierte Ereignisse wie Namensänderungen und
  Controller für Ereignisse werden von der Erweiterung "Ereignis-Tracker"
  verfolgt.
* Beim Öffnen, Schließen, Neuordnen (Windows 11) oder Wechseln zwischen
  virtuellen Desktops gibt NVDA den Namen des aktiven virtuellen Desktops an
  (z. B. Desktop 2).
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

## Cortana

Die meisten Elemente sind bei Verwendung von Cortana-Unterhaltungen (Windows
10 Version 2004 und neuer) anwendbar.

* Rückmeldungstexte von Cortana werden in den meisten Situationen
  angekündigt.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.

## Mail

* Beim Navigieren durch Elemente in der Nachrichtenliste können Sie nun
  Tabellen-Navigationsbefehle verwenden, um Betreffzeilen zu überprüfen. Die
  Navigation zwischen Zeilen (Nachrichten) wird noch nicht unterstützt.

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
* Beim Herunterladen von Inhalten wie Apps und Filmen gibt NVDA den
  Produktnamen und den Download-Fortschritt an.

## Moderne virtuelle Tastaturen

Dazu gehören Emoji-Panel, Zwischenablageverlauf, Diktat-/Spracheingabe,
Hardware-Eingabevorschläge und moderne Eingabemethoden-Editoren für
bestimmte Sprachen. Aktivieren Sie beim Anzeigen von Emojis für die beste
Erfahrung die Unicode-Konsortium-Einstellung in den Spracheinstellungen von
NVDA und stellen Sie die Symbolstufe auf "Einige" oder höher ein. Drücken
Sie beim Einfügen aus dem Zwischenablageverlauf in Windows 10 die Leertaste
anstelle der Eingabetaste, um das ausgewählte Element einzufügen. NVDA
unterstützt auch das Panel für aktualisierte Eingabe-Erlebnisse in Windows
11.

* Wenn eine Emoji-Gruppe (einschließlich Kaomoji- und Symbolgruppe in
  Windows 10 Version 1903 oder neuer) ausgewählt wird, verschiebt NVDA das
  Navigatorobjekt nicht mehr in bestimmte Emojis.
* Unterstützung für das aktualisierte Erlebnis-Panel für die Eingabe
  (kombiniertes Emoji-Panel und Zwischenablageverlauf) in Windows 11
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
* Ungerade Steuerelementbezeichnungen in bestimmten Windows-Installationen
  wurden korrigiert.
* NVDA wird den Namen des optionalen Qualitäts-Update-Links, falls
  vorhanden, bekannt geben, normalerweise mit dem Namen "Jetzt herunterladen
  und installieren".

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
