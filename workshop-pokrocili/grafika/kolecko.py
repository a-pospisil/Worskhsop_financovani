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


def spv():
    b = [header("POKROČILÁ STRATEGIE FINANCOVÁNÍ · 2", "Úskalí kolečka a varianta SPV")]
    # levý sloupec – problém
    lx, ly, lw = 90, 230, 520
    b.append(f'<rect x="{lx}" y="{ly}" width="{lw}" height="560" rx="16" fill="{CARD}" stroke="{RED}" stroke-width="3"/>')
    b.append(text(lx + 32, ly + 56, "PROBLÉM V ROZVAZE", 22, RED, "bold", spacing=3))
    b.append(lines(lx + 32, ly + 110, ["Zápůjčka FO je ve výkazech", "firmy jako pohledávka", "za společníky."], 27, "#FFFFFF", "bold"))
    b.append(lines(lx + 32, ly + 240, ["ČSOB i další banky tento", "závazek FO přičtou", "do splátek → horší DSTI/DTI."], 24, TXT))
    b.append(lines(lx + 32, ly + 380, ["Přeúčtovat na „jiné pohledávky“", "lze, ale banky řádek čím dál", "častěji rozklíčují."], 24, MUTED))
    b.append(text(lx + 32, ly + 520, "→ řešení: úvěr a zápůjčka v SPV", 24, GOLD, "bold"))
    # pravá část – schéma
    X0 = 660
    b.append(text(X0, 260, "VARIANTA MONETA: SPV", 22, GOLD, "bold", spacing=3))
    bw, bh = 330, 130
    mat = (X0, 300)
    spvb = (X0 + 430, 300)
    bank = (X0 + 860, 300)
    fo = (X0 + 430, 560)
    ten = (X0 + 860, 560)
    b.append(box(*mat, bw, bh, "Původní s.r.o.", ["má bonitu", "→ ručí za úvěr SPV"], CYAN))
    b.append(box(*spvb, bw, bh, "SPV s.r.o.", ["dlužník, eviduje úvěr", "i zápůjčku"], GOLD, CARD2))
    b.append(box(*bank, 300, bh, "Moneta", ["SBL · zástava", "nemovitosti FO"], CYAN))
    b.append(box(fo[0], fo[1], bw, bh, "FO (investor)", ["vlastní nemovitosti,", "dává zástavu"], GREEN))
    b.append(box(ten[0], ten[1], 300, bh, "Koncový nájemník", ["třetí osoba", "(ne ESSO)"], CYAN))
    # šipky
    b.append(arrow(mat[0] + bw, 365, spvb[0] - 6, 365, "ručení", CYAN, (mat[0] + bw + spvb[0]) / 2, 338))
    b.append(arrow(bank[0], 365, spvb[0] + bw + 6, 365, "úvěr", CYAN, (bank[0] + spvb[0] + bw) / 2, 338))
    b.append(arrow(spvb[0] + 110, 430, fo[0] + 110, 554, "zápůjčka za tržní úrok", GOLD, spvb[0] + 96, 500, "end"))
    b.append(arrow(fo[0] + 220, 554, spvb[0] + 220, 436, "nájem", GOLD, spvb[0] + 236, 500, "start"))
    b.append(arrow(spvb[0] + bw, 420, ten[0] + 10, 556, "podnájem", GOLD, spvb[0] + bw + 90, 470, "start"))
    b.append(arrow(ten[0] + 150, 554, bank[0] + 150, 436, "", CYAN))
    b.append(text(ten[0] + 166, 500, "nájemné = obrat", 21, CYAN, "bold"))
    b.append(text(ten[0] + 166, 526, "SPV od 3. osoby", 21, CYAN, "bold"))
    # spodní pás podmínek
    y0 = 740
    cards = [
        ("OBRAT", ["≥ 2× měsíční splátka na BÚ SPV,", "jen od třetích osob, ne od ESSO"], GOLD),
        ("VÝHLED", ["depozitní účet 3–6 splátek", "→ pak stačí obrat 1× splátka"], CYAN),
        ("BONUS", ["podnájem má nižší ochranu", "nájemníka než přímý nájem"], GREEN),
    ]
    cw = 380
    for i, (h, s, col) in enumerate(cards):
        x = X0 + i * (cw + 20)
        b.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="160" rx="14" fill="{CARD}" stroke="{col}" stroke-width="2"/>')
        b.append(text(x + 26, y0 + 46, h, 22, col, "bold", spacing=3))
        b.append(lines(x + 26, y0 + 90, s, 22, TXT))
    b.append(text(90, 1010, "Moneta: zástava může být nemovitost třetí osoby · zápůjčka PO → FO vždy za tržní úrok · "
                  "ilustrativní schéma, konkrétní strukturu ověřit s bankou a daňovým poradcem", 20, MUTED))
    return svg("".join(b))


if __name__ == "__main__":
    out = Path(__file__).parent
    (out / "kolecko-strategie.svg").write_text(kolecko(), encoding="utf-8")
    (out / "kolecko-spv.svg").write_text(spv(), encoding="utf-8")
