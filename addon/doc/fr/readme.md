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
  dans un sous-ensemble de Windows Insiders.

Pour obtenir la liste des changements effectuées entre chaque version de
l'extension, reportez-vous au document [changelogs pour les versions de
l'extension][1].

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
