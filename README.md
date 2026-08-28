# Pipeline de Monitoramento Econômico

Pipeline de dados para acompanhar a evolução de indicadores econômicos brasileiros — cotação do dólar (Banco Central) e, futuramente, dados populacionais/inflação (IBGE) — mantendo um histórico confiável e consultável.

Projeto integrador desenvolvido ao longo de um roadmap de 6 meses de Engenharia de Dados, evoluindo mês a mês em complexidade: de um script simples até um pipeline orquestrado, testado e documentado.

## Status atual do projeto

**Fase:** Fundamentos de Python para Dados 

O que já está implementado:
- Extração de dados a partir de arquivo estático (CSV) da série histórica de câmbio do Banco Central
- Exploração inicial da estrutura dos dados brutos (tipos, nulos, duplicatas)

O que ainda não foi implementado (propositalmente, por andamento dos meus estudos):
- Transformação/limpeza dos dados (conversão de tipos, tratamento de formato brasileiro)
- Organização do código em classes (Extractor/Transformer)
- Carga em banco de dados relacional
- Extração via API real (atualmente usa arquivo baixado manualmente)

## Arquitetura (visão atual)

```
Arquivo CSV bruto (data/raw/)
        │
        ▼
  Extração (src/extract.py)
        │
        ▼
DataFrame em memória, sem tratamento de tipos
```

A extração foi implementada como uma função isolada, sem nenhuma lógica de transformação junto — decisão intencional para manter as responsabilidades separadas desde o início (extração "burra", que só lê o dado como ele vem, sem interpretar).

## Fonte de dados

**Banco Central do Brasil — SGS (Sistema Gerenciador de Séries Temporais)**
Série 1: cotação do dólar comercial (venda).

Nesta fase do projeto, o arquivo é baixado manualmente via URL do SGS e salvo em `data/raw/`. A automação dessa extração via `requests`, com autenticação e tratamento de erros, está planejada para o Mês 4 do roadmap.

## Estrutura de pastas

```
pipeline-economic.../
├── data/
│   ├── raw/          # Dados brutos, como extraídos da fonte — nunca modificados manualmente
│   └── processed/    # Dados já tratados (ainda não utilizado)
├── notebooks/        # Exploração e testes pontuais, fora do código de produção
├── src/
│   ├── __init__.py
│   └── extract.py    # Função de extração dos dados brutos
├── tests/             # Testes automatizados (ainda não implementado)
├── venv/              # Ambiente virtual (não versionado)
├── requirements.txt
└── README.md
```

## Decisões técnicas

- **Dados brutos não são versionados no Git** (`data/raw/*.csv` está no `.gitignore`) — o repositório versiona o código que obtém os dados, não os dados em si.
- **Extração retorna os tipos originais do arquivo** (strings, sem conversão) — a normalização de tipos (datas, números com vírgula decimal) é responsabilidade da etapa de transformação, ainda não implementada.
- **`src/` é um pacote Python** (`__init__.py` presente), preparando o projeto para imports organizados conforme o código cresce.

## Como rodar

```bash
# Ativar o ambiente virtual
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Rodar a extração
python src/extract.py
```

## Próximos passos

- [ ] Implementar transformação: conversão de `data` para `datetime` e `valor` para `float` (formato brasileiro)
- [ ] Salvar dados tratados em `data/processed/`
- [ ] Escrever primeiros testes unitários para a função de extração
- [ ] Adicionar segunda fonte de dados (IBGE)