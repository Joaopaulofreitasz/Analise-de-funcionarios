# Analise-de-funcionarios
Nome - João Paulo de Freitas Costa - matrícula - 202404000095
Dashboard interativo desenvolvido com Streamlit para análise de dados, com filtros dinâmicos, KPIs, tabelas e gráficos. Permite explorar informações de forma simples e visual utilizando apenas Python.

## Objetivo

Este projeto consiste em um dashboard interativo desenvolvido em Python utilizando Streamlit, com foco na análise de dados de funcionários. A aplicação permite visualizar métricas, explorar dados filtrados, gerar gráficos interativos e trabalhar com arquivos CSV personalizados.

## Funcionalidades

O dashboard possui as seguintes funcionalidades:

* Filtros interativos na sidebar:

  * Seleção de cidades
  * Faixa salarial (slider)
  * Categoria salarial (selectbox)

* Indicadores (KPIs):

  * Salário médio
  * Total de funcionários
  * Salário máximo

* Tabela interativa com os dados filtrados

* Gráficos interativos com Plotly:

  * Salário por cidade com cores por categoria
  * Distribuição por categoria salarial
  * Tooltip customizado com informações detalhadas

* Tabela dinâmica (Pivot Table):

  * Média salarial por cidade e categoria

* Upload de CSV:

  * Permite substituir os dados padrão por um arquivo enviado pelo usuário

* Download:

  * Exportação dos dados filtrados em formato CSV

## Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* NumPy
* Plotly

## Como Executar o Projeto

1. Clone o repositório:

```
git clone <https://github.com/Joaopaulofreitasz/Analise-de-funcionarios>
cd <Aula 04>
```

2. Instale as dependências:

```
pip install streamlit pandas numpy plotly
```

3. Execute o aplicativo:

```
streamlit run app.py
```

4. O dashboard será aberto automaticamente no navegador.

## Estrutura dos Dados

Para utilizar a funcionalidade de upload, o arquivo CSV deve conter pelo menos as seguintes colunas:

* nome
* idade
* cidade
* salario

A coluna `categoria_salario` é criada automaticamente pela aplicação com base no valor do salário.

## Lógica do Projeto

O fluxo do dashboard segue os seguintes passos:

1. Carregamento dos dados (ou leitura do CSV enviado)
2. Tratamento e criação de novas colunas
3. Aplicação dos filtros definidos na sidebar
4. Geração das métricas (KPIs)
5. Exibição da tabela e visualizações
6. Disponibilização de download dos dados filtrados

## Melhorias Implementadas

Este projeto inclui melhorias em três níveis de complexidade:

* Filtro adicional por categoria salarial utilizando selectbox
* Substituição dos gráficos nativos por visualizações interativas com Plotly
* Implementação de upload de CSV com integração completa aos filtros existentes

## Observações

* O uso de cache com `@st.cache_data` melhora a performance ao evitar recarregamentos desnecessários
* Os gráficos são atualizados automaticamente conforme os filtros são alterados
* O sistema é totalmente reativo, característica principal do Streamlit

## Autor

Projeto desenvolvido para fins educacionais no contexto de aprendizado de dashboards com Streamlit.

