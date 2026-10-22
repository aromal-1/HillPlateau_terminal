"""Places the window can open onto. Coordinates are approximate (to ~1 km)."""
from dataclasses import dataclass

RESEARCH, MONASTERY, TEMPLE, FOLK = "research_center", "monastery", "temple", "folk"


@dataclass(frozen=True)
class Place:
    name: str
    kind: str
    lat: float
    lon: float
    country: str
    buddhist: bool = True


PLACES = [
    Place("Visva-Bharati, Santiniketan", RESEARCH, 23.68, 87.68, "India", buddhist=False),
    Place("Nalanda Mahavihara", RESEARCH, 25.137, 85.444, "India"),
    Place("Central Institute of Higher Tibetan Studies, Sarnath", RESEARCH, 25.375, 83.02, "India"),
    Place("Library of Tibetan Works and Archives, Dharamshala", RESEARCH, 32.224, 76.326, "India"),
    Place("Mahabodhi Temple, Bodh Gaya", TEMPLE, 24.696, 84.991, "India"),
    Place("Dhamek Stupa, Sarnath", TEMPLE, 25.381, 83.024, "India"),
    Place("Tsuglagkhang Complex, McLeod Ganj", TEMPLE, 32.233, 76.324, "India"),
    Place("Namdroling Monastery, Bylakuppe", MONASTERY, 12.43, 75.97, "India"),
    Place("Rumtek Monastery, Sikkim", MONASTERY, 27.288, 88.561, "India"),
    Place("Ghum Monastery, Darjeeling", MONASTERY, 27.01, 88.25, "India"),
    Place("Tawang Monastery", MONASTERY, 27.586, 91.857, "India"),
    Place("Hemis Monastery, Ladakh", MONASTERY, 33.913, 77.703, "India"),
    Place("Raghurajpur Heritage Crafts Village, Odisha", FOLK, 19.85, 85.84, "India", buddhist=False),
    Place("Kerala Folklore Museum, Kochi", FOLK, 9.93, 76.30, "India", buddhist=False),
    Place("Jokhang Temple, Lhasa", TEMPLE, 29.653, 91.132, "Tibet"),
    Place("Potala Palace, Lhasa", TEMPLE, 29.658, 91.117, "Tibet"),
    Place("Sera Monastery, Lhasa", MONASTERY, 29.70, 91.133, "Tibet"),
    Place("Tashilhunpo Monastery, Shigatse", MONASTERY, 29.27, 88.866, "Tibet"),
    Place("Boudhanath Stupa, Kathmandu", TEMPLE, 27.721, 85.362, "Nepal"),
    Place("Maya Devi Temple, Lumbini", TEMPLE, 27.469, 83.276, "Nepal"),
    Place("Temple of the Sacred Tooth Relic, Kandy", TEMPLE, 7.294, 80.641, "Sri Lanka"),
    Place("Kagyu Samye Ling, Scotland", MONASTERY, 55.29, -3.19, "United Kingdom"),
    Place("Plum Village, Dordogne", MONASTERY, 44.73, 0.43, "France"),
]
