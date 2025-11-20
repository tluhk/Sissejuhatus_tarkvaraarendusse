# Seminar 5: Sprint 3 - Arendamine | Seminaritöö ja kodutöö näide

## "FindFood" projekti tutvustus

**"FindFood"** on mobiilirakendus, mis aitab tudengitel leida lähimaid ja soodsamaid restorane/kohvikuid kooli läheduses. Projekt keskendub asukoha-põhisele otsingule ja hinnafiltreerimisele.

### Sprint 1 ja 2 tulemused:
- **Sprint 1**: Projektiplaan, rollid, tehniline arhitektuur
- **Sprint 2**: 2 persoonat (Joonas, Maarja), wireframe'id, user journey

### Sprint 3 eesmärk:
Simuleerida arendusprotsessi - võtta Sprint 2 disain ja "arendada" see dokumentatsiooni kaudu, ilma koodi kirjutamata.

---

## Seminari praktilise osa näide

### Sprint 2 Review - "FindFood" (15 min)

#### Demo presentatsioon

**Meeskond:**
- Indrek (Product Owner/Project Manager)
- Mihkel (Developer)
- Dagmar (UX/UI Designer)

**Sprint 2 eesmärk meeldetuletus:**
> "Kasutajaliidese prototüüp on loodud ja testitud, arendus saab alustada tööga."

**Saavutused:**
```markdown
1. Personas:
   - Joonas Tamm, 28 - otsib taskukohast lõunat
   - Maarja Kask, 20 - tahab päevapakkumisi

2. Wireframes:
   - 8 ekraani (kaart, otsing, filtreerimine, restoran detail)
   - Mobile-first lähenemine

3. User Journey:
   - 4-etapiline teekond (probleem → otsing → leidmine → kasutamine)

4. Sprint 2 mõõdikud:
   - Planeeritud: 16 SP
   - Täidetud: 18 SP (112%)
   - Velocity: 18 SP
```

**Stakeholder'ite küsimused:**
- Q: "Kuidas see tehniliselt töötab?"
- A: "Kasutame GPS-i asuk oha leidmiseks ja Google Maps API-t restoranide kuvamiseks"

---

### Sprint 2 Retrospective - "FindFood"

#### Start-Stop-Continue analüüs:

**CONTINUE (mis läks hästi):**
- Wireframe'id olid selged ja kasutajatele mõistetavad
- Personas aitasid fokuseerida kõige olulisematele funktsioonidele
- User journey näitas selgelt, kus kasutajal probleemid tekivad
- Meeskonna koostöö toimis - kõik panustasid

**STOP (mida lõpetada):**
- Liiga palju detaile prototüüpides (kulutasime aega värvide peale)
- Unustasime error state'id (mis juhtub kui GPS ei tööta?)
- Liiga palju väikesi PR-e (8 PR-i 3 nädalaga)

**START (mida alustada Sprint 3-s):**
- Task breakdown varem - ei jäta viimase hetkeni
- Kirjutame technical decisions dokumendi kohe alguses
- Kasutame GitHub Projects'i automated workflow'sid
- Testimise task'id lisame kohe alguses, mitte lõpus

#### Action Items Sprint 3-ks:

1. **Indrek (PO/PM):** Loob technical decisions template'i
2. **Mihkel (Dev):** Uurib GitHub Projects automation'eid
3. **Dagmar (UX):** Dokumenteerib error state'id wireframe'ides
4. **Kõik:** Max 1 PR päevas, kõik sisaldavad testeerimist

---

## Epic Breakdown Workshop näide

### Valitud Epic: "Restoranide otsing ja kuvamine"

See on "FindFood" peamine funktsioon - kasutaja peab leidma lähimad restoranid kaardil.

#### User Stories Breakdown:

