---
title: "Gerador diesel para energia de emergência em hospitais: guia de dimensionamento"
date: "2026-10-28"
excerpt: "Como dimensionar um gerador diesel para emergência hospitalar: lista de cargas, cálculo em kVA, partida de motores, autonomia de combustível, redundância e teste em banco de carga."
image: "/images/blog/hospital-generator-sizing.jpg"
---

![Gerador diesel silenciado para emergência hospitalar em nossa fábrica em Yangzhou](/images/blog/hospital-generator-sizing.jpg)

# Gerador diesel para energia de emergência em hospitais: guia de dimensionamento

Uma queda de rede em um hospital não é um incômodo. Em segundos, o centro cirúrgico perde a iluminação, os ventiladores da UTI passam para baterias que duram minutos e não horas, as geladeiras do banco de sangue começam a passar de 6 °C, os elevadores param entre andares com pacientes dentro e o sistema de chamada de enfermagem apaga.

Por isso um **gerador diesel para emergência hospitalar** é especificado de forma diferente de um gerador para fábrica ou obra. Não é “o maior conjunto que cabe no orçamento”, mas uma máquina de segurança de vida cuja potência, comportamento de partida, autonomia de combustível, acústica e registros de teste precisam ser defensáveis diante de um auditor de acreditação.

Este guia percorre a sequência real de cálculo que usamos em projetos hospitalares: montar a lista de cargas, converter para kVA com as correções necessárias, verificar a partida dos motores e então definir combustível, redundância, ruído e escopo de testes. Os números vêm das nossas folhas técnicas da série KC, incluindo dois conjuntos reais de classe hospitalar.

## 1. O que o gerador realmente alimenta em um hospital

A instalação elétrica hospitalar costuma ser dividida entre um suprimento normal e um ou mais barramentos essenciais. Apenas os barramentos essenciais passam pelo gerador. Definir bem essa fronteira é metade do trabalho.

| Grupo de carga | Conteúdo típico | O que significa para o cálculo |
|---|---|---|
| Segurança de vida | Iluminação de centro cirúrgico e UTI, alarme de incêndio, extração de fumaça, iluminação de escape, alarmes de gases medicinais | Transferência em cerca de 10 segundos, nunca pode ser desligada |
| Crítico | Equipamentos de UTI e neonatal, diálise, refrigeração do banco de sangue, cadeia de frio da farmácia, incubadoras de laboratório, TI e chamada de enfermagem | Estabilidade de tensão importa mais que potência bruta |
| Equipamentos | Elevadores, bombas de água, bomba de incêndio, climatização, esterilização, parte da cozinha e lavanderia | Manda a partida de motores, não a potência em regime |
| Opcional | Tomadas das enfermarias, ar-condicionado padrão, parte da cozinha | Normalmente não entra ou é desligado em sobrecarga |

Daí saem duas regras práticas. Primeira: não coloque o hospital inteiro no gerador se o orçamento e o tanque de combustível não sustentam isso — a maioria dos projetos leva 40–60 % da carga instalada ao barramento essencial. Segunda: trate cargas de motor como problema de partida, não de regime; um motor de elevador de 15 kW pode puxar de cinco a sete vezes a corrente nominal por um ou dois segundos.

O marco regulatório varia por país — NFPA 99 e NFPA 110 nos Estados Unidos, HTM 06-01 no Reino Unido, IEC 60364-7-710 para locais médicos na Europa e em muitos mercados de exportação. Diferem em detalhes, mas concordam no essencial: barramento essencial definido, tempo de transferência definido, duração de combustível definida e testes periódicos documentados. Confirme a edição local antes de fechar os kVA.

## 2. Primeiro a lista de cargas, depois os kVA

Toda discussão sobre potência hospitalar é, na prática, uma discussão sobre a lista de cargas. Faça em planilha, circuito por circuito.

Para cada item registre quatro dados: kW de placa, fator de potência, fator de demanda (quanto roda ao mesmo tempo) e método de partida (direta, estrela-triângulo, soft starter, inversor).

