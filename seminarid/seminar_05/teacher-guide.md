# Seminar 5: Sprint 3 - Arendamine (Simuleerimine) | Õpetaja juhend

## Seminari ülevaade

**Kestus**: 3 tundi (30 min + 90 min + 90 min)
**Osavõtjaid**: ~20 tudengit, 4-5 meeskonda
**Fookus**: Arendusprotsessi simuleerimine, epic breakdown, sprint jälgimine
**Oluline**: Tudengid EI KOODI - nad simuleerivad arendust dokumentatsiooni ja planeerimise kaudu

## Kritiline mõte: Arendamine ilma koodita

See seminar õpetab, **mida arendajad teevad** ilma et tudengid peaksid programmeerima:
- Kuidas ülesandeid jagatakse ja koordineeritakse
- Kuidas jälgitakse progressi ja eemaldatakse takistusi
- Kuidas tehakse tehnilisi otsuseid
- Kuidas toimib meeskonnatöö arenduse ajal

Tudengid töötavad oma projektidega (nt "FindFood", "Kooli Köök"), kasutades Sprint 2 wireframe'e ja personaid.

---

## Eeltööd (õpetaja ettevalmistus)

### Vajalikud materjalid
- [ ] Post-it märkmed (3 värvi - burndown chart simulatsiooniks)
- [ ] A4 paberid (task breakdown workshopiks)
- [ ] Pliiatsid/markerid
- [ ] Timer/stopper (sprint simulation jaoks)

### Tehnilised ettevalmistused
- [ ] Projektor slides.md jaoks
- [ ] Kontrolli, et kõik meeskonnad esitasid Sprint 2 kodutöö
- [ ] Vaata läbi Sprint 2 tulemused (personas, wireframes)
- [ ] Valmista ette näidis GitHub Projects board Sprint 3 jaoks

### Sprint 2 kontrolltellimus
- [ ] Kas kõik meeskonnad said wireframe'id valmis?
- [ ] Kas personas on loodud?
- [ ] Kas user journey'd on dokumenteeritud?

---

## OSA 1: Sprint 2 Review ja Retrospective (30 min)

### 1.1 Sprint 2 Review (15 min)

**Eesmärk**: Vaadata üle Sprint 2 disaini tulemused enne arenduse alustamist

**Õpetaja ülesanded:**

1. **Demo struktuuri meeldetuletus** (2 min)
   ```
   Selgita: "Täna vaatame, mida te Sprint 2-s disainisite. Seejärel hakkame seda 'arendama'."
   Rõhuta: Disain on arenduse plaan - ilma selleta ei saa arendada
   ```

2. **Meeskondade demo'd** (10 min - 2 min/meeskond)
   ```
   Iga meeskond näitab:
   - Sprint 2 wireframe'id (pildid)
   - Personas (kes on kasutajad?)
   - User journey (kuidas kasutajad rakendust kasutavad?)
   - Sprint 2 velocity (mitu SP täitsid?)

   Teised meeskonnad = stakeholderid, küsivad:
   - "Kas see on arusaadav kasutajale?"
   - "Kuidas see tehniliselt töötab?"
   ```

3. **Õpetaja küsimused igale meeskonnale** (3 min)
   ```
   - "Mis oli kõige raskem Sprint 2-s?"
   - "Mida muudaksite oma disainis?"
   - "Kas olete valmis seda 'arendama'?"
   ```

**Õpetaja märkmed:**
- Jälgi, kas wireframe'id on piisavalt detailsed arenduse simuleerimiseks
- Kui meeskond ei ole valmis - anna kiireid soovitusi
- Märgi üles head lahendused, mida teistele näidata

### 1.2 Sprint 2 Retrospective (15 min)

**Eesmärk**: Analüüsida Sprint 2 protsessi ja valmistuda Sprint 3-ks

**Õpetaja ülesanded:**

1. **Start-Stop-Continue meetodi meeldetuletus** (2 min)
   ```
   Sama meetod kui Sprint 1 järel:
   CONTINUE - mis toimis hästi?
   STOP - mida lõpetada?
   START - mida proovida?
   ```

