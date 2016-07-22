# Windows 10 App Essentials #

* Auteur : Joseph Lee
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
* Calculatrice (modern).
* Cortana
* Insider Hub/Feedback Hub  (Windows Insiders seulement).
* Microsoft Edge
* Paramètres (paramètres système, Windows+I).
* Twitter.
* TeamViewer Touch.
* Divers modules pour des contrôles tels que les tuiles du Menu Démarrer.

## Générale

* Dans les menus contextuels pour les tuiles sous-menus du Menu Démarrer
  sont correctement reconnus.
* Quand on minimise les fenêtres (Windows+M), "volet" n'est plus annoncé
  (notable si on utilise les préversions Insider).
* Certaines boîtes de dialogue sont maintenant reconnues comme des boîtes de
  dialogue propres. Ceci incluent le dialogue Insider Preview (settings app)
  et le dialogue nouveau style UAC dans la build 14328 et versions
  ultérieur.
* L'annonce  du sélecteur de l'heure fonctionne dans des différente
  localizations de l'anglais.

## Alarmes et horloge

* Les valeurs du sélecteur de l'heure sont maintenant annoncées. Ceci
  affecte également le contrôle utilisé pour sélectionner lors de redémarrer
  pour terminer l'installation des mises à jour de Windows.

## Calculatrice

* Lorsque vous appuyez sur entrée, NVDA annonce les résultats du calcul.

## Cortana

* Les réponses textuelles de Cortana sont annoncées dans la plupart des
  situations (si ce n'est pas le cas, réouvrez le menu Démarrer et réessayez
  la recherche).

## Insider/Feedback Hub et TeamViewer Touch

* Insider Hub (Feedback Hub in Anniversary Update) seulement : Destiné à
  être utilisé par Windows Insiders en exécution d'une Insider build.
* Étiquettes pour les boutons radio sont annoncés.
* TeamViewer Touch: Étiquettes pour les boutons sont annoncés.

## Microsoft Edge

* Notifications telles que les téléchargements de fichiers sont maintenant
  annoncées.
* Notez que le support global est expérimental à ce point (vous ne devez pas
  utiliser Edge comme votre navigateur principal pendant un certain temps).

## Paramètres

* Certaines informations telles que l'avancement de la Mise à jour de
  Windows est maintenant signalé automatiquement.
* Les valeurs de la barre de progression ne sont plus annoncés deux fois.

## Bank of America/Twitter

* Étiquettes des boutons sont maintenant annoncées.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
