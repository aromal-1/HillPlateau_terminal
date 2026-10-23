# monastery_gate: the Gate for travellers

An entry point for visitors from all around the world. Pure Python 3, no dependencies.

```sh
python3 -m monastery_gate --name Tenzin --born Lhasa --country Tibet --visa refugee \
    --lat 23.68 --lon 87.68                  # a perpetual visit to Santiniketan
python3 -m monastery_gate --name Ana --visa migrant --lat 27.7 --lon 85.3 --nights 3 --nightly 2500
python3 -m unittest tests.test_monastery_gate
```

| Part | What it does |
|---|---|
| **Gate** (`admit`) | Every visitor is admitted. `refugee`, `migrant`, `stateless` and every other visa state are allowed in. The visitor gets a pass id. |
| **Window** (`open_window`) | Finds the nearest research centre, monastery, temple and folk house to the visitor's location automatically, and chains them by distance. Buddhist sites rank first among places at a similar distance. |
| **Management** (`quote`) | A perpetual visit is free, with no accommodation charge and no GST. A stay is charged per night plus GST at India's hotel slabs (5% up to Rs 7,500 a night, 18% above). Check the current rates before charging anyone. |
| **Knowledge centre** (`KnowledgeCentre`) | Keeps the artefacts and tales visitors bring in a JSON lines file. It starts with Indian Jataka tales and the Tibetan tale of the monkey and the rock ogress. |

Personal details (birthplace, country, visa state) are used only to greet the visitor and make the pass id.
They aren't written anywhere: the knowledge centre stores only the pass id next to what was deposited.

Places live in `places.py`, and their coordinates are approximate. Add more there to widen the window.
