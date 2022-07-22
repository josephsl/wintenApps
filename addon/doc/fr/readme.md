# Windows App Essentials #

* Auteurs: Joseph Lee, Derek Riemer et autres utilisateurs
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* Compatibilité NVDA: 2021.3 et ultérieure

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

* Calculatrice
* Cortana
* Cartes
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* Bloc-notes (Windows 11)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Voice access (Windows 11 22H2)
* Météo
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer

Notes:

* Cette extension nécessite Windows 10 21H1 (build 19043), Windows 11 21H2
  (build 22000) ou version ultérieure.
* Bien que l'installation soit possible, cette extension ne prend pas en
  charge les versions Windows Enterprise LTSC (Long-Term Servicing Channel)
  et Windows Server.
* Toutes les fonctionnalités des builds Windows Insider Preview ne seront
  pas prises en charge.
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
* Pour une meilleure expérience avec les applications qui intègrent des
  technologies et du contenu Web tels que le menu Démarrer et son menu
  contextuel, activez le paramètre "Mode formulaire automatique lors des
  changements de focus" dans le panneau des paramètres du Mode navigation de
  NVDA.

Pour obtenir la liste des changements effectuées entre chaque version de
l'extension, reportez-vous au document [changelogs pour les versions de
l'extension][3].

## Générale

* En plus des gestionnaires d'événements UIA fournis par NVDA, les
  événements et propriétés UIA suivants sont reconnus : drag complete, drag
  drop effect, drop target dropped. Avec le niveau de journalisation de NVDA
  défini sur débogage, ces événements seront suivis et enregistrés.
* Lors de l'ouverture, de la fermeture, de la réorganisation (Windows 11)
  ou du basculement entre les bureaux virtuels (build 21337 ou ultérieure),
  , NVDA annonce l'ID de bureau actuel (bureau 2, par exemple).
* Lorsque vous organisez les éléments épinglées (tuiles dans Windows 10) du
  menu Démarrer ou des actions rapides du Centre de Notifications avec les
  touches Alt+Maj+touches fléchées, NVDA annoncera des informations sur les
  éléments déplacés ou la nouvelle position de l'élément déplacé.
* L'annonces tels que les changements de volume / luminosité dans
  l'Explorateur de fichiers et les notifications de mise à jour de
  l'application de Microsoft Store peuvent être supprimés en désactivant
  Annoncer les notifications dans les Paramètres de NVDA, Présentation des
  Objets.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* NVDA ne répétera plus la sortie de texte dans Windows Terminal 1.12.10733
  et versions ultérieures. Cela fait maintenant partie de NVDA 2022.1.
* NVDA annoncera à nouveau les détails des résultats de la recherche dans le
  menu Démarrer. Cela fait maintenant partie de NVDA 2022.2.
* In Windows 11, Taskbar items and other shell user interface elements can
  be detected properly when using mouse and/or touch interaction. This is
  now part of NVDA 2022.2.

## Calculatrice

* Dans Windows 10, les éléments de l'historique et de la liste de mémoire
  sont correctement étiquetés. Cela fait maintenant partie de NVDA 2022.1.
* NVDA annoncera le contenu de l'affichage de la calculatrice lors de
  l'exécution de commandes en mode scientifique telles que des opérations de
  trigonométrie. Cela fait maintenant partie de NVDA 2022.2.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations.
* NVDA sera silencieux quand vous vous adresserez vocalement à Cortana via
  la voix.

## Cartes

* NVDA joue un bip du lieux pour les lieux sur la carte.

## Microsoft Solitaire Collection

* NVDA annoncera les noms des cartes et des jeux de cartes.

## Clavier moderne

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions (preview), and modern input
method editors for certain languages across Windows 10 and 11. When viewing
emojis, for best experience, enable Unicode Consortium setting from NVDA's
speech settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* Dans Windows 10, lorsqu'un groupe d'emojis (y compris le groupe Kaomoji et
  symboles) est sélectionné, NVDA ne déplacera plus l'objet navigateur vers
  certains emojis.
* Dans Windows 11, il est à nouveau possible d'utiliser les touches fléchées
  pour parcourir les emojis lorsque le panneau emoji s'ouvre. Cela fait
  maintenant partie de NVDA 2022.1.
* Dans l'historique du presse-papiers de Windows 11, le mode navigation sera
  désactivé par défaut, conçu pour permettre à NVDA d'annoncer les éléments
  du menu d'entrée de l'historique du presse-papiers.
* In Insider Preview build 25115 and later (backported to Windows 11 beta
  build 22622), NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard.

## Bloc-notes

Ceci se rapporte à la version 11 ou ultérieure du Bloc-notes de Windows 11.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed. This is now part of NVDA 2022.2.

## Personnes

* Lors de la recherche de contacts, la première suggestion sera annoncée, en
  particulier si vous utilisez une version récente d'application.

## Paramètres

* Les étiquettes de contrôle étranges vues dans certaines installations
  Windows ont été corrigées.
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
