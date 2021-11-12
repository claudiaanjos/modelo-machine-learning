<img src="https://uploaddeimagens.com.br/images/003/534/518/original/Sem_t%C3%ADtulo.png?1636732351" width="300"/>

# Aplicação de um modelo de Machine Learning

## 📚  Descrição

O projeto faz parte da quarta oficina de **Data Science** - *Hands On: Aplicando um modelo de M.L.* da Semana das *Mulheres no Mundo da Tecnologia* promovida pela Fatech Girls e a DP6.

## Contexto do problema

*Contexto do negócio*: A Google, além de ser dona de várias ferramentas, também tem uma loja online chamada **Google Merchandise Store**. 

*Objetivos:* Existe a necessidade de se entender o comportamento de acessos à loja online durante os próximos meses, isso porque a equipe de mídia digital e UX da Google Merchandise está planejando ações mensais promovendo uma maior retenção do usuário no site, tanto com novas campanhas e anúncios, quanto com promoções internas dentro do site, buscando atrair os usuários que podem desistir da compra.

*Estratégias:* Entender o comportamento esperado de acessos diariamente do próximo mês para ser utilizado como base na construção das metas para as áreas e planejamento das ações:


- **UX**: nos dias onde se espera maior volume de usuários acessando o site promover as ações internas (dentro do site) incentivando o funil de compra
- **Mídia digital**: nos dias onde se espera um volume menor de acessos ter ações de publicidade online (fora do site) para atrair novos usuários para a loja e melhorar o Conhecimento e Engajameno de usuários com a marca 

## Cliente: loja do Google

#### [Google Official Merchandise Store](https://www.googlemerchandisestore.com/)

![](https://uploaddeimagens.com.br/images/003/534/314/original/google.png?1636726817)

## Dados Disponíveis

![](https://uploaddeimagens.com.br/images/003/534/327/original/google.png?1636727111)

![](https://uploaddeimagens.com.br/images/003/534/338/original/google.png?1636727265)

## Avaliação da amostra de dados existente

#### 1. Qual mês quero entender e prever o comportamento dos acessos?
#### 2. Existem dados suficientes para realizar a previsão?

#### Visualizando rapidamente os dados históricos e ao longo do tempo

![](https://uploaddeimagens.com.br/images/003/534/347/original/google.png?1636727497)

#### Observando os acessos ao longo de 2 anos aproximadamente

![](https://uploaddeimagens.com.br/images/003/534/351/original/google.png?1636727604)

#### Evolutivo do volume de acessos agrupados por semana

![](https://uploaddeimagens.com.br/images/003/534/356/original/google.png?1636727701)

#### Evolutivo do volume de acessos agrupados por mês

![](https://uploaddeimagens.com.br/images/003/534/366/original/google.png?1636727811)

#### Analisando a evolução de outras métricas relevantes ao longo do tempo, como visualização de páginas, novas visitas e receita

![](https://uploaddeimagens.com.br/images/003/534/376/original/google.png?1636727915)


## Escolha do modelo de forecast: **Prophet**

### [Documentação Prophet](https://facebook.github.io/prophet/docs/installation.html#python)

Vamos utilizar o Prophet por ser um modelo que:  

*   Lida bem com séries temporais estacionárias e não-estacionárias 
*   Trabalha com dois tipos de séries temporais não estacionárias: uma série aditiva com uma tendência linear; uma série aditiva com uma tendência do tipo logística;
*   Modela a sazonalidade como sendo séries de fourier e permite a entrada de variáveis externas ao histórico
*   Fácil implementação

#### Agrupando as métricas relevantes em função da data para estar no formato certo na hora de rodar o modelo

![](https://uploaddeimagens.com.br/images/003/534/411/original/google.png?1636728383)

#### Salvando o nome das colunas de target e data para facilitar a execução e criando nossa baseline para o modelo

![](https://uploaddeimagens.com.br/images/003/534/420/original/google.png?1636728489)

#### A série temporal e sua tendência mensal

![](https://uploaddeimagens.com.br/images/003/534/472/original/google.png?1636730376)

## O modelo

#### Visualizando toda a série e o mês previsto

![](https://uploaddeimagens.com.br/images/003/534/481/original/google.png?1636730730)

## Avaliando o modelo

![](https://uploaddeimagens.com.br/images/003/534/484/original/google.png?1636730881)


&nbsp;


<a href="https://www.linkedin.com/in/claudia-nogueira-dos-anjos-b71726215/" target="_blank">
        <img src="https://img.shields.io/badge/claudiaanjos-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white&link=mailto:https://www.linkedin.com/in/claudia-nogueira-dos-anjos-093407180/">
</a>