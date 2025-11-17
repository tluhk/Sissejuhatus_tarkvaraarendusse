# Seminar 5: Sprint 3 - Arendamine (Simuleerimine)

---

## Täna õpime

1. **Sprint 2 Review ja Retrospective** - disaini tulemuste ülevaade
2. **Epic Breakdown** - suurte ülesannete jagamine
3. **Story Points ja Estimating** - keerukuse hindamine
4. **Sprint Metrics** - velocity, burndown charts
5. **Sprint Simulation** - 2 nädala arendus 40 minutiga

---

## Seminari struktuur

- **30 min** - Sprint 2 Review & Retrospective
- **90 min** - Teooria (Epic breakdown, metrics, communication)
- **90 min** - Praktika (Sprint simulation, burndown tracking)

---

## Oluline!

**Me EI koodi!**

Täna simuleerime arendusprotsessi:
- Kuidas arendajad ülesandeid jagavad
- Kuidas meeskonnad koostööd teevad
- Kuidas progressi jälgitakse
- Mis toimub "päris" Sprint 3 ajal

---

# Sprint 2 Review
## "Mida me disainisime?"

---

## Sprint 2 Review eesmärk

- **Demonstreerida** Sprint 2 disaini tulemusi
- **Näidata** wireframe'e ja personaid
- **Kinnitada** et olemevalmis "arendamiseks"
- **Saada tagasiside** teistelt meeskondadelt

---

## Demo struktuur (15 min)

1. **Sprint 2 eesmärk** (2 min)
2. **Disaini tulemused** (10 min)
   - Personas
   - Wireframes
   - User journeys
3. **Sprint 2 mõõdikud** (3 min)

---

## Teie demo

**Iga meeskond (2 min):**
- Näita 2-3 persoonat
- Näita wireframe'e (pildid)
- Selgita user journey
- Ütle, mitu SP täitsite

**Teised meeskonnad küsivad:**
- "Kuidas see tehniliselt töötab?"
- "Kas see on kasutajale arusaadav?"

---

## Sprint 2 mõõdikud

Näide:

- **Planeeritud**: 16 Story Points
- **Täidetud**: 18 Story Points (112%)
- **Velocity**: 18 SP
- **Wireframe'id**: 8 ekraani
- **Personas**: 3 detailset

---

# Sprint 2 Retrospective
## "Kuidas me disainisime?"

---

## Retrospective eesmärk

- **Analüüsida** Sprint 2 disaini protsessi
- **Leida** parandamise võimalusi
- **Valmistuda** Sprint 3-ks (arendus)
- **Tugevdada** meeskonda

---

## Start-Stop-Continue meetod

**CONTINUE** - Mis läks hästi disainis?

**STOP** - Mida lõpetada?

**START** - Mida proovida Sprint 3-s?

---

## Näide: "FindFood" Retrospective

**CONTINUE**
- Wireframe'id olid selged
- Personas aitasid fokuseerida
- User journey oli kasulik

**STOP**
- Liiga palju detaile prototüüpides
- Unustasime error state'id

**START**
- Task breakdown varem
- Rohkem kasutajate testimist

---

## Action Items Sprint 3-ks

Iga meeskond valib 2 action item'it:

Näited:
- "Kirjutame technical decisions dokumenti"
- "Kasutame GitHub Projects'i aktiivsemalt"
- "Teeme daily standup'e järjepidevamalt"

---

# Epic Breakdown
## Suurtest ülesannetest väikesteks

---

## Hierarhia: Projekt → Epic → User Story → Task

```
PROJEKT: FindFood
  └── EPIC: Restoranide otsing
      └── USER STORY: Kasutaja näeb lähimaid restorane
          └── TASK 1: Loo kaardi komponent (UI)
          └── TASK 2: Hangi kasutaja asukoht (Backend)
          └── TASK 3: Lae restoranide andmed (Backend)
          └── TASK 4: Kuva restoranid kaardil (UI)
          └── TASK 5: Testi kaardi laadimist (Testing)
```

---

## Miks me jagame väiksemaks?

**Suured ülesanded on:**
- Raske hinnata
- Raske jagada
- Raske jälgida
- Raske testida

**Väikesed task'id on:**
- Selged
- 1-3 päeva töö
- Konkreetsed
- Testitavad

---

## Task'ide 5 tüüpi

