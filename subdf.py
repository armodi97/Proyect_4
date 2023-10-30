import pandas as pd

# leer los datos
vehicles_df = pd.read_csv("vehicles_us.csv")

"""extraemos los valores unicos de las columnas con valores cualitativos para usarlos como filtro en el dashboard"""

brand = vehicles_df["model"].str.split(" ").str[0].unique()
transmission = vehicles_df["transmission"].unique()
condition = vehicles_df["condition"].unique()
type = vehicles_df["type"].unique()
