# Kodutöö 5: Sprint 3 - arendamine (simuleerimine)

**Kodutöö = Sprint 3 Issues täitmine**

## Ülevaade

Sprint 3 on arenduse simulatsioon - te EI kirjuta koodi, vaid dokumenteerite ja simuleerite arendusprotsessi. Eesmärk on mõista, kuidas päris arendusmeeskond töötab.

---

## Kohustuslikud ülesanded

### 1. Loo Sprint 3 plaan
**Fail:** `sprint-3-plan.md`

**Sisu:**
- Sprint Goal (1 lause - mida tahate saavutada? Näiteks: "Broneerimise funktsionaalsus on tehniliselt kirjeldatud ja testitud")
- Selected EPIC (milline peamine funktsioon/EPIC Sprint 3-sse võtate? Näiteks: "Mikrolaineahju broneerimine")
- Team members (kes milliseid rolle täidab? Developer, Tester, jne)
- Definition of Done (millal on Sprint valmis? Näiteks: "Kõik pseudokoodid kirjutatud, testid dokumenteeritud, API kirjeldatud")

---

### 2. Ülesannete jaotus
**Fail:** `task-breakdown.md`

**Ülesanne:**
- Vali 1 peamine funktsioon teie projektist (see on teie **EPIC** Scrum terminoloogias)
- Kirjelda, mida see funktsioon teeb (1-2 lauset)
- Jaga 5-10 ülesandeks (need on **TASK'id**)
- Iga ülesanne peab sisaldama:
  - Ülesande kirjeldus (mida tehakse?)
  - Tüüp (Programmeerimine/Testimine/Dokumentatsioon)
  - Vastutaja (kes teeb?)
  - Staatus (Tehtud/Pooleli/Ei alanud)

**EPIC vs Funktsioon:**
Teie valitud "peamine funktsioon" on tegelikult **EPIC** Scrum terminoloogias. Näiteks "Mikrolaineahju broneerimine" on EPIC. Selles ülesandes keskendute ühele EPICule ja jagate selle konkreetseteks ülesanneteks (TASK'ideks). Valikuliselt võite jagada EPICu ka USER STORY'deks enne TASK'ide loomist, kui see aitab struktuuril.

**Märkus:** Sprint 3 keskendub arendusele, seega ülesanded on programmeerimise, testimise ja dokumenteerimisega seotud. Disaini ülesanded olid Sprint 2 osa.

**Näide:**
```markdown
# Funktsioon: Mikrolaineahju broneerimine

## Mida see funktsioon teeb?
Kasutaja saab broneerida vaba mikrolaineahju kuni 15 minutiks.

## Ülesanded:
1. **Kirjuta pseudokood broneerimise loogikale** (Programmeerimine) - @jaan
2. **Kirjuta pseudokood aja kontrollimisele** (Programmeerimine) - @jaan
3. **Testi broneerimist erinevate stsenaariumidega** (Testimine) - @liis
4. **Dokumenteeri API endpoint'id** (Dokumentatsioon) - @mari
5. **Kirjuta kasutajajuhend broneerimisele** (Dokumentatsioon) - @liis
...


---
```

### 3. Kanban
**GitHub Projects:** Ülesandeid haldame visuaalselt board'il (To Do / In Progress / Done)

### 4. Daily Standups ja progress
**Fail:** `daily-standups.md`  

**Ülesanne:**
- Kirjutage standup kirjeid 2 nädala jooksul (ei pea olema iga päev)
- Iga standup korral KÕIK meeskonnaliikmed kirjutavad:
  - Mida "eile" tegid (kuna iga päev ei kirjuta, siis "eelmine kord")
  - Mida "täna" teevad
  - Mis "takistab" (blockerid, probleemid)
- Lisage iga standup lõppu progress kokkuvõte (mitu ülesannet tehtud/pooleli/alustamata)
- Haldage ülesandeid GitHub Projects board'il ja lisage link board'ile standup kirjetesse

**Oluline:** Teil on kaks võimalust:
1. **Simuleeritud variant:** Kirjutate kõik 6-8 standup kirjet korraga lõpus, kujutades ette mis oleks tegelikult juhtunud (nö simulatsioon)
2. **Reaalajas variant:** Kirjutate standup kirjeid kahe nädala jooksul 3-5 korda nädalas vastavalt sellele, kuidas tegelikult tegutsete

Mõlemal juhul peab kokku olema vähemalt 6-8 standup kirjet, et mõista meeskonna kommunikatsiooni ja progressi jälgimist.

**Template iga standup kohta:**
```markdown
## Standup [Kuupäev] - Päev X

### Jaan (Developer)
**Eile:** Kirjeldasin tehnilise arhitektuuri
**Täna:** Dokumenteerin API endpoint'e
**Takistab:** Ei ole veel otsustanud andmebaasi struktuuri

### Mari (Developer)
**Eile:** Kirjutasin pseudokoodi broneerimise loogikale
**Täna:** Alustan aja kontrollimise algoritmi kirjutamist
**Takistab:** Ei ole kindel, kuidas kattuvaid broneeringuid kontrollida

### Progress kokkuvõte
- Tehtud: 2 ülesannet
- Pooleli: 3 ülesannet
- Alustamata: 5 ülesannet
- GitHub Projects: [link board'ile]

### Märkused
- Blocker lahendatud: Jaan sai abi andmebaasi struktuuri küsimuses
- Uuendasime GitHub board'i
```

---

### 4. Tehnilised otsused
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

### 5. Sprint 3 Review
**Fail:** `sprint-3-review.md`

**Sisu:**
- Mis "valmis sai" (simulatsiooni tulemus)
- Kas Sprint Goal saavutati?
- Mis läks plaanist erinevalt?
- Stakeholder'ite tagasiside (teiste meeskondade kommentaarid)

---

### 6. Sprint 3 Retrospective
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

### Jaan (Developer)
Õppisin kuidas suurtest ülesannetest väikseid task'e teha. Pseudokoodi kirjutamine oli alguses raske, aga näidete abil sain paremini aru. Sprint simulation aitas mõista, miks on vaja järjepidevat kommunikatsiooni ja miks blockerid tuleb kiiresti lahendada.

### Mari (Developer)
...
```

---

## Rolli-põhised ülesannete näited

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