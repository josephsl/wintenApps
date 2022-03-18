# Windows App Essentials #

* Autoren: Joseph Lee, Derek Riemer und weitere
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2021.3 und neuer

Hinweis: Ursprünglich als Windows 10 App Essentials bezeichnet, wurde es
2021 in Windows App Essentials umbenannt, um Windows 10 und zukünftige
Versionen wie Windows 11 zu unterstützen. Teile dieser Erweiterung beziehen
sich weiterhin auf den ursprünglichen Namen der Erweiterung.

Diese Erweiterung ist eine Sammlung von App-Modulen für verschiedene moderne
Windows-Apps sowie Verbesserungen und Korrekturen für bestimmte
Steuerelemente in Windows 10 und neuer.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Rechner
* Cortana
* Mail
* Karten
* Microsoft Solitaire Collection
* Moderne Tastatur
  (Emoji-Panel/Diktat/Spracheingabe/Hardware-Eingabevorschläge/Zwischenablageverlauf/moderne
  Eingabemethoden-Editoren)
* Notepad (Windows 11)
* Kontakte
* Einstellungen (System-Einstellungen, Windows+I)
* Wetter
* Verschiedene Module für Bedienelemente wie Startmenü-Kacheln

Hinweise:

* Diese Erweiterung benötigt Windows 10 Version 21H1 (Build 19043) oder
  neuer und ist kompatibel mit Windows 11.
* Obwohl eine Installation möglich ist, unterstützt diese Erweiterung keine
  Versionen von Windows Enterprise LTSC (Long-Term Servicing Channel) und
  Windows Server.
* Nicht alle Funktionen von Windows Insider Preview Builds werden
  unterstützt.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* Bei Einträgen, die unten nicht aufgeführt sind, können Sie davon ausgehen,
  dass Funktionen Teil von NVDA sind und nicht mehr nutzbar sind, da die
  Erweiterung nicht unterstützte Windows-Versionen wie alte Windows
  10-Versionen nicht unterstützt oder Änderungen an Windows und Apps
  vorgenommen wurden, die keine Einträge mehr vornehmen.
* Einige Apps unterstützen den kompakten Overlay-Modus (z. B. im
  Taschenrechner immer ganz oben). Dieser Modus funktioniert mit der
  portablen NVDA-Version nicht ordnungsgemäß.
* Für eine optimale Nutzung von Anwendungen, die Webtechnologien und
  -inhalte einbetten, wie z. B. das Startmenü und sein Kontextmenü,
  aktivieren Sie die Einstellung "Automatischer Fokusmodus bei
  Fokusänderungen" im NVDA-Einstellungsdialogfeld für den Suchmodus.

Eine Liste aller Änderungen in den einzelnen Versionen der Erweiterung
finden Sie im Dokument [Änderungsprotokolle  der veröffentlichten
Versionen][3].

## Allgemein

* Zusätzlich zu den von NVDA bereitgestellten UIA-Ereignis-Handlern werden
  die folgenden UIA-Ereignisse und -Eigenschaften der Effekte erkannt: Drag
  abgeschlossen, Drag & Drop, Drop Target. Wenn die Protokollstufe in NVDA
  auf Debug eingestellt ist, werden diese Ereignisse verfolgt und
  protokolliert.
* Beim Öffnen, Schließen, Neuordnen (Windows 11) oder Wechseln zwischen
  virtuellen Desktops gibt NVDA den Namen des aktiven virtuellen Desktops an
  (z. B. Desktop 2).
* Beim Anordnen von angehefteten Einträgen (Kacheln in Windows 10) im
  Startmenü oder in den Schnellaktionen des Action Centers mit
  Alt+Umschalt+Pfeiltasten teilt NVDA Informationen über verschobene
  Elemente oder die neue Position des verschobenen Elements mit.
* Rückmeldungen wie z. B. Lautstärke-/Helligkeitsänderungen im
  Datei-Explorer und App-Update-Benachrichtigungen aus dem Microsoft Store
  können unterdrückt werden, indem die Benachrichtigung über Berichte in den
  Objektpräsentationseinstellungen von NVDA deaktiviert wird.
* In den Windows 11 Insider Preview-Builds wird der Status die
  Stummschaltung für das Mikrofon (Win+Alt+K) von überall her angezeigt.

## Rechner

* NVDA liest die Bildschirmmeldung des Grafikrechners nicht mehr doppelt
  vor.
* In Windows 10 sind Verlaufs- und Speicherlistenelemente richtig
  beschriftet. Dies ist jetzt Teil von NVDA 2022.1.
* NVDA teilt nun den Inhalt der Anzeige des Taschenrechners mit, wenn
  Befehle im wissenschaftlichen Modus ausgeführt werden,
  z. B. trigonometrische Operationen.

## Cortana

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

## Microsoft Solitaire Collection

* NVDA sagt nun die Karten und den Kartenstapel an.

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

* Wenn in Windows 10 eine Emoji-Gruppe (einschließlich Kaomoji- und
  Symbolgruppe) ausgewählt ist, verschiebt NVDA das Navigator-Objekt nicht
  mehr in bestimmte Emojis.
* Unterstützung für das aktualisierte Erlebnis-Panel für die Eingabe
  (kombiniertes Emoji-Panel und Zwischenablageverlauf) in Windows 11
  hinzugefügt.
* In Windows 11 ist es wieder möglich, die Pfeiltasten zu verwenden, um
  Emojis zu überprüfen, wenn das Emoji-Panel geöffnet wird. Dies ist jetzt
  Teil von NVDA 2022.1.
* In der Zwischenablage von Windows 11 ist der Lesemodus standardmäßig
  ausgeschaltet, damit NVDA Menüeinträge für die Zwischenablage mitteilen
  kann.

## Notepad

Dies bezieht sich auf Windows 11 Notepad Version 11 oder neuer.

* NVDA teilt die Status-Elemente wie Zeilen- und Spalteninformationen mit,
  wenn der Befehl Statusleiste mitteilen (NVDA+Ende im Desktop-Layout,
  NvDA+Umschalt+Ende im Laptop-Layout) ausgeführt wird.
* NVDA liest den eingegebenen Text nicht mehr vor, sobald die Eingabetaste
  im Dokument gedrückt wird.

## Kontakte

* Bei der Suche nach Kontakten wird der erste Vorschlag angekündigt,
  insbesondere bei Verwendung aktueller App-Veröffentlichungen.

## Einstellungen

* Ungerade Steuerelementbezeichnungen in bestimmten Windows-Installationen
  wurden korrigiert.
* NVDA teilt den Namen optionaler Qualitätsupdates mit, falls vorhanden
  (Link zum Download und Jetzt installieren in Windows 10,
  Download-Schaltfläche in Windows 11).
* In Windows 11 werden die Breadcrumb-Leisten richtig erkannt.

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
