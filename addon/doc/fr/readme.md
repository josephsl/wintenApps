# Windows App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et autres utilisateurs
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* NVDA compatibility: 2022.2 and later

Remarque : à l'origine appelé Windows 10 App Essentials, elle a été renommée
Windows App Essentials en 2021 pour prendre en charge Windows 10 et les
versions futures telles que Windows 11. Certaines parties de ce module
complémentaire feront toujours référence au nom du module complémentaire
d'origine.

Cette extension est une collection d'app modules pour diverses apps de
Windows 10, ainsi que des améliorations et des correctifs pour certains
contrôles de Windows 10 et versions ultérieures.

Les app modules suivants ou la prise en charge des modules pour certaines
apps sont inclus (voir chaque section app pour plus de détails sur ce qui
est inclus) :

* Cortana
* Cartes
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions/modern input method
  editors)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Voice access (Windows 11 22H2)
* Météo
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer

Notes:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Bien que l'installation soit possible, cette extension ne prend pas en
  charge les versions Windows Enterprise LTSC (Long-Term Servicing Channel)
  et Windows Server.
* If Add-on Updater 22.08 or later is installed and background add-on
  updates is enabled, Windows App Essentials will not install at all on
  unsupported Windows releases.
* Toutes les fonctionnalités des builds Windows Insider Preview ne seront
  pas prises en charge.
* Certaines fonctionnalités de l'extension font ou feront partie du lecteur
  d'écran NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows, apps, and NVDA that makes entries no longer applicable.
* Certaines Apps prennent en charge le mode de superposition compact
  (Toujours au-dessus pour la calculatrice par exemple), et ce mode ne
  fonctionne pas bien avec la version portable de NVDA.
* Pour une meilleure expérience avec les applications qui intègrent des
  technologies et du contenu Web tels que le menu Démarrer et son menu
  contextuel, activez le paramètre "Mode formulaire automatique lors des
  changements de focus" dans le panneau des paramètres du Mode navigation de
  NVDA.

Pour obtenir la liste des changements effectuées entre chaque version de
l'extension, reportez-vous au document [changelogs pour les versions de
l'extension][3].

## Générale

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example).
* When dragging and dropping items such as arranging pinned entries (tiles
  in Windows 10) in Start menu or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce "dragging" and/or drag and drop
  effects before and while dragging items, respectively. This is now part of
  NVDA 2022.4.
* Announcements such as volume/brightness/microphone mute (Windows 11 22H2
  and later) changes in File Explorer and app update notifications from
  Microsoft Store can be suppressed by turning off Report Notifications in
  NVDA's object presentation settings.
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations.
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana via
  la voix.

## Cartes

* NVDA joue un bip du lieux pour les lieux sur la carte.

## Clavier moderne

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions, and modern input method
editors for certain languages across Windows 10 and 11. When viewing emojis,
for best experience, enable Unicode Consortium setting from NVDA's speech
settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* In Windows 10 emoji panel, when an emoji group (including kaomoji and
  symbols group) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Dans l'historique du presse-papiers de Windows 11, le mode navigation sera
  désactivé par défaut, conçu pour permettre à NVDA d'annoncer les éléments
  du menu d'entrée de l'historique du presse-papiers.
* In Windows 11 22H2 Moment 1 and later, NVDA will announce suggested
  actions when compatible data such as phone numbers is copied to the
  clipboard.

## Personnes

* When searching for contacts, first suggestion will be announced.

## Paramètres

* NVDA annoncera le nom du contrôle de mise à jour facultative s'il est
  présent (lien télécharger et installer maintenant dans Windows 10, bouton
  de téléchargement dans Windows 11).
* Dans Windows 11, les éléments du fil d'Ariane des paramètres sont
  correctement reconnus.
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report
  updates to Windows Update status as download and install progresses. This
  may result in speech interruption when navigating Settings app while
  updates are being downloaded and installed. If using Windows 11 22H2 and
  later, if selective UIA event registration is on, you must move focus to
  updates list as soon as they appear so NVDA can announce update progress.

## Accès vocal

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA annoncera l'état du microphone lors du basculement du microphone
  depuis l'interface d'accès vocal.

## Météo

* Les onglets tels que "prévisions" et "cartes" sont reconnus comme des
  onglets propres (patch par Derek Riemer).
* Lorsque vous lisez une prévision, utilisez les flèches gauche et droite
  pour vous déplacer entre les éléments. Utilisez les flèches haut et bas
  pour lire les éléments individuels. Par exemple, en appuyant sur la flèche
  droite peut annoncer "Lundi: 79 degrés, partiellement nuageux, ..." en
  appuyant sur la flèche bas il va dire "Lundi" Puis en appuyant à nouveau
  sur celle-ci il va lire l'élément suivant (Comme la température). Ceci
  fonctionne actuellement pour les prévisions quotidienne,  et toutes les
  heures.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
