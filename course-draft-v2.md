# Sissejuhatus tarkvaraarendusse - Kursuse kavand v2.0

## Kursuse üldinfo
- **Kursuse nimi**: Sissejuhatus tarkvaraarendusse
- **Maht**: 6 EAP
- **Seminarid**: 6 + eksam
- **Sihtgrupp**: Algajad tudengid, kes ei tea tarkvaraarendusest midagi
- **Fookus**: tarkvaraarenduse protsessid, koostöö, projektihaldus
- **Keskne tööriist**: Git/GitHub (GUI-põhine, mitte terminal)

## Kursuse eesmärgid

### Peamised õpiväljundid
Kursuse lõpus tudeng on läbinud **täieliku tarkvaraarenduse elutsükli**:
- **Projekti juhtimine**: organiseerib ja planeerib projekte
- **Probleemi uurimine**: analüüsib kasutajate vajadusi ja probleeme
- **Nõuete kogumine**: kirjeldab funktsionaalseid ja mitte-funktsionaalseid nõudeid
- **Disaini kavandamine**: loob paberprototüüpe ja kasutajaliidese visandeid
- **Arenduse planeerimine**: jagab tööd ülesanneteks ja planeerib sprinte
- **Kvaliteedi tagamine**: testib, dokumenteerib ja vatab üle
- **Versiooni haldamine**: Oskab kasutada Git/GitHub-i kogu protsessi vältel
- **Tiimitöö**: töötab erinevates rollides ja annab tagasisidet

### Läbiv filosoofia: täielik arendusprotsess
Iga seminar vastab **ühele arenduse etapile**:
1. ✅ **Alustamine** - Tööriistad ja versioonikontroll
2. ✅ **Uurimine** - Probleemi defineerimine ja analüüs  
3. ✅ **Sprint 1: Planeerimine** - Projektijuhtimine, meeskonnatöö ja sprint käivitamine
4. ✅ **Sprint 2: Disainimine** - Kasutajaliides ja prototüüpimine
5. **Sprint 3: Arendamine** - Epic breakdown ja süvitsi töö
6. **Lõplik esitlus ja hindamine** - Demo ja kursuse lõpetamine

---

## KURSUSE KESKNE PROJEKT

### Projekti ülevaade
Tudengid **lahendavad päris probleemi**, mis viib nad läbi kogu tarkvaraarenduse protsessi. Ei koodita.

### Projekti areng läbi seminaride

#### **Seminar 1:** tööriistade ja keskkondade tutvustus
- Git
- Github
- Github desktop (esimesel poolaastal pole terminali kasutamine vajalik)
- Markdown

#### **Seminar 2: Uurimise algus** 
Tudengid valivad **päris probleemi** lahendamiseks, midagi oma igapäevaelust. Näiteks:
- tudengite elu väljakutsed (kodutööde tähtajad, söögikohad)
- haridusprotsessi parandused (kursuste planeerimine, grupitöö koordineerimine)
- kohalikud kogukonna küsimused (ürituste avastamine, ressursside jagamine)
- keskkonna-/jätkusuutlikkuse väljakutsed

**Esialgsed tulemused:**
- `problem-definition.md` - Valitud ja analüüsitud probleem
- `user-research.md` - Intervjuu tulemused päris kasutajatega
- `requirements.md` - Funktsionaalsed ja mitte-funktsionaalsed nõuded
- `competitive-analysis.md` - Olemasolevate lahenduste analüüs

#### **Seminar 3: Sprint 1 - Planeerimine ja setup**
**Rollide jaotamine** - iga tudeng võtab konkreetse rolli:
- **Product Owner**: kasutajate vajadused, äriloogika ja prioriteedid
- **Project Manager**: projekti koordineerimine, ajakavad ja protsessid
- **Developer**: tehnilised lahendused ja arenduse planeerimine  
- **UX/UI Designer**: kasutajakogemus, visuaalne disain ja testimine

**Sprint 1 eesmärgid:**
- Täielik projektiplaan ja roadmap
- GitHub Projects seadistamine advanced workflow-dega
- Riskianalüüs ja leevendamise strateegiad
- Meeskonna kommunikatsiooni protokollid
- **Sprint rytmi loomine**

