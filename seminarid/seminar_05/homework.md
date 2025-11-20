# Kodutöö 5: Sprint 3 - Arendamine (Simuleerimine)

**Kodutöö = Sprint 3 Issues täitmine**

## Ülevaade

Sprint 3 on arenduse simulatsioon - te EI kirjuta koodi, vaid dokumenteerite ja simuleerite arendusprotsessi. Eesmärk on mõista, kuidas päris arendusmeeskond töötab.

---

## Kohustuslikud ülesanded

### 1. Loo Sprint 3 plaan
**Fail:** `sprint-3-plan.md`

**Sisu:**
- Sprint Goal (1 lause - mida tahate saavutada?)
- Selected tasks (mis ülesanded Sprint 3-sse võtate? Loetlege 5-10 ülesannet)
- Team members (kes mida teeb?)
- Definition of Done (millal on Sprint valmis?)

---

### 2. Ülesannete jaotus
**Fail:** `task-breakdown.md`

**Ülesanne:**
- Vali 1 peamine funktsioon teie projektist
- Kirjelda, mida see funktsioon teeb (1-2 lauset)
- Jaga 5-10 ülesandeks
- Iga ülesanne peab sisaldama:
  - Ülesande kirjeldus (mida tehakse?)
  - Tüüp (Disain/Programmeer imine/Testimine/Dokument atsioon)
  - Vastutaja (kes teeb?)
  - Staatus (Tehtud/Pooleli/Ei alanud)

**Näide struktuuri:**
```markdown
# Funktsioon: Mikrolaineahju broneerimine

## Mida see funktsioon teeb?
Kasutaja saab broneerida vaba mikrolaineahju kuni 15 minutiks.

## Ülesanded:
1. **Disaini broneerimise ekraan** (Disain) - @mari - Tehtud
2. **Kirjuta pseudokood broneerimise loogikale** (Programmeerimine) - @jaan - Pooleli
3. **Testi broneerimist erinevate stsenaariumidega** (Testimine) - @liis - Ei alanud
...
```

---

### 3. Daily Standups (simuleeritud)
**Fail:** `daily-standups.md`

**Ülesanne:**
- Kirjuta 10 päeva standup kirjeid (simuleeritud 2 nädalat)
- Iga päev KÕIK meeskonnaliikmed kirjutavad:
  - Mida "eile" tegid
  - Mida "täna" teevad
  - Mis "takistab"

**Oluline:** Simuleeritud tähendab, et kirjutate 3. dets korraga kõik 10 päeva kirjed, kujutades ette mis oleks tegelikult juhtunud.

**Template iga päeva kohta:**
```markdown
## Päev X [Kuupäev]

### Mari (UX Designer)
**Eile:** Lõpetasin wireframe'i parandused
**Täna:** Alustan kasutajatestide dokumenteerimist
**Takistab:** Ei ole kindel, kas wireframe on piisavalt detailne

### Jaan (Developer)
**Eile:** Kirjeldasin tehnilise arhitektuuri
**Täna:** Dokumenteerin API endpoint'e
**Takistab:** Ei ole veel otsustanud andmebaasi struktuuri
```

---

### 4. Sprint Progress Tracking
**Fail:** `sprint-progress.md`

**Sisu:**
- Ülesannete progress (mitu tehtud, mitu pooleli, mitu alustamata)
- Blockerite log (mis takistas tööd?)
- Päevade kaupa progress

**Template:**
```markdown
# Sprint 3 Progress

## Progress ülevaade

| Päev | Tehtud ülesanded | Pooleli | Alustamata | Märkused |
|------|------------------|---------|------------|----------|
| 1    | 0                | 1       | 9          | Sprint algus, alustasin disainiga |
| 2    | 1                | 2       | 7          | Disain valmis, alustasin pseudokoodiga |
| 3    | 2                | 2       | 6          | 2 ülesannet valmis |
...
| 10   | 10               | 0       | 0          | Sprint valmis! |

## Tulemus
- **Planeeritud:** 10 ülesannet
- **Täidetud:** 10 ülesannet
- **Lõpetamata:** 0 ülesannet

## Blockerid
1. **Päev 3:** Ei tea, kuidas pseudokoodi kirjutada (lahendatud: uurisin näiteid)
2. **Päev 7:** Ootan teammate'i tagasisidet (lahendatud päev 8)
```

---

### 5. Tehnilised otsused
**Fail:** `technical-decisions.md`

**Ülesanne:**
- Dokumenteeri 3 tehnilist otsust, mida teie projekt nõuab
- Selgita, MIKS see otsus tehti

**Näited tehnilistest otsustest:**
- Mobile-first vs Desktop-first
- Millist andmebaasi kasutada (SQL vs NoSQL)
- REST API vs GraphQL
- Single Page App vs Multi-Page App
- Autentimine (JWT vs Session)

