# Eksami esitlus: Sissejuhatus tarkvaraarendusse

## Esitluse struktuur ja juhised

**Eesmärk:** Esitleda mida õppisite tarkvaraarenduse kohta läbi kolme sprindi, mitte ainult seda, mida teie toode teeb.

**Kestus:** 10-15 minutit + 5 minutit küsimused

**Hindamiskriteeriumid:**
- Arusaam tarkvaraarenduse protsessist (40%)
- Meeskonnatöö ja rollide mõistmine (30%)
- Õpitud metoodikate rakendamine (20%)
- Refleksioon ja kriitilisus (10%)

---

## Esitluse struktuur

### 1. Sissejuhatus (1-2 minutit)

**Mis esitada:**
- Meeskonna nimi ja liikmed
- Lühike ülevaade projektist (1 lause: mis probleemi lahendasite?)
- Esitluse ülesehitus

**Näide:**
> "Oleme meeskond X ja meie projekt oli Y probleem. Täna räägime sellest, kuidas me õppisid tarkvaraarenduse protsessi läbi kolme sprindi - uurimisest planeerimiseni ja arenduseni."

---

### 2. Protsessi ülevaade (2-3 minutit)

**Mis esitada:**
- Kolme sprindi ülevaade
- Mis oli iga sprindi eesmärk?
- Kuidas sprintid omavahel seostusid?

**Soovitatud visuaal:**
```
Sprint 1: UURIMINE → Sprint 2: PLANEERIMINE → Sprint 3: ARENDAMINE
    ↓                      ↓                        ↓
Probleemi             Meeskonnatöö            Epic breakdown
mõistmine            seadistamine             ja simuleerimine
Kasutajad            Rollide jaotus           Daily standups
Nõuded               Backlog                  Blockerid
```

**Fookus tarkvaraarendusel:**
- Miks algab arendus alati probleemi mõistmisest?
- Kuidas iga sprint ehitas eelmise peale?
- Mis oleks juhtunud, kui otse koodimist alustasite?

---

### 3. Õpitud põhimõtted (3-4 minutit)

**Valige 3-4 kõige olulisemat õppetundi ja esitlege neid:**

#### Näide 1: Kasutajakesksus

**Mis õppisime:**
- Probleemi defineerimine enne lahenduse leidmist
- Kasutajate intervjueerimine ja personad
- Journey mapping ja valupunktide leidmine

**Kuidas rakendusime:**
- Sprint 1: intervjueerisime X kasutajat
- Lõime Y personat põhinedes reaalsete andmete põhjal
- Avastasime, et meie algne eeldus oli vale: [näide]

**Mida see meile õpetas:**
> "Õppisime, et ilma kasutajaid mõistmata võib ehitada täiesti vale lahenduse."

#### Näide 2: Meeskonnatöö ja rollid

**Mis õppisime:**
- Scrum rollid: Product Owner, Project Manager, Developer, UX/UI Designer
- Iga rolli vastutus ja panus
- Kommunikatsiooni olulisus (daily standups, retrospectives)

**Kuidas rakendusime:**
- Jaotasime rollid vastavalt huvile ja oskustele
- Pidime X daily standup'i
- Kohtasime Y blocker'it ja lahendasime neid meeskonnana

**Mida see meile õpetas:**
> "Õppisime, et tarkvaraarendus on meeskonnatöö, mitte üksiku programmeerija töö."

#### Näide 3: Agiilne metoodika

**Mis õppisime:**
- Sprint tsükkel: planning → daily standups → review → retrospective
- Iteratiivne vs lineaarne (Waterfall) lähenemine
- Velocity ja burndown chart'i kasutamine

**Kuidas rakendusime:**
- Iga sprint lõppes review ja retrospective'iga
- Sprint 3 simulatsioon näitas, kuidas blocker'id mõjutavad velocity't
- Õppisime oma estimating'ut parandama

**Mida see meile õpetas:**
> "Õppisime, et paindlikkus ja pidev tagasiside on olulisemad kui täiuslik algne plaan."

#### Näide 4: Dokumenteerimine ja GitHub workflow

**Mis õppisime:**
- Git branching ja pull request workflow
- Dokumenteerimine kui osa tarkvarast
- Issue tracking ja project management GitHub'is

**Kuidas rakendusime:**
- Igal dokumendil oli branch → PR → review → merge
- Lõime X issue'd ja Y pull request'i
- GitHub Projects aitas visualiseerida progressi

**Mida see meile õpetas:**
> "Õppisime, et versioonihaldus ja dokumenteerimine ei ole järelmõte, vaid osa arendusprotsessist."

---

### 4. Toote lühitutvustus (2 minutit)

**Nüüd võite näidata oma toodet, aga fookus on PROTSESSIL:**

