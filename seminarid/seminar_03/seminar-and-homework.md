# Seminar 3: Sprint 1 - Planeerimine | Seminaritöö ja kodutöö näide

## "Kooli Köök" projekti tutvustus

**"Kooli Köök"** on nutisüsteem, mis lahendab kooli köögiseadmete kasutamise probleemid. Projekt keskendub mikrolaineahjude broneerimisele ja toidu jagamise kogukonna loomisele.

### Põhiprobleem:
Tudengid ja töötajad kulutavad päevas 10-15 minutit mikrolaineahju otsimisele ja ootamisele järjekorras. Info vabade ahjude kohta puudub, tekitades stressi ja ajakulu.

### Lahendus:
- **IoT-põhine broneerimissüsteem** - reaalajas info vabade mikrolaineahjude kohta
- **Nutika broneerimise platvorm** - kasutajad saavad ette broneerida ahju kindlaks ajaks
- **Toidu jagamise kogukond** - kasutajad saavad jagada ülejäänud toitu ja organiseerida ühisostusid
- **Mobile-first lähenemine** - kiire ligipääs telefonist

### Sihtgrupp:
- **Peakasutajad**: Kooli tudengid ja töötajad
- **Toetavad kasutajad**: Köögipersonal ja hooldajad

See projekti näide demonstreerib, kuidas Sprint 1 metoodikaid rakendatakse päris elus kasutada leidva rakenduse planeerimiseks.

---

## Seminari praktilise osa näide

### Rollide jaotamine - "Kooli Köök" meeskond

Meeskond otsustas rollid järgmiselt:

**Product Owner - Liisa**
```markdown
## Minu roll: Product Owner

### Minu vastutused:
- Prioritiseerida funktsioone kasutajate vajaduste põhjal
- Suhelda "kasutajatega" (teiste tudengitega) ja koguda tagasisidet
- Kirjutada user story-sid ja aktsepteerimiskriteeriumeid
- Otsustada, millised funktsioonid on must-have vs nice-to-have

### Minu eesmärgid:
- Tagada, et platvorm lahendab päriselt kooli toidu soojendamise ja jagamise probleemi
- Hoida meeskond keskendunult kõige olulisematele funktsioonidele
- Luua selge visioon toote tulevikust

### Kuidas mõõdan edu:
- Kasutajad leiavad vaba mikrolaineahju 30 sekundiga
- Vähemalt 80% kooli mikrolaineahjudest on süsteemi ühendatud
- Kasutajad annavad tagasisidet regulaarselt
```

**Project Manager - Marko**
```markdown
## Minu roll: Project Manager

### Minu vastutused:
- Planeerida sprinte ja hoida meeskonda graafikus
- Koordineerida meeskonnaliikmete tööd
- Jälgida progressi ja eesmärkide täitmist
- Lahendada takistusi ja kommunikatsiooni probleeme

### Minu eesmärgid:
- Tagada, et kõik teaksid oma ülesandeid ja tähtaegu
- Hoida meeskond motiveerituna ja keskendununa
- Luua sujuv töövoog ja kommunikatsioon

### Kuidas mõõdan edu:
- Kõik sprindi eesmärgid saavad täidetud õigel ajal
- Meeskonnaliikmed on rahul koostööga
- Probleemid lahendatakse kiiresti ja tõhusalt
```

**Developer - Jaan**
```markdown
## Minu roll: Developer

### Minu vastutused:
- Planeerida tehnilise arhitektuuri ja andmebaasi
- Hinnata tehniliste lahenduste keerukust ja ajakulu
- Tagada, et lahendus on skaleeruv ja turvaline
- Konsulteerida meeskonda tehniliste võimaluste osas

### Minu eesmärgid:
- Luua usaldusväärne ja kiire rakendus
- Tagada, et IoT integratsioon mikrolaineahjudega töötab sujuvalt
- Planeerida broneerimsüsteemi arhitektuur

### Kuidas mõõdan edu:
- Rakendus näitab ahjude olekut reaalajas (alla 30 sekundi)
- Andmebaas on hästi struktureeritud
- Turvanõuded on täidetud
```

