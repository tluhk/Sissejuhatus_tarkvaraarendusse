# Sprint 3 pseudokoodi näited - "Kooli Köök"

## Sissejuhatus

Sprint 3-s me **EI KIRJUTA PÄRIS KOODI**! Selle asemel kirjeldame algoritme pseudokoodiga - see on nagu retsept, mis selgitab sammhaaval, mida arvuti peaks tegema.

**Miks pseudokood?**
- ✅ Keskendume loogikale, mitte programmeerimiskeele süntaksile
- ✅ Igaüks saab aru, isegi ilma programmeerimisoskusteta
- ✅ Aitab planeerida päris koodi kirjutamist
- ✅ Võimaldab arutada algoritme meeskonnaga

---

## Näide 1: Vaba mikrolaineahju leidmine

### Kasutajateekond
> **Mari** tuleb lõunale kooli. Ta avab "Kooli Köök" rakenduse telefonis ja soovib leida lähima vaba mikrolaineahju, et oma toitu soojendada.

### Mida rakendus peab tegema?

**Lihtsustatud sammud:**
1. Küsi kasutaja asukoht (GPS)
2. Leia kõik mikrolaineahjud andmebaasist
3. Kontrolli iga ahju olekut (VABA, KASUTUSES, BRONEERITUD)
4. Arvuta kaugus kasutajast
5. Näita kasutajale lähimaid vabasid ahjusid

---

### Pseudokood: Vabade ahjude otsimine

```
FUNKTSIOON leia_vabad_ahjud(kasutaja_asukoht):
    // Samm 1: Leia kõik ahjud andmebaasist
    kõik_ahjud = OTSI andmebaasist kõik mikrolaineahjud

    // Samm 2: Loo tühi nimekiri vabadele ahjudele
    vabad_ahjud = tühi_nimekiri

    // Samm 3: Käi läbi iga ahi
    KORDA iga ahi kõik_ahjud listis:
        // Kontrolli kas ahi on vaba
        KUI ahi.olek == "VABA":
            // Arvuta kui kaugel ahi on
            kaugus = ARVUTA kaugus kasutaja_asukoht ja ahi.asukoht vahel

            // Lisa kaugus ahju juurde
            ahi.kaugus_kasutajast = kaugus

            // Lisa vabade ahjude nimekirja
            LISA vabad_ahjud nimekirja ahi

    // Samm 4: Sorteeri lähimad enne
    SORTEERI vabad_ahjud kauguse järgi (väiksemad numbrid enne)

    // Samm 5: Näita ainult 5 lähimat
    viis_lähimat = VÕTA esimesed 5 ahi nimekirjast vabad_ahjud

    // Samm 6: Tagasta tulemus
    TAGASTA viis_lähimat
LÕPP
```

### Näide sisend ja väljund

**Sisend:**
- Kasutaja asukoht: Mare õppehoone, 2. korrus

**Andmebaasis olevad ahjud:**
```
Ahi #1: A-korpus, 1. korrus - VABA - 0.2 km kaugusel
Ahi #2: A-korpus, 2. korrus - KASUTUSES - 0.15 km kaugusel
Ahi #3: Mare, 2. korrus - VABA - 0.05 km kaugusel
Ahi #4: Mare, 1. korrus - VABA - 0.1 km kaugusel
Ahi #5: B-korpus, 3. korrus - BRONEERITUD - 0.5 km kaugusel
```

**Väljund (sorteeritud nimekiri):**
```
1. Ahi #3: Mare, 2. korrus - VABA - 0.05 km (50 meetrit)
2. Ahi #4: Mare, 1. korrus - VABA - 0.1 km (100 meetrit)
3. Ahi #1: A-korpus, 1. korrus - VABA - 0.2 km (200 meetrit)
```

**Selgitus:** Ainult 3 vaba ahju leiti. Ahi #2 on kasutuses ja #5 on broneeritud, seega ei kuvata neid.

---

### Lihtsustatud kauguse arvutamine

