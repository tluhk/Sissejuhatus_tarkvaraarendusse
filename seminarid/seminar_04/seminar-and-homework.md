# Seminar 4: Sprint 2 - Disainimine | Seminaritöö ja kodutöö näide

## Seminari struktuur
**Kestus**: 3h (30 min Sprint 1 ülevaade + 90 min teooria + 90 min praktikat)

### ALGUS: Sprint 1 Review ja Retrospective (30 min)

Enne Sprint 2 alustamist vaatame üle Sprint 1 tulemused ja õpime sprindi lõpetamise rituaale.

#### Sprint 1 Review (15 min) - "Mis me tegime?"

**Eesmärk**: Demonstreerida Sprint 1 tulemusi ja saada stakeholder'ite tagasiside

**"Kooli Köök" Sprint 1 Demo struktuur:**

```markdown
## SPRINT 1 DEMO AGENDA (15 minutit)

### 1. Sprint Goal meeldetuletus (2 min)
"Projekt on käivitamiseks valmis - meeskond organiseeritud, IoT integratsiooniplaan valmis ja broneerimissüsteemi tehniline keskkond loodud."

### 2. Saavutatud tulemused (8 min)
**Product Owner (Liisa) esitleb:**
- `project-charter.md` - projekti visioon ja eesmärgid
- `product-backlog.md` - 12 prioritiseeritud user story-t
- Konkurentsianalüüs - 3 sarnase rakenduse analüüs

**Project Manager (Marko) esitleb:**  
- `team-roles.md` - selged vastutusalad 4 liikmele
- `project-timeline.md` - 3 sprindi roadmap
- `communication-plan.md` - daily standup protokoll

**Developer (Jaan) esitleb:**
- `technical-architecture.md` - millega süsteem peab hakkama saama, mis osadest koosnema

**UX/UI Designer (Kristel) esitleb:**
- `design-strategy.md` - mobile-first lähenemine  
- Kasutajateekondade visandid - 3 peamist flow'd
- Esialgsed wireframe'i sketšid

### 3. Sprint mõõdikud (3 min)
- **Planeeritud**: 14 Story Points
- **Täidetud**: 15 Story Points (107% - väike overcommit)
- **Velocity**: 15 SP (baseline järgmisteks sprintideks)
- **Blockers**: 2 väikest (TLU IT-ga integreerimise küsimused)

### 4. Stakeholder tagasiside (2 min)
- "Kas projekt suund vastab teie ootustele?"
- "Millised küsimused/muudatusettepanekud?"
- "Sprint 2 prioriteetide kinnitamine"
```

**Praktilise harjutuse juhend:**
1. **Iga meeskond** (4 tudengit) korraldab oma Sprint 1 review'i
2. **Teised meeskonnad** on audience/stakeholder'id
3. **Aeg**: 5 min demonstreerimist + 2 min küsimusi meeskonna kohta
4. **Fookus**: näidatkee konkreetseid tulemusi, mitte plaane

#### Sprint 1 Retrospective (15 min) - "Kuidas me töötasime?"

**Eesmärk**: Analüüsida meeskonna koostööd ja leida parandamise võimalusi järgmise sprindi jaoks

**Retrospective meetod: "Start-Stop-Continue"**

```markdown
## SPRINT 1 RETROSPECTIVE - "Kooli Köök" meeskond

### 🟢 CONTINUE (Jätka tegema)
**Mis läks hästi ja peaks jääma?**
- ✅ Daily standupid GitHub Discussions-is töötasid hästi
- ✅ Rollide jaotus oli selge - igaüks teadis oma vastutust  
- ✅ Dokumenteerimine Markdown-is oli efektiivne
- ✅ Peer review GitHub-is tõi kvaliteeti juurde

### 🔴 STOP (Lõpeta tegemine)  
**Mis ei töötanud ja tuleks lõpetada?**
- ❌ Liiga pikad arutelud user story hindamisel (1h asemel 20min)
- ❌ Iga väikese muudatuse jaoks eraldi PR (liiga palju notificationseid)
- ❌ Üksikasjalik dokumenteerimine kõige jaoks (time waste)

### 🟡 START (Alusta tegema)
**Mida järgmises sprintis teisiti teha?**
- 🚀 Planning poker cards user story hindamiseks (kiirem konsensus)
- 🚀 Combination PR-id seotud ülesannete jaoks  
- 🚀 Definition of Done checklistid iga user story jaoks
- 🚀 Vähemalt 1 informal check-in nädalas (voice call)

### Action Items Sprint 2-ks
1. **Marko** - Planning poker digitaalne tööriist meeskonnale
2. **Kristel** - DoD template kõigi design task-ide jaoks
3. **Kõik** - Max 3 PR-i nädalas inimese kohta (batching)
4. **Liisa** - Stakeholder feedback schedule Sprint 2-ks
```