**UX/UI Designer - Kristel**
```markdown
## Minu roll: UX/UI Designer

### Minu vastutused:
- Disainida intuitiivne kasutajaliides broneerimissüsteemile
- Luua kasutajateekonnad (user journeys)
- Testida prototüüpe kasutajatega
- Tagada, et disain on mobile-friendly

### Minu eesmärgid:
- Luua lihtne ja kiire kasutajakogemus
- Tagada, et kasutajad leiavad vaba ahju 30 sekundi jooksul
- Disainida visuaalselt atraktiivne ja selge liides

### Kuidas mõõdan edu:
- Kasutajad leiavad vajaliku info ilma juhendamiseta
- Broneering võtab aega alla 1 minuti
- Prototüübi testimine annab positiivse tagasiside
```

### Project Charter - "Kooli Köök"

```markdown
# PROJEKTI AJAKAVA - Sprint 1

## Projekti ülevaade
- **Projekti nimi**: Kooli Köök
- **Probleemi kokkuvõte**: Tudengid ja töötajad peavad ootama pikalt järjekorras mikrolaineahjude juures või ei leia vaba kohta oma toidu soojendamiseks, tekitades stressi ja ajakulu.
- **Lahenduse visioon**: Nutisüsteem, mis võimaldab mikrolaineahjude broneerimist, näitab reaalajas vabade ahjude asukohti ning ühendab kasutajaid toidu jagamiseks ja ühisostudeks.

## Eesmärgid ja edu kriteeriumid

### Peamised eesmärgid:
- Vähendada mikrolaineahju otsimisele ja ootamisele kuluvat aega 10-15 minutilt alla 2 minuti
- Luua tõhus broneerimissüsteem kõigile kooli mikrolaineahjudele
- Võimaldada kasutajatel jagada toitu ja organiseerida ühisostusid
- Suurendada kooli köögiseadmete kasutamise efektiivsust
- Luua kogukondlik keskkond toidu ümber koolis

### Edu kriteeriumid:
- Kasutaja leiab vaba mikrolaineahju 30 sekundi jooksul
- Vähemalt 80% kooli mikrolaineahjudest on süsteemi integreeritud
- Keskmine ootamise aeg väheneb 70% võrra
- Toidu jagamise funktsioonide kaudu tekib vähemalt 20 edukakku jagamist nädalas
- Rakendus töötab sujuvalt nii arvutis kui mobiiltelefonil
```

### GitHub Projects seadistamine - "Kooli Köök"

**Custom Fields:**
- **Story Points**: 1, 2, 3, 5, 8, 13 (hindame broneerimissüsteemi põhjal: 1 punkt = lihtne UI täiendus, 5 punkti = IoT integratsioon)
- **Priority**: Critical (kasutajate põhivajadused), High (täiendavad funktsioonid), Medium (optimiseerimised), Low (nice-to-have)
- **Component**: Hardware (IoT integratsioon), Design (kasutajaliides), Backend (broneerimisloogika), Planning (sprintide planeerimine)
- **Sprint**: Sprint 1, Sprint 2, Sprint 3

**Sprint Board View:**
```
To Do | In Progress | Review | Done
Filter: Sprint = "Sprint 1" AND Component = "Planning"
Nähtavad ülesanded: Project charter, rollide kirjeldused, IoT integratsiooni plaan
```

### Backlog Management - "Kooli Köök" näide

#### Epicute jagamine

**Alustame suurest pildist ja jagame väiksemaks:**

