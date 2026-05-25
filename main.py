# -*- coding: utf-8 -*-

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("WorldCups.csv")

df.columns = [
    "Year",
    "Country",
    "Winner",
    "RunnersUp",
    "Third",
    "Fourth",
    "GoalsScored",
    "QualifiedTeams",
    "MatchesPlayed",
    "Attendance"
]

colunas_numericas = [
    "Year",
    "GoalsScored",
    "QualifiedTeams",
    "MatchesPlayed",
    "Attendance"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

def mostrar_tabela(dataframe, titulo):

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(dataframe.columns)),
        cells=dict(values=[dataframe[col] for col in dataframe.columns])
    )])

    fig.update_layout(title=titulo)

    fig.show(renderer="browser")

def agrupar_campeoes():

    agrupado = (
        df.groupby("Winner")
        .size()
        .reset_index(name="Titulos")
        .sort_values(by="Titulos", ascending=False)
    )

    fig = px.bar(
        agrupado.head(10),
        x="Winner",
        y="Titulos",
        title="Paises com Mais Titulos"
    )

    fig.show(renderer="browser")

def top_gols():

    ordenado = df.sort_values(
        by="GoalsScored",
        ascending=False
    )

    tabela = ordenado[
        ["Year", "Country", "GoalsScored"]
    ].head(10)

    mostrar_tabela(tabela, "Copas com Mais Gols")

def comparar_paises():

    dados = pd.DataFrame({
        "Pais": ["Brazil", "Germany", "Italy"],
        "Titulos": [
            len(df[df["Winner"] == "Brazil"]),
            len(df[df["Winner"] == "Germany"]),
            len(df[df["Winner"] == "Italy"])
        ]
    })

    fig = px.bar(
        dados,
        x="Pais",
        y="Titulos",
        title="Comparacao de Titulos"
    )

    fig.show(renderer="browser")

def operacoes_conjuntos():

    campeoes = set(df["Winner"])
    vice_campeoes = set(df["RunnersUp"])

    intersecao = list(campeoes.intersection(vice_campeoes))

    tabela = pd.DataFrame({
        "Paises Campeoes e Vice": intersecao
    })

    mostrar_tabela(tabela, "Operacoes com Conjuntos")

def grafico_titulos():

    titulos = (
        df.groupby("Winner")
        .size()
        .reset_index(name="Titulos")
        .sort_values(by="Titulos", ascending=False)
    )

    fig = px.bar(
        titulos,
        x="Winner",
        y="Titulos",
        title="Paises com Mais Titulos da Copa"
    )

    fig.show(renderer="browser")

def grafico_gols():

    fig = px.line(
        df,
        x="Year",
        y="GoalsScored",
        title="Quantidade de Gols por Copa",
        markers=True
    )

    fig.show(renderer="browser")

while True:

    print("\n================================")
    print(" SISTEMA COPA DO MUNDO ")
    print("================================")
    print("1 - Agrupar Campeoes")
    print("2 - Top Copas com Mais Gols")
    print("3 - Comparar Paises")
    print("4 - Operacoes com Conjuntos")
    print("5 - Grafico de Titulos")
    print("6 - Grafico de Gols")
    print("0 - Sair")

    opcao = input("\nEscolha uma opcao: ")

    if opcao == "1":
        agrupar_campeoes()

    elif opcao == "2":
        top_gols()

    elif opcao == "3":
        comparar_paises()

    elif opcao == "4":
        operacoes_conjuntos()

    elif opcao == "5":
        grafico_titulos()

    elif opcao == "6":
        grafico_gols()

    elif opcao == "0":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpcao invalida!")