Exemplo para um hospital geral de 200 leitos com chillers, cozinha e lavanderia no barramento essencial. São valores de planejamento, não substituem o diagrama unifilar do projeto:

| Carga | kW conectados | Fator de demanda | kW em regime |
|---|---|---|---|
| Centros cirúrgicos, UTI, iluminação de emergência, sistemas de incêndio | 120 | 1,0 | 120 |
| Equipamentos de UTI, banco de sangue, farmácia, TI | 90 | 1,0 | 90 |
| Elevadores (4 × 15 kW) | 60 | 0,6 | 36 |
| Chiller (um no barramento essencial) | 90 | 1,0 | 90 |
| Bombas, tratamento de água, bomba de incêndio | 55 | 1,0 | 55 |
| Cozinha e lavanderia, parcial | 60 | 1,0 | 60 |
| **Total em regime** | | | **451** |

Um fator de diversidade de 0,9 resulta em cerca de **406 kW**. Some crescimento — o hospital ganha imagem, leitos, climatização — por isso 20 % é uma reserva realista: **487 kW**. O conjunto padrão mais próximo é uma unidade de **500 kW / 625 kVA**.

Depois revise a partida. Se o chiller parte direto com seis vezes a corrente enquanto o centro cirúrgico já está carregado, o conjunto precisa absorver esse degrau sem que a queda de tensão desligue equipamentos médicos. Se o teste falhar, a resposta não é automaticamente um gerador maior: é um soft starter ou inversor no chiller, normalmente mais barato do que 200 kW extras de alternador.

## 3. A fórmula e as quatro correções

A conversão básica é simples:

**kVA = kW ÷ fator de potência**

Com o fator padrão 0,8 indutivo dos nossos conjuntos de 50 Hz, 400 kW de carga em regime exigem 500 kVA de alternador antes de corrigir. Aplicam-se então quatro correções.

**Reserva de crescimento.** 15–25 % para hospital novo: ninguém dimensiona para o número de leitos de hoje.

**Partida de motores e carga em degraus.** A queda transitória de tensão deve ficar dentro do que o equipamento médico tolera. Nossas folhas da série KC especificam: desvio transitório de tensão ≤ 15 %, regulação de tensão em regime ≤ 0,5 %, desvio transitório de frequência ≤ 0,5 % e recuperação de tensão e frequência ≤ 3 segundos. É exatamente o que um monitor de UTI vê durante a transferência.

**Desclassificação por site.** Um conjunto nominal a 40 °C perde capacidade a 45 °C e perde mais em altitude. Se a sala é quente porque o radiador sopra contra um canto, desclassifique ou corrija a vazão de ar.

**Regime.** Potência de emergência (horas limitadas, sem sobrecarga) contra potência principal (contínua, 10 % de sobrecarga por uma hora). Um hospital que roda o conjunto oito horas durante reparo de rede está em emergência; um hospital com quedas diárias está em regime principal e precisa ser especificado assim.

## 4. Duas referências reais

Orientação abstrata é fácil de escrever e difícil de aplicar. Estes são dois conjuntos que fabricamos para serviço hospitalar, com dados tirados diretamente das folhas técnicas KC.

| Parâmetro | KC-YC200 | KC-YC1600 |
|---|---|---|
| Potência nominal / emergência | 200 kW / 220 kW | 1.600 kW / 1.760 kW |
| Tensão / corrente | 380/220 V, 360 A | 380/220 V, 2.880 A |
| Frequência, fator de potência | 50 Hz, 0,8 indutivo | 50 Hz, 0,8 indutivo |
| Motor | Yuchai YC6MK350L-D20, 235 / 258,5 kW | Yuchai YC16VTD2700-D30, 1.805 / 1.985 kW |
| Cilindros / cilindrada | Em linha 6, 10,34 L, 123 × 145 mm | V16, 52,26 L, 152 × 180 mm |
| Sobrealimentação / regulador | Turbo com trocador, eletrônico | Turbo com trocador, eletrônico |
| Consumo de combustível | 200 g/kWh | 200 g/kWh |
| Alternador | KCI-200, sem escovas, AVR, IP23, classe H, cobre | KCI-1600, sem escovas, AVR, IP23, classe H, cobre |
| Dimensões (C × L × A) | 3.000 × 1.100 × 1.750 mm | 5.500 × 2.200 × 2.700 mm |
| Peso | 2.800 kg | 15.800 kg (referência) |
| Ruído (LP7M) | 102 dB(A) | 102 dB(A) |