```
FUNKTSIOON arvuta_kaugus(asukoht1, asukoht2):
    // Võtame lihtsustatud lähenemise
    // Eestis 1 kraad ≈ 111 km

    // Arvuta erinevus laiuskraadis ja pikkuskraadis
    lat_erinevus = asukoht2.laiuskraad - asukoht1.laiuskraad
    lon_erinevus = asukoht2.pikkuskraad - asukoht1.pikkuskraad

    // Teisenda kilomeetriteks
    lat_km = lat_erinevus * 111
    lon_km = lon_erinevus * 111

    // Kasuta Pythagorase teoreemi: c² = a² + b²
    kaugus = RUUTJUUR(lat_km * lat_km + lon_km * lon_km)

    TAGASTA kaugus
LÕPP
```

**Näide:**
```
Kasutaja: laiuskraad 59.3947, pikkuskraad 24.6652
Ahi: laiuskraad 59.3950, pikkuskraad 24.6655

lat_erinevus = 0.0003
lon_erinevus = 0.0003

lat_km = 0.0003 * 111 = 0.0333 km
lon_km = 0.0003 * 111 = 0.0333 km

kaugus = RUUTJUUR(0.0333² + 0.0333²) ≈ 0.047 km ≈ 47 meetrit
```

---

## Näide 2: Mikrolaineahju broneerimine

### Kasutajateekond
> **Mari** leidis vaba ahju Mare õppehoone 2. korrusel. Ta soovib selle broneerida 12:30-12:40 ajaks, et kindel olla, et saab oma toitu soojendada.

### Mida rakendus peab kontrollima?

1. ✅ Kas ahi on päriselt vaba?
2. ✅ Kas Mari ei broneeri minevikku?
3. ✅ Kas broneeringaeg on lubatud (max 15 min)?
4. ✅ Kas keegi teine ei ole juba seda aega broneerinud?
5. ✅ Kas Mari ei ole juba teist ahju broneerinud?

---

### Pseudokood: Ahju broneerimine

```
FUNKTSIOON broneeri_ahi(kasutaja, ahi, algus_aeg, kestus):
    // ========================================
    // KONTROLLI 1: Kas aeg on õige?
    // ========================================

    praegune_aeg = PRAEGUNE_AEG()

    // Kas püüab broneerida minevikku?
    KUI algus_aeg < praegune_aeg:
        TAGASTA viga: "Ei saa broneerida minevikku!"

    // Kas kestus on lubatud?
    KUI kestus > 15 minutit:
        TAGASTA viga: "Maksimaalne aeg on 15 minutit!"

    KUI kestus < 1 minut:
        TAGASTA viga: "Minimaalne aeg on 1 minut!"

    // Arvuta lõpu aeg
    lõpp_aeg = algus_aeg + kestus

    // ========================================
    // KONTROLLI 2: Kas ahi on vaba?
    // ========================================

    KUI ahi.olek != "VABA":
        TAGASTA viga: "Ahi pole praegu vaba!"

    // ========================================
    // KONTROLLI 3: Kas on konflikte?
    // ========================================

    // Leia kõik selle ahju broneeringud
    broneeringud = OTSI kõik broneeringud kus ahi_id == ahi.id

    KORDA iga broneering broneeringud listis:
        // Kontrolli kas meie aeg kattub olemasoleva broneeringuga
        KUI meie_aeg_kattub_olemasolevaga(algus_aeg, lõpp_aeg, broneering):
            TAGASTA viga: "Ahi on juba broneeritud ajaks {broneering.algus} - {broneering.lõpp}"

    // ========================================
    // KONTROLLI 4: Kas kasutajal on juba broneering?
    // ========================================

    kasutaja_broneeringud = OTSI broneeringud kus kasutaja_id == kasutaja.id JA staatus == "AKTIIVNE"

    KUI kasutaja_broneeringud.arv > 0:
        TAGASTA viga: "Sul on juba aktiivne broneering!"

    // ========================================
    // KÕIK ON OK - LOO BRONEERING!
    // ========================================

    uus_broneering = LOO uus broneering:
        kasutaja_id = kasutaja.id
        ahi_id = ahi.id
        algus_aeg = algus_aeg
        lõpp_aeg = lõpp_aeg
        staatus = "AKTIIVNE"
        loodud = praegune_aeg

    SALVESTA andmebaasi uus_broneering

    // Muuda ahju olekut
    ahi.olek = "BRONEERITUD"
    SALVESTA andmebaasi ahi

    // Saada teade kasutajale
    SAADA_TEADE kasutajale: "Broneering kinnitatud! Ahi {ahi.asukoht}, {algus_aeg}-{lõpp_aeg}"

    TAGASTA edu: uus_broneering
LÕPP
```

