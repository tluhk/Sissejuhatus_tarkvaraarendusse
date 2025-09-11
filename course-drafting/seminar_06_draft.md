# Seminar 6: testimine ja release - kvaliteedi tagamine ja väljastamine

**Kestus**: 3h (90 min teooria + 90 min praktikat)  
**Fookus**: arendusprotsessi 5. etapp - testimine, kvaliteedi tagamine ja toote väljastamine

## Eesmärgid
Kursuse lõpus tudeng:
- Mõistab erinevaid testimise liike ja metoodikaid
- Oskab planeerida ja läbi viia kasutajateste
- Teab kvaliteedi tagamise protsesse ja töövahendeid
- Mõistab release management põhimõtteid
- Oskab koostada release dokumentatsiooni
- Suudab reflekteerida õppimist ja anda tagasisidet

---

## OSA 1: TEOORIA (90 minutit)

### 1.1 Testimise liigid ja metoodikad (30 min)

#### Testimise hierarhia (test pyramid) (10 min)
```
                /\
               /  \    E2E Tests
              /    \   (vähemused)
             /      \
            /________\
           /          \  Integration Tests
          /            \ (mõõdukalt)
         /              \
        /________________\
       /                  \ Unit Tests
      /____________________\ (enamus)
```

**Unit Tests** (Ühiktestid):
- **Mis**: Testivad üksikuid funktsioone või komponente
- **Näide**: Kas parooli valideerimise funktsioon töötab õigesti?
- **Kiirus**: Väga kiired (millisektundid)
- **Maht**: Sadadest tuhandeteni

**Integration Tests** (Integratsioonitestid):
- **Mis**: Testivad komponentide koostööd
- **Näide**: Kas frontend ja backend API kommunikatsioon toimib?
- **Kiirus**: Keskmised (sekundid)
- **Maht**: Kümneid kuni sadu

**End-to-End Tests** (E2E testid):
- **Mis**: Testivad täielikke kasutaja stsenaariumeid
- **Näide**: Kasutaja registreerimisest kuni toote ostuni
- **Kiirus**: Aeglased (minutid)
- **Maht**: Kümneid

#### Manuaalne vs automaatne testimine (10 min)

**Manuaalne testimine**:
✅ **Eelised**:
- Inimlik intuitsioon ja kreatiivus
- Kasutajakogemuse hindamine
- Ad-hoc testimine ja uurimine
- Visuaalse disaini kontroll

❌ **Puudused**:
- Aeganõudev ja kulukas
- Inimlik eksimise võimalus
- Raske skaleerida
- Ei saa pidevalt käitada

**Automaatne testimine**:
✅ **Eelised**:
- Kiire ja järjepidev
- Saab integreerida CI/CD pipeline-i
- Regressioonitestide jaoks suurepärane
- Pikemas plaanis odavam

❌ **Puudused**:
- Aeganõudev seadistamine
- Ei leia kasutajakogemuse probleeme
- Maintenance overhead
- False positive/negative tulemused

#### QA protsessid (10 min)

**Shift-left testing**: Testimine algab varajases faasis
```
Planeerimine → Disain → Arendamine → Testimine → Release
     ↑           ↑         ↑           ↑         ↑
  Test planning  Test cases  Unit tests  QA testing  UAT
```

**Quality Gates**: Kindlad kriteeriumid enne järgmisesse faasi liikumist
- Code review peab olema tehtud
- Kõik automaattestid peavad läbima
- Test coverage peab olema > 80%
- Performance kriteeriumid täidetud

**Bug lifecycle**:
1. **New**: Bug avastatud ja raporteeritud
2. **Assigned**: Määratud arendajale
3. **In Progress**: Arendaja töötab parandusega
4. **Fixed**: Arendaja märgib parandatuks
5. **Verified**: QA kinnitab paranduse
6. **Closed**: Bug suletud

### 1.2 Kasutajatestide planeerimine (20 min)

#### Usability testing meetodid (10 min)

**Moderated vs unmoderated**:
- **Moderated**: Testija juhendab kasutajat reaalajas
- **Unmoderated**: Kasutaja testib iseseisvalt

**Remote vs in-person**:
- **Remote**: Odavam, laiem geograafiline ulatus
- **In-person**: Parem vaatlus, detail-tagasiside

**Think-aloud protocol**:
- Kasutaja räägib valjusti oma mõtetest
- "Ma otsin nüüd logimise nuppu..."
- "See nüüp on segadust tekitav..."

#### Test protokolli koostamine (10 min)

