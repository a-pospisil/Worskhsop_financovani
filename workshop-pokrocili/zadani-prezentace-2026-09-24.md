# Zadání prezentace – Workshop financování pro pokročilé investory

**Termín:** 24. 9. 2026, 18:00–20:30 · **Místo:** Baťův palác, Václavské náměstí 774/6, Praha 1 · **Lektor:** Adam Pospíšil, Evergreen Finance (egfin.cz), adamovyfinance.cz
**Rozsah:** 20 slidů (vč. 12a, 12b), 16:9, česky · **Verze zadání:** 24. 9. 2026, v5 (Credix podle hovoru 24. 9.: slidy 6, 12, 17, nový slide 12b; v4: slide 16 SPV; v3: Home Credit, slide 12a; v2: místo a čas, startup ČS) · **Navazuje na:** `../workshop-zacatecnici/zadani-prezentace-2026-09-23.md` (stejný vizuální systém)

## Jak se zadáním pracovat

- Každý slide má: účel, rozvržení, přesný obsah (texty, čísla, tabulky) a poznámky pro lektora („Lektor říká“).
- Texty a čísla ze sekce „Obsah slidu“ přebírat doslova. „Lektor říká“ patří jen do speaker notes.
- Formát čísel: tisíce s mezerou (20 364 Kč), miliony „mil. Kč“, procenta s mezerou (70 %), desetinná čárka.
- Placeholdery v hranatých závorkách nechat viditelné jako rámeček s popiskem – doplní se ručně.
- Princip obsahu: **ne představování produktů, ale srovnání parametrů – co je kde možné a kde je hranice.**
- Podklady: `grafika/kolecko-strategie.png` a `grafika/kolecko-spv.png` (předloha diagramů pro slidy 14 a 16, stejné barvy jako egfin.cz; SVG zdroj a generátor `grafika/kolecko.py`), fotky a logo z `../workshop-zacatecnici/podklady/fotky/`.

### Prompt pro Claude Design (zkopírovat)

> Vytvoř prezentaci pro živý workshop pro pokročilé investory: 20 slidů (1–12, 12a, 12b, 13–18), 16:9, česky, přesně podle přiloženého souboru zadani-prezentace-2026-09-24.md. Sekce „3. Slidy“ definuje každý slide: titulek, rozvržení, přesný obsah a poznámky pro lektora. Texty a čísla přebírej doslova, nic nepřidávej, nevymýšlej a nezaokrouhluj. Poznámky pro lektora patří jen do speaker notes. Vizuální styl stejný jako u workshopu pro začátečníky podle webu egfin.cz: tmavě zelené titulní, předělové a závěrečné slidy (#06231C, bílý text, akcent světlá zlatá #D9BE7F), světlé obsahové slidy (#FAFAF7 střídavě #F0F2ED) s bílými kartami (ohraničení #E3E7E0, zaoblení 8–12 px, jemný stín), nadpisy #06231C, tlumený text #68746F, zlatá #C9A962 na štítky bloků a čísla kroků, zelená #238A6C jen jako sekundární zvýraznění. Písma: Playfair Display Bold na titulky, Poppins na text, JetBrains Mono na čísla a tabulky. Tabulky srovnání bank jsou hlavní obsah – řádky parametrů, sloupce banky, nejlepší hodnota v řádku zvýrazněná zelenou #238A6C, hranice/omezení varovnou #E0951A. Slidy 14 a 16 jsou diagramy: překresli je nativně podle přiložených obrázků kolecko-strategie.png a kolecko-spv.png (tmavě zelené pozadí, zlaté šipky), texty z nich převezmi doslova. Jeden zlatý akcentní slide (slide 15, kolečko v číslech). Každý slide má vlevo nahoře malý štítek bloku (např. „BLOK 2 · POSLOUPNOST BANK“), titulek 36–40 pt, obsah v kartách, tabulkách nebo velkých číslech; minimální velikost textu 12 pt. Žádné ozdobné pruhy, emoji ani přechody mimo fotku na titulním slidu. Logo mark egfin-icon.svg do patičky každého slidu. Nejdřív mi ukaž slide 6 (matice bank) a slide 14 (kolečko). Po odsouhlasení vygeneruj zbývající slidy ve stejném systému.

### Doplňující prompt pro Claude Design – Home Credit (v3, zkopírovat do rozpracované prezentace)

> Aktualizuj prezentaci podle nové verze zadání (v3, přikládám zadani-prezentace-2026-09-24.md). Měň jen Home Credit, ostatní slidy nech beze změny. 1) Slide 6 (matice bank), sloupec Home Credit: sazba 8,5–10,5 %; max. LTV Praha a Brno 70–75 %, krajská města 65–70 %, komerce 60 %; výše 5–150 mil. Kč na projekt, 200 mil. Kč na skupinu; splatnost max. 20 let, anuitně; bonita 90 % čistého nájmu (bez služeb a fondu oprav), příjmy ESSO přes ručitelskou společnost; poplatky 2 %, max. 80 000 Kč + supervize 15 000 Kč. 2) Slide 12 (Fio, Credix, Home Credit): přepiš sloupec Home Credit a přidej řádek „Bonita“ přesně podle tabulky v zadání; kartu Home Credit změň na „bridge, refinancování + hotovost navíc, refinancování s rekonstrukcí i při dočasném výpadku nájmu, development bez předprodejů (slide 12a)“; speaker notes podle „Lektor říká“. 3) Vlož nový slide 12a „Home Credit: investiční a developerský úvěr“ mezi slide 12 a 13, štítek „BLOK 4 · BANKY“, světlé pozadí: vlevo karta „Investiční úvěr“, vpravo karta „Development“ s procesem čerpání jako 4 číslované kroky se zlatými čísly (fotky a videa stavby → supervize prostavěnosti Air Bank → čerpání druhý den → opakovat do konce stavby), velká čísla 8,5–10,5 % a 8,5–9,5 % v JetBrains Mono, dole pruh „Pravidla splácení“ se zvýrazněním „žádné balony“ zelenou #238A6C. Texty a čísla převezmi doslova ze sekce „Slide 12a“, poznámky pro lektora jen do speaker notes. 4) Slide 17: v kartě Zástava nahraď text o Home Creditu textem „HC: vyvázání jednotky při prodeji – 80 % ceny bez DPH na splátku“. Styl, písma a barvy zachovej stejné jako na ostatních slidech. Ukaž mi nejdřív slide 12a.

### Doplňující prompt pro Claude Design – slide 16 (v4, zkopírovat do rozpracované prezentace)

