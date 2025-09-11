# Seminar 3: planeerimine - projektijuhtimine ja meeskonnatöö

**Kestus**: 3h (90 min teooria + 90 min praktikat)  
**Fookus**: arendusprotsessi 2. etapp - projekti struktureerimine ja meeskonna organiseerimine

## Eesmärgid
Kursuse lõpus tudeng:
- Mõistab erinevaid arendusmetoodikaid ja nende rakendamist
- Oskab planeerida projekte ja jagada tööd
- Teab tarkvaraarenduse rolle ja vastutusi
- Oskab kasutada GitHub-i projektijuhtimise tööriistadena
- Mõistab meeskonnatöö dünaamikat ja kommunikatsiooni

---

## OSA 1: TEOORIA (90 minutit)

### 1.1 Arendusmetoodikate ülevaade (35 min)

#### Kosk/Waterfall mudel (10 min)
**Iseloomustus**: lineaarne, sammhaaval 

**Etapid**:
1. Nõuete kogumine ja analüüs
2. Süsteemi disain
3. Rakendamine (koodimine)
4. Testimine
5. Juurutamine
6. Hooldus

**Eelised**:
- ✅ Selge struktuur ja dokumentatsioon
- ✅ Hea, kui nõuded ei muutu tihti
- ✅ Lihtne planeerida ja jälgida

**Puudused**:
- ❌ Vähe paindlikkust muudatusteks
- ❌ Hiline tagasiside
- ❌ Risk, et lõpptulemus ei vasta vajadustele

**Millal kasutada**: Selged, stabiilsed nõuded; reguleeritud valdkonnad

#### Agiilne arendus ja põhimõtted (10 min)
**4 põhiväärtust**:
1. **Inimesed ja koostöö** > protsessid ja tööriistad
2. **Töötav tarkvara** > põhjalik dokumentatsioon
3. **Koostöö kliendiga** > lepingu tingimused
4. **Reageerimine muudatustele** > plaani järgimine

**12 agiilse arenduse põhimõtet** (võtmepunktid):
- Kliendi rahulolu läbi pideva väärtuse tarnimise
- Muudatusi saab teha ka projekti hilises faasis
- Töötavat tarkvara sage tarnimine (nädalad, mitte kuud)
- Äri ja arendajad töötavad koos iga päev
- Saab ehitada projektid motiveeritud inimeste ümber

#### Scrum raamistik (15 min)
**Rollid**:
- **Product Owner**: Toote omanik, backlog haldamine, prioriteedid
- **Scrum Master**: Protsessi juhtimine, takistuste eemaldamine
- **Development Team**: Arendusmeeskond, toote arendamine

**Sündmused (Ceremonies)**:
- **Sprint Planning**: Sprint eesmärkide määramine (2-4h)
- **Daily Scrum**: Igapäevane sünkroniseerimine (15 min)
- **Sprint Review**: Tulemuste demonstreerimine (1-2h)
- **Sprint Retrospective**: Protsessi parandamine (1h)

**Artefaktid**:
- **Product Backlog**: Prioritiseeritud funktsioonide nimekiri
- **Sprint Backlog**: Aktiivselt töödeldavad ülesanded
- **Increment**: Tööta tarkvara sprint lõpus

**Sprint tsükkel**: 1-4 nädalat, tavaliselt 2 nädalat

### 1.2 Kanban ja Lean põhimõtted (20 min)

#### Kanban süsteem (10 min)
**Põhiprintsiip**: Töövoogude visualiseerimine ja piiramine

**Kanban tahvel**:
```
To Do | In Progress | Review | Done
------|-------------|---------|------
 □    |     □       |    □    |   ■
 □    |     □       |    □    |   ■
 □    |             |         |   ■
```