```
PROJEKT: Kooli Köök - Toidu soojendamise ja jagamise keskkond
│
├── EPIC: Mikrolaineahjude broneerimissüsteem 
│   ├── USER STORY: Kasutaja näeb vabade ahjude reaalajas olekut
│   │   ├── TASK: IoT sensorite andmete API 📍 Sprint 3 - arendusprotsess
│   │   ├── TASK: Reaalajas statusse näitav kaart 📍 Sprint 2 - disainimine  
│   │   └── TASK: Mobile-responsive ahju vaade 📍 Sprint 2 - disainimine
│   ├── USER STORY: Kasutaja saab broneerida ahju kindlaks ajaks  
│   │   ├── TASK: Broneerimise UI komponent 📍 Sprint 2 - disainimine
│   │   └── TASK: Broneerimisloogika backend 📍 Sprint 3 - arendusprotsess
│   └── USER STORY: Kasutaja saab tühistada broneeringu
│       ├── TASK: Tühistamise funktsioon 📍 Sprint 3 - arendusprotsess
│       └── TASK: Teadete süsteem vabade kohtade kohta 📍 Sprint 3 - arendusprotsess
│
└── EPIC: Toidu jagamise ja ühisostude platvorm
    ├── USER STORY: Kasutaja saab pakkuda ülejäänud toitu
    │   ├── TASK: Toidu pakkumise vormi disain 📍 Sprint 2 - disainimine
    │   ├── TASK: Pildi üleslaadimise funktsioon 📍 Sprint 3 - arendusprotsess
    │   └── TASK: Pakkumiste filtreerimise süsteem 📍 Sprint 3 - arendusprotsess
    ├── USER STORY: Kasutaja saab liituda ühisostuga
    │   ├── TASK: Ühiostu loomise interface 📍 Sprint 2 - disainimine
    │   └── TASK: Maksejaotuse kalkulaator 📍 Sprint 3 - arendusprotsess
    └── USER STORY: Kasutaja näeb kogukonna aktiivsust
        ├── TASK: Kogukonna statistika dashboard 📍 Sprint 2 - disainimine
        └── TASK: Hinnangute ja tagasiside süsteem 📍 Sprint 3 - arendusprotsess
```

NB! ### Epicute ajaline jaotus:

📍 Sprint 1 - projekti setup = Organiseerimise ja planeerimise taskid  
📍 Sprint 2 - disainimine = Kasutajaliidese ja kogemuse disain  
📍 Sprint 3 - arendusprotsess = Arenduse simuleerimine ja koordineerimine  

SPRINT 1 FOCUS: Projekti organiseerimine ja meeskonnakorraldus

- [ ] **Meeskonna rollide jaotamine** (2 SP) 📍 Sprint 1 - setup
- [ ] **Project charter dokument** (3 SP) 📍 Sprint 1 - setup  
- [ ] **GitHub Projects seadistamine** (2 SP) 📍 Sprint 1 - setup
- [ ] **Kommunikatsiooni protokoll** (2 SP) 📍 Sprint 1 - setup
- [ ] **High-level roadmap 3 sprindiks** (2 SP) 📍 Sprint 1 - setup
- [ ] **Riskianalüüs** (2 SP) 📍 Sprint 1 - setup
- [ ] **Stakeholderite kaardistamine** (1 SP) 📍 Sprint 1 - setup

💡 Märkus: Sprint 1-s EI disaini ega arendata veel midagi - ainult planeerime!

SPRINT 2 FOCUS: Kasutajaliidese ja kogemuse kavandamine

Sprint 2 taskid Epic breakdown-ist:
- [ ] **Reaalajas kaardi komponendi disain** (3 SP)
- [ ] **Mobile-responsive ahju vaate wireframe** (2 SP) 
- [ ] **Broneerimise UI komponendi prototüüp** (5 SP)
- [ ] **Toidu pakkumise vormi disain** (3 SP)
- [ ] **Ühiostu interface mockup** (3 SP)
- [ ] **Kogukonna dashboard wireframe** (2 SP)

