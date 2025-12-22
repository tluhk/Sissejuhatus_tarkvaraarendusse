# Eksam

Eksam koosneb esitlusest ja testist.  
Eksamile pääsemise eelduseks on osalemine grupitöödes ja seminarides.

## Esitluse struktuur ja juhised

**Eesmärk:** Esitleda mida õppisite tarkvaraarenduse kohta läbi kolme sprindi ja teooria osade, mitte ainult seda, mida teie toode teeb.

**Kestus:** 10-15 minutit + 5 minutit küsimused

**Hindamiskriteeriumid:**
- Arusaam tarkvaraarenduse protsessist (40%)
- Meeskonnatöö ja rollide mõistmine (30%)
- Õpitud metoodikate rakendamine (20%)
- Refleksioon ja kriitilisus (10%)

---

## Esitluse struktuur

### 1. Sissejuhatus (1-2 minutit)

**Mida esitada:**
- Meeskonna nimi ja liikmed
- Lühike ülevaade projektist (1 lause: mis probleemi lahendasite?)
- Esitluse ülesehitus

**Näide:**
> "Oleme meeskond X ja meie projekt oli Y probleem. Täna räägime sellest, kuidas me õppisime tarkvaraarenduse protsessi läbi kolme sprindi - uurimisest planeerimiseni ja arenduseni."

---

### 2. Protsessi ülevaade (2-3 minutit)

**Mida esitada:**
- Kolme sprindi ülevaade
- Mis oli iga sprindi eesmärk?
- Kuidas sprindid omavahel seostusid?

**Fookus tarkvaraarendusel:**
- Miks algab arendus alati probleemi mõistmisest?
- Kuidas iga sprint ehitati eelmise peale?
- Mis oleks juhtunud, kui oleks otse koodimist alustanud?

---

### 3. Õpitud põhimõtted (3-4 minutit)

**Valige 3-4 kõige olulisemat õppetundi ja esitlege neid:**

#### Näide 1: Kasutajakesksus

**Mis õppisime:**
- Probleemi defineerimine enne lahenduse leidmist
- Kasutajate intervjueerimine ja persoonad
- Journey mapping ja valupunktide leidmine

**Kuidas töötasime:**
- Intervjueerisime X kasutajat
- Lõime Y personat põhinedes reaalsete andmete põhjal
- Avastasime, et meie algne eeldus oli vale: [näide]

**Mida see meile õpetas:**
> "Õppisime, et ilma kasutajaid mõistmata võib ehitada täiesti vale lahenduse."

#### Näide 2: Meeskonnatöö ja rollid

**Mis õppisime:**
- Scrum rollid: Product Owner, Project Manager, Developer, UX/UI Designer
- Iga rolli vastutus ja panus
- Kommunikatsiooni olulisus (daily standups, retrospectives)

**Kuidas töötasime:**
- Jaotasime rollid vastavalt huvile ja oskustele
- Tegime X daily standup'i
- Kohtasime Y blocker'it ja lahendasime neid meeskonnana

**Mida see meile õpetas:**
> "Õppisime, et tarkvaraarendus on meeskonnatöö..."

#### Näide 3: Agiilne metoodika

**Mida õppisime:**
- Sprint tsükkel: planning → daily standups → review → retrospective
- Iteratiivne vs lineaarne (Waterfall) lähenemine
- Velocity ja burndown chart'i kasutamine

**Kuidas töötasime:**
- Iga sprint lõppes review ja retrospective'iga
- Sprint 3 simulatsioon näitas, kuidas blocker'id mõjutavad velocity't
- Õppisime oma estimating'ut parandama

**Mida see meile õpetas:**
> "Õppisime, et paindlikkus ja pidev tagasiside on olulisemad kui täiuslik algne plaan."

#### Näide 4: Dokumenteerimine ja GitHub workflow

**Mida õppisime:**
- Git branching ja pull request workflow
- Dokumenteerimine kui osa tarkvarast
- Issue tracking ja project management GitHub'is

**Kuidas töötasime:**
- Igal dokumendil oli branch → PR → review → merge
- Lõime X issue'd ja Y pull request'i
- GitHub Projects aitas visualiseerida progressi

**Mida see meile õpetas:**
> "Õppisime, et versioonihaldus ja dokumenteerimine on osa arendusprotsessist."

---

### 4. Toote lühitutvustus (2 minutit)

**Nüüd võite näidata oma toodet, aga fookus on PROTSESSIL:**

**Mida näidata:**
- Lühikirjeldus  
- Wireframed  
- Üks peamine user story demonstratsioonina  
- Kuidas see lahendab kasutajate probleemi (persoonade ja journey map'i jne põhjal)  

**Visuaalid:**
- Persoonad (kes on teie kasutajad?)
- Journey map (kuidas nad toodet kasutavad?)
- Wireframe'id või paberprototüübid

**VÄLTIDA:**
- Liiga palju funktsionaalsuse kirjeldamist
- Tehniliste detailide ülepakkumist
- Keskendumist ainult sellele, MIS teie toode on, mitte KUIDAS te selle lõite

---

### 5. Väljakutsed ja õppetunnid (2-3 minutit)

**Mida esitada:**
- 2-3 peamist väljakutset, millega kokku puutusite
- Kuidas neid lahendasite?
- Mida õppisite vigadest? Millised vead olid?

**Näited:**

**Väljakutse 1: Scope creep**
- **Probleem:** Sprint 2 planeerides võtsime liiga palju user story-sid
- **Lahendus:** Õppisime MoSCoW prioritiseerimist ja viisime "Could have" story-d järgmisse sprinti
- **Õppetund:** Fokusseerimine on oluline, ei saa kõike korraga teha

**Väljakutse 2: Kommunikatsioon**
- **Probleem:** Meeskonnaliige ei teadnud, et teine liige vajab tema tööd
- **Lahendus:** Hakkasime asünkroonseid standup'e kirjutama ja dependency-sid märkima
- **Õppetund:** Transparentsus ja regulaarne kommunikatsioon vältivad blocker'eid

**Väljakutse 3: Estimating**
- **Probleem:** Hindasime task'e liiga optimistlikult (2 SP asemel 5 SP)
- **Lahendus:** Kasutasime planning poker'it ja arutlesime meeskonnaga
- **Õppetund:** Kollektiivne hindamine on täpsem kui individuaalne

---

### 6. Refleksioon (1-2 minutit)

**Mida esitada:**
- Mis muutus teie arusaamises tarkvaraarendusest?
- Mida võtate kaasa tulevastesse projektidesse?
- Mis üllattas teid kõige rohkem?

---

### 7. Kokkuvõte ja küsimused (1 minut)

**Mida esitada:**
- Kokkuvõte kolmest peamisest õppetunnist
- Küsimused-vastused

---