```markdown
# EPIC: Restoranide otsing ja kuvamine

## User Story 1: Kaardil kuvamine (8 SP)
**Prioriteet:** Must Have
**Kirjeldus:** Kui näljas tudeng, siis soovin näha kõiki restorane kaardil,
              et leida lähim koht lõunaks.

**Acceptance Criteria:**
✅ Kasutaja näeb oma asukohta kaardil
✅ Kõik restoranid 2km raadiuses on nähtavad markeritena
✅ Kaart laadib alla 3 sekundi jooksul
✅ Töötab nii iPhone kui Android telefonides

### Tasks:

#### TASK 1: Loo kaardi komponent (UI) - 2 SP
**Assignee:** Dagmar (UX Designer)
**Kirjeldus:** Loo kaardi komponendi layout mobiilivaates
**DoD:**
- Kaart on responsive (320px - 428px)
- Bottom navigation bar ei kata kaarti
- Zoom in/out nupud on nähtavad
- Wireframe täpselt järgitud

#### TASK 2: Hangi kasutaja GPS asukoht (Backend) - 2 SP
**Assignee:** Mihkel (Developer)
**Kirjeldus:** Kasuta browser'i Geolocation API-t asukoja hankimiseks
**DoD:**
- Küsib kasutajalt loa asukoh a kasutamiseks
- Käsitleb "deny" stsenaariumi (näitab Tallinna keskpunkti)
- Salvestab asukoha local storage'sse
- Uuendab asukohta iga 5 minuti tagant

#### TASK 3: Lae restoranide andmed API-st (Backend) - 3 SP
**Assignee:** Mihkel (Developer)
**Kirjeldus:** Integreeri Google Places API restoranide andmete saamiseks
**DoD:**
- API päring tagastab 20 lähimat restorani
- Andmed sisaldavad: nimi, aadress, hinnang, lahtiolekuaeg
- Error handling kui API ei vasta (näita cached data)
- Rate limiting (max 1 päring 30 sek jooksul)

#### TASK 4: Filtreeri restoranid 2km raadiuses (Backend) - 2 SP
**Assignee:** Mihkel (Developer)
**Kirjeldus:** Arvuta kaugus kasutaja asukohast ja filtreeri
**DoD:**
- Kasuta Haversine formula kauguse arvutamiseks
- Sorteeri restoranid läheduse järgi
- Näita ainult 2km raadiuses olevaid
- Performance: toimib <1 sek 100 restoran iga puhul

#### TASK 5: Kuva restoranid markeritena kaardil (UI) - 3 SP
**Assignee:** Dagmar (UX Designer)
**Kirjeldus:** Lisa restoranide markerid kaardile
**DoD:**
- Marker icon eristub taustast
- Marker'ile vajutades avaneb restoran info
- Clusterimine kui liiga palju markereid (>50)
- Animatsioon marker'i ilmumisel

#### TASK 6: Testi kaardi funktsionaalsust (Testing) - 2 SP
**Assignee:** Indrek (PM) + Dagmar (UX)
**Kirjeldus:** Testi kõiki kaardi funktsioone erinevatel seadmetel
**DoD:**
- Testitd iPhone 12 Mini ja Samsung Galaxy S21 simulaatorites
- GPS töötab obides seadmetes
- Markerid kuvatakse õigesti
- Zoom in/out töötab sujuvalt
- Dokumenteeritud 3 test case'i

#### TASK 7: Dokumenteeri kaardi rakendamine (Docs) - 1 SP
**Assignee:** Indrek (PO/PM)
**Kirjeldus:** Kirjuta dokumentatsioon kuidas kaart töötab
**DoD:**
- Selgita API integratsioon
- Näita data flow diagramm
- Kirjelda error handling stsenaariumid
- Lisa screenshots olemuslikest ekraanidest

**Kokku US1:** 15 SP
```

---

## User Story 2: Hinna järgi filtreerimine (5 SP)