#### **Seminar 4: Sprint 2 - Disainimine**
**Sprint 2 eesmärgid:**
- **3 detailset persoonat** uurimisandmete põhjal
- **Täielik kasutajateekonna kaardistamine** peamiste stsenaariumite jaoks
- **Paberprototüübid** kõigi võtme ekraanide ja interaktsioonide jaoks
- **Disainisüsteemi dokumentatsioon** (komponendid, reeglid, standardid)

**Rolli-spetsiifilised Sprint 2 panused:**
- UX/UI Designer: Teekonna kaardid ja kasutatavuse testimise plaanid
- Product Owner: Prioritiseeritud backlog äriväärtusega
- Project Manager: Sprint 2 koordineerimine ja kvaliteedi tagamine
- Developer: Tehnilise teostatavuse analüüs

#### **Seminar 5: Sprint 3 - Arendamine**
**Sprint 3 eesmärgid:**
- **Epic-ute süvitsi jagamine** detailseteks arendusülesanneteks  
- **Advanced GitHub Projects** kasutamine ja automation
- **Velocity tracking** ja meetrikate analüüs
- **Sprint retrospective** ja protsessi parandamine

**Rolli-põhised Sprint 3 tegevused:**
- Product Owner: Backlog refinement ja kasutajate tagasiside
- Project Manager: Sprint koordineerimine ja takistuste lahendamine
- Developer: Tehniliste lahenduste detailimine
- UX/UI Designer: Prototüüpide iteratsioon ja testimine

#### **Seminar 6: Lõplik esitlus ja hindamine**
**Seminar 6 eesmärgid:**
- **Sprint 3 lõpetamine ja retrospektiiv**
- **Kasutajatestide sessioonid** 3+ välise osalejaga
- **Vigade raporteerimine** ja kvaliteedi dokumenteerimine
- **GitHub Pages deployment** projekti showcase jaoks
- **Projektide demo esitlused**
- **Portfolio hindamine**

**Lõplikud tulemused:**
- Täielik release pakett koos dokumentatsiooniga
- Demo esitlus (5-7 minutit meeskonnale)
- Individuaalne portfoolio rolli reflektsioonidega
- **Kogu projekti retrospektiiv** (3 sprindi analüüs)

### Näidisprojekt: "StudySync" - Tudengite tähtaegade haldamine

**Probleem:** Haapsalu kolledži tudengitel on raske jälgida kodutööde tähtaegu mitmes süsteemis (Moodle, e-mail, Discord), mistõttu 40% tähtaegadest unustatakse.

**Lahenduse areng:**
1. **Uurimine:** Intervjuud 15+ tudengiga paljastavad valupunktid
2. **Planeerimine:** 6-liikmelise meeskonna rollidega ja 12-nädalase roadmap-iga
3. **Disain:** Paberprototüübid mobile-first kalendri liidese jaoks
4. **Arendus:** Sprint-i simuleerimine 45+ GitHub issue-ga
5. **Testimine:** Kasutajatestimine näitab 8,2/10 kasutatavuse skoori
6. **Release:** Täielik dokumentatsioon ja deployment strateegia

---

## Seminaride kavand

### **Seminar 1: sissejuhatus** ✅ (juba toimunud)
**Kestus**: 3h  
**Fookus**: alused ja esimesed sammud

#### Teemad:
- Sissejuhatus tarkvaraarendusse
- **Tarkvara** - mis see on ja miks me seda vajame?
- **Tarkvaraarendus** - protsessina ja elukutse
- Git ja GitHub algkursus
- Markdown põhitõed
- **.gitignore** - failide varjamine
- Repositooriumi loomine ja kloonimine
- Esimesed commit-id ja push-id

#### Praktilised harjutused:
- GitHub konto loomine
- Esimese repo loomine
- README.md kirjutamine
- Basic Git workflow VSCode-s

---

### **Seminar 2: uurimine - probleemi analüüs ja kasutajate mõistmine**
**Kestus**: 3h (90 min teooria + 90 min praktikat)
**Fookus**: arendusprotsessi 1. etapp - probleemi defineerimine ja uurimine