**Test session struktuur**:
1. **Sissejuhatus** (5 min): Testimise selgitamine, nõusolek
2. **Tausta küsimused** (5 min): Demograafia, kogemused
3. **Tasks** (30-40 min): Konkreetsed ülesanded
4. **Post-task questions** (10 min): Tagasiside ja SUS hindamine
5. **Lõpetamine** (5 min): Tänamine ja järgmised sammud

**Test tasks näited**:
```
TASK 1: Esmatutvumine
"Kujutage ette, et sattusite esimest korda sellele lehele. 
Vaadake ringi ja rääkige, mida näete."

TASK 2: Konkreetne eesmärk
"Proovige leida oma täna tähtaegade kodutöö."

TASK 3: Keerulisem stsenaarium
"Teil tekib küsimus kodutöö kohta. Kuidas võtaksite 
õpetajaga ühendust?"
```

### 1.3 Release management (25 min)

#### Versioning strategies (10 min)

**Semantic Versioning (SemVer)**:
```
MAJOR.MINOR.PATCH (2.1.4)

MAJOR: Breaking changes (2.0.0 → 3.0.0)
MINOR: New features, backward compatible (2.1.0 → 2.2.0)  
PATCH: Bug fixes (2.1.4 → 2.1.5)
```

**Git tagging**:
```bash
git tag v1.0.0
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

**GitHub Releases**:
- Release notes automaatgeneereerimine
- Binary failide lisamine
- Pre-release märgendamine

#### Release planning (8 min)

**Release types**:
- **Major release**: Suured muudatused, marketingi võimalus
- **Minor release**: Uued funktsioonid, regulaarselt
- **Patch release**: Kiired vigade parandused
- **Hotfix**: Kriitilised turvalisuse parandused

**Release timeline**:
```
4 weeks before: Feature freeze
3 weeks before: Code freeze  
2 weeks before: Testing sprint
1 week before: Release candidates
Release day: Go live + monitoring
```

#### DevOps ja deployment (7 min)

**Continuous Integration/Continuous Deployment**:
```
Code → Test → Build → Deploy → Monitor
  ↑                                ↓
  └─── Feedback ← Metrics ←────────┘
```

**Deployment strategies**:
- **Blue-Green**: Kaks identset keskkonda, kiire ümberlülitus
- **Rolling**: Järkjärguline uuendamine
- **Canary**: Väikese kasutajategrupi testimine

**GitHub Pages näide**:
```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Node
        uses: actions/setup-node@v2
      - name: Build
        run: npm run build
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
```

### 1.4 Dokumentatsiooni standardid (15 min)

#### Release notes kirjutamine (8 min)

**Hea release note struktuud**:
```markdown
# Release v2.1.0 - November 2024

## 🚀 New Features
- Added dark mode toggle in settings
- Integrated calendar sync with Google Calendar

## 🐛 Bug Fixes  
- Fixed notification timing issues
- Resolved mobile navigation overlap

## 🔧 Improvements
- Improved page loading speed by 40%
- Updated color scheme for better accessibility

## ⚠️ Breaking Changes
- API endpoint /api/v1/users deprecated, use /api/v2/users

## 📖 Documentation
- Added deployment guide
- Updated API documentation
```

**Audientsi arvestamine**:
- **Technical audience**: API changes, dependencies
- **End users**: UI changes, new features
- **Stakeholders**: Business impact, metrics

#### API dokumentatsiooni (7 min)

**README.md standard struktuud**:
```markdown
# Project Name

## Description
What the project does and why it's useful.

## Installation
Step-by-step setup instructions.

## Usage
Examples of how to use the project.

## Contributing  
How others can contribute.

## License
Legal usage terms.
```

**Dokumentatsiooni automatsiooon**:
- GitHub Pages automaatne deployment
- Docusaurus või GitBook integratsioon
- API docs JSDoc või OpenAPI genereerimisega

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 minutit)

### 2.1 Kasutajatestide läbiviimine (35 min)

#### Test protokolli ettevalmistus
**Aeg**: 10 minutit  
**Ülesanne**: Iga grupp valmistab ette kasutajatesti:

**Test scenario loomine**:
- Vali 3 peamist user story-t testimiseks
- Kirjuta task-id loomuliku keele kasutamisega
- Valmista ette post-task küsimused

**Template kasutamine**:
```markdown
## Test Session Plan

### Participant: ___________
### Date: _______________

#### Background Questions (5 min)
1. Kui sageli kasutate sarnaseid äppe?
2. Milline on teie tehniline kogemustase?

#### Tasks (25 min)
**Task 1**: [konkretne ülesanne]
- Success criteria: [millal on edukas]
- Observations: [märkmed]