> Přepracuj slide 16 „Úskalí kolečka a varianta SPV“ podle nové verze zadání (v4, přikládám zadani-prezentace-2026-09-24.md) a podle přiloženého obrázku kolecko-spv.png. Ostatní slidy nech beze změny. Slide je tmavě zelený (#06231C). Vlevo na 2/3 šířky překresli nativně schéma šesti uzlů ve dvou řadách: nahoře Původní s.r.o. (RUČITEL / PŘISTUPITEL), SPV s.r.o. (DLUŽNÍK, zvýrazněný zlatým rámečkem) a Moneta; dole Nemovitost, FO (investor) a Koncový nájemník – texty uzlů převezmi doslova ze zadání. Šipky mezi uzly mají číslo kroku v kroužku a tři barvy: zlatá #D9BE7F = peníze, světlá mátová #B6DCCB = smluvní vztah (ručení, nájem, podnájem), zelená #238A6C = nemovitost; směr a číslování šipek přesně podle seznamu „šipky“ v zadání (R, 1–8), pod schématem legenda barev. Vpravo na 1/3 šířky karta „PROČ SPV, A NE PŮVODNÍ S.R.O.“ s varovným rámečkem #E0951A a textem ze zadání, tučně „V SPV zůstává úvěr i zápůjčka.“. Dole pás osmi kroků ve dvou řadách po čtyřech, každý se zlatým číslem, tučným názvem a jednořádkovým popisem podle tabulky kroků v zadání. Patička slidu podle zadání, poznámky pro lektora jen do speaker notes. Písma, štítek bloku a logo v patičce stejné jako na ostatních slidech. Ukaž mi výsledek.

### Doplňující prompt pro Claude Design – Credix a úpravy po review (v5, zkopírovat do rozpracované prezentace)

> Aktualizuj prezentaci podle zadání v5 (přikládám zadani-prezentace-2026-09-24.md). Ostatní slidy nech beze změny, pokud nejsou níže uvedené.
> 1) Slide „Matice bank: co je kde možné“: sloupec Credix přepiš podle tabulky v zadání (sazba 9–10 %, LTV podle typu, bridge 12–36 měsíců, zástava jen vlastní / skupina / FO společníka, poplatek do 2 %, exit fee do 1 roku 2–3 %, schválení i čerpání ~10 pracovních dnů). Zároveň tabulku zjednoduš: na slidu nech jen řádky Dlužník, Sazba, Max. LTV, Výše úvěru, Splatnost, Zástava 3. osoby; řádky Bonita, Poplatky, Předčasné splacení a Rychlost přesuň do speaker notes. Oprav zarovnání řádku Bonita a zvětši písmo na min. 12 pt.
> 2) Slide „Projektové financování: Fio, Credix, Home Credit“: přepiš sloupec Credix a přidej řádek „Zástava“ podle tabulky v zadání; kartu Credix změň na „bridge 12–36 měsíců na rychlý nákup, činžovní dům → prohlášení vlastníka → rozprodej nebo refinancování, provozní úvěr se zástavou nemovitosti (slide 12b)“. Oprav kolizi titulku s hlavičkou tabulky (titulek nahoře, tabulka začíná pod ním s mezerou) a blok „Kdy použít“ nesmí překrývat logo v patičce.
> 3) Vlož nový slide 12b „Credix: bridge financování“ hned za slide „Home Credit: investiční a developerský úvěr“, štítek „BLOK 5 · STARTUP A PROJEKTOVÉ“, světlé pozadí, stejná struktura jako slide Home Credit: vlevo karta „Bridge 12–36 měsíců“ s velkými čísly 9–10 %, 12–36 měsíců, ~10 pracovních dnů v JetBrains Mono a tokem ve 3 číslovaných krocích se zlatými čísly (Credix zafinancuje nákup → nájmy 6–12 měsíců → refinancování do banky, nejčastěji Moneta); vpravo tabulka LTV podle typu nemovitosti; dole pruh „Zástava a vlastní zdroje“ se zvýrazněním „zástava třetí osoby ne“ varovnou #E0951A. Texty a čísla doslova ze sekce „Slide 12b“, poznámky pro lektora do speaker notes.
> 4) Slide „Zástava, odhad a proces“: v kartě Zástava přidej „Credix: zástava třetí osoby ne – bez protiplnění ji může insolvenční správce zpochybnit“; v kartě Odhad nahraď text o Credixu textem „Credix: odhadci Banky CREDITAS, nad 25 mil. Kč supervize v bance (lze i vlastní bankovní znalec)“; v kartě Proces a čas nahraď „Credix rychlý prescoring“ textem „Credix schválení i čerpání ~10 pracovních dnů“.
> 5) Slide „Shrnutí, diskuze a kontakty“, bod 02: „(ČS) → RB → Moneta → Credix / Home Credit / Fio; bridge Credix → refinancování do Monety.“
> 6) Opravy napříč deckem: znak „↔“ se nevykresluje (titulní slide, slide Kolečko, shrnutí) – nahraď ho textem „FO a PO“ (titulek „Kolečko FO a PO“). Sjednoť sazby Monety na všech slidech na hodnoty ze slidu „Moneta SBL: Mini, Plus, Pro“ (Mini 7 %, Plus a Pro 6,5 %) – tedy i na slidech „Kde končí bonita FO“, „Matice bank“, „Moneta: co je nového“ (splátka 3 mil. Kč při 7 % / 30 let = 19 959 Kč) a „Shrnutí“ bod 03. Slide „PROFIT rezidenční / komerční“ přejmenuj na „Raiffeisenbank: hypotéka na pronájem a DSCR“. Na slidu „Kde končí bonita FO“ oprav „omezeně (čsobs ok)“ na „omezeně (ČSOBS ano)“. Na slidu „Rekapitulace: roadmapa“ odstraň závorky u „(Modrá pyramida)“ a „(Partners banka)“, nebo je vysvětli v poznámce. V matici bank sjednoť rychlost RB s RB slidem (schválení do 3 pracovních dnů).
> Ukaž mi nejdřív slide 12b a upravenou matici bank.

## 1. Parametry akce a publikum

| Položka | Hodnota |
| --- | --- |
| Cílová skupina | investoři s 1+ nemovitostí, OSVČ a majitelé s.r.o., absolventi workshopu pro začátečníky (23. 9. 2026) |
| Předpokládané znalosti | LTV, DSTI, DTI, bonita, účel, zástava, roadmapa ČSOB/stavební spořitelny |
| Co si účastník odnese | posloupnost bank · srovnání parametrů napříč bankami · Moneta jako most k firemnímu financování · startup úvěry pro SPV · strategii kolečka FO ↔ PO a její úskalí |
| Zdroj programu | egfin.cz/workshopy – workshop pro pokročilé |
| Tón | profesionální, čísla a srovnání, žádný marketing produktů |

## 2. Struktura a časování (18:00–20:30)

| # | Slide | Blok | Čas | Minuty |
| --- | --- | --- | --- | --- |
| 1 | Titulní | – | 18:00 | 2 |
| 2 | Program večera | – | 18:02 | 3 |
| 3 | Rekapitulace: roadmapa k 30 mil. Kč | 1 · NAVÁZÁNÍ | 18:05 | 5 |
| 4 | Kde končí bonita FO | 1 | 18:10 | 8 |
| 5 | Posloupnost bank | 2 · POSLOUPNOST BANK | 18:18 | 7 |
| 6 | Matice bank: co je kde možné | 2 | 18:25 | 10 |
| 7 | Moneta SBL: Mini, Plus, Pro | 3 · MONETA | 18:35 | 8 |
| 8 | Moneta: co je nového a kde je hranice | 3 | 18:43 | 7 |
| 9 | Raiffeisenbank: hypotéka na pronájem a DSCR | 4 · BANKY | 18:50 | 8 |
| 10 | Česká spořitelna: firemní úvěry | 4 | 18:58 | 7 |
| – | Přestávka | – | 19:05–19:20 | 15 |
| 11 | Startup úvěry: ČS vs. ČSOB | 4 | 19:20 | 5 |
| 12 | Projektové financování: Fio, Credix, Home Credit | 4 | 19:25 | 6 |
| 12a | Home Credit: investiční a developerský úvěr | 4 | 19:31 | 3 |
| 12b | Credix: bridge financování | 4 | 19:34 | 3 |
| 13 | Bonita právnické osoby | 5 · STRATEGIE | 19:37 | 5 |
| 14 | Kolečko FO ↔ PO | 5 | 19:42 | 8 |
| 15 | Kolečko v číslech | 5 | 19:50 | 5 |
| 16 | Úskalí kolečka a varianta SPV | 5 | 19:55 | 8 |
| 17 | Zástava, odhad a proces | 6 · PRAXE | 20:03 | 6 |
| 18 | Shrnutí, diskuze a kontakty | 6 | 20:09–20:30 | 21 |

Při skluzu zkrátit slidy 10 a 17, ne blok 5 (strategie je vyvrcholení).

