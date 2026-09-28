# Nota de diseño

Tres `deque`, una por nivel, permiten añadir y extraer en O(1) dentro de cada nivel. Al revisar los niveles 1, 2 y 3 en ese orden, se mantiene prioridad estricta y FIFO sin reordenar la cola. Una sola `deque` necesitaría buscar pacientes prioritarios; una lista ordenada implicaría desplazar elementos al insertar; un heap gestiona prioridades, pero requiere desempatar por llegada para conservar FIFO y no ofrece una ventaja aquí frente a las tres colas.

Si varios trabajadores accedieran concurrentemente, seleccionar y extraer al siguiente paciente tendría que ocurrir como una sola operación protegida (por ejemplo, mediante un `threading.Lock`). Así se evita que dos trabajadores obtengan y atiendan al mismo paciente. La implementación actual no incluye concurrencia.
