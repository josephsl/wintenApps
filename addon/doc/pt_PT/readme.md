# Windows 10 aplicações essenciais #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* NVDA compatibility: 2020.4 and beyond

Este extra é uma colecção de módulos de aplicações para várias aplicações do
Windows 10, bem como aprimoramentos e correcções para determinados
controlos.

Os seguintes módulos de aplicações ou módulos de suporte para algumas
aplicações estão incluídos (consulte a secção de cada aplicação para obter
detalhes sobre o que está incluído):

* Calculator (modern)
* Calendário.
* Cortana (Conversations)
* Correio.
* Mapas.
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input
  suggestions/clipboard history/modern input method editors)
* Pessoas.
* Configurações (configurações do sistema, Windows + I)
* Meteorologia
* Miscellaneous modules for controls such as Start Menu tiles

Notas:

* This add-on requires Windows 10 Version 2004 (build 19041) or later. For
  best results, use the add-on with latest Windows 10 stable release
  (21H1/build 19043).
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.
* Para entradas não listadas abaixo, pode assumir que os recursos fazem já
  parte do NVDA, não sendo mais aplicáveis, pois o complemento não suporta
  versões antigas do Windows 10, ou foram feitas alterações no Windows 10 e
  nos aplicativos que tornam as entradas desnecessárias.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with portable version of
  NVDA.

Para obter uma lista de alterações feitas entre cada release do extra,
consulte o documento [changelogs for releases, release][3].

## Geral

* Na maioria dos casos, o NVDA pode anunciar a contagem de sugestões ao
  realizar uma pesquisa. Esta opção é controlada pelo ítem "fornecer
  informações de posição do objecto" no painel de apresentação de objectos
  que pode ser encontrado nas configurações do NVDA.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped. With NVDA's log
  level set to debug, these events will be tracked, and for UIA notification
  event, a debug tone will be heard if notifications come from somewhere
  other than the currently active app. Some events will provide additional
  information such as element count in controller for event, state of the
  element for state change event, and item text for item status event.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* When opening, closing, reordering (build 21337 or later), or switching
  between virtual desktops, NVDA will announce active virtual desktop name
  (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.

## Calculadora

* NVDA will no longer announce graphing calculator screen message twice.

## Calendário.

* O NVDA já não anuncia "editar" ou "somente leitura" no corpo da mensagem e
  em outros campos.

## Cortana

Most items are applicable when using Cortana Conversations (Version 2004 and
later).

* Textual responses from Cortana are announced in most situations.
* O NVDA ficará em silêncio ao falar com Cortana via voz.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## Correio.

* Ao rever itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para rever os respectivos cabeçalhos. Observe que a
  navegação entre linhas (mensagens) não é suportada.
* Ao escrever uma mensagem, a aparência das sugestões de menção é indicada
  pelos sons.

## Mapas.

* NVDA reproduz o sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  activada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Microsoft Store

* Depois de verificar as atualizações da aplicação, os nomes das aplicações,
  na lista de aplicações a serem actualizadas, são indicados correctamente.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Teclado moderno

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher. Also, NVDA
supports updated input experience panel in build 21296 and later.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* When an emoji group (including kaomoji and symbols group in Version 1903
  or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in build 21296 and later.

## Pessoas.

* Ao procurar contactos, a primeira sugestão será anunciada, principalmente
  se usar os aplicativos mais recentes.

## Configurações

* Certas informações, como o progresso da actualização do Windows, são
  relatadas automaticamente, incluindo sentido / disco de armazenamento e os
  erros da actualização do Windows.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* A caixa de diálogo de lembretes do Windows Update é reconhecida como um
  diálogo apropriado.
* Etiquetas de controlo ímpar, vistas em determinadas instalações do Windows
  10, foram corrigidas.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## Meteorologia

* Separadores como "previsão" e "mapas" são reconhecidos como separadores
  adequados (patch de Derek Riemer).
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
