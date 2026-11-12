from model.dashboard_model import obtener_datos
from io import BytesIO
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def calcular_estadisticas():
    df = obtener_datos()
    return {
        "total_ventas": float(df["ventas"].sum()),
        "promedio_ventas": float(df["ventas"].mean()),
        "total_clientes": int(df["clientes"].sum()),
        "mejor_mes": str(df.loc[df["ventas"].idxmax(), "mes"])
    }

def generar_grafico(tipo):
    df = obtener_datos()
    fig, ax = plt.subplots(figsize=(9, 4))

    if tipo == "barras":
        ax.bar(df["mes"], df["ventas"], color="royalblue")
        ax.set_title("Ventas por mes")
        ax.set_ylabel("Ventas ($)")
    else:
        ax.plot(df["mes"], df["clientes"], marker="o", color="green", linewidth=3)
        ax.set_title("Crecimiento de clientes")
        ax.set_ylabel("Clientes")

    ax.grid(axis="y", alpha=0.2)
    plt.xticks(rotation=25)
    plt.tight_layout()

    imagen = BytesIO()
    fig.savefig(imagen, format="png", dpi=120)
    plt.close(fig)
    return imagen.getvalue()