**Quando a classe de 200 kW serve.** Clínicas, centros de cirurgia ambulatorial, hospitais pequenos e anexos de imagem cujo barramento essencial se limita a iluminação de centro cirúrgico, equipamentos de UTI, sistemas de incêndio, TI e alguns elevadores, com o chiller no suprimento normal. Com 2.800 kg e 3 m de comprimento, entra em sala de máquinas no subsolo sobre paleteira — decisivo em retrofit com porta de 1,2 m.

**Quando a classe de 1.600 kW serve.** Hospitais regionais e universitários cujo barramento essencial inclui de fato chillers centrais, cozinha, lavanderia, imagem e 10–20 elevadores. Com 15.800 kg e 5,5 m, exige sala real, laje ou recinto no nível do solo, plano de içamento e, normalmente, duas unidades em paralelo em vez de uma.

Entre as duas há degraus intermediários; o ponto é que a folha técnica seja completa o bastante para o projetista lançar os números direto no modelo elétrico.

## 5. Autonomia: a pergunta das 72 horas

Combustível é onde as especificações hospitalares mais reprovam, porque o consumo é citado por kWh e todos esquecem de converter.

Com 200 g/kWh e diesel a cerca de 0,84 kg/L:

**Litros por hora = kW nominais × 0,2 ÷ 0,84**

| Carga (KC-YC200) | Combustível por hora | Em 24 h | Em 72 h |
|---|---|---|---|
| 100 % (200 kW) | 47,6 L/h | 1.143 L | 3.429 L |
| 50 % média (100 kW) | 23,8 L/h | 571 L | 1.714 L |
| 25 % média (50 kW) | 11,9 L/h | 286 L | 857 L |

Assim, um conjunto de 200 kW com média realista de meia carga precisa de cerca de **1.700 L para 72 horas**. Especifique um tanque principal de 2.000 L e sobra margem mais o volume não utilizável. Para o conjunto de 1.600 kW em meia carga são cerca de **4.570 L por 24 horas**, razão pela qual grandes hospitais instalam tanque enterrado ou com bacia de contenção e contrato de polimento de combustível, em vez de tanque na base.

Três detalhes que os inspetores verificam: **tanque diário** para 8 horas de operação (para que um problema no principal não pare o conjunto), **contenção de 110 %** do volume e **alarmes de nível alto e baixo** ligados à automação predial. Na linha de combustível, válvula de corte resistente ao fogo na saída do tanque e nunca passando pela caixa de escada.

## 6. Redundância, paralelismo e transferência

Um único gerador é um único ponto de falha. Hospitais raramente aceitam isso em obra nova.

| Esquema | Significado | Uso típico |
|---|---|---|
| N | Uma unidade dimensionada para a carga essencial | Clínicas, hospitais pequenos |
| N+1 | Uma unidade extra capaz de assumir a carga se qualquer uma falhar | Hospitais gerais, 3 × 500 kW para 1.000 kW |
| 2N | Dois suprimentos completos e independentes, salas separadas | Hospitais universitários, grandes campi |

O paralelismo entrega mais que redundância: duas unidades a 60 % em vez de uma a 100 % reduzem consumo e ruído noturno, e permitem manter uma enquanto a outra segura a carga. Nossos controladores suportam divisão de carga, divisão isócrona e sincronização automática, com barra de interligação para isolar uma unidade.