#### Teooria (90 min):
- **Tarkvaraarenduse olemus** (15 min)
  - Tarkvara definitsioon ja komponendid
  - Arendusprotsessi etapid ja elutsükkel
  - Tarkvaraarendus vs programmeerimine

- **Probleemi defineerimine** (20 min)
  - "Hea" probleemi kriteeriumid
  - Probleemi analüüsi raamistik
  - Näited headest ja halbadest definitsioonidest

- **Kasutajate uurimise meetodid** (25 min)
  - Kvalitatiivsed meetodid (intervjuud, vaatlused, fookusgrupid)
  - Kvantitatiivsed meetodid (küsitlused, analüütika, A/B testimine)
  - Kombineeritud lähenemised

- **Nõuete tüübid** (20 min)
  - Funktsionaalsed nõuded ja näited
  - Mitte-funktsionaalsed nõuded (jõudlus, turvalisus, kasutatavus)
  - Kvaliteedi kriteeriumid

- **Konkurentsianalüüs** (15 min)
  - Konkurentsianalüüsi tähtsus
  - Analüüsi raamistik
  - Dokumenteerimise head tavad

#### Praktiline töötuba (90 min):
- **Probleemi valimine** (20 min): Grupitöö probleemi brainstorm ja valik
- **Kasutajate uurimine** (30 min): Intervjuu küsimuste koostamine ja rollimäng
- **Nõuete kogumine** (25 min): Funktsionaalsete ja mitte-funktsionaalsete nõuete määratlemine
- **Konkurentsianalüüs** (15 min): 2-3 konkurendi tuvastamine ja analüüs

#### Kodutöö 2:
**Grupi osa:**
- Probleemi süvaanalüüs täiendavate allikatega
- Laiendatud kasutajate uurimine (vähemalt 3 päris intervjuud)
- Detailne konkurentsianalüüs (5+ konkurenti)
- Stakeholder analüüs

**Individuaalne osa** (rollide järgi):
- Product Owner: Täiendavad intervjuud ja ärimudeli analüüs
- Project Manager: Konkurendid ja turuanalüüs
- Developer: Tehnilised lahendused ja teostatavuse analüüs
- UX/UI Designer: Kasutajate uurimine ja disainianalüüs

---

### **Seminar 3: planeerimine - projektijuhtimine ja meeskonnatöö**
**Kestus**: 3h (90 min teooria + 90 min praktikat)
**Fookus**: arendusprotsessi 2. etapp - projekti struktureerimine ja meeskonna organiseerimine

#### Teooria (90 min):
- **Arendusmetoodikate ülevaade** (35 min)
  - Waterfall mudel: etapid, eelised, puudused
  - Agile arenduse põhiväärtused ja põhimõtted
  - Scrum raamistik: rollid, sündmused, artefaktid
  - Kanban süsteem ja Lean põhimõtted

- **Rollid tarkvaraarenduses** (20 min)
  - Product Owner: kasutajate esindamine ja äriloogika
  - Project Manager: projekti koordineerimine ja kvaliteet
  - Developer: tehnilised lahendused ja rakendamine
  - UX/UI Designer: kasutajakogemus ja visuaalne disain

- **Meeskonnatöö ja kommunikatsioon** (15 min)
  - Efektiivse meeskonna omadused
  - Kommunikatsiooni raamistikud (sünkroonsed vs asünkroonsed)
  - Remote vs co-located meeskonnad

- **Backlog management** (20 min)
  - Epic-ute jagamine user story-deks
  - Story points ja hindamine
  - Prioritiseerimise tehnikad (MoSCoW, Value vs Effort matrix)

#### Praktiline töötuba (90 min):
- **Rollide jaotamine** (15 min): Iga tudeng valib peamise rolli
- **Projekti ajakava loomine** (20 min): Charter, roadmap, riskianalüüs
- **GitHub organisatsiooni seadistamine** (25 min): Advanced Projects, labelid, automation
- **Sprint 1 planeerimine** (20 min): Sprint goal, backlog selection, capacity planning
- **Daily workflow seadistamine** (10 min): Standup protokoll ja kommunikatsioon

#### Kodutöö 3: Sprint 1 dokumentatsioon