## 3. Slidy

### Slide 1 – Titulní

- **Rozvržení:** hero jako u začátečníků: fotka `egfin-home.jpg` (nebo `adam-hero.jpg`) s tmavě zeleným přechodem, bílý titulek vlevo dole, zlatý štítek, logo vpravo nahoře.
- **Obsah slidu:**
  - Štítek: WORKSHOP PRO POKROČILÉ INVESTORY · 2026
  - Titulek: Financování investičních nemovitostí
  - Podtitul: Když bonita fyzické osoby nestačí: firma, posloupnost bank a kolečko FO ↔ PO
  - Řádek témat: Posloupnost bank · Moneta · Startup úvěry · Projektové financování · Kolečko FO ↔ PO
  - Patička: 24. 9. 2026 · Baťův palác, Praha 1 · Adam Pospíšil · egfin.cz
- **Lektor říká:** rychlá otázka do sálu – kdo má s.r.o. se ziskem, kdo má nemovitost bez zástavy? Tyto dvě věci jsou palivo pro dnešní strategii.

### Slide 2 – Program večera

- **Rozvržení:** světlé pozadí, vlevo malá karta lektora (portrét `egfin-adam-pospisil-original.jpg`, jméno, jedna věta), vpravo program 01–06.
- **Obsah slidu:**
  - Karta: Adam Pospíšil · „Banka vidí úvěr. Já vidím portfolio.“ · 87 obchodů a 633 mil. Kč v roce 2026 (Raynet k 22. 9. 2026)
  - Program:

| # | Blok |
| --- | --- |
| 01 | Navázání: roadmapa a kde končí bonita FO |
| 02 | Posloupnost bank a matice parametrů |
| 03 | Moneta – most k firemnímu financování |
| 04 | RB, ČS, startup úvěry, projektové financování |
| 05 | Pokročilá strategie: kolečko FO ↔ PO a SPV |
| 06 | Zástava, proces, diskuze |

- **Lektor říká:** včera jsme vyčerpali bonitu FO, dnes ji přesuneme na firmu.

### Slide 3 – Rekapitulace: roadmapa k 30 mil. Kč (BLOK 1 · NAVÁZÁNÍ)

- **Účel:** v 5 minutách připomenout výsledek workshopu pro začátečníky (převzato ze zadání 23. 9.).
- **Rozvržení:** vodorovná osa 7 kroků (číslo zlatě, nástroj, částka JetBrains Mono), vpravo tmavě zelená karta s výsledkem.
- **Obsah slidu:**

| Krok | Nástroj | Rámec |
| --- | --- | --- |
| 1 | Příjmy do ČSOB → předschválený limit | až 15 mil. Kč |
| 2 | Buřinka | 2,5–3,5 mil. Kč |
| 3 | RSTS | 2 mil. Kč |
| 4 | Modrá pyramida | 2,5 mil. Kč |
| 5 | Partners banka | až 3 mil. Kč |
| 6 | Hypotéky ČSOB z limitu | do 15 mil. Kč |
| 7 | ČSOBS na evidovaný příjem | až 15 mil. Kč |

  - Karta výsledku: **cca 30 mil. Kč** v úvěrech · LTV portfolia **70 %** · volná zástavní hodnota do 80 % LTV **3,8 mil. Kč** (do 90 %: 7,6 mil. Kč)
  - Řádek pod osou: Tady končí bonita fyzické osoby: DTI 7× a LTV 70 % od 3. nemovitosti.
- **Lektor říká:** zbyla nám volná zástava a nevyužitá bonita firmy – z toho je dnešní večer. Most = Moneta.

### Slide 4 – Kde končí bonita FO (BLOK 1)

- **Účel:** srovnat, co umí FO a co PO – ne jako volbu, ale jako dvě poloviny jedné strategie.
- **Rozvržení:** dvě karty vedle sebe (FO / PO) se stejnými řádky, dole zlatý pruh s pointou.
- **Obsah slidu:**

| Parametr | Fyzická osoba | Právnická osoba (s.r.o.) |
| --- | --- | --- |
| Limit bonity | DTI 7× a LTV 70 % od 3. nemovitosti | žádné DTI – hospodářský výsledek, EBITDA, DSCR |
| Sazba (orient.) | od 5,29 % (RB hypotéka na pronájem) | 6,8–7,2 % Moneta SBL, projektové 8,5–10,5 % |
| Nájem do bonity | 70 % (HC 90 % čistého nájmu; RB i budoucí nájmy) | nájemní smlouvy, výnosová metoda, DSCR |
| Zisk z s.r.o. u FO | ř. 53 VZZ × 0,85 ÷ 12 (rozdíl > 20 % → průměr 2 let) | – |
| Prodej nemovitosti | osvobozen po 10 letech (pořízené od 2021) | daň z příjmů PO + zdanění výplaty |
| Zástava třetí osoby | – | Moneta SBL, Živnohypotéka, HC (jednatel, SJM) |

  - Zlatý pruh: Nemovitosti drží FO, bonitu nese firma.
- **Lektor říká:** ČS Privátní business hypotéka na RČ se řídí zákonem o spotřebitelském úvěru – DSTI 45 % (50 %), DTI 10 (7), změna od 1. 4. 2026. DTI 12× u prvních nemovitostí není limit ČNB, jen interní limit banky.

### Slide 5 – Posloupnost bank (BLOK 2 · POSLOUPNOST BANK)

- **Účel:** pořadí, v jakém čerpat úvěry, a proč právě takhle.
- **Rozvržení:** schodiště zleva doprava (4 stupně), stupeň 0 přerušovaně jako volitelný; nad schody šipka „cena ↑ · flexibilita ↑ · přísnost ↓“.
- **Obsah slidu:**
  - Stupeň 0 (volitelně): **Česká spořitelna** – startup úvěr, projektové fin. na pronájem
  - Stupeň 1: **Raiffeisenbank** – nejlevnější zdroj, hypotéka na pronájem, RE úvěr
  - Stupeň 2: **Moneta** – SBL, Živnohypotéka, zástava třetí osoby
  - Stupeň 3: **Credix · Home Credit · Fio** – na stejné úrovni, projektové financování
  - Řádek: Každá další banka vidí úvěry té předchozí. Levné zdroje se zamykají, dokud je bonita čistá.
- **Lektor říká:** nebankovní a projektové zdroje jsou poslední stupeň nebo bridge – cílem je vždy refinancovat zpět do banky.

### Slide 6 – Matice bank: co je kde možné (BLOK 2)

- **Účel:** hlavní srovnávací slide večera – jeden pohled na všechny parametry.
- **Rozvržení:** tabulka přes celý slide, sloupce = banky, řádky = parametry; nejlepší hodnota v řádku zeleně, omezení oranžově; pod tabulkou poznámka o sazbách.
- **Obsah slidu:**

