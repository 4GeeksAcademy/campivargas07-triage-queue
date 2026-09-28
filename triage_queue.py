from collections import deque
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Patient:
    name: str
    triage_level: int
    arrived_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if self.triage_level not in (1, 2, 3):
            raise ValueError("El nivel de triage debe ser 1, 2 o 3.")

    def __str__(self):
        return (
            f"{self.name} — nivel {self.triage_level} "
            f"(llegada: {self.arrived_at:%Y-%m-%d %H:%M:%S})"
        )


class TriageQueue:
    def __init__(self):
        self._queues = {level: deque() for level in (1, 2, 3)}

    def enqueue(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Se esperaba un objeto Patient.")
        if patient.triage_level not in self._queues:
            raise ValueError("El nivel de triage debe ser 1, 2 o 3.")
        self._queues[patient.triage_level].append(patient)

    def dequeue(self):
        for level in (1, 2, 3):
            if self._queues[level]:
                return self._queues[level].popleft()
        return None

    def peek(self):
        for level in (1, 2, 3):
            if self._queues[level]:
                return self._queues[level][0]
        return None

    def list_queue(self):
        return [patient for level in (1, 2, 3) for patient in self._queues[level]]

    def stats(self):
        return {level: len(self._queues[level]) for level in (1, 2, 3)}


def main():
    queue = TriageQueue()
    options = (
        "1. Añadir paciente",
        "2. Llamar al siguiente",
        "3. Ver cola",
        "4. Ver estadísticas",
        "5. Salir",
    )

    while True:
        print("\n=== Triage Queue ===")
        print("\n".join(options))
        try:
            choice = input("Selecciona una opción: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSaliendo de Triage Queue.")
            break

        if choice == "1":
            try:
                name = input("Nombre del paciente: ").strip()
                if not name:
                    print("El nombre no puede estar vacío.")
                    continue
                level = int(input("Nivel de triage (1-3): ").strip())
                patient = Patient(name=name, triage_level=level)
                queue.enqueue(patient)
                print(f"Paciente añadido: {patient}")
            except ValueError as error:
                print(f"Entrada inválida: {error}")
            except (EOFError, KeyboardInterrupt):
                print("\nRegistro cancelado.")
        elif choice == "2":
            patient = queue.dequeue()
            if patient is None:
                print("No hay pacientes en espera.")
            else:
                print(f"Siguiente paciente: {patient}")
        elif choice == "3":
            patients = queue.list_queue()
            if not patients:
                print("La cola está vacía.")
            else:
                print("Pacientes en orden de atención:")
                for position, patient in enumerate(patients, start=1):
                    print(f"{position}. {patient}")
        elif choice == "4":
            print("Pacientes en espera por nivel:")
            for level, count in queue.stats().items():
                print(f"Nivel {level}: {count}")
        elif choice == "5":
            print("Saliendo de Triage Queue.")
            break
        else:
            print("Opción inválida. Elige un número del 1 al 5.")


if __name__ == "__main__":
    main()
