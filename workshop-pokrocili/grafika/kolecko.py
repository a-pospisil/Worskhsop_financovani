"""Generuje SVG grafiku kolečka pokročilé strategie financování (barvy podle egfin.cz, jako zadání pro Claude Design)."""
import math
from pathlib import Path

BG, CARD, CARD2 = "#06231C", "#0A2E24", "#12453A"
GOLD, CYAN, GREEN, RED = "#D9BE7F", "#B6DCCB", "#238A6C", "#E0951A"
TXT, MUTED = "#FFFFFF", "#B3BDB9"
FONT = "Liberation Sans, Arial, Helvetica, sans-serif"
W, H = 1920, 1080


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=24, color=TXT, weight="normal", anchor="start", spacing=0):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" '
            f'font-weight="{weight}" text-anchor="{anchor}"{ls}>{esc(s)}</text>')


def lines(x, y, rows, size=24, color=TXT, weight="normal", anchor="start", lh=1.3):
    return "".join(text(x, y + i * size * lh, r, size, color, weight, anchor) for i, r in enumerate(rows))


def header(kicker, title):
    return (text(90, 100, kicker, 22, GOLD, "bold", spacing=4)
            + text(90, 162, title, 54, "#FFFFFF", "bold"))


def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" fill="{BG}"/>'
            '<defs><marker id="aw" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="30" markerHeight="30" markerUnits="userSpaceOnUse" '
            f'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{GOLD}"/></marker>'
            '<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{GOLD}"/></marker>'
            '<marker id="ahc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{CYAN}"/></marker></defs>'
            f'{body}</svg>')


def kolecko():
    cx, cy, r = 640, 620, 330
    b = [header("POKROČILÁ STRATEGIE FINANCOVÁNÍ", "Kolečko FO ↔ PO")]
    # prstenec a šipky po směru hodinových ručiček
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{CARD2}" stroke-width="26"/>')
    for a0 in (-90, 0, 90, 180):
        a1, a2 = math.radians(a0 + 24), math.radians(a0 + 66)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        b.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {x2:.1f},{y2:.1f}" fill="none" '
                 f'stroke="{GOLD}" stroke-width="10" stroke-linecap="round" marker-end="url(#aw)"/>')
    # střed
    b.append(f'<circle cx="{cx}" cy="{cy}" r="150" fill="{CARD}" stroke="{GOLD}" stroke-width="3"/>')
    b.append(text(cx, cy - 42, "OPAKUJ", 34, GOLD, "bold", "middle", 4))
    b.append(lines(cx, cy + 2, ["dokud nedojde", "bonita PO", "nebo volná zástava"], 24, TXT, "normal", "middle"))
    nodes = [
        (cx, cy - r, "1", "Zástava FO", ["FO dá volnou nemovitost", "do zástavy za úvěr firmy"], CYAN),
        (cx + r, cy, "2", "Úvěr PO", ["s.r.o. s bonitou čerpá", "podnikatelský úvěr"], GOLD),
        (cx, cy + r, "3", "Zápůjčka PO → FO", ["vždy za tržní úrok,", "ne vyvádění peněz"], GREEN),
        (cx - r, cy, "4", "Nákup na FO", ["další nemovitost na FO", "= nová zástava"], CYAN),
    ]
    cw, ch = 380, 150
    for x, y, n, t, sub, col in nodes:
        b.append(f'<rect x="{x - cw / 2}" y="{y - ch / 2}" width="{cw}" height="{ch}" rx="16" fill="{CARD}" '
                 f'stroke="{col}" stroke-width="3"/>')
        b.append(f'<circle cx="{x - cw / 2 + 44}" cy="{y - 28}" r="24" fill="{col}"/>')
        b.append(text(x - cw / 2 + 44, y - 19, n, 26, BG, "bold", "middle"))
        b.append(text(x - cw / 2 + 84, y - 18, t, 30, "#FFFFFF", "bold"))
        b.append(lines(x - cw / 2 + 28, y + 24, sub, 22, MUTED))
    # pravý panel
    px, py, pw = 1230, 250, 600
    b.append(f'<rect x="{px}" y="{py}" width="{pw}" height="720" rx="16" fill="{CARD}" stroke="{CARD2}" stroke-width="2"/>')
    b.append(text(px + 36, py + 60, "PROČ TO FUNGUJE", 22, GOLD, "bold", spacing=3))
    items = [
        ("Bonitu nese firma", ["DSCR / EBITDA s.r.o., ne DTI 7× u FO"]),
        ("Nemovitosti drží FO", ["nejlevnější hypotéky a prodej na FO"]),
        ("Zástava třetí osoby", ["Moneta SBL, Živnohypotéka ji přijmou"]),
    ]
    y = py + 120
    for h, s in items:
        b.append(f'<circle cx="{px + 48}" cy="{y - 9}" r="9" fill="{GREEN}"/>')
        b.append(text(px + 72, y, h, 27, "#FFFFFF", "bold"))
        b.append(lines(px + 72, y + 36, s, 22, MUTED))
        y += 108
    b.append(f'<line x1="{px + 36}" y1="{y - 20}" x2="{px + pw - 36}" y2="{y - 20}" stroke="{CARD2}" stroke-width="2"/>')
    b.append(text(px + 36, y + 30, "PŘÍKLAD · LTV 75 %, 6,8 %, 30 LET", 22, GOLD, "bold", spacing=2))
    ex = [("1. kolo", "6,0 → 4,50 mil. Kč"), ("2. kolo", "4,5 → 3,38 mil. Kč"), ("3. kolo", "3,4 → 2,53 mil. Kč")]
    y += 78
    for k, v in ex:
        b.append(text(px + 36, y, k, 24, MUTED))
        b.append(text(px + pw - 36, y, v, 24, "#FFFFFF", "bold", "end"))
        y += 40
    b.append(text(px + 36, y + 14, "Σ 10,41 mil. Kč · splátka PO 67 841 Kč/měs.", 24, CYAN, "bold"))
    return svg("".join(b))