**Praktilise harjutuse juhend:**
1. **Aeg**: 10 min grupi retrospective + 5 min action items
2. **Reeglid**: 
   - Fookus protsessil, mitte isikutel
   - Konkreetsed näited, mitte üldised hinnangud
   - Iga punkt peab olema actionable
3. **Väljund**: Vähemalt 2 action item Sprint 2 parenduseks

---

## "Kooli Köök" projekti Sprint 2 käivitamine

**"Kooli Köök"** projekti Sprint 2 keskendub kasutajaliidese kavandamisele ja prototüüpimisele. Sprint 1-s lõime projekti struktuuri ja meeskonna, nüüd arendame välja konkreetse kasutajakogemuse.

### Sprint 2 eesmärk:
Sprint 1 tulemuste põhjal (projektiplaani, rollide jaotuse ja tehnilise arhitektuuri) luua täielik kasutajaliidese disain, mis lahendab mikrolaineahjude broneerimise ja toidu jagamise probleemid.

### Põhilised väljakutsed Sprint 2-s:
- **Kasutajakogemuse optimeerimine** - kuidas vähendada mikrolaineahju leidmise aega 10-15 minutilt alla 30 sekundi
- **Mobile-first lähenemine** - 95% kasutajatest kasutab telefoni
- **IoT integratsioon** - kuidas näidata reaalajas andmeid kasutajasõbralikult
- **Kogukonna funktsioonid** - toidu jagamise ja ühisostude disainimine

---

## OSA 1: TEOORIA (90 minutit)

### 1.1 Design thinking metoodika (25 min)

#### Design thinking ülevaade (10 min)
**Definitsioon**: inimesekeskne lähenemine innovatsioonile, mis integreerib inimeste vajadused, tehnoloogia võimalused ja äri nõudmised.

**5 etappi**:
1. **Empaatia (Empathize)**: kasutajate mõistmine
2. **Defineerimine (Define)**: probleemi selge formuleerimine  
3. **Ideation**: lahenduste genereerimine
4. **Prototüüpimine (Prototype)**: kiired, odavad testversioonid
5. **Testimine (Test)**: kasutajatega valideerimine

#### Double Diamond protsess (8 min)
```
    DISCOVER  |  DEFINE   |  DEVELOP  |  DELIVER
       /\     |    \/     |    /\     |    \/
      /  \    |   /  \    |   /  \    |   /  \
Divergent -> Convergent -> Divergent -> Convergent
```

**Esimene teemant**: õige probleemi leidmine
- **Discover**: lai uurimine, mitmete võimaluste kaardistamine
- **Define**: fookuse leidmine, konkreetse probleemi valimine

**Teine teemant**: õige lahenduse leidmine  
- **Develop**: mitmete lahenduste genereerimine ja katsetamine
- **Deliver**: parima lahenduse vajemine ja ellurakendamine

#### Human-Centered Design põhimõtted (7 min)
- **Inimesed esimeses kohas**: tehnoloogia teenib inimesi, mitte vastupidi
- **Konteksti mõistmine**: kus, millal ja kuidas inimesed toodet kasutavad
- **Iteratiivne protsess**: jätkuv tagasiside ja parandamine
- **Multidistsiplinaarne koostöö**: erinevad vaatenurgad ja oskused
- **Empaatia**: kasutajate emotsioonide ja motivatsiooni mõistmine

