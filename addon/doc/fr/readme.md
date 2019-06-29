# Windows 10 App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et d’autres utilisateurs de Windows 10
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* NVDA compatibility: 2018.4 to 2019.2

Cette extension est une collection d'app modules pour diverses apps de
Windows 10, ainsi que des améliorations et des correctifs pour certains
contrôles de windows 10.

Les app modules suivants ou la prise en charge des modules pour certaines
apps sont inclus (voir chaque section app pour plus de détails sur ce qui
est inclus) :

* Action center
* Alarmes et Horloge.
* Calculatrice (modern).
* Calendrier
* Cortana
* Hub de commentaires
* Courrier
* Cartes
* Microsoft Edge
* Clavier moderne (panneau des emoji/suggestions de saisie
  matérielle/éléments de presse-papiers du cloud dans la Version 1709 et
  ultérieures)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Store
* Météo.
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer.

Notes:

* Cette extension nécessite Windows 10 Version 1803 (build 17134) ou version
  ultérieure et NVDA 2018.4 ou version ultérieure. Pour de meilleurs
  résultats, utilisez l'extension avec la dernière version stable de Windows
  10 (build 18362) et la dernière version stable de NVDA.
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
* Les éléments de sous-menu sont correctement reconnus dans diverses
  applications, y compris le menu contextuel pour les tuiles du Menu
  Démarrer et le menu de l'application de Microsoft Edge (Redstone 5).
* En plus des dialogues reconnus par NVDA, d'autres dialogues sont
  maintenant reconus et annoncés comme tels, incluant le dialogue de Insider
  Preview (app de paramètres).
* NVDA peut annoncer le nombre de suggestions lors d'une recherche dans la
  majorité des cas. Cette option est contrôlée par "Annoncer le rang de
  l'objet dans une liste" dans le dialogue Présentation des Objets.
* Dans certains menus contextuels (comme dans Edge), les informations sur la
  position (par exemple 1 sur 2) n'est plus annoncé.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* Les suggestions pour Edge et pour les applications universelles sont
  reconnues et seront annoncées.
* Lors de l'ouverture, de la fermeture ou du basculement entre les bureaux
  virtuels, NVDA annonce l'ID de bureau actuel (bureau 2, par exemple).
* NVDA n'annoncera plus le texte de la taille du menu Démarrer lorsque vous
  changez la résolution ou l'orientation de l'écran.
* In Version 1903 (May 2019 Update), NVDA will announce volume and
  brightness changes immediately if focused on File Explorer. This is now
  part of NVDA 2019.2.

## Action center

* L'action rapide de luminosité est maintenant un bouton au lieu d'un bouton
  à bascule. Cela est intégré nativement à partir de NVDA 2019.1.
* Divers changements d'état, tels que l'Assistance du Focus et la
  luminosité, sont signalés. Cela est intégré nativement à partir de NVDA
  2019.1

## Alarmes et horloge

* Les valeurs du sélecteur de l'heure sont maintenant annoncées, elles sont
  perceptibles lors du déplacement du focus vers les commandes du
  sélecteur. Ceci affecte également le contrôle utilisé pour sélectionner le
  moment du redémarrage pour terminer l'installation des mises à jour de
  Windows. Cela est intégré nativement à partir de NVDA 2019.1

## Calculatrice

* Lorsque vous appuyez sur Entrée ou Échap, NVDA annonce les résultats du
  calcul.
* Pour les calculs tels que le convertisseur d'unités et le convertisseur de
  devises, NVDA annoncera les résultats dès que les calculs seront entrés.
* NVDA n'annoncera plus le "titre niveau" pour les résultats de la
  calculatrice.
* NVDA notifiera lorsque le nombre maximum de chiffres aura été atteint lors
  de la saisie d'expressions.

## calendrier

* NVDA n'annoncera plus "edition" ou "lecture seule" dans le corps du
  message et d'autres  champs.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations (si ce n'est pas le cas, réouvrez le menu Démarrer et réessayez
  la recherche).
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana via
  la voix.
* NVDA annoncera maintenant un rappel de confirmation après que vous
  définissez une.

## Hub de commentaires

* Pour les nouvelles versions des applications, NVDA n'annonce plus deux
  fois les catégories de commentaires.

## Courrier

* Lorsque vous examinez les éléments dans la liste des messages, vous pouvez
  maintenant utiliser les commandes de navigation dans les  tableaux pour
  examiner les en-têtes des messages. Notez que la navigation entre les
  lignes (messages) n'est pas prise en charge.
* Lors de l'écriture d'un message, l'apparence des suggestions de mention
  est indiquée par des sons.