2. **Meeskondade retrospective** (10 min)
   ```
   Iga meeskond eraldi (võivad kasutada GitHub Discussions):
   - 5 min: kirjutavad post-it märkmetel (või digitaalselt)
   - 5 min: arutlevad ja valivad 2 action item'it Sprint 3-ks

   Näited, mida võivad mainida:
   - "Wireframe'id võtsid kauem aega kui arvasime"
   - "Personas aitasid mõista kasutajaid paremini"
   - "Järgmine kord alustame varem"
   ```

3. **Õppetundide jagamine** (3 min)
   ```
   Iga meeskond jagab 1-2 peamist õppetundi
   Õpetaja märgib tahvlile ühised mustrid
   ```

**Õpetaja märkmed:**
- Vaata, kas Sprint 2 retrospective'id on GitHubis dokumenteeritud
- Kui meeskond ei leia ühtegi parandust - küsi: "Mis võiks olla veelgi parem?"
- Rõhuta: Retrospective pole kritiseerimine, vaid õppimine

---

## OSA 2: Teooria (90 min)

### 2.1 Epic Breakdown ja Task Hierarhia (25 min)

**Interaktiivne selgitus:**

**Epic → User Story → Task hierarhia** (10 min)
```
Tahvlile suur diagramm:

PROJEKT: [Meeskonna projekt]
  └── EPIC: Kasutaja registreerimine
      └── USER STORY: Kasutaja saab e-posti teel registreerida
          └── TASK 1: Loo registreerimise ekraan (UI)
          └── TASK 2: Valideeri e-posti formaat
          └── TASK 3: Salvesta kasutaja andmebaasi
          └── TASK 4: Saada kinnitusmail

Selgita: Epic on suur funktsioon, User Story on kasutaja vajadus, Task on konkreetne töö
```

**Näide tudengite projektist** (10 min)
```
Võta "FindFood" projekt PR #74-st:
"Me tahame, et kasutaja leiaks lähimad restoranid"

EPIC: Restoranide otsing
  USER STORY 1: Kasutaja näeb kaardil lähimaid restorane
    TASK: Loo kaardi komponent
    TASK: Hangi kasutaja asukoht
    TASK: Lae restoranide andmed
    TASK: Kuva restoranid kaardil

  USER STORY 2: Kasutaja saab filtreerida restorane
    TASK: Lisa filtreerimise nupp
    TASK: Loo filtreerimise menüü
    TASK: Rakenda filtreerimise loogika

Küsi tudengitelt: "Miks me ei saa kohe "restoranide otsingut" ühe taskina teha?"
```

**Task'ide tüübid** (5 min)
```
Selgita 5 tüüpi task'e:
1. UI/Frontend: ekraanid, nupud, disain
2. Backend/Logic: andmete töötlemine, äriloogika
3. Database: andmete salvestamine ja pärimine
4. Testing: kas kõik töötab?
5. Documentation: kuidas kasutada/mõista

Küsi: "Milliseid tüüpe teie projekt vajab?"
```

**Õpetaja märkmed:**
- Rõhuta: Task peab olema nii väike, et üks inimene saab 1-3 päevaga valmis
- Näita: Task'id ei ole alati lineaarsed - mõned võib teha paralleelselt
- Jälgi: Kas tudengid mõistavad hierarhiat?

### 2.2 Story Points ja Estimeerimise Tehnikad (20 min)

**Planning Poker demonstratsioon:**

**Story pointide meeldetuletus** (5 min)
```
Slides + tahvel:
Story point = keerukus, mitte aeg
Fibonacci skeem: 1, 2, 3, 5, 8, 13

1 SP: Lihtne, teame kuidas
2 SP: Selge, vähe tööd
3 SP: Keskmine, eeldab mõtlemist
5 SP: Keeruline, eeldab uurimist
8 SP: Väga keeruline - peaks jagama!
```