```markdown
**Kirjeldus:** Kui tudeng, siis soovin filtreerida restorane hinna järgi,
              et leida taskukohane koht.

**Tasks:**
- TASK 8: Loo filtreerimise UI (2 SP) - Dagmar
- TASK 9: Rakenda filtreerimise loogika (2 SP) - Mihkel
- TASK 10: Testi filtreerimist (1 SP) - Indrek

**Kokku US2:** 5 SP
```

---

## User Story 3: Lahtiolekuaegade kuvamine (3 SP)

```markdown
**Kirjeldus:** Kui tudeng, siis soovin näha restorani lahtiolekuaegu,
              et teada kas praegu avatud.

**Tasks:**
- TASK 11: Kuva lahtiolekuajad (2 SP) - Dagmar
- TASK 12: Märgi "hetkel avatud" markerid (1 SP) - Dagmar

**Kokku US3:** 3 SP
```

---

## Sprint 3 Planning - "FindFood"

### Sprint Goal

> "Põhifunktsioonid (kaardil kuvamine ja filtreerimine) on tehniliselt
> kirjeldatud, ülesanded jagatud ja simuleeritud arendusprotsess dokumenteeritud."

### Capacity

**Meeskond (3 liiget):**
- Indrek (PO/PM): 5 SP
- Mihkel (Developer): 6 SP
- Dagmar (UX Designer): 6 SP

**Kokku Sprint 3:** 17 SP

**Põhjendus:**
- Sprint 2 velocity oli 18 SP
- Sprint 3 on simulatsioon - vähem praktilist tööd
- Fookus dokumentatsioonil ja breakdown'il

### Selected Tasks Sprint 3-ks

**Must Have (15 SP):**
1. Epic breakdown: Restoranide otsing (5 SP) - Kõik
2. Technical decisions dokumentatsioon (5 SP) - Mihkel
3. Daily standup simulation (3 SP) - Kõik
4. Sprint progress tracking (2 SP) - Indrek

**Should Have (juhul kui jõuavad):**
5. Usability testing plaan (3 SP) - Dagmar

---

## Sprint Simulation - "FindFood" (10 päeva)

### Burndown Chart

| Päev | Planeeritud | Alles | Valmis saanud | Märkused |
|------|-------------|-------|---------------|----------|
| 1 | 17 SP | 17 SP | - | Sprint Planning |
| 2 | 17 SP | 15 SP | Epic breakdown alustatud (2 SP) | |
| 3 | 17 SP | 12 SP | Epic breakdown valmis (3 SP) | |
| 4 | 17 SP | 10 SP | Tech decisions 1-2 (2 SP) | |
| 5 | 17 SP | 10 SP | **BLOCKER**: Ootame PO feedback'i | |
| 6 | 17 SP | 7 SP | Tech decision 3 + standup (3 SP) | Blocker lahendatud |
| 7 | 17 SP | 5 SP | Daily standups dokument (2 SP) | |
| 8 | 17 SP | 3 SP | Progress tracking (2 SP) | |
| 9 | 17 SP | 1 SP | Usability testing plaan (2 SP) | Bonus! |
| 10 | 17 SP | 0 SP | Sprint review ja retro (1 SP) | Sprint valmis! |

**Velocity:** 17 SP täidetud / 17 SP planeeritud = 100%

---

## Daily Standups näide - "FindFood"

### Päev 3 [15.11.2025]

#### Indrek (Product Owner / Project Manager)
**Eile:**
- Viimistlesime epic breakdown'i koos meeskonnaga
- Kontrollisin üle, et kõik task'id on GitHub Projects'is

**Täna:**
- Alustan technical decisions dokumenti
- Koordineerun Mihkliga API valiku üle

**Takistab:**
- Ei ole veel kindel, kas Google Places API on parim valik (tasuda või tasuta alternatiiv?)

#### Mihkel (Developer)
**Eile:**
- Uurisin Google Places API dokumentatsiooni
- Kirjutasin TASK 2 (GPS) detailse kirjelduse