Disaini-spetsiifilised taskid:
- [ ] **3 detailset persoonat** (3 SP)
- [ ] **Kasutajateekondade kaardistamine** (2 SP)
- [ ] **Paberprototüüpide testimine** (2 SP)

SPRINT 3 FOCUS: Arenduse simuleerimine ja projekti koordineerimine  

Sprint 3 taskid Epic breakdown-ist:
- [ ] **IoT sensorite API spetsifikatsioon** (5 SP)
- [ ] **Broneerimisloogika pseudo-algoritm** (5 SP)
- [ ] **Tühistamise funktsiooni plaan** (3 SP)
- [ ] **Teadete süsteemi arhitektuur** (3 SP)
- [ ] **Pildi upload funktsiooni spetsifikatsioon** (2 SP)
- [ ] **Filtreerimise süsteemi disain** (3 SP)
- [ ] **Maksejaotuse algoritm** (5 SP)
- [ ] **Tagasiside süsteemi spetsifikatsioon** (2 SP)

Arendusprotsessi taskid:
- [ ] **Daily standup-te protokollid** (1 SP)
- [ ] **Sprint ceremonies läbiviimine** (2 SP)
- [ ] **Velocity tracking ja burndown** (2 SP)

#### Story Points hinnangud

**Fibonacci skaalat kasutades:**

- **1 punkt**: "Staatilise kaardi lisamine ahjude asukohtadega" (triviaalne, andmed olemas)
- **2 punkti**: "Broneerimise tühistamise nupp" (lihtne, UI komponent)
- **3 punkti**: "Kasutaja autentimine kooli kaarti põhjal" (keskmine keerukus)
- **5 punkti**: "IoT sensorite integratsioon mikrolaineahjudega" (keeruline, riistvara + tarkvara)
- **8 punkti**: "Täielik maksejaotuse süsteem ühisostudele" (väga keeruline - peaks jagama väiksemateks)

**Praktilised näited meeskonna harjutuseks:**

Klassiga koos hinnatud user story-d:
- ✅ "GitHub konto loomine meeskonna jaoks" - **1 punkt** (teame kuidas, kiire)
- ✅ "Kooli köögiseadmete kaardistamine" - **2 punkti** (struktureeritud uurimistöö)  
- ✅ "Konkurentsianalüüs 3 broneerimisrakendusega" - **3 punkti** (uurimistöö, võtab päeva)
- ✅ "Täieliku prototüübi loomine Figmas" - **5 punkti** (keeruline disainitöö)
- ❌ "Valmis süsteemi testimine kasutajatega" - **8 punkti** (liiga suur - peaks jagama: "Testplaani koostamine" 2 SP + "Piloteerimise 5 ahjuga" 3 SP + "Tulemuste analüüs" 2 SP)

#### MoSCoW prioritiseerimine

**Praktiline harjutus "Kooli Köök" funktsioonidega:**

**Must Have** (ilma selleta ei ole projekt kasulik):
- ✅ Mikrolaineahjude reaalajas oleku näitamine (põhifunktsioon)
- ✅ Broneerimise süsteem ajapiirangutega (kriitilise tähtsusega)
- ✅ Kasutaja autentimine kooli süsteemiga (turvalisuse nõue)
- ✅ Mobile-responsive disain (kiire ligipääsu vajadus)

**Should Have** (väga oluline, aga saab ka ilma):
- ✅ Push teavitused vabadest ahjudest (kasutajakogemuse parandamine)
- ✅ Asukoha järgi sorteerimine (lähima ahju leidmine)
- ✅ Toidu jagamise funktsioon (kogukonna loomine)

**Could Have** (tore lisa, kui aeg lubab):
- ✅ Ühisostude organiseerimine (kogukonna funktsioon)
- ✅ Lemmik ahjude salvestamine (isikupärastamine)
- ✅ Sotsiaalsed funktsioonid ja reitingud (lisaväärtus)

