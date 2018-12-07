# Windows 10 App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et d’autres utilisateurs de Windows 10
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Ce module complémentaire est une collection d'app modules pour diverses apps
de Windows 10, ainsi que des améliorations et des correctifs pour certains
contrôles de windows 10.

Les suivantes app modules ou la prise en charge des modules pour certaines
apps sont inclus (voir chaque section app pour plus de détails sur ce qui
est inclus) :

* Action center
* Alarmes et Horloge.
* Calendrier
* Calculatrice (modern).
* Cortana
* Hub de commentaires
* Game Bar
* Courrier
* Cartes
* Microsoft Edge
* Clavier moderne (panneau des emoji/suggestions de saisie
  matérielle/éléments de presse-papiers du cloud dans la Version 1709 et
  ultérieure)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Skype (universal app)
* Store
* Météo.
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer.

Notes:

* Ce module complémentaire nécessite Windows 10 Version 1709 (build 16299)
  ou version ultérieure et NVDA 2018.3 ou version ultérieure. Pour de
  meilleurs résultats, utilisez le module complémentaire avec la dernière
  version stable de Windows 10 (build 17763) et la dernière version stable
  de NVDA.
* Certaines fonctionnalités du module complémentaire font ou feront partie
  du lecteur d'écran NVDA.
* Pour les entrées non répertoriées ci-dessous, vous pouvez supposer que les
  fonctionnalités font partie de NVDA. Elles ne sont plus applicables car le
  module complémentaire ne prend pas en charge les anciennes versions de
  Windows 10 ou des modifications ont été apportées aux applications pour
  que les entrées ne soient plus applicables.

Pour obtenir la liste des changements effectuées entre chaque version du
module complémentaire, reportez-vous au document [changelogs pour les
versions du module complémentaire][3].

## Générale

* Changements internes afin de rendre le module complémentaire compatible
  avec les futures versions de NVDA.
* Si le  module complémentaire Add-on Updater est installé, ce module
  complémentaire vérifiera les mises à jour de Windows 10 App Essentials.
* L'intervalle de vérification de mise à jour par défaut a été remplacé par
  des vérifications hebdomadaires pour les versions stable et de
  développement. Ceci est applicable si le module complémentaire vérifie
  lui-même les mises à jour.
* Si le module complémentaire est configuré pour rechercher des mises à
  jour, lors de la mise à jour du module complémentaire, si la nouvelle
  version du module complémentaire nécessite une version plus récente de
  NVDA, un message d'erreur s'affiche.
* Petits changements dans la façon dont certains messages sont présentés
  dans des langues autres que l'anglais.
* Les éléments de sous-menu sont correctement reconnus dans diverses
  applications, y compris le menu contextuel pour les tuiles du Menu
  Démarrer et le menu de l'application de Microsoft Edge (Redstone 5).
* Certaines boîtes de dialogue sont maintenant reconnues comme des boîtes de
  dialogue propres et signalées comme telles, y compris le dialogue Insider
  Preview (settings app). Cela fait maintenant partie de NVDA 2018.3.
* NVDA peut annoncer le nombre de suggestions lors d'une recherche dans la
  majorité des cas. Cette option est contrôlée par "Annoncer le rang de
  l'objet dans une liste" dans la boîte de dialogue Présentation des
  Objets/panneau.
* Dans certains menus contextuels (comme dans Edge), les informations sur la
  position (par exemple 1 sur 2) n'est plus annoncé.
* Les événements UIA suivants sont reconnus : changement de position du
  texte actif, contrôleur pour, début de déplacement, annulation de
  déplacement, déplacement complet, élément sélectionné, état de l'élément,
  changement de région en direct, notification, alerte système, suggestion
  ouverte, fenêtre ouverte. Avec NVDA configuré pour être exécuté avec le
  journal activé en mode débogage ces événements seront suivis et pour
  l'événement de notification UIA, une tonalité de débogage sera entendue si
  les notifications proviennent d'un endroit autre que l'application
  actuellement active.
* Les notifications des versions plus récentes des applications sur Windows
  10 version 1709 (build 16299) et ultérieures sont annoncées. NVDA 2018.2
  et les versions ultérieures prennent cela en charge, avec 2018.3 ajoutant
  un support pour plus de notifications.
* Les suggestions pour Edge et pour les applications universelles sont
  reconnues et seront annoncées.
* Lors de l'ouverture, de la fermeture ou le basculement entre les bureaux
  virtuels, NVDA annonce l'ID de bureau actuel (bureau 2, par exemple).
* NVDA n'annoncera plus le texte de la taille du menu Démarrer lorsque vous
  changez la résolution ou l'orientation de l'écran.

## Action center

* L'action rapide de luminosité est maintenant un bouton au lieu d'un bouton
  à bascule.
* Divers changements d'état, tels que l'Assistance du Focus et la
  luminosité, seront signalés.

## Alarmes et horloge

* Les valeurs du sélecteur de l'heure sont maintenant annoncées, elles sont
  perceptibles lors du déplacement du focus vers les commandes du
  sélecteur. Ceci affecte également le contrôle utilisé pour sélectionner
  lors de redémarrer pour terminer l'installation des mises à jour de
  Windows.

## Calculatrice

