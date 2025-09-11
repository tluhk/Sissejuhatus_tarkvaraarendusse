# Sissejuhatus tarkvaraarendusse - uus kursuse kavand

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
- **Projekti juhtimine**: Oskab organiseerida ja planeerida projekte
- **Probleemi uurimine**: Oskab analüüsida kasutajate vajadusi ja probleeme
- **Nõuete kogumine**: Oskab kirjeldada funktsionaalseid ja mitte-funktsionaalseid nõudeid
- **Disaini kavandamine**: Oskab luua paberprototüüpe ja kasutajaliidese visandeid
- **Arenduse planeerimine**: Oskab jagada tööd ülesanneteks ja planeerida sprinte
- **Kvaliteedi tagamine**: Oskab testida, dokumenteerida ja üle vaadata
- **Versiooni haldamine**: Oskab kasutada Git/GitHub-i kogu protsessi vältel
- **Tiimitöö**: Oskab töötada erinevates rollides ja anda tagasisidet

### Läbiv filosoofia: täielik arendusprotsess
Iga seminar vastab **ühele arenduse etapile**:
1. ✅ **Alustamine** - Tööriistad ja versioonikontroll
2. **Uurimine** - Probleemi defineerimine ja analüüs  
3. **Planeerimine** - Projektijuhtimine ja meeskonnatöö
4. **Disainimine** - Kasutajaliides ja prototüüpimine
5. **Arendamine** - Ülesannete haldamine ja sprint-id
6. **Testimine ja release** - kvaliteedikontroll ja väljastamine

### Kasutatavad oskused (mitte kodeerimine):
- **Dokumenteerimine** (Markdown)
- **Paberprototüüpimine** (käsitsi joonistamine)
- **Projekti haldamine** (GitHub Projects)
- **Uurimistöö** (kasutajate intervjuud, analüüs)
- **Testimine** (kasutajatestid prototüüpidega)
- **Meeskonnatöö** (rollid, kommunikatsioon)

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
**Kestus**: 3h  
**Fookus**: arendusprotsessi 1. etapp - probleemi defineerimine ja uurimine

#### Arenduse etapp: problem discovery ja user research
**Pärisarenduses**: Analüütikud ja UX-uurijad koguvad andmeid kasutajate kohta  
**Meie kursuses**: Tudengid õpivad uurima ja dokumenteerima probleeme

#### Teemad:
- Probleemi defineerimine ja analüüs
- Kasutajate uurimise meetodid (intervjuud, küsitlused, vaatlused)
- **Harjutus nõuete väljaselgitamiseks** - praktiline meetod
- VSCode + Markdown uurimistulemuste dokumenteerimiseks
- Konkurentsianalüüs ja turu-uuringud
- **Funktsionaalsed vs mitte-funktsionaalsed nõuded**
- Nõuete kogumine ja dokumenteerimine

#### Praktilised harjutused:
- **Grupi probleemi valimine** (järgmiste seminarite jaoks)
- **Kasutajate "intervjueerimine"** (rollimäng või päris intervjuud)
- **Konkurentsianalüüs** (olemasolevate lahenduste uurimine)
- **Uurimistulemuste dokumenteerimine** Markdown-is
- **GitHub töövoog**: Research → Document → PR → Review

#### Kodutöö 2:
- **Teema**: Süvauurimine valitud probleemi kohta
- **Ülesanne**: 
  - Grupp valib ühise probleemi (nt tudengite ajakava haldamine)
  - Igaüks uurib erinevat aspekti: kasutajad, konkurendid, tehnoloogiad, ärimudel
  - Koosta põhjalik uurimisraport Markdown-is
- **Tulem**: Probleemi täielik analüüs ja dokumentatsioon
- **Protsess**: Individual research → Branch → PR → Peer review → Merge

---

### **Seminar 3: planeerimine - projektijuhtimine ja meeskonnatöö**
**Kestus**: 3h  
**Fookus**: arendusprotsessi 2. etapp - projekti struktureerimine ja meeskonna organiseerimine

#### Arenduse etapp: project planning ja team organization
**Pärisarenduses**: Projekti juhid planeerivad tööd, moodustavad meeskonnad ja määravad rollid  
**Meie kursuses**: Tudengid õpivad planeerima projekte ja organiseerima meeskonnatööd