### 1.2 Persoonade loomine (20 min)

#### Mis on persoona? (5 min)
**Definitsioon**: persoona on fiktiivsne karakter, mis esindab reaalset kasutajagruppi ja on loodud kasutajauuringute tulemuste põhjal.

**Persoona eesmärk**:
- aitab meeskonnal keskenduda konkreetse kasutaja vajadustele
- teeb otsuste tegemise lihtsamaks ("Kas Mari kasutaks seda funktsiooni?")
- loob ühise arusaama kasutajatest
- aitab vältida iseenda projekteerimist

#### Persoona elemendid (10 min)
**Põhiinfo**:
- nimi ja pilt (aitab meeldejätta)
- vanus, elukutse, haridus
- tehnika kogemus ja oskused

**Kontekst ja keskkond**:
- kus ja millal toodet kasutab
- millised seadmed ja tehnoloogiad
- ajaline koormus ja stress

**Eesmärgid ja motivatsioon**:
- miks tahab toodet kasutada
- millised on tema peamised eesmärgid
- mis teda motiveerib või demotiveerib

**Frustatsioonid ja takistused**:
- mis teda praegu segab
- millised on tema peamised väljakutsed
- milliseid vigu ei tohi teha

**Käitumismustrid**:
- kuidas tavaliselt uusi tööriistasid omaks võtab
- kui palju aega investeerib õppimisse
- kas eelistab kiireid lahendusi või põhjalikku uurimist

#### Persona näide (5 min)
```
MARI METS, 20, rakendusinformaatika tudeng

"Ma soovin rohkem aega huvialadele, mitte kodutööde tähtaegade jälgimisele."

KONTEKST:
- Õpib täistööajaga, töötab õhtuti
- Kasutab peamiselt telefoni ja sülearvutit
- Liigub palju TLU kampuste vahel

EESMÄRGID:
- Kiire ülevaade kõigist tähtaegadest
- Automaatsed meeldetuletused
- Ühilduvus olemasolevate kalendritega

FRUSTATSIOONID:
- Info on hajutatud (Moodle, email, Discord)
- Ei saa kiirelt ülevaadet prioriteetidest
- Unustab tähtaegu stress-perioodidel

KÄITUMINE:
- Kontrollib telefoni iga 30 min
- Eelistab visuaalseid ülevaateid
- Vajab kiiret seadistamist (max 5 min)
```

### 1.3 Kasutajalugude kirjutamine (20 min)

#### User story formaat (8 min)
**Põhiformaat**:
```
"[kasutaja tüübina] soovin ma [eesmärk/funktsioon], et [kasutaja väärtus/põhjus]."
```

**Näited**:
- "Tudengina soovin ma näha kõiki oma kodutöid ühes kalendris, et ma ei unustaks ühtegi tähtaega."
- "Õppejõuna soovin ma saada ülevaadet tudengite progressist, et ma saaksin õigeaegselt abi pakkuda."

#### INVEST kriteeriumid (7 min)
Hea user story peab olema:

**I - Independent**: sõltumatu teistest user storydest  
**N - Negotiable**: läbiräägitav, mitte fikseeritud spetsifikatsioon  
**V - Valuable**: väärtuslik kasutaja või äri jaoks  
**E - Estimable**: hinnatav - saab anda tööle mahuhinnagu  
**S - Small**: piisavalt väike, et mahuks ühte sprint-i  
**T - Testable**: testitav - saab kontrollida, kas on valmis  

#### Aksepteerimiskriteeriumid (5 min)
**Definitsioon**: tingimused, mis peavad olema täidetud, et user story oleks "valmis".

**Näide**:
```
USER STORY: Tudengina soovin näha kõiki tähtaegu kalendrivaates.

Aksepteerimiskriteeriumid:
✅ Kasutaja näeb kõiki kodutöid kronoloogilises järjekorras
✅ Iga ülesande juures on näha tähtaeg ja õppeaine
✅ Võib filtreerida õppeainete kaupa
✅ Näitab ainult aktiivseid (mitte aegunud) ülesandeid
✅ Uuendub automaatselt Moodle-st andmete sünkroonimmisel
```