**6 Kanban praktikat**:
1. **Visualiseeri töövoog**: Nähtav tahvel
2. **Piira WIP** (Work in Progress): Max. ülesanded samaaegselt
3. **Juhi voogu**: Tõhusus üle kiiruse
4. **Muuda reeglid selgeks**: Millal liigub järgmisesse veergu
5. **Tagasiside tsüklid**: Regulaarsed ülevaated
6. **Paranda koostöös**: Meeskonnaga koos

**Eelised**:
- Paindlik, ei vaja kindlaid rolle
- Jätkuv voog, mitte sprint-id
- Kiire reageermine muudatustele

#### Lean põhimõtted (10 min)
**7 raiskamise liiki tarkvaraarenduses**:
1. **Üleproduktsioon**: Ebavajalikud funktsioonid
2. **Ootamine**: Blokeeritud ülesanded
3. **Transport**: Informatsiooni edastamine
4. **Üleprotsessimine**: Liigne dokumenteerimine
5. **Ladu**: Pooleliolevad tööd
6. **Liikumine**: Konteksti vahetus
7. **Defektid**: Vead ja parandamise vajadus

**Lean eesmärk**: Maksimaalne väärtus minimaalse raiskamisega

### 1.3 Rollid tarkvaraarenduses (20 min)

#### Tehnilised rollid (10 min)
**Front-end Developer**:
- Kasutajaliides ja kasutajakogemus
- HTML, CSS, JavaScript, React/Vue/Angular
- Brauseriühilduvus, responsiivne disain

**Back-end Developer**:
- Server, andmebaas, API-d
- Java, Python, Node.js, SQL
- Jõudlus, turvalisus, skaleeruvus

**Full-stack Developer**:
- Nii front-end kui back-end
- Väiksemad meeskonnad, prototüübid

**DevOps Engineer**:
- Infrastruktuur, deployment, monitoring
- Docker, Kubernetes, AWS/Azure
- CI/CD, automatiseerimine

#### Projektijuhtimise rollid (5 min)
**Product Manager**:
- Toote visioon ja strateegia
- Turuanalüüs, konkurentsianalüüs
- Funktsioonide prioritiseerimine

**Project Manager**:
- Projekti planeerimine ja koordineerimine
- Ressursside haldamine, ajakavad
- Kommunikatsioon sidusrühmadega

**Scrum Master**:
- Agile protsessi jälgimine
- Takistuste eemaldamine
- Meeskonna coaching

#### Disaini ja kvaliteedi rollid (5 min)
**UX Designer**:
- Kasutajakogemuse disain
- Uuringud, prototüübid, testimine

**UI Designer**:
- Visuaalne disain ja graafiline kujundus
- Stiilijuhendid, komponendid

**QA Engineer/Tester**:
- Kvaliteedi tagamine, testimine
- Test case-id, automaattestid
- Bug reporting ja jälgimine

### 1.4 Meeskonnatöö ja kommunikatsioon (15 min)

#### Efektiivse meeskonna omadused (5 min)
- **Psühholoogiline ohutus**: Võib teha vigu ja küsida
- **Usaldusväärsus**: Kõik teevad kokkulepitud töö
- **Struktuur ja selgus**: Rollid ja eesmärgid selged
- **Tähenduse tunne**: Töö on oluline
- **Mõju**: Näeb oma panuse tulemusi

#### Kommunikatsiooni raamistikud (5 min)
**Sünkroonne kommunikatsioon**:
- Stand-up meetingud: Iga päev, 15 min
- Planning sessions: Sprint alguses
- Review ja retrospective: Sprint lõpus

**Asünkroonne kommunikatsioon**:
- GitHub kommentaarid ja PR-id
- Dokumentatsioon ja wiki
- Slack/Teams sõnumid

#### Remote vs co-located meeskonnad (5 min)
**Remote töö väljakutsed**:
- Kommunikatsiooni takistused
- Kultuurilised erinevused
- Ajavööndite erinevused

**Lahendused**:
- Regulaarsed video-kõned
- Asünkroonsed töövood
- Hästi dokumenteeritud protsessid
- Kultuuriline teadlikkus

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 minutit)