#### Teemad:
- **Rollid tarkvaraarenduses**: Product Owner, Scrum Master, Developer, QA, UX Designer
- **Projekti planeerimine**: Ajakavad, ressursid, riskid
- **Arendusmetoodikad võrdlus**:
  - **Waterfall**: Traditsioonilised sammud, dokumentatsioon
  - **Agile**: Iteratiivne, koostöö, paindlikkus
  - **Scrum**: Sprint-id, rollid, seremoniad
  - **Kanban**: Voog, WIP limitid, jätkuv parandamine
  - **Lean**: Raiskamise vähendamine, väärtuse optimeerimine
- **Meeskonnatöö ja kommunikatsioon**:
  - **Remote vs co-located teams**: Hajusmeeskonnatöö
  - **Communication frameworks**: Stand-ups, retrospectives, planning
  - **Conflict resolution**: Konstruktiivne tagasiside, konsensus
- **Git branching strategies**: Feature branches, merge strategies
- **Collaboration tools**: GitHub workflow, project management platforms

#### Praktilised harjutused:
- **Rollide jaotamine**: Iga tudeng valib rolli järgmisteks seminariteks
- **Projekti charter loomine**: Eesmärgid, skopp, ajakava
- **GitHub repository setup**: Organisational structure
- **GitHub organisatsiooni vaadete loomine**: Custom views, dashboards
- **Branching strategy** määramine ja praktiline harjutamine
- **Team communication workflow** GitHub Issues/Projects kaudu

#### Kodutöö 3:
- **Teema**: Projektijuhtimise plaan
- **Ülesanne**: 
  - Grupp koostab täieliku projektijuhtimise plaani eelmise kodutöö probleemile
  - Rollide jaotus, vastutused, ajakava, riskianalüüs
  - Sprint planning ja backlog struktuuri kavandamine
- **Rollid praktikas**: Product Owner, Scrum Master, Lead Developer, QA Lead
- **Tulem**: Projekti juhtimine dokument + töövoo kirjeldus
- **Protsess**: Role-based contributions → Feature branches → PR → Cross-role review

---

### **Seminar 4: disainimine - kasutajaliidese kavandamine ja prototüüpimine**
**Kestus**: 3h  
**Fookus**: arendusprotsessi 3. etapp - kasutajaliidese ja kasutajakogemuse disainimine

#### Arenduse etapp: UI/UX design ja prototyping
**Pärisarenduses**: UX/UI disainerid loovad wireframe-id, mockup-id ja prototüüpe  
**Meie kursuses**: Tudengid loovad paberprototüüpe ja planeerivad kasutajakogemust

#### Osa 1: kasutajakeskne disain ja design thinking (45 min)
- **Design Thinking metoodika**: Empaatia → Definitsioon → Ideation → Prototüüp → Test
- **Kasutajate mõistmine**: Persoonade loomine uurimistulemuste põhjal
- **Kasutajalugude kirjutamine**: "Kasutajana soovin..."
- **Stsenaariumide arendamine**: Samm-sammulised kasutaja teekond
- **Kasutaja teekond (customer journey)**: Täielik kogemuse kaardistamine
- **RK lehekülje kasutajalood**: Praktiline näide haridusportaalist
- **Funktsionaalsed vs mitte-funktsionaalsed nõuded**

#### Osa 2: paberprototüüpimine (90 min) ✅
- **Requirements → Wireframes**: Nõuetest ekraanide juurde
- **Paberprototüüpide loomine** gruppides (säilitatud edukas meetod!)
- **User flow mapping**: Kasutaja teekonna visualiseerimine
- **Prototüüpide testimine**: Rollimäng kasutajatega

#### Osa 3: dokumenteerimine (45 min)
- **Prototüüpide digitaliseerimine**: Foto + kirjeldused
- **Design specifications**: Komponendid, funktsioonid, reeglid
- **GitHub dokumenteerimine**: Design docs, user flows

#### Kodutöö 4:
- **Teema**: Täielik UI/UX disaini dokumentatsioon
- **Ülesanne**: 
  - **Persoonad**: 2-3 erinevat kasutajat uurimistulemuste põhjal
  - **Kasutajalood**: 5-7 põhifunktsiooni kirjeldus
  - **Paper prototypes**: Kõik olulised ekraanid + user flow
  - **Design specifications**: Komponendid, reeglid, stiilileht
