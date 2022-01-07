# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* Compatibilidade com NVDA: 2021.2 e posteriores

Nota: Originalmente chamado de Windows 10 App Essentials, foi renomeado para
Windows App Essentials em 2021 para oferecer suporte ao Windows 10 e versões
futuras, como Windows 11. Partes deste complemento ainda farão referência ao
nome do complemento original.

Este complemento é uma coleção de módulos de aplicativos (app modules) para
vários aplicativos modernos do Windows, bem como aprimoramentos e correções
para determinados controles encontrados no Windows 10 e posteriores.

Os seguintes módulos de aplicativos ou módulos de suporte para alguns
aplicativos estão incluídos (consulte a seção de cada aplicativo para obter
detalhes sobre o que está incluso):

* Calculadora
* Cortana
* Email
* Mapas
* Microsoft Solitaire Collection (Coleção de Paciência)
* Teclado moderno (painel de emoji/ditado/digitação por voz/sugestões de
  entrada de hardware/histórico da área de transferência/editores de métodos
  de entrada modernos)
* Pessoas
* Configurações (configurações do sistema, Windows+I)
* Clima
* Módulos diversos para controles, como blocos do Menu Iniciar

Notas:

* Este complemento requer o Windows 10 21H1 (compilação 19043) ou
  posteriores e é compatível com o Windows 11.
* Embora a instalação seja possível, este complemento não oferece suporte
  para Windows Enterprise LTSC (Long-Term Servicing Channel — Canal de
  Manutenção de Longo Prazo) e versões do Windows Server.
* Alguns recursos do complemento são ou farão parte do leitor de tela NVDA.
* * Para entradas não listadas abaixo, você pode presumir que os recursos
  fazem parte do NVDA, não são mais aplicáveis, pois o complemento não
  oferece suporte a versões não suportadas do Windows, como versões antigas
  do Windows 10, ou alterações foram feitas no Windows e aplicativos que
  tornam as entradas não mais aplicáveis.
* Alguns aplicativos suportam o modo de sobreposição compacta (sempre no
  topo da Calculadora, por exemplo), e este modo não funcionará corretamente
  com a versão portátil do NVDA.

Para obter uma lista de alterações feitas entre cada lançamento do
complemento, consulte o documento [changelogs for add-on releases][3].

## Geral

* O NVDA pode anunciar a contagem de sugestões ao realizar uma pesquisa na
  maioria dos casos, incluindo quando a contagem de sugestões muda à medida
  que a pesquisa avança. Isso agora faz parte do NVDA 2021.3.
* Além dos manipuladores de eventos UIA fornecidos pelo NVDA, os seguintes
  eventos UIA são reconhecidos: drag complete, drop target dropped, layout
  invalidated. Com o nível de log do NVDA definido para depuração, esses
  eventos serão rastreados e, para eventos de notificação UIA, um tom de
  depuração será ouvido se as notificações vierem de outro lugar que não o
  aplicativo atualmente ativo. Os eventos integrados ao NVDA, como mudança
  de nome e controlador de eventos, são rastreados a partir de um
  complemento chamado Event Tracker.
* Ao abrir, fechar, reordenar (Windows 11) ou alternar entre áreas de
  trabalho virtuais, o NVDA anunciará o nome do desktop virtual ativo (área
  de trabalho 2, por exemplo).
* O NVDA não anunciará mais o texto do tamanho do menu Iniciar ao alterar as
  resoluções ou orientação da tela.
* Ao organizar os blocos do menu Iniciar ou as ações rápidas da Central de
  Ações com as teclas Alt+Shift+setas, o NVDA anuncia informações sobre
  itens arrastados ou nova posição do item arrastado.
* Anúncios como alterações de volume/brilho no Explorador de Arquivo e
  notificações de atualização de aplicativos da Microsoft Store podem ser
  suprimidos desativando Anunciar Notificações nas configurações de
  apresentação de objetos do NVDA.

## Calculadora

* O NVDA não anunciará mais a mensagem de tela calculadora gráfica duas
  vezes.
* No Windows 10, os itens de lista do histórico e memória são devidamente
  rotulados.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações.
* O NVDA ficará em silêncio ao falar com Cortana via voz.

## Email

* Ao explorar itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para explorar os respectivos cabeçalhos. Note que a
  navegação entre linhas (mensagens) não é suportada.

## Mapas

* NVDA reproduz sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  ativada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Microsoft Solitaire Collection (Coleção de Paciência)

* O NVDA anunciará os nomes das cartas e dos baralhos.

## Teclado moderno

Isso inclui painel de emoji, histórico da área de transferência,
ditado/digitação por voz, sugestões de entrada de hardware e editores de
métodos de entrada modernos para determinados idiomas. Ao visualizar emojis,
para melhor experiência, habilite a configuração de Consórcio Unicode das
configurações de voz do NVDA e defina o nível do símbolo para "pouco" ou
superior. Ao colar do histórico da área de transferência no Windows 10,
pressione a tecla Espaço em vez da tecla Enter para colar o item
selecionado. O NVDA também suporta painel de experiência de entrada
atualizado no Windows 11.

* No Windows 10, quando um grupo de emoji (incluindo kaomoji e grupo de
  símbolos) é selecionado, o NVDA não moverá mais a navegação de objeto para
  certos emojis.
* Adicionado suporte para painel de experiência de entrada atualizado
  (painel de emoji combinado e histórico da área de transferência) no
  Windows 11.

## Pessoas

* Ao pesquisar contatos, a primeira sugestão será anunciada, principalmente
  se estiver usando versões recentes do aplicativo.

## Configurações

* Certas informações, como o progresso do Windows Update, são relatadas
  automaticamente, incluindo o widget Sensor de armazenamento/limpeza de
  disco e os erros do Windows Update.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* Foram corrigidos Rótulos de controle estranhos vistos em certas
  instalações do Windows.
* O NVDA anunciará o nome do controle de atualização de qualidade opcional,
  se houver (link para baixar e instalar agora no Windows 10, botão de
  download no Windows 11).
* No Windows 11, os itens da barra de localização atual são reconhecidos
  corretamente.

## Clima

* Abas como "previsão" e "mapas" são reconhecidas como guias adequadas
  (patch de Derek Riemer).
* Ao ler uma previsão, use as setas esquerda e direita para se mover entre
  os itens. Use as setas para cima e para baixo para ler os itens
  individuais. Por exemplo, pressionar a seta para a direita pode indicar
  "Segunda-feira: 79 graus, parcialmente nublado, ..." pressionar a seta
  para baixo dirá "Segunda-feira". Em seguida, pressionar novamente lerá o
  próximo item (como a temperatura). Atualmente, isso funciona para
  previsões diárias e horárias.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
