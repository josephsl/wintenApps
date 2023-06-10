# Windows App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et autres utilisateurs
* Télécharger [version stable][1]
* Télécharger [version béta][2]
* Télécharger [version de développement][3]
* Compatibilité NVDA: 2023.1 et ultérieure

Remarque : à l'origine appelé Windows 10 App Essentials, elle a été renommée
Windows App Essentials en 2021 pour prendre en charge Windows 10 et les
versions futures telles que Windows 11. Certaines parties de cette feront
toujours référence au nom de l'extension d'origine.

Cette extension est une collection d'app modules pour diverses apps de
Windows 10, ainsi que des améliorations et des correctifs pour certains
contrôles de Windows 10 et versions ultérieures.

Les app modules suivants ou la prise en charge des modules pour certaines
apps sont inclus (voir chaque section app pour plus de détails sur ce qui
est inclus) :

* Cortana
* Cartes
* Clavier moderne (panneau des emojis/clavier tactile/dictée/saisie
  vocale/suggestions de saisie matérielle/historique du
  presse-papiers/éditeurs de méthodes de saisie modernes)
* Paramètres (paramètres système, Windows+I)
* Accès vocal (Windows 11 22H2)
* Météo
* Divers modules pour des contrôles et des fonctionnalités tels que les
  annonces de bureau virtuels

Notes:

* Cette extension nécessite Windows 10 22H2 (build 19045), Windows 11 21H2
  (build 22000) ou version ultérieure.
* La durée du support de mise à jour des fonctionnalités est liée à la durée
  du support des consommateurs (Home, Pro, Pro Education, Pro for
  Workstations Editions) et l'extension peut mettre fin à la prise en charge
  d'une mise à jour des fonctionnalités avant la fin du support des
  consommateurs. Voir aka.ms/WindowsTargetVersioninfo pour plus
  d'informations et les dates de support.
* Bien que l'installation soit possible, cette extension ne prend pas en
  charge les versions Windows Enterprise LTSC (Long-Term Servicing Channel)
  et Windows Server.
* Si Add-on Updater est installé et que les mises à jour des extensions en
  arrière-plan sont activées, Windows App Essentials ne s'installera pas du
  tout sur les versions Windows non prises en charge.
* Toutes les fonctionnalités des builds Windows Insider Preview ne seront
  pas prises en charge, plus encore pour les fonctionnalités introduites
  dans Windows Insiders sous canary et dev channels.
* Le canal de développement de l'extension comprendra des modifications, y
  compris le contenu expérimental qui peut ou non être inclus dans les
  versions béta et stables, et le canal béta sera livré avec des
  modifications prévues pour les futures versions stables.
* Certaines fonctionnalités de l'extension font ou feront partie du lecteur
  d'écran NVDA.
* Pour une meilleure expérience avec les applications qui intègrent des
  technologies et du contenu Web tels que le menu Démarrer et son menu
  contextuel, activez le paramètre "Mode formulaire automatique lors des
  changements de focus" dans le panneau des paramètres du Mode navigation de
  NVDA.

Pour obtenir la liste des changements effectuées entre chaque version de
l'extension, reportez-vous au document [changelogs pour les versions de
l'extension][4].

## Générale

* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example). This is now
  part of NVDA 2023.2.
* Amélioration de l'expérience de la barre des tâches de Windows 10 et 11,
  notamment en annonçant les résultats de réorganisation des icônes lors de
  l'appui sur Alt+Shift+les touches flèche gauche / droite (Windows 11) et
  en rapportant la position de l'élément lors du déplacement des icônes de
  la barre des tâches  (Windows 10 et 11).
* Dans des aps  tels que File Explorer et Notepad  où les fenêtres à onglets
  sont prises en charge, NVDA annoncera le nom et la position des onglets
  lors de la commutation entre eux. Cela fait maintenant partie de NVDA
  2023.2.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations.

## Cartes

* NVDA n'interrompra plus la parole lorsqu'il est focalisé  sur des éléments
  autres que le contrôle de la carte dans certains cas.

## Clavier moderne

Cela inclut le panneau emoji, l'historique du presse-papiers, le clavier
tactile, la dictée/la saisie vocale, les suggestions d'entrée matérielle,
les actions suggérées et les éditeurs de méthodes de saisie modernes pour
certaines langues sur Windows 10 et 11. Lors de l'affichage des emojis, pour
une meilleure expérience, activez le paramètre Unicode Consortium à partir
des paramètres vocaux de NVDA et réglez le niveau de symbole sur "certains"
ou plus. Lors du collage à partir de l'historique du presse-papiers dans
Windows 10, appuyez sur la touche Espace au lieu de la touche Entrée pour
coller l'élément sélectionné.

* Sous Windows 11 22H2 et versions ultérieures, NVDA annoncera des actions
  suggérées lorsque des données compatibles telles que des numéros de
  téléphone sont copiées dans le presse-papiers.

## Paramètres

* NVDA annoncera le nom du contrôle de mise à jour facultative s'il est
  présent (lien télécharger et installer maintenant dans Windows 10, bouton
  de téléchargement dans Windows 11).
* Dans Windows 11, les éléments du fil d'Ariane des paramètres sont
  correctement reconnus.
* NVDA signalera les mises à jour de l'état de Windows Update au fur et à
  mesure que le téléchargement et l'installation progressent. Cela peut
  entraîner une interruption de la parole lors de la navigation dans
  l'application Paramètres pendant le téléchargement et l'installation des
  mises à jour. Si vous utilisez Windows 11 si l'enregistrement sélectif des
  événements UIA est activé ou défini sur sélectif, vous devez déplacer le
  focus sur la liste des mises à jour dès qu'elles apparaissent afin que
  NVDA puisse annoncer la progression de la mise à jour.

## Accès vocal

Il s'agit de la fonction d'accès vocal introduit dans Windows 11 22H2.

* NVDA annoncera l'état du microphone lors du basculement du microphone
  depuis l'interface d'accès vocal.

## Météo

* Les onglets tels que "prévisions" et "cartes" sont reconnus comme des
  onglets propres (patch par Derek Riemer).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
