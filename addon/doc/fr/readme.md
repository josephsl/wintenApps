# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* NVDA compatibility: 2021.2 and beyond

Remarque : à l'origine appelé Windows 10 App Essentials, elle a été renommée
Windows App Essentials en 2021 pour prendre en charge Windows 10 et les
versions futures telles que Windows 11. Certaines parties de ce module
complémentaire feront toujours référence au nom du module complémentaire
d'origine.

Cette extension est une collection d'app modules pour diverses apps de
Windows 10, ainsi que des améliorations et des correctifs pour certains
contrôles de windows 10et versions ultérieures.

Les app modules suivants ou la prise en charge des modules pour certaines
apps sont inclus (voir chaque section app pour plus de détails sur ce qui
est inclus) :

* Calculatrice
* Cortana
* Courrier
* Cartes
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Météo
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer.

Notes:

* This add-on requires Windows 10 20H2 (build 19042) or later and is
  compatible with Windows 11.
* Bien que l'installation soit possible, cette extension ne prend pas en
  charge les versions Windows Enterprise LTSC (Long-Term Servicing Channel)
  et Windows Server.
* Certaines fonctionnalités de l'extension font ou feront partie du lecteur
  d'écran NVDA.
* Pour les entrées non répertoriées ci-dessous, vous pouvez supposer que les
  fonctionnalités font partie de NVDA, qu'elles ne sont plus applicables,
  car l'extension ne prend pas en charge les anciennes versions de Windows
  10 ou des modifications ont été apportées à Windows 10 et aux applications
  pour que les entrées ne soient plus applicables.
* Certaines Apps prennent en charge le mode de superposition compact
  (Toujours au-dessus pour la calculatrice par exemple), et ce mode ne
  fonctionne pas bien avec la version portable de NVDA. 

Pour obtenir la liste des changements effectuées entre chaque version de
l'extension, reportez-vous au document [changelogs pour les versions de
l'extension][3].

## Générale

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses. This
  is now part of NVDA 2021.3.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag complete, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  are tracked from an add-on called Event Tracker.
* Lors de l'ouverture, de la fermeture, de la réorganisation (Windows 11)
  ou du basculement entre les bureaux virtuels (build 21337 ou ultérieure),
  , NVDA annonce l'ID de bureau actuel (bureau 2, par exemple).
* NVDA n'annoncera plus la taille du menu Démarrer lorsque vous changez la
  résolution ou l'orientation de l'écran.
* Lorsque vous organisez les tuiles du menu Démarrer ou le Centre de
  notifications Actions rapides avec les touches Alt+Maj+touches fléchées,
  NVDA annoncera des informations sur les éléments glissés ou la nouvelle
  position de l'élément glissé.
* L'annonces tels que les changements de volume / luminosité dans
  l'Explorateur de fichiers et les notifications de mise à jour de
  l'application de Microsoft Store peuvent être supprimés en désactivant
  Annoncer les notifications dans les Paramètres de NVDA, Présentation des
  Objets.

## Calculatrice

* NVDA n'annoncera plus deux fois le message de l'écran de la calculatrice
  graphique.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations.
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana via
  la voix.

## Courrier

* Lorsque vous examinez les éléments dans la liste des messages, vous pouvez
  maintenant utiliser les commandes de navigation dans les  tableaux pour
  examiner les en-têtes des messages. Notez que la navigation entre les
  lignes (messages) n'est pas prise en charge.

## Cartes

* NVDA joue un bip du lieux pour les lieux sur la carte.
* Lorsque vous utilisez la vue latérale de la rue et que l'option "utiliser
  le clavier" est activée, NVDA annoncera les adresses des rues lorsque vous
  utilisez les touches fléchées pour naviguer dans la carte.

## Microsoft Solitaire Collection

* NVDA annoncera les noms des cartes et des jeux de cartes.

## Microsoft Store

* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Clavier moderne

Cela inclut le panneau d'emoji, l'historique du presse-papiers, la dictée/la
saisie vocale, les suggestions d'entrée matérielle et les éditeurs de
méthodes d'entrée modernes pour certaines langues. Lorsque vous affichez des
emojis, pour une expérience optimale, activez le paramètre Consortium
Unicode dans les paramètres vocaux de NVDA et définissez le niveau des
symboles sur "certains" ou plus. Lors du collage à partir de l'historique du
presse-papiers dans Windows 10, appuyez sur la touche Espace au lieu de la
touche Entrée pour coller l'élément sélectionné. NVDA prend également en
charge le panneau d'expérience de saisie mis à jour dans Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group)
  is selected, NVDA will no longer move navigator object to certain emojis.
* Ajout de la prise en charge du panneau d'expérience de saisie mis à jour
  (panneau emoji combiné et historique du presse-papiers) dans Windows 11.

## Personnes

* Lors de la recherche de contacts, la première suggestion sera annoncée, en
  particulier si vous utilisez une version récente d'application.

## Paramètres

* Certaines informations telles que l'avancement de la Mise à jour de
  Windows sont maintenant signalées automatiquement, y compris le widget
  Détection de stockage / nettoyage de disque.
* Les valeurs de la barre de progression et d'autres informations ne sont
  plus annoncés deux fois.
* Les étiquettes de contrôle étranges vues dans certaines installations
  Windows ont été corrigées.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.

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