### 1.4 Kasutajateekond ja stsenaariumid (15 min)

#### Customer Journey Map (8 min)
**Definitsioon**: visuaalne esitlus kasutaja kogemusest toote või teenusega.

**Elemendid**:
- **Puutepunktid (Touchpoints)**: kus kasutaja tootega kohtub
- **Tegevused (Actions)**: mida kasutaja teeb
- **Mõtted (Thoughts)**: mis kasutaja mõtleb
- **Emotsioonid (Emotions)**: kuidas kasutaja tunneb
- **Võimalused (Opportunities)**: kus saab parendada

**Näide lühikesest kasutajateekonnast**:
```
ETAPP 1: tekib probleem
- Tegevus: meenutab, et täna on tähtaeg
- Mõtted: "Millal see oli? Kas mul on aega?"
- Emotsioon: 😰 stress
- Võimalus: varajane meeldetuletus

ETAPP 2: otsib infot
- Tegevus: kontrollib Moodle-t, emaile
- Mõtted: "kus see info oli?"
- Emotsioon: 😤 frustratsioon
- Võimalus: keskne info koht

ETAPP 3: leiab info
- Tegevus: leiab ülesande ja tähtaja
- Mõtted: "Õnneks veel aega"
- Emotsioon: 😌 kergendus
- Võimalus: p arem visualiseerimine
```

#### Stsenaariumide kirjutamine (7 min)
**Definitsioon**: detailne kirjeldus sellest, kuidas kasutaja konkreetses olukorras tootega suhtleb.

**Stsenaariumi elemendid**:
- **Kontekst**: kus ja millal
- **Kasutaja**: kes (viide persoonale)
- **Eesmärk**: mida tahab saavutada
- **Sammud**: mida täpselt teeb
- **Tulemus**: mida saavutab või mitte

**Näide stsenaariumist**:
```
STSENAARIUM: tähtaja kontrollimine hommikul

KONTEKST: Mari istub Tallinn Haapsalu bussi
KASUTAJA: Mari Mets (20a, rakendusinformaatika tudeng)
EESMÄRK: kiire ülevaade päeva kohustustest

SAMMUD:
1. Avab telefonis tähtaegade rakenduse
2. Vaatab päevase vaate
3. Näeb 2 kodutööd: üks täna, teine homme
4. Kontrollib detaile - tänane on juba valmis
5. Lisab homsele ülesandele meeldetuletuse õhtuks

TULEMUS: ✅ Teab päeva plaani, saab keskenduda muule
ALTERNATIIV: ❌ Kui info puudub → stress ja ajaraiskamine
```

### 1.5 Funktsionaalsed vs mitte-funktsionaalsed nõuded (10 min)

#### Funktsionaalsed nõuded (5 min)
**Definitsioon**: Mida süsteem TEEB - konkreetsed funktsioonid ja käitumised.

**Näited**:
- Kasutaja saab sisse logida kasutajanimega ja parooliga
- Süsteem saadab automaatse meeldetuletuse 24h enne tähtaega
- Administraator saab lisada uusi kasutajaid süsteemi
- Kasutaja saab filtreerida ülesandeid õppeaine järgi

#### Mittefunktsionaalsed nõuded (5 min)
**Definitsioon**: KUIDAS süsteem käitub - kvaliteedi ja jõudluse nõuded.

**Kategooriad ja näited**:

**Jõudlus**:
- leht laadib 3 sekundi jooksul
- toetab kuni 1000 samaegset kasutajat

**Kasutatavus**:
- uus kasutaja õpib põhifunktsioonid 5 minutiga
- töötab iOS Safari ja Android Chrome brauserites

**Turvalisus**:
- parool peab olema vähemalt 8 märki
- andmed krüpteeritakse ülekandmisel

**Skaleeruvus**:
- süsteem peab toetama 10x kasutajate kasvu
- võimalik lisada uusi õppeasutusi

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 minutit)

### 2.1 Sprint 2 Planning - "Kooli Köök" GitHub Projects (20 min)

