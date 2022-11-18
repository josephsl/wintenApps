# Windows App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et autres utilisateurs
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* Compatibilité NVDA: 2022.2 et ultérieure

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
* Clavier moderne (panneau des emojis/dictée/saisie vocale/suggestions de
  saisie matérielle/historique du presse-papiers/éditeurs de méthodes de
  saisie modernes)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Accès vocal (Windows 11 22H2)
* Météo
* Miscellaneous modules for controls and features such as virtual desktops
  announcements

Notes:

* Cette extension nécessite Windows 10 21H2 (build 19044), Windows 11 21H2
  (build 22000) ou version ultérieure.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Bien que l'installation soit possible, cette extension ne prend pas en
  charge les versions Windows Enterprise LTSC (Long-Term Servicing Channel)
  et Windows Server.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in dev
  channel. For beta channel, only the latest build (22623) is supported.
* Certaines fonctionnalités de l'extension font ou feront partie du lecteur
  d'écran NVDA.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with the portable version
  of NVDA.
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
  grabbed, drop target effect. These events are now part of NVDA 2022.4.
* Lors de l'ouverture, de la fermeture ou du basculement entre les bureaux
  virtuels, NVDA annoncera le nom du bureau virtuel actif (bureau 2, par
  exemple).
* Lorsque vous réorganisez les entrées épinglées (mosaïques dans Windows 10)
  dans le menu Démarrer ou les actions rapides du Centre d'action avec Alt +
  Maj + touches fléchées, NVDA annoncera des effets de "glisser" et/ou de
  glisser-déposer avant et pendant le déplacement des éléments ,
  respectivement. Cela fait maintenant partie de NVDA 2022.4.
* Les annonces telles que les changements de volume/luminosité/coupure du
  microphone (Windows 11 22H2 et versions ultérieures) dans l'Explorateur de
  fichiers et les notifications de mise à jour d'application du Microsoft
  Store peuvent être supprimées en désactivant les notifications de rapport
  dans les paramètres de présentation des objets de NVDA.
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens. This is now part of NVDA 2023.1.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations.
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana via
  la voix.

## Cartes

* NVDA joue un bip du lieux pour les lieux sur la carte.

## Clavier moderne

Cela inclut le panneau emoji, l'historique du presse-papiers, la dictée/la
saisie vocale, les suggestions d'entrée matérielle, les actions suggérées et
les éditeurs de méthodes de saisie modernes pour certaines langues sur
Windows 10 et 11. Lors de l'affichage des emojis, pour une meilleure
expérience, activez le paramètre Unicode Consortium à partir des paramètres
vocaux de NVDA et réglez le niveau de symbole sur "certains" ou plus. Lors
du collage à partir de l'historique du presse-papiers dans Windows 10,
appuyez sur la touche Espace au lieu de la touche Entrée pour coller
l'élément sélectionné.

* Dans le panneau emoji de Windows 10, lorsqu'un groupe d'emoji (y compris
  le groupe kaomoji et symboles) est sélectionné, NVDA ne déplacera plus
  l'objet navigateur vers certains emojis.
* Dans l'historique du presse-papiers de Windows 11, le mode navigation sera
  désactivé par défaut, conçu pour permettre à NVDA d'annoncer les éléments
  du menu d'entrée de l'historique du presse-papiers.
* Sous Windows 11 22H2 Moment 1 et versions ultérieures, NVDA annoncera des
  actions suggérées lorsque des données compatibles telles que des numéros
  de téléphone sont copiées dans le presse-papiers.

## Personnes

* Lors de la recherche de contacts, la première suggestion sera annoncée.

## Paramètres

* NVDA annoncera le nom du contrôle de mise à jour facultative s'il est
  présent (lien télécharger et installer maintenant dans Windows 10, bouton
  de téléchargement dans Windows 11).
* Dans Windows 11, les éléments du fil d'Ariane des paramètres sont
  correctement reconnus.
* Sous Windows 10 et 11 22H2 et versions ultérieures, NVDA interrompra la
  parole et signalera les mises à jour de l'état de Windows Update au fur et
  à mesure que le téléchargement et l'installation progressent. Cela peut
  entraîner une interruption de la parole lors de la navigation dans
  l'application Paramètres pendant le téléchargement et l'installation des
  mises à jour. Si vous utilisez Windows 11 22H2 et versions ultérieures, si
  l'enregistrement sélectif des événements UIA est activé, vous devez
  déplacer le focus sur la liste des mises à jour dès qu'elles apparaissent
  afin que NVDA puisse annoncer la progression de la mise à jour.

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