**Won't Have** (praegu teadlikult välja jätame):
- ❌ Täielik toidutellimise süsteem (väljaspool skoopi)
- ❌ Krediitkaardi maksed ühisostudele (keeruline, mitte MVP skoobis)
- ❌ Inventuuri haldamine köögitarvetele (liiga keeruline MVP jaoks)

**Järgmise sprindi planning poker harjutus:**

Liisa (Product Owner) ütleb: *"Meie uuringust selgus, et kasutajatel läheb 10-15 minutit vaba mikrolaineahju leidmiseks. Meie eesmärk on viia see alla 30 sekundi. Millise story pointiga hindate 'Kasutaja leiab vaba ahju 30 sekundiga' user story?"*

Meeskond arutleb:
- Marko: "3 punkti - vajab head UX disaini ja optimeerimist"
- Jaan: "5 punkti - IoT andmete kiirus peab olema suurepärane"  
- Kristel: "2 punkti - peamiselt disaini küsimus"
- Liisa: "Arutame läbi... konsensus on 3 punkti"

### Sprint 1 planeerimine - "Kooli Köök"

**Sprint Goal**: "Projekt on käivitamiseks valmis - meeskond on organiseeritud, IoT integratsiooniplaan valmis ja broneerimissüsteemi tehniline keskkond loodud."

**Capacity Planning** (4-liikmelise meeskonna jaoks):
- Liisa (Product Owner): 3 story point-i nädalas
- Marko (Project Manager): 4 story point-i nädalas  
- Jaan (Developer): 4 story point-i nädalas
- Kristel (UX/UI Designer): 3 story point-i nädalas
- **Kokku Sprint 1 jaoks**: 14 story point-i

**Sprint 1 Tasks:**

- [ ] **Project charter dokument valmis** (3 SP) - kasutades mikrolaineahjude kasutamise analüüsi
  - *Vastutab*: Marko (Project Manager)
  - *Definition of Done*: Dokument sisaldab projekti eesmärke, edu kriteeriume ja on meeskonna poolt heaks kiidetud

- [ ] **Kõigi rollide detailsed kirjeldused** (2 SP)
  - *Vastutab*: Kõik (igaüks kirjutab oma rolli)
  - *Definition of Done*: Selged vastutusalad, eesmärgid ja edu mõõdikud

- [ ] **Technical architecture plaan** (5 SP) - IoT integratsioon ja broneerimissüsteem
  - *Vastutab*: Jaan (Developer)
  - *Definition of Done*: Arhitektuuriskeem, tehnoloogia valikud, IoT protokolli spetsifikatsioon

- [ ] **Design strategy dokument** (3 SP) - kasutajakogemus mikrolaineahjude broneerimiseks
  - *Vastutab*: Kristel (UX/UI Designer)  
  - *Definition of Done*: Kasutajateekonnad, wireframe'id, disaini põhimõtted

- [ ] **Product backlog prioritiseerimine** (2 SP) - broneerimissüsteemide analüüsi põhjal
  - *Vastutab*: Liisa (Product Owner)
  - *Definition of Done*: Prioritiseeritud user story-d, MoSCoW kategoriseerimine

**Kokku**: 15 SP (pisut üle capacity, aga Sprint 1 on organiseerimisele keskendunud)

### Daily Standup protokoll - "Kooli Köök" meeskonnale

**GitHub Discussions template:**

```markdown
## Daily Standup [25.09.2024]

**Nimi:** Liisa
**Roll:** Product Owner

### ✅ Eile tegin:
- Analüüsisin kooli köögiseadmete kasutamise mustreid
- Prioritiseerisin user story-d MoSCoW meetodil
- Suhtlesin 3 koolitöötajaga täiendava tagasiside saamiseks

### 🎯 Täna teen:  
- Lõpetan product backlog dokumenti
- Kirjutan aktsepteerimiskriteeriumid 5 kõige olulisema user story jaoks
- Review'n Kristeli design strategy mustandit

### ❌ Mind takistab:
- Vajaks Jaani sisendit IoT piirangute osas user story-de jaoks
```

