#!/usr/bin/env python3
"""ASCII reformations of HillPlateau_terminal/mount_tapestry.

faux(pi, x) is a "fake pi": the Leibniz partial sum 4 * sum((-1)^k / (2k+1))
over x terms. It zig-zags above and below pi and settles on it, like a
switchback path that climbs to a temple. Every scene below is drawn from it.

    python3 tapestry/faux_pi.py            # all scenes
    python3 tapestry/faux_pi.py curve      # one scene, see SCENES
"""
import itertools
import math
import shutil
import sys


def faux(pi, x):
    """Leibniz partial sum with x terms; tends to pi as x grows."""
    s = 0.0
    for k in range(int(x)):
        s += (-1) ** k / (2 * k + 1)
    return 4 * s if pi else s


TEMPLE = [
    r"         ˀ         ",
    r"        |||        ",
    r"   /////|||\\\\\   ",
    r"   \-----------/   ",
    r"    |(((+++)))|    ",
    r" IIIIIIIIIIIIIIIII ",
    r"  | | | | | | | |  ",
    r" /_______________\ ",
    r" |IIIIIIIIIIIIIII| ",
    r" |  ===========  | ",
    r" [][][][][][][][][]",
]

MINISTER = [  # a minister carrying a pot on his head
    "(_)",
    "\\o/",
    " | ",
    "/ \\",
]

EMPTY_HANDED = [  # a minister still looking for a pot
    "   ",
    " o?",
    "/|\\",
    "/ \\",
]


class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.g = [[" "] * w for _ in range(h)]

    def put(self, x, y, ch):
        if 0 <= x < self.w and 0 <= y < self.h and ch != " ":
            self.g[y][x] = ch

    def text(self, x, y, s):
        for i, ch in enumerate(s):
            self.put(x + i, y, ch)

    def sprite(self, x, y, rows):
        for j, row in enumerate(rows):
            self.text(x, y + j, row)

    def render(self):
        return "\n".join("".join(r).rstrip() for r in self.g)


def scene_curve(n=40, h=15):
    """faux(pi, x) for x = 1..n, with the temple's floor at y = pi."""
    lo, hi = 2.6, 4.05
    c = Canvas(n * 2 + 12, h + 2)
    row = lambda v: round((hi - v) / (hi - lo) * (h - 1))
    for x in range(n * 2):
        c.put(x + 8, row(math.pi), "-")
    c.text(0, row(math.pi), "pi  ")
    c.text(0, row(4.0), "4.0 ")
    c.text(0, row(2.67), "2.67")
    for x in range(1, n + 1):
        c.put(x * 2 + 6, row(faux(math.pi, x)), "*" if x % 2 else "o")
    c.text(8, h, "+" + "-" * (n * 2 - 1))
    c.text(8, h + 1, "x=1" + " " * (n * 2 - 9) + f"x={n}")
    return "faux(pi, x): odd x overshoots (*), even x undershoots (o)\n" + c.render()


def scene_temple():
    return "mount_tapestry, reformed small\n" + "\n".join(TEMPLE)


def hill_height(col, width, peak, plateau=12):
    """Hill with a flat plateau; its flanks step by faux(pi, x) - pi."""
    half = width / 2
    d = max(0.0, abs(col - half) - plateau) / (half - plateau)
    base = peak * (1 - d ** 1.3)
    terrace = (faux(math.pi, 1 + int(d * 10)) - math.pi) * 2 * d
    return max(0.0, base + terrace)


