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
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions/modern input method
  editors)
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
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows, apps, and NVDA that makes entries no longer applicable.
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
  starten/abbrechen/abschließen (wird als Zustandsänderungsereignis
  erkannt), Drag-Drop-Effekt, Ziehen eines Elements wird erfasst,
  Drop-Ziel-Effekt.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example).
* Beim Ziehen und Ablegen von Elementen, z. B. beim Anordnen von
  angehefteten Einträgen (Kacheln in Windows 10) im Startmenü oder bei
  Schnellaktionen im Action Center mit Alt+Umschalt+Pfeiltasten, meldet NVDA
  vor bzw. während des Ziehens von Elementen "Ziehen" und/oder Zieh- und
  Ablegeeffekte. Dies ist nun Teil von NVDA 2022.4.
* Rückmeldungen wie z. B. Lautstärke-/Helligkeitsänderungen im
  Datei-Explorer und App-Update-Benachrichtigungen aus dem Microsoft Store
  können unterdrückt werden, indem die Benachrichtigung über Berichte in den
  Objektpräsentationseinstellungen von NVDA deaktiviert wird.
* In Windows 11 Version 22H2 und neuer wird der Status der
  Mikrofon-Stummschaltung (Windows+Alt+K) von überall her mitgeteilt.

## Cortana

* Rückmeldungstexte von Cortana werden in den meisten Situationen
  angekündigt.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.

## Karten

* NVDA spielt einen Ortungston für Kartenstandorte ab.

## Moderne virtuelle Tastaturen

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions, and modern input method
editors for certain languages across Windows 10 and 11. When viewing emojis,
for best experience, enable Unicode Consortium setting from NVDA's speech
settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* Wenn im Emoji-Panel von Windows 10 eine Emoji-Gruppe (einschließlich der
  Kaomoji- und Symbolgruppe) ausgewählt wird, verschiebt NVDA das
  Navigations-Objekt nicht mehr zu bestimmten Emojis.
* In der Zwischenablage von Windows 11 ist der Lesemodus standardmäßig
  ausgeschaltet, damit NVDA Menüeinträge für die Zwischenablage mitteilen
  kann.
* In Windows 11 22H2 Moment 1 and later, NVDA will announce suggested
  actions when compatible data such as phone numbers is copied to the
  clipboard.

## Kontakte

* Bei der Suche nach Kontakten wird der erste Vorschlag angezeigt.

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

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
