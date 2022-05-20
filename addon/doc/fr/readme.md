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
* Courrier
* Cartes
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* Bloc-notes (Windows 11)
* Personnes
* Paramètres (paramètres système, Windows+I)
* Accès vocal (Windows 11)
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
* Dans les versions de Windows 11 Insider Preview, l'état de la
  désactivation du microphone (Windows + Alt + K) est annoncé de partout.
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

## Courrier

* Lorsque vous examinez les éléments dans la liste des messages, vous pouvez
  maintenant utiliser les commandes de navigation dans les  tableaux pour
  examiner les en-têtes des messages. Notez que la navigation entre les
  lignes (messages) n'est pas prise en charge.

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
* In Insider Preview build 25115, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

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
* Sous Windows 10, NVDA interrompra la parole et signalera les mises à jour
  de l'état de Windows Update au fur et à mesure que le téléchargement et
  l'installation progressent. Cela peut entraîner une interruption de la
  parole lors de la navigation dans l'application Paramètres pendant le
  téléchargement et l'installation des mises à jour.

## Accès vocal

Cela fait référence à la fonctionnalité d'accès vocal introduite dans
l'aperçu de Windows 11 22H2.

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