### Abiline funktsioon: Kas ajad kattuvad?

```
FUNKTSIOON meie_aeg_kattub_olemasolevaga(meie_algus, meie_lõpp, olemasolev_broneering):
    olemas_algus = olemasolev_broneering.algus_aeg
    olemas_lõpp = olemasolev_broneering.lõpp_aeg

    // 3 viisi kuidas ajad võivad kattuda:

    // 1. Meie algus on olemasoleva keskel
    KUI meie_algus >= olemas_algus JA meie_algus < olemas_lõpp:
        TAGASTA TRUE  // Kattub!

    // 2. Meie lõpp on olemasoleva keskel
    KUI meie_lõpp > olemas_algus JA meie_lõpp <= olemas_lõpp:
        TAGASTA TRUE  // Kattub!

    // 3. Meie broneering katab kogu olemasoleva broneeringu
    KUI meie_algus <= olemas_algus JA meie_lõpp >= olemas_lõpp:
        TAGASTA TRUE  // Kattub!

    // Ei kattu
    TAGASTA FALSE
LÕPP
```

### Näide samm-sammult

**Olukord:**
- Mari soovib broneerida Ahi #3 (Mare, 2. korrus)
- Aeg: 12:30-12:40 (kestus 10 minutit)
- Praegune aeg: 12:15

**Andmebaasis:**
```
Ahi #3 olek: VABA
Ahi #3 broneeringud:
  - Jaan: 12:00-12:15 (LÕPPENUD)
  - Liis: 12:50-13:00 (AKTIIVNE)

Mari broneeringud: 0 (pole ühtegi)
```

**Algoritmi käik:**

1. ✅ Kontrolli aega: 12:30 > 12:15 (praegune) → OK
2. ✅ Kontrolli kestust: 10 min ≤ 15 min → OK
3. ✅ Kontrolli ahju olekut: "VABA" → OK
4. ✅ Kontrolli konflikte:
   - Jaani broneering (12:00-12:15): Ei kattu (juba lõppenud)
   - Liisi broneering (12:50-13:00): Ei kattu (Mari lõpeb 12:40, Liis algab 12:50)
5. ✅ Kontrolli Mari olemasolevaid broneeringuid: 0 → OK
6. ✅ Loo broneering ja salvesta!

**Tulemus:**
```
✅ Broneering loodud
✅ Ahi #3 olek muudetud: "VABA" → "BRONEERITUD"
✅ Mari saab teate: "Broneering kinnitatud! Ahi Mare 2. korrus, 12:30-12:40"
```

---

### Mis juhtub kui keegi ei ilmu?

```
FUNKTSIOON kontrolli_kas_kasutaja_ilmus(broneering):
    // See funktsioon käivitatakse automaatselt 2 minutit pärast broneeringu algust

    praegune_aeg = PRAEGUNE_AEG()
    kontroll_aeg = broneering.algus_aeg + 2 minutit

    // Kas on aeg kontrollida?
    KUI praegune_aeg < kontroll_aeg:
        TAGASTA  // Ei ole veel aeg

    // Leia ahi
    ahi = OTSI andmebaasist ahi kus id == broneering.ahi_id

    // Kas ahi on "KASUTUSES"? (Tähendab et keegi kasutab)
    KUI ahi.olek == "KASUTUSES":
        // Kasutaja ilmus!
        broneering.kasutaja_ilmus = TRUE
        SALVESTA andmebaasi broneering
        MÄRGI LOGISSE: "Kasutaja ilmus: {broneering.id}"

    MUIDU:
        // Kasutaja EI ILMUNUD - tühista!
        broneering.staatus = "TÜHISTATUD"
        SALVESTA andmebaasi broneering

        // Vabasta ahi
        ahi.olek = "VABA"
        SALVESTA andmebaasi ahi

        // Teavita kasutajat
        SAADA_TEADE kasutajale: "Sinu broneering tühistati, kuna sa ei ilmunud!"

        MÄRGI LOGISSE: "Kasutaja ei ilmunud, broneering tühistatud: {broneering.id}"
LÕPP
```

