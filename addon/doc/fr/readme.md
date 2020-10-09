# Windows 10 App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et d’autres utilisateurs de Windows 10
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* NVDA compatibility: 2020.1 to 2020.3

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
* cClavier moderne (panneau des emoji/dictée/suggestions de saisie
  matérielle/historique du presse-papiers du cloud/éditeurs de méthode de
  saisie moderne)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Météo.
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer.

Notes:

* Cette extension nécessite Windows 10 Version 1909 (build 18363) ou version
  ultérieur. Pour de meilleurs résultats, utilisez l'extension avec la
  dernière version stable de Windows 10 (build 19041).
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
* Lors de la recherche dans le menu Démarrer ou l'Explorateur de fichiers
  dans la version 1909 (November 2019 Update) et ultérieure, les instances
  de NVDA annonce des résultats de recherche deux fois lorsque les résultats
  en révision sont moins visibles, ce qui rend également la sortie braille
  plus cohérente lors de la révision des éléments.
* Les événements UIA suivants sont reconnus : contrôleur pour, début de
  déplacement, annulation de déplacement, déplacement complet, déplacement
  de la sible entrer, déplacement de la sible en direct, déplacement de la
  sible glissée, élément sélectionné, état de l'élément, changement de
  région en direct, notification, alerte système, suggestion ouverte,
  fenêtre ouverte. Avec NVDA configuré pour être exécuté avec le journal
  activé en mode débogage ces événements seront suivis et pour l'événement
  de notification UIA, une tonalité de débogage sera entendue si les
  notifications proviennent d'un endroit autre que l'application
  actuellement active. Certains événements fourniront des informations
  complémentaires telles que le nombre d'éléments dans le contrôleur pour
  l'événement, le changement de l'état de l'élément de l'événement et la
  position du texte de l'élément pour l'état de l'événement de l'élément.
* Il est possible de faire le suivi seul des événements spécifiques et / ou
  des événements à venir à partir des applications spécifiques.
* NVDA ne semblera plus rien faire et ne jouera pas des tonalités d'erreur
  si UIA Automation Id pour un élément ne pouvait être enregistré lors des
  suivi des événements.
* Lors de l'ouverture, de la fermeture ou du basculement entre les bureaux
  virtuels, NVDA annonce l'ID de bureau actuel (bureau 2, par exemple).
* NVDA will no longer announce Start menu size text when changing screen
  resolution or orientation.
* Lorsque vous organisez les tuiles du menu Démarrer ou le Centre de
  notifications Actions rapides avec les touches Alt+Maj+touches fléchées,
  NVDA annoncera des informations sur les éléments glissés ou la nouvelle
  position de l'élément glissé.
* Dans les versions récentes de Word 365,, NVDA n'annonce plus "delete back
  word" lorsque vous appuyez sur Contrôle+Retour arrière.
* L'annonces tels que les changements de volume / luminosité dans
  l'Explorateur de fichiers et les notifications de mise à jour de
  l'application de Microsoft Store peuvent être supprimés en désactivant
  Annoncer les notifications dans les Paramètres de NVDA, Présentation des
  Objets.
* Le dialogue Ouvrir avec dans la Version 2004 (May 2020 Update) et
  ultérieure est annoncée lorsqu'il est ouvert.

## Calculatrice

* Lorsque vous appuyez sur Entrée ou Échap, NVDA annonce les résultats du
  calcul.
* Pour les calculs tels que le convertisseur d'unités et le convertisseur de
  devises, NVDA annoncera les résultats dès que les calculs seront entrés.
* NVDA n'annoncera plus le "titre niveau" pour les résultats de la
  calculatrice.
* NVDA notifiera lorsque le nombre maximum de chiffres aura été atteint lors
  de la saisie d'expressions.
* Ajout du support pour toujours en mode Calculatrice Version 10.1908 et
  ultérieure.

## Calendrier

* NVDA n'annoncera plus "edition" ou "lecture seule" dans le corps du
  message et d'autres  champs.

## Cortana

La plupart des éléments ne sont plus applicables à la Version 1903 et
ultérieure à moins que Cortana Conversations (Version 2004 et ultérieure)
est en cours d'utilisation.

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations.
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana via
  la voix.
* Dans la Version 1909 (November 2019 Update) et ultérieure, l'expérience de
  recherche moderne dans l'Explorateur de fichiers alimenté par l'interface
  utilisateur Windows Search est pris en charge.

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

* NVDA annoncera les noms des cartes et des jeux de cartes.

## Microsoft Store

* Après vérification des mises à jour des applications, le nom des
  applications dans la liste des applications à mettre à jour sera
  correctement étiqueté.
* Lors du téléchargement de contenus tels que des applications et des films,
  NVDA annoncera le nom du produit et la progression du téléchargement.

## Clavier moderne

Cela comprend le panneau des emoji, historique du presse-papiers, dictée,
suggestions de saisie matérielle et éditeurs de méthode de saisie moderne
pour certaines langues. Lors de l'affichage des emoji, pour une meilleure
expérience, activer  le Consortium Unicode dans les Paramètres de NVDA,
Parole et configurer le Niveau de ponctuations et symboles  sur
"quelques-uns" ou la plupart.

* Lors de l'ouverture de l'historique du presse-papiers, NVDA n'annoncera
  "presse-papiers" quand il y a des éléments dans le presse-papiers dans
  certaines circonstances.
* Sur certains systèmes exécutant Windows Version 1903 (May 2019 Update) et
  ultérieure, NVDA ne paraîtra plus inactif quand le panneau d'emoji
  s'ouvre.
* Ajout du support pour le chinois moderne, japonais et coréen (CJK) IME
  candidates interface introduite dans la Version 2004 (build 18965 et
  ultérieure).
* Lorsqu'un groupe emoji (y compris Kaomoji et un groupe des symboles dans
  la Version 1903 ou ultérieure) est sélectionné, NVDA ne sera plus déplacer
  à l'objet navigateur vers certains emojis.
* NVDA will announce selected emoji if emoji panel is opened more than once
  in build 20226.

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
* Dans les révisions les plus récentes de la Version 1803 et ultérieure en
  raison de modifications apportées à la procédure Windows Update pour les
  mises à jour de fonctionnalités, un lien "télécharger et installer
  maintenant" a été ajouté. NVDA annonce maintenant le titre de la nouvelle
  mise à jour si elle est présente.

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
