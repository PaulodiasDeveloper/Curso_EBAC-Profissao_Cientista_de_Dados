# Análise de Dados de Telemarketing - Dashboard Interativo

![Banner](img/Bank-Branding.jpg)

Dashboard Streamlit para análise de campanhas de telemarketing bancário com filtros interativos e visualizações dinâmicas.

## 📌 Funcionalidades

- **📊 Visualização de Dados**
  - Gráficos de barras/pizza comparativos
  - Tabelas interativas
  - Proporções de conversão

- **🎚️ Filtros Avançados**
  - Controles deslizantes para idade
  - Multi-seleção para categorias
  - Filtros combinados

- **📤 Exportação**
  - Download dos dados filtrados (Excel)
  - Download das análises

## 🛠️ Tecnologias

- Python 3.10+
- Streamlit
- Pandas
- Seaborn
- Matplotlib
- Pillow

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone [https://github.com/PaulodiasDeveloper/Curso_EBAC-Profissao_Cientista_de_Dados.git]
```
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o dashboard:

```bash
streamlit run telemarketing_analysis.py
```

🗂️ Estrutura de Arquivos

```bash
project/
├── telemarketing_analysis.py  # Código principal
├── README.md                  # Este arquivo
├── requirements.txt           # Dependências
└── img/                       # Imagens
    ├── Bank-Branding.jpg      # Banner
    └── telmarketing_icon.png  # Ícone
```

📋 Pré-requisitos de Dados

Seu arquivo de dados deve conter estas colunas:

| Coluna       | Tipo      | Descrição                          |
|--------------|-----------|------------------------------------|
| age          | numérico  | Idade do cliente                   |
| job          | texto     | Profissão do cliente               |
| marital      | texto     | Estado civil                       |
| default      | texto     | Se possui inadimplência            |
| housing      | texto     | Possui financiamento imobiliário?  |
| loan         | texto     | Possui empréstimo pessoal?         |
| contact      | texto     | Meio de contato utilizado          |
| month        | texto     | Mês do último contato              |
| day_of_week  | texto     | Dia da semana do último contato    |
| y            | texto     | Aceitou a oferta? (target)         |


🎞️ Pequeno vídeo do projeto

<video width="600" controls>
  <source src="https://github.com/user-attachments/assets/24b5d6b2-4b9b-42c6-8a33-132acb5deb56" type="video/webm">
  Seu navegador não suporta o vídeo.
</video>


📄 Licença
MIT License - LICENSE

