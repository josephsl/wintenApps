# Windows App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et autres utilisateurs

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

* Clavier moderne
* Paramètres (Windows+I)

Notes:

* Cette extension nécessite Windows 10 22H2 64 bits (build 19045), 11 22H2
  (build 22621), ou des versions ultérieures.
* La durée du support de mise à jour des fonctionnalités est liée à la durée
  du support des consommateurs (Home, Pro, Pro Education, Pro for
  Workstations Editions) et l'extension peut mettre fin à la prise en charge
  d'une mise à jour des fonctionnalités avant la fin du support des
  consommateurs. Voir <https://aka.ms/WindowsTargetVersioninfo> pour plus
  d'informations et les dates de support.
* Bien que l'installation soit possible, cette extension ne prend pas en
  charge les versions Windows Enterprise LTSC (Long-Term Servicing Channel)
  et Windows Server.
* Toutes les fonctionnalités des builds Windows Insider Preview ne seront
  pas prises en charge, plus encore pour les fonctionnalités introduites
  dans Windows Insiders sous canary et dev channels.
* L'extension peut émuler les modifications incluses dans les builds Insider
  Preview qui sont ensuite supprimées, et pour ces modifications,
  l'extension peut les supprimer dans des versions futures.
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
l'extension][1].

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

* Sous Windows 11, NVDA annoncera des actions suggérées lorsque des données
  compatibles telles que des numéros de téléphone sont copiées dans le
  presse-papiers. Cela fait désormais partie de NVDA 2024.2.

## Paramètres (Windows+I)

* NVDA signalera les mises à jour de l'état de Windows Update au fur et à
  mesure que le téléchargement et l'installation progressent. Sous Windows
  10, cela peut entraîner une interruption de la parole lors de la
  navigation dans l'application Paramètres pendant le téléchargement et
  l'installation des mises à jour. Sous Windows 11, la navigation par objets
  peut être utilisée dans la liste des mises à jour pour vérifier l'état de
  mise à jour des entrées individuelles.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
