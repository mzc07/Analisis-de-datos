def segmentacion_tendencia(df):
    print("\n=== SEGMENTACIÓN DE TENDENCIAS POR PAÍS ===\n")

    tendencias = []  # lista donde guardaremos los resultados

    # Lista de todos los países
    paises = df["Country Name"].unique()

    for pais in paises:
        datos_pais = df[df["Country Name"] == pais].sort_values("Year")

        # Tasa inicial y final
        tasa_inicial = datos_pais["Suicide Rate"].iloc[0]
        tasa_final = datos_pais["Suicide Rate"].iloc[-1]

        # Clasificación según cambio
        cambio = tasa_final - tasa_inicial

        if cambio > 0.2:
            tendencia = "Sube"
        elif cambio < -0.2:
            tendencia = "Baja"
        else:
            tendencia = "Estable"

        tendencias.append({
            "Country": pais,
            "Tasa_inicial": tasa_inicial,
            "Tasa_final": tasa_final,
            "Cambio": cambio,
            "Tendencia": tendencia
        })

    # Convertimos a DataFrame para imprimirlo bonito
    resultado = pd.DataFrame(tendencias)

    print(resultado.sort_values("Tendencia"))
    print("\nFin de la segmentación.\n")

    input("Presiona ENTER para volver al menú...")

    return resultado
