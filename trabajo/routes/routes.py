from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse
from model.dashboard_model import obtener_datos
from controller.controllers import calcular_estadisticas, generar_grafico

router = APIRouter()

@router.get("/datos")
def datos():
    df = obtener_datos()
    return df.to_dict(orient="records")

@router.get("/estadisticas")
def estadisticas():
    return calcular_estadisticas()

@router.get("/grafico/barras")
def grafico_barras():
    imagen = generar_grafico("barras")
    return Response(content=imagen, media_type="image/png")

@router.get("/grafico/lineas")
def grafico_lineas():
    imagen = generar_grafico("lineas")
    return Response(content=imagen, media_type="image/png")

@router.get("/", response_class=HTMLResponse)
def dashboard():
    df = obtener_datos()
    total = df["ventas"].sum()
    promedio = df["ventas"].mean()
    clientes = df["clientes"].sum()

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="UTF-8"><title>Dashboard de Ventas</title></head>
    <body style="font-family: Arial; padding: 30px; background: #f0f4f8;">
        <h1>Dashboard de Ventas</h1>
        <p>Ventas Totales: ${total:,.2f} | Promedio: ${promedio:,.2f} | Clientes: {clientes}</p>
        <div>
            <img src="/grafico/barras" style="max-width:48%;">
            <img src="/grafico/lineas" style="max-width:48%;">
        </div>
        <p><a href="/docs">Documentación API</a></p>
    </body>
    </html>
    """
    return HTMLResponse(content=html)