def box(x, y, w, h, title, sub, col, fill=CARD):
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{col}" stroke-width="3"/>'
           + text(x + w / 2, y + 44, title, 28, "#FFFFFF", "bold", "middle"))
    return out + lines(x + w / 2, y + 80, sub, 21, MUTED, "normal", "middle")


def arrow(x1, y1, x2, y2, label="", col=GOLD, lx=None, ly=None, anchor="middle"):
    m = "ahc" if col == CYAN else "ah"
    out = (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="5" '
           f'marker-end="url(#{m})"/>')
    if label:
        out += text(lx if lx is not None else (x1 + x2) / 2, ly if ly is not None else (y1 + y2) / 2 - 12,
                    label, 21, col, "bold", anchor)
    return out


def numbered_arrow(x1, y1, x2, y2, n, col=GOLD, t=0.5, dashed=False):
    """Šipka s číslem kroku v kroužku (t = poloha kroužku na šipce 0–1)."""
    m = "ahc" if col == CYAN else "ah"
    dash = ' stroke-dasharray="12,10"' if dashed else ""
    out = (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="5"{dash} '
           f'marker-end="url(#{m})"/>')
    cx, cy = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
    out += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="22" fill="{col}" stroke="{BG}" stroke-width="4"/>'
    out += text(cx, cy + 9, str(n), 24, BG, "bold", "middle")
    return out


