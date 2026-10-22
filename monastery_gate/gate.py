"""Admission and the search window."""
import hashlib
import math
from dataclasses import dataclass
from enum import Enum

from .places import PLACES, Place


class VisaState(str, Enum):
    CITIZEN = "citizen"
    TOURIST = "tourist"
    STUDENT = "student"
    REFUGEE = "refugee"
    MIGRANT = "migrant"
    STATELESS = "stateless"
    OTHER = "other"


@dataclass
class Visitor:
    name: str
    birthplace: str = ""
    country: str = ""
    visa_state: VisaState = VisaState.OTHER

    @property
    def visitor_id(self):
        """A stable pass id; the gate records this, not the visitor's details."""
        raw = f"{self.name}|{self.birthplace}|{self.country}".encode()
        return "V-" + hashlib.sha256(raw).hexdigest()[:10].upper()


def admit(visitor):
    """Every visitor is admitted, whatever their visa state."""
    return {"visitor_id": visitor.visitor_id, "admitted": True, "gate": "Main Gate"}


def distance_km(lat1, lon1, lat2, lon2):
    """Great-circle distance (haversine)."""
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(a))


def open_window(lat, lon, places=PLACES, limit=5):
    """The window chain: the nearest place of each kind, then the nearest others.

    Buddhist sites rank first among places at a similar distance (within 25 km).
    """
    ranked = sorted(
        places,
        key=lambda p: (round(distance_km(lat, lon, p.lat, p.lon) / 25), not p.buddhist,
                       distance_km(lat, lon, p.lat, p.lon)),
    )
    chain, kinds = [], set()
    for p in ranked:
        if p.kind not in kinds:
            chain.append(p)
            kinds.add(p.kind)
    chain += [p for p in ranked if p not in chain][: max(0, limit - len(chain))]
    chain.sort(key=lambda p: distance_km(lat, lon, p.lat, p.lon))
    return [(p, distance_km(lat, lon, p.lat, p.lon)) for p in chain[:limit]]