1. **UI/Frontend**: Ekraanid, nupud, disain
2. **Backend/Logic**: Andmete töötlemine, äriloogika
3. **Database**: Andmete salvestamine
4. **Testing**: Kas kõik töötab?
5. **Documentation**: Kuidas kasutada?

---

## Näide: "FindFood" Epic Breakdown

**EPIC**: Kasutaja registreerimine

**USER STORY 1**: Kasutaja saab e-posti teel registreerida
- TASK: Loo registreerimise ekraan (UI) - 3 SP
- TASK: Valideeri e-posti formaat (Backend) - 2 SP
- TASK: Salvesta kasutaja andmebaasi (Database) - 3 SP
- TASK: Saada kinnitusmail (Backend) - 2 SP
- TASK: Testi registreerimist (Testing) - 2 SP

**USER STORY 2**: Kasutaja saab parooli taastada
- TASK: ... (sarnane breakdown)

---

## Task'i hea kriteerium

**Hea task:**
- 1 inimene saab 1-3 päevaga valmis
- On selge Definition of Done
- Ei sõltu liiga paljudest teistest task'idest
- On max 5 Story Points

**Halb task:**
- "Tee rakendus valmis" (liiga suur)
- "Paranda kõik" (ebaselge)
- "Uuri midagi" (ei ole lõppu)

---

# Story Points ja Estimating
## Keerukuse hindamine

---

## Story Points meeldetuletus

**Story Point = Keerukus, MITTE aeg**

```
1 SP: Lihtne - teame täpselt kuidas
2 SP: Selge - väike töö
3 SP: Keskmine - mõtlemist vajavad
5 SP: Keeruline - uurimist vajab
8 SP: Väga keeruline - peaks jagama!
13 SP: Liiga suur - JAGA KINDLASTI!
```

**Fibonacci skeem**: 1, 2, 3, 5, 8, 13

---

## Miks Fibonacci?

Suuremad numbrid = suurem ebakindlus

```
1-3 SP vahel: väike erinevus (lihtsad task'id)
5-8 SP vahel: suur erinevus (keerulised task'id)
```

Kui ei suuda valida 5 vs 8 - task on liiga suur, jaga väiksemaks!

---

## Planning Poker

**Kuidas hinnata:**

1. Product Owner kirjeldab task'i
2. Iga liige valib saladuses oma hinnangu (1-13)
3. Kõik näitavad korraga
4. Kõige kõrgem ja madalaim selgitavad oma põhjendust
5. Arutelu ja uus hinnang
6. Konsensus

---

## Planning Poker näide

**TASK**: "Loo sisselogimise ekraan"

```
Mari (UX): 2 SP - "Mul on wireframe olemas"
Jaan (Dev): 5 SP - "Peab valideerima sisendeid"
Liisa (PO): 3 SP - "Keskmine keerukus"
Marko (PM): 5 SP - "Nõustun Jaaniga"

Arutelu → Konsensus: 3 SP
Põhjus: UI on lihtne, aga validation teeb keerulisemaks
```

---

## Tavalised estimeerimise vead

**Liiga optimistlik:**
- "See on lihtne!" (aga tegelikult ei ole)
- Unustame testimise, dokumentatsiooni

**Liiga pessimistlik:**
- "See on võimatu!" (aga tegelikult keskmine)
- Kartame tundmatut

**Scope creep:**
- Task muutub töö käigus suuremaks
- "Aga me peaksime ka seda tegema..."

---

# Arenduse Meetrikad
## Kuidas jälgida progressi?

---

## Velocity - Meeskonna kiirus

**Velocity** = Story Points täidetud per Sprint

**Näide "Kooli Köök":**
```
Sprint 1: 15 SP (planeerimine)
Sprint 2: 18 SP (disain) - kasvas!
Sprint 3 plaan: 17-19 SP (realistlik)
```

**Velocity kasvab:** Meeskond õpib koostööd
**Velocity langeb:** Probleemid, blockerid

---

## Velocity kasutamine

**Planeerimisel:**
- Sprint 2 velocity: 18 SP
- Sprint 3 capacity: 17-19 SP (realistlik)
- Ära planeeri 30 SP - see on ebareaalne!

**Analüüsimisel:**
- Kas velocity on stabiilne?
- Miks muutus?
- Kas meeskond on ülekoormatud?

---

## Burndown Chart

**Burndown Chart** näitab, kui palju tööd on alles

