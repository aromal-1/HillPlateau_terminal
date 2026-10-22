"""python -m monastery_gate --name NAME --lat LAT --lon LON [--visa refugee] [--nights N --nightly RS]"""
import argparse

from . import KnowledgeCentre, Visitor, VisaState, admit, open_window, quote

GATE = r"""
            ˀ
           |||
      /////|||\\\\\
      \-----------/
   §§§|  M A I N  |§§§
   |=||   GATE    ||=|
 __|_||___________||_|__
"""


def main(argv=None):
    ap = argparse.ArgumentParser(prog="monastery_gate")
    ap.add_argument("--name", required=True)
    ap.add_argument("--born", default="")
    ap.add_argument("--country", default="")
    ap.add_argument("--visa", choices=[v.value for v in VisaState], default="other")
    ap.add_argument("--lat", type=float, required=True)
    ap.add_argument("--lon", type=float, required=True)
    ap.add_argument("--nights", type=int, default=0)
    ap.add_argument("--nightly", type=float, default=0.0)
    ap.add_argument("--ledger", default="knowledge_centre.jsonl")
    a = ap.parse_args(argv)

    visitor = Visitor(a.name, a.born, a.country, VisaState(a.visa))
    entry = admit(visitor)
    print(GATE)
    print(f"Welcome, {visitor.name}. Pass {entry['visitor_id']}: admitted ({visitor.visa_state.value}).\n")
    print("Window: nearest places")
    for place, km in open_window(a.lat, a.lon):
        print(f"  {km:7.0f} km  {place.kind:<15} {place.name} ({place.country})")
    q = quote(entry["visitor_id"], a.nights, a.nightly)
    print(f"\nFees: {q['kind']}: accommodation Rs {q['accommodation']:.2f}, "
          f"GST {q['gst_rate']:.0%} Rs {q['gst']:.2f}, total Rs {q['total']:.2f}")
    print("\nKnowledge centre:")
    for t in KnowledgeCentre(a.ledger).artefacts():
        print(f"  [{t['origin']}] {t['title']}")


if __name__ == "__main__":
    main()
