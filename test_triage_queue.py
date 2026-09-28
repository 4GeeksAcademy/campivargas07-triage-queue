import unittest
from datetime import datetime, timedelta

from triage_queue import Patient, TriageQueue


class TriageQueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = TriageQueue()

    def patient(self, name, level, minutes_after=0):
        return Patient(
            name=name,
            triage_level=level,
            arrived_at=datetime(2026, 1, 1) + timedelta(minutes=minutes_after),
        )

    def test_priority_between_levels(self):
        self.queue.enqueue(self.patient("Nivel 3", 3))
        self.queue.enqueue(self.patient("Nivel 2", 2, 1))
        self.queue.enqueue(self.patient("Crítico tardío", 1, 2))

        self.assertEqual(
            [patient.name for patient in self.queue.list_queue()],
            ["Crítico tardío", "Nivel 2", "Nivel 3"],
        )

    def test_fifo_within_same_level(self):
        self.queue.enqueue(self.patient("Primero", 2))
        self.queue.enqueue(self.patient("Segundo", 2, 1))

        self.assertEqual(self.queue.dequeue().name, "Primero")
        self.assertEqual(self.queue.dequeue().name, "Segundo")

    def test_empty_queue_operations(self):
        self.assertIsNone(self.queue.peek())
        self.assertIsNone(self.queue.dequeue())
        self.assertEqual(self.queue.list_queue(), [])
        self.assertEqual(self.queue.stats(), {1: 0, 2: 0, 3: 0})

    def test_invalid_triage_level(self):
        with self.assertRaises(ValueError):
            Patient("Inválido", 4)


if __name__ == "__main__":
    unittest.main()
