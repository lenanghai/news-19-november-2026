"""Build entry.png: front page of world news for Thursday 19 November 2026.

Layout: dated masthead, a large lead story (the Trump-Xi-Putin summit),
10 illustrated story cards, a labelled world map with numbered pins, and
one-line briefs by region. Run locally (needs Pillow and Windows fonts):
python build.py. Sources for every item are listed in SOURCES.md.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONTS = "C:/Windows/Fonts/"
INK = (22, 22, 26)
PAPER = (244, 240, 230)
CARD = (255, 254, 249)
RED = (180, 28, 36)
NAVY = (20, 44, 86)
GREY = (88, 86, 84)
SEA = (194, 218, 236)
LAND = (220, 205, 160)
WHITE = (255, 255, 255)
SKIN = (232, 192, 152)


def font(name, size):
    return ImageFont.truetype(FONTS + name, size)


F_MAST = font("georgiab.ttf", 44)
F_DATE = font("arialbd.ttf", 21)
F_TAG = font("arialbd.ttf", 13)
F_HEAD = font("arialbd.ttf", 19)
F_HERO = font("arialbd.ttf", 26)
F_SUB = font("arial.ttf", 13)
F_HSUB = font("arial.ttf", 15)
F_REG = font("arialbd.ttf", 13)
F_BRIEF = font("arial.ttf", 12)
F_PIN = font("arialbd.ttf", 12)
F_MAPL = font("arialbd.ttf", 10)
F_NAME = font("arialbd.ttf", 11)
F_FOOT = font("arial.ttf", 12)

HERO = ("CHINA · FIRST US-CHINA-RUSSIA SUMMIT", "SHENZHEN",
        "Trump, Xi and Putin sign a 'peace declaration'",
        "Nuclear risk, oil, UN reform, ICC limits; Ukraine not named",
        (114, 22))

# (tag, big fact, headline, subline, icon, panel colour, (lon, lat) for the map pin)
CARDS = [
    ("WORLD COURT", "GENOCIDE", "ICJ rules Myanmar committed genocide",
     "Against the Rohingya in 2017", "gavel", (232, 226, 240), (96, 20)),
    ("WALL STREET", "-2.0%", "S&P 500 falls for a sixth straight day",
     "Dow -1,101 to 49,097; AI stocks slide", "chart", (232, 232, 232), (-74, 41)),
    ("TECH · IPO", "+34%", "Anthropic soars in record Nasdaq debut",
     "Valued near $1.5 trillion", "rocket", (226, 236, 246), (-122, 37)),
    ("UKRAINE · RUSSIA", "3RD HIT", "Ukraine strikes Crimea bridge again",
     "Rail halted; Putin vows response", "bridge", (226, 234, 242), (36, 45)),
    ("GAMING", "17M", "GTA VI launches after 13-year wait",
     "Over 17 million copies sold", "pad", (246, 230, 238), (-80, 26)),
    ("GAZA", "YELLOW LINE", "Israeli tanks push deeper into Gaza",
     "Thousands of Palestinians flee again", "tank", (240, 226, 196), (34, 31)),
    ("COP31 · TURKIYE", "NO FOSSILS", "Fossil fuels cut from COP31 draft",
     "Climate talks near their end in Antalya", "globe", (226, 240, 222), (31, 37)),
    ("COLOMBIA", "STRIKE", "National strike against tax reform",
     "President warns against roadblocks", "protest", (246, 236, 216), (-74, 4)),
    ("ARCTIC", "PACT", "Denmark approves Greenland pact with US",
     "Danish MPs back security deal", "ice", (222, 236, 246), (-42, 72)),
    ("NIGERIA", "36 OF 36", "All Nigerian states back state police",
     "Amendment now needs Tinubu's assent", "police", (226, 238, 226), (8, 9)),
]

BRIEFS = [
    ("EUROPE", ["Leaders reject 'Yalta 2.0' Ukraine deal", "UK inflation at 12-month high",
                "EU Commission hit by cyberattack", "Court bars Imamoglu from 2028 race",
                "Van Gogh sells for $173m"]),
    ("N. AMERICA", ["Democrats pick Jeffries for Speaker", "DHS chief grilled over FAA ground stop",
                    "Sheinbaum seeks US trade deal", "Measles spreading again in US",
                    "Trump: no rush on Iran decision"]),
    ("LATIN AM.", ["Hegseth lands in Ecuador", "Brazil's real at 19-month low",
                   "Lula nears finance minister pick", "Hegseth ties with Colombia",
                   "Sheinbaum flies home for parade"]),
    ("MIDEAST", ["Iran attacks on Hormuz ships escalate", "Israel strikes Hezbollah in Lebanon",
                 "Houthis threaten Saudi targets", "Gaza doctor's detention extended",
                 "Iraq orders militias out of area"]),
    ("AFRICA", ["Ghana defends $61m presidential jet", "74.6% of Malawi water contaminated",
                "Migrant boat capsizes off Senegal", "Africa alliance on misinformation",
                "Nigeria, Kenya ease travel talks"]),
    ("S. ASIA", ["Violent protests in Bangladesh", "Japan, India deepen defence ties",
                 "Pakistan backs new security setup", "Hasina's planned return stirs unrest"]),
    ("ASIA-PAC", ["Takaichi meets Putin, first in 7 years", "Takaichi leaves without Xi talks",
                  "Lee urges North Korea dialogue", "IAEA: N. Korea expands enrichment"]),
]

CONTINENTS = [
    [(-168, 66), (-140, 70), (-95, 72), (-80, 62), (-60, 50), (-80, 30), (-81, 25), (-97, 18), (-105, 22),
     (-117, 32), (-125, 48), (-150, 60)],
    [(-55, 60), (-20, 70), (-30, 82), (-70, 78)],
    [(-80, 10), (-60, 8), (-35, -7), (-40, -22), (-58, -38), (-70, -55), (-75, -40), (-72, -15), (-81, -3)],
    [(-10, 36), (-9, 44), (-5, 48), (5, 52), (8, 57), (25, 70), (40, 68), (45, 45), (28, 40), (15, 38)],
    [(-6, 50), (2, 51), (-3, 59), (-7, 56)],
    [(-17, 15), (-5, 35), (10, 37), (32, 31), (43, 12), (51, 11), (40, -15), (32, -28), (20, -35), (12, -18),
     (9, 4), (-8, 5)],
    [(45, 45), (40, 68), (70, 73), (110, 76), (140, 72), (170, 66), (142, 50), (122, 30), (108, 20), (100, 8),
     (80, 8), (72, 20), (57, 25), (48, 30), (35, 32), (28, 40)],
    [(114, -22), (130, -12), (142, -11), (153, -27), (146, -39), (135, -34), (115, -34)],
    [(130, 31), (141, 36), (142, 43), (138, 38)],
]
MAP_LABELS = [("N. AMERICA", (-110, 52)), ("S. AMERICA", (-60, -25)), ("EUROPE", (18, 62)),
              ("AFRICA", (20, -8)), ("ASIA", (95, 58)), ("OCEANIA", (134, -30))]

WARN = []


def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def fit(d, text, name, size, width):
    while size > 12 and d.textlength(text, font=font(name, size)) > width:
        size -= 1
    return font(name, size)


def star(d, cx, cy, r, fill):
    pts = []
    for k in range(10):
        rr = r if k % 2 == 0 else r * 0.42
        a = -math.pi / 2 + math.pi * k / 5
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=fill)


# ---------- flags ----------

def flag_china(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16), outline=INK)
    star(d, x + w * 0.24, y + h * 0.34, h * 0.24, (255, 222, 0))


def flag_us(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=WHITE)
    hh = h / 7
    for k in range(0, 7, 2):
        d.rectangle([x, y + k * hh, x + w, y + (k + 1) * hh], fill=RED)
    d.rectangle([x, y, x + w * 0.42, y + 4 * hh], fill=NAVY)
    d.rectangle([x, y, x + w, y + h], outline=INK)


def flag_russia(d, x, y, w, h):
    for k, col in enumerate([WHITE, (0, 57, 166), (213, 43, 30)]):
        d.rectangle([x, y + k * h / 3, x + w, y + (k + 1) * h / 3], fill=col)
    d.rectangle([x, y, x + w, y + h], outline=INK)


# ---------- lead illustration: three leaders at one table ----------

def leader(d, cx, base, suit, tie, hair):
    d.rectangle([cx - 15, base - 50, cx + 15, base], fill=suit, outline=INK, width=2)
    d.polygon([(cx - 4, base - 50), (cx + 4, base - 50), (cx, base - 30)], fill=tie)
    d.ellipse([cx - 13, base - 78, cx + 13, base - 50], fill=SKIN, outline=INK, width=2)
    d.chord([cx - 13, base - 80, cx + 13, base - 58], 180, 360, fill=hair)


def hero_art(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 222, 200))
    d.rectangle([x, y, x + w, y + h * 0.46], fill=(196, 40, 40))
    for k in range(5):
        d.line([x + 10 + k * w / 5, y + h * 0.46, x + 30 + k * w / 5, y + 6], fill=(170, 30, 30), width=3)
    # three flags on the back wall
    for k, fl in enumerate([flag_us, flag_china, flag_russia]):
        fx = x + w * (0.2 + 0.3 * k) - 20
        d.line([fx, y + 8, fx, y + h * 0.5], fill=INK, width=2)
        fl(d, fx + 2, y + 10, 40, 25)
    # leaders seated behind the table
    tb = y + h * 0.74
    for k, (nm, suit, tie, hair) in enumerate([("TRUMP", NAVY, RED, (232, 200, 120)),
                                               ("XI", (40, 40, 48), RED, (30, 30, 30)),
                                               ("PUTIN", (60, 60, 70), (40, 60, 120), (170, 150, 120))]):
        cx = x + w * (0.2 + 0.3 * k)
        leader(d, cx, tb, suit, tie, hair)
        d.rounded_rectangle([cx - 24, tb + 6, cx + 24, tb + 20], radius=3, fill=WHITE, outline=INK)
        d.text((cx, tb + 13), nm, font=F_NAME, fill=INK, anchor="mm")
    d.rectangle([x + 4, tb - 2, x + w - 4, tb + 4], fill=(120, 80, 50))
    d.rectangle([x + 4, tb + 22, x + w - 4, y + h - 4], fill=(150, 100, 60), outline=INK)
    # the declaration document
    d.rectangle([x + w * 0.42, tb + 28, x + w * 0.58, y + h - 8], fill=WHITE, outline=INK)
    for k in range(3):
        d.line([x + w * 0.44, tb + 34 + k * 6, x + w * 0.56, tb + 34 + k * 6], fill=GREY, width=1)
    d.rectangle([x, y, x + w, y + h], outline=INK, width=2)


# ---------- card icons: each drawn inside box (x, y, s) ----------

def icon_gavel(d, x, y, s):
    d.rectangle([x + s * 0.1, y + s * 0.78, x + s * 0.9, y + s * 0.92], fill=(120, 80, 50), outline=INK)
    d.line([x + s * 0.3, y + s * 0.7, x + s * 0.8, y + s * 0.2], fill=(140, 95, 60), width=7)
    cx, cy = x + s * 0.32, y + s * 0.34
    d.polygon([(cx - 22, cy - 6), (cx - 6, cy - 22), (cx + 18, cy + 2), (cx + 2, cy + 18)], fill=(110, 70, 40),
              outline=INK)
    d.text((x + s * 0.72, y + s * 0.62), "ICJ", font=font("arialbd.ttf", 15), fill=NAVY, anchor="mm")


def icon_chart(d, x, y, s):
    d.rectangle([x + 2, y + 2, x + s - 2, y + s - 2], fill=WHITE, outline=INK, width=2)
    for k in range(1, 4):
        d.line([x + 4, y + s * k / 4, x + s - 4, y + s * k / 4], fill=(220, 220, 220))
    pts = [(x + 8, y + s * 0.2), (x + s * 0.25, y + s * 0.3), (x + s * 0.4, y + s * 0.36),
           (x + s * 0.55, y + s * 0.5), (x + s * 0.7, y + s * 0.6), (x + s * 0.85, y + s * 0.72),
           (x + s - 10, y + s * 0.86)]
    d.line(pts, fill=RED, width=5)
    ex, ey = pts[-1]
    d.polygon([(ex - 4, ey + 9), (ex + 9, ey - 5), (ex - 12, ey - 8)], fill=RED)


def icon_rocket(d, x, y, s):
    d.rectangle([x + 2, y + 2, x + s - 2, y + s - 2], fill=(20, 30, 60))
    for k in range(6):
        d.ellipse([x + 8 + k * 12, y + 8 + (k * 17) % 50, x + 10 + k * 12, y + 10 + (k * 17) % 50], fill=WHITE)
    cx, cy = x + s * 0.55, y + s * 0.45
    d.polygon([(cx + 24, cy - 24), (cx - 4, cy - 10), (cx - 12, cy + 12), (cx + 10, cy + 4)], fill=WHITE,
              outline=INK)
    d.ellipse([cx + 4, cy - 14, cx + 14, cy - 4], fill=(80, 150, 220), outline=INK)
    d.polygon([(cx - 12, cy + 12), (cx - 30, cy + 30), (cx - 6, cy + 18)], fill=(245, 150, 30))
    d.line([x + 8, y + s - 10, x + s * 0.3, y + s * 0.62], fill=(90, 200, 120), width=4)


def icon_bridge(d, x, y, s):
    d.rectangle([x + 2, y + s * 0.6, x + s - 2, y + s - 2], fill=(80, 140, 200))
    d.rectangle([x + 2, y + s * 0.42, x + s * 0.42, y + s * 0.5], fill=GREY, outline=INK)
    d.rectangle([x + s * 0.58, y + s * 0.42, x + s - 2, y + s * 0.5], fill=GREY, outline=INK)
    for px in (0.15, 0.85):
        d.rectangle([x + s * px - 4, y + s * 0.5, x + s * px + 4, y + s * 0.95], fill=GREY, outline=INK)
    pts = []
    for k in range(14):
        r = s * (0.2 if k % 2 == 0 else 0.09)
        a = math.pi * 2 * k / 14
        pts.append((x + s * 0.5 + r * math.cos(a), y + s * 0.4 + r * math.sin(a)))
    d.polygon(pts, fill=(245, 150, 30), outline=RED)


def icon_pad(d, x, y, s):
    d.rounded_rectangle([x + 4, y + s * 0.3, x + s - 4, y + s * 0.78], radius=16, fill=(40, 40, 46), outline=INK)
    d.rectangle([x + s * 0.18, y + s * 0.48, x + s * 0.34, y + s * 0.54], fill=WHITE)
    d.rectangle([x + s * 0.23, y + s * 0.43, x + s * 0.29, y + s * 0.59], fill=WHITE)
    for dx, dy, col in ((0.7, 0.44, (230, 70, 70)), (0.8, 0.52, (70, 170, 230)), (0.6, 0.52, (90, 200, 120)),
                        (0.7, 0.6, (240, 200, 60))):
        d.ellipse([x + s * dx - 5, y + s * dy - 5, x + s * dx + 5, y + s * dy + 5], fill=col)
    d.text((x + s / 2, y + s * 0.16), "VI", font=font("georgiab.ttf", 22), fill=(230, 60, 140), anchor="mm")


def icon_tank(d, x, y, s):
    d.rectangle([x + 4, y + s * 0.5, x + s - 4, y + s * 0.74], fill=(95, 105, 70), outline=INK, width=2)
    d.rectangle([x + s * 0.26, y + s * 0.32, x + s * 0.64, y + s * 0.51], fill=(110, 120, 80), outline=INK, width=2)
    d.line([x + s * 0.6, y + s * 0.4, x + s - 1, y + s * 0.3], fill=INK, width=5)
    for k in range(5):
        wx = x + 12 + k * (s - 24) / 4
        d.ellipse([wx - 6, y + s * 0.74 - 4, wx + 6, y + s * 0.74 + 8], fill=GREY, outline=INK)
    d.line([x, y + s * 0.95, x + s, y + s * 0.95], fill=(230, 190, 40), width=5)


def icon_globe(d, x, y, s):
    cx, cy, r = x + s * 0.42, y + s / 2, s * 0.38
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(80, 150, 210), outline=INK, width=2)
    d.polygon([(cx - r * 0.6, cy - r * 0.4), (cx - r * 0.1, cy - r * 0.6), (cx, cy), (cx - r * 0.5, cy + r * 0.3)],
              fill=(90, 160, 80))
    d.polygon([(cx + r * 0.2, cy + r * 0.1), (cx + r * 0.7, cy - r * 0.1), (cx + r * 0.5, cy + r * 0.6)],
              fill=(90, 160, 80))
    bx, by = x + s * 0.78, y + s * 0.62
    d.rectangle([bx - 10, by - 18, bx + 10, by + 14], fill=(40, 40, 44), outline=INK)
    d.line([bx - 22, by - 30, bx + 22, by + 26], fill=RED, width=6)


def icon_protest(d, x, y, s):
    for k, col in enumerate([(200, 60, 60), (60, 90, 170), (230, 180, 40)]):
        cx = x + s * (0.22 + 0.28 * k)
        d.ellipse([cx - 8, y + s * 0.5, cx + 8, y + s * 0.5 + 16], fill=SKIN, outline=INK)
        d.rectangle([cx - 10, y + s * 0.5 + 17, cx + 10, y + s - 4], fill=col, outline=INK)
    d.line([x + s * 0.5, y + s * 0.5, x + s * 0.5, y + s * 0.12], fill=INK, width=3)
    d.rectangle([x + s * 0.18, y + 4, x + s * 0.82, y + s * 0.3], fill=WHITE, outline=INK, width=2)
    d.text((x + s * 0.5, y + s * 0.17), "NO TAX", font=font("arialbd.ttf", 12), fill=RED, anchor="mm")


def icon_ice(d, x, y, s):
    d.rectangle([x + 2, y + s * 0.6, x + s - 2, y + s - 2], fill=(70, 120, 180))
    d.polygon([(x + 8, y + s * 0.62), (x + s * 0.3, y + s * 0.2), (x + s * 0.55, y + s * 0.42),
               (x + s * 0.75, y + s * 0.15), (x + s - 6, y + s * 0.62)], fill=WHITE, outline=(140, 170, 200))
    fx, fy = x + s * 0.18, y + s * 0.66
    d.rectangle([fx, fy, fx + 26, fy + 16], fill=(200, 16, 46))
    d.rectangle([fx + 8, fy, fx + 12, fy + 16], fill=WHITE)
    d.rectangle([fx, fy + 6, fx + 26, fy + 10], fill=WHITE)
    flag_us(d, x + s * 0.58, y + s * 0.66, 26, 16)


def icon_police(d, x, y, s):
    cx, cy = x + s / 2, y + s * 0.52
    pts = [(cx, cy - s * 0.42), (cx + s * 0.36, cy - s * 0.26), (cx + s * 0.3, cy + s * 0.2),
           (cx, cy + s * 0.42), (cx - s * 0.3, cy + s * 0.2), (cx - s * 0.36, cy - s * 0.26)]
    d.polygon(pts, fill=(0, 135, 81), outline=INK)
    star(d, cx, cy - 2, s * 0.2, WHITE)
    d.text((cx, cy + s * 0.24), "36", font=font("arialbd.ttf", 13), fill=WHITE, anchor="mm")


ICONS = dict(gavel=icon_gavel, chart=icon_chart, rocket=icon_rocket, bridge=icon_bridge, pad=icon_pad,
             tank=icon_tank, globe=icon_globe, protest=icon_protest, ice=icon_ice, police=icon_police)


def draw_map(d, x0, y0, w, h, pins):
    lon0, lon1, lat0, lat1 = -170, 180, -50, 80

    def p(lon, lat):
        return (x0 + (lon - lon0) / (lon1 - lon0) * w, y0 + (lat1 - lat) / (lat1 - lat0) * h)
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=SEA, outline=INK, width=2)
    for poly in CONTINENTS:
        d.polygon([p(a, b) for a, b in poly], fill=LAND, outline=(150, 135, 100))
    for name, ll in MAP_LABELS:
        d.text(p(*ll), name, font=F_MAPL, fill=(120, 105, 70), anchor="mm")
    placed = []
    for num, ll in pins:
        px, py = p(*ll)
        for _ in range(6):  # nudge a pin that would overlap an earlier one
            if all(math.hypot(px - qx, py - qy) >= 19 for qx, qy in placed):
                break
            py += -19 if py > y0 + 30 else 19
        placed.append((px, py))
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED, outline=WHITE, width=2)
        d.text((px, py), str(num), font=F_PIN, fill=WHITE, anchor="mm")


def tag_bar(d, x, y, w, num, tag):
    d.rectangle([x, y, x + w, y + 20], fill=NAVY)
    d.ellipse([x + 4, y + 2, x + 20, y + 18], fill=RED)
    d.text((x + 12, y + 10), str(num), font=F_TAG, fill=WHITE, anchor="mm")
    d.text((x + 26, y + 10), tag, font=F_TAG, fill=WHITE, anchor="lm")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    d.rectangle([0, 0, W, 56], fill=INK)
    d.text((W / 2, 29), "THE DAY'S WORLD NEWS", font=F_MAST, fill=PAPER, anchor="mm")
    d.rectangle([0, 56, W, 82], fill=RED)
    d.text((W / 2, 69), "THURSDAY, 19 NOVEMBER 2026  ·  ONE PAGE, SEVEN REGIONS", font=F_DATE,
           fill=WHITE, anchor="mm")

    top, gap, ch = 88, 6, 200
    cw = (W - 16 - 3 * gap) / 4

    # lead story spans two columns of the first row
    hw = 2 * cw + gap
    d.rectangle([8, top, 8 + hw, top + ch], fill=CARD, outline=INK, width=2)
    tag_bar(d, 8, top, hw, 1, HERO[0])
    hero_art(d, 12, top + 24, 250, ch - 28)
    tx, tw = 270, 8 + hw - 270 - 6
    d.text((tx, top + 26), HERO[1], font=fit(d, HERO[1], "arialbd.ttf", 34, tw), fill=RED)
    ty = top + 64
    for ln in wrap(d, HERO[2], F_HERO, tw):
        d.text((tx, ty), ln, font=F_HERO, fill=INK)
        ty += 29
    sl = wrap(d, HERO[3], F_HSUB, tw)
    sy = top + ch - 8 - 18 * len(sl)
    if sy < ty:
        WARN.append("OVERLAP: lead story")
    for ln in sl:
        d.text((tx, sy), ln, font=F_HSUB, fill=GREY)
        sy += 18

    slots = [(2, 0), (3, 0)] + [(c, r) for r in (1, 2) for c in range(4)]
    for i, ((tag, fact, head, sub, ic, panel, _), (col, row)) in enumerate(zip(CARDS, slots)):
        cx = 8 + col * (cw + gap)
        cy = top + row * (ch + gap)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=CARD, outline=INK, width=2)
        tag_bar(d, cx, cy, cw, i + 2, tag)
        d.rounded_rectangle([cx + 5, cy + 25, cx + 91, cy + 109], radius=8, fill=panel)
        ICONS[ic](d, cx + 8, cy + 27, 80)
        ff = fit(d, fact, "arialbd.ttf", 30, cw - 102)
        d.text((cx + 94 + (cw - 98) / 2, cy + 67), fact, font=ff, fill=RED, anchor="mm")
        lines = wrap(d, head, F_HEAD, cw - 12)
        if len(lines) > 3:
            WARN.append(f"WRAP: card {i + 2} headline {len(lines)} lines")
        ty = cy + 114
        for ln in lines:
            d.text((cx + 6, ty), ln, font=F_HEAD, fill=INK)
            ty += 22
        sl = wrap(d, sub, F_SUB, cw - 12)
        if len(sl) > 1:
            WARN.append(f"WRAP: card {i + 2} subline {len(sl)} lines")
        if cy + ch - 20 < ty:
            WARN.append(f"OVERLAP: card {i + 2}")
        d.text((cx + 6, cy + ch - 20), sl[0], font=F_SUB, fill=GREY)

    # bottom: map (left) and briefs (right)
    by = top + 3 * ch + 2 * gap + 6
    bh = H - 26 - by
    mw = 400
    d.text((8, by), "WHERE THE 11 LEAD STORIES HAPPENED", font=F_REG, fill=RED)
    pins = [(1, HERO[4])] + [(i + 2, c[6]) for i, c in enumerate(CARDS)]
    draw_map(d, 8, by + 18, mw, bh - 20, pins)

    bx = mw + 18
    d.text((bx, by), "MORE NEWS FROM 19 NOVEMBER, BY REGION", font=F_REG, fill=RED)
    rh = (bh - 18) / len(BRIEFS)
    n = 1 + len(CARDS)
    for k, (reg, items) in enumerate(BRIEFS):
        ry = by + 18 + k * rh
        d.rectangle([bx, ry + 2, bx + 82, ry + rh - 3], fill=NAVY)
        d.text((bx + 41, ry + rh / 2), reg, font=F_REG, fill=WHITE, anchor="mm")
        lines = wrap(d, "  •  ".join(items), F_BRIEF, W - 8 - bx - 90)
        if len(lines) > 2:
            WARN.append(f"WRAP: briefs {reg} {len(lines)} lines")
        ly = ry + rh / 2 - 7.5 * len(lines)
        for ln in lines:
            d.text((bx + 90, ly), ln, font=F_BRIEF, fill=INK)
            ly += 15
        n += len(items)
        d.line([bx, ry + rh - 1, W - 8, ry + rh - 1], fill=(200, 192, 175), width=1)

    # footer
    d.rectangle([0, H - 22, W, H], fill=INK)
    d.text((W / 2, H - 11), f"DATE CHECK: Thursday 19 Nov 2026 · {n} stories, 7 regions · Sources: AP, "
           "Guardian, Euronews, Democracy Now!, Kyodo, allAfrica, Reuters, NPR",
           font=F_FOOT, fill=PAPER, anchor="mm")

    assert n >= 40, n
    img.save("entry.png", optimize=True)
    print("stories:", n)
    for w in WARN:
        print(w)


if __name__ == "__main__":
    main()