**Template:**
```markdown
# Tehnilised Otsused

## Otsus 1: Mobile-First lähenemine

**Probleem:** Kas arendame esmalt mobile või desktop versiooni?

**Otsus:** Mobile-first

**Põhjendus:**
- 85% kasutajatest on mobiilseadmetel
- Lihtsam skaleerida mobile → desktop kui vastupidi
- Sunnib keskenduma olulistele funktsioonidele

**Alternatiivid kaalutud:**
- Desktop-first (keeruline, liiga palju funktsioone)
- Samaaegselt (ressursside puudus)

**Mõju projekti:**
- UI disain algab 375px ekraanist
- Naviga atsioon on bottom navigation bar
- Kõik funktsioonid peavad töötama puutetundliku ekraaniga
```

---

### 6. Sprint 3 Review
**Fail:** `sprint-3-review.md`

**Sisu:**
- Mis "valmis sai" (simulatsiooni tulemus)
- Kas Sprint Goal saavutati?
- Mis läks plaanist erinevalt?
- Stakeholder'ite tagasiside (teiste meeskondade kommentaarid)

---

### 7. Sprint 3 Retrospective
**Fail:** `sprint-3-retrospective.md`

**Sisu:**
- Start-Stop-Continue analüüs
- Iga meeskonnaliikme refleksioon
- Action items järgmiseks (kuigi järgmist Sprinti pole)

**Template:**
```markdown
# Sprint 3 Retrospective

## Start-Stop-Continue

### CONTINUE (mis läks hästi)
- Epic breakdown aitas mõista töö ulatust
- Daily standup simulation oli kasulik
- Meeskond töötas hästi koos

### STOP (mida lõpetada)
- Liiga optimistlik estimating
- Unustasime testing task'id alguses

### START (mida alustada)
- Varem breakdown teha
- Rohkem technical research'i

## Individuaalsed reflektsioonid

### Mari (UX Designer)
Õppisin kuidas arendajad mõtlevad UI implementeerimisest. Mõistsin, et minu wireframe'id peavad olema detailsemad - peab märkima interaktsioone ja state'e. Sprint simulation aitas näha, kui oluline on järjepidev kommunikatsioon.

### Jaan (Developer)
...
```

---

## Rolli-põhised lisaülesanded

### Product Owner
**Fail:** `backlog-refinement.md`

**Sisu:**
- Kuidas backlog'i täpsustati Sprint 3 käigus
- Milliseid user story-sid prioritiseeriti
- Millised nõuded muutusid ja miks
- Aktsepteerimiskriteeriumid pseudokoodile (kas vastab kasutajate vajadustele?)

---

### Project Manager
**Fail:** `blockers-log.md`

**Sisu:**
- Kõik blockerid detailselt
- Kuidas igaüks lahendati
- Mõju Sprint timeline'le
- Õppetunnid blockerite vältimiseks

---

### Developer
**Fail:** `algorithms/` (kaust pseudokoodiga)

**Sisu:**
- Kirjuta **3-4 pseudokoodi algoritmi** põhifunktsioonide jaoks
- Iga algoritm peab sisaldama:
  - Kasutajateekond (kes, mida, miks?)
  - Pseudokood (lihtsas eesti keeles)
  - Testjuhtumid (sisend → väljund)
  - Edge case'id (mis võib minna valesti?)

**Näited:**
- Broneerimise loogika
- Otsingu/filtreerimise algoritm
- Andmete töötlemise algoritm
- Maksejaotuse arvutamine

**Vaata näiteid:** `pseudocode-examples.md` failist!

**Fail:** `technical-architecture.md`

**Sisu:**
- Süsteemi arhitektuur (komponendid)
- Andmevoog läbi süsteemi
- Tehnoloogia stack (mis tööriistadega ehitataks)
- Integratsioonid (API-d, kolmandad osapooled)

---

### UX/UI Designer
**Fail:** `ui-logic.md`

**Sisu:**
- Kuidas kasutajaliides valideerib sisendeid (pseudokoodiga)
- Milliseid veateateid millal näidata
- Kuidas UI reageerib kasutaja tegevustele
- Loading state'id ja error state'id

**Näide:**
```markdown
## Broneerimisvormi valideerimine

FUNKTSIOON valideeri_broneerimise_vorm(algus_aeg, kestus):
    KUI kestus > 15 minutit:
        NÄITA veateade: "Maksimaalne aeg on 15 minutit"
        BLOKEERI nupp "Broneeri"

    KUI algus_aeg < PRAEGUNE_AEG():
        NÄITA veateade: "Ei saa broneerida minevikku"
        BLOKEERI nupp "Broneeri"

    MUIDU:
        AKTIVEERI nupp "Broneeri"
LÕPP
```

**Fail:** `usability-testing-plan.md`

**Sisu:**
- Kuidas wireframe'e testiti (või testitaks)
- Testimise protokoll
- Oodatavad tulemused
- Kuidas tulemusi kasutataks järgmistes iteratsioonides

---

## GitHub Workflow