**GitHub dokumentatsioon:**
- `project-charter.md` - projekti kirjeldus ja eesmärgid
- `team-roles.md` - rollide kirjeldused ja vastutused  
- `project-timeline.md` - ajakava ja milestoneid
- `risk-analysis.md` - riskide analüüs ja leevendamise strateegiad
- `communication-plan.md` - meeskonna suhtluse protokollid
- `sprint-1-plan.md` - Sprint 1 eesmärgid ja ülesanded
- `sprint-1-review.md` - Sprint 1 tulemused ja analüüs

**Rolli-põhised ülesanded:**
- Product Owner: `product-backlog.md` - prioritiseeritud backlog acceptance criteria-ga
- Project Manager: `project-management-plan.md` - projekti koordineerimise strateegia
- Developer: `technical-architecture.md` - tehnilise lahenduse ülevaade
- UX/UI Designer: `design-strategy.md` - kasutajate testimise ja design system plaan

---

### **Seminar 4: disainimine - kasutajaliidese kavandamine ja prototüüpimine**
**Kestus**: 3h (90 min teooria + 90 min praktikat)
**Fookus**: arendusprotsessi 3. etapp - kasutajaliidese ja kasutajakogemuse disainimine

#### Teooria (90 min):
- **Design thinking metoodika** (25 min)
  - Design thinking ülevaade ja 5 etappi
  - Double Diamond protsess
  - Human-Centered Design põhimõtted

- **Persoonade loomine** (20 min)
  - Persoona definitsioon ja eesmärk
  - Persoona elemendid: taustainfo, kontekst, eesmärgid, frustatsioonid
  - Näidispersoona analüüs

- **Kasutajalugude kirjutamine** (20 min)
  - User story formaat ja näited
  - INVEST kriteeriumid
  - Acceptance criteria määratlemine

- **Kasutajateekond ja stsenaariumid** (15 min)
  - Customer Journey Map elementi
  - Stsenaariumide kirjutamise tehnika
  - User flow mapping

- **Funktsionaalsed vs mitte-funktsionaalsed nõuded** (10 min)
  - Selge eristamine ja näited
  - Nõuete kvaliteedi kriteeriumid

#### Praktiline töötuba (90 min):
- **Persoonade loomine** (20 min): Uurimistulemuste analüüs ja persoonade töötuba
- **Kasutajalugude töötuba** (25 min): Epic-ute hierarhia ja user story brainstorm
- **Paberprototüüpide loomine** (35 min): Lo-fi wireframe-id ja interaktiivsuse planeerimine
- **Kasutajateekonna kaardistamine** (10 min): Journey map loomine põhifunktsiooni kohta

#### Kodutöö 4: Sprint 2 dokumentatsioon

**GitHub dokumentatsioon:**
- `personas.md` - 3 detailset kasutajapersoonat
- `user-stories.md` - täielik user story backlog prioriteetidega
- `user-journey-maps.md` - kasutajateekondade kaardistamine
- `design-system.md` - komponendid, värvid, stiilid
- `paper-prototypes.md` - paberprototüüpide dokumenteerimine (fotod + kirjeldused)
- `wireframes.md` - ekraanide struktuur ja navigatsioon
- `interaction-flows.md` - kasutaja tegevuste voog läbi süsteemi
- `sprint-2-review.md` - Sprint 2 tulemused ja analüüs

**Rolli-põhised ülesanded:**
- UX/UI Designer: `usability-testing-plan.md` - testimise metoodika ja protokoll
- Product Owner: `business-requirements.md` - ärilised user story-d ja edu meetrikad
- Project Manager: `quality-plan.md` - kvaliteedi tagamise strateegia
- Developer: `technical-requirements.md` - tehnilised user story-d ja süsteemi nõuded

**Märkus:** Kõik paberprototüübid tuleb pildistada ja lisada Markdown dokumentidesse kirjeldustega!

---

### **Seminar 5: arendamine - sprint-ide haldamine ja ülesannete jälgimine**
**Kestus**: 3h (90 min teooria + 90 min praktikat)
**Fookus**: arendusprotsessi 4. etapp - töö organiseerimine ja jälgimine arenduse ajal

