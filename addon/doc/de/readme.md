# Windows App Essentials #

* Autoren: Joseph Lee, Derek Riemer und weitere
* [Stabile Version herunterladen][1]
* [Beta-Version herunterladen][2]
* [Entwicklerversion herunterladen][3]
* NVDA-Kompatibilität: 2022.4 und neuer

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
  (Emoji-Panel/Touch-Tastatur/Diktat/Sprachsteuerung/Hardware-Eingabevorschläge/Zwischenablage-Verlauf/Vorgeschlagene
  Aktionen/Editoren für moderne Eingabemethoden)
* Einstellungen (System-Einstellungen, Windows+I)
* Sprachzugang (Windows 11 Version 22H2)
* Wetter
* Verschiedene Module für Steuerungen und Funktionen wie die Mitteilung
  virtueller Desktops

Hinweise:

* Diese Erweiterung erfordert Windows 10 Version 21H2 (Build 19044), Windows
  11 Version 21H2 (Build 22000) oder neuere Versionen.
* Die Dauer der Unterstützung für Feature-Updates ist an die Dauer des
  Consumer-Supports (Home, Pro, Pro Education, Pro for Workstations
  Editionen) gebunden und die Erweiterung kann den Support für ein
  Feature-Update vor dem Ende des Consumer-Supports beenden. Unter
  aka.ms/WindowsTargetVersioninfo finden Sie weitere Informationen und
  Support-Informationen dazu.
* Obwohl eine Installation möglich ist, unterstützt diese Erweiterung keine
  Versionen von Windows Enterprise LTSC (Long-Term Servicing Channel) und
  Windows Server.
* Wenn der Updater für NVDA-Erweiterungen installiert ist und Add-on-Updates
  im Hintergrund aktiviert sind, wird Windows App Essentials auf nicht
  unterstützten Windows-Versionen überhaupt nicht installiert.
* Nicht alle Funktionen von Windows Insider Preview-Builds werden
  unterstützt. Dies gilt vor allem für Funktionen, die einer Untergruppe von
  Windows Insidern im Canary- und Dev-Channel vorgestellt werden.
* Der Dev-Kanal der NVDA-Erweiterung wird Änderungen enthalten,
  einschließlich experimenteller Inhalte, die in den Beta- und
  Stable-Releases enthalten sein können oder auch nicht, und der Beta-Kanal
  wird Änderungen enthalten, die für zukünftige Stable-Releases geplant
  sind.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* Für eine optimale Nutzung von Anwendungen, die Webtechnologien und
  -inhalte einbetten, wie z. B. das Startmenü und sein Kontextmenü,
  aktivieren Sie die Einstellung "Automatischer Fokusmodus bei
  Fokusänderungen" im NVDA-Einstellungsdialogfeld für den Suchmodus.

Eine Liste der Änderungen, die zwischen den einzelnen Versionen der
NVDA-Erweiterung vorgenommen wurden, finden Sie im Dokument
[Änderungsprotokolle für Versionen der NVDA-Erweiterung][4].

## Allgemein

* Beim Öffnen, Schließen oder Umschalten zwischen virtuellen Desktops teilt
  NVDA den Namen des aktiven virtuellen Desktops mit (z. B. Desktop 2).
* In Windows 11 zeigt NVDA beim Öffnen des Startmenüs die Highlights der
  Suche an. Dies ist jetzt Teil von NVDA 2023.1.
* In Windows 11 Version 22H2 und neuer kann die Maus- bzw. Touch-Interaktion
  zur Interaktion mit dem neu gestalteten Überlauffenster der Taskleiste und
  dem Dialogfeld "Öffnen mit" verwendet werden. Dies ist nun Teil von NVDA
  2023.1.
* NVDA zeichnet die Prozessor-Architektur für die aktuelle
  Windows-Installation (x86/32-bit, AMD64, ARM64) auf, wenn es gestartet
  wird. Dies ist nun Teil von NVDA 2023.1.
* Die Taskleiste von Windows 10 und 11 wurde verbessert, u. a. durch die
  Anzeige der Ergebnisse der Neuanordnung von Symbolen beim Drücken von
  Alt+Umschalt+Pfeiltasten nach links/rechts (Windows 11 vor Build 25267)
  und durch die Anzeige der Elementposition beim Bewegen durch die
  Taskleistensymbole (Windows 10 und 11 vor Build 25281).
* In Programmen wie dem Datei-Explorer und dem Notepad, in denen Fenster mit
  Registerkarten unterstützt werden, zeigt NVDA den Namen und die Position
  der Registerkarten an, wenn zwischen ihnen gewechselt wird. Dies ist nun
  Teil in NVDA 2023.2.

## Cortana

* Rückmeldungstexte von Cortana werden in den meisten Situationen
  angekündigt.

## Karten

* NVDA unterbricht in manchen Fällen die Sprachausgabe nicht mehr, wenn der
  Fokus auf anderen Elementen als der Kartensteuerung liegt.

## Moderne virtuelle Tastaturen

Dazu gehören das Emoji-Bedienfeld, der Verlauf der Zwischenablage, die
Touch-Tastatur, Diktat-/Spracheingabe, Hardware-Eingabevorschläge,
vorgeschlagene Aktionen und moderne Eingabemethoden-Editoren für bestimmte
Sprachen in Windows 10 und 11. Aktivieren Sie bei der Anzeige von Emojis die
Unicode-Konsortium-Einstellung in den NVDA-Spracheinstellungen und setzen
Sie die Symbolebene auf "Einige" oder höher. Drücken Sie beim Einfügen aus
dem Verlauf der Zwischenablage in Windows 10 die Leertaste anstelle der
Eingabetaste, um das ausgewählte Element einzufügen.

* Wenn im Emoji-Panel von Windows 10 eine Emoji-Gruppe (einschließlich der
  Kaomoji- und Symbolgruppe) ausgewählt wird, verschiebt NVDA das
  Navigations-Objekt nicht mehr zu bestimmten Emojis.
* In der Zwischenablage von Windows 11 wird der Durchsuchen-Modus
  standardmäßig ausgeschaltet, damit NVDA Menü-Einträge für die
  Zwischenablage mitteilen kann. Dies ist nun Teil von NVDA 2023.1.
* In Windows 11 Version 22H2 und neuer zeigt NVDA vorgeschlagene Aktionen
  an, wenn kompatible Daten wie Telefonnummern in die Zwischenablage kopiert
  werden.

## Einstellungen

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
