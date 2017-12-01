# Windows 10 App Essentials #

* Autors: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version][1] herunterladen
* [Entwicklerversion][2] herunterladen

Diese Erweiterung ist ein Paket von App-Modulen für diverse Windows 10 Apps
sowie Korrekturen in einigen Windows 10 Steuerung.

Die folgenden App-Module oder unterstützte Module für einige Apps sind
inbegriffen (siehen Sie in jeden App-Bereich für Details, um zu sehen,
welche inbegriffen sind):

* Wecker und Uhr
* Kalender
* Rechner (modern)
* Cortana
* Spieleleiste
* Mail
* Karten
* Microsoft Edge
* Kontakte
* Einstellungen (Systemeinstellungen, Windows+I)
* Skype (universal app)
* Store
* Wetter
* Diverse Steuermodule wie beispielsweise die Startmenübereiche

Hinweis: Diese Erweiterung benötigt Windows 10 Version 1607 (Build 14393)
oder höher und NVDA 2017.3 oder höher. Um beste Ergebnisse zu erzielen,
verwenden Sie die Erweiterung mit dem neuesten stabilen Build von Windows 10
(Build 16299) und der neuesten stabilen Version von NVDA. Nachdem Sie die
Aktualisierungseinstellungen für die Erweiterung geändert haben, sollten Sie
auch die NVDA-Einstellungen speichern.

## Allgemein

* Im Kontextmenü von Kacheln werden untermenüs korrekt erkannt
* Bestimmte Dialoge werden nun als richtige Dialogfelder erkannt. Dazu
  gehören das Dialogfeld"Insider-Vorschau" (Einstellungsanwendung) und der
  neue UAC-Dialog in Build 14328 und höher für NvDA 2016.2 oder früher.
* NVDA kann die Anzahl der Vorschläge bei der Suche in den meisten Fällen
  bekannt geben. Diese Option wird gesteuert durch Meldung von
  Objektpositionsdaten im Dialog der Objektpräsentation.
* In bestimmten Kontextmenüs (z.B. in Edge) werden Positionsinformationen
  (z.B. 1 von 2) nicht mehr angesagt.
* Folgende UIA-Ereignisse werden erkannt: Controller für Live-Region Change,
  Systemalarm, Element ausgewählt, Fenster geöffnet. Wenn NVDA so
  eingestellt ist, dass es mit aktiviertem Debug-Logging läuft, werden diese
  Ereignisse verfolgt.
* Möglichkeit hinzugefügt, über den neuen Windows 10 App Essentials Dialog
  im NVDA-Einstellungsmenü nach Aktualisierungen für diese Erweiterung
  (automatisch oder manuell) zu suchen. Standardmäßig werden stabile- und
  Entwicklerversionen wöchentlich bzw. täglich automatisch nach neuen
  Updates suchen.
* Unterstützung für das schwebende Emoji-Eingabefeld in der Windowsversion
  1709 (Fall Creators Update). Für beste Erfahrungen beim Lesen von Emojis
  verwenden Sie Windows-OneCore-Sprachausgaben.
* Support for hardware keyboard input suggestions in build 17040 and later.
* In einigen Apps wird Live-Region-Text angekündigt. Dazu gehören Meldungen
  in Edge, Ergebnisse im Windowsrechner und andere. Beachten Sie, dass dies
  in manchen Fällen zu einer doppelten Aussprache führen kann, da die
  meisten Szenarien nun Bestandteil von NVDA ab 2017.3 sind.

## Wecker und Uhr

* Die Werte für den Zeitbalken werden nun angezeigt. Dies macht sich beim
  Verschieben des Fokus auf die Balkensteuerung bemerkbar. Es betrifft auch
  das Steuerelement fuer die Festlegung des Neustarts nach einer erfolgreich
  abgeschlossenen Aktualisierung.

## Rechner

* NVDA sagt die Rechenergebnisse beim Drücken der Eingabe- oder Escape-Taste
  an.
* Für Berechnungen wie im Einheitenumrechner und Währungsumrechner gibt NVDA
  die Ergebnisse bekannt, sobald die Berechnungen eingegeben wurden.

## Kalender

* NVDA verkündet nicht mehr "bearbeiten" oder"schreibgeschützt" im
  Nachrichtentext und in anderen Feldern.

## Cortana

* Textuelle Antworten von Cortana werden in den meisten Fällen angezeigt
  (falls nicht, öffnen Sie das StartMenü und starten Sie die Suche erneut).
* NVDA verstummt bei der Verwendung von Cortana, so dass die Stimmen nicht
  mehr sich in die Quere kommen.
* NVDA wird nun eine Erinnerungsbestätigung ankündigen, nachdem Sie eine
  eingestellt haben.

## Spieleleiste

* NVDA wird das Erscheinen des Fensters mit der Spieleleiste
  ankündigen. Aufgrund technischer Einschränkungen kann NVDA nicht
  vollständig mit der Spieleleiste interagieren.

## Mail