**Planning Poker mäng** (10 min)
```
Praktika klassiga:
1. Õpetaja kirjeldab task'i: "Loo sisselogimise ekraan"
2. Tudengid näitavad kaartidel/sõrmedel oma hinnangut (1-8)
3. Kõige kõrgem ja madalam selgitavad oma põhjendust
4. Arutelu ja konsensus

Proovi 3-4 task'iga erinevate projektide põhjal
```

**Estimeerimise vead** (5 min)
```
Selgita tavalised vead:
- Liiga optimistlik: "See on lihtne!" (aga ei ole)
- Liiga pessimistlik: "See on võimatu!" (aga tegelikult keskmine)
- Scope creep: Task muutub töö käigus suuremaks

Rõhuta: Esimesed estimeeringud on alati valed - see on normaalne!
```

### 2.3 Arenduse Jälgimise Meetrikad (20 min)

**Velocity tracking:**

**Velocity selgitus** (8 min)
```
Slides + näide:
Velocity = Story Points täidetud per Sprint

"Kooli Köök" näide:
Sprint 1: 15 SP
Sprint 2: 18 SP (parem!)
Sprint 3 plaan: 17-19 SP (realistlik)

Selgita: Velocity kasvab, kui meeskond õpib koostööd
Velocity langeb, kui on probleeme või blockerid
```

**Burndown Chart** (8 min)
```
Tahvlile joonista:

SP
20 |\
   | \
15 |  \____
   |      \
10 |       \
   |        \___
 0 |____________\
   D1 D3 D5 D7 D9

Selgita:
- Alguses on kõik task'id veel tegemata (kõrge)
- Iga päev peaks joon langema
- Ideaalne vs tegelik joon
- Mis juhtub, kui joon ei lange? (Probleemid!)

Küsi: "Mida teha, kui märkate et burndown pole peal graafik?"
```

**Blocker tracking** (4 min)
```
Selgita: Blocker = takistus, mis peatab töö

Näited:
- "Ma ei saa jätkata, kuni X teeb Y valmis" (Dependency)
- "Ma ei tea, kuidas seda teha" (Teadmiste puudus)
- "Meil pole ligipääsu sellele tööriistale" (Ressurss)

Küsi: "Milliseid blockereid võite te kogeda oma projektides?"
```

**Õpetaja märkmed:**
- Rõhuta: Meetrikad pole eesmärk, vaid tööriist probleemide märkamiseks
- Näita: Hea meeskond tunnistab probleeme vara
- Jälgi: Kas tudengid mõistavad, miks me mõõdame?

### 2.4 Daily Standups ja Koordineerimine (15 min)

**Daily standup formaat:**

**3 küsimuse struktuur** (5 min)
```
Tahvlile:
1. Mida ma eile tegin?
2. Mida ma täna teen?
3. Mis mind takistab?

Selgita:
- Mitte probleemide lahendamine, vaid info jagamine
- Max 15 minutit kogu meeskonnale
- Kui probleem suur - võtta eraldi arutelu

Demo: Õpetaja teeb näidis standup'i ise
```

**Asünkroonne standup GitHub-is** (5 min)
```
Näita slides-is template'i:
## Daily Standup [11.11.2025]
**Nimi:** Mari
**Roll:** UX Designer

### Eile tegin:
- Lõpetasin wireframe'i testimise
- Sain 3 tudengilt tagasisidet

### Täna teen:
- Parandused wireframe'is
- Uuen GitHub Projects board'i

### Mind takistab:
- Ei tea, kas peaksin komponente veel detailsemaks tegema

Selgita: GitHub Discussions või Issues kommentaarid
```

**Koordineerimise head tavad** (5 min)
```
Rõhuta:
- Tag-i inimesi, kellelt vajad vastust (@kasutajanimi)
- Ole aus takistuste kohta
- Paku abi teistele

Anti-patterns:
- "Ma ei tea, mida teha" ilma küsimata
- "Kõik on hästi" kui tegelikult on probleeme
- "Ma lihtsalt ei jõudnud" ilma põhjenduseta
```

### 2.5 Continuous Integration põhitõed (10 min)

