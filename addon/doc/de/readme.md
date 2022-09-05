# Windows App Essentials #

* Autoren: Joseph Lee, Derek Riemer und weitere
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2022.2 und neuer

Hinweis: Ursprünglich als Windows 10 App Essentials bezeichnet, wurde es
2021 in Windows App Essentials umbenannt, um Windows 10 und zukünftige
Versionen wie Windows 11 zu unterstützen. Teile dieser Erweiterung beziehen
sich weiterhin auf den ursprünglichen Namen der Erweiterung.

Diese Erweiterung ist eine Sammlung von App-Modulen für verschiedene moderne
Windows-Apps sowie Verbesserungen und Korrekturen für bestimmte
Steuerelemente in Windows 10 und neuer.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Cortana
* Karten
* Moderne Tastatur
  (Emoji-Bedienfeld/Diktat/Sprachsteuerung/Hardware-Eingabevorschläge/Zwischenablage-Verlauf/Vorgeschlagene
  Aktionen (Vorschau) bzw. Moderne Eingabemethoden-Editoren)
* Kontakte
* Einstellungen (System-Einstellungen, Windows+I)
* Sprachzugang (Windows 11 Version 22H2)
* Wetter
* Verschiedene Module für Bedienelemente wie Startmenü-Kacheln

Hinweise:

* Diese Erweiterung erfordert Windows 10 Version 21H2 (Build 19044), Windows
  11 Version 21H2 (Build 22000) oder neuere Versionen.
* Obwohl eine Installation möglich ist, unterstützt diese Erweiterung keine
  Versionen von Windows Enterprise LTSC (Long-Term Servicing Channel) und
  Windows Server.
* Wenn der Updater für NVDA-Erweiterungen 22.08 oder neuer installiert ist
  und Add-on-Updates im Hintergrund aktiviert sind, wird Windows App
  Essentials auf nicht unterstützten Windows-Versionen überhaupt nicht
  installiert.
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
  die folgenden UIA-Ereignisse und -Eigenschaften erkannt: Ziehen
  abgeschlossen, Ziehen-fallenlassen-Effekt, Ziel fallenlassen. Wenn die
  NVDA-Protokollebene auf Debug eingestellt ist, werden diese Ereignisse
  verfolgt und protokolliert.
* Beim Öffnen, Schließen, Neuordnen (Windows 11) oder Wechseln zwischen
  virtuellen Desktops gibt NVDA den Namen des aktiven virtuellen Desktops an
  (z. B. Desktop 2).
* Beim Ziehen und Ablegen von Objekten, z. B. beim Anordnen von angehefteten
  Einträgen (Kacheln in Windows 10) im Startmenü oder bei Schnellaktionen im
  Action Center mit Alt+Umschalt+Pfeiltasten, meldet NVDA vor bzw. während
  des Ziehens von Objekten "Ziehen" und/oder Zieh- und Ablegeeffekte. Die
  NVDA-Ansage "Ziehen" ist Teil von NVDA 2022.4.
* Rückmeldungen wie z. B. Lautstärke-/Helligkeitsänderungen im
  Datei-Explorer und App-Update-Benachrichtigungen aus dem Microsoft Store
  können unterdrückt werden, indem die Benachrichtigung über Berichte in den
  Objektpräsentationseinstellungen von NVDA deaktiviert wird.
* In Windows 11 Version 22H2 und neuer wird der Status der
  Mikrofon-Stummschaltung (Windows+Alt+K) von überall her mitgeteilt.
* Änderungen des Elementstatus werden in weiteren Anwendungen,
  einschließlich Visual Studio Community 2022, mitgeteilt. Dies ist Teil von
  NVDA 2022.4.

## Cortana

* Rückmeldungstexte von Cortana werden in den meisten Situationen
  angekündigt.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.

## Karten

* NVDA spielt einen Ortungston für Kartenstandorte ab.

## Moderne virtuelle Tastaturen

Dazu gehören das Emoji-Bedienfeld, der Verlauf der Zwischenablage,
Diktat-/Stimmeingabe, Hardware-Eingabevorschläge, vorgeschlagene Aktionen
(Vorschau) und moderne Eingabemethoden-Editoren für bestimmte Sprachen in
Windows 10 und 11. Aktivieren Sie bei der Anzeige von Emojis die Einstellung
Unicode-Konsortium in den NVDA-Spracheinstellungen und setzen Sie die
Symbolebene auf "Einige" oder höher. Drücken Sie beim Einfügen aus dem
Zwischenablageverlauf in Windows 10 die Leertaste anstelle der Eingabetaste,
um das ausgewählte Element einzufügen.

* Wenn in Windows 10 eine Emoji-Gruppe (einschließlich Kaomoji- und
  Symbolgruppe) ausgewählt ist, verschiebt NVDA das Navigator-Objekt nicht
  mehr in bestimmte Emojis.
* In Windows 11 ist es wieder möglich, die Pfeiltasten zu verwenden, um
  Emojis zu überprüfen, wenn das Emoji-Panel geöffnet wird. Dies ist jetzt
  Teil von NVDA 2022.1.
* In der Zwischenablage von Windows 11 ist der Lesemodus standardmäßig
  ausgeschaltet, damit NVDA Menüeinträge für die Zwischenablage mitteilen
  kann.
* In der Insider Preview Build 25115 (auch ab Windows 11 beta build 22622
  verfügbar) wird NVDA vorgeschlagene Aktionen mitteilen, wenn kompatible
  Daten wie Telefonnummern in die Zwischenablage kopiert werden.

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
* In Windows 10 und 11 22H2 unterbricht NVDA die Sprachausgabe und meldet
  Updates an den Windows Update-Status, während der Download und die
  Installation fortschreiten. Dies kann zu Sprachunterbrechungen führen,
  wenn Sie in der Einstellungen-App navigieren, während Updates
  heruntergeladen und installiert werden. Wenn Sie Windows 11 22H2 und neuer
  mit aktivierter selektiver Eventregistrierung verwenden, müssen Sie den
  Fokus in die Update-Liste bewegen, sobald diese erscheinen, damit NVDA den
  Fortschritt lesen kann.

## Sprachzugang

Dies bezieht sich auf die in Windows 11 Version 22H2 eingeführte Funktion
für den Sprachzugang.

* NVDA teilt den Mikrofon-Status mit, wenn das Mikrofon über die
  Sprachzugriffsoberfläche umgeschaltet wird.

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
