# Windows 10 aplicações essenciais #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* NVDA compatibility: 2019.3 to 2020.1

Este extra é uma colecção de módulos de aplicações para várias aplicações do
Windows 10, bem como aprimoramentos e correcções para determinados
controlos.

Os seguintes módulos de aplicações ou módulos de suporte para algumas
aplicações estão incluídos (consulte a secção de cada aplicação para obter
detalhes sobre o que está incluído):

* Calculadora (moderna).
* Calendário.
* Cortana (Conversations)
* Correio.
* Mapas.
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Pessoas.
* Configurações (configurações do sistema, Windows + I)
* Meteorologia.
* Módulos diversos para controlos, como ecrãs do menu Iniciar.

Notas:

* This add-on requires Windows 10 Version 1903 (build 18362) or later. For
  best results, use the add-on with latest Windows 10 stable release (build
  18363).
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
* Para além dos diálogos já reconhecidos pelo NVDA, mais diálogos são agora
  reconhecidos como diálogos apropriados e relatados como tal, incluindo o
  diálogo Insider Preview (app de configurações).
* Na maioria dos casos, o NVDA pode anunciar a contagem de sugestões ao
  realizar uma pesquisa. Esta opção é controlada pelo ítem "fornecer
  informações de posição do objecto" no painel de apresentação de objectos
  que pode ser encontrado nas configurações do NVDA.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* Os seguintes eventos UIA são, agora, reconhecidos: alteração da posição do
  texto activo, controlador para, arrastar início, arrastar cancelamento,
  arrastar completo, elemento selecionado, alterar região ao vivo,
  notificação, alerta do sistema, tooltip aberta, janela aberta. Com o NVDA
  configurado para ser executado com o log de depuração activado, esses
  eventos serão rastreados e, para o evento de notificação UIA, um beep de
  depuração será ouvido se as notificações vierem de algum lugar diferente
  do aplicativo actualmente activo.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* Ao abrir, fechar ou alternar entre áreas de trabalho virtuais, o NVDA
  anunciará o nome da área de trabalho (área de trabalho 2, por exemplo).
* O NVDA deixará de anunciar o tamanho do texto do menu Iniciar quando
  alterar as resoluções ou a orientação do ecrã.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.
* IN recent releases of Word 365, NVDA will no longer announce "delete back
  word" when pressing Control+Backspace.

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

Most items are no longer applicable on Version 1903 and later unless Cortana
Conversations (Version 2004 and later) is in use.

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

## Microsoft Store

* Depois de verificar as atualizações da aplicação, os nomes das aplicações,
  na lista de aplicações a serem actualizadas, são indicados correctamente.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Teclado moderno

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

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
