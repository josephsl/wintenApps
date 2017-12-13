# Windows 10 App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et d’autres utilisateurs de Windows 10
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Ce module complémentaire est une collection d'app modules pour diverses apps
de Windows 10, ainsi que des correctifs pour certains contrôles de windows
10.

Les suivantes app modules ou la prise en charge des modules pour certaines
apps sont inclus (voir chaque section app pour plus de détails sur ce qui
est inclus) :

* Alarmes et Horloge.
* Calendrier
* Calculatrice (modern).
* Cortana
* Game Bar
* Courrier
* Cartes
* Microsoft Edge
* Personnes
* Paramètres (paramètres système, Windows+I)
* Skype (universal app)
* Store
* Météo.
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer.

Note: ce module complémentaire nécessite Windows 10 Version 1607 (build
14393) ou version ultérieure et NVDA 2017.3 ou version ultérieure. Pour de
meilleurs résultats, utilisez le module complémentaire avec la dernière
build stable (build 16299) et la dernière version stable de NVDA. De plus,
après avoir modifié les paramètres de mise à jour pour le module
complémentaire, n'oubliez pas de sauvegarder la configuration de NVDA.

## Générale

* Dans les menus contextuels pour les tuiles sous-menus du Menu Démarrer
  sont correctement reconnus.
* Certaines boîtes de dialogue sont maintenant reconnues comme des boîtes de
  dialogue propres. Ceci incluent le dialogue Insider Preview (settings app)
  et le dialogue nouveau style UAC dans la build 14328 et version ultérieur
  pour NVDA 2016.2.1 ou version antérieure.
* NVDA peut annoncer le nombre de suggestions lors d'une recherche dans la
  majorité des cas. Cette option est contrôlée par "Annoncer le rang de
  l'objet dans une liste" dans la boîte de dialogue Présentation des Objets.
* Dans certains menus contextuels (comme dans Edge), les informations sur la
  position (par exemple 1 sur 2) n'est plus annoncé.
* Les événements UIA suivants sont reconnus : Contrôleur pour changement de
  région en direct, alerte système, élément sélectionné, fenêtre
  ouverte. Avec NVDA configuré pour être exécuté avec le journal activé en
  mode débogage ces événements seront suivis.
* Ajout de la possibilité de vérifier les mises à jour du module
  complémentaire(automatiques ou manuelles) via la nouvelle boîte de
  dialogue Windows 10 App Essentials qui se trouve dans le menu Préférences
  de NVDA. Par défaut, les versions stables et de développement vérifieront
  automatiquement les nouvelles mises à jour sur une base hebdomadaire ou
  quotidienne, respectivement.
* Prise en charge pour les Emoji flottants du panneau de saisie dans la
  Version 1709 (Fall Creators Update). Pour une meilleure expérience lors de
  la lecture d'emojis,, utiliser le synthétiseur vocal Windows OneCore.
* Prise en charge des suggestions de saisie au clavier matériel dans la
  build 17040 et ultérieure.
* Dans certaines applications, le texte de la région en direct est
  annoncé. Cela inclut les alertes dans Edge, résultats dans la calculatrice
  et autres. Notez que cela peut entraîner une double verbalisation dans
  certains cas. La plupart des scénarios font maintenant partie de NVDA
  2017.3.

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

## calendrier

* NVDA n'annoncera plus "edition" ou "lecture seule" dans le corps du
  message et d'autres  champs.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations (si ce n'est pas le cas, réouvrez le menu Démarrer et réessayez
  la recherche).
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana.
* NVDA annoncera maintenant un rappel de confirmation après que vous
  définissez une.

## Game Bar

* NVDA annoncera l'apparition de la fenêtre Game Bar. En raison de
  limitations techniques, NVDA ne peut pas interagir entièrement avec Game
  Bar.

## Courrier

* Lorsque vous examinez les éléments dans la liste des messages, vous pouvez
  maintenant utiliser les commandes de navigation de tableau pour examiner
  les en-têtes des messages.
* Lors de l'écriture d'un message, l'apparence des suggestions de mention
  est indiquée par des sons.

## Cartes

* NVDA joue un bip du lieux pour les lieux sur la carte.
* Lorsque vous utilisez la vue latérale de la rue et que l'option "utiliser
  le clavier" est activée, NVDA annoncera les adresses des rues lorsque vous
  utilisez les touches fléchées pour naviguer dans la carte.

## Microsoft Edge

* Notifications telles que les téléchargements de fichiers et les
  différentes alertes de la page Web sont maintenant annoncées. La plupart
  de ces scénarios font maintenant partie de NVDA 2017.3.

## Personnes

* Lors de la recherche de contacts, un son sera joué s'il existe des
  résultats de recherche.

## Paramètres

* Certaines informations telles que l'avancement de la Mise à jour de
  Windows est maintenant signalé automatiquement. NVDA elle-même traitera la
  majorité des cas dans la 2017.3.
* Les valeurs de la barre de progression et d'autres informations ne sont
  plus annoncés deux fois.
* Si il faut du temps pour rechercher des paramètres, NVDA annoncera
  "recherch en cours" et l'état du résultat de la recherche tel comme si un
  paramètre est introuvable. Ceci est maintenant fait à partir de NVDA dans
  la 2017.3.
* Les groupes de paramètres sont reconnus lorsque vous utilisez la
  navigation par objet pour naviguer entre les commandes.
* Pour certaines zones de liste déroulantes, NVDA ne manquera plus de
  reconnaître les étiquettes et/ou d'annoncer les changements de
  valeur. Correction de changement de valeur est inclus dans NVDA 2017.3.
* Les bips de la barre de progression du volume audio ne sont plus audibles
  dans la build 17035 et ultérieure.

## Skype

* L'indicateur de frappe de texte est annoncé exactement comme pour le Skype
  for Desktop client.
* Retour partiel de Contrôle+NVDA+commandes numéro de ligne pour lire
  l'historique de conversation récente et pour déplacer l'objet navigator
  aux entrées de conversation tout comme Skype for Desktop.
* Vous pouvez maintenant appuyer sur Alt+numéro de ligne pour localiser et
  se déplacer à la conversations (1), liste des contacts (2), bots (3) et la
  zone d'édition de la conversation si visible (4). Notez que ces commandes
  fonctionneront correctement si la mise à jour de Skype mise à jour en mars
  2017 est installée.
* Étiquettes de liste déroulante pour Skype preview app publié en Novembre
  2016 sont annoncées.
* NVDA n'annoncera plus "Message Skype"lors de la révision des messages pour
  la majorité des cas.
* Différents problèmes lors de l'utilisation de Skype avec des terminaux
  braille ont été corrigés, y compris l'impossibilité de réviser les
  éléments de l'historique des messages en braille.
* Dans la liste d'historique des messages, appuyer sur NVDA+D sur un élément
  de message permettra à NVDA d'annoncer des informations détaillées sur un
  message tel que le type de canal, la date et l'heure envoyées, etc.

## Store

* Après vérification des mises à jour d'applications, le nom des
  applications dans la liste des applications à mettre à jour sera
  correctement étiqueté.
* L'apparition des suggestions de recherche est maintenant annoncée. Cela
  fait maintenant partie de NVDA 2017.3.
* Lors du téléchargement de contenus tels que des applications et des films,
  NVDA annoncera le nom du produit et la progression du téléchargement. Une
  solution de base fait désormais partie de NVDA 2017.3.

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