**Täna:**
- Kirjutan technical decision: "Miks Google Places API"
- Hakkan kirjeldama API integratsioon architektuurki

**Takistab:**
- Vajan Indrekilt kinnitust API valiku kohta enne jätkamist

#### Dagmar (UX/UI Designer)
**Eile:**
- Lõpetasin epic breakdown UI task'ide osa
- Uurisin map marker design patterns'e

**Täna:**
- Hakkan kirjutama usability testing plaani
- Dokumenteerin wireframe'ide täpsustusi

**Takistab:**
- Midagi ei takista, saan jätkata

---

### Päev 5 [17.11.2025] - BLOCKER PÄEV

#### Indrek (PO/PM)
**Eile:**
- Kirjutasin 2 technical decision'it (Mobile-first, Google API)
- Lõin blockerite log dokumendi

**Täna:**
- **BLOCKER**: Ootan õpetaja tagasisidet API valiku kohta
- Saan teha standup dokumentatsiooni vahepeal

**Takistab:**
- Ei saa jätkata technical decisions'iga enne kinnitust

#### Mihkel (Developer)
**Eile:**
- Alustasin technical architecture dokumenti
- Kirjeldasin data flow'i

**Täna:**
- **BLOCKER**: Ootan Indrekilt kinnitust enne API sektsiooni
- Teen vahepeal task'ide detailseid kirjeldusi

**Takistab:**
- API valik mõjutab kõiki backend task'e

#### Dagmar (UX Designer)
**Eile:**
- Alustasin usability testing plaani
- Kirjeldasin test scenarium'e

**Täna:**
- Jätkan usability testing plaaniga (blocker ei mõjuta)
- Dokumenteerin error state'id

**Takistab:**
- Midagi ei takista (õnneks!)

---

### Päev 6 [18.11.2025] - BLOCKER LAHENDATUD

#### Indrek (PO/PM)
**Eile:**
- Sain õpetajalt kinnituse - Google Places OK!
- Uuendasin blockerite log'i

**Täna:**
- Lõpetan technical decision #3
- Alustan sprint progress tracking dokumendi

**Takistab:**
- Blocker lahendatud! Saame edasi minna

---

## Technical Decisions näide - "FindFood"

### Otsus 1: Mobile-First lähenemine

**Kontekst:**
Peame otsustama, kas arendame esmalt mobile või desktop versiooni.

**Probleem:**
Meil on piiratud aeg ja ressursid. Ei saa mõlemaid paralleelselt arendada.

**Otsus:**
Mobile-first lähenemine

**Põhjendus:**
1. **Kasutajastatistika:** 92% meie sihtgrupist (tudengid) kasutab peamiselt telefoni
2. **Kontekst:** Kasutaja otsib restorani liikvel olles, mitte arvuti taga
3. **GPS vajalik:** Mobiilsed seadmed omavad GPS-i, desktop mitte alati
4. **Lihtsam skaleerida:** Mobile → desktop on lihtsam kui vastupidi
5. **Design philosophy:** Mobile-first sunnib keskenduma olulistele funktsioonidele

**Kaalutud alternatiivid:**
- **Desktop-first:** Keeruline, liiga palju funktsioone korraga
- **Responsive samaaegselt:** Ressursside puudus, aeglustaks arendust
- **Ainult mobile:** Võimalik, aga kaotame desktop kasutajad (8%)

**Mõju projektile:**
- UI disain algab 375px ekraanist (iPhone SE)
- Navigatsioon on bottom navigation bar (sõrmega kättesaadav)
- Kõik funktsioonid peavad töötama puutetundliku ekraaniga
- Map component peab olema optimeeritud mobiilikasutuseks
- Filtreerimise menüü on drawer (avaldub alt)

**Tehnilised piirangud:**
- Performance: max 50MB bundle size
- Battery: GPS kasutus peab olema optimeeritud
- Offline: cached data kui internet puudub

---