**Sprint Goal**: "Kasutajad saavad kiiresti leida vaba mikrolaineahju ja jagada toitu - täielik kasutajaliides ja prototüübid on loodud ja testitud."

#### GitHub Projects Sprint 2 seadistamine

**Custom Fields uuendamine Sprint 2-ks:**
- **Story Points**: 1, 2, 3, 5, 8, 13 (sama süsteem jätkub)
- **Priority**: Critical (MVP funktsioonid), High (important UX), Medium (nice UX), Low (future features)
- **Component**: Design (kasutajaliides), Research (kasutajauuringud), Validation (testimine), Documentation (kirjeldused)
- **Sprint**: Sprint 1, Sprint 2, Sprint 3
- **Assignee**: Liisa, Marko, Jaan, Kristel

**Sprint 2 Board View:**
```
To Do | In Progress | Review | Done
Filter: Sprint = "Sprint 2" AND Component = "Design"
Nähtavad ülesanded: Persoonade loomine, UI prototüübid, kasutajatestimise plaan
```

#### Sprint 2 Capacity Planning
Eelnevalt Sprint 1 velocity põhjal (15 SP → 18 SP kasv):
- **Liisa (Product Owner)**: 4 SP (kasvas - rohkem uurimistööd ja valideerimist)
- **Marko (Project Manager)**: 3 SP (vähenes - koordineerimine, kvaliteedi tagamine)  
- **Jaan (Developer)**: 5 SP (kasvas - tehnilise teostatavuse analüüsid)
- **Kristel (UX/UI Designer)**: 6 SP (kõige rohkem - disaini spetsialist Sprint 2-s)
- **Kokku Sprint 2**: 18 SP (tiimi arenev koostöö)

#### Sprint 2 GitHub Issues struktuur

**EPIC #1: Kasutajakogemuse disainimine** 

Issues Sprint 2 backlog-is (Sprint 1 Epic breakdown põhjal):

**Sprint 2 prioritiseeritud GitHub Issues:**

**Design Epic Issues (12 SP):**

**Issue #8**: 🎭 **Loo 3 detailset persoonat uurimistulemuste põhjal** (3 SP)
- **Assignee**: Kristel (UX/UI Designer) + Liisa (Product Owner) review
- **Labels**: `enhancement`, `design`, `research`, `sprint-2`
- **Component**: Design + Research
- **Priority**: Critical
- **Definition of Done**: 
  ```
  ✅ 3 persoonat loodud Sprint 1 uurimistulemuste põhjal
  ✅ Iga persoona sisaldab: taustainfo, kontekst, eesmärgid, frustatsioonid, käitumine
  ✅ Persoonad on konkreetsed (numbrid, brändid, käitumismustrid)
  ✅ Seotud kasutajateekondadega
  ✅ Liisa (PO) on review'nud ärilisest vaatepunktist
  ✅ Dokumenteeritud personas.md failis
  ```

**Issue #9**: **Disaini mikrolaineahjude broneerimise kasutajaliides** (5 SP)
- **Assignee**: Kristel (UX/UI Designer)
- **Labels**: `enhancement`, `design`, `ui`, `sprint-2`
- **Component**: Design
- **Priority**: Critical
- **Definition of Done**:
  ```
  ✅ Paberprototüüp 4+ ekraani: dashboard, broneering, kinnitamine, olek
  ✅ Digitaalne wireframe Figma/Sketch-is (valikuline)
  ✅ Mobile-first lähenemine (75%+ kasutajatest telefonis)
  ✅ Selge navigatsioon ekraanide vahel (nooled, clickable elemendid)
  ✅ Kasutajatestitud vähemalt 2 kasutajaga
  ✅ Dokumenteeritud paper-prototypes.md failis pilditega
  ```