def scene_hill(width=78, peak=12):
    top = len(TEMPLE)
    h = top + peak + 1
    c = Canvas(width, h)
    ground = h - 1
    surface = [ground - round(hill_height(x, width, peak)) for x in range(width)]
    for x, y in enumerate(surface):
        prev = surface[x - 1] if x else y
        c.put(x, y, "/" if y < prev else "\\" if y > prev else "_")
        for yy in range(y + 1, ground):
            if (x * 7 + yy * 3) % 11 == 0:
                c.put(x, yy, ".")
    c.sprite(width // 2 - len(TEMPLE[0]) // 2, min(surface) - top, TEMPLE)
    # ministers on the left slope; the higher ones have found their pots
    for i, x in enumerate((7, 13, 19, 25)):
        feet = min(surface[x:x + 3]) - 1
        c.sprite(x, feet - 3, MINISTER if i >= 2 else EMPTY_HANDED)
    c.text(0, ground, "~" * width)
    return "Visiting the temple: ministers climbing faux(pi, x) hill\n" + c.render()


def scene_procession(count=6):
    rows = [""] * 4
    for i in range(count):
        sprite = MINISTER if faux(math.pi, i + 1) > math.pi else EMPTY_HANDED
        for j in range(4):
            rows[j] += sprite[j] + "   "
    gate = ["  §§|§§", "  |===|", "  |   |", "__|   |__"]
    lines = [r + g for r, g in zip(rows, gate)]
    caption = "x where faux(pi, x) > pi carries a pot; the rest are still trying to get one"
    return "Procession to the gate\n" + "\n".join(lines) + "\n" + caption


RAMP = " .:-=+*#%@"  # pixel coverage, empty to full


def scene_cavern(width=78, height=16):
    """A cavern under the hill, shaded by how much rock covers each cell."""
    c = Canvas(width, height)
    for y in range(height):
        for x in range(width):
            u = (x - width / 2) / (width / 2)
            v = (y - height / 2) / (height / 2)
            # the hollow's edge wobbles by faux(pi, x) - pi along its length
            edge = 0.75 + (faux(math.pi, 2 + int(abs(u) * 14)) - math.pi) * 0.6
            rock = (u * u * 0.8 + v * v * 1.6) / edge
            cover = max(0.0, min(1.0, (rock - 0.55) * 2.2))
            c.put(x, y, RAMP[round(cover * (len(RAMP) - 1))])
    c.sprite(width // 2 - 4, height // 2 - 1, MINISTER[:1] + ["\\o/ (_)", " |      ", "/ \\"])
    return ("Cavern: pixel coverage of rock, @ is solid, blank is hollow\n"
            + c.render() + "\na minister has found a pot hidden in the cavern")


TOWER = ["[]_[]_[]", "|  ..  |", "|  []  |", "|      |", "|  /\\  |", "|_|  |_|"]
WALL = ["       ", "_[]_[]_", "  : :  ", "       ", "  : :  ", "_______"]


def castle_columns():
    """Yields the castle one column at a time, forever: width = Infinity."""
    for k in itertools.count():
        module = TOWER if faux(math.pi, k + 1) > math.pi else WALL
        for i in range(len(module[0])):
            yield [row[i] for row in module]


def scene_castle(width=None):
    width = width or min(shutil.get_terminal_size((80, 24)).columns, 78)
    cols = list(itertools.islice(castle_columns(), width - 4))
    rows = ["".join(col[j] for col in cols) for j in range(len(TOWER))]
    rows = [r + " ..." if j == 3 else r for j, r in enumerate(rows)]
    return ("Castle of width Infinity: towers where faux(pi, x) > pi, walls between\n"
            + "\n".join(rows) + "\n" + "~" * width
            + f"\n(an endless generator, cropped to {width} columns)")


CHANT = "realm of existence"
TENSES = [
    ("past", "was the"),
    ("present", "is the"),
    ("plus-future", "will have been the"),
]


def scene_chant():
    """The chant in every tense, along a rod; each echo fades (de-max)."""
    out = ["Chant along the rod: all tenses, each echo fainter"]
    for name, verb in TENSES:
        line = f"{verb} {CHANT}"
        out.append(f"  ||  [{name}]")
        for echo, ch in enumerate(RAMP[::-1][:4]):
            out.append(f"  ||  {ch * 2} " + " " * (echo * 2) + line)
    out.append(" _||_")
    out.append("|____|  Dev.rod(map.schema): each tense maps one band of the rod")
    return "\n".join(out)


SCENES = {
    "curve": scene_curve,
    "temple": scene_temple,
    "hill": scene_hill,
    "procession": scene_procession,
    "cavern": scene_cavern,
    "castle": scene_castle,
    "chant": scene_chant,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(SCENES)
    print("\n\n".join(SCENES[n]() for n in names))
