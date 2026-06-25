import streamlit as st
import pandas as pd
import numpy as np
import os

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="SEDAPAL - Control Hídrico",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILO CSS PARA LA INTERFAZ INSTITUCIONAL
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
        
        /* Fondo general de la aplicación */
        .stApp {
            background-color: #F8F9FA;
            font-family: 'Open Sans', sans-serif;
        }
        
        /* Cabecera oficial en azul fuerte que te gustó */
        .sedapal-banner {
            background: linear-gradient(90deg, #005492 0%, #0076c0 100%);
            padding: 20px 30px;
            border-radius: 6px;
            margin-bottom: 25px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        
        /* Tarjetas de métricas (KPIs) */
        div[data-testid="stMetric"] {
            background-color: #FFFFFF;
            border-top: 4px solid #005492;
            border-radius: 4px;
            padding: 20px 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        }
        div[data-testid="stMetricValue"] {
            font-size: 28px !important;
            font-weight: 700 !important;
            color: #005492 !important;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 13px !important;
            color: #4B5563 !important;
            font-weight: 600;
        }
        
        /* Barra lateral con sutil contraste */
        [data-testid="stSidebar"] {
            background-color: #ECEFF1 !important;
            border-right: 1px solid #CFD8DC;
        }
        
        /* Estilos de títulos académicos */
        h1, h2, h3 {
            color: #005492 !important;
            font-weight: 700 !important;
        }
        
        /* Cuadro de texto destacado */
        .highlight-box {
            background-color: #E3F2FD;
            padding: 18px;
            border-radius: 6px;
            border-left: 5px solid #005492;
            margin-bottom: 20px;
            color: #1E3A8A;
        }
    </style>
""", unsafe_allow_html=True)

# 3. CABECERA CON BANNER AZUL
st.markdown("""
    <div class="sedapal-banner">
        <div style="color: white; font-size: 24px; font-weight: 700; letter-spacing: 0.5px;">
            SEDAPAL
        </div>
    </div>
""", unsafe_allow_html=True)

# Verificación de la imagen local para evitar errores visuales si aún no la descargas
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", width=140)
else:
    st.sidebar.markdown("<h2 style='color:#005492; margin-top:0;'>SEDAPAL</h2>", unsafe_allow_html=True)

# 4. BARRA LATERAL (Menú Operativo)
st.sidebar.markdown("<b style='color:#005492;'>MENÚ OPERATIVO</b>", unsafe_allow_html=True)
opcion = st.sidebar.radio(
    "Seleccione el módulo:",
    ["Resumen Ejecutivo", "Modelo Predictivo (Regresión)", "Evolución del ANF"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Facultad de Ingeniería\nUniversidad Científica del Sur")

# DATOS HISTÓRICOS ASOCIADOS
anos = [2013, 2014, 2015, 2016, 2017]
produccion = [680, 695, 710, 725, 740]
consumo_real = [420, 431, 438, 442, 451]

# 5. RENDERIZADO DE LAS SECCIONES
if opcion == "Resumen Ejecutivo":
    col_text, col_img = st.columns([2, 1])
    
    with col_text:
        st.subheader("Accesos Rápidos e Indicadores de Gestión")
        st.markdown("""
            <div class="highlight-box">
                <b>Evaluación General del Sistema:</b> Monitoreo integral de los volúmenes de distribución, 
                continuidad y cobertura de micromedición de agua potable en toda la red de Lima Metropolitana.
            </div>
        """, unsafe_allow_html=True)
    
    with col_img:
        st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=400&q=80")

    # Grid de KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Eficiencia General Red", value="60.9 %", delta="0.4 %")
    with col2:
        st.metric(label="Producción Promedio", value="710 MMC", delta="15 MMC")
    with col3:
        st.metric(label="Cobertura Micromedición", value="67.2 %", delta="1.1 %")
    with col4:
        st.metric(label="Continuidad Operativa", value="21.5 h/d", delta="0.3 h/d")
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Distribución de Consumo Facturado por Tipo de Conexión")
    
    df_usuarios = pd.DataFrame({
        'Categoría de Usuario': ['Conexión Doméstica', 'Conexión Comercial', 'Conexión Industrial', 'Uso Estatal / Público'],
        'Volumen Facturado Anual (m³)': ['285,400,000', '82,100,000', '43,500,000', '40,000,000'],
        'Participación del Sector': ['63.3%', '18.2%', '9.6%', '8.9%']
    })
    st.table(df_usuarios)

elif opcion == "Modelo Predictivo (Regresión)":
    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Análisis Analítico mediante Modelo de Regresión Multivariable")
        st.markdown("""
            <div class="highlight-box">
                <b>Optimización Predictiva:</b> Ajuste las variables de entrada del sistema para calcular de forma 
                inmediata la proyección estimada de la demanda en millones de metros cúbicos (MMC).
            </div>
        """, unsafe_allow_html=True)
    with col_img:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80")

    st.markdown("---")
    col_params, col_graph = st.columns([1, 2])
    
    with col_params:
        st.markdown("#### Parámetros del Sistema")
        prod_input = st.slider("Volumen de Producido (MMC)", 600, 800, 710)
        cont_input = st.slider("Horas de Continuidad de Servicio", 12, 24, 21)
        med_input = st.slider("Índice de Micromedición (%)", 50, 100, 67)
        
        prediccion = (prod_input * 0.55) + (cont_input * 1.8) + (med_input * 0.3)
        
    with col_graph:
        st.markdown("#### Proyección de la Demanda Estimada")
        st.metric(label="Consumo Estimado por el Modelo", value=f"{prediccion:,.2f} MMC")
        
        df_chart = pd.DataFrame({
            'Línea de Tiempo': anos + [2026],
            'Consumo Operativo (MMC)': consumo_real + [prediccion]
        }).set_index('Línea de Tiempo')
        st.line_chart(df_chart, height=260)

elif opcion == "Evolución del ANF":
    st.subheader("Monitoreo de Agua No Facturada (ANF)")
    
    st.markdown("""
        <div class="highlight-box">
            <b>Balance Hídrico Dinámico:</b> Comparativa histórica entre el volumen inyectado a las redes primarias 
            frente al volumen óptimo facturado comercialmente.
        </div>
    """, unsafe_allow_html=True)
    
    df_anf = pd.DataFrame({
        'Línea de Tiempo': anos,
        'Volumen Facturado': consumo_real,
        'Agua No Facturada (Pérdidas)': [260, 264, 272, 283, 289]
    }).set_index('Línea de Tiempo')
    
    st.area_chart(df_anf, height=320)