**Näide:**
```
Mari broneeriS: 12:30-12:40
Kell on nüüd: 12:32 (2 minutit pärast algust)

Ahi #3 olek: "BRONEERITUD" (mitte "KASUTUSES")

Tulemus:
❌ Mari ei kasutanud ahju
✅ Broneering tühistatakse
✅ Ahi muudetakse: "BRONEERITUD" → "VABA"
✅ Teised kasutajad saavad nüüd seda ahju kasutada
```

---

## Näide 3: Toidu pakkumiste filtreerimine

### Kasutajateekond
> **Jaan** otsib toitu, mida keegi jagab. Tal on pähkliallergia ja ta soovib leida ainult läheduses (max 1 km) olevaid pakkumisi.

### Mida rakendus peab tegema?

1. Näita ainult toitu, mis EI sisalda pähkleid
2. Näita ainult toitu, mis on max 1 km kaugusel
3. Sorteeri lähimad enne

---

### Pseudokood: Toidu filtreerimine

```
FUNKTSIOON filtreeri_toitu(kasutaja_asukoht, allergeenid, max_kaugus):
    // ========================================
    // SAMM 1: Leia kõik pakkumised
    // ========================================

    kõik_pakkumised = OTSI andmebaasist kõik toidu pakkumised kus staatus == "AKTIIVNE"

    sobivad_pakkumised = tühi_nimekiri

    // ========================================
    // SAMM 2: Filtreeri iga pakkumine
    // ========================================

    KORDA iga pakkumine kõik_pakkumised listis:

        // Filter 1: Kas sisaldab allergeeni?
        sisaldab_allergeeni = FALSE

        KORDA iga allergeen allergeenid listis:
            KUI allergeen ON pakkumine.allergeenid listis:
                sisaldab_allergeeni = TRUE
                VÄLJU tsüklist

        // Kui sisaldab allergeeni, jäta vahele
        KUI sisaldab_allergeeni == TRUE:
            JÄTKA järgmise pakkumisega

        // Filter 2: Kas on piisavalt lähedal?
        kaugus = ARVUTA kaugus kasutaja_asukoht ja pakkumine.asukoht vahel

        KUI kaugus > max_kaugus:
            JÄTKA järgmise pakkumisega  // Liiga kaugel

        // Läbis kõik filtrid!
        pakkumine.kaugus = kaugus  // Lisa kaugus sorteerimiseks
        LISA sobivad_pakkumised nimekirja pakkumine

    // ========================================
    // SAMM 3: Sorteeri lähimad enne
    // ========================================

    SORTEERI sobivad_pakkumised kauguse järgi

    TAGASTA sobivad_pakkumised
LÕPP
```

### Näide samm-sammult

**Sisend:**
- Jaani asukoht: Mare õppehoone
- Allergeenid: ["pähklid"]
- Max kaugus: 1 km

**Andmebaasis olevad pakkumised:**
```
Pakkumine #1: Ceasar salat
  - Allergeenid: ["pähklid", "piim"]
  - Asukoht: Mare, 1. korrus
  - Kaugus: 0.1 km

Pakkumine #2: Köögivilasalat
  - Allergeenid: ["gluteen"]
  - Asukoht: Mare, 2. korrus
  - Kaugus: 0.05 km

Pakkumine #3: Tomatsupp
  - Allergeenid: []
  - Asukoht: A-korpus
  - Kaugus: 0.3 km

Pakkumine #4: Pannkoogid
  - Allergeenid: ["piim", "munad"]
  - Asukoht: B-korpus
  - Kaugus: 1.5 km
```

**Algoritmi käik:**

**Pakkumine #1:**
- ❌ Sisaldab pähkleid → Jäta vahele

**Pakkumine #2:**
- ✅ Ei sisalda pähkleid
- ✅ Kaugus 0.05 km < 1 km
- ✅ Lisa tulemustesse

**Pakkumine #3:**
- ✅ Ei sisalda pähkleid
- ✅ Kaugus 0.3 km < 1 km
- ✅ Lisa tulemustesse

**Pakkumine #4:**
- ✅ Ei sisalda pähkleid
- ❌ Kaugus 1.5 km > 1 km → Liiga kaugel, jäta vahele

**Tulemus (sorteeritud):**
```
1. Köögivilasalat - 0.05 km (Mare, 2. korrus)
2. Tomatsupp - 0.3 km (A-korpus)
```