**Kokkulepitud reeglid:**
- Iga päev kell 9:00 postitame standup
- Vähemalt 4 korda nädalas (E-T-K-N)
- Takistuste puhul märgistame vastava rolli omaniku @ märgiga
- Reede õhtul teeme nädala kokkuvõtte

---

# Kodutöö 3: Sprint 1 dokumentatsioon - "Kooli Köök" näitel

## GitHub dokumentatsiooni struktuur

### Põhidokumendid (kõigile kohustuslikud):

#### `project-charter.md`
```markdown
# Kooli Köök - Project Charter

## Projekti taust
Kooli uuringute põhjal selgus, et 90% kasutajatest kulutab mikrolaineahju otsimisele ja ootamisele 10-15 minutit päevas. Peamised probleemid on pikad järjekorrad ja info puudumine vabade ahjude kohta.

## Äriloogika
Praegused lahendused puuduvad või on aegunud. Kooli Köök loob esimese nutika broneerimissüsteemi kooli köögiseadmetele.

[Ülejäänud põhineb mikrolaineahjude kasutamise analüüsil...]
```

#### `team-roles.md` 
```markdown
# Meeskonna rollid ja vastutused

## Ülevaade
4-liikmeline meeskond, igal liikmel spetsiifiline vastutusala 3 sprindi jooksul.

## Rollide kirjeldused
[Põhinevad ülalpool väljatöötatud rollidel...]
```

#### `project-timeline.md`
```markdown
# Projekti ajakava

## Sprint ülevaade
- **Sprint 1** (nädalad 1): Planeerimine ja seadistamine
- **Sprint 2** (nädalad 2): IoT integratsioon ja disainimine  
- **Sprint 3** (nädalad 3): Piloteerimine ja viimistlemine

## Peamised milestoned
Baseeruvad broneerimissüsteemi funktsionaalsetel nõuetel...
```

#### `risk-analysis.md`
```markdown
# Riskide analüüs - Kooli Köök

## Tehnilised riskid
**Risk**: IoT sensorid ei integreeru mikrolaineahjudega
- *Tõenäosus*: Keskmine
- *Mõju*: Kõrge
- *Leevendamine*: Alustame lihtsamate lahendusega (manuaalne oleku uuendamine) ja liigume järk-järgult automatiseeritud süsteemi poole.

**Risk**: Broneerimissüsteem muutub liiga keeruliseks
- *Tõenäosus*: Madal
- *Mõju*: Keskmine  
- *Leevendamine*: Kasutajatest 95% on mobiilikasutajad - prioritiseerime lihtsust.

[Ülejäänud riskid...]
```

#### `communication-plan.md`
```markdown
# Kommunikatsiooni plaan

## Daily Standups
Asünkroonselt GitHub Discussions kaudu, template määratletud

## Sprint sündmused
- **Sprint Planning**: Esmaspäev 14:00 (30 min)
- **Sprint Review**: Reede 16:00 (45 min) - demo mikrolaineahjude broneerimise prototüübist
- **Sprint Retrospective**: Reede 16:45 (15 min)

[Detailsed reeglid...]
```

#### `sprint-1-plan.md`
```markdown
# Sprint 1 Plaan

## Sprint Goal
"Projekt on käivitamiseks valmis - meeskond organiseeritud, IoT integratsiooniplaan valmis ja broneerimissüsteemi tehniline keskkond loodud."

## Capacity ja Tasks
[Ülalpool defineeritud 14 SP ja 5 peamist task'i]

## Definition of Done
Iga task'i jaoks eraldi määratletud, baseeruvad IoT ja broneerimissüsteemi kvaliteedikriteeriumitel.
```

