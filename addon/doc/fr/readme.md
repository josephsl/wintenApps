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
* Bank of America
* Calendrier
* Calculatrice (modern).
* Cortana
* Courrier
* Cartes
* Microsoft Edge
* Paramètres (paramètres système, Windows+I).
* Skype Preview
* Store
* Twitter.
* TeamViewer Touch.
* Météo.
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer.

Note: ce module complémentaire nécessite Windows 10 Version 1507 (build
10240) ou version ultérieure et NVDA 2016.3 ou version ultérieure. Pour de
meilleurs résultats, utilisez le module complémentaire avec la dernière
build stable (build 14393).

## Générale

* Dans les menus contextuels pour les tuiles sous-menus du Menu Démarrer
  sont correctement reconnus.
* Quand on minimise les fenêtres (Windows+M), "volet" n'est plus annoncé
  (notable si on utilise les préversions Insider).
* Certaines boîtes de dialogue sont maintenant reconnues comme des boîtes de
  dialogue propres. Ceci incluent le dialogue Insider Preview (settings app)
  et le dialogue nouveau style UAC dans la build 14328 et version ultérieur
  pour NVDA 2016.2.1 ou version antérieure.
* Apparence/fermeture des suggestions pour certains champs de recherche
  (notamment Settings app) est annoncé En passant par des sons et/ou le
  braille.
* Dans certains menus contextuels (comme dans Edge), les informations sur la
  position (par exemple 1 sur 2) n'est plus annoncé.
* Les événements UIA suivants sont reconnus : Controller pour, live region
  changed (handled par name change event).

## Alarmes et horloge

* Les valeurs du sélecteur de l'heure sont maintenant annoncées. Ceci
  affecte également le contrôle utilisé pour sélectionner lors de redémarrer
  pour terminer l'installation des mises à jour de Windows.

## Calendrier et Courrier

* NVDA n'annoncera plus "lecture seule" pour le sujet du rendez-vous dans le
  Calendrier et le contenu du message dans le Courrier.

## Calculatrice

* Lorsque vous appuyez sur entrée, NVDA annonce les résultats du calcul.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations (si ce n'est pas le cas, réouvrez le menu Démarrer et réessayez
  la recherche).
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana.
* NVDA annoncera maintenant un rappel de confirmation après que vous
  définissez une.

## Courrier et calendrier

* NVDA n'annoncera plus "edition" ou "lecture seule" dans le corps du
  message et d'autres  champs.

## Cartes

* NVDA joue un bip du lieux pour les lieux sur la carte.

## Microsoft Edge

* Notifications telles que les téléchargements de fichiers sont maintenant
  annoncées.
* Notez que le support global est expérimental à ce point (vous ne devez pas
  utiliser Edge comme votre navigateur principal pendant un certain temps).

## Paramètres

* Certaines informations telles que l'avancement de la Mise à jour de
  Windows est maintenant signalé automatiquement.
* Les valeurs de la barre de progression et d'autres informations ne sont
  plus annoncés deux fois.
* Si il faut du temps pour rechercher des paramètres, NVDA annoncera
  "recherch en cours" et l'état du résultat de la recherche tel comme si un
  paramètre est introuvable.

## Skype Preview

* L'indicateur de frappe de texte est annoncé exactement comme pour le Skype
  for Desktop client.
* Retour partiel de Contrôle+NVDA+commandes numéro de ligne pour lire
  l'historique de conversation récente et pour déplacer l'objet navigator
  aux entrées de conversation tout comme Skype for Desktop.
* Vous pouvez maintenant appuyer sur Alt+numéro de ligne pour localiser et
  se déplacer à la liste des contacts (1), conversations (2) et la zone
  d'édition de la conversation (3). Notez que l'on doit activer ces onglets
  pour passer à la partie souhaitée.

## Store

* Après vérification des mises à jour d'applications, le nom des
  applications dans la liste des applications à mettre à jour sera
  correctement étiqueté.

## TeamViewer Touch

* Étiquettes pour les boutons radio sont annoncés.
* Étiquettes pour les boutons sont annoncés.

## Bank of America/Twitter

* Étiquettes des boutons sont maintenant annoncées.

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

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