**Issue #10**: **Loo toidu jagamise ja ühisostude interface** (3 SP)
- **Assignee**: Kristel + Liisa koostöö
- **Labels**: `enhancement`, `design`, `community`, `sprint-2`
- **Component**: Design
- **Priority**: High
- **Definition of Done**:
  ```
  ✅ Toidu pakkumise vorm (pilt + kirjeldus + asukoht)
  ✅ Ühisostude loomise interface
  ✅ Kogukonna aktiivsuse dashboard
  ✅ Social features: like, comment, share
  ✅ Wireframe-id 3+ ekraani kohta
  ✅ Liisa (PO) kinnitanud ärilise väärtuse
  ```

**Issue #11**: **Loo Design System dokumentatsioon** (1 SP)
- **Assignee**: Kristel (UX/UI Designer)
- **Labels**: `documentation`, `design`, `sprint-2`
- **Component**: Design + Documentation
- **Priority**: Medium
- **Definition of Done**:
  ```
  ✅ Värviskeem (primary, secondary, warning, neutral)
  ✅ Typography guidelines (sizes, weights)
  ✅ Button styles ja states
  ✅ Mobile-first responsive breakpoints
  ✅ Component library (cards, forms, navigation)
  ✅ Dokumenteeritud design-system.md failis
  ```

**Research ja Validation Epic Issues (6 SP):**

**Issue #12**: **Loo kasutajatestimise plaan ja protokoll** (2 SP)
- **Assignee**: Kristel + Liisa koostöö
- **Labels**: `research`, `testing`, `validation`, `sprint-2`
- **Component**: Research + Validation
- **Priority**: High
- **Definition of Done**:
  ```
  ✅ Testimise meetod (think-aloud + task-based testing)
  ✅ 3 test-ülesannet põhifunktsionaalsuse kohta
  ✅ Testiliste kasutajate kriteeriumid (3 tudengit + 1 töötaja)
  ✅ Edu kriteeriumid (completion rate >85%, task time <60s)
  ✅ Post-test interview küsimused
  ✅ Dokumenteeritud usability-testing-plan.md failis
  ```

**Issue #13**: **Täienda konkurentsianalüüsi broneerimisrakendustega** (2 SP)
- **Assignee**: Liisa (Product Owner)
- **Labels**: `research`, `competitive-analysis`, `sprint-2`
- **Component**: Research
- **Priority**: High
- **Definition of Done**:
  ```
  ✅ 5 broneerimisrakenduse detailne analüüs
  ✅ Võrdlustabel funktsioonide ja UX võrdlusega
  ✅ Pricing model'ite võrdlus
  ✅ Best practices ja kasutatavuse õppetunnid
  ✅ Eristumise võimalused "Kooli Köök" jaoks
  ✅ Lisatud business-requirements.md faili
  ```

**Issue #14**: **Analüüsi Sprint 2 disaini tehnilise teostatavuse** (2 SP)
- **Assignee**: Jaan (Developer)
- **Labels**: `research`, `technical`, `feasibility`, `sprint-2`
- **Component**: Research + Documentation
- **Priority**: Medium
- **Definition of Done**:
  ```
  ✅ UI komponendite tehnilise keerukuse hinnang
  ✅ Mobile-responsive lahenduste analüüs
  ✅ Real-time andmete kuvamise tehnoloogilised valikud
  ✅ Integration punktid TLU süsteemidega
  ✅ Performance requirements UI/UX jaoks
  ✅ Dokumenteeritud technical-requirements.md failis
  ```

#### Sprint 2 Task-ide jaotus

**Sprint 2 fookus: Kasutajaliidese kavandamine ja valideerimine**

Sprint 1 Epic breakdown-ist tulevad Sprint 2-sse:
- ✅ **Reaalajas kaardi komponendi disain** → Issue #9 osa
- ✅ **Mobile-responsive ahju vaate wireframe** → Issue #9 osa  
- ✅ **Broneerimise UI komponendi prototüüp** → Issue #9 osa
- ✅ **Toidu pakkumise vormi disain** → Issue #10 osa
- ✅ **Ühiostu interface mockup** → Issue #10 osa
- ✅ **Kogukonna dashboard wireframe** → Issue #10 osa

Sprint 2 spetsiifilised disaini ülesanded:
- ✅ **3 detailset persoonat** → Issue #8
- ✅ **Kasutajateekondade kaardistamine** → Issue #8 osa
- ✅ **Paberprototüüpide testimine** → Issue #12