#### `sprint-1-review.md` (täidetakse sprindi lõpus)
```markdown
# Sprint 1 Review

## Saavutatud tulemused
- [Täidetakse pärast sprindi lõppu]

## Demo
- [Näidatakse loodud dokumentatsiooni ja IoT plaani]

## Tagasiside
- [Meeskonna ja stakeholder'ite tagasiside]

## Järgmised sammud
- Sprint 2 fookus: IoT sensorite integreerimine ja kasutajaliidese disainimine
```

### Rolli-põhised dokumendid:

#### `product-backlog.md` (Product Owner - Liisa)
```markdown
# Product Backlog - Kooli Köök

## Prioritiseeritud User Stories

### Must Have (MoSCoW)
1. **Kasutaja näeb vabade mikrolaineahjude reaalajas olekut** (8 SP)
   - *Aktsepteerimiskriteeriumid*: Olek uuendatakse 30 sekundi jooksul, näitab asukohta ja hinnangulist vabakssaamise aega
   - *Alus*: 90% kasutajatest vajab seda põhifunktsiooni

2. **Kasutaja saab broneerida ahju kindlaks ajaks** (5 SP)
   - *Aktsepteerimiskriteeriumid*: Broneering kehtib 15 minutit, automaatne tühistamine
   - *Alus*: Järjekordade vähendamise peamine mehhanism

[Ülejäänud user story-d...]
```

#### `project-management-plan.md` (Project Manager - Marko)
```markdown
# Projektijuhtimise plaan

## Sprintide planeerimine
Mikrolaineahjude süsteemi analüüs näitas, et projekt on 3 sprindiga teostatav:
- Sprint 1: Dokumentatsioon ja IoT planeerimine
- Sprint 2: MVP prototüüp broneerimissüsteemiga
- Sprint 3: Piloteerimine ja viimistlemine

## Resource management
[Meeskonnaliikmete tööjõu planeerimine...]
```

#### `technical-architecture.md` (Developer - Jaan)  
```markdown
# Tehniline arhitektuur

## Tehnoloogia valikud
Broneerimissüsteemi nõuete põhjal:
- **Frontend**: React (mobile-responsive broneerimisliides)
- **Backend**: Node.js + Express + WebSocket (reaalajas uuendused)
- **Andmebaas**: PostgreSQL (broneeringud ja seadmete olekud)
- **IoT**: MQTT protokoll mikrolaineahjude oleku edastamiseks

## Arhitektuuri skeem
[Baseerub IoT + broneerimissüsteemi integratsioonil...]
```

#### `design-strategy.md` (UX/UI Designer - Kristel)
```markdown
# Disaini strateegia

## Kasutajateekonnad

### Peamine kasutajateekond - Tudeng soojendab toitu
1. **Kontekst**: Vahetund, 15 minutit aega
2. **Eesmärk**: Leida vaba mikrolaineahi kiiresti  
3. **Käitumismuster**: 80% tahab lähimat vaba ahju
4. **Ideaalne voog**: Ava app → vaata kaardilt lähim vaba ahi → broneeri → mine kohale (max 30 sekundit)

[Ülejäänud disaini põhimõtted...]
```

## Esitamise workflow

1. **Branch loomine**: `feature/project-charter`
2. **Pull Request**: "Add project charter based on microwave booking system analysis"
3. **Review**: Vähemalt 2 meeskonnaliikme approval
4. **Merge**: Main branch'i

**Tähtaeg**: 1 nädal pärast seminari

---

## Kokkuvõte

See näide demonstreerib, kuidas "Kooli Köök" projekt jookseb läbi Sprint 1 dokumentatsiooni loomise. Kõik seminaril loodavad dokumendid baseeruvad kooli köögiseadmete kasutamise analüüsil ja mikrolaineahjude broneerimise vajadusest, luues tervikliku lähenemise tõhusama koolitoitlustamise keskkonna loomiseks.