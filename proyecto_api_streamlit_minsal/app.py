import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from api_client import get_locales, get_turnos
from analysis import to_dataframe, coerce_types, resumen_basico, top_por_categoria, abrir_vs_cerrar_promedio
from charts import bar_top, line_by_date

st.set_page_config(page_title="Farmacias MINSAL - Análisis API", layout="wide")
st.title("Análisis y presentación de datos utilizando APIs en Python")
st.caption("Fuente: Ministerio de Salud (MIDAS/Farmanet). Endpoints publicados en datos.gob.cl")