#### Teooria (90 min):
- **Sprint planning põhimõtted** (25 min)
  - Sprint-i anatoomia ja komponendid
  - Epic-ute jagamine user story-deks ja task-ideks
  - Story points ja estimation

- **Backlog management** (20 min)
  - Backlog grooming protsess
  - Prioritiseerimise tehnikad (MoSCoW, Kano mudel)
  - User story refinement

- **Arenduse jälgimise meetrikad** (20 min)
  - Velocity tracking ja kasutamine
  - Burndown charts ja analüüs
  - Cycle time ja lead time

- **Daily standups ja kommunikatsioon** (15 min)
  - Daily standup struktuur ja reeglid
  - Remote teams kommunikatsioon
  - Anti-patterns vältida

- **Continuous Integration basics** (10 min)
  - CI/CD kontseptsioon ja eelised
  - GitHub Actions sissejuhatus

#### Praktiline töötuba (90 min):
- **Epic breakdown** (30 min): Design epic-ute analüüs ja jagamine task-ideks
- **GitHub Projects advanced setup** (25 min): Custom fields, automation, views
- **Sprint simulation** (25 min): Sprint 1 planning ja daily standup simulation
- **Metrics setup** (10 min): Burndown chart ja velocity baseline

#### Kodutöö 5: Sprint 3 dokumentatsioon

**GitHub dokumentatsioon:**
- `sprint-3-plan.md` - kolmanda sprint-i eesmärk, backlog ja ajakava
- `daily-standups.md` - igapäevased uuendused 2 nädala jooksul
- `epic-breakdown.md` - epic-ute jagamine task-ideks
- `sprint-progress.md` - burndown chart ja velocity jälgimine
- `blockers-log.md` - takistuste dokumenteerimine ja lahendused
- `sprint-3-review.md` - kolmanda sprint-i tulemuste kokkuvõte
- `retrospective.md` - Sprint 3 retrospektiiv: mis läks hästi, mis paremini

**Rolli-põhised igapäevased uuendused:**
- Product Owner: `po-daily-updates.md` - backlog hooldamine, stakeholder-itega suhtlemine
- Project Manager: `pm-daily-updates.md` - projekti koordineerimine, meetrikate jälgimine  
- Developer: `dev-daily-updates.md` - tehniliste ülesannete progress
- UX/UI Designer: `design-daily-updates.md` - prototüüpide testimine ja iteratsioon

**Märkus:** 
- 3 sprinti: Seminarid 3, 4, 5 (Seminar 6 on lõplik esitlus)
- Kõik GitHub Issues ja Projects board peavad olema aktiivselt kasutusel!
- Sprint ceremonies toimuvad iga seminari alguses ja lõpus

---

### **Seminar 6: lõplik esitlus ja hindamine**
**Kestus**: 3h (60 min testimine + 120 min esitlused ja hindamine)  
**Fookus**: Sprint 3 lõpetamine, testimine ja projektide esitlused

#### Teooria (90 min):
- **Testimise liigid ja metoodikad** (30 min)
  - Testimise hierarhia (test pyramid)
  - Manuaalne vs automaatne testimine
  - QA protsessid ja quality gates

- **Kasutajatestide planeerimine** (20 min)
  - Usability testing meetodid
  - Test protokolli koostamine
  - Think-aloud protocol

- **Release management** (25 min)
  - Versioning strategies (SemVer)
  - Release planning ja types
  - DevOps ja deployment strategies

- **Dokumentatsiooni standardid** (15 min)
  - Release notes kirjutamine
  - API dokumentatsioon ja README structure
  - Dokumentatsiooni automatiseerimine

#### Praktiline töötuba (90 min):
- **Kasutajatestide läbiviimine** (35 min): Test protokolli ettevalmistus ja simulatsioon
- **Bug reporting** (20 min): Bug raportite kirjutamine ja quality checklist
- **Release ettevalmistus** (25 min): Release package ja GitHub Pages deployment
- **Esitluste ettevalmistus** (10 min): Demo structure planeerimine

#### Kodutöö 6: Final release ja portfolio