**Mis näidata:**
- Wireframe'id või prototüübid (mitte ainult kirjeldus)
- Üks peamine user story demonstratsioonina
- Kuidas see lahendab kasutajate probleemi (personade ja journey map'i põhjal)

**Visuaalid:**
- Personad (kes on teie kasutajad?)
- Journey map (kuidas nad toodet kasutavad?)
- Wireframe'id või paberprototüübid

**VÄLTIDA:**
- Liiga palju funktsionaalsuse kirjeldamist
- Tehniliste detailide ülepakkumist
- Keskendumist ainult sellele, MIS teie toode on, mitte KUIDAS te selle lõite

---

### 5. Väljakutsed ja õppetunnid (2-3 minutit)

**Mis esitada:**
- 2-3 peamist väljakutset, millega kokku puutusite
- Kuidas neid lahendasite?
- Mida õppisite vigadest?

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

**Mis esitada:**
- Mis muutus teie arusaamises tarkvaraarendusest?
- Mida võtate kaasa tulevastesse projektidesse?
- Mis üllattas teid kõige rohkem?

**Näited:**

> "Alguses arvasin, et tarkvaraarendus on põhiliselt koodimine. Nüüd saan aru, et see on terve protsess alates probleemi mõistmisest kuni kasutajate testimiseni. Programmeerimine on ainult üks etapp."

> "Õppisime, et dokumenteerimine ei ole igav kohustus, vaid oluline suhtlusvahend meeskonna vahel. GitHub workflow aitas hoida kõiki kursis."

> "Meile meeldis enim sprint retrospective, kus saime ausalt rääkida, mis läks hästi ja mis mitte. See kultuur - õppida vigadest ja pidevalt pareneda - on see, mis eristab häid meeskondi."

---

### 7. Kokkuvõte ja küsimused (1 minut)

**Mis esitada:**
- Kokkuvõte kolmest peamisest õppetunnist
- Täname kuulamast
- Küsimused-vastused

**Näide:**
> "Kokkuvõtteks: õppisime, et tarkvaraarendus algab kasutajatest, nõuab meeskonnatööd ja paindlikku protsessi. Need põhimõtted on aluseks igale edukale projektile."

---

## Visuaalide soovitused

### Must-have slaidid:
1. **Tiitelleht**: meeskond, projekt, kuupäev
2. **Protsessi ülevaade**: 3 sprinti visualiseeritud
3. **Personad**: 1-2 personat piltide ja detailidega
4. **Journey map**: kasutajateekond visualiseeritud
5. **Wireframe'id**: 2-3 ekraani näidet
6. **Retrospective**: Start-Stop-Continue kokkuvõte
7. **Õppetunnid**: 3-4 peamist põhimõtet

### Nice-to-have slaidid:
- GitHub Projects board (kanban või backlog view)
- Burndown chart Sprint 3 simulatsioonist
- Konkurentsianalüüsi võrdlus
- Epic breakdown näide
- Sprint velocity graafik

---

## Näpunäited

### Tehke:
✅ Rääkige protsessist, mitte ainult tootest
✅ Kasutage konkreetseid näiteid oma projektist
✅ Näidake refleksiooni ja õppimist
✅ Visuaalne materjal aitab jutustamist
✅ Jagage esitluse osad meeskonnaliikmete vahel
✅ Harjutage enne

### Ärge:
❌ Loetlege kõiki funktsioone, mida teie toode peaks omama
❌ Süvenege tehnilisse žargooni ilma selgitamata
❌ Keskenduge ainult tootele, mitte õppimisele
❌ Lubage ühel inimesel kogu esitlust teha
❌ Unustage ajapiiranguid (10-15 min!)

---

## Hindamise rubriik (teadmiseks)

### Tarkvaraarenduse protsessi mõistmine (40%)
- Kas mõistavad, miks iga sprint oli vajalik?
- Kas näevad seost uurimise, planeerimise ja arenduse vahel?
- Kas oskavad selgitada agiilse metoodika põhimõtteid?

### Meeskonnatöö ja rollid (30%)
- Kas mõistavad erinevate rollide vastutust?
- Kas näitavad head kommunikatsiooni ja koostööd?
- Kas oskavad kirjeldada blocker'ite lahendamist?

### Metoodikate rakendamine (20%)
- Kas kasutasid personasid, journey map'i, user story-sid?
- Kas rakendasid GitHub workflow'i korrektselt?
- Kas dokumenteerisid protsessi struktureeritult?

### Refleksioon ja kriitilisus (10%)
- Kas tunnistavad vigu ja väljakutseid?
- Kas näitavad õppimist ja arengut?
- Kas oskavad kriitiliselt hinnata oma tööd?

---

## Küsimused, milleks valmis olla

### Protsessi kohta:
- Miks alustasite kasutajate uurimisega?
- Kuidas sprint retrospective aitas teil pareneda?
- Mis oleks teistmoodi, kui kasutaksite Waterfall mudelit?

### Meeskonnatöö kohta:
- Kuidas jaotas rollid meeskonnas?
- Kuidas lahendasite konflikte või erimeelsusi?
- Mis oli kõige keerulisem meeskonnatöö aspekt?

### Metoodikate kohta:
- Kuidas personad mõjutasid teie disainiotsuseid?
- Miks kasutasite story points'e aja asemel?
- Kuidas GitHub Projects aitas teil projekti hallata?

### Toote kohta:
- Kuidas teate, et teie lahendus vastab kasutajate vajadustele?
- Milliseid kompromisse tegite prioritiseerimisel?
- Mis oleksid järgmised sammud toote arendamisel?

---

## Kokkuvõte

Teie esitlus peaks jutustama lugu:
1. **Algus:** Probleem, mida soovisime lahendada
2. **Teekond:** Kuidas õppisime protsessi, meeskonnatööd ja metoodikaid
3. **Tulemus:** Mida saavutasime ja mida õppisime
4. **Tulevik:** Mida võtame kaasa järgmistesse projektidesse

**Peamine sõnum:**
> Tarkvaraarendus on rohkem kui koodimine - see on kasutajate mõistmine, meeskonnatöö, protsess ja pidev õppimine.

Edu eksamil!