**CI/CD kontseptsioon ilma tehnilise detailita:**

**Mis on CI/CD?** (5 min)
```
Selgita lihtsalt:
CI = Continuous Integration = Pidev kokkupanemine
CD = Continuous Deployment = Pidev avaldamine

Analoogia: Nagu lego ehitamine
- Iga kord kui keegi lisab tüki, kontrollime kas kõik sobib kokku
- Kui ei sobi, märkame kohe (mitte 2 nädala pärast!)

Küsi: "Mis juhtub, kui 5 inimest ehitavad erinevaid osi 2 nädalat ja siis üritavad kokku panna?"
```

**GitHub Actions sissejuhatus** (5 min)
```
Näita slides-is:
GitHub Actions = automaatne töö tegemine

Näited:
- Automaatne kontroll: "Kas kõik failid on olemas?"
- Automaatne test: "Kas readme on kirjutatud?"
- Automaatne deployment: "Avalda veebilehel"

Selgita: Te ei pea seda veel kasutama, aga hea teada et eksisteerib
```

---

## OSA 3: Praktiline töötuba (90 min)

### 3.1 Sprint 3 Planning (20 min)

**Meeskondade ettevalmistus:**

**Sprint 3 Goal seadmine** (5 min)
```
Iga meeskond kirjutab oma Sprint 3 Goal:
"Mida me tahame saavutada?"

Näited:
- "Põhifunktsioonid on tehniliselt kirjeldatud ja ülesanded jagatud"
- "Arenduse simulatsioon läbitud ja dokumenteeritud"
- "Kõik tehnilised otsused on dokumenteeritud"

Kontrolli: Kas goal on mõõdetav?
```

**Capacity planning** (5 min)
```
Meeskonnad hindavad oma capacity:
- Võta Sprint 2 velocity (nt 18 SP)
- Sprint 3 on simulatsioon - võib olla pisut vähem (15-17 SP)
- Arvestada: 1 nädal + seminari töö

Kirjuta tahvlile igale meeskonnale nende capacity
```

**Backlog selection** (10 min)
```
Meeskonnad valivad Sprint 3 ülesandeid:
1. Epic breakdown (kohustuslik - 5 SP)
2. Technical specification (kohustuslik - 5 SP)
3. Daily standup simulation (kohustuslik - 3 SP)
4. Sprint progress tracking (kohustuslik - 2 SP)

Kokku: ~15 SP

Lisa projekti GitHub Projects board'i
```

**Õpetaja märkused:**
- Jälgi, et ülesanded on realistlikud
- Aita meeskondadel mõista, et nad ei koodi - nad kirjeldavad ja simuleerivad
- Kontrolli: Kas GitHub Projects board on kasutusel?

### 3.2 Epic Breakdown Workshop (30 min)

**Juhendatud töötuba meeskondade projektidega:**

**Epic'u valik** (5 min)
```
Iga meeskond valib 1 peamise Epic'u oma projektist:
Näide "FindFood": "Restoranide otsing ja kuvamine"
Näide "Kooli Köök": "Mikrolaineahjude broneerimissüsteem"

Küsimus: "Milline on teie projekti kõige tähtsam funktsioon?"
```

**User Story breakdown** (10 min)
```
Iga meeskond jagab Epic'u 3-5 User Story-ks:

Template tahvlil:
EPIC: [Nimi]
  USER STORY 1: Kui [kasutaja], siis soovin [funktsioon], et [väärtus]
  USER STORY 2: ...
  USER STORY 3: ...

Näide "FindFood":
EPIC: Restoranide otsing
  US1: Kui näljas tudeng, siis soovin näha kõiki restorane kaardil, et leida lähim
  US2: Kui tudeng, siis soovin filtreerida restorane hinna järgi, et leida odavam
  US3: Kui tudeng, siis soovin näha restorani lahtiolekuaegu, et teada kas avatud

Liikuge meeskondade vahel ja aidake
```

