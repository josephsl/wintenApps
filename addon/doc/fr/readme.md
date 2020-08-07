# Windows 10 App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et d’autres utilisateurs de Windows 10
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* NVDA compatibility: 2020.1 to 2020.2

Cette extension est une collection d'app modules pour diverses apps de
Windows 10, ainsi que des améliorations et des correctifs pour certains
contrôles de windows 10.

Les app modules suivants ou la prise en charge des modules pour certaines
apps sont inclus (voir chaque section app pour plus de détails sur ce qui
est inclus) :

* Calculatrice (modern).
* Calendrier
* Cortana (Conversations)
* Courrier
* Cartes
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Météo.
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer.

Notes:

* This add-on requires Windows 10 Version 1909 (build 18363) or later. For
  best results, use the add-on with latest Windows 10 stable release (build
  19041).
* Certaines fonctionnalités de l'extension font ou feront partie du lecteur
  d'écran NVDA.
* Pour les entrées non répertoriées ci-dessous, vous pouvez supposer que les
  fonctionnalités font partie de NVDA, qu'elles ne sont plus applicables,
  car l'extension ne prend pas en charge les anciennes versions de Windows
  10 ou des modifications ont été apportées à Windows 10 et aux applications
  pour que les entrées ne soient plus applicables.

Pour obtenir la liste des changements effectuées entre chaque version de
l'extension, reportez-vous au document [changelogs pour les versions de
l'extension][3].

## Générale

* NVDA ne lira plus les sons d'erreur ou ne cesse plus de fonctionner si
  cette extension est utilisée sous Windows 7, windows 8.1 et des versions
  incompatibles de Windows 10.
* En plus des dialogues reconnus par NVDA, d'autres dialogues sont
  maintenant reconus et annoncés comme tels, incluant le dialogue de Insider
  Preview (app de paramètres).
* NVDA peut annoncer le nombre de suggestions lors d'une recherche dans la
  majorité des cas. Cette option est contrôlée par "Annoncer le rang de
  l'objet dans une liste" dans le dialogue Présentation des Objets.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app. Some events will provide
  additional information such as element count in controller for event,
  state of the element for state change event, and item text for item status
  event.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* NVDA will no longer appear to do nothing or play error tones if UIA
  Automation Id for an element could not be recorded when tracking events.
* Lors de l'ouverture, de la fermeture ou du basculement entre les bureaux
  virtuels, NVDA annonce l'ID de bureau actuel (bureau 2, par exemple).
* NVDA n'annoncera plus le texte de la taille du menu Démarrer lorsque vous
  changez la résolution ou l'orientation de l'écran.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.
* IN recent releases of Word 365, NVDA will no longer announce "delete back
  word" when pressing Control+Backspace.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.
* Open With dialog in Version 2004 (May 2020 Update) and later is announced
  when opened.

## Calculatrice

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* Pour les calculs tels que le convertisseur d'unités et le convertisseur de
  devises, NVDA annoncera les résultats dès que les calculs seront entrés.
* NVDA n'annoncera plus le "titre niveau" pour les résultats de la
  calculatrice.
* NVDA notifiera lorsque le nombre maximum de chiffres aura été atteint lors
  de la saisie d'expressions.
* Added support for always on mode in Calculator version 10.1908 and later.

## Calendrier

* NVDA n'annoncera plus "edition" ou "lecture seule" dans le corps du
  message et d'autres  champs.

## Cortana

Most items are no longer applicable on Version 1903 and later unless Cortana
Conversations (Version 2004 and later) is in use.

* Textual responses from Cortana are announced in most situations.
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana via
  la voix.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## Courrier

* Lorsque vous examinez les éléments dans la liste des messages, vous pouvez
  maintenant utiliser les commandes de navigation dans les  tableaux pour
  examiner les en-têtes des messages. Notez que la navigation entre les
  lignes (messages) n'est pas prise en charge.
* Lors de l'écriture d'un message, l'apparence des suggestions de mention
  est indiquée par des sons.

## Cartes

* NVDA joue un bip du lieux pour les lieux sur la carte.
* Lorsque vous utilisez la vue latérale de la rue et que l'option "utiliser
  le clavier" est activée, NVDA annoncera les adresses des rues lorsque vous
  utilisez les touches fléchées pour naviguer dans la carte.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Microsoft Store

* Après vérification des mises à jour des applications, le nom des
  applications dans la liste des applications à mettre à jour sera
  correctement étiqueté.
* Lors du téléchargement de contenus tels que des applications et des films,
  NVDA annoncera le nom du produit et la progression du téléchargement.

## Clavier moderne

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).
* When an emoji group (including kaomoji and symbols group in Version 1903
  or later) is selected, NVDA will no longer move navigator object to
  certain emojis.

## Personnes

* Lors de la recherche de contacts, la première suggestion sera annoncée, en
  particulier si vous utilisez une version récente d'application.

## Paramètres

* Certaines informations telles que l'avancement de la Mise à jour de
  Windows sont maintenant signalées automatiquement, y compris le widget
  Détection de stockage / nettoyage de disque.
* Les valeurs de la barre de progression et d'autres informations ne sont
  plus annoncés deux fois.
* Pour certaines zones de liste déroulantes et boutons radio, NVDA ne
  manquera plus de reconnaître les étiquettes et/ou d'annoncer les
  changements de valeur.
* NVDA ne semblera plus rien faire et ne jouera pas des tonalités d'erreur
  si des commandes pour la navigation par objet sont utilisées dans
  certaines circonstances.
* Le dialogue de rappel de Windows Update est reconnu comme un dialogue
  propre.
* Correction de quelques labels qui étaient incorrectes dans quelques cas
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## Météo

* Les onglets tels que "prévisions" et "cartes" sont reconnus comme des
  onglets propres (patch par Derek Riemer).
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
