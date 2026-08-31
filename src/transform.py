import pandas as pd

def transformar_dados(df):
    """
    Recebe o DataFrame bruto (colunas 'data' e 'valor' como string, 
    no formato brasileiro) e retorna um DataFrame tratado, com:
    - 'data' convertida para datetime
    - 'valor' convertido para float
    - validações de qualidade (nulos e duplicatas)
    """
    # Guarda o número de nulos ANTES da conversão, para comparação posterior
    nulos_antes = df[["data", "valor"]].isnull().sum().sum()

    # Converte 'data': string dd/mm/aaaa -> datetime
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)

    # Converte 'valor': string com vírgula decimal -> float
    df["valor"] = pd.to_numeric(df["valor"].str.replace(",", "."))

    # Conta os nulos DEPOIS da conversão
    nulos_depois = df[["data", "valor"]].isnull().sum().sum()

    # Valida que os tipos foram convertidos corretamente
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)


    assert pd.api.types.is_datetime64_any_dtype(df["data"]), "Coluna 'data' não foi convertida corretamente"
    assert df["valor"].dtype == "float64", "Coluna 'valor' não foi convertida corretamente"

    # Valida que a conversão não introduziu nulos novos (silenciosamente)
    assert nulos_depois == nulos_antes, (
        f"A conversão gerou {nulos_depois - nulos_antes} valores nulos novos! "
        "Verifique dados mal formatados."
    )

    # Checa duplicatas (não corrige automaticamente, só reporta por enquanto)
    duplicatas = df.duplicated().sum()
    print(f"Linhas duplicadas encontradas: {duplicatas}")

    return df

if __name__ == "__main__":
    from extract import extrair_dados_brutos

    df_bruto = extrair_dados_brutos("data/raw/cotacao_dolar.csv")
    df_tratado = transformar_dados(df_bruto)

    print(df_tratado.head())
    print(df_tratado.dtypes)

    df_tratado.to_csv("data/processed/cotacao_dolar_tratado.csv", index=False)
    print("Dados tratados salvos em data/processed/")