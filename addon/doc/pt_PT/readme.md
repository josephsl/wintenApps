# Windows 10 aplicações essenciais #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* NVDA compatibility: 2019.2 to 2019.3

Este extra é uma colecção de módulos de aplicações para várias aplicações do
Windows 10, bem como aprimoramentos e correcções para determinados
controlos.

Os seguintes módulos de aplicações ou módulos de suporte para algumas
aplicações estão incluídos (consulte a secção de cada aplicação para obter
detalhes sobre o que está incluído):

* Calculadora (moderna).
* Calendário.
* Cortana (Classic and Conversations)
* Central de comentários
* Correio.
* Mapas.
* Microsoft Edge
* Microsoft Store
* Teclado moderno (painel de emoji / ditado / sugestões de entrada de
  hardware / itens da área de transferência na nuvem na versão 1709 e
  posterior)
* Pessoas.
* Configurações (configurações do sistema, Windows + I)
* Meteorologia.
* Módulos diversos para controlos, como ecrãs do menu Iniciar.

Notas:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18363) and latest stable version of NVDA.
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.
* Para entradas não listadas abaixo, pode assumir que os recursos fazem já
  parte do NVDA, não sendo mais aplicáveis, pois o complemento não suporta
  versões antigas do Windows 10, ou foram feitas alterações no Windows 10 e
  nos aplicativos que tornam as entradas desnecessárias.

Para obter uma lista de alterações feitas entre cada release do extra,
consulte o documento [changelogs for releases, release][3].

## Geral

* O NVDA não reproduzirá mais os tons de erro ou não fará nada se este extra
  ficar activo no Windows 7 e 8.1 ou em versões não suportadas do windows
  10.
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu in Version 1809
  (October 2018 Update).
* Para além dos diálogos já reconhecidos pelo NVDA, mais diálogos são agora
  reconhecidos como diálogos apropriados e relatados como tal, incluindo o
  diálogo Insider Preview (app de configurações).
* Na maioria dos casos, o NVDA pode anunciar a contagem de sugestões ao
  realizar uma pesquisa. Esta opção é controlada pelo ítem "fornecer
  informações de posição do objecto" no painel de apresentação de objectos
  que pode ser encontrado nas configurações do NVDA.
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu. This will be part of NVDA 2019.3.
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
  announced. This will be part of NVDA 2019.3.
* Ao abrir, fechar ou alternar entre áreas de trabalho virtuais, o NVDA
  anunciará o nome da área de trabalho (área de trabalho 2, por exemplo).
* O NVDA deixará de anunciar o tamanho do texto do menu Iniciar quando
  alterar as resoluções ou a orientação do ecrã.
* App name and version for various Microsoft Store apps are now shown
  correctly. This will be part of NVDA 2019.3.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.

## Calculadora

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* Para cálculos como conversor de unidades e conversor de moeda, o NVDA
  anunciará os resultados assim que os cálculos forem inseridos.
* O NVDA não anunciará mais "nível de cabeçalho" para os resultados da
  calculadora.
* ao inserir expressões, o NVDA notificará se a contagem máxima de dígitos
  foi atingida.
* Added support for always on mode in Calculator version 10.1908 and later.

## Calendário.

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
* In Version 1909 (November 2019 Update) and 20H1 build 18945 and later,
  modern search experience in File Explorer powered by Windows Search user
  interface is supported.

## Central de comentários

* Para os lançamentos mais recentes de aplicativos, o NVDA deixará de os
  anunciar duas vezes.

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

## Microsoft Edge

This refers to classic EdgeHTML-based Microsoft Edge.

* Text auto-complete will be tracked and announced in address omnibar. This
  will be part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This will be part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This will be part
  of NVDA 2019.3.

## Microsoft Store

* Depois de verificar as atualizações da aplicação, os nomes das aplicações,
  na lista de aplicações a serem actualizadas, são indicados correctamente.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Teclado moderno

Most features below are now part of NVDA 2018.3 or later.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in build
  18963 and later as the app has been renamed. If using NVDA releases
  earlier than 2018.4, for best experience when reading emojis, use Windows
  OneCore speech synthesizer. If 2018.4 or later is in use, enable Unicode
  Consortium setting from NvDA's speech settings and set symbol level to
  "some" or higher.
* O NVDA não anunciará mais "área de transferência" quando houver itens na
  área de transferência em algumas circunstâncias.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in 20H1 build 18965 and later.

## Pessoas.

* Ao procurar contactos, a primeira sugestão será anunciada, principalmente
  se usar os aplicativos mais recentes.

## Configurações

* Certas informações, como o progresso da actualização do Windows, são
  relatadas automaticamente, incluindo sentido / disco de armazenamento e os
  erros da actualização do Windows.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* Para algumas caixas combinadas e botões de rádio, o NVDA não falhará ao
  reconhecer os rótulos e / ou anunciar mudanças de valor.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later. This will be part of NVDA 2019.3.
* O NVDA não irá mais parecer não fazer nada ou tocar tons de erro se usar
  comandos de navegação de objectos sob algumas circunstâncias.
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