| Parametr | ČS | RB | Moneta SBL | Fio | Credix | Home Credit |
| --- | --- | --- | --- | --- | --- | --- |
| Dlužník | FOP, PO, SPV | FO, s.r.o. | OSVČ, s.r.o. | PO | jen PO (nemovitost vlastní PO) | FOP, PO |
| Sazba orient. | 9,9 % startup | od 5,29 % | 6,8–7,2 % | PRIBOR + 2,2 % | 9–10 % | 8,5–10,5 % |
| Max. LTV | 70/80 % výnos. hodnoty | 70 % (RE 65 %) | 65–80 % | 60–70 % | byty a domy 65–80 %, bytové domy typicky 70–75 %, krajská města max. 70 % | Praha, Brno 70–75 %, krajská města 65–70 %, komerce 60 % |
| Výše úvěru | do 30 mil. Kč | 20 mil. rezid. / 12 mil. komerce | 1–80 mil. Kč | individuálně | 5–80 mil. Kč (činžovní domy Praha, Brno až 100 mil. Kč na výjimku) | 5–150 mil. Kč na projekt, 200 mil. Kč na skupinu |
| Splatnost | 15–30 let dle typu | 30 let rezid. / 20 let komerce | 30 let (komerce 20) | ~25 let | bridge 12–36 měsíců | max. 20 let, anuitně |
| Bonita | EBITDA, 2 DP | budoucí nájmy, zisk s.r.o., DSCR | výkazy, DSCR | výkazy, záměr | záměr + exit (refinancování do banky nebo prodej) | 90 % čistého nájmu (bez služeb a FO), ESSO přes ručitelskou společnost |
| Zástava 3. osoby | individuálně | – | ano | + podíly, pohledávky | jen vlastní, skupina nebo FO společníka – ne třetí osoba | ano (jednatel, SJM) |
| Poplatky | 0 Kč startup | – | – | 0,5 % + 0,3 % ročně | do 2 % z rámce | 2 %, max. 80 000 Kč + supervize 15 000 Kč |
| Předčasné splacení | – | – | – | zdarma | do 1 roku 2–3 %, pak zdarma | po 12 měs. zdarma (dřív 3 %) |
| Rychlost | – | do 3 prac. dnů | – | ~3 měsíce | schválení i čerpání ~10 prac. dnů | ~1 měsíc |

  - Poznámka: Sazby orientační k 24. 9. 2026. Pomlčka = není předmětem srovnání / individuálně.
- **Lektor říká:** tuhle tabulku si vyfoťte. Otázka není „která banka je nejlepší“, ale „která banka umí můj případ a v jakém pořadí“.

### Slide 7 – Moneta SBL: Mini, Plus, Pro (BLOK 3 · MONETA)

- **Účel:** detail klíčového produktu – rozdíly mezi balíčky.
- **Rozvržení:** tabulka tří sloupců, nahoře tři velké sazby (JetBrains Mono), dole řádek společných parametrů.
- **Obsah slidu:**
  - Velká čísla: **7,2 %** Mini · **6,8 %** Plus · **6,8 %** Pro

| Parametr | SBL Mini | SBL Plus | SBL Pro |
| --- | --- | --- | --- |
| Výše úvěru | 1–20 mil. Kč | 1–50 mil. Kč (angažovanost až 80 mil. Kč) | 1–80 mil. Kč (angažovanost až 100 mil. Kč) |
| Max. LTV rezidence / komerce | 65 % / nelze | 75 % / 60 % | 80 % / 70 % |
| Min. obrat klienta | 500 tis. Kč | 1 mil. Kč | 1,5 mil. Kč |
| Zajištění | jen rezidenční nemovitost | bez omezení kromě ubytovacích zařízení | bez omezení |
| Bonita | finanční výkazy | výkazy + DSCR včetně budoucích nájmů | výkazy + DSCR včetně budoucích nájmů |
| Fixace | 1 / 3 roky | 1 / 3 roky | 1 / 3 / 5 let |

  - Společné: nákup, refinancování vlastních zdrojů i úvěru jiné banky · splatnost až 30 let (byty, RD, BD), 20 let komerce a pozemky · zástavou může být i nemovitost třetí osoby · bez věkového omezení splatnosti
- **Lektor říká:** interně – LTV panelových domů Mini 50 %, Plus 60 %, Pro 65 %; Pro jen přes SME bankéře, Mini a Plus online; klient s daňovou evidencí max. 20 mil. Kč; příjmy z HPP zatím neakceptuje. Na slide nedávat.

### Slide 8 – Moneta: co je nového a kde je hranice (BLOK 3)

- **Účel:** co je u Monety možné už teď a srovnání s alternativami pro OSVČ/firmu.
- **Rozvržení:** nahoře tři dlaždice „co jde“, dole srovnávací tabulka tří produktů.
- **Obsah slidu – dlaždice:**
  - **3 mil. Kč** s jedním daňovým přiznáním a 12 měsíci historie · splátka 20 364 Kč (7,2 %, 30 let)
  - **Průběžná čísla** – nesplňuji obrat z DP? Doložím letošní průběžné výkazy a úvěr mám hned
  - **Obrat 2× splátka** – následná podmínka: obrat na BÚ od třetích osob, ne od ekonomicky spjaté skupiny; výhledově depozit 3–6 splátek a pak obrat 1× splátka
- **Obsah slidu – tabulka:**

| | Hypotéka FO | Živnohypotéka Moneta | SBL Plus / Pro |
| --- | --- | --- | --- |
| Dlužník | FO | OSVČ i s.r.o. | OSVČ i s.r.o. |
| LTV | 70 % od 3. nemovitosti | 80 % | 75–80 % |
| Limit bonity | DTI 7×, DSTI | EBITDA kryje dluhovou službu | výkazy + DSCR vč. budoucích nájmů |
| Zástava třetí osoby | ne | ano | ano |
| Kdy použít | dokud je bonita FO | OSVČ s dobrým ziskem | když FO narazí na DTI |

- **Lektor říká:** Moneta je první místo, kde bonitu nese firma a zástavu může dát fyzická osoba – na tom stojí kolečko v bloku 5.

### Slide 9 – Raiffeisenbank: hypotéka na pronájem a DSCR (BLOK 4 · BANKY)

- **Účel:** proč je RB první stupeň a jak počítá maximální úvěr z nájmu.
- **Rozvržení:** vlevo karta parametrů, vpravo výpočet ve třech krocích (velká čísla JetBrains Mono).
- **Obsah slidu – parametry:**
  - Hypotéka na pronájem: od **5,29 %** · LTV **70 %** · rezidence max. 20 mil. Kč / 30 let · komerce max. 12 mil. Kč / 20 let · fixace 1–7, 10 nebo 15 let · schválení do 3 pracovních dnů
  - Uznává: **budoucí příjmy z pronájmu**, zisk společníka s.r.o., příjmy OSVČ · neuzná: nájem vykázaný v § 7
  - Real Estate úvěr (PO): LTV 65 % z výnosové hodnoty · stačí generální dodavatel (ČS max. 3 dodavatelé)
- **Obsah slidu – výpočet DSCR (příklad: nájem 200 000 Kč měsíčně):**
  - Krok 1: měsíční nájem ÷ 120 = 200 000 ÷ 120 = **1 666,67 Kč** (DSCR koeficient)
  - Krok 2: koeficient × 100 = **166 667 Kč** maximální měsíční splátka
  - Krok 3: max. splátka ÷ 8 000 Kč (cena 1 mil. Kč úvěru) = **20,83 mil. Kč** maximální úvěr
- **Lektor říká:** 1 mil. Kč při 6 % na 25 let stojí 6 443 Kč měsíčně – 8 000 Kč v sobě má stresovou rezervu. Budoucí nájmy RB uzná, ČSOB ne.

### Slide 10 – Česká spořitelna: firemní úvěry (BLOK 4)

- **Účel:** co kde v ČS jde – limity a splatnosti vedle sebe, plus KO kritéria.
- **Rozvržení:** vlevo tabulka produktů (2/3), vpravo varovná karta KO kritérií.
- **Obsah slidu – tabulka:**

| Produkt | Max. výše | Splatnost | Na co / pro koho |
| --- | --- | --- | --- |
| Komerční hypotéka | 30 mil. Kč | 15 let logistika · 20 let kanceláře, ubytování · 25 let rezidence · 30 let novostavba | nákup, rekonstrukce, výstavba, refinancování |
| Projektové fin. – pronájem | 30 mil. Kč | až 25 let (30 let nová rezidence) | SPV bez vlastního cash flow, splácení z budoucího nájmu, LTV 70/80 % výnosové hodnoty |
| Neúčelový zajištěný | 20 mil. Kč / 10 let · 12,5 mil. Kč / 20 let | 10–20 let | vždy zástava rezidence, průměr 2 DP + LTV |
| Neúčelový nezajištěný | 6 mil. Kč (VIP 9 mil. Kč) | 8 let | limit z DP nebo z 6 měsíců výpisů |
| Privátní business hypotéka | 50 mil. Kč rezidence / 30 mil. Kč ostatní | až 30 let | FO na RČ, DSTI 45 % (50 %), DTI 10 (7) |