---

## Näide 4: Ühisostu maksejaotus

### Kasutajateekord
> **Mari, Jaan ja Liis** tellisid koos pitsat. Mari maksis kogu summa (48€ toidu eest + 5€ kohaletoimetamine). Nüüd nad peavad arvutama, kui palju Jaan ja Liis peavad Marile tagasi maksma.

### Mida rakendus peab arvutama?

1. Jaga kohaletoimetamise tasu võrdselt kõikide vahel
2. Arvuta iga inimese kogusumma
3. Arvuta, kui palju igaüks võlgneb eelmaksjale

---

### Pseudokood: Maksejaotuse arvutamine

```
FUNKTSIOON arvuta_maksejaotus(ühisost):
    // ========================================
    // SAMM 1: Loe andmed
    // ========================================

    osalejad = ühisost.osalejad
    toidu_kogusumma = 0

    // Arvuta toidu kogusumma
    KORDA iga osaleja osalejad listis:
        toidu_kogusumma = toidu_kogusumma + osaleja.toidu_summa

    kohaletoimetamine = ühisost.kohaletoimetamise_tasu
    kogusumma = toidu_kogusumma + kohaletoimetamine

    // ========================================
    // SAMM 2: Jaga kohaletoimetamine võrdselt
    // ========================================

    kohaletoimetamine_per_inimene = kohaletoimetamine / osalejad.arv

    // ========================================
    // SAMM 3: Arvuta iga inimese osa
    // ========================================

    maksejaotus = tühi_nimekiri

    KORDA iga osaleja osalejad listis:
        osaleja_osa = osaleja.toidu_summa + kohaletoimetamine_per_inimene

        // Kas see inimene maksis ette?
        KUI osaleja.maksis_ette == TRUE:
            // Eelmaksja saab raha TAGASI
            saab_tagasi = kogusumma - osaleja_osa
            võlgnevus = 0
        MUIDU:
            // Tavaline osaleja VÕLGNEB
            saab_tagasi = 0
            võlgnevus = osaleja_osa

        // Lisa tulemustesse
        LISA maksejaotus nimekirja:
            nimi = osaleja.nimi
            toidu_summa = osaleja.toidu_summa
            kohaletoimetamise_osa = kohaletoimetamine_per_inimene
            kokku = osaleja_osa
            võlgneb = võlgnevus
            saab_tagasi = saab_tagasi

    TAGASTA maksejaotus
LÕPP
```

### Näide samm-sammult

**Sisend:**
```
Ühisost:
  - Mari: 2 pitsat = 24€ (maksis kogu summa 53€ ette)
  - Jaan: 1 pitsa = 12€
  - Liis: 1 pitsa = 12€
  - Kohaletoimetamine: 5€
```

**Arvutamine:**

**Samm 1:** Toidu kogusumma
```
Toidu kogusumma = 24€ + 12€ + 12€ = 48€
Kogusumma (koos kohaletoimetamisega) = 48€ + 5€ = 53€
```

**Samm 2:** Kohaletoimetamine per inimene
```
Kohaletoimetamine per inimene = 5€ / 3 = 1.67€
```

**Samm 3:** Iga inimese osa

**Mari:**
```
Toidu summa: 24€
Kohaletoimetamine: 1.67€
Kokku: 25.67€

Mari maksis ette: 53€
Mari peaks saama: 53€ - 25.67€ = 27.33€ tagasi
```

**Jaan:**
```
Toidu summa: 12€
Kohaletoimetamine: 1.67€
Kokku: 13.67€

Jaan võlgneb Marile: 13.67€
```

**Liis:**
```
Toidu summa: 12€
Kohaletoimetamine: 1.67€
Kokku: 13.67€

Liis võlgneb Marile: 13.67€
```

**Kontroll:**
```
Jaan maksab: 13.67€
Liis maksab: 13.67€
Kokku: 27.34€ (≈ 27.33€ - väike erinevus ümardamise tõttu)

Mari saab: 27.33€ tagasi ✅
```

**Väljund:**
```
Mari: Maksid 53€, saad 27.33€ tagasi
Jaan: Pead maksma Marile 13.67€
Liis: Pead maksma Marile 13.67€
```

---

## Kokkuvõte: Mida sa pead tegema Sprint 3-s?