### Branchid ja Pull Request'id

```bash
# 1. Loo uus branch
git checkout -b feature/sprint-3

# 2. Loo kaust ja failid
mkdir sprint3
cd sprint3
# Loo kõik vajalikud .md failid

# 3. Commit ja push
git add .
git commit -m "Add Sprint 3 simulation documentation"
git push origin feature/sprint-3

# 4. Loo Pull Request GitHub-is
# Title: "Sprint 3: Arenduse simuleerimine"
# Description: Kirjelda, mida tegite ja mida õppisite

# 5. Peer review - teised meeskonnaliikmed vaatavad üle

# 6. Merge main'i pärast approval'eid
```

---

## GitHub Issues

Loo järgmised Issues oma projekti:

**Issue #X:** Ülesannete jaotus - vali funktsioon ja jaga ülesanneteks
**Issue #X:** Daily standup simulation - 10 päeva kirjeid
**Issue #X:** Technical decisions - dokumenteeri 3 otsust
**Issue #X:** Sprint progress tracking - ülesannete progress päevade kaupa
**Issue #X:** Sprint review - kokkuvõte Sprint 3 tulemustest
**Issue #X:** Retrospective - refleksiooni sprint 3 kohta

**Labels:**
- `Sprint-3`
- `documentation`
- `simulation`

**Assignees:** Jaga issues meeskonnaliikmete vahel vastavalt rollidele

---

## Repositooriumi struktuur

```
project_root/
├── sprint1/
│   └── ... (Sprint 1 failid)
├── sprint2/
│   └── ... (Sprint 2 failid)
├── sprint3/                          ← UUS!
│   ├── README.md                     (ülevaade Sprint 3 kohta)
│   ├── sprint-3-plan.md              (kohustuslik)
│   ├── task-breakdown.md             (kohustuslik - asendab epic-breakdown)
│   ├── daily-standups.md             (kohustuslik)
│   ├── sprint-progress.md            (kohustuslik)
│   ├── technical-decisions.md        (kohustuslik)
│   ├── sprint-3-review.md            (kohustuslik)
│   ├── sprint-3-retrospective.md     (kohustuslik)
│   ├── algorithms/                   (Developer - pseudokood!)
│   │   ├── algorithm-1.md
│   │   ├── algorithm-2.md
│   │   └── payment-split-algorithm.md
│   ├── ui-logic.md                   (UX - kasutajaliidese loogika)
│   ├── backlog-refinement.md         (PO)
│   ├── blockers-log.md               (PM)
│   ├── technical-architecture.md     (Dev)
│   └── usability-testing-plan.md     (UX)
└── README.md
```

---

## Hindamiskriteeriumid

### 1. Completeness (25%)
- Kas kõik kohustuslikud failid on olemas?
- Kas rolli-põhine fail on olemas?
- Kas GitHub Issues on loodud?

### 2. Detail Level (25%)
- Kas epic breakdown on piisavalt detailne?
- Kas daily standup'id on realistlikud?
- Kas technical decisions on põhjendatud?

### 3. Realism (25%)
- Kas võiks olla päris Sprint?
- Kas velocity on realistlik?
- Kas blockerid on usutavad?

### 4. Team Coordination (25%)
- Kas kõik meeskonnaliikmed panustasid?
- Kas kommunikatsioon on dokumenteeritud?
- Kas peer review tehti korralikult?

---

## Tähtaeg

**1 nädal pärast seminari**

**Esitamine:**
1. Push kõik muudatused GitHub'i
2. Loo Pull Request
3. Peer review (kõik meeskonnaliikmed vaatavad üle)
4. Merge main branch'i
5. Lisa `submission` label oma esimesele Issue-le
6. Lisa Assignee-ks õpetaja

---

## Näpunäited

1. **Austa simulatsiooni:** Kirjuta nii, nagu see oleks päris Sprint. Realistlikud blockerid, realistlik progress.

2. **Kasuta seminari materjale:** Epic breakdown, mille te seminaris tegite, on hea alus.

3. **Õpi arendajate mõtteviisist:** Kuigi te ei koodi, mõelge kuidas arendajad tehnilisi otsuseid teevad.

4. **Kommunikatsioon on võti:** Daily standup'id peavad näitama, kuidas meeskond koordineerib tööd.

5. **Ole aus retrospective'is:** Kirjuta, mida te tegelikult õppisite, mitte mis kõlab hästi.

---

## Küsimused?

Kui midagi on ebaselge, küsi:
- GitHub Discussions'is oma repositooriumis
- Seminari järel õpetajalt
- Teistelt meeskondadelt

---

> [!NOTE]
> Õppematerjalid leiad [siit](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse)

> [!IMPORTANT]
> **Selle ülesande lahendus lisa GitHub'i**
> - Loo pull request kõigi failidega
> - Lisa "submission" label
> - Assignee-ks õpetaja
> - Tähtaeg: 1 nädal pärast seminari