```
SP
20 |\
   | \            Ideaalne joon
15 |  \____       (püsiv langus)
   |      \
10 |       \____  Tegelik joon
   |            \ (ei lange ühtlaselt)
 0 |____________\
   D1 D3 D5 D7 D9 (Päevad)
```

---

## Burndown Chart analüüs

**Ideaalne joon:**
- Langeb ühtlaselt
- Jõuab 0-ni Sprint lõpuks

**Tegelik joon:**
- Alguses aeglane (setup, planeerimine)
- Keskpaigas kiire (produktiivne töö)
- Lõpus taas aeglane (testimine, parandused)

**Ohumärgid:**
- Joon ei lange → Blocker!
- Joon tõuseb → Uued task'id lisatud!

---

## Blockers - Takistused

**Blocker** = Takistus, mis peatab töö

**Tüübid:**
```
Dependency Blocker:
"Ma ei saa jätkata, kuni X teeb Y valmis"

Knowledge Blocker:
"Ma ei tea, kuidas seda teha"

Resource Blocker:
"Meil pole ligipääsu sellele tööriistale"

External Blocker:
"Ootame kliendi tagasisidet"
```

---

## Blockerite juhtimine

**Kui märkad blocker'it:**
1. Kirjuta GitHub Issues'sse
2. Maini inimest, kes saab aidata
3. Otsi alternatiivsed task'id
4. Küsi abi daily standup'is

**Project Manager jälgib:**
- Kui kaua blocker kestab?
- Kes saab aidata?
- Kas see mõjutab Sprint goal'i?

---

# Daily Standups
## Igapäevane koordineerimine

---

## Daily Standup formaat

**3 küsimust:**

```
1. Mida ma EILE tegin?
2. Mida ma TÄNA teen?
3. Mis mind TAKISTAB?
```

**Reeglid:**
- Max 15 minutit kogu meeskonnale
- Mitte probleemide lahendamine
- Ainult info jagamine
- Kui probleem suur → eraldi arutelu

---

## Asünkroonne Standup GitHub-is

**Template:**
```markdown
## Daily Standup [17.11.2025]
**Nimi:** Mari
**Roll:** UX Designer

### Eile tegin:
- Lõpetasin wireframe'i testimise
- Sain 3 tudengilt tagasisidet

### Täna teen:
- Parandused wireframe'is
- Uuendan GitHub Projects board'i

### Mind takistab:
- Ei tea, kas peaksin komponente
  veel detailsemaks tegema
```

---

## Standup head tavad

**DO:**
- Ole aus takistuste kohta
- Tag-i inimesi, kellelt vajad vastust (@nimi)
- Paku abi teistele
- Uuenda GitHub Projects board'i

**DON'T:**
- "Ma ei tea, mida teha" (küsi kohe abi!)
- "Kõik on hästi" (kui tegelikult ei ole)
- "Ma lihtsalt ei jõudnud" (selgita põhjust)

---

# Continuous Integration (CI)
## Automaatne kvaliteedikontroll

---

## Mis on CI/CD?

**CI = Continuous Integration** = Pidev kokkupanemine
**CD = Continuous Deployment** = Pidev avaldamine

**Analoogia: Lego ehitamine**
- Iga kord kui keegi lisab tüki, kontrollime kas sobib kokku
- Kui ei sobi, märkame KOHE (mitte 2 nädala pärast!)

---

## Ilma CI-ta

```
5 inimest ehitavad erinevaid osi 2 nädalat

Sprint lõpus:
"Paneme kokku!"

Tulemus:
- Osad ei sobi kokku
- Konfliktid koodis
- 3 päeva parandamist
```

---

## CI-ga

```
Iga päev:
1. Keegi lisab muudatuse
2. Automaatne test: "Kas kõik töötab?"
3. Kui ei tööta → parandame KOHE

Sprint lõpus:
"Juba kokku pandud!"

Tulemus:
- Kõik töötab
- Vähem strssi
- Kiirem release
```

---

## GitHub Actions näide

**Automaatsed ülesanded:**

```yaml
Iga kord kui keegi teeb commit'i:
1. Kontrolli: Kas kõik failid on olemas?
2. Kontrolli: Kas README on kirjutatud?
3. Kontrolli: Kas test läbib?
4. Kui kõik OK → merge lubatud
5. Kui ERROR → märgista punasega
```