### 2.1 Rollide jaotamine ja meeskonna moodustamine (15 min)

#### Rollide tutvustus ja valik
**Ülesanne**: Iga tudeng valib endale peamise rolli järgmisteks seminariteks:

**Võimalikud rollid**: (Ilmselt mõistlik muuta, kuna Scrummasteriks niteks peaks ikka õppima jms)
- **Product Owner**: Toote visioon, prioriteedid, kasutajate esindamine
- **Scrum Master**: Protsessi koordineerimine, takistuste lahendamine
- **UX Designer**: Kasutajakogemus, uuringud, testimine
- **Technical Lead**: Tehnilised otsused, arhitektuur
- **QA Lead**: Kvaliteedi tagamine, testimine
- **Documentation Manager**: Dokumentatsiooni ja kommunikatsiooni koordineerimine

#### Rolli kirjelduse koostamine
**Aeg**: 10 minutit  
**Ülesanne**: Iga tudeng kirjutab:
- Oma rolli peamised vastutused projektis
- Millised tulemused on tema vastutada
- Kuidas ta oma rolli edukust mõõdab

### 2.2 Projekti ajakava loomine (25 min)

#### Projekti ajakava workshop
**Aeg**: 20 minutit  
**Ülesanne**: Grupp täidab projekti ajakava templiidi:

```markdown
# PROJECT AJAKAVA

## Projekti ülevaade
- **Projekti nimi**: 
- **Probleemi kokkuvõte**: (1-2 lauset)
- **Lahenduse visioon**: (1-2 lauset)

## Eesmärgid ja edu kriteeriumid
- **Peamised eesmärgid**: (3-5 punkti)
- **Edu kriteeriumid**: (kuidas mõõdame edu?)
- **Mitte-eesmärgid**: (mida me EI tee)

## Meeskond ja rollid
| Roll | Nimi | Vastutus |
|------|------|----------|
| Product Owner | | |
| Scrum Master | | |
| UX Designer | | |

## Ajakava ja milestoneid
| Milestone | Kuupäev | Kirjeldus |
|-----------|---------|-----------|
| Prototype 1 | | Esimene paberprototüüp |
| User Testing | | Kasutajatestide läbiviimine |
| Final Prototype | | Lõplik prototüüp ja dokumentatsioon |

## Riskid ja väljakutsed
- **Peamised riskid**: (3-5 riski)
- **Leevendamise strateegiad**: (kuidas riske vähendada)
```

#### Ajakava visualiseerimine
**Aeg**: 5 minutit  
**Ülesanne**: Roadmap loomine Miros/Figmas või paberil

### 2.3 GitHub organisatsiooni ja projekti seadistamine (30 min)

#### Repositooriumi struktuuri planeerimine
**Aeg**: 10 minutit  
**Ülesanne**: Meeskond lepib kokku:
- Repositooriumi nime ja kirjelduse
- Folder struktuuri (dokumentatsioon, disain, prototypes jne)
- Branching strateegia (main, develop, feature branches)
- Commit message konventsioonid

#### GitHub Projects konfigureerimine
**Aeg**: 15 minutit  
**Ülesanne**: 
1. **Project board loomine** GitHub-is
2. **Vaadete (views) seadistamine**:
   - Backlog view: Kõik ülesanded prioriteediga
   - Sprint board: To Do, In Progress, Review, Done
   - Roadmap: Timeline view milestoneitega
3. **Labelite süsteemi** loomine:
   - Tüübid: feature, bug, documentation, research
   - Prioriteedid: high, medium, low
   - Komponendid: frontend, backend, design, testing

#### Epic-ute ja esimeste issue-te loomine
**Aeg**: 5 minutit  
**Ülesanne**: 
- Loo 3-4 epic-ut järgmiste seminarite jaoks
- Lisa esimesed 5-6 issue-t backlog-i
- Määra igale issue-le assignee ja label

### 2.4 Branching strateegia harjutus (20 min)