- **Rollid**: UX Researcher, UI Designer, Usability Tester, Technical Writer
- **Protsess**: Role-based design → Prototype → Test → Document → PR

---

### **Seminar 5: arendamine - sprint-ide haldamine ja ülesannete jälgimine**
**Kestus**: 3h  
**Fookus**: arendusprotsessi 4. etapp - töö organiseerimine ja jälgimine arenduse ajal

#### Arenduse etapp: development sprint management
**Pärisarenduses**: Arendajad töötavad sprint-idena, PM-id jälgivad progressi, Scrum Master-id juhtivad protsesse  
**Meie kursuses**: Tudengid simuleerivad arenduse sprint-e GitHub Projects kaudu

#### Osa 1: sprint planning (60 min)
- **Design → Development**: Prototüüpidest arendusülesannete juurde
- **Epic-ute jagamine**: Suurtest eesmärkidest väikeste ülesannete juurde
- **Story points ja hinnangud**: Tööde komplekssuse hindamine
- **Sprint backlog**: Kellel, mis, millal valmis

#### Osa 2: GitHub Projects praktiline seadistamine (90 min)
- **Epic-ute loomine**: Design specifications → Development epics
- **Issue-te konvertimine**: Prototüübi komponendid → Arendusülesanded
- **Kanban board**: To Do → In Progress → Review → Done
- **Labels ja prioriteedid**: frontend, backend, testing, documentation
- **Milestone-d ja releases**: Sprint-ide planeerimine

#### Osa 3: sprint simulation (30 min)
- **Daily standup simulation**: Mis tegin, mis teen, mis takistab
- **Progressi jälgimine**: Burndown chart, velocity tracking
- **Blocker-ite käsitlemine**: Probleemide eskaleerimine

#### Kodutöö 5:
- **Teema**: Sprint-ide läbiviimine ja jälgimine
- **Ülesanne**: 
  - **2-nädalase sprint-i simuleerimine**: Prototüüpide alusel arendusülesannete loomine
  - **Iga päev**: GitHub Issues update, progressi dokumenteerimine
  - **Sprint review**: Mida saavutati, retrospektiiv
- **Rollid**: Product Owner (prioritiseerib), Scrum Master (jälgib protsessi), Developers (täidavad ülesandeid)
- **Protsess**: Daily updates → Weekly review → Sprint retrospective

---

### **Seminar 6: testimine ja release - kvaliteedi tagamine ja väljastamine**
**Kestus**: 3h  
**Fookus**: arendusprotsessi 5. etapp - testimine, kvaliteedi tagamine ja toote väljastamine

#### Arenduse etapp: quality assurance ja release management
**Pärisarenduses**: QA testijad testavad toodet, DevOps-id tegelevad väljastamisega, PM-id koostavad release note-sid  
**Meie kursuses**: Tudengid testavad prototüüpe, dokumenteerivad kvaliteeti ja valmistuvad "release-iks"

#### Osa 1: kvaliteedi testimine ja QA metoodikad (60 min)
- **Testimise liigid**: Unit, integration, system, user acceptance testing
- **QA protsessid**: Manuaalne vs automaatne testimine
- **Prototype testing**: Paberprototüüpide kasutajatestid
- **User acceptance testing**: Kas prototüüp vastab nõuetele?
- **Documentation review**: Kas dokumentatsioon on täielik ja arusaadav?
- **Cross-team review**: Teiste gruppide tööde hindamine
- **Bug reporting**: Probleemide dokumenteerimine GitHub Issues-is

#### Osa 2: release ettevalmistus ja DevOps alused (90 min)
- **Release management**: Versioonid, tagid, changelog
- **DevOps põhimõtted**: Continuous integration/deployment kontseptsioonid
- **Release notes kirjutamine**: Mis valmis? Mis muutus? Mis järgmine?
- **Final documentation**: README, user manuals, API docs
- **GitHub Pages seadistamine**: Projekti esitlus veebis (deployment näide)
- **Deployment checklist**: Mis peab olema valmis toote väljastamiseks?
- **Retrospective**: Mis läks hästi? Mis paremini? Mida õppisime?

#### Osa 3: "product launch" - esitlused (30 min)
- **Product demo**: Iga grupp esitab oma "toote" (3-5 min)
- **Process presentation**: Kuidas töötasime? Millised rollid? Kuidas koostööd tegime?
- **Lessons learned**: Mida õppisime arendusprotsessist?

