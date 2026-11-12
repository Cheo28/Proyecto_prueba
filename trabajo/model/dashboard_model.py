from DB.conexion import ARCHIVO
import pandas as pd

def crear_dataset():
    if not ARCHIVO.exists():
        datos = {
            "mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
            "ventas": [1200, 1800, 1500, 2300, 2800, 3500],
            "clientes": [25, 32, 29, 40, 46, 58]
        }
        df = pd.DataFrame(datos)
        df.to_csv(ARCHIVO, index=False)

def obtener_datos():
    crear_dataset()
    return pd.read_csv(ARCHIVO)