### Kui sa oled **Developer (arendaja)**:
1. ✅ Kirjuta pseudokood 3-4 peamise funktsiooni jaoks
2. ✅ Kirjelda, kuidas algoritm töötab (kommentaaridega)
3. ✅ Lisa testjuhtumid (sisend → väljund)
4. ✅ Selgita tehnilisi otsuseid

### Kui sa oled **UX/UI Designer**:
1. ✅ Kirjelda, kuidas kasutajaliides valideerib sisendeid
2. ✅ Kirjuta, milliseid veateateid millal näidata
3. ✅ Selgita, mis juhtub kui kasutaja teeb vea

### Kui sa oled **Product Owner**:
1. ✅ Kontrolli, kas pseudokood vastab kasutajate vajadustele
2. ✅ Kinnita, et algoritm lahendab õige probleemi
3. ✅ Lisa ärilised nõuded

### Kui sa oled **Project Manager**:
1. ✅ Jälgi, et kõik saavad oma ülesanded tehtud
2. ✅ Dokumenteeri probleeme (blockerid)
3. ✅ Uuenda burndown chart'i

---

## Näpunäited pseudokoodi kirjutamiseks

### ✅ Hea pseudokood:

```
FUNKTSIOON leia_lähim_vaba_ahi(kasutaja_asukoht):
    // Leia kõik ahjud
    kõik_ahjud = OTSI andmebaasist kõik ahjud

    lähin_ahi = NULL
    väikseim_kaugus = VÄGA_SUUR_NUMBER

    // Vaata iga ahi läbi
    KORDA iga ahi kõik_ahjud:
        // Kas ahi on vaba?
        KUI ahi.olek == "VABA":
            kaugus = ARVUTA kaugus kasutaja_asukoht ja ahi.asukoht vahel

            // Kas see on lähim seni?
            KUI kaugus < väikseim_kaugus:
                lähin_ahi = ahi
                väikseim_kaugus = kaugus

    TAGASTA lähin_ahi
LÕPP
```

**Miks see on hea:**
- ✅ Selged muutujate nimed (eesti keeles!)
- ✅ Kommentaarid selgitavad iga sammu
- ✅ Lihtne loogika (IF, KORDA)
- ✅ Igaüks saab aru, isegi ilma programmeerimisoskusteta

---

### ❌ Halb pseudokood:

```
FUNKTSIOON f(x):
    a = SELECT * FROM t
    b = NULL
    c = 9999
    FOR i IN a:
        IF i.s == "V":
            d = calc(x, i.l)
            IF d < c:
                b = i
                c = d
    RETURN b
LÕPP
```

**Miks see on halb:**
- ❌ Ebaselged muutujate nimed (a, b, c, x - mis need on?)
- ❌ Puuduvad kommentaarid
- ❌ Segab eesti ja inglise keelt
- ❌ Raske aru saada, mida funktsioon teeb

---

## Kasulikud sõnad pseudokoodi jaoks

**Eesti keeles:**
- `FUNKTSIOON` - funktsioon/algoritm
- `TAGASTA` - return (anna tulemus tagasi)
- `KUI` - if (tingimus)
- `MUIDU` - else (vastasel juhul)
- `KORDA` - for/while (korda tsükkel)
- `JA` - and (loogiline JA)
- `VÕI` - or (loogiline VÕI)
- `OTSI` - päring andmebaasist
- `SALVESTA` - salvesta andmebaasi
- `LISA` - add (lisa nimekirja)
- `ARVUTA` - calculate (arvuta)
- `PRAEGUNE_AEG()` - praegune kellaaeg
- `RUUTJUUR()` - square root

---

## Mida sa õpid pseudokoodiga töötades?

1. 🧠 **Algoritmilise mõtlemise** - kuidas jagada suur probleem väikesteks sammudeks
2. 📊 **Loogika planeerimise** - mis peab juhtuma enne mida
3. ⚠️ **Veatöötluse** - mis võib minna valesti ja kuidas seda käsitleda
4. 👥 **Meeskonnatöö** - kuidas selgitada oma ideed teistele
5. 📝 **Dokumenteerimise** - miks on oluline kirjutada selgeid selgitusi

---

**Edu Sprint 3-s! Küsi julgelt abi, kui midagi ei ole selge.**
