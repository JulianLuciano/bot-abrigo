# API de Recomendación de Abrigo

Este proyecto despliega una API en FastAPI que predice qué abrigo deberías usar, basada en datos meteorológicos.

## Archivos

- `api.py`: Servidor FastAPI principal.
- `utils.py`: Funciones auxiliares para predicción.
- `weather.py`: Obtención de datos meteorológicos.
- `modelo_catboost3.cbm`: Modelo entrenado (agregar manualmente).
- `requirements.txt`: Dependencias del proyecto.

## Cómo desplegar en Railway

1. Crear cuenta en [Railway](https://railway.app)
2. Crear nuevo proyecto y subir estos archivos (menos el bot).
3. Establecer el comando de inicio en Settings:

```
uvicorn api:app --host 0.0.0.0 --port $PORT
```

4. Activar "on-demand instances" para no consumir horas innecesarias.

## Uso

El endpoint es:

```
POST /predecir
```

Body:
```json
{
  "lat": -34.6,
  "lon": -58.4,
  "lead": 2
}
```

Respuesta:
```json
{
  "abrigo": "buzo"
}
```

