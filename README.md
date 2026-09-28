# Triage Queue — Gestor de Cola de Prioridad

Gestor de cola de prioridad para una sala de triage, implementado en Python y sin dependencias externas. Los pacientes se atienden primero según su nivel de triage (1 es la prioridad más alta); dentro de cada nivel se respeta el orden de llegada.

## Cómo ejecutar

Requiere Python 3. Ejecuta el gestor de cola con:

```bash
python triage_queue.py
```

Para ejecutar las pruebas:

```bash
python -m unittest -v
```