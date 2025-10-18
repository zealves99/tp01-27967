# TP01 – Integração e Análise de Dados (Consumos de Energia ao longo de um espetáculo)
**Autor:** José Alves  
**Número de Aluno:** 27967  

---

## Estrutura do Repositório
O projeto segue a seguinte organização de pastas:

```
tp01-27967/
├── .gitattributes
├── node-red-graph-generator.json           # Fluxo Node-RED para geração e integração de dados
├── requirements.txt                        # Dependências Python
│
├── data/
│   ├── input/                              # Ficheiros de entrada do pipeline
│   │   ├── marat-sade.xml                  # Dados principais do espetáculo Marat/Sade
│   │   ├── patchfiles.csv                  # Ficheiro com nome dos ficheiros de patch
│   │   ├── power_consumption.csv           # Potências máximas de cada máquina/tipo de máquina
│   │   └── patch/                          # Ficheiros CSV por camada de patch
│   │       ├── ALCOVAS LAT_t.csv
│   │       ├── AUTOYOKE_t.csv
│   │       ├── BANCOS_t.csv
│   │       ├── BANHEIRA_t.csv
│   │       ├── CADEIRA COUMIER_t.csv
│   │       ├── CANTORES_t.csv
│   │       ├── CODA PUB_t.csv
│   │       ├── CONTRAS_t.csv
│   │       ├── FRENTES_t.csv
│   │       ├── FUMO_t.csv
│   │       ├── GUILHOTINA_t.csv
│   │       ├── LATERAIS RED_t.csv
│   │       ├── LEQUE PAREDES_t.csv
│   │       ├── MUSICOS_t.csv
│   │       ├── PORTA_t.csv
│   │       ├── REV4_t.csv
│   │       └── VENTOINHAS_t.csv
│   │
│   └── output/                             # Resultados e gráficos gerados
│       ├── cueData.txt
│       ├── cueTimes.txt
│       ├── dimmer_consumption.csv
│       ├── dim_export.txt
│       ├── fixture-graph-data.json
│       ├── fixtures_export.txt
│       ├── fixture_consumption.csv
│       ├── http-out.txt
│       ├── layer-graph-data.json
│       ├── total-energy-graph-data.json
│       ├── total-power-graph-data.json
│       └── graphs/
│           ├── layer_bar_graph.png
│           └── layer_pie_graph.png
│
├── dataint/                                # Processos ETL em Pentaho Data Integration (Kettle)
│   ├── a27967.kjb                          # Job principal
│   ├── Calculate_Power_Consumption.ktr      # Cálculo de consumo energético
│   ├── Get_CueData_From_XML.ktr             # Extração de dados de cues a partir do XML
│   ├── Graph_Creation.ktr                   # Geração de datasets para gráficos
│   ├── Patch_Import.ktr                     # Importação e normalização de ficheiros patch
│   └── SendEmail.ktr                        # Envio automático de resultados por email
│
├── report/
│   └── essay.pdf                            # Relatório final em PDF
│
└── scripts/
    └── graph_generator.py                   # Script Python para criação dos gráficos finais
```

---

## Descrição do Projeto
O projeto **TP01 – Integração e Análise de Dados (Consumos de Energia ao longo de um espetáculo)** consiste na construção de um **pipeline completo de ETL e análise de consumos energéticos** num contexto de **iluminação cénica teatral**.

O objetivo é **integrar dados provenientes de múltiplas fontes (XML, CSV, Node-RED)**, **calcular métricas de consumo de energia**, e **gerar visualizações automáticas** que auxiliam na análise da eficiência dos diferentes grupos de projetores e elementos técnicos.

### Principais componentes:

#### **Aquisição e Integração de Dados**
- O ficheiro `marat-sade.xml` contém os dados estruturados das cues e fixtures do espetáculo.
- Dados de patch e consumo energético são recolhidos e integrados via **Pentaho Kettle** e **Node-RED**.
- Cada fixture ou grupo técnico (e.g. ALCOVAS, BANHEIRA, GUILHOTINA) é representado por um ficheiro individual em `data/input/patch`.

#### **Transformação e Enriquecimento (Pentaho)**
- Normalização de nomes e timestamps.
- Cálculo de consumos energéticos agregados por cue, layer e fixture.
- Geração automática de ficheiros `.csv` e `.json` para análise.
- Exportação para o formato visual de gráficos e datasets estruturados.

#### **Análise e Visualização (Python)**
- O script `graph_generator.py` processa os dados gerados e cria gráficos:
  - Distribuição de consumo por layer (`layer_bar_graph.png`)
  - Percentagem de energia por grupo técnico (`layer_pie_graph.png`)
  - Gráficos agregados de energia total e potência por tempo.

#### **Relatório**
- O relatório técnico (`report/essay.tex` → `report/essay.pdf`) descreve o processo de integração, análise e resultados obtidos.

---

## Como Executar

### Pré-requisitos
- **Pentaho Data Integration (Kettle)** versão 10.2 ou superior  
- **Node-RED** (para integração e simulação de dados)
- **Python 3.10+** com os pacotes indicados em `requirements.txt`, nomeadamente:
  - `pandas`
  - `matplotlib`
  - `numpy`

### Passos de Execução

1. **Gerar ou importar dados com Node-RED**  
   - Abrir `node-red-graph-generator.json` no Node-RED.  
   - Dar deploy do fluxo.

2. **Executar o processo ETL no Pentaho**  
   - Abrir `dataint/a27967.kjb` no **Pentaho Data Integration (Spoon)**.  
   - Executar o job principal, que chama as transformações (`*.ktr`) para importar, calcular e exportar dados.  
   - Os resultados serão gerados em `data/output/`.

3. **Gerar gráficos e relatórios com Python**  
   - Executar o script:
     ```bash
     python scripts/graph_generator.py
     ```
   - Os gráficos serão criados na pasta `data/output/graphs`.

4. **Visualizar o relatório final**  
   - Relatório completo disponível em:  
     `http://127.0.0.1:1880/ui`

---

## Repositório Online
O repositório completo do projeto encontra-se disponível em:  
[https://github.com/zealves99/tp01-27967](https://github.com/zealves99/tp01-27967)

---

## Licença
Este projeto é disponibilizado apenas para fins académicos no âmbito da unidade curricular **Integração e Análise de Dados**.
