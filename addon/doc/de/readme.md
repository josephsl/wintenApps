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
* Die Unterstützung für Windows 11 ist experimentell und einige Funktionen
  funktionieren nicht (siehe entsprechende Einträge für Details).
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

* NVDA kann in den meisten Fällen die Anzahl der Vorschläge bei der
  Durchführung einer Suche bekannt geben. Diese Option wird durch
  "Objekt-Positionsinformationen mitteilen" im Objektpräsentationsfenster in
  den NVDA-Einstellungen gesteuert.
* Bei der Suche im Startmenü oder Datei-Explorer in Windows 10 Version 1909
  (November 2019 Update) und neuer sind Fälle, in denen NVDA Suchergebnisse
  beim Überprüfen der Ergebnisse zweimal ankündigt, weniger auffällig, was
  auch die Brailleausgabe beim Überprüfen von Elementen konsistenter macht.
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

Dazu gehören Emoji-Panel, Zwischenablageverlauf, Diktat,
Hardware-Eingabevorschläge und moderne Eingabemethoden-Editoren für
bestimmte Sprachen. Aktivieren Sie beim Anzeigen von Emojis für die beste
Erfahrung die Unicode-Konsortium-Einstellung in den Spracheinstellungen von
NVDA und setzen Sie die Symbolstufe auf "Einige" oder höher. Außerdem
unterstützt NVDA das aktualisierte Eingabeerlebnis-Panel in Windows 11.

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
