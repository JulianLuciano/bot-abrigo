# API de Recomendación de Abrigo

Este proyecto despliega una API en FastAPI que predice qué abrigo deberías usar, basada en datos meteorológicos.

## Archivos

- `api.py`: Servidor FastAPI principal.
- `utils.py`: Funciones auxiliares para predicción.
- `weather.py`: Obtención de datos meteorológicos.
- `modelo_catboost3.cbm`: Modelo entrenado (agregar manualmente).
- `requirements.txt`: Dependencias del proyecto.
- `render.yaml`: Configuración para desplegar gratis en Render.

## Cómo desplegar en Render

1. Crear cuenta en [Render.com](https://render.com)
2. Subí estos archivos a un repositorio de GitHub.
3. Andá a Render → "New Web Service" → "Deploy from GitHub"
4. En el deploy configurá:

   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn api:app --host 0.0.0.0 --port 10000`
   - **Port**: 10000
   - **Instance Type**: Free

## Endpoint

```
POST /predecir
```

### Body esperado

```json
{
  "lat": -34.6,
  "lon": -58.4,
  "lead": 2
}
```

### Respuesta esperada

```json
{
  "abrigo": "buzo"
}
```