**Task breakdown** (15 min)
```
Iga meeskond võtab 1 User Story ja jagab Task'ideks:

Template:
USER STORY: [Nimi]
  UI TASK: Loo...
  BACKEND TASK: Töötle...
  DATABASE TASK: Salvesta...
  TESTING TASK: Testi...
  DOCS TASK: Dokumenteeri...

Näide "FindFood" US1:
US1: Restoranide kuvamine kaardil
  TASK 1 (UI): Loo kaardi komponent ekraanil
  TASK 2 (Backend): Hangi kasutaja GPS asukoht
  TASK 3 (Backend): Lae restoranide andmed API-st
  TASK 4 (Backend): Filtreeri restoranid 2km raadiuses
  TASK 5 (UI): Kuva restoranid markeritena kaardil
  TASK 6 (Testing): Testi kas kaart laeb õigesti
  TASK 7 (Docs): Kirjelda kuidas kaart töötab

Iga task saab story point'i (planning poker!)
```

**Õpetaja märkused:**
- Jälgi: Kas task'id on piisavalt väikesed? (max 5 SP)
- Aita mõista: Task peab olema konkreetne tegevus
- Kontrolli: Kas kõik rollid on kaasatud? (UI, Backend, Testing, Docs)

### 3.3 Sprint Simulation - "2 nädala arendus 40 minutiga" (25 min)

**Kompresseeritud Sprint kogemus:**

**Simulatsiooni ülesseadmine** (5 min)
```
Selgita reeglid:
- 10 vooru = 10 tööpäeva (2 nädalat)
- Iga voor kestab 3 minutit
- Iga voor = 1 päev arenduses

Iga vooru ajal:
1. Kirjuta daily standup (30 sek)
2. Vali üks task ja "tee see valmis" = kirjuta, mida tegid (1 min)
3. Uuenda GitHub Projects board (30 sek)
4. Viska täringut: võib-olla tuleb event! (30 sek)
5. Uuenda burndown chart (30 sek)

Valmista ette:
- Timer nähtaval
- Burndown chart tahvlil/paberil
- Event kaardid (valikuline)
```

**Event kaardid** (valikuline - annab mängulisust):
```
Võimalikud sündmused (õpetaja valib juhuslikult):
- "Blocker: Vajad teise tiimiliikmelt infot" (1 voor ooteaeg)
- "Boost: Task läks kiiremini kui arvasid" (-2 SP burndown'ist)
- "Bug found: Lisa 1 uus test task" (+2 SP burndown'i)
- "Stakeholder feedback: Muuda 1 wireframe'i" (1 voor lisa tööd)
- "Teammate on vacation: Võta üle tema task" (rohkem tööd)
```

**Simulatsiooni käivitamine** (18 min)
```
Voor 1-10:
Õpetaja hõikab: "Päev 1! 3 minutit algab!"
Timer käima
Meeskonnad töötavad

Õpetaja liigub ringi:
- Kontrollib: kas standup kirjutatud?
- Küsib: "Mis teil takistab?"
- Abistab: burndown chart uuendamisel

Vahepeal (päev 5): "Sprint on poolel! Vaadake burndown'i - kas olete graafikus?"

Lõpus (päev 10): "Sprint läbi! Vaadake tulemusi"
```

**Õpetaja märkused:**
- Hoia aega rangelt - 3 min on 3 min
- Jälgi: kas meeskonnad uuendavad GitHub Projects'i?
- Aita: kui keegi on hätta jäänud
- Märgi üles: millised meeskonnad kasutavad head praktikat

### 3.4 Burndown Chart Analüüs (15 min)

**Tulemuste analüüs:**

**Meeskondade burndown'ide võrdlus** (5 min)
```
Iga meeskond näitab oma burndown chart'i:
- Kas jõudsid 0-ni?
- Kus oli kõige suurem langus?
- Kas olid blockerid?

Tahvlile joonista:
- Ideaalne joon
- Meeskondade tegelikud jooned

Küsi: "Mis sarnast? Mis erinevat?"
```