#### Post-Task Questions (10 min)
1. SUS score (1-10): Kui lihtne oli kasutada?
2. Mis oli kõige frustreerivam?
3. Mida parandaksite?
```

#### Kasutajatestide simulatsioon
**Aeg**: 20 minutit  
**Ülesanne**: Grupid paaristavad ja testivad teineteise prototüüpe:

**Rollid**:
- **Moderator**: Juhendab testisessiooni
- **Observer**: Märgib käitumist ja kommentaare
- **Participant**: Proovib prototüüpi kasutada
- **Note-taker**: Dokumenteerib tulemused

**Protsess**:
- 10 min: Grupp A testib grupi B prototüüpi
- 10 min: Grupp B testib grupi A prototüüpi

#### Tulemuste analüüs
**Aeg**: 5 minutit  
**Ülesanne**: Kogu tagasiside analüüs:
- Millised on peamised usability probleemid?
- Mis oli ootamatult hästi?
- Mida kindlasti muuta tuleb?

### 2.2 Bug reporting ja quality assurance (20 min)

#### Bug reporting harjutus
**Aeg**: 15 minutit  
**Ülesanne**: Kasutajatestide põhjal bug raportite kirjutamine:

**Bug report template**:
```markdown
## Bug Report #001

### Title: [Lühike kirjeldus]

### Priority: High/Medium/Low

### Steps to Reproduce:
1. Step 1
2. Step 2  
3. Step 3

### Expected Result:
What should happen

### Actual Result:
What actually happened

### Environment:
- Device: iPhone 12
- Browser: Safari 14
- Screen size: 375x812

### Screenshots:
[Attach if relevant]

### Additional Notes:
Any other relevant information
```

**Bug kategoriseerimine**:
- **Critical**: Rakendus ei toimi
- **High**: Peamine funktsioon rikutud
- **Medium**: Ebasobiv kasutajakogemus
- **Low**: Cosmelised probleemid

#### Quality checklist loomine
**Aeg**: 5 minutit  
**Ülesanne**: Definition of Done kriteeriumide täpsustamine:

```markdown
## Definition of Done Checklist

### Functionality
- [ ] Feature works as described in acceptance criteria
- [ ] Edge cases are handled appropriately
- [ ] Error messages are user-friendly

### Quality
- [ ] Code reviewed by teammate
- [ ] No critical bugs found in testing
- [ ] Performance meets requirements

### Documentation
- [ ] README updated if needed
- [ ] User guide updated
- [ ] API documentation current

### User Experience
- [ ] Works on mobile and desktop
- [ ] Accessible design principles followed
- [ ] User feedback incorporated
```

### 2.3 Release ettevalmistus (25 min)

#### Release package'i koostamine
**Aeg**: 15 minutit  
**Ülesanne**: Iga grupp valmistab ette oma "toote" release:

**GitHub repository korrastamine**:
- README.md täielik uuendamine
- Dokumentatsiooni organiseerumine
- Mittevajalike failide puhastamine
- License faili lisamine

**Release notes draft**:
```markdown
# [Product Name] v1.0.0 - Final Release

## 📝 Overview
This is the first major release of [Product Name], 
a solution for [problem description].

## ✨ Key Features
- **Feature 1**: Description and benefit
- **Feature 2**: Description and benefit
- **Feature 3**: Description and benefit

## 👥 User Personas Supported
- **Primary**: [Main persona] - [key use case]
- **Secondary**: [Second persona] - [key use case]

## 🔄 User Journeys
- [Main user journey]: [description]
- [Secondary journey]: [description]

## 📋 Testing Results
- **User tests conducted**: X sessions
- **Key findings**: [summary]
- **Usability score**: X/10

## 🚀 Future Roadmap
- **Next release**: [planned features]
- **Long-term vision**: [future plans]

