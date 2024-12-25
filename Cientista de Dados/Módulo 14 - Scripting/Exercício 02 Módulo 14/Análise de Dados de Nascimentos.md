# Análise de Dados de Nascimentos

## Descrição
Este projeto tem como objetivo analisar dados de nascimentos utilizando a linguagem Python e bibliotecas de análise de dados. Ele gera gráficos a partir de tabelas dinâmicas (pivot tables) para visualizar informações como quantidade de nascimentos, média de idade das mães, média de peso dos bebês, e índices APGAR.

## Tecnologias Utilizadas
- Python
- Pandas
- Matplotlib
- Seaborn

## Instalação
1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/analise-dados-nascimentos.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd analise-dados-nascimentos
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso
1. Coloque os arquivos CSV de entrada na pasta `./input`.
2. Execute o script passando os meses como argumentos:
    ```sh
    python "gerar_analise.py" JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ
    ```
    ![Script sendo executado no CMD](https://github.com/user-attachments/assets/e7a136e1-057d-4d43-af6e-25ad6a9de60c)
3. Os gráficos gerados serão salvos na pasta `./output/figs`:
    - Quantidade de nascimentos
    - Média da idade das mães por sexo
    - Média do peso dos bebês por sexo
    - Mediana do APGAR1 por escolaridade das mães
    - Média do APGAR1 por gestação
    - Média do APGAR5 por gestação

## Contribuição
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT.

## Contato
Para mais informações, entre em contato pelo email: [paulo.roberto@example.com](https://github.com/PaulodiasDeveloper)