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

## Ejemplo de uso

Al iniciar el programa, puedes registrar pacientes de distintos niveles, consultar el orden de atención y llamar al siguiente. El nivel 1 tiene la prioridad más alta; dentro del mismo nivel se respeta el orden de llegada. En esta transcripción se omiten los menús que se vuelven a mostrar tras cada acción.

```text
$ python triage_queue.py
=== Triage Queue ===
1. Añadir paciente
2. Llamar al siguiente
3. Ver cola
4. Ver estadísticas
5. Salir
Selecciona una opción: 1
Nombre del paciente: Lucía
Nivel de triage (1-3): 3
Paciente añadido: Lucía — nivel 3 (llegada: 2026-09-28 10:00:00)

Selecciona una opción: 1
Nombre del paciente: Mateo
Nivel de triage (1-3): 1
Paciente añadido: Mateo — nivel 1 (llegada: 2026-09-28 10:01:00)

Selecciona una opción: 1
Nombre del paciente: Sara
Nivel de triage (1-3): 2
Paciente añadido: Sara — nivel 2 (llegada: 2026-09-28 10:02:00)

Selecciona una opción: 3
Pacientes en orden de atención:
1. Mateo — nivel 1 (llegada: 2026-09-28 10:01:00)
2. Sara — nivel 2 (llegada: 2026-09-28 10:02:00)
3. Lucía — nivel 3 (llegada: 2026-09-28 10:00:00)

Selecciona una opción: 2
Siguiente paciente: Mateo — nivel 1 (llegada: 2026-09-28 10:01:00)
```

Las fechas y horas mostradas son ilustrativas; el programa utiliza la hora local al registrar cada paciente.