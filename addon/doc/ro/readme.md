# Windows 10 Aplicații Esențiale #

* Autori: Joseph Lee, Derek Riemer și alți utilizatori Windows 10 
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

Acest add-on cuprinde o colecție de module pentru diverse aplicații din
Windows 10 și soluții pentru anumite comenzi din Windows 10.

Următoarele module de aplicații sau module de suport pentru unele aplicații
sunt incluse (verificați fiecare secțiune a aplicației pentru detalii cu
privire la ceea ce este inclus):

* Alarme și ceas.
* Banca Americii
* Calendar
* Calculator (modern).
* Cortana
* Poștă electronică
* Hărți
* Microsoft Edge
* Setări (setări sistem, Windows+I).
* Skype Preview
* Magazin
* Twitter.
* TeamViewer Touch.
* Meteo.
* Diverse module de control precum tile-urile din meniul start.

Notă: acest add-on necesită Windows 10 versiunea 1507 (build 10240) sau mai
nou și NVDA 2016.3 sau mai nou.

## General

* În meniurile contextuale ale tile-urilor din cadrul Start Meniu,
  submeniurile sunt recunoscute corect.
* La minimizarea ferestrelor (Windows+M), „panou” nu mai este anunțat (de
  remarcat pentru utilizatorii build-urilor din cadrul programului de
  insider).
* Anumite dialoguri sunt acum recunoscute ca dialoguri
  corespunzătoare. Aceasta include dialogul de examinare al insiderului (în
  aplicația Setări) și un nou stil în dialogul UAC în build 14328 și mai nou
  pentru NvDA 2016.2.1 sau mai vechi.
* Aspectul/aproape de sugestii pentru anumite domenii de căutare (în special
  în aplicația Setări) este anunțat prin sunete și/sau braille.
* În anumite meniuri contextuale (cum ar fi în Edge), informația poziției
  (e.g. 1 din 2) nu mai este anunțată.

## Alarme și ceas

* Acum sunt anunțate valorile selectorului de dată. De asemenea, aceasta
  afectează comanda utilizată pentru a selecta atunci când reporniți ca să
  finalizați actualizările Windows.

## Calendarul și Poșta electronică

* NVDA nu mai anunță „doar citire” pentru numirea subiectului în calendar și
  conținutul mesajului în Poșta electronică.

## Calculator

* Când Enterul este apăsat, NVDA anunță rezultatele calculului.

## Cortana

* Răspunsurile textuale de la Cortana sunt anunțate în cele mai multe
  situații (dacă nu, redeschideți meniul start și încercați căutarea din
  nou).
* NVDA va tace atunci când vorbiți cu Cortana prin voce.
* NVDA va anunța o confirmare memento după ce ați setat unul.

## Poșta electronică și calendarul

* NVDA nu mai anunță „Editare” sau „doar citire” în corpul mesajului sau în
  alte câmpuri.

## Hărți

* NVDA redă bipul locației pentru locațiile hărții.

## Microsoft Edge

* Notificări, cum ar fi descărcări de fișiere, sunt acum anunțate.
* Rețineți că sprijinul global este experimental în acest moment (nu trebuie
  să utilizați Edge ca browser-ul principal pentru un timp).

## Setări

* Anumite informații, cum ar fi o actualizare Windows în curs de descărcare
  și/sau instalare esunt raportate automat.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.

## Skype Preview

* Textul indicatorului de scriere este anunțat la fel ca Skype pentru
  Desktop.
* Revenire parțială a comenzii Control+NvDA+1 până la 0 pentru citirea
  istoricul chatului recent și pentru deplasarea obiectului navigator la
  intrările chatului (la fel ca Skype pentru Desktop).

## Magazin

* După căutarea actualizărilor aplicației, nume de aplicații în lista
  aplicațiilor care urmează să fie actualizate sunt etichetate corect.

## TeamViewer Touch.

* sunt anunțate etichete pentru butoane rotative.
* sunt anunțate etichete pentru butoane.

## Banca Americii/Twitter

* Etichetele butoanelor sunt acum anunțate.

## Meteo

* Etichete precum „vremea” și „hărțile” sunt recunoscute ca etichete
  adegvate (patch de Derek Riemer).
* atunci când citiți o prognoză, utilizați săgețile stânga și  dreapta
  pentru a vă deplasa între elemente. Utilizați săgețile sus și jos pentru a
  citi articolele individuale. De exemplu, apăsând pe săgeata din dreapta
  poate raporta un "luni: 79 de grade, parțial noros, ...", apăsând săgeata
  în jos va spune "luni" Apoi, apăsând din nou va citi elementul următor (La
  fel ca temperatura). Acest lucru funcționează în prezent pentru
  previziunile zilnice și orare.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