**GitHub Projects Sprint 2 Milestones:**

**Milestone: Sprint 2 Review (1 nädal)**
- Kõik 6 Issue-t Done status-es
- Demo valmis: persoonad + prototüübid + testitulemused
- Sprint 2 dokumentatsioon repository-s

**Sprint 2 Daily Standups:**
- GitHub Discussions kasutamine
- Template ülesanded: mis tegin eile, teen täna, mis takistab
- Issues'ide uuendamine progress-iga

### 2.2 Persoonade loomine uurimistulemuste põhjal (20 min)

#### Uurimisandmete analüüs Sprint 1-st
Sprint 1 uuringud näitasid kolme peamist kasutajagruppi:

**Tulemused kasutajauuringutest:**
- 78% vastanutest kulutab mikrolaineahju otsimisele 10+ minutit päevas
- 65% unustab toitu jaheda või külma söömisega
- 45% oleks valmis jagama ülejäänud toitu teistega
- 23% on huvitatud ühisostudest

#### Persoonade loomine rollijaotusega

**UX Designer (Kristel) - Peamine kasutaja:**
```markdown
# MARI METS, 20, rakendusinformaatika tudeng

"Ma tahan kiiresti soojendada oma lõunat ja jätkata õppimist, mitte seista järjekordades."

## Taustainfo
- 2. kursuse tudeng, elub ülikooli lähedal
- Kasutab telefoni 95% ajast (iPhone 12)
- Toob kodust kaasa lõunat 4 päeva nädalas
- Tunniplaan tihe, vahetunnid 15-20 minutit

## Kontekst
- Kasutab mikrolaineahju 1-2 korda päevas
- Kiireloomuline - eelistab efektiivsust
- Liigub TLU kampuste vahel (Ülemiste ↔ Noblessner)
- Peak hours: 12:00-13:00 ja 16:00-17:00

## Eesmärgid
- Leida vaba mikrolaineahi alla 30 sekundi
- Broneerida ette, et mitte ootama jääda  
- Näha, millal ahi vabaneb (kui kõik broneeritud)
- Lihtne, kiire kasutamine ilma õppeta

## Frustatsioonid
- Pikad järjekorrad lõunapausil
- Ei tea, kus lähim vaba ahi asub
- Info puudub - peab käima ringi ja otsima
- Aeg läheb õppimise asemel ahju otsimisele

## Käitumine
- Kontrollib telefoni iga 30 min
- Ei loe pikki juhendeid - peab olema intuitiivne
- Jagab kogemusi sõpradega (social proof)
- Eelistab visuaalset infot tekstile
```

### 2.3 Kasutajalugude brainstorming - Sprint 2 spetsiifilised (25 min)

#### Epic Breakdown Sprint 2-ks

**EPIC: Kasutajaliidese disainimine**

Sprint 2 user story-d prioriteedijärjekorras:

**Must Have (8 SP):**

1. **Kasutaja näeb reaalajas kõigi mikrolaineahjude olekut** (3 SP)
```markdown
USER STORY: 
Kui tudeng, siis soovin näha ühel vaatel kõigi kooli mikrolaineahjude praegust olekut 
(vaba/broneeritud/kasutusel), et ma ei peaks käima ringi ja otsima.

ACCEPTANCE CRITERIA:
✅ Näitab kõiki 12 mikrolaineahju ühel kaardil/nimekirjas
✅ Olek uuendatakse iga 30 sekundi järel automaatselt
✅ Selge visuaalne eristus: roheline (vaba), kollane (varsti vabaneb), punane (kasutusel)
✅ Näitab asukoht (Ülemiste/Noblessner/aadress)
✅ Töötab nii telefonil kui arvutil
```

