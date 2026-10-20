---
date: '2026-10-16'
excerpt: Um único grupo de 500kW carregando toda a planta é um problema de planejamento diferente de um grupo de emergência. Sequenciamento de cargas, combustível e redundância decidem se o plano sobrevive ao contato com o chão.
title: 'Operando uma fábrica inteira em um único grupo de 500kW: Como os compradores planejam'
---

![Grupo diesel silencioso Weichai 500kW em canopy grande](/images/blog/blog-weichai-500kw-silent.jpg)

Há um momento em muitos projetos de fábrica quando o comprador olha para a cotação de conexão à rede e toma uma decisão: ou esperar seis meses pela concessionária estender um cabo novo e pagar a taxa de conexão, ou instalar um grupo a diesel que se torna a principal energia da planta.

Quando isso acontece, o gerador deixa de ser um backup e se torna um investimento. Um único grupo silencioso Weichai de 500 kW (cerca de 625 kVA) é uma forma comum para essa decisão. O planejamento, no entanto, é diferente de comprar uma unidade standby.

## Standby não é prime

A primeira coisa a internalizar: um grupo de 500 kW comprado como *potência primária* é uma máquina diferente da mesma caixa comprada como standby.

- Grupos standby ficam parados 99% do tempo. Rodam algumas horas por ano. O motor é dimensionado para esse ciclo de serviço.
- Grupos prime rodam de 8 a 24 horas por dia. São a principal fonte de energia. O motor deve ser dimensionado para serviço contínuo, com o sistema de combustível, refrigeração e lubrificação corretos.

Compre um grupo com classificação standby como prime e você o reconstruirá muito antes do esperado. Compre um grupo com classificação prime como standby e terá gasto um pouco mais que o necessário, mas a máquina é construída para vida mais longa.

## Sequenciamento de carga é todo o jogo

Um grupo de 500 kW não começa a carregar toda a fábrica em um segundo. Ele carrega em uma sequência projetada:

1. **Primeiros 0–30 segundos:** iluminação, escritório de controle, sistemas de segurança. O grupo esquenta até a tensão nominal.
2. **Próximo minuto:** motores menores, esteiras transportadoras, bombas d'água, ligados em ordem escalonada pelo controlador.
3. **Após três minutos:** grandes cargas — compressor de ar, chillers, motores principais de produção — ligados um a um.

Sem sequenciamento, a primeira partida do grande motor derruba a tensão e o grupo dispara em sobrecarga. Com sequenciamento, a fábrica sobe como subiria na rede.

É por isso que o controlador importa. Um controlador barato de três funções que só liga e desliga não é suficiente para um grupo prime de fábrica inteira. Você precisa de um controlador PLC que gerencie a sequência de partida e elimine cargas não essenciais se o grupo esquentar.

## A questão do combustível

Um grupo de 500 kW queima cerca de 90 a 110 litros por hora em carga média. Se rodar 12 horas por dia, são mais de mil litros por dia.

Planejar uma instalação de fábrica inteira significa planejar combustível:

- Tanque diário no grupo, 8–12 horas.
- Tanque bulk no pátio, dimensionado para uma semana de operação.
- Contrato de entrega com fornecedor local de diesel que consegue chegar ao local no prazo.

Pular o tanque bulk é como uma fábrica de potência primária se encontra esperando por um caminhão de combustível em um dia de produção.

## A questão da redundância

Um único grupo de 500 kW é um ponto único de falha. Para uma fábrica pequena, isso pode ser aceitável: quando o grupo está em manutenção, a produção pausa. Para uma fábrica com pedidos para embarcar, os compradores costumam planejar ou:

- Dois grupos de 300 kW em paralelo, dividindo a carga. Quando um está fora, o outro carrega a carga essencial.
- Um grupo de 500 kW mais uma unidade standby de 250 kW, para que a linha crítica fique no ar durante a manutenção.

Qual forma se encaixa depende de quão caro é um dia pausado para o negócio. Orçamos os dois e deixamos a matemática decidir.

## Weichai neste tamanho

Motores Weichai na faixa de 400–500 kW são comuns para instalações de potência primária porque o bloco é simples, mecânico e bem suportado em toda a Ásia e África. A tolerância ao combustível é boa para a qualidade local do diesel, e a rede de peças é densa. Para uma fábrica em um mercado em crescimento, essa reparabilidade é o que mantém a produção rodando.

## Fale conosco antes de especificar

Se você está decidindo entre uma conexão de rede e um grupo de potência primária, envie-nos a lista de cargas, as horas de operação por dia e o preço local do combustível. Faremos as contas e mostraremos qual opção realmente vence em cinco anos.