* Beim Navigieren durch Elemente in der Nachrichtenliste können Sie nun
  Tabellen-Navigationsbefehle verwenden, um Nachrichtenköpfe zu überprüfen.
* Wenn Sie eine Nachricht schreiben, wird das Erscheinen von Vorschlägen
  durch Töne angezeigt.

## Karten

* NVDA spielt einen Ortungston für Kartenstandorte ab.
* Wenn Sie die Straßenseitenansicht verwenden und die Option"Tastatur
  verwenden" aktiviert ist, wird NVDA Straßenadressen ankündigen, während
  Sie mit den Pfeiltasten durch die Karte navigieren.

## Microsoft Edge

* Benachrichtigungen wie Datei-Downloads und verschiedene
  Website-Benachrichtigungen werden nun angesagt. Die meisten dieser
  Szenarien sind nun Bestandteil von NVDA 2017.3.

## Kontakte

* Wenn nach Kontakten gesucht wird, ertönt bei Erfolg ein Signalton.

## Einstellungen

* Bestimmte Informationen, wie z.B. der Fortschritt von Windows Update,
  werden nun automatisch gemeldet. Die meisten Fälle sind standardmäßig in
  NVDA 2017.3 integriert.
* Werte in Fortschrittsbalken und andere Informationen werden nicht mehr
  zweimal angesagt.
* Wenn die Suche nach Einstellungen zu lange dauert, wird NVDA den Status
  der Suche und des Suchergebnisses ankündigen, z.B. wenn eine Einstellung
  nicht gefunden werden kann. Dies ist nun auch bestandteil von NVDA ab
  2017.3.
* Einstellungsgruppen werden erkannt, wenn Objektnavigation zur Navigation
  zwischen Controllern angewendet wird.
* Bei einigen Ausklapplisten wird NVDA nun die Beschriftung erkennen
  und/oder Wertänderungen ankündigen. Diese Funktion ist in NVDA ab 2017.3
  enthalten.
* Audio Volume progress bar beeps are no longer heard in build 17035 and
  later.

## Skype

* Die Eingabe des Indikatortextes wird wie bei Skype für Desktop-Client
  angekündigt.
* Teilweise Rückgabe von Control+NVDA+Zahlen aus der Zahlenreihe zum Lesen
  des letzten Chatverlaufs und zum Verschieben des Navigator-Objekts in
  Chat-Einträgen wie bei Skype für Desktop.
* Sie können nun die Alt+Zahlen aus der Zahlenreihe  drücken, um Gespräche
  (1), Kontaktliste (2), Bots (3) und Chat-Eingabefeld zu suchen und zu
  verschieben, falls sichtbar (4). Beachten Sie, dass diese Befehle
  ordnungsgemäß funktionieren, wenn das im März 2017 veröffentlichte
  Skype-Update installiert ist.
* Die Beschriftungen für Ausklapplisten für die Skype-Vorschau-App, welche
  in November 2016 veröffentlich wurde, werden angekündigt.
* NVDA wird in den meisten Fällen nicht mehr "Skype-Nachricht" ankündigen,
  wenn durch die Nachrichten navigiert wird.
* Verschiedene Probleme bei der Verwendung von Skype mit Braillezeilen
  wurden behoben, einschließlich der fehlenden Fähigkeit,
  Nachrichtenprotokolle in Braille-Schrift darzustellen.
* Wenn Sie in der Liste des Nachrichtenverlaufs auf einem Nachrichteneintrag
  NVDA+D drücken, kann NVDA nun detaillierte Informationen zu einer
  Nachricht wie z.B. Kanaltyp, Sendedatum, Uhrzeit usw. ankündigen.

## Store

* Nach der Suche nach App-Aktualisierungen werden die App-Namen in der Liste
  der zu aktualisierenden Apps korrekt beschriftet.
* Das Erscheinen von Suchvorschlägen wird nun angekündigt. Dies ist nun Teil
  von NVDA 2017.3.
* Beim Herunterladen von Inhalten wie Apps und Filmen wird NVDA den
  Produktnamen und den Fortschritt des Downloads bekannt geben. Ein
  grundlegender Fix ist jetzt Bestandteil von NVDA 2017.3.

## Wetter

* Registerkarten wie"Prognose" und"Karten" werden als richtige
  Registerkarten erkannt (Patch von Derek Riemer).
* Wenn Sie eine Prognose lesen, können Sie mit den Pfeiltasten nach links
  und rechts zwischen den Elementen wechseln. Verwenden Sie die Aufwärts-
  und Abwärtspfeile, um die einzelnen Teile eines Elements zu lesen. Zum
  Beispiel könnte ein Druck auf den Pfeil nach rechts den Bericht "Montag:
  33 Grad, teilweise bewölkt, ..." anzeigen. Wenn man den Pfeil nach unten
  drückt, heißt es"Montag", dann wird ein erneuter Druck auf den Pfeil den
  nächsten Punkt anzeigen (wie z.B. die Temperatur). Dies funktioniert
  derzeit für Tages- und Stundenvorhersagen.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