- **Obsah slidu – KO kritéria:** negativní záznam v registrech CRÚ/CCB · insolvence v ekonomicky spjaté skupině · paušální daň · záporný vlastní kapitál · záporný výsledek hospodaření · zahraniční neprůhledná vlastnická struktura
- **Lektor říká:** u SPV na pronájem banka chce půjčku společníka, doložení toků peněz a následně podřízenost pohledávky.

### Slide 11 – Startup úvěry: ČS vs. ČSOB (BLOK 4)

- **Účel:** snadno dosažitelný první zdroj pro nové SPV.
- **Rozvržení:** dvě karty vedle sebe se stejnými řádky, velká čísla nahoře.
- **Obsah slidu:**

| | Česká spořitelna – Firemní úvěr Start Up | ČSOB – Úvěr pro začínající podnikatele |
| --- | --- | --- |
| Výše | 50 000 – 1 200 000 Kč | 200 000 – 1 000 000 Kč |
| Sazba | 9,9 % p. a., fixně po celou dobu | individuálně |
| Splatnost | 84 měsíců (7 let) | individuálně |
| Splátka při max. výši | zhruba 20 400 Kč | – |
| Odklad splátek | první splátka až o 5 měsíců | – |
| Pro koho | FOP i PO do 3 let od založení – i nové SPV | nově vzniklé firmy a podnikatelé |
| Doklady | bez daňového přiznání, bez prokazování účelu | dle bankéře |
| Zajištění | záruka Evropské investiční banky (EIF), blankosměnka s avalem, zástava účtu | podpora EU přes EIF |
| Poplatky | zřízení i vedení 0 Kč | běžný účet zdarma |

  - Řádek: Úvěr je zajištěný Evropskou investiční bankou → lehce dosažitelný, vhodný pro rozjezd podnikání i nového SPV.
- **Lektor říká:** startup úvěr = vlastní zdroje do SPV, první obraty a historie pro Monetu.
- **Ověřit před finalizací:** sazbu a splatnost ČSOB doplnit od bankéře.

### Slide 12 – Projektové financování: Fio, Credix, Home Credit (BLOK 4)

- **Účel:** tři poskytovatelé na stejném stupni – kdy který.
- **Rozvržení:** tabulka tří sloupců, pod ní tři karty „kdy použít“.
- **Obsah slidu – tabulka:**

| Parametr | Fio | Credix | Home Credit |
| --- | --- | --- | --- |
| Dlužník | PO, ručí FO | jen PO (nemovitost ve vlastnictví PO) | FOP i PO; nový projekt = SPV + vždy ručitelská společnost |
| Sazba | PRIBOR + 2,2 % (~5,8–6,3 %) | 9–10 % | 8,5–10,5 % (development 8,5–9,5 %) |
| LTV | 60–70 % | byty a domy 65–80 % · bytové domy typicky 70–75 % (Praha, Brno výš) · krajská města max. 70 % · pozemek se SP 65–70 %, bez SP 50–55 % · min. 20 % vlastních zdrojů (v rámci skupiny i 100 %) | Praha, Brno 70–75 % · krajská města 65–70 % · komerce 60 % · min. 20 % vlastních zdrojů |
| Výše | individuálně | 5–80 mil. Kč (125 mil. Kč na ESS; činžovní domy Praha, Brno až 100 mil. Kč na výjimku) | 5–150 mil. Kč na projekt, 200 mil. Kč na skupinu |
| Splatnost | ~25 let | bridge 12–36 měsíců, pak refinancování do banky | max. 20 let (i komerce a development) |
| Splácení | anuitně | měsíčně úroky (z nájmů) a jistina ve splatnosti, nebo balon s kapitalizací úroků | vždy měsíčně anuitně, žádné balony |
| Poplatky | 0,5 % přistavení, 0,3 % monitoring ročně | do 2 % z úvěrového rámce | 2 %, max. 80 000 Kč · supervize 15 000 Kč · katastr 1 600 Kč · notářský zápis |
| Předčasné splacení | zdarma | do 1 roku exit fee 2–3 %, pak zdarma (lze 0 % po 6 měsících za vyšší sazbu) | v prvních 12 měsících 3 %, pak zdarma |
| Bonita | výkazy, záměr | záměr + exit strategie; dlouhodobý pronájem umí, ale klient odchází do banky o ~3 p. b. levněji | celá splátka: 90 % nájmu očištěného o služby a fond oprav + příjmy ESSO přes ručitele |
| Zástava | financovaná nemovitost + podíly, pohledávky | jen vlastní nemovitost, nemovitost PO ze skupiny nebo FO společníka – ne třetí osoba (ani rodina) | i nemovitost jednatele / SJM |
| Rychlost | ~3 měsíce | schválení i čerpání ~10 pracovních dnů, čerpání na návrh na vklad | ~1 měsíc (refi + hotovost 2–3 měsíce) |

- **Obsah slidu – karty:**
  - Fio: plánovaný projekt s časovou rezervou – nejlevnější z trojice
  - Credix: bridge 12–36 měsíců na rychlý nákup, činžovní dům → prohlášení vlastníka → rozprodej nebo refinancování, provozní úvěr se zástavou nemovitosti (slide 12b)
  - Home Credit: bridge, refinancování + hotovost navíc, refinancování s rekonstrukcí i při dočasném výpadku nájmu, development bez předprodejů (slide 12a)
  - Řádek: Strategie: bridge → oprava bonity nebo projektu → refinancování do banky.
- **Lektor říká:** HC úvěr 10 mil. Kč orientačně = poplatky cca 116 400 Kč (zpracování 80 000 Kč + supervize Air Bank 15 000 Kč + katastr 1 600 Kč + notářský zápis cca 19 800 Kč); vše schvaluje mateřská Air Bank. Nákup pod cenou HC zohlední jen částečně – min. 20 % vlastních zdrojů. Credix: sazba 9–10 % podle hovoru 24. 9. (prezentace uvádí od 8,9 %), krajská města nad 70 % LTV nejdou (Plzeň centrum, špatný stav, refi + rekonstrukce: 65–70 %).

### Slide 12a – Home Credit: investiční a developerský úvěr (BLOK 4)

- **Účel:** co u Home Creditu jde nad rámec bank – hlavně development bez předprodejů (zdroj: hovor s Home Creditem 24. 9. 2026).
- **Rozvržení:** vlevo karta „Investiční úvěr“, vpravo karta „Development“ s procesem čerpání ve 4 krocích; dole pruh „Pravidla splácení“.
- **Obsah slidu – Investiční úvěr:**
  - **8,5–10,5 %** · LTV Praha a Brno 70–75 %, krajská města 65–70 %, komerce 60 % · max. **20 let**
  - Bonita: musí pokrýt celou splátku · **90 % nájmu** očištěného o služby a fond oprav · příjmy ekonomicky spjaté skupiny přes ručitelskou společnost
  - Nový projekt: SPV + vždy ručitelská společnost, která projekt udrží při výpadku
  - Umí refinancování + kompletní rekonstrukci i při dočasném výpadku nájmu
  - Nezajištěný podnikatelský úvěr jen přes centrálu, max. 0,5 mil. Kč
