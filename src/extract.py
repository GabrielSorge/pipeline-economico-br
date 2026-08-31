import pandas as pd

def extrair_dados_brutos(caminho_arquivo, separador=";"):
    """
    Lê o arquivo CSV bruto e retorna um DF sem nenhum tratamento
    """
    df = pd.read_csv(caminho_arquivo, sep=separador)
    return df


if __name__ == "__main__":
    caminho = "data/raw/cotacao_dolar.csv"
    df_bruto = extrair_dados_brutos(caminho)

    print("=== Exploração inicial dos dados brutos ===")
    print(df_bruto.head())
    print("\nFormato (linhas, colunas):", df_bruto.shape)
    print("\nTipos de dados:")
    print(df_bruto.dtypes)
    print("\nValores nulos por coluna:")
    print(df_bruto.isnull().sum())
    print("\nLinhas duplicadas:", df_bruto.duplicated().sum())