* NVDA ne produira plus de tonalités d'erreur ou ne cessera plus de
  fonctionner à la fermeture de cette application. Cela est intégré
  nativement à partir de NVDA 2019.1.

## Cartes

* NVDA joue un bip du lieux pour les lieux sur la carte.
* Lorsque vous utilisez la vue latérale de la rue et que l'option "utiliser
  le clavier" est activée, NVDA annoncera les adresses des rues lorsque vous
  utilisez les touches fléchées pour naviguer dans la carte.

## Microsoft Edge

* Le texte à saisie automatique sera suivi et annoncé dans l'adresse
  omnibar.
* NVDA ne jouera plus un son de suggestion lorsque vous appuyez sur F11 pour
  basculer en plein écran.

## Clavier moderne

Note: la plupart des fonctionnalités ci-dessous font maintenant partie de
NVDA 2018.3 et ultérieurs.

* Prise en charge pour les Emoji flottants du panneau de saisie dans la
  Version 1709 (Fall Creators Update) et ultérieure, y compris le panneau
  redessiné dans la version 1809  (build 17661 et ultérieure) et
  modifications apportées au 19H1 (build 18262, y compris les catégories
  kaomoji et symboles dans la build 18305). Si vous utilisez des versions de
  NVDA antérieures à 2018.4, pour une meilleure expérience lors de la
  lecture d'emojis,, utiliser le synthétiseur vocal Windows OneCore. Si vous
  utilisez 2018.4 ou une version ultérieure, activez le paramètre Consortium
  Unicode à partir des Paramètres Parole de NVDA et définissez le niveau de
  ponctuations et symboles sur "quelques-uns" ou plus.
* Prise en charge des suggestions de saisie au clavier matériel dans la
  Version 1803 ((Mise à jour d'avril 2018) et ultérieure.
* Dans les builds postérieures à la 1709, NVDA annoncera le premier emoji
  sélectionné lors de l'ouverture du panneau emoji. Ceci est plus visible
  dans la build 18262 et ultérieures où le panneau emoji peut s'ouvrir
  jusqu'à la dernière catégorie consultée, tel que l'affichage du
  modificateur skin tone lorsqu'il est ouvert dans la catégorie Personnes.
* Prise en charge de l'annonce des éléments du presse-papiers du cloud dans
  la version 1809 (build 17666 et ultérieure).
* Réduit la verbosité inutile lorsque vous travaillez avec le clavier
  moderne et ses fonctionnalités. Il ne s'agit plus d'annoncer "Microsoft
  Candidate UI" lors de l'ouverture des suggestions de saisie au clavier
  matériel et de rester silencieux lorsque certaines touches du clavier
  tactile déclenchent un événement de changement de nom sur certains
  systèmes.
* NVDA ne produira plus de tonalités d'erreur ou autre à la fermeture du
  panneau d'emoji dans les builds les plus récentes de 19H1 Insider
  Preview. Ceci fera partie de NVDA 2019.1.
* Dans la version 1809 (mise à jour d'octobre 2018) et ultérieures, NVDA
  annoncera les résultats de la recherche pour les emojis, si possible.
  Ceci fera partie de NVDA 2019.1.
* NVDA n'annoncera pous "presse-papiers" quand il y a des éléments dans le
  presse-papiers dans certaines circonstances.
* Sur certains systèmes exécutant Windows Version 1903 (May 2019 Update),
  NVDA ne paraîtra plus inactif quand le panneau d'emoji s'ouvre.

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
* Les bips de la barre de progression du volume audio ne sont plus audibles
  dans la Version 1803 et ultérieure.
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

## Store

* Après vérification des mises à jour des applications, le nom des
  applications dans la liste des applications à mettre à jour sera
  correctement étiqueté.
* Lors du téléchargement de contenus tels que des applications et des films,
  NVDA annoncera le nom du produit et la progression du téléchargement.

## Météo

* Les onglets tels que "prévisions" et "cartes" sont reconnus comme des
  onglets propres (patch par Derek Riemer).
* Lorsque vous lisez une prévision, utilisez les flèches gauche et droite
  pour vous déplacer entre les éléments. Utilisez les flèches haut et bas
  pour lire les éléments individuels. Par exemple, en appuyant sur la flèche
  droite peut annoncer "Lundi: 79 degrés, partiellement nuageux, ..." en
  appuyant sur la flèche bas il va dire "Lundi" Puis en appuyant à nouveau
  sur celle-ci il va lire l'élément suivant (Comme la température). Ceci
  travaille actuellement pour les prévisions quotidiennes et toutes les
  heures.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