## 👏 Team Credits
- [Role]: [Name] - [contribution]
- [Role]: [Name] - [contribution]
```

#### GitHub Pages deployment
**Aeg**: 10 minutit  
**Ülesanne**: Project presentation veebilehe seadistamine:

**Structure näide**:
```
docs/
├── index.html          # Project overview
├── user-research/      # Research findings  
├── design/            # Prototypes and design
├── development/       # Technical documentation
└── testing/          # Testing results
```

### 2.4 Esitluste ettevalmistus (10 min)

#### Demo structure planeerimine
**Ülesanne**: Grupp planeerib 5-minutilise esitluse:

**Esitluse struktuud**:
1. **Problem** (30s): Mis probleemi lahendame?
2. **Solution** (60s): Meie lahenduse demo
3. **Process** (120s): Kuidas töötasime?
4. **Results** (60s): Mida saavutasime?
5. **Learning** (30s): Peamine õppetund?

**Demo ettevalmsutus**:
- Kes mida räägib?
- Millised ekraanid näitame?
- Kuidas prototüüpi demonstreerime?
- Millised on backup plaanid?

---

## Kodutöö 6: final release ja portfolio

### Ülesande kirjeldus
**Tähtaeg**: 1 nädal  
**Vorm**: Täielik GitHub portfolio + projekt release

### Grupi deliverables
- **Complete project release**: Dokumenteeritud ja testitud toode
- **Release documentation**: Release notes, user guide, technical docs
- **Portfolio website**: GitHub Pages projekt esitlus
- **Demo video**: 3-5 minutit project walkthrough

### Individuaalsed deliverables

#### Kõik rollid
- **Individual portfolio README**: Kõigi kursuse projektide ülevaade
- **Role reflection**: 2-3 lk analüüs oma rolli kogemusest
- **Tool evaluation**: VSCode, GitHub, markdown töövahendite hinnang
- **Peer evaluation**: Tiimiliikmete töö hindamine

#### UX Designer
- **Usability testing report**: Põhjalik testimistulemuste analüüs  
- **Design evolution**: Kuidas disain arenes läbi iteratsioonide
- **Future improvements**: Mida edasi arendada

#### Product Owner
- **Product roadmap**: Tuleviku arenduste plaan
- **Business case**: Miks see toode on vajalik
- **Success metrics**: Kuidas edu mõõta

#### Technical Lead  
- **Technical documentation**: Arhitektuur ja tehnilised valikud
- **Implementation plan**: Kuidas toote tegelikult ehitada
- **Technical debt analysis**: Tehnilised riskid ja parandused

#### QA Lead
- **Quality report**: Testimise tulemused ja kvaliteedi hinnang
- **Test strategy**: Kompleksne testimise raamistik
- **Quality roadmap**: Kuidas kvaliteeti edasi tagada

#### Scrum Master (või Documentation Manager)
- **Process analysis**: Kuidas meeskond töitas
- **Communication effectiveness**: Mis toimis, mis mitte
- **Process improvements**: Soovitused tuleviku projektideks

### Portfolio struktuud
```
github.com/[username]/portfolio/
├── README.md              # Portfolio overview
├── course-reflection.md   # Learning journey analysis
├── [project-name]/        # Main course project
│   ├── README.md         # Project overview
│   ├── research/         # User research findings
│   ├── design/           # Prototypes and designs  
│   ├── development/      # Sprint documentation
│   ├── testing/          # QA and user testing
│   └── release/          # Final release materials
└── individual-work/      # Personal contributions
    ├── role-reflection.md
    ├── tool-evaluation.md
    └── peer-feedback.md
```

### Esitlused (seminar lõpus)
- **5 minutit grupile**: Project demo ja tulemused
- **2 minutit isiklikult**: Peamine õppetund oma rollist

### Hindamise kriteeriumid
- **Completeness**: Kas kõik deliverable-id on valmis
- **Quality**: Dokumentatsiooni ja analüüsi tase
- **Integration**: Kas grupi- ja individuaaltöö on integreeritud
- **Reflection**: Õppimise ja arengu reflektsiooni kvaliteet
- **Presentation**: Demo ja esitluse professionaalsus

---

## Materjalid ja ressursid

### Kohustuslik lugemine
- [Don't Make Me Think](https://sensible.com/dont-make-me-think/) - Steve Krug
- [The Design of Everyday Things](https://jnd.org/the-design-of-everyday-things-revised-and-expanded-edition/) - Don Norman

### Testing tools
- **Usability testing**: Zoom screen sharing, mobile screen recording
- **Bug tracking**: GitHub Issues, linear, notion
- **Documentation**: GitBook, Docusaurus, GitHub Pages

### Templates ja näited
- `usability-test-protocol.md`
- `bug-report-template.md`
- `release-notes-template.md`
- `portfolio-readme-template.md`

### Portfolio inspiratsioon
- [GitHub Portfolio Examples](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
- [Developer Portfolio Ideas](https://github.com/emmawedekind/developer-portfolios)

---

## Kursuse lõpetamine

### Järgmised sammud
- **Portfolio säilitamine**: GitHub repo public või private?
- **Networking**: LinkedIn profiili uuendamine omandatud oskustega
- **Continuous learning**: Järgmised kursused ja resource-id

### Refleksioon
**Kursuse võtmesõnum**: 
> *"Tarkvara ei ole lihtsalt kood - see on protsess inimeste probleemide lahendamiseks, kus kood on ainult üks osa suuremast pildist."*

### Kursusee tagasiside
- Anonymous feedback form kursuse kohta
- Soovitused järgmiste semestrite jaoks
- Resource-ide ja materjalide hinnang