- **Obsah slidu – Development:**
  - **8,5–9,5 %** (cca 2,5–3 p. b. nad bankou) · LTV **65–75 %** ve výstavbě · limit **150 mil. Kč** na projekt
  - Podmínky: stavební povolení, smlouva o dílo, rozpočet, harmonogram, odhad stávající i budoucí tržní hodnoty
  - **Bez předprodejů a bez vázaných účtů** – zálohy od kupců zůstávají developerovi
  - Proces čerpání: 1 fotky a videa stavby → 2 supervize prostavěnosti (Air Bank) → 3 čerpání druhý den → 4 opakovat do konce stavby
  - Umí financovat i dluhovou službu (půjčí na splátky), pokud to LTV a vlastní zdroje dovolí
  - Vyvazování: HC určí minimální prodejní cenu, z každé jednotky jde 80 % ceny bez DPH na splátku, zbytek developerovi
  - Smlouva na 20 let, reálně ~2 roky; prodej jednotky koncovému klientovi lze splatit i do 1 roku bez sankce · hypotéky pro kupce přes Air Bank
- **Obsah slidu – pruh Pravidla splácení:** vždy měsíčně anuitně (jistina + úrok), žádné balony · mimořádná splátka do 12 měsíců 3 %, pak zdarma · mimořádnou splátku předem nahlásit a v daném měsíci zaplatit i řádnou splátku
- **Lektor říká:** developer bez předprodejů zahájí prodej až na hrubé stavbě – kupci vidí dispozice a prodává se za plnou cenu, ne pod tlakem podmínky banky. Proto se vyšší sazba často vyplatí. Balonové úvěry jsou riziko: při neschopnosti splatit se prodlužují za další poplatek z jistiny.

### Slide 12b – Credix: bridge financování (BLOK 4)

- **Účel:** kdy dává Credix smysl – rychlý nákup, činžovní dům k rozdělení, cesta do Monety (zdroj: hovor s Credixem 24. 9. 2026).
- **Rozvržení:** vlevo karta „Bridge 12–36 měsíců“ s velkým číslem sazby a tokem ve 3 krocích, vpravo tabulka LTV podle typu a lokality; dole pruh „Zástava a vlastní zdroje“.
- **Obsah slidu – Bridge:**
  - **9–10 %** · **12–36 měsíců** · schválení i čerpání **~10 pracovních dnů**
  - Tok: 1 Credix zafinancuje nákup → 2 klient nastaví nájemní smlouvy, nájmy chodí 6–12 měsíců (podle požadavku banky) → 3 refinancování do banky o ~3 p. b. levněji, nejčastěji Moneta (Živnohypotéka až 30 let)
  - Moneta bere Credix jako banku – refinancuje ho napřímo; sama u něj parkuje klienty, kteří potřebují koupit rychle
  - Splácení: z nájmů měsíčně úrok, jistina ve splatnosti z refinancování; nebo balon s kapitalizací úroků
  - Poplatky: zpracování do 2 % z rámce · exit fee do 1 roku 2–3 %, pak 0 % (lze 0 % už po 6 měsících za vyšší sazbu)
- **Obsah slidu – tabulka LTV:**

| Typ nemovitosti | LTV |
| --- | --- |
| Byty a rodinné domy | 65–80 % |
| Bytové domy | typicky 70–75 %, Praha a Brno výš |
| Krajská města (Plzeň, refi + rekonstrukce) | max. 70 % |
| Pozemek se stavebním povolením | 65–70 % |
| Pozemek jen podle územního plánu | 50–55 % (spekulace) |
| Rizikové lokality: Karlovy Vary, Ostrava, Ústecký kraj | individuálně, nižší |

  - Řádek pod tabulkou: Preferované lokality: Praha, Brno, střední Čechy, pak krajská města. Limit 80 mil. Kč; činžovní domy v Praze a Brně až 100 mil. Kč na výjimku Banky CREDITAS.
- **Obsah slidu – pruh Zástava a vlastní zdroje:** min. **20 % vlastních zdrojů** (nákup v rámci skupiny i 100 % kupní ceny) · 100 % projektových nákladů, pokud je zajištěno jinou nemovitostí PO, PO ze skupiny nebo FO společníka · **zástava třetí osoby ne** (ani rodina) – reputační riziko a bez protiplnění ji insolvenční správce může zpochybnit · činžovní dům bez prohlášení vlastníka se ocení jako celek, po prohlášení po jednotkách → vyšší zástavní hodnota → Credix může proplatit část vlastních zdrojů
- **Lektor říká:** pro indikaci stačí kupní cena (≈ ocenění), doba, zda měsíční úroky nebo kapitalizace, lokalita a typ – bez přesného LV, i slepá poptávka. Odhad od odhadců Banky CREDITAS; nad 25 mil. Kč jde na supervizi do banky, lze použít i vlastního bankovního znalce. Zástava od společnosti ze skupiny potřebuje smlouvu o protiplnění. Exit z bridge: Moneta, případně UniCredit.

### Slide 13 – Bonita právnické osoby (BLOK 5 · STRATEGIE)

- **Účel:** co musí firma ukázat, aby mohla nést bonitu za celou strategii.
- **Rozvržení:** čtyři karty (Výsledek · Cash flow · Struktura · Rozvaha).
- **Obsah slidu:**
  - Výsledek: EBITDA musí krýt roční dluhovou službu včetně nového úvěru · odpisy se přičítají · skokový zisk po letech ztrát komentovat
  - Cash flow: DSCR – RB měsíční nájem ÷ 120 · Moneta výkazy + DSCR vč. budoucích nájmů · obrat 2× splátka od třetích osob
  - Struktura: ekonomicky spjatá skupina, mateřská a dceřiná společnost, beneficient = ručitel FO
  - Rozvaha: záporný vlastní kapitál = KO · závazky ke společníkům přeúčtovat do kapitálových fondů nebo podřídit · **pohledávky za společníky banky rozklíčují** (viz slide 16)
- **Lektor říká:** poslední bod je most ke kolečku – pohledávka za společníkem je přesně to, co u něj vznikne.

### Slide 14 – Kolečko FO ↔ PO (BLOK 5)

- **Účel:** hlavní myšlenka večera v jednom diagramu.
- **Rozvržení:** tmavě zelený slide; vlevo kruh se čtyřmi kartami a zlatými šipkami po směru hodinových ručiček, uprostřed „OPAKUJ“; vpravo karta „Proč to funguje“. Předloha: `grafika/kolecko-strategie.png`.
- **Obsah slidu:**
  - 1 **Zástava FO** – FO dá volnou nemovitost do zástavy za úvěr firmy
  - 2 **Úvěr PO** – s.r.o. s bonitou čerpá podnikatelský úvěr
  - 3 **Zápůjčka PO → FO** – vždy za tržní úrok, ne vyvádění peněz
  - 4 **Nákup na FO** – další nemovitost na FO = nová zástava
  - Střed: OPAKUJ – dokud nedojde bonita PO nebo volná zástava
  - Karta „Proč to funguje“: Bonitu nese firma (DSCR / EBITDA s.r.o., ne DTI 7× u FO) · Nemovitosti drží FO (nejlevnější hypotéky a prodej na FO) · Zástava třetí osoby (Moneta SBL, Živnohypotéka ji přijmou)
- **Lektor říká:** právnická osoba si půjčí se zajištěním nemovitosti, kterou vlastní FO. Peníze půjčí FO, ta nakoupí další nemovitost přímo na sebe, a ta se stane zástavou pro další podnikatelský úvěr – dokud se nevyčerpají volné zdroje nebo zástava. Zápůjčka musí mít vždy tržní úrok, jinak jde o vyvádění peněz ze společnosti.

### Slide 15 – Kolečko v číslech (BLOK 5, zlatý akcentní slide)