**Velocity arvutamine** (5 min)
```
Iga meeskond arvutab:
- Planeeritud SP: 15 SP
- Täidetud SP: ? (simulatsiooni põhjal)
- Velocity = täidetud SP

Võrdle Sprint 2-ga:
Sprint 2: 18 SP
Sprint 3: 15 SP (simulatsioon)
Kas realistlik?
```

**Õppetunnid** (5 min)
```
Küsi igalt meeskonnalt:
- "Mis oli üllatav?"
- "Mida tegite hästi?"
- "Mida teeksite teisiti päris Sprint'is?"

Kirjuta tahvlile peamised õppetunnid
```

---

## Seminari lõpp ja kodutöö juhendamine (10 min)

### Kodutöö 5 tutvustus

**Õpetaja selgitus:**

```
Kodutöö = dokumenteerida Sprint 3 simulatsioon ja lisada detailid

Kohustuslikud failid:
1. sprint-3-plan.md - Sprint 3 goal, capacity, selected tasks
2. epic-breakdown.md - 1 Epic → User Stories → Tasks
3. daily-standups.md - 10 päeva standup kirjeid (simuleeritud)
4. sprint-progress.md - Burndown chart + velocity analüüs
5. technical-decisions.md - 3 tehnilist otsust (nt miks mobile-first?)
6. sprint-3-review.md - Mis "valmis sai"?
7. sprint-3-retrospective.md - Start-Stop-Continue Sprint 3 kohta

Rolli-põhised lisad:
- Product Owner: backlog refinement dokumentatsioon
- Project Manager: blockerite jälgimine ja lahendused
- Developer: tehnilise arhitektuuri kirjeldus
- UX/UI Designer: testimise dokumentatsioon

Tähtaeg: 1 nädal
GitHub workflow: branch → commit → push → PR
```

**Hindamiskriteeriumid** (3 min)
```
Näita slides-is:
1. Completeness - kas kõik failid olemas? (25%)
2. Detail level - kas piisavalt detailne? (25%)
3. Realism - kas võiks olla päris sprint? (25%)
4. Team coordination - kas meeskond töötas koos? (25%)
```

**Küsimused-vastused** (2 min)

---

## Õpetaja märkmed ja nõuanded

### Aja juhtimine
- Sprint simulation võib venida - ole valmis kohandama
- Kui aeg lõpeb - lühenda voore 2 min-le
- Pausid on olulised - 90 min järel 10 min paus

### Väljakutsed ja lahendused

**Väljakutse**: "Me ei saa aru, kuidas task'e jaotada ilma koodimist teadmata"
**Lahendus**: "Kirjeldage, mida kasutaja näeb ja mida süsteem peab tegema. Nt 'Kasutaja vajutab nuppu' (UI task) ja 'Süsteem saadab e-maili' (backend task)"

**Väljakutse**: "Sprint simulation on segane"
**Lahendus**: "Esimesed 2 vooru tehke koos - näidake tahvlil oma näidet"

**Väljakutse**: "Burndown chart ei lange"
**Lahendus**: "See on normaalne! Päris projektides juhtub sama. Miks? Rääkige sellest!"

### Järgmise seminari ettevalmistus

**Seminar 6 = Final presentations**
- Kontrolli: kas kõik meeskonnad esitasid Sprint 3 kodutöö
- Valmista ette: esitluste hindamise rubric
- Planeeri: 5-7 min esitlus meeskonna kohta

---

## Tagasiside kogumine

**Seminari lõpus:**
1. Kas sprint simulation oli kasulik?
2. Kas mõistate nüüd, mida arendajad teevad?
3. Mis oli kõige huvitavam?

---

## Kokkuvõte õpetajale

**Seminari edu tunnused:**
- Tudengid mõistavad epic → story → task hierarhiat
- Meeskonnad suutsid simuleerida 2-nädalast sprinti
- Burndown chart on mõistetav
- Tudengid teavad, mida arendamine tähendab (ilma koodita!)

**Järgmine samm:**
Seminar 6 = Lõplikud esitlused, kogu projekti retrospective, portfolio hindamine
