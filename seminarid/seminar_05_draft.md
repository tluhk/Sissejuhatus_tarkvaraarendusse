# Seminar 5: arendamine - sprint-ide haldamine ja ülesannete jälgimine

**Kestus**: 3h (90 min teooria + 90 min praktikat)  
**Fookus**: arendusprotsessi 4. etapp - töö organiseerimine ja jälgimine arenduse ajal

## Eesmärgid
Kursuse lõpus tudeng:
- Mõistab sprint-ide planeerimise ja haldamise põhimõtteid
- Oskab jagada suuremaid epic-uid väiksemateks ülesanneteks
- Teab arenduse jälgimise meetrikaid ja töövahendeid
- Oskab kasutada GitHub Projects keerukamaid funktsioone
- Mõistab continuous integration/delivery põhimõtteid
- Oskab organiseerida ja läbi viia daily standup-e

---

## OSA 1: TEOORIA (90 minutit)

### 1.1 Sprint planning põhimõtted (25 min)

#### Sprint-i anatoomia (10 min)
**Sprint-i definitsioon**: Fikseeritud ajaperiood (tavaliselt 1-4 nädalat), mille jooksul meeskond töötab kindlate eesmärkide nimel.

**Sprint-i komponendid**:
- **Sprint Goal**: Selge eesmärk, mida tahame saavutada
- **Sprint Backlog**: Konkreetsed ülesanded sprint-i jaoks
- **Definition of Done**: Kriteeriumid, millal ülesanne on valmis
- **Sprint commitment**: Meeskonna lubadus eesmärkide saavutamiseks

#### Epic-ute jagamine (user story decomposition) (10 min)
**Hierarhia**:
```
THEME (Teema)
├── EPIC (Suurem eesmärk)
│   ├── USER STORY (Kasutaja funktsioon)
│   │   ├── TASK (Konkreetne töö)
│   │   └── SUBTASK (Töö osa)
│   └── USER STORY
└── EPIC
```

**Näide jagamisest**:
```
THEME: Tudengite tähtaegade haldamine

EPIC: Tähtaegade visualiseerimine
├── USER STORY: Kalendrivaade
│   ├── TASK: Kalendri komponendi disain
│   ├── TASK: Andmete integreerimine
│   └── TASK: Mobile-responsive kujundus
├── USER STORY: Listvaade
│   ├── TASK: Sorteerimise funktsioon
│   └── TASK: Filtreerimise võimalused
└── USER STORY: Timeline vaade
    ├── TASK: Ajatelje visualiseerimine
    └── TASK: Drag & drop funktsioon
```

#### Story points ja estimating (5 min)
**Story points**: Suhteline keerukuse või jõupingutuse mõõt, mitte aeg.

**Fibonacci skaal**: 1, 2, 3, 5, 8, 13, 21
- **1 punkt**: Triviaalne ülesanne (30 min - 1h)
- **2 punkti**: Lihtne ülesanne (2-4h)
- **3 punkti**: Keskmine ülesanne (halb päev)
- **5 punkti**: Keeruline ülesanne (2-3 päeva)
- **8+ punkti**: Peaks jagama väiksemateks

**Planning poker**: Meeskond hindab koos, arutab erinevusi, jõuab konsensusele.

### 1.2 Backlog management ja prioritiseerimine (20 min)

#### Product backlog grooming (10 min)
**Backlog grooming** (refinement): Regulaarne protsess backlog-i parandamiseks.

**Grooming tegevused**:
- **Story breakdown**: Suurte epic-ute jagamine
- **Details adding**: Acceptance criteria täpsustamine
- **Estimation**: Story points hindamine
- **Ordering**: Prioriteetide määramine
- **Cleanup**: Vananenud user story-de eemaldamine

**Regulaarsus**: Tavaliselt sprint-i keskpaiku, 1-2h meeskonnaga.

#### Prioritiseerimise tehnikad (10 min)
**MoSCoW meetod**:
- **Must have**: Kritilised funktsioonid
- **Should have**: Olulised, aga mitte kriitilised
- **Could have**: Nice-to-have funktsioonid
- **Won't have**: Praegu välistatud

**Value vs Effort matrix**:
```
               High Value    Low Value
High Effort   [ Quick Wins ]  [ Fill-ins ]
Low Effort    [ Major Projects ] [ Thankless tasks ]
```

