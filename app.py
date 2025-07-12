import streamlit as st
import json
from extraer_datos import analizar_historia_clinica
from evaluador_ensayos import cargar_ensayos, evaluar_paciente

st.title("Evaluador de elegibilidad para ensayos clínicos")

historia = st.text_area("Pega aquí el texto clínico (en catalán o español)")

if st.button("Analizar"):
    datos_json = analizar_historia_clinica(historia)
    try:
        paciente = json.loads(datos_json)
        ensayos = cargar_ensayos("ensayos.json")
        resultados = evaluar_paciente(paciente, ensayos)
        st.subheader("Datos extraídos:")
        st.json(paciente)
        st.subheader("Evaluación de elegibilidad:")
        st.json(resultados)
    except Exception as e:
        st.error(f"Error analizando los datos: {e}")
