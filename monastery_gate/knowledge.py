"""The knowledge centre: artefacts and tales visitors bring, kept in a JSON lines file."""
import json
from pathlib import Path

SEED_TALES = [
    {"title": "Mahakapi Jataka (the great monkey king)", "origin": "India",
     "tale": "A monkey king makes a bridge of his own body so his troop can escape across a river."},
    {"title": "The monkey and the rock ogress", "origin": "Tibet",
     "tale": "The Tibetan people descend from a meditating monkey and a rock ogress who asked him to marry her."},
    {"title": "Ruru Jataka (the golden deer)", "origin": "India",
     "tale": "A golden deer saves a drowning man, who later betrays him to a king; the king learns mercy."},
]


class KnowledgeCentre:
    def __init__(self, path="knowledge_centre.jsonl"):
        self.path = Path(path)

    def deposit(self, visitor_id, title, origin, tale):
        entry = {"visitor_id": visitor_id, "title": title, "origin": origin, "tale": tale}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        return entry

    def artefacts(self):
        if not self.path.exists():
            return list(SEED_TALES)
        with self.path.open(encoding="utf-8") as f:
            return list(SEED_TALES) + [json.loads(line) for line in f if line.strip()]
