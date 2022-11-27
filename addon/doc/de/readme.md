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
  (Emoji-Bedienfeld/Diktierfunktion/Sprachsteuerung/Hardware-Eingabevorschläge/Zwischenablage-Historie/Vorgeschlagene
  Aktionen/Editoren für moderne Eingabemethoden)
* Kontakte
* Einstellungen (System-Einstellungen, Windows+I)
* Sprachzugang (Windows 11 Version 22H2)
* Wetter
* Miscellaneous modules for controls and features such as virtual desktops
  announcements

Hinweise:

* Diese Erweiterung erfordert Windows 10 Version 21H2 (Build 19044), Windows
  11 Version 21H2 (Build 22000) oder neuere Versionen.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Obwohl eine Installation möglich ist, unterstützt diese Erweiterung keine
  Versionen von Windows Enterprise LTSC (Long-Term Servicing Channel) und
  Windows Server.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in dev
  channel. For beta channel, only the latest build (22623) is supported.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with the portable version
  of NVDA.
* Für eine optimale Nutzung von Anwendungen, die Webtechnologien und
  -inhalte einbetten, wie z. B. das Startmenü und sein Kontextmenü,
  aktivieren Sie die Einstellung "Automatischer Fokusmodus bei
  Fokusänderungen" im NVDA-Einstellungsdialogfeld für den Suchmodus.

Eine Liste aller Änderungen in den einzelnen Versionen der Erweiterung
finden Sie im Dokument [Änderungsprotokolle  der veröffentlichten
Versionen][3].

## Allgemein

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect. These events are now part of NVDA 2022.4.
* Beim Öffnen, Schließen oder Umschalten zwischen virtuellen Desktops teilt
  NVDA den Namen des aktiven virtuellen Desktops mit (z. B. Desktop 2).
* Beim Ziehen und Ablegen von Elementen, z. B. beim Anordnen von
  angehefteten Einträgen (Kacheln in Windows 10) im Startmenü oder bei
  Schnellaktionen im Action Center mit Alt+Umschalt+Pfeiltasten, meldet NVDA
  vor bzw. während des Ziehens von Elementen "Ziehen" und/oder Zieh- und
  Ablegeeffekte. Dies ist nun Teil von NVDA 2022.4.
* Mitteilungen wie Lautstärke-/Helligkeits-/Mikrofonstummschaltung (Windows
  11 Version 22H2 und neuer), Änderungen im Datei-Explorer und
  App-Update-Benachrichtigungen aus dem Microsoft Store können unterdrückt
  werden, indem Sie in den NVDA-Einstellungen für die Objekt-Darstellung
  "Benachrichtigungen mitteilen" deaktivieren.
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens. This is now part of NVDA 2023.1.

## Cortana

* Rückmeldungstexte von Cortana werden in den meisten Situationen
  angekündigt.
* NVDA verstummt bei der Verwendung von Cortana, so dass sich die Stimmen
  nicht mehr in die Quere kommen.

## Karten

* NVDA spielt einen Ortungston für Kartenstandorte ab.

## Moderne virtuelle Tastaturen

Dazu gehören das Emoji-Bedienfeld, der Verlauf der Zwischenablage,
Diktier-/Stimmeingabe, Hardware-Eingabevorschläge, vorgeschlagene Aktionen
und moderne Eingabemethoden-Editoren für bestimmte Sprachen in Windows 10
und 11. Aktivieren Sie bei der Anzeige von Emojis die Einstellung
Unicode-Konsortium in den Spracheinstellungen von NVDA und setzen Sie die
Symbolebene auf "einige" oder höher. Drücken Sie beim Einfügen aus dem
Zwischenablageverlauf in Windows 10 die Leertaste anstelle der Eingabetaste,
um das ausgewählte Element einzufügen.

* Wenn im Emoji-Panel von Windows 10 eine Emoji-Gruppe (einschließlich der
  Kaomoji- und Symbolgruppe) ausgewählt wird, verschiebt NVDA das
  Navigations-Objekt nicht mehr zu bestimmten Emojis.
* In der Zwischenablage von Windows 11 ist der Lesemodus standardmäßig
  ausgeschaltet, damit NVDA Menüeinträge für die Zwischenablage mitteilen
  kann.
* In Windows 11 Version 22H2 Moment 1 und neuer sagt NVDA vorgeschlagene
  Aktionen an, wenn kompatible Daten wie Telefonnummern in die
  Zwischenablage kopiert werden.

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
