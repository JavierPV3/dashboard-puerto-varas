import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos de Puerto Varas Basket
data_equipo = {
    "Métrica": ["Puntos Favor", "Puntos Contra", "Diferencia", "Tiros de 2P (%)", "Tiros de 3P (%)", "Tiros Libres (%)",
                "Rebotes Totales", "Asistencias", "Pérdidas"],
    "Puerto Varas": [78.08, 78.00, 0.08, 54.0, 31.9, 65.4, 32.42, 18.33, 11.83],
    "Promedio Liga": [77.35, 76.93, 0.42, 50.73, 32.04, 70.36, 35.28, 17.18, 14.23]
}
df_equipo = pd.DataFrame(data_equipo)

# Datos de rendimiento de jugadores
data_jugadores = {
    "Jugador": ["Joshua Morris", "Patricio Arroyo", "Luis Mérida", "Marcelo Pérez", "Andrew Corum", "Nicolás Villagrán"],
    "Valoración Cambio": [5.6, 3.5, 5.8, -6.2, -7.9, -0.2],
    "Puntos Cambio": [1.7, 3.0, 5.1, -5.6, -4.7, 2.3],
    "Rebotes Totales Cambio": [2.8, -0.7, -0.3, -0.6, -1.3, 0.9],
    "Asistencias Cambio": [0.0, 0.9, 0.2, -1.4, 0.0, -0.7]
}
df_jugadores = pd.DataFrame(data_jugadores)

# Configurar Streamlit
st.title("Dashboard Interactivo - Puerto Varas Basket 🏀")

# Filtro de métricas
st.sidebar.header("Filtros")
métrica_seleccionada = st.sidebar.selectbox("Selecciona una métrica", df_equipo["Métrica"])

# Gráfico de comparación de métricas
def graficar_metricas(métrica):
    df_seleccionado = df_equipo[df_equipo["Métrica"] == métrica]
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=["Puerto Varas", "Promedio Liga"], y=[df_seleccionado.iloc[0, 1], df_seleccionado.iloc[0, 2]], ax=ax)
    ax.set_title(métrica)
    ax.set_ylabel("Valor")
    st.pyplot(fig)

graficar_metricas(métrica_seleccionada)

# Filtro de jugadores
jugador_seleccionado = st.sidebar.selectbox("Selecciona un jugador", df_jugadores["Jugador"])

def graficar_jugador(jugador):
    df_jugador = df_jugadores[df_jugadores["Jugador"] == jugador].melt(id_vars=["Jugador"], var_name="Métrica", value_name="Valor")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x="Métrica", y="Valor", data=df_jugador, ax=ax, palette="coolwarm")
    ax.set_title(f"Rendimiento de {jugador}")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    st.pyplot(fig)

graficar_jugador(jugador_seleccionado)

st.write("📊 **Este dashboard permite analizar el rendimiento del equipo y sus jugadores en comparación con la liga.**")