#### Git workflow demonstration
**Aeg**: 10 minutit  
**Demonstratsioon**: Õpetaja näitab:
1. Main branch kaitse seadistamine
2. Feature branch loomine
3. Pull request protsess
4. Code review workflow
5. Merge strateegiad

#### Praktiline harjutus
**Aeg**: 10 minutit  
**Ülesanne**: Iga tudeng:
1. Loob oma feature branch-i
2. Lisab oma rolli kirjelduse faili
3. Teeb commit konventsiooni järgi
4. Esitab pull request-i
5. Vaatab üle kellegi teise PR-i

---

## Kodutöö 3: projektijuhtimise plaan

### Ülesande kirjeldus
**Tähtaeg**: 1 nädal  
**Vorm**: GitHub repositoorium + individuaalne panus

### Grupi osa
- **Täielik projekti plaan**: Charter, roadmap, riskianalüüs
- **GitHub Projects seadistamine**: Backlog, workflows, automation
- **Meeskonna töökorraldus**: Kommunikatsiooni plaanid, regulaarsed aruanded
- **Sprint planning**: Esimese sprint-i planeerimine

### Rolli-põhised ülesanded

#### Product Owner
- **Product backlog prioritiseerimine**: Kõik user stories prioriteediga
- **Acceptance criteria**: Igale user story-le selged kriteeriumid
- **Stakeholder communication plan**: Kuidas sidusrühmi kaasata

#### Scrum Master
- **Sprint rytmi planeerimine**: Planning, daily, review, retro schedule
- **Metrics definition**: Velocity, burndown, cycle time mõõtmise plaan
- **Process documentation**: Kuidas me töötame kokkuleppe

#### UX Designer
- **User research strategy**: Kuidas kasutajaid kaasame ja testide
- **Design system plan**: Komponendid ja standardid
- **Usability testing framework**: Testimise metoodika

#### Technical Lead
- **Technical architecture**: Ülevaade tehnilisest lahendusest
- **Development workflow**: Coding standards, review process
- **Risk mitigation**: Tehniliste riskide analüüs

#### QA Lead
- **Testing strategy**: Millised testid ja millal
- **Quality metrics**: Kuidas kvaliteeti mõõdame
- **Bug tracking process**: Vigade raporteerimise süsteem

#### Documentation Manager
- **Documentation strategy**: Mis dokumenteerida ja kuidas
- **Communication protocols**: Meeting notes, status updates
- **Knowledge management**: Kuidas infot organiseerida

### Esitamise vorm
- **GitHub repository**: Täielik projektijuhtimise dokumentatsioon
- **Role-based branches**: Iga roll töötab oma branch-is
- **Cross-role review**: Rollide vaheline ülevaatus
- **Final integration**: Kõigi osade integreerimine

### Hindamise kriteeriumid
- **Terviklikkus**: Kas kõik aspektid on kaetud
- **Realistlikkus**: Kas plaanid on teostatavad
- **Detailsus**: Rolli-spetsiifilise töö kvaliteet
- **Koostöö**: GitHub workflow ja cross-role review

---

## Materjalid ja ressursid

### Kohustuslik lugemine
- [Scrum Guide](https://scrumguides.org/) - ametlik Scrum definitsioon
- [Agile Manifesto](https://agilemanifesto.org/) - algne agile manifest
- [Kanban Guide](https://kanbanguides.org/) - ametlik Kanban juhend

### Soovituslikud tööriistad
- **Project planning**: GitHub Projects, Miro, Notion
- **Communication**: Discord/Slack workspace
- **Documentation**: Notion, Confluence, GitBook

### Template failid
- `project-charter-template.md`
- `sprint-planning-template.md`
- `role-description-template.md`
- `risk-assessment-template.md`

---

## Järgmine seminar
**Seminar 4: disainimine** - kuidas projektiplaan ja kasutajate uuringud muuta konkreetseteks prototüüpideks ja kasutajaliideseks.
