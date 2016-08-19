# Windows 10 App Essentials #

* Autor: Joseph Lee
* [Stabile Version][1] herunterladen
* [Entwicklerversion][2] herunterladen

Diese Erweiterung ist ein Paket von App-Modulen für diverse Windows 10 Apps
sowie Korrekturen in einigen Windows 10 Steuerung.

Die folgenden App-Module oder unterstützte Module für einige Apps sind
inbegriffen (siehen Sie in jeden App-Bereich für Details, um zu sehen,
welche inbegriffen sind):

* Wecker und Uhr.
* Bank of America
* Rechner (modern).
* Cortana
* Insider Hub/Feedback-Hub (Nur für Windows Insider).
* Microsoft Edge
* Einstellungen (System-Einstellungen mit Win+I).
* Skype Preview
* Twitter.
* TeamViewer Touch.
* Diverse Steuermodule wie beispielsweise die Startmenübereiche

## Allgemein

* Im Kontextmenü von Kacheln werden untermenüs korrekt erkannt
* Beim Minimieren aller Anwendungen mit Windows+m wird nicht mehr "Feld"
  angezeigt (betrifft die Insider-Versionen)
* Einige Dialoge werden jetzt als richtige Dialoge erkannt. Dazu gehören
  Dialoge der technischen Vorschau (Einstellungs-app) sowie neue UAC-Dialoge
  in Version 14328 und neuer.
* Time picker announcement works in non-English locales.

## Wecker und Uhr

* Das Steuerelement zum Einstellen der Weckzeit wird nun erkannt. Dies
  betrifft auch das Steuerelement zum Einstellen des geplanten Zeitpunkts
  für einen neustart des Systems nach der Installation von Aktualisierungen
  für Windows.

## Rechner

* Wenn Sie die Eingabetaste drücken, wird das Ergebnis der Berechnung
  angesagt.

## Cortana

* Textuelle Antworten von Cortana werden in den meisten Fällen angezeigt
  (falls nicht, öffnen Sie das StartMenü und starten Sie die Suche erneut).

## Insider/Feedback Hub und TeamViewer Touch

* Nur Insider Hub (Feedback Hub in jährlichen Updates): Sofern Windows
  Insider benutzt wird, wird auch nur die Insider-Version verwendet.
* Beschriftungen für Auswahlschalter werden nun angesagt.
* TeamViewer Touch: Schalterbeschriftungen werden nun angesagt.

## Microsoft Edge

* Notifications such as file downloads are now announced.
* Note that overall support is experimental at this point (you should not
  use Edge as your primary browser for a while).

## Einstellungen

* Bestimmte Informationen wie der Fortschritt bei Windows Updates werden nun
  automatisch angesagt.
* Progress bar values and other information are no longer announced twice.

## Skype Preview

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat
  history.

## Bank of America/Twitter

* Schalterbeschriftungen werden nun angesagt.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
