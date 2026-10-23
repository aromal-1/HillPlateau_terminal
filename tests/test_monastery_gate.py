import tempfile
import unittest
from pathlib import Path

from monastery_gate import KnowledgeCentre, Visitor, VisaState, admit, open_window, quote


class GateTest(unittest.TestCase):
    def test_every_visa_state_is_admitted(self):
        for state in VisaState:
            self.assertTrue(admit(Visitor("A", visa_state=state))["admitted"])

    def test_window_from_santiniketan_starts_there(self):
        chain = open_window(23.68, 87.68)
        self.assertEqual(chain[0][0].name, "Visva-Bharati, Santiniketan")
        self.assertEqual(len({p.kind for p, _ in chain}), 4)

    def test_window_from_lhasa_finds_jokhang_or_potala(self):
        self.assertIn("Lhasa", open_window(29.655, 91.13)[0][0].name)

    def test_visit_is_free_and_stay_pays_gst(self):
        self.assertEqual(quote("V-1")["total"], 0.0)
        self.assertEqual(quote("V-1", nights=2, nightly=2000)["total"], 4200.0)
        self.assertEqual(quote("V-1", nights=1, nightly=10000)["gst"], 1800.0)

    def test_knowledge_centre_keeps_deposits(self):
        with tempfile.TemporaryDirectory() as d:
            kc = KnowledgeCentre(Path(d) / "k.jsonl")
            kc.deposit("V-1", "A song", "Bhutan", "...")
            self.assertEqual(kc.artefacts()[-1]["origin"], "Bhutan")


if __name__ == "__main__":
    unittest.main()