**Te ei pea veel kasutama, aga hea teada!**

---

# Praktika
## Sprint 3 Planning

---

## Sprint 3 eesmärk

**Sprint Goal:**

"Põhifunktsioonid on tehniliselt kirjeldatud,
ülesanded jagatud ja simuleeritud arendusprotsess
läbi viidud dokumentatsiooni kaudu."

**Oluline:** Me ei koodi, me SIMULEERIME arendust!

---

## Sprint 3 Capacity

**Võta Sprint 2 velocity:**
- Näide: 18 SP

**Sprint 3 on simulatsioon:**
- Vähem töö (15-17 SP)
- Fookus: breakdown, tracking, simulation

**Teie meeskonna capacity:**
- Iga liige hindab ise
- Kokku 15-17 SP

---

## Sprint 3 kohustuslikud ülesanded

```
1. Epic Breakdown (5 SP)
   - Vali 1 Epic
   - Jaga User Story-deks
   - Jaga Task-ideks

2. Technical Specification (5 SP)
   - Kirjelda tehnilisi otsuseid
   - Dokumenteeri arhitektuur

3. Daily Standup Simulation (3 SP)
   - 10 päeva standup kirjeid (simuleeritud)

4. Sprint Progress Tracking (2 SP)
   - Burndown chart
   - Velocity analüüs

Kokku: 15 SP
```

---

# Epic Breakdown Workshop
## Teie projektiga

---

## Samm 1: Vali Epic (5 min)

**Teie meeskond valib:**

1 peamine Epic teie projektist

**Näited:**
- "FindFood": Restoranide otsing ja kuvamine
- "Kooli Köök": Mikrolaineahjude broneerimissüsteem

**Küsimus:** Milline on teie projekti kõige tähtsam funktsioon?

---

## Samm 2: Jaga User Story-deks (10 min)

**Template:**

```
EPIC: [Teie Epic nimi]

  USER STORY 1: Kui [kasutaja], siis soovin
                [funktsioon], et [väärtus]

  USER STORY 2: ...

  USER STORY 3: ...
```

**Eesmärk:** 3-5 User Story't Epic'u kohta

---

## Näide: "FindFood" Breakdown

```
EPIC: Restoranide otsing

  US1: Kui näljas tudeng, siis soovin näha
       kõiki restorane kaardil, et leida lähim

  US2: Kui tudeng, siis soovin filtreerida
       restorane hinna järgi, et leida odavam

  US3: Kui tudeng, siis soovin näha restorani
       lahtiolekuaegu, et teada kas avatud
```

---

## Samm 3: Jaga Task-ideks (15 min)

**Võta 1 User Story ja jaga:**

```
USER STORY: [Nimi]
  UI TASK: Loo...
  BACKEND TASK: Töötle...
  DATABASE TASK: Salvesta...
  TESTING TASK: Testi...
  DOCS TASK: Dokumenteeri...
```

**Iga task saab Story Point'i (Planning Poker!)

---

## "FindFood" US1 Task Breakdown

```
US1: Restoranide kuvamine kaardil

  TASK 1 (UI): Loo kaardi komponent - 2 SP
  TASK 2 (Backend): Hangi GPS asukoht - 2 SP
  TASK 3 (Backend): Lae restoranide andmed - 3 SP
  TASK 4 (Backend): Filtreeri 2km raadiuses - 2 SP
  TASK 5 (UI): Kuva restoranid markeritena - 3 SP
  TASK 6 (Testing): Testi kaardi laadimine - 2 SP
  TASK 7 (Docs): Kirjelda kuidas töötab - 1 SP

Kokku: 15 SP
```

---

# Sprint Simulation
## 2 nädala arendus 40 minutiga

---

## Simulatsiooni reeglid

**10 vooru = 10 tööpäeva = 2 nädalat**

**Iga voor (3 min):**
1. Kirjuta daily standup (30 sek)
2. "Tee task valmis" = kirjuta mida tegid (1 min)
3. Uuenda GitHub Projects (30 sek)
4. Viska täringut - võib tulla event! (30 sek)
5. Uuenda burndown chart (30 sek)

**Valmista ette:**
- Burndown chart (paber/tahvel)
- GitHub Projects board
- Timer

---

## Event kaardid (juhuslikud)

**Võimalikud sündmused:**