def spv():
    b = [header("POKROČILÁ STRATEGIE FINANCOVÁNÍ · 2", "Úskalí kolečka a varianta SPV")]
    # ---- schéma vlevo (x 90–1270) ----
    W_, H_ = 280, 120
    A = (90, 250)      # původní s.r.o.
    B = (520, 250)     # SPV (šířka 320)
    C = (990, 250)     # Moneta
    E = (90, 600)      # nemovitost
    D = (520, 600)     # FO (šířka 320)
    F = (990, 600)     # nájemník
    b.append(box(*A, W_, H_, "Původní s.r.o.", ["má bonitu a historii", "RUČITEL / PŘISTUPITEL"], CYAN))
    b.append(box(*B, 320, H_, "SPV s.r.o.", ["nová firma · DLUŽNÍK", "eviduje úvěr i zápůjčku"], GOLD, CARD2))
    b.append(box(*C, W_, H_, "Moneta", ["SBL · zástava =", "nemovitost FO"], CYAN))
    b.append(box(*E, W_, H_, "Nemovitost", ["koupená na FO", "= nová volná zástava"], GREEN))
    b.append(box(D[0], D[1], 320, H_, "FO (investor)", ["vlastník nemovitostí,", "dává zástavu"], GREEN))
    b.append(box(*F, W_, H_, "Koncový nájemník", ["třetí osoba", "(ne ESSO)"], CYAN))
    # peníze = zlatá, smluvní vztah / nemovitost = mátová
    b.append(numbered_arrow(C[0], 292, B[0] + 320 + 6, 292, 1, GOLD, 0.5))                 # Moneta → SPV úvěr
    b.append(numbered_arrow(B[0] + 320, 330, C[0] - 6, 330, 8, GOLD, 0.5))                 # SPV → Moneta splátka
    b.append(numbered_arrow(A[0] + W_, 310, B[0] - 6, 310, "R", CYAN, 0.5))               # ručení
    b.append(numbered_arrow(B[0] + 60, B[1] + H_, D[0] + 60, D[1] - 6, 2, GOLD, 0.5))     # SPV → FO zápůjčka
    b.append(numbered_arrow(B[0] + 160, B[1] + H_, D[0] + 160, D[1] - 6, 7, GOLD, 0.5))   # SPV → FO nájem
    b.append(numbered_arrow(D[0] + 260, D[1], B[0] + 260, B[1] + H_ + 6, "7", GOLD, 0.5)) # FO → SPV úrok
    b.append(numbered_arrow(D[0], 660, E[0] + W_ + 6, 660, 3, GREEN, 0.5))               # FO → nemovitost koupě
    b.append(numbered_arrow(E[0] + W_ - 40, E[1], B[0] + 20, B[1] + H_ + 6, 4, CYAN, 0.55)) # nemovitost → SPV nájem FO→SPV
    b.append(numbered_arrow(B[0] + 300, B[1] + H_, F[0] + 20, F[1] - 6, 5, CYAN, 0.3))  # SPV → nájemník podnájem
    b.append(numbered_arrow(F[0] + 130, F[1], B[0] + 320 + 6, B[1] + H_ - 20, 6, GOLD, 0.7)) # nájemník → SPV nájemné
    # legenda
    b.append(f'<line x1="90" y1="770" x2="150" y2="770" stroke="{GOLD}" stroke-width="5"/>')
    b.append(text(162, 777, "peníze", 20, TXT))
    b.append(f'<line x1="260" y1="770" x2="320" y2="770" stroke="{CYAN}" stroke-width="5"/>')
    b.append(text(332, 777, "smluvní vztah (ručení, nájem, podnájem)", 20, TXT))
    b.append(f'<line x1="760" y1="770" x2="820" y2="770" stroke="{GREEN}" stroke-width="5"/>')
    b.append(text(832, 777, "nemovitost", 20, TXT))
    # ---- pravý panel: proč SPV ----
    px, py, pw, ph = 1330, 240, 500, 550
    b.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="{CARD}" stroke="{RED}" stroke-width="3"/>')
    b.append(text(px + 32, py + 52, "PROČ SPV, A NE PŮVODNÍ S.R.O.", 21, RED, "bold", spacing=2))
    b.append(lines(px + 32, py + 100, ["Zápůjčka FO je v rozvaze firmy", "pohledávka za společníky."], 25, "#FFFFFF", "bold"))
    b.append(lines(px + 32, py + 176, ["ČSOB i další banky ji FO přičtou", "do splátek → horší DSTI a DTI", "u hypoték na FO."], 22, TXT))
    b.append(lines(px + 32, py + 276, ["„Jiné pohledávky“ banky čím dál", "častěji rozklíčují."], 22, MUTED))
    b.append(f'<line x1="{px + 32}" y1="{py + 330}" x2="{px + pw - 32}" y2="{py + 330}" stroke="{CARD2}" stroke-width="2"/>')
    b.append(text(px + 32, py + 372, "V SPV zůstává úvěr i zápůjčka.", 24, GOLD, "bold"))
    b.append(lines(px + 32, py + 410, ["Původní s.r.o. jen ručí / přistupuje", "k závazku – její výkazy nenesou", "zápůjčku společníkovi."], 22, TXT))
    b.append(lines(px + 32, py + 500, ["Podmínka Monety: obrat SPV ≥ 2× splátka", "od třetích osob → řeší krok 6."], 22, CYAN))
    # ---- spodní pás: kroky ----
    steps = [
        ("1", "Moneta půjčí SPV", "zástava = nemovitost FO · R = ručení s.r.o."),
        ("2", "SPV půjčí FO", "zápůjčka vždy za tržní úrok"),
        ("3", "FO koupí nemovitost", "na sebe → nová volná zástava"),
        ("4", "FO ji pronajme SPV", "nájemní smlouva FO → SPV"),
        ("5", "SPV ji podnajme", "koncovému nájemníkovi (nižší ochrana)"),
        ("6", "Nájemník platí SPV", "nájemné = obrat od třetí osoby"),
        ("7", "SPV platí FO nájem", "FO platí SPV úrok ze zápůjčky"),
        ("8", "SPV splácí Monetě", "z nájemného; výhled: depozit 3–6 splátek"),
    ]
    x0, y0, cw, ch = 90, 810, 425, 96
    for i, (n, h, sub) in enumerate(steps):
        x = x0 + (i % 4) * (cw + 13)
        y = y0 + (i // 4) * (ch + 12)
        b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="{CARD}" stroke="{CARD2}" stroke-width="2"/>')
        b.append(f'<circle cx="{x + 34}" cy="{y + 36}" r="20" fill="{GOLD}"/>')
        b.append(text(x + 34, y + 44, n, 22, BG, "bold", "middle"))
        b.append(text(x + 66, y + 42, h, 22, "#FFFFFF", "bold"))
        b.append(text(x + 66, y + 74, sub, 18, MUTED))
    b.append(text(90, 1050, "Ilustrativní schéma – konkrétní strukturu ověřit s bankou a daňovým poradcem (převodní ceny, tržní úrok zápůjčky).", 18, MUTED))
    return svg("".join(b))


if __name__ == "__main__":
    out = Path(__file__).parent
    (out / "kolecko-strategie.svg").write_text(kolecko(), encoding="utf-8")
    (out / "kolecko-spv.svg").write_text(spv(), encoding="utf-8")