### Otsus 2: Google Places API vs Alternatiivsed lahendused

**Kontekst:**
Vajame restoranide andmeid - nimi, asukoht, hinnang, lahtiolekuajad, pildid.

**Probleem:**
Millist API-t kasutada? Tasuline vs tasuta? Kvaliteet vs hind?

**Otsus:**
Google Places API (Tasuta tier kuni 1000 päringut kuus)

**Põhjendus:**
1. **Andmete kvaliteet:** Kõige täpsemad ja uuendatud andmed
2. **Katvus:** 100% Eesti restoranid kaetud
3. **Tasuta tier piisav:** 1000 päringut/kuu = 33 kasutajat päevas
4. **Dokumentatsioon:** Väga hea, palju näiteid
5. **Integratsioon:** Lihtne Google Maps'iga

**Kaalutud alternatiivid:**

**Foursquare API:**
- Plussid: Tasuta, head ratingud
- Miinused: Eesti katvus 70%, vähe lahtiolekuaegu

**OpenStreetMap + Overpass API:**
- Plussid: Täiesti tasuta, open-source
- Miinused: Andmed ei ole alati uuendatud, puuduvad ratingud

**Oma andmebaas (manual input):**
- Plussid: Täielik kontroll
- Miinused: Hoolduskulu, andmete vananemineaja

**Mõju projektile:**
- Need API key Google Cloud Console'st
- Implementeeri rate limiting (max 1 päring per 30 sek)
- Cache'i tulemused lokaalses storage'is
- Error handling kui quota ületatud
- Kuvame "powered by Google" logo

**Kulud:**
- Tasuta tier: 0€ (1000 päringut/kuu)
- Kui ületame: $0.017 per päring (alates 1001-st)
- Predicted cost esimesel kuul: 0€

---

### Otsus 3: Local Storage vs Backend Database

**Kontekst:**
Kus me salvestame kasutaja eelistused (filter settings, favorite restoranid)?

**Probleem:**
Backend pole veel valmis (simulatsioon!). Kas ehitame kohe või kasutame local storage'i?

**Otsus:**
Alguses Local Storage (browser), hiljem migratsioon backend'ile

**Põhjendus:**
1. **Kiirem arendus:** Local storage on lihtne implementeerida
2. **Offline töö:** Toimib ilma internetita
3. **Privaatsus:** Andmed kasutaja seadmes, mitte serveris
4. **MVP piisav:** Esimeses versioonis ei vaja sync'i

**Kaalutud alternatiivid:**
- **Firebase:** Kiire, aga vendor lock-in
- **Oma backend:** Liiga keeruline MVP jaoks
- **IndexedDB:** Võimsam kui Local Storage, aga overkill

**Migratsioonimatee:**
```
V1 (MVP): Local Storage
  ↓
V2: Local Storage + Backend sync
  ↓
V3: Peamiselt Backend, Local Storage cache'ina
```

**Tehnilised detailid:**
- Max 10MB Local Storage per domeen
- JSON vormingus: `{filters: {...}, favorites: [...]}`
- Expire after 30 päeva
- Clear on logout

---

## Sprint 3 Review - "FindFood"

### Sprint Goal

Kas saavutasime?: **JAH ✅**

> "Põhifunktsioonid on tehniliselt kirjeldatud, ülesanded jagatud
> ja simuleeritud arendusprotsess dokumenteeritud."

### Mis valmis sai

**Planeeritud 17 SP:**
1. ✅ Epic breakdown: Restoranide otsing (5 SP) - VALMIS
2. ✅ Technical decisions dokumentatsioon (5 SP) - VALMIS (3 otsust)
3. ✅ Daily standup simulation (3 SP) - VALMIS (10 päeva)
4. ✅ Sprint progress tracking (2 SP) - VALMIS (burndown chart)
5. ✅ Usability testing plaan (3 SP) - BONUS! Jõudsime ka selle teha