- "Blocker: Vajad info teiselt liikelt" (+1 voor ooteaeg)
- "Boost: Task läks kiiremini!" (-2 SP burndown'ist)
- "Bug found: Lisa test task" (+2 SP burndown'i)
- "Stakeholder muudatus: Muuda wireframe'i" (+1 voor tööd)
- "Teammate on vacation: Võta üle task" (rohkem tööd)

**Õpetaja valib juhuslikult!**

---

## Simulatsioon algab!

**Voor 1-10:**

Õpetaja hõikab: "Päev 1! START!"

**3 minutit toimub:**
- Daily standup kirjutamine
- Task'ide "tegemine"
- Board'i uuendamine
- Burndown chart uuendamine

**Päev 5:** "Poolaeg! Kontrollige burndown'i!"

**Päev 10:** "Sprint LÄBI! Vaadake tulemusi!"

---

## Burndown Chart Analüüs

**Pärast simulatsiooni:**

1. Kas jõudsite 0-ni?
2. Kus oli suurim langus?
3. Kas olid blockerid?
4. Võrdle ideaalse joonega

**Velocity arvutamine:**
- Planeeritud: 15 SP
- Täidetud: ? SP
- Velocity = täidetud SP

---

## Õppetunnid

**Küsimused igale meeskonnale:**

- Mis oli üllatav?
- Mida tegite hästi?
- Mida teeksite teisiti päris Sprint'is?
- Kas mõistate nüüd arendusprotsessi?

---

# Kodutöö 5
## Sprint 3 Dokumentatsioon

---

## Kodutöö ülevaade

**Dokumenteeri Sprint 3 simulatsioon ja lisa detailid**

**7 kohustuslikku faili:**
1. `sprint-3-plan.md` - Goal, capacity, tasks
2. `epic-breakdown.md` - Epic → Stories → Tasks
3. `daily-standups.md` - 10 päeva kirjeid
4. `sprint-progress.md` - Burndown + velocity
5. `technical-decisions.md` - 3 tehnilist otsust
6. `sprint-3-review.md` - Mis "valmis sai"
7. `sprint-3-retrospective.md` - Start-Stop-Continue

---

## Rolli-põhised lisad

**Product Owner:**
- `backlog-refinement.md` - Kuidas backlog'i täpsustati

**Project Manager:**
- `blockers-log.md` - Blockerite jälgimine ja lahendused

**Developer:**
- `technical-architecture.md` - Tehnilise arhitektuuri kirjeldus

**UX/UI Designer:**
- `usability-testing-plan.md` - Kuidas wireframe'e testiti

---

## Repositooriumi struktuur

```
sprint3/
├── sprint-3-plan.md
├── epic-breakdown.md
├── daily-standups.md
├── sprint-progress.md
├── technical-decisions.md
├── sprint-3-review.md
├── sprint-3-retrospective.md
├── backlog-refinement.md (PO)
├── blockers-log.md (PM)
├── technical-architecture.md (Dev)
├── usability-testing-plan.md (UX)
└── README.md
```

---

## Hindamiskriteeriumid

**4 kategooriat (igaüks 25%):**

1. **Completeness** - Kas kõik failid olemas?
2. **Detail level** - Kas piisavalt detailne?
3. **Realism** - Kas võiks olla päris sprint?
4. **Team coordination** - Kas meeskond töötas koos?

---

## GitHub Workflow

```
1. Loo branch: feature/sprint-3
2. Loo failid sprint3/ kausta
3. Commit + Push
4. Loo Pull Request
5. Peer review (teised meeskonnaliikmed)
6. Merge main'i
7. Lisa "submission" label
```

**Tähtaeg:** 1 nädal

---

## Järgmine seminar

**Seminar 6: Lõplikud esitlused**

- Sprint 3 Review
- Kogu projekti retrospektiiv (3 sprinti)
- Portfolio esitlused (5-7 min)
- Projekti hindamine

**Valmista ette:**
- Demo (kõik 3 sprinti)
- Õppetunnid
- Portfolio

---

# Küsimused?

**Täna õppisime:**
- Epic Breakdown hierarhiat
- Story Point'e ja Planning Poker'it
- Velocity ja Burndown Chart'e
- Daily Standup'e
- Sprint'i simuleerimist

**Järgmiseks:**
Sprint 3 dokumentatsiooni loomine ja arenduse simuleerimine

---

# Edu Sprint 3-ga!