- **Účel:** ukázat, kolik kolečko reálně dá a co to udělá s firmou.
- **Rozvržení:** vlevo tabulka kol, vpravo tři velká čísla dopadů na PO, dole řádek předpokladů.
- **Obsah slidu:**

| Kolo | Zástava | Úvěr PO (LTV 75 %) | Nákup FO |
| --- | --- | --- | --- |
| 1 | 6,0 mil. Kč | 4,50 mil. Kč | 4,50 mil. Kč |
| 2 | 4,5 mil. Kč | 3,38 mil. Kč | 3,38 mil. Kč |
| 3 | 3,4 mil. Kč | 2,53 mil. Kč | 2,53 mil. Kč |
| Celkem | | **10,41 mil. Kč** | **+10,41 mil. Kč nemovitostí** |
| Strop (nekonečně kol) | | 4,5 ÷ (1 − 0,75) = **18 mil. Kč** | |

  - Velká čísla: **67 841 Kč** splátka PO měsíčně · **135 682 Kč** potřebný obrat měsíčně od třetích osob (2× splátka) · **1,02 mil. Kč** EBITDA ročně pro DSCR 1,25
  - Řádek: Předpoklady: volný byt FO 6 mil. Kč, Moneta SBL Plus, LTV 75 %, 6,8 %, 30 let, nákupy FO za hotové (nová nemovitost zůstane volná). Ilustrativní příklad.
- **Lektor říká:** úrok, který FO platí firmě (při 7 % je to 728 438 Kč ročně), je příjem PO – ale od ekonomicky spjaté osoby, do obratu pro Monetu se nepočítá. Obrat musí přijít zvenku.

### Slide 16 – Úskalí kolečka a varianta SPV (BLOK 5)

- **Účel:** kde kolečko narazí (pohledávka za společníky v rozvaze) a jak to řeší varianta s SPV – kdo je dlužník, kdo ručí a jak tečou peníze.
- **Rozvržení:** tmavě zelený slide. Vlevo (2/3 šířky) schéma šesti uzlů ve dvou řadách: nahoře Původní s.r.o. · SPV s.r.o. · Moneta, dole Nemovitost · FO (investor) · Koncový nájemník. Šipky s číslem kroku v kroužku; barvy šipek: zlatá = peníze, světlá mátová = smluvní vztah (ručení, nájem, podnájem), zelená = nemovitost; pod schématem legenda. Vpravo (1/3) varovná karta „Proč SPV, a ne původní s.r.o.“. Dole pás osmi číslovaných kroků (4 × 2). Předloha: `grafika/kolecko-spv.png`.
- **Obsah slidu – uzly:**
  - Původní s.r.o. – má bonitu a historii · RUČITEL / PŘISTUPITEL
  - SPV s.r.o. – nová firma · DLUŽNÍK · eviduje úvěr i zápůjčku (zvýrazněný uzel, zlatý rámeček)
  - Moneta – SBL · zástava = nemovitost FO
  - Nemovitost – koupená na FO = nová volná zástava
  - FO (investor) – vlastník nemovitostí, dává zástavu
  - Koncový nájemník – třetí osoba (ne ESSO)
- **Obsah slidu – šipky (číslo = krok):** R Původní s.r.o. → SPV (ručení, mátová) · 1 Moneta → SPV (zlatá) · 8 SPV → Moneta (zlatá) · 2 SPV → FO (zlatá) · 7 SPV → FO (zlatá) a 7 FO → SPV (zlatá) · 3 FO → Nemovitost (zelená) · 4 Nemovitost → SPV (mátová) · 5 SPV → Koncový nájemník (mátová) · 6 Koncový nájemník → SPV (zlatá)
- **Obsah slidu – kroky (pás dole):**

| # | Krok | Popis |
| --- | --- | --- |
| 1 | Moneta půjčí SPV | zástava = nemovitost FO · R = ručení s.r.o. |
| 2 | SPV půjčí FO | zápůjčka vždy za tržní úrok |
| 3 | FO koupí nemovitost | na sebe → nová volná zástava |
| 4 | FO ji pronajme SPV | nájemní smlouva FO → SPV |
| 5 | SPV ji podnajme | koncovému nájemníkovi (nižší ochrana) |
| 6 | Nájemník platí SPV | nájemné = obrat od třetí osoby |
| 7 | SPV platí FO nájem | FO platí SPV úrok ze zápůjčky |
| 8 | SPV splácí Monetě | z nájemného; výhled: depozit 3–6 splátek |

- **Obsah slidu – karta „Proč SPV, a ne původní s.r.o.“:** Zápůjčka FO je v rozvaze firmy pohledávka za společníky. · ČSOB i další banky ji FO přičtou do splátek → horší DSTI a DTI u hypoték na FO. · „Jiné pohledávky“ banky čím dál častěji rozklíčují. · **V SPV zůstává úvěr i zápůjčka.** Původní s.r.o. jen ručí / přistupuje k závazku – její výkazy nenesou zápůjčku společníkovi. · Podmínka Monety: obrat SPV ≥ 2× splátka od třetích osob → řeší krok 6.
  - Patička slidu: Ilustrativní schéma – konkrétní strukturu ověřit s bankou a daňovým poradcem (převodní ceny, tržní úrok zápůjčky).
- **Lektor říká:** SPV je dlužník, původní s.r.o. ručitel nebo přistupitel k závazku. SPV půjčí FO, FO koupí nemovitost, tu pronajme SPV a SPV ji podnajme koncovému nájemníkovi. Nájemné tak platí koncový nájemník do SPV – to je obrat od třetí osoby, který Moneta vyžaduje – a z SPV jdou peníze FO formou nájmu. Bonus: podnájem má nižší ochranu nájemníka než přímý nájem. Start SPV lze podpořit startup úvěrem ČS (1,2 mil. Kč, 84 měsíců, lze i na nové SPV) – vlastní zdroje, první obraty a historie.

### Slide 17 – Zástava, odhad a proces (BLOK 6 · PRAXE)

- **Účel:** praktické hranice – vyvazování, odhady, časy.
- **Rozvržení:** tři sloupce karet.
- **Obsah slidu:**
  - Zástava: kolečko = vědomá práce se zástavou třetí osoby · podmínky vyvázání vyjednat předem do smlouvy · 1 nemovitost = 1 úvěr, kde to jde · HC: vyvázání jednotky při prodeji – 80 % ceny bez DPH na splátku · Credix: zástava třetí osoby ne – bez protiplnění ji může insolvenční správce zpochybnit
  - Odhad: výnosová metoda nebo cena budoucí = alfa a omega · Credix: odhadci Banky CREDITAS, nad 25 mil. Kč supervize v bance (lze i vlastní bankovní znalec) · HC odhad max. 6 měsíců starý · nájem musí být potvrzen v odhadu
  - Proces a čas: RB hypotéka do 3 pracovních dnů · Home Credit ~1 měsíc, zápis zástavy na KN min. 20 dní · Fio ~3 měsíce – začít s předstihem · Credix schválení i čerpání ~10 pracovních dnů
- **Lektor říká:** u kolečka prodej nemovitosti FO zablokuje banka firmy, pokud vyvázání není ve smlouvě.

### Slide 18 – Shrnutí, diskuze a kontakty (BLOK 6)