#### Kodutöö 6:
- **Teema**: Final release ja portfolio
- **Ülesanne**: 
  - **Release package**: Täielik dokumenteeritud "toode" GitHub-is
  - **Portfolio README**: Kõigi kursuse projektide ülevaade
  - **Varasemate kodutööde seis**: Reflektsioon õppimisest ja progressist
  - **Kuidas on läinud VSCode ja GitHub tööriistadega?**: Tööriistade hindamine
  - **Individual reflection**: Isiklik õppimise reflektsioon (2-3 lk)
  - **Peer evaluation**: Tiimiliikmete töö hindamine
- **Tulem**: Professionaalne GitHub portfolio + projekt "release"
- **Protsess**: Final testing → Documentation → Release → Portfolio → Reflection

---

## Kodutööde üldstruktuur

### Igas kodutöös:
1. **Individual/grupi töö** vastavalt ülesandele
2. **Git workflow**: Fork/Branch → Commit → Push → PR
3. **Peer review**: Kaaslane vaatab üle ja kommenteerib
4. **Teacher review**: Õpetaja lõplik heakskiit
5. **Reflektsioon**: `protsess.md` fail iga kodutööga

### Hindamissüsteem:
- **50%** kodutööd (6 kodutööd)
- **50%** eksam (teooria + praktilised ülesanded)

### Kodutööde teemad (development lifecycle):
1. ✅ **Setup** - Git/GitHub tööriistad ja workflow
2. **Research** - probleemi analüüs ja kasutajate uurimine
3. **Planning** - projekti planeerimine ja meeskonna organiseerimine  
4. **Design** - UI/UX disain ja prototüüpimine
5. **Development** - sprint-ide simuleerimine ja jälgimine
6. **Release** - testimine, kvaliteedikontroll ja väljastamine

---

## Ressursid ja tööriistad

### Kohustuslikud tööriistad:
- **Git** (GUI kaudu VSCode-s või GitHub Desktop-is)
- **GitHub** (repositories, issues, projects, pages)
- **VSCode** (Markdown extensions, Git integration)
- **Markdown** (dokumentatsioon, README-d)

### Soovituslikud ressursid:
- Paaber ja pliiats (prototüüpimiseks)
- Telefon/kaamera (prototüüpide dokumenteerimiseks)
- Miro/Figma (digitaalseks koostööks)

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

## Muudatused eelmise versiooni suhtes

### Lisatud:
- ✅ 6 seminarit (oli 4)
- ✅ Süvenenud VSCode koolitus
- ✅ Tugevam fookus GitHub projektihaldusele
- ✅ Hands-on prototüüpimine (säilitatud!)
- ✅ Structured peer review process
- ✅ Portfolio loomise aspekt

### Muudetud:
- ✅ Vähem teoreetilist materjali, rohkem praktikat
- ✅ Iga seminar seotud GitHub workflow-ga
- ✅ Proggressiivne õpe (lihtsamalt keerukamale)
- ✅ Grupitöö ja individuaaltöö paremini tasakaalustatud

### Säilitatud edukas:
- ✅ Paberprototüüpimine (väga populaarne!)
- ✅ Pull request workflow
- ✅ Peer review kultuur
- ✅ Markdown-i kasutamine
- ✅ Praktilised, käegakatsutavad tulemused

---

---

## 🎯 KURSUSE PEAMINE VÄÄRTUS

### Täielik software development lifecycle kogemus
Tudengid läbivad **päris arendusprotsessi** ilma koodimiseta:

| **Arenduse etapp** | **Seminar** | **Praktilised oskused** | **Tööriist** |
|---|---|---|---|
| **Project kickoff** | Seminar 1 ✅ | Git/GitHub workflow, dokumenteerimine | VSCode + Git |
| **Research ja analysis** | Seminar 2 | kasutajate uurimine, probleemi analüüs | Markdown docs |
| **Project planning** | Seminar 3 | meeskond, rollid, ajakavad | GitHub Projects |
| **Design ja prototyping** | Seminar 4 | UI/UX, wireframes, prototypes | paaber + foto |
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
- 💡 **Vastus küsimusele**: "Kuidas saab ideest siis lõpuks tarkvara?" - täielik pildi

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