**Kano mudel**:
- **Basic needs**: Peab olemas olema
- **Performance needs**: Mida rohkem, seda parem
- **Delighters**: Ootamatud positiivsed üllatused

### 1.3 Arenduse jälgimise meetrikad (20 min)

#### Velocity tracking (8 min)
**Velocity**: Meeskonna produktiivsus story pointides sprint-i kohta.

**Arvutamine**:
```
Sprint 1: 18 story points (valmis)
Sprint 2: 22 story points (valmis)  
Sprint 3: 15 story points (valmis)
Average velocity: (18+22+15)/3 = 18.3 points/sprint
```

**Kasutamine**:
- **Planning**: Kui palju võtta järgmisesse sprint-i?
- **Forecasting**: Millal feature X valmis saab?
- **Improvement**: Kas meeskond muutub produktiivsemaks?

#### Burndown charts (7 min)
**Sprint burndown**: Kui palju tööd sprint-i jooksul järele jäi?

```
Story Points
     |
  25 |●
     |  ●
  20 |    ●
     |      ●●
  15 |         ●
     |           ●
  10 |             ●
     |               ●
   5 |                 ●
     |                   ●
   0 |____________________●
     Day 1  3  5  7  9  11  13
```

**Ideaalne vs tegelik**:
- **Ideaalne joon**: Lineaarne langus nullini
- **Tegelik joon**: Näitab tegelikku progressi
- **Analüüs**: Kas oleme plaaniga kursil?

#### Cycle time ja lead time (5 min)
**Lead time**: Aeg idee esitamisest kuni valmis tooteni  
**Cycle time**: Aeg töö alustamisest kuni valmimiseni

```
[Ideation] → [Backlog] → [Development] → [Testing] → [Done]
←------------- Lead Time ---------------→
              ←--- Cycle Time ---→
```

**Optimiseerimine**:
- Lühendada cycle time = kiirem tagasiside
- Vähendada WIP (work in progress) = vähem multitasking
- Automatiseerida testimine = kiirem deployment

### 1.4 Daily standups ja kommunikatsioon (15 min)

#### Daily standup struktuud (8 min)
**3 küsimust**:
1. **Mida tegid eile?** (edusammud)
2. **Mida teed täna?** (plaanid)
3. **Mis sind takistab?** (blocker-id)

**Reeglid**:
- **15 minutit max**: Lühidalt ja konkreetselt
- **Standing up**: Füüsiliselt püsti (või virtuaalselt "kiire")
- **Same time, same place**: Rutiin ja järjepidevus
- **Team focus**: Mitte manager reporting

**Anti-patterns vältida**:
- ❌ Detailne status reporting
- ❌ Probleemide lahendamine (tee eraldi)
- ❌ Uute ülesannete jagamine
- ❌ Hilised, puuduvad, multitasking

#### Remote teams kommunikatsioon (7 min)
**Asynchronous standup**:
- **Slack bot**: Daily kysimused automaatselt
- **Written updates**: Slack channel-is või Notion-is
- **Video recordings**: Lühikesed Loom videod

**Collaboration tools**:
- **GitHub**: Code review, issues, discussions
- **Slack/Discord**: Quick communication
- **Zoom/Teams**: Video meetings ja pairing
- **Notion/Confluence**: Documentation ja knowledge sharing

### 1.5 Continuous Integration basics (10 min)

#### CI/CD kontseptsioon (5 min)
**Continuous Integration**: Kood integreeritakse peamisse branch-i pidevalt (päevas mitu korda).

**CI pipeline näide**:
```
Developer push → Automated tests → Code review → Merge → Deploy
```

**Benefits**:
- Konfliktid leitakse kiiresti
- Automaatne kvaliteedi kontroll
- Deployment on predictable
- Vähem "integration hell"

#### GitHub Actions sisritus (5 min)
**Workflow näide**:
```yaml
name: Test and Deploy
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: npm test
      - name: Deploy to staging
        if: github.ref == 'refs/heads/main'
        run: deploy.sh
```

**Meie kontekstis**: GitHub Pages automaatne deployment dokumentatsioonile.

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 minutit)

### 2.1 Epic breakdown ja sprint planning (30 min)

#### Design epic-ute analüüs
**Aeg**: 10 minutit  
**Ülesanne**: Grupp analüüsib eelmise kodutöö tulemusi:
- Millised on peamised epic-ud prototüübi põhjal?
- Millised funktsioonid on kõige olulisemad?
- Millised on sõltuvused epic-ude vahel?

