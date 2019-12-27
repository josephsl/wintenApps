# Windows 10 aplicativos essenciais #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][4] compatible with NVDA 2019.2.1 and earlier

Este complemento é uma coleção de módulos de aplicativos — app modules —
para vários aplicativos do Windows 10, bem como aprimoramentos e correções
para determinados controles.

Os seguintes módulos de aplicativos ou módulos de suporte para alguns
aplicativos estão incluídos (consulte a seção de cada aplicativo para obter
detalhes sobre o que está incluído):

* Calculadora (moderna).
* Calendário
* Cortana (Classic and Conversations)
* Central de comentários
* Email
* Mapas
* Microsoft Edge
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Pessoas
* Configurações (configurações do sistema, Windows+I)
* Clima.
* Módulos diversos para controles, como telas do menu Iniciar.

Notas:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18363) and latest stable version of NVDA.
* Alguns recursos do complemento são ou farão parte do leitor de tela NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to Windows 10 and apps that makes entries
  no longer applicable.

Para obter uma lista de alterações feitas entre cada lançamento do
complemento, consulte o documento [changelogs for add-on releases][3].

## Geral

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7, Windows 8.1, and unsupported releases of Windows
  10.
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu in Version 1809
  (October 2018 Update).
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu. This is now part of NVDA 2019.3.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* Em determinados menus de contexto (como no Edge), as informações de
  posição (por exemplo, 1 de 2) deixaram de ser anunciadas.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* Tooltips from Edge and universal apps are recognized and will be
  announced. This is now part of NVDA 2019.3.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* O NVDA deixará de anunciar o tamanho do texto do menu Iniciar quando
  alterar as resoluções ou a orientação da tela.
* App name and version for various Microsoft Store apps are now shown
  correctly. This is now part of NVDA 2019.3.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.

## Calculadora

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* Para cálculos como conversor de unidades e conversor de moeda, o NVDA
  anunciará os resultados assim que os cálculos forem inseridos.
* O NVDA não anunciará mais "nível de cabeçalho" para os resultados da
  calculadora.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.
* Added support for always on mode in Calculator version 10.1908 and later.

## Calendário

* O NVDA já não anuncia "editar" ou "somente leitura" no corpo da mensagem e
  em outros campos.

## Cortana

Most items are no longer applicable on Version 1903 and later. Classic
Cortana refers to older Cortana interface which was part of Start menu.

* Textual responses from Cortana (both Classic and Conversations UI) are
  announced in most situations (if using Classic Cortana, reopen Start menu
  and try searching again if responses are not announced).
* O NVDA ficará em silêncio ao falar com Cortana via voz.
* In Classic Cortana, NVDA will announce reminder confirmation after you set
  one.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## Central de comentários

* Para os lançamentos mais recentes de aplicativos, o NVDA deixará de os
  anunciar duas vezes.

## Email

* Ao explorar itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para explorar os respectivos cabeçalhos. Note que a
  navegação entre linhas (mensagens) não é suportada.
* Ao escrever uma mensagem, a aparência das sugestões de menção é indicada
  pelos sons.

## Mapas

* NVDA reproduz o sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  ativada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Microsoft Edge

This refers to classic EdgeHTML-based Microsoft Edge.

* Text auto-complete will be tracked and announced in address omnibar. This
  is now part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This is now part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This is now part
  of NVDA 2019.3.

## Microsoft Store

* Depois de verificar as atualizações de aplicativos, os nomes dos
  aplicativos na lista de aplicativos a serem atualizados, são indicados
  corretamente.
* Ao baixar conteúdos, como aplicativos e filmes, o NVDA anunciará o nome do
  produto e o progresso da transferência.

## Teclado moderno

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including redesigned panel in Version 1809 (build 17661 and later)
  and changes made in Version 1903 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in Version
  2004 (build 18963 and later) as the app has been renamed. All of these
  changes are now part of NVDA 2019.3.
* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

## Pessoas

* Ao procurar contatos, a primeira sugestão será anunciada, principalmente
  se usar os aplicativos mais recentes.

## Configurações

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* Para algumas caixas combinadas e botões de opção, o NVDA não falhará ao
  reconhecer os rótulos e / ou anunciar mudanças de valor.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later. This is now part of NVDA 2019.3.
* O NVDA não irá mais parecer não fazer nada ou tocar tons de erro se usar
  comandos de navegação de objetos sob algumas circunstâncias.
* A caixa de diálogo do lembrete do Windows Update é reconhecida como um
  diálogo apropriado.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## Clima

* Abas como "previsão" e "mapas" são reconhecidas como guias adequadas
  (patch de Derek Riemer).
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog

[4]: https://addons.nvda-project.org/files/get.php?file=w10-2019