* Lorsque vous appuyez sur Entrée ou Échap, NVDA annonce les résultats du
  calcul.
* Pour les calculs tels que le convertisseur d'unités et le convertisseur de
  devises, NVDA annoncera les résultats dès que les calculs seront entrés.
* NVDA n'annoncera plus le "titre niveau" pour les résultats de la
  calculatrice.

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

## Game Bar

* NVDA annoncera l'apparition de la fenêtre Game Bar. En raison de
  limitations techniques, NVDA ne peut pas interagir entièrement avec Game
  Bar antérieur à la build 17723.

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

## Microsoft Edge

* Les notifications telles que les téléchargements de fichiers et les
  différentes alertes de la page Web, ainsi que la disponibilité de Reading
  View (si vous utilisez la version 1709 et les versions ultérieures) sont
  annoncées.
* Le texte à saisie automatique sera suivi et annoncé dans l'adresse
  omnibar.

## Clavier moderne

Note: la plupart des fonctionnalités ci-dessous font maintenant partie de
NVDA 2018.3.

* Prise en charge pour les Emoji flottants du panneau de saisie dans la
  Version 1709 (Fall Creators Update) et ultérieure, y compris le panneau
  redessiné dans la version 1809  (build 17661 et ultérieure) et
  modifications apportées au 19H1 (build 18262). Pour une meilleure
  expérience lors de la lecture d'emojis,, utiliser le synthétiseur vocal
  Windows OneCore.
* Prise en charge des suggestions de saisie au clavier matériel dans la
  Version 1803 ((Mise à jour d'avril 2018) et ultérieure.
* Dans les builds postérieures à la 1709, NVDA annoncera le premier emoji
  sélectionné lors de l'ouverture du panneau emoji. Ceci est plus visible
  dans la build 18262 et ultérieures où le panneau emoji peut s'ouvrir
  jusqu'à la dernière catégorie consultée, tel que l'affichage du
  modificateur skin tone lorsqu'il est ouvert dans la catégorie People.
* Prise en charge de l'annonce des éléments du presse-papiers du cloud dans
  la version 1809 (build 17666 et ultérieure).
* Réduit la verbosité inutile lorsque vous travaillez avec le clavier
  moderne et ses fonctionnalités. Il ne s'agit plus d'annoncer "Microsoft
  Candidate UI" lors de l'ouverture des suggestions de saisie au clavier
  matériel et de rester silencieux lorsque certaines touches du clavier
  tactile déclenchent un événement de changement de nom sur certains
  systèmes.
* NVDA ne lira plus les tonalités d'erreur ou ne fera plus rien lors de la
  fermeture du panneau emoji dans les builds plus récentes de Insider
  Preview.
* NVDA annoncera les résultats de la recherche pour les emojis, si possible.

## Personnes

* Lors de la recherche de contacts, la première suggestion sera annoncée, en
  particulier si vous utilisez une version récente d'application.

## Paramètres

* Certaines informations telles que l'avancement de la Mise à jour de
  Windows est maintenant signalé automatiquement, y compris le widget
  Détection de stockage / nettoyage de disque.
* Les valeurs de la barre de progression et d'autres informations ne sont
  plus annoncés deux fois.
* Les groupes de paramètres sont reconnus lorsque vous utilisez la
  navigation par objet pour naviguer entre les commandes.
* Pour certaines zones de liste déroulantes et boutons radio, NVDA ne
  manquera plus de reconnaître les étiquettes et/ou d'annoncer les
  changements de valeur.
* Les bips de la barre de progression du volume audio ne sont plus audibles
  dans la Version 1803 et ultérieure.
* Plus de messages sur l'état de Windows Update sont annoncés, surtout si
  Windows Update rencontre des erreurs.
* NVDA ne semblera plus rien faire et ne jouera pas des tonalités d'erreur
  si des commandes pour la navigation par objet sont utilisées dans
  certaines circonstances.
* Divers liens ajoutés dans la build 18282 sans étiquettes ont maintenant
  des étiquettes.
* Le dialogue de rappel de Windows Update est reconnu comme un dialogue
  propre.

## Skype

Note: les entrées ci-dessous ne fonctionneront pas correctement dans Skype
14 universal app.

* L'indicateur de frappe de texte est annoncé exactement comme pour le Skype
  for Desktop client.
* Contrôle+NVDA+commandes numéro de ligne pour lire l'historique de
  conversation récente et pour déplacer l'objet navigator aux entrées de
  conversation tout comme Skype for Desktop, sont également disponibles dans
  Skype UWP.
* Vous pouvez maintenant appuyer sur Alt+numéro de ligne pour localiser et
  se déplacer à la conversations (1), liste des contacts (2), bots (3) et la
  zone d'édition de la conversation si visible (4). Notez que ces commandes
  fonctionneront correctement si la mise à jour de Skype publiée en mars
  2017 est installée.
* NVDA n'annoncera plus "Message Skype"lors de la révision des messages pour
  la majorité des cas.
* Dans la liste de l'historique des messages, appuyer sur NVDA+D sur un
  élément de message permettra à NVDA d'annoncer des informations détaillées
  sur un message tel que le type de canal, la date et l'heure d'envoi, etc.

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