Na transferência, fixe cedo o tempo de comutação. Circuitos de segurança de vida costumam ser atendidos em cerca de 10 segundos; centros cirúrgicos e UTI cobrem essa lacuna com nobreak ou chave estática em vez de contar com gerador instantâneo. Teste toda a sequência — queda de rede, sinal do ATS, partida, excitação, fechamento do disjuntor, aceitação de carga — em bancada, não na noite do apagão.

## 7. Ruído, implantação e vizinhança

As duas unidades da tabela são de base aberta a 102 dB(A) medidos a 7 metros no ponto de referência LP7M. É alto, na ordem de uma motosserra. Aceitável em sala bem tratada ou em local remoto, inaceitável a 30 metros da janela de uma enfermaria.

Opções por ordem de custo:

- **Capô acústico** — em geral leva a unidade para a faixa de 70–75 dB(A) a 7 m.
- **Tratamento da sala** — revestimento acústico, portas vedadas, piso flutuante e atenuadores de entrada e saída de ar bem dimensionados. Em conjuntos grandes costuma ser o caminho mais barato para um limite rigoroso na divisa.
- **Implantação** — afastar a descarga do radiador e a chaminé da fachada das enfermarias e conferir a altura em relação à janela praticável mais próxima.

Verifique os limites de divisa antes de escolher, pois variam muito; muitas jurisdições aplicam algo na faixa de 45–55 dB(A) no receptor sensível mais próximo à noite. Não presuma que só o capô resolve em uma máquina de 1,6 MW: não resolve.

## 8. Detalhes de instalação que decidem o resultado

São eles que transformam uma folha técnica correta em instalação funcionando:

- **Ar de refrigeração.** O radiador precisa de entrada livre e saída canalizada para o exterior. Sala com grelha do tamanho de uma caixa de correio desclassifica o conjunto e cozinha o alternador.
- **Contrapressão de escape.** Trechos longos, curvas fechadas e silenciadores subdimensionados elevam a contrapressão e custam potência. Trace com a contrapressão máxima admissível do fornecedor em mãos.
- **Isolamento de vibração.** Apoios de mola ou borracha sob a base, foles flexíveis no escape e conexão flexível de combustível. Sem eles o ruído viaja pela laje até as enfermarias acima.
- **Bitola de cabos.** Calcule pela corrente nominal na temperatura real e mantenha cabos de potência e de controle em eletrocalhas separadas.
- **Aterramento e neutro.** Confirme o esquema de aterramento com o engenheiro elétrico do hospital: o tratamento do neutro do gerador deve combinar com a instalação, não o contrário.
- **Compartimentação contra incêndio.** A sala do gerador é um compartimento com detecção própria e, em geral, extinção própria.
- **Acesso.** Deixe acessíveis a extremidade do alternador e os dois lados do motor: conjunto que não pode ser mantido falha cedo.

## 9. Testes: a parte que a maioria dos fornecedores pula

Um gerador de hospital é julgado na noite em que é necessário. Por isso cada unidade que sai da nossa fábrica em Yangzhou passa por um banco de carga digital antes do embarque, em sequência fixa:

| Etapa | Duração | O que se verifica |
|---|---|---|
| Sem carga | — | Aquecimento, pressão de óleo, tensão de carga |
| 25 % de carga | 30 min | Estabilidade de tensão e frequência, temperatura de escape |
| 50 % de carga | 30 min | Resposta do regulador, consumo, ruído |
| 75 % de carga | 60 min | Sistema de arrefecimento, temperatura do líquido, tensão da correia |
| 100 % de carga | 60 min | Potência nominal plena, regulação de tensão dentro de ±1,5 % |
| Sobrecarga 110 % | 1 min | Desarme de proteções e verificação de alarmes |

Após o ensaio verificamos resistência de isolação e continuidade de terra depois de ciclagem térmica, conferimos todas as proteções (sobrevelocidade, alta temperatura da água, baixa pressão de óleo, sobrecorrente, parada de emergência) e testamos a sequência do ATS de ponta a ponta em bancada. O relatório de ensaio viaja com a unidade.

