import pandas as pd
import plotly.express as px
import streamlit as st
import subdf


st.header("Análisis estadístico de un conjunto de autos en venta")


# Crea los valores de multiselect para filtrar
def checkboxes_gen(list):
    selection = st.sidebar.multiselect("Selecciona:", list)
    return selection


# Creamos un sidebar para añadir algunos filtros
st.sidebar.header("Filtrar por:")

# Filtro de marca
brand_check = st.sidebar.checkbox("Marca")
if brand_check:
    brands_selected = checkboxes_gen(subdf.brand)

else:
    brands_selected = subdf.brand.tolist()


# Filtro de condición
condition_check = st.sidebar.checkbox("Condición")
if condition_check:
    conditions_selected = checkboxes_gen(subdf.condition)

else:
    conditions_selected = subdf.condition.tolist()


# Filtro de transmisión
transmission_check = st.sidebar.checkbox("Transmisión")
if transmission_check:
    transmission_selected = checkboxes_gen(subdf.transmission)

else:
    transmission_selected = subdf.transmission.tolist()


# Filtro de tipo
type_check = st.sidebar.checkbox("Tipo")
if type_check:
    type_selected = checkboxes_gen(subdf.type)

else:
    type_selected = subdf.type.tolist()


# ejecutar filtro
confirm_filter = st.sidebar.button("Filtrar")
if confirm_filter:
    car_data = subdf.vehicles_df[
        (subdf.vehicles_df["transmission"].isin(transmission_selected))
        & (subdf.vehicles_df["type"].isin(type_selected))
        & (subdf.vehicles_df["model"].str.contains("|".join(brands_selected)))
        & (subdf.vehicles_df["condition"].isin(conditions_selected))
    ]
else:
    car_data = subdf.vehicles_df

# Creamos un dataframe para mostrar en el dashboard
st.dataframe(car_data)

# Creamos un grafico de dispersión para mostrar en el dashboard
fig = px.scatter(car_data, x="odometer", y="price")
st.plotly_chart(fig)

# Crear un histograma
choices = ["model_year", "price", "odometer", "date_posted", "days_listed"]
option = st.radio("Selecciona para ver la distribución:", choices)
hist = px.histogram(car_data, x=option)
st.plotly_chart(hist)
