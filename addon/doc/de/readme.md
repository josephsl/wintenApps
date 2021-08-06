# Windows App Essentials #

* Autoren: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2020.4 und neuer

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

* Diese Erweiterung benötigt Windows 10 Version 20H2 (Build 19042) oder
  neuer. Verwenden Sie für beste Ergebnisse die Erweiterung mit der neuesten
  Windows-Version (Windows 10 21H1 Build 19043).
* Obwohl eine Installation möglich ist, unterstützt diese Erweiterung keine
  Versionen von Windows Enterprise LTSC (Long-Term Servicing Channel) und
  Windows Server.
* Support for Windows 11 is experimental, and some features will not work
  (see relevant entries for details). A warning dialog will be shown if
  trying to install stable versions of this add-on on Windows 11 prior to
  general availability.
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
  cases, including when suggestion count changes as search progresses. This
  option is controlled by "Report object position information" in Object
  presentation panel found in NVDA settings.
* Bei der Suche im Startmenü oder Datei-Explorer in Windows 10 Version 1909
  (November 2019 Update) und neuer sind Fälle, in denen NVDA Suchergebnisse
  beim Überprüfen der Ergebnisse zweimal ankündigt, weniger auffällig, was
  auch die Brailleausgabe beim Überprüfen von Elementen konsistenter macht.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  will be tracked from an add-on called Event Tracker.
* Es ist möglich, nur bestimmte Ereignisse bzw. Ereignisse aus bestimmten
  Anwendungen zu verfolgen.
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

## Kalender

* NVDA sagt nicht mehr "bearbeiten" oder"schreibgeschützt" im
  Nachrichtentext und in anderen Feldern an.

## Cortana

Die meisten Elemente sind bei Verwendung von Cortana-Unterhaltungen (Windows
10 Version 2004 und neuer) anwendbar.

* Rückmeldungstexte von Cortana werden in den meisten Situationen
  angekündigt.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.
* In Windows 10 Version 1909 (November 2019 Update) und neuer wird die
  moderne Sucherfahrung im Datei-Explorer unterstützt von der
  Benutzeroberfläche der Windows-Suche unterstützt.

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
* Beim Herunterladen von Inhalten wie Apps und Filmen gibt NVDA den
  Produktnamen und den Downloadfortschritt an (funktioniert im
  aktualisierten Microsoft Store in Windows 11 nicht ordnungsgemäß).

## Moderne virtuelle Tastaturen

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* Beim Öffnen des Verlauf der Zwischenablage wird NVDA unter Umständen nicht
  mehr das Wort "Zwischenablage" mitteilen, wenn sich Elemente in der
  Zwischenablage befinden.
* Auf einigen Systemen, auf denen Windows 10 Version 1903 (Update vom Mai
  2019) und neuer ausgeführt wird, scheint NVDA nicht mehr zu tun, wenn das
  Emoji-Panel geöffnet wird.
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
* Das Erinnerungsdialogfeld von Windows Update wird als richtiger Dialog
  erkannt.
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