2. **Kasutaja saab broneerida vaba mikrolaineahju** (5 SP)
```markdown
USER STORY:
Kui tudeng, siis soovin broneerida vaba mikrolaineahju kuni 15 minutiks,
et ma ei peaks kartma järjekorras ootamist.

ACCEPTANCE CRITERIA:
✅ Broneering kestab max 15 minutit
✅ Automaatne tühistamine, kui ei kasuta 5 min jooksul
✅ Saab broneerida kuni 2 tundi ette
✅ Push teavitus: "Teie broneering algab 5 min pärast"
✅ Võib tühistada broneeringu enne kasutamist
```

### 2.4 Paberprototüüpide loomine (25 min)

#### Prototüüpimise põhimõtted
**Aeg**: 5 minutit  
**Põhimõtted**:
- **Kiirus > Täpsus**: ei pea ilus olema, peab olema arusaadav
- **Fokus funktsioonidele**: vorm tuleb hiljem
- **Iteratiivne**: tee kiiresti, testi, paranda
- **Kaasahaarav**: kõik saavad kaasa rääkida

#### Lo-fi wireframe-ide loomine
**Aeg**: 20 minutit  
**Ülesanne**: Igaüks joonistab 3-5 ekraani:

**Ekraanide jaotus rollidega**:
- **UX Designer**: peamised user flow'd
- **Product Owner**: dashboard ja overview ekraanid
- **Developer**: seadistused ja admin vaated
- **QA Lead**: Error state'd ja edge case'd

**Joonistamise reeglid**:
- kasuta lihtsa pliiatsit ja paberit
- tee suured kastid komponentidele
- kirjuta tekstid väikeses kirjas
- märgi clickable elemendid selgelt
- näita navigatsiooni

---

## Kodutöö 4: Sprint 2 disaini dokumentatsioon

**Kodutöö = Sprint 2 Issues täitmine**

1. **Loo sprindi plaan** – mida te teete, kes mille eest vastutab jne
2. **Loo vajalikud failid**
3. **Loo wireframed**
4. **Loo GitHub Issues projekti**
5. **Määra Labels, Assignee, Components**
6. **Töö In Progress** → **Review (omavaheline ülevaateus)** → **Done**
7. **Sprint review ja Retrospective** võtke seekordne sprint kokku. Lisage igaüks enda poolt kommentaar, mida õppisid, mis oleks võinud olla teisit, mis on endiselt segane või muud kommenteerimits vajavad jutud.

---

### Issued täitmiseks

**Issue #X**: Loo 2-3 detailsat persoonat.
**Issue #X**: Loo persoonade baasil kasutajateekonnad või stsenaarium või storyboard, mis vastavad ülesannetele, mida kasutaja peaks/saaks rakenduses sooritada.
**Issue #X**: Loo rakenduse kuvad (wireframed), mida saaksid järgmisel korral kasutajate peal testida. Kuvade arv vali, et saaksid anda testimiseks vähemalt kaks ülesannet.

---

### Repositooriumi struktuur selle ülesande raames

```
sprint2/
├── sprint_plan.md
├── personas.md
├── scenario-journey-storyboard.md
├── images/wireframes dokumenteerimise huvides
├── daily-standups.md (juhul kui teete)
├── sprint-2-review.md
├── sprint-2-retrospective.md
└── README.md (üldised selgitused selle kodutöö sisu kohta, kus mis ja miks on)
```

> [!NOTE]
> Õppematerjalid leiad [siit](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse)



> [!IMPORTANT]
> **Selle ülesande lahendus lisa selle Issue kommentaari**
> Lisa oma lahendus otse selle issue kommentaariks
> või kui Sul on failid, lisa need oma repository-sse ja viita neile kommentaaris
> Kui ülesanne on valmis, siis lisa issue-le "submission" silt
> Issuele lisa Assignee-ks õpetaja

---

## Järgmine seminar

**Seminar 5: Sprint 3 - Arendamine** - kuidas Sprint 2 disainidokumendid muuta detailseteks arendusülesanneteks ning simuleerida "arendusprotsessi" läbi projekt-koordineerimise.

**Sprint 3 eelvaade**:
- Epic-ute jagamine detailseteks task-ideks  
- Advanced GitHub Projects automation
- Velocity tracking ja burndown charts
- Sprint retrospective methodology
- Quality assurance ja bug reporting