**GitHub dokumentatsioon:**
- `usability-testing-results.md` - kasutajatestide tulemused (vähemalt 3 sessiooni)
- `bug-reports.md` - leitud probleemid ja nende lahendused
- `quality-assessment.md` - kvaliteedi hindamine vastavalt DoD kriteeriumitele
- `release-notes.md` - toote versiooni kirjeldus ja muudatused
- `user-manual.md` - kasutajajuhend prototüübile
- `final-presentation.md` - demo script ja esitluse plaan
- `sprint-3-final-review.md` - kolmanda (viimase) sprint-i tulemuste kokkuvõte
- `project-retrospective.md` - kogu projekti analüüs ja 3 sprindi ülevaade

**Individuaalsed failid:**
- `individual-portfolio.md` - isikliku töö ülevaade kõigi seminaride kohta
- `role-reflection.md` - oma rolli analüüs (2-3 lk)
- `tools-evaluation.md` - VSCode, GitHub, Markdown tööriistade hinnang
- `peer-evaluation.md` - meeskonnaliikmete töö hindamine

**GitHub Pages deployment:**
- Projekti esitluse veebileht kõigi dokumentidega
- Demo video (3-5 min) projektist
- Visuaalsed materjalid (prototüüpide fotod, diagrammid)

**Märkus:** Pole vaja tegelikku koodi kirjutada - kõik on dokumentatsioon, pildid ja kirjeldused!

---

## Hindamissüsteem

### **Kodutööd: 50%**
- 6 kodutööd, igaüks ehitab eelmise peale
- Rolli-spetsiifilised panused cross-team review-ga
- GitHub workflow peer review protsessidega

### **Eksam: 50%**

#### **Soovituslik Option 1: Projekti-põhine hindamine**
- **Portfolio presentation** (15 min meeskonna kohta)
- **Individual role defense** (5 min tudeng kohta)
- **Peer evaluation** meeskonna panuste kohta
- **Process reflection** essee (2-3 lk)

#### **Option 2: Traditsiooniline eksam + projekt**
- Seminar 6 toimub plaani järgi
- Lisa eraldi praktiline eksam:
  - GitHub workflow stsenaariumid
  - Projektijuhtimise case study-d
  - Protsessi optimeerimise väljakutsed

---

## Projekti võtmeomadused

✅ **Pärismaailma relevantne** - Käsitleb päriseid probleeme, millega tudengid kokku puutuvad  
✅ **Täielik elutsükkel** - Iga professionaalse arenduse faas  
✅ **Rolli spetsialiseermine** - Iga tudeng arendab ekspertiis ühes valdkonnas  
✅ **Koostöö workflow** - Kasutab professionaalseid tööriistu (GitHub, Projects)  
✅ **Käegakatsutavad tulemused** - Portfolio-valmis deliverable-id  
✅ **Kodeerimine pole vajalik** - Fookus protsessil, planeerimisil ja koostööl  

---

## Ressursid ja tööriistad

### Kohustuslikud tööriistad:
- **Git** (GUI kaudu VSCode-s või GitHub Desktop-is)
- **GitHub** (repositories, issues, projects, pages)
- **VSCode** (Markdown extensions, Git integration)
- **Markdown** (dokumentatsioon, README-d)

### Soovituslikud ressursid:
- Paber ja pliiats (prototüüpimiseks)
- Telefon/kaamera (prototüüpide dokumenteerimiseks)
- Miro/Figma (digitaalseks koostööks)

### Dokumentatsiooni formaat:
- **Kõik tööd Markdown (.md) failidesse**
- Pildid lisada kui failid repositooriumisse
- Diagrammid võivad olla käsitsi joonistatud ja pildistatud
- Prototüübid pildistada ja dokumenteerida
- **Tegelikku koodi ei kirjutata** - ainult dokumentatsioon ja disain

---

## Edukriteeriumid

### Kursuse lõpuks tudeng oskab:
1. **Git/GitHub workflow**: Clone → Branch → Commit → Push → PR → Review → Merge
2. **Projekti seadistamine**: Repository → Issues → Projects → Labels → Milestones
3. **Dokumenteerimine**: Markdown, README-d, wiki-d
4. **Koostöö**: Peer review, tagasiside andmine, meeskonnatöö
5. **Planeerimine**: Backlog, sprint planning, roadmap
6. **Prototüüpimine**: Ideest paberprototüübini dokumenteeritud vormis