Se o projeto exige teste com testemunho, laudo de inspeção de terceiros (BV, SGS ou TUV) ou protocolo FAT específico, isso deve ser reservado antes de a unidade entrar em produção, não na semana anterior ao embarque.

## 10. Por que hospitais trabalham com a Kaichen

Fabricamos grupos geradores em Yangzhou, na China, de 20 kVA a 3.000 kVA, e o segmento hospitalar é parte importante do nosso trabalho. Três coisas pesam mais aqui do que em qualquer outro setor.

**Fabricamos nossos próprios alternadores.** A série KCI tem enrolamento de cobre, isolação classe H, proteção IP23, regulação AVR e é produzida na mesma planta da montagem. Quando um hospital precisa de resposta transitória específica, trocamos o alternador em vez de comprar fora.

**Testamos em plena carga, em casa.** Um banco de carga digital de 2 MW permite provar uma unidade de 1.600 kW a 110 % antes do embarque, e não apenas em vazio no pátio.

**Documentamos no idioma do cliente.** Folhas técnicas, manuais de operação e manutenção, descrições da lógica de controle e placas podem ser fornecidos nos idiomas em que publicamos, o que encurta a comissionamento quando a equipe de obra não fala inglês.

Nossas referências hospitalares vão de uma unidade de 200 kW para um hospital municipal a instalações de classe 1.600–1.800 kW para campi de hospitais regionais, incluindo máquinas que estão em serviço de emergência há anos com testes de carga programados. Cada embarque inclui documentação CE e ISO 9001, kit de peças para o primeiro intervalo de manutenção e suporte técnico 24/7 durante o comissionamento.

## Perguntas frequentes

**Que tamanho de gerador um hospital precisa?**
Depende do barramento essencial, não do número de leitos. Uma clínica com iluminação de centro cirúrgico, equipamentos de UTI e dois elevadores costuma precisar de 150–250 kW. Um hospital geral de 200 leitos com chillers no barramento essencial fica normalmente entre 400 e 600 kW. Um campus regional com cozinha, lavanderia, imagem e mais de 15 elevadores costuma precisar de 1.200–2.000 kW, geralmente duas ou mais unidades em paralelo.

**Quanto tempo o combustível deve durar?**
Especificações comuns pedem 72 horas em uma carga definida, às vezes 96 horas em instalações críticas. Dimensione o tanque pelo consumo real em g/kWh na carga média prevista: para uma unidade de 200 kW em meia carga, cerca de 1.700 L cobrem 72 horas.

**Um gerador diesel pode alimentar centros cirúrgicos?**
Sim, mas não diretamente. O centro cirúrgico é normalmente alimentado por nobreak ou chave estática que cobre os 10–30 segundos até o gerador assumir a carga; depois disso o gerador precisa manter tensão e frequência dentro dos limites tolerados pelo equipamento.

**Capô acústico ou base aberta?**
Acústico para tudo que seja audível de enfermarias, equipe ou divisa. Base aberta só é prática em sala bem tratada ou recinto remoto.

**Com que frequência testar um gerador de hospital?**
Rodagens mensais em vazio ou baixa carga mais um teste anual em plena carga no banco são uma base comum; muitos esquemas de acreditação exigem testes mensais documentados e anuais em potência nominal. Teste o ATS junto, não separadamente.

## Próximo passo

Se você está especificando um conjunto hospitalar, envie a lista de cargas do barramento essencial e as condições do site — altitude, temperatura ambiente, limite de ruído na divisa, autonomia exigida — e dimensionaremos pela partida real, não por regra de bolso. Você pode ver a classe de máquina que fabricamos nas páginas do [gerador Cummins 200 kW silenciado](/pt/products/cummins-200kw-silent-diesel-generator/), do [gerador Yuchai 300 kW silenciado](/pt/products/yuchai-300kw-silent-diesel-generator/) e do [gerador Mitsubishi 1000 kW aberto](/pt/products/mitsubishi-1000kw-open-diesel-generator/), ou [fale conosco](/pt/contact/) com seu diagrama unifilar.