**Täidetud:** 17 SP / 17 SP = 100%
**Velocity:** 17 SP (võrreldes Sprint 2: 18 SP - väike langus simulatsiooni tõttu)

### Mis läks plaanist erinevalt

**Blockerid:**
- Päev 5: API valiku kinnituse ootamine (1 päev delay)
- Lahendus: Tegime vahepeal muid task'e

**Üllatused:**
- Jõudsime usability testing plaani teha (ei olnud planeeritud!)
- Technical decisions võtsid vähem aega kui arvamine (5 SP → 4 SP tegelikult)

### Stakeholder'ite tagasiside

**Teised meeskonnad (Kooli Köök, XYZ projekt):**
- "Epic breakdown oli väga detailne - inspireeris meid"
- "Technical decisions dokument on hea näide põhjendamisest"
- "Daily standups näitavad hästi, kuidas päris meeskond suhtleb"

**Õpetaja tagasiside:**
- "Hea töö blockerite käsitlemisega"
- "Technical architecture võiks olla veidi detailsem"
- "Väga realistlikud daily standups"

### Järeldused

**Kas olemeksvalmis "arendama"?:** JAH

Sprint 3 simulatsioon näitas, et meie disain (Sprint 2 wireframe'id) on piisavalt detailne ja tehniliselt teostatav. Kui see oleks päris projekt, saaksime nüüd koodimise käivitada.

---

## Sprint 3 Retrospective - "FindFood"

### Start-Stop-Continue

#### CONTINUE (mis läks hästi)

**Epic breakdown:**
- Detailne task'ide kirjeldus aitas mõista töö ulatust
- Planning poker andis realistlikud story points
- Igal task'il oli selge DoD (Definition of Done)

**Meeskonnatöö:**
- Daily standup simulatsioonis osaresime kõik
- Blockerid dokumenteeriti ja lahendati kiiresti
- Kommunikatsioon GitHub-is oli selge

**Dokumentatsioon:**
- Technical decisions olid hästi põhjendatud
- Burndown chart aitas visuaalselt jälgida progressi

#### STOP (mida lõpetada)

**Ülemäärne optism:**
- Esialgu arvasime, et jõuame 20 SP teha (tegelikult 17 SP)
- Järgmises projektis oleme realistlikumad

**Hilise testimise planeerimine:**
- Testing task'id lisasime epic breakdown'i viimastena
- Oleks pidanud olema koos user story'ga

**Dokumentatsiooni ootamine:**
- Mõned dokumendid kirjutasime viimsel päeval
- Oleks saanud paralleelselt teha

#### START (mida järgmises projektis)

**Varasem technical research:**
- Otsustame API-d ja arhitektuuri enne Sprint'i
- Väldime blockereid

**Rohkem automatiseerimist:**
- GitHub Projects automation
- Auto-assign labels

**Paremini testida:**
- Lisame test task'id kohe alguses
- Iga user story peab sisaldama test casei

### Individuaalsed reflektsioonid

#### Indrek (Product Owner / Project Manager)

**Mida õppisin:**
Sprint 3 simulatsioon avas silmad, kui keeruline on arenduse koordineerimine.
Product Owner roll tähendab pidevaid otsuseid - API valik, feature prioriteedi.
Mõistsin, et technical knowledge on oluline ka PO-le - ei saa ainult "kasutaja vajadusi"
tunda, peab ka tehnilisi piiranguid mõistma.

**Mis oli keeruline:**
Epic breakdown võttis kauem aega kui arvasin. Iga task pidi olema piisavalt väike,
aga mitte liiga väike. 5 SP task jagasin kolmeks 2-3 SP task'iks.

**Mis üllatav:**
Blockerite käsitlemine oli huvitav - päris projektis oleks see ilmselt veel
keerulisem. Õppisin, et blocker peab dokumenteeri ma kohe, mitte lõpus.

#### Mihkel (Developer)

**Mida õppisin:**
Technical decisions dokumendi kirjutamine oli kasulik harjutus. Sunnitud selgitama
MIKS me midagi valime, mitte ainult VAT. Mõistsin, et iga valik on trade-off -
Google API vs tasuta alternatiiv näiteks.

**Mis oli keeruline:**
Task'ide hindamine (story points) oli raske. Kartsin, et hindan liiga optimistlikult
või pessimistlikult. Planning poker simulatsioon aitas - teiste hinnangud näitasid
teisi perspektiive.

**Mis üllatav:**
Kui palju dokumenteerimist arendus vajab! Arvasin, et developer ainult koodib,
aga tegelikult on vaja API dokumentatsioone, arhitektuuri diagramme, technical
decisions dokumente jne.

#### Dagmar (UX/UI Designer)

**Mida õppisin:**
Epic breakdown näitas, kui oluline on minu wireframe'ide detailsus. Developer'id
vajasid täpseid mõõtmeid, interaktsioonide kirjeldusi, error state'e. Sprint 2-s
ma ei mõelnud sellele.

**Mis oli keeruline:**
Mõista, kuidas UI task'id sõltuvad backend task'idest. Näiteks marker'id kaardil
(UI task) ei saa valmis, kui API integratsioon (backend task) pole valmis.
Dependencies on keerulised!

**Mis üllatav:**
Usability testing plaan oli huvitav kirjutada. Mõtlesin läbi, kuidas ma testiksin
wireframe'e päris kasutajatega. Sprint 3 andis julguse selleks - nüüd tean, et
testimine pole "optional", see on osa arendust.

### Õppetunnid kogu meeskonnale

1. **Planeerimine on 50% tööst:** Epic breakdown võttis palju aega, aga see tasusis
   järgnevat "arendust" (simulatsiooni).

2. **Kommunikatsioon on kriit iline:** Daily standups (isegi simuleeritud) näitasid,
   kui oluline on igapäevane info jagamine.

3. **Dokumentatsioon pole igav:** Technical decisions ja architecture dokumendid
   on vajalikud - tulevikus ei mäleta keegi, miks me midagi valisime.

4. **Testamine algab alguses:** Oleksime pidanud test task'id planeerima koos
   development task'idega, mitte lõpus.

5. **Realism aitab:** Sprint simulation oleks olnud lihtsam, kui oleksime olnud
   algusest peale realistlikumad velocity hindamisel.

---

## Kokkuvõte

"FindFood" Sprint 3 oli edukas - saavutasime Sprint Goal'i ja õppisime arendusprotsessist
palju ilma ühtegi koodi rida kirjutamata. Nüüd mõistame, mida arendajad teevad, kuidas
meeskond koordineerib tööd ja miks documentation on oluline.

**Järgmine samm:** Seminar 6 - lõplikud esitlused, kus näitame kogu 3 Sprint'i tulemust!

---

## Failide näited

Kõik "FindFood" Sprint 3 failid asuvad repositooriumis:
```
project_findfood/
├── 01_Sprint_1/ (Sprint 1 materjalid)
├── 02_Sprint_2/ (Sprint 2 materjalid)
└── 03_Sprint_3/               ← UUS!
    ├── README.md
    ├── sprint-3-plan.md
    ├── epic-breakdown.md
    ├── daily-standups.md
    ├── sprint-progress.md
    ├── technical-decisions.md
    ├── sprint-3-review.md
    ├── sprint-3-retrospective.md
    ├── backlog-refinement.md (Indrek - PO)
    ├── blockers-log.md (Indrek - PM)
    ├── technical-architecture.md (Mihkel - Dev)
    └── usability-testing-plan.md (Dagmar - UX)
```

**Kokku:** 12 dokumenti, 17 SP tööd, 10 päeva simulation, 3 tehnilist otsust,
1 blocker lahendatud, 100% Sprint Goal saavutatud! 🎉