### Praktiline väljund:
Igal tudengil on kursuse lõpuks **GitHub portfolio** järgmiste elementidega:
- Professionaalne profiil
- Dokumenteeritud projektid
- Koostöö näited (PR-id, review-d)
- Uurimistööd ja reflektsioonid
- Prototüüpide dokumentatsioon

---

## 🎯 KURSUSE PEAMINE VÄÄRTUS

### Täielik software development lifecycle kogemus
Tudengid läbivad **päris arendusprotsessi** ilma koodimiseta:

| **Arenduse etapp** | **Seminar** | **Praktilised oskused** | **Tööriist** |
|---|---|---|---|
| **Project kickoff** | Seminar 1 ✅ | Git/GitHub workflow, dokumenteerimine | VSCode + Git |
| **Research ja analysis** | Seminar 2 | kasutajate uurimine, probleemi analüüs | Markdown docs |
| **Project planning** | Seminar 3 | meeskond, rollid, ajakavad | GitHub Projects |
| **Design ja prototyping** | Seminar 4 | UI/UX, wireframes, prototypes | paber + foto |
| **Development sprint** | Seminar 5 | sprint planning, progress tracking | GitHub Issues |
| **Testing ja release** | Seminar 6 | QA, release management, demo | GitHub Pages |

### Miks see toimib?
✅ **Kättesaadav algajatele** - ainult oskused, mida nad juba omavad  
✅ **Praktiline õpe** - päris projektide loomine, mitte ainult teooria  
✅ **Meeskonnatöö** - koostöö ja kommunikatsioon kogu protsessi vältel  
✅ **Nähtavad tulemused** - GitHub portfolio, prototüübid, dokumentatsioon  
✅ **Tööturul kasutatav** - Git, project management, collaboration skills  

### Tudengite väljund:
Kursuse lõpus on igal tudengil:
- 🗂️ **GitHub portfolio** professionaalsete projektidega
- 📋 **Täielik projekt** - alates uuringutest kuni "release-ini"
- 🤝 **Meeskonnatöö kogemus** erinevates rollides
- 📚 **Praktilised oskused** tööturul vajalikud (Git, project management, documentation)
- 🎯 **Arusaamine** kuidas tarkvaraarendus tegelikult töötab
- 💡 **Vastus küsimusele**: "Kuidas saab ideest siis lõpuks tarkvara?" - täielik pilt

---

## 🔄 Kuidas saab ideest siis lõpuks tarkvara?

Kursuse lõpuks mõistavad tudengid täielikult **tee ideest tarkvarani**:

### **1. IDEE** → **2. UURIMINE** → **3. PLANEERIMINE** → **4. DISAINIMINE** → **5. ARENDAMINE** → **6. TARKVARA**

| **Etapp** | **Küsimus** | **Tulemus** | **Kursuses õpitud** |
|---|---|---|---|
| **Idee** | "Mis probleemi lahendame?" | Probleemi definitsioon | Nõuete väljaselgitamine |
| **Uurimine** | "Kes on kasutajad?" | Kasutajate vajadused | Persoonad, kasutajalood |
| **Planeerimine** | "Kuidas töötame?" | Projekti plaan | GitHub Projects, rollid |
| **Disainimine** | "Kuidas see välja näeb?" | Prototüübid | Paberprototüüpimine |
| **Arendamine** | "Kuidas seda ehitame?" | Toote komponendid | Sprint-ide haldamine |
| **Tarkvara** | "Kas see töötab?" | Töötav toode | Testimine, release |

### **Kursuse võtmesõnum:**
> *"Tarkvara ei ole lihtsalt kood - see on protsess inimeste probleemide lahendamiseks, kus kood on ainult üks osa suuremast pildist."*

---

## Järgmised sammud

1. **Materjalde loomine** - iga seminari jaoks praktiliste harjutuste juhendid
2. **Template-de loomine** - GitHub repo template-id kodutöödeks
3. **Hindamiskriteeriumi täpsustamine** - rubric-ud iga kodutöö jaoks
4. **Eksami kujundamine** - praktiline eksam GitHub-is
5. **Õpetaja ressursside loomine** - juhendid kursuse läbiviimiseks