#### Epic-ute jagamine task-ideks
**Aeg**: 20 minutit  
**Ülesanne**: Iga roll tegeleb oma valdkonna epic-ute jagamisega:

**UX Designer**: Kasutajaliidese epic-ud
```
EPIC: Kasutajaliidese arendamine
├── USER STORY: Põhilehe layout
│   ├── TASK: Header komponendi disain
│   ├── TASK: Navigation menüü
│   └── TASK: Footer layout
├── USER STORY: Mobile responsive
│   ├── TASK: Breakpoint-ide defineerimine
│   └── TASK: Mobile navigation
```

**Product Owner**: Äriloogika epic-ud
```
EPIC: Kasutajate haldamine
├── USER STORY: Registreerimine
├── USER STORY: Sisse logimine
└── USER STORY: Profiili haldamine
```

**Technical Lead**: Tehnilised epic-ud
```
EPIC: Andmehaldus
├── USER STORY: Andmebaasi struktuur
├── USER STORY: API endpoints
└── USER STORY: Andmete sünkroniseerimine
```

**QA Lead**: Kvaliteedi epic-ud
```
EPIC: Testimine ja kvaliteet
├── USER STORY: Automaattestid
├── USER STORY: Kasutajatestid
└── USER STORY: Performance testing
```

### 2.2 GitHub Projects advanced setup (25 min)

#### Custom fields ja automation
**Aeg**: 15 minutit  
**Ülesanne**: Grupp seadistab advanced GitHub Projects funktsioone:

**Custom fields**:
- **Story Points**: Number field (1, 2, 3, 5, 8, 13)
- **Priority**: Select (Critical, High, Medium, Low)
- **Component**: Select (Frontend, Backend, Design, Testing)
- **Sprint**: Select (Sprint 1, Sprint 2, etc.)

**Automation rules**:
- Auto-assign PR-i author issues-le
- Auto-move "In Progress" kui branch luuakse
- Auto-move "Done" kui PR merge-itakse
- Auto-set labels based on file paths

#### Views ja workflows
**Aeg**: 10 minutit  
**Ülesanne**: Looge kolm view-d:

**1. Sprint Board**:
```
To Do | In Progress | Review | Done
Filter: Sprint = "Current Sprint"
Group by: Assignee
```

**2. Backlog Management**:
```
Table view:
Columns: Title, Priority, Story Points, Assignee, Sprint
Sort: Priority (desc), Story Points (asc)
```

**3. Roadmap Timeline**:
```
Timeline view:
Group by: Epic
Date field: Sprint dates
```

### 2.3 Sprint simulation (25 min)

#### Sprint 1 planning
**Aeg**: 15 minutit  
**Ülesanne**: Grupp simuleerib esimest sprint planning sessiooni:

**Sprint Goal määramine** (5 min):
- Üks lause, mis kirjeldab sprint-i eesmärki
- Näide: "Kasutajad saavad esimest korda sisse logida ja oma põhiandmed sisestada"

**Capacity planning** (5 min):
- Iga tudeng: 10-15 story points 2-nädalaseks sprint-iks
- Grupp kokku: ~40-60 story points
- Arvestada exam-e, muid kohustusi

**Tasks valimise** (5 min):
- Vali user stories eesmärgi saavutamiseks
- Kontrolli sõltuvusi ja prioriteete
- Määra assignee-d

#### Daily standup simulation
**Aeg**: 10 minutit  
**Ülesanne**: Simuleerige kolme päeva daily standup-e:

**Päev 1** (sprint algus):
- **Eile**: Sprint planning, ülesannete analüüs
- **Täna**: Esimeste task-idega alustamine
- **Blocker**: Ootan täpsustust design nõuetele

**Päev 5** (sprint keskpaik):
- **Eile**: Login komponent 80% valmis
- **Täna**: Testing ja bug fixes
- **Blocker**: API endpoint veel puudub

**Päev 10** (sprint lõpp):
- **Eile**: Kõik task-id valmis, testing
- **Täna**: Demo preparation ja retrospective
- **Blocker**: Ei ole

### 2.4 Metrics ja tracking setup (10 min)

#### Burndown chart loomine
**Ülesanne**: Looge template burndown chart tracking jaoks:

```
Sprint 1 Burndown Chart
Day 1:  40 points remaining
Day 3:  35 points remaining  
Day 5:  28 points remaining
Day 7:  18 points remaining
Day 10: 0 points remaining (ideal)
```

#### Velocity baseline määramine
**Ülesanne**: Meeskond lepib kokku:
- Esimese sprint-i velocity expectation
- Kuidas jälgida ja parandada
- Millal teha sprint planning järgmiseks

---

## Kodutöö 5: sprint-ide läbiviimine ja jälgimine

### Ülesande kirjeldus
**Tähtaeg**: 2 nädalat  
**Vorm**: Aktiivne GitHub projekt + daily updates

### Simulation struktuud
- **Sprint length**: 2 calendar weeks
- **Daily updates**: Iga tööpäev GitHub-is
- **Sprint ceremonies**: Planning, review, retrospective

### Ülesanded rollidega

#### Product Owner
- **Backlog prioritization**: Iga päev backlog-i hooldamine
- **Stakeholder communication**: Weekly updates "stakeholder-itele" (klassikaaslased)
- **Acceptance testing**: User stories acceptance criteria validation

#### Scrum Master  
- **Daily standup facilitation**: Daily updates koordineerimine
- **Metrics tracking**: Burndown, velocity, cycle time
- **Blockers management**: Takistuste dokumenteerimine ja lahendamine

#### UX Designer
- **Design validation**: Prototype testing kasutajatega (3+ feedback sessions)
- **User story refinement**: Acceptance criteria täpsustamine
- **Design iteration**: Prototype parandused feedback põhjal

#### Technical Lead
- **Technical task breakdown**: Epic-ute detailne jagamine
- **Architecture decisions**: Tehniliste valikute dokumenteerimine
- **Code review simulation**: GitHub PR-ide ülevaatamise simulatsioon

#### QA Lead
- **Test planning**: Test case-ide loomine iga user story jaoks
- **Bug tracking**: "Vigade" leidmine ja dokumenteerimine
- **Quality metrics**: Definition of Done kriteeriumite jälgimine

### Daily workflow
**Igal tööpäeval**:
1. **Daily standup update** GitHub Discussions-is
2. **Task progress update** GitHub Issues-is
3. **Documentation** oma töö kohta
4. **Collaboration** teiste rollidega

### Sprint ceremonies

#### Sprint Planning (nädal 1, algus)
- **Sprint goal** defineeritmine
- **User stories** valik ja breakdown
- **Capacity planning** ja commitments

#### Daily standups (iga tööpäev)
- **Asynchronous** GitHub Discussions kaudu
- **3 questions** formaat
- **Blockers** escalation

#### Sprint Review (nädal 2, lõpp)
- **Demo preparation**: Mida saavutati
- **Stakeholder feedback**: Klassikaaslaste kommentaarid
- **Retrospective input**: Mis läks hästi/halvasti

#### Sprint Retrospective (nädal 2, lõpp)
- **What went well**: Positiivsed aspektid
- **What could improve**: Parandamise kohad
- **Action items**: Järgmise sprint-i parandused

### Deliverables
- **Active GitHub Project**: Täielik sprint simulation
- **Daily updates**: Kõigi tööpäevade dokumenteerimine
- **Sprint artifacts**: Planning notes, retrospective summary
- **Individual reflection**: Oma rolli kogemus ja õppemised

### Hindamise kriteeriumid
- **Consistency**: Kas daily updates olid regulaarsed
- **Quality**: Ülesannete ja dokumentatsiooni kvaliteet
- **Collaboration**: Kuivõrd hästi rollid koos töötasid
- **Process adherence**: Kas järgisite sprint metodoloogiat
- **Learning reflection**: Iseharimise kvaliteet

---

## Materjalid ja ressursid

### Kohustuslik lugemine
- [The Sprint Book](https://www.thesprintbook.com/) - Jake Knapp
- [Scrum Guide](https://scrumguides.org/) - Jeff Sutherland & Ken Schwaber

### GitHub specifics
- [GitHub Projects documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub Actions for beginners](https://github.com/features/actions)

### Tools and templates
- **Project management**: GitHub Projects, Linear, Jira
- **Time tracking**: Toggl, Harvest (vabatahtlik)
- **Documentation**: Daily standup templates, retrospective formats

### Sprint templates
- `sprint-planning-template.md`
- `daily-standup-template.md`
- `sprint-review-template.md`
- `retrospective-template.md`

---

## Järgmine seminar
**Seminar 6: testimine ja release** - kuidas sprint-ide tulemusi testida, kvaliteeti tagada ja "toode" release-iks valmistada.