- **Rozvržení:** vlevo šest číslovaných karet, vpravo karta Q&A s kontakty, dole disclaimer.
- **Obsah slidu:**
  - 01 Navázání – bonita FO končí na DTI 7× a LTV 70 %; zbývá volná zástava a bonita firmy.
  - 02 Posloupnost – (ČS) → RB → Moneta → Credix / Home Credit / Fio; bridge Credix → refinancování do Monety.
  - 03 Moneta – Mini 7,2 %, Plus a Pro 6,8 %; 1 DP + 12 měsíců = až 3 mil. Kč; zástava třetí osoby.
  - 04 Startup – ČS 1,2 mil. Kč / 9,9 % / 84 měsíců, i pro nové SPV, zajištění Evropskou investiční bankou.
  - 05 Kolečko FO ↔ PO – bonitu nese firma, nemovitosti drží FO; zápůjčka vždy za tržní úrok.
  - 06 Úskalí – pohledávka za společníky v rozvaze a obrat SPV od třetích osob.
  - Karta Q&A: Diskuze a vaše dotazy · propočet kolečka na vaší rozvaze v 1:1 konzultaci · Adam Pospíšil · egfin.cz · adamovyfinance.cz
  - Disclaimer: Prezentace je informační. Podmínky bank se mění – vždy je ověřte u svého poradce nebo přímo v bance. Sazby orientační k 24. 9. 2026.

## 3b. Review decku Workshop_pokročilí – EGFIN (PDF 24 stran, 24. 9. 2026)

### Chyby k opravě

| # | Slide | Problém | Návrh |
| --- | --- | --- | --- |
| 1 | 1, 18, 23 | znak „↔“ se nevykresluje („Kolečko FO   PO“) | nahradit „FO a PO“ |
| 2 | 5, 7, 11, 12, 23 | sazby Monety nesedí: slide 11 uvádí Mini 7 %, Plus a Pro 6,5 %; slide 5 „6,8–7,2 %“, slide 7 „6,5–7,2 %“, slide 12 splátka počítaná ze 7,2 %, shrnutí „Mini 7,2 %, Plus a Pro 6,8 %“ | sjednotit podle slidu 11; při 7 % je splátka 3 mil. Kč / 30 let 19 959 Kč |
| 3 | 7 | řádek Bonita má rozhozené sloupce; písmo pod 12 pt; rychlost RB „~1 měsíc“ vs. slide 9 „do 3 pracovních dnů“ | zjednodušit tabulku (viz níže), sjednotit RB |
| 4 | 15 | hlavička tabulky koliduje s titulkem; blok „Kdy použít“ překrývá logo v patičce | posunout tabulku pod titulek, zmenšit blok |
| 5 | 5 | „omezeně (čsobs ok)“ | „omezeně (ČSOBS ano)“ |
| 6 | 4 | „(Modrá pyramida)“ a „(Partners banka)“ v závorkách bez vysvětlení; dolní třetina slidu prázdná | závorky odstranit nebo vysvětlit; kartu výsledku zvětšit |
| 7 | 9 | titulek „PROFIT rezidenční / komerční“ je název produktu, ne téma; pravý dolní roh prázdný | „Raiffeisenbank: hypotéka na pronájem a DSCR“ |
| 8 | 22 | Credix „rychlý prescoring“ – zastaralé | „schválení i čerpání ~10 pracovních dnů“ |
| 9 | 20 | karta „Proč SPV“ se dotýká pásu kroků; text uzlů malý | viz zjednodušení |

### Zjednodušení a zpřehlednění

1. **Matice bank (slide 7):** 11 řádků × 6 sloupců při ~10 pt je z projektoru nečitelné. Nechat 6 klíčových řádků (Dlužník, Sazba, Max. LTV, Výše, Splatnost, Zástava 3. osoby); Poplatky, Předčasné splacení, Rychlost a Bonita přesunout do speaker notes – u projektových poskytovatelů jsou stejně na slidu 15. Písmo min. 12 pt.
2. **Projektové financování (slide 15):** po přidání řádku Zástava má tabulka 11 řádků. Nechat 8 (Dlužník, Sazba, LTV, Výše, Splatnost, Splácení, Předčasné splacení, Zástava), Poplatky a Rychlost přesunout na slidy 12a/12b a do notes. Blok „Kdy použít“ zkrátit na jednu větu na poskytovatele.
3. **RB podnikatelské úvěry (slide 10):** pro investory jsou podstatné Investiční úvěr, Americká hypotéka a Offset. Neúčelový a kontokorentní úvěr zkrátit na jeden řádek „ostatní“ nebo do notes; sloupec Poznámka zkrátit na max. 2 položky.
4. **Úskalí kolečka a SPV (slide 20):** rozdělit na dva slidy: 20a diagram + legenda + karta „Proč SPV“ (větší uzly, písmo 14 pt), 20b osm kroků jako 4 × 2 karty s jednou větou navíc u kroku 6 (obrat od třetí osoby) a 7 (nájem vs. úrok). Časově to nic nestojí, kroky se stejně odvyprávějí.
5. **Bonita v praxi (slide 3):** je to rekapitulace z workshopu pro začátečníky; když bude skluz, první kandidát na vypuštění. Alternativa: ponechat jen dvě velká čísla (6,83–13,22 mil. Kč a rozdíl 6,4 mil. Kč) bez tabulky.
6. **Bonita PO (slide 17):** čtyři karty jsou z poloviny prázdné. Přidat do karty Rozvaha řádek „pohledávky za společníky → varianta SPV“ jako zlatý odkaz a snížit výšku karet, nebo doplnit pátou kartu „Co doložit“ (výkazy 2 roky, nájemní smlouvy, ARES, bezdlužnost).
7. **Posloupnost bank (slide 6):** ČS je na schodech dvakrát (0 a 3). Sloučit do jednoho stupně „ČS: projektové financování (volitelně před RB) · Startup úvěr (výjimka, až za Monetou)“, ať schody mají 4 stupně a stejnou výšku.
8. **Patička:** logo je na všech slidech, text patičky jen na některých. Sjednotit: „egfin.cz · Workshop pro pokročilé investory · 24. 9. 2026“ na všech obsahových slidech.
9. **Startup ČS vs. posloupnost:** slide 6 říká „čerpat až za Monetou“, slide 14 „vhodný pro rozjezd nového SPV“. Do notes slidu 14 doplnit, kdy který případ: nové SPV bez Monety → startup první; existující firma před Monetou → startup až po Monetě, aby nezatížil bonitu.

## 4. Otevřené body k ověření před finalizací

1. ČSOB startup: sazba a splatnost na webu neuvedeny – doplnit od bankéře.
2. ČS projektové financování na pronájem: LTV 70/80 % výnosové hodnoty (poznámky ČS) vs. 65 % ve starém decku.
3. Příklad kolečka (slide 15) je ilustrativní: DSCR 1,25 a tržní úrok 7 % jsou předpoklady.

Potvrzeno lektorem 24. 9.: posloupnost bank, parametry startup úvěru ČS podle nahrávky, místo a čas.

## 5. Zdroje

- Pocket, 24. 9. 2026: „Podmínky bridge financování v Credixu“ (15:33), „Podnikatelské úvěry Home Credit“ (13:29), „Příprava obsahu workshopu pro pokročilé“ (10:34), „Pokročilá strategie financování“ (11:15), „Pokročilé strategie financování 2 a SPV“ (11:50)
- Zadání workshopu pro začátečníky 23. 9. 2026 (roadmapa, SBL Mini/Plus/Pro, vizuální styl)
- Workshop_Pokrocili_v3.pptx (struktura, RB DSCR, Fio, křížová zástava)
- CREDIX – Firemní úvěry, základní parametry (2026); Home Credit – Zajištěný úvěr pro podnikatele 2026; Česká spořitelna – Firemní úvěry, SB Praha 01/2026
- [ČS – financování pro začínající podnikatele](https://www.csas.cz/cs/firmy/uvery/financovani-pro-zacinajici-podnikatele) · [ČSOB – úvěr pro začínající podnikatele](https://www.csob.cz/firmy/uvery-a-financovani/nabidka-pro-zacinajici-podnikatele) · [RB – hypotéka na pronájem (hypotecnikalkulacka.cz)](https://www.hypotecnikalkulacka.cz/produkt/hypoteka-na-pronajem-od-raiffeisenbank/)
