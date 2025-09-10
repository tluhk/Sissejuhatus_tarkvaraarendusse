# Seminar 4: disainimine - kasutajaliidese kavandamine ja prototüüpimine

**Kestus**: 3h (90 min teooria + 90 min praktikat)  
**Fookus**: arendusprotsessi 3. etapp - kasutajaliidese ja kasutajakogemuse disainimine

## Eesmärgid
Kursuse lõpus tudeng:
- Mõistab design thinking metoodikat ja selle rakendamist
- Oskab luua persoonasid uurimistulemuste põhjal
- Oskab kirjutada kvaliteetseid kasutajalugusid
- Oskab kavandada ja luua paberprototüüpe
- Mõistab kasutaja teekonna kaardistamise tähtsust
- Oskab testida prototüüpe kasutajatega

---

## OSA 1: TEOORIA (90 minutit)

### 1.1 Design thinking metoodika (25 min)

#### Design thinking ülevaade (10 min)
**Definitsioon**: Inimesekeskne lähenemine innovatsioonile, mis integreerib inimeste vajadused, tehnoloogia võimalused ja äri nõudmised.

**5 etapit**:
1. **Empaatia (Empathize)**: Kasutajate mõistmine
2. **Defineerimine (Define)**: Probleemi selge formuleerimine  
3. **Ideation**: Lahenduste genereerimine
4. **Prototüüpimine (Prototype)**: Kiired, odavad testversioonid
5. **Testimine (Test)**: Kasutajatega valideerimine

#### Double Diamond protsess (8 min)
```
    DISCOVER  |  DEFINE   |  DEVELOP  |  DELIVER
       /\     |    \/     |    /\     |    \/
      /  \    |   /  \    |   /  \    |   /  \
Divergent -> Convergent -> Divergent -> Convergent
```

**Esimene teemant**: Õige probleemi leidmine
- **Discover**: Laia uurimine, mitmete võimaluste kaardistamine
- **Define**: Fookuse leidmine, konkreetse probleemi valimine

**Teine teemant**: Õige lahenduse leidmine  
- **Develop**: Mitmete lahenduste genereerimine ja katsetamine
- **Deliver**: Parima lahenduse valjemine ja ellurakendamine

#### Human-Centered Design põhimõtted (7 min)
- **Inimesed esimeses kohas**: Tehnoloogia teenib inimesi, mitte vastupidi
- **Konteksti mõistmine**: Kus, millal ja kuidas inimesed toodet kasutavad
- **Iteratiivne protsess**: Jätkuv tagasiside ja parandamine
- **Multidistsiplinaarne koostöö**: Erinevad vaatenurgad ja oskused
- **Empaatia**: Kasutajate emotsioonide ja motivatsiooni mõistmine

### 1.2 Persoonade loomine (20 min)

#### Mis on persoona? (5 min)
**Definitsioon**: Persoona on fiktiivsne karakter, mis esindab reaalset kasutajagruppi ja on loodud kasutajauuringute tulemuste põhjal.

**Persoona eesmärk**:
- Aitab meeskonnal keskenduda konkreetse kasutaja vajadustele
- Teeb otsuste tegemise lihtsamaks ("Kas Mari kasutaks seda funktsiooni?")
- Loob ühise arusaama kasutajatest
- Aitab vältida iseenda projekteerimist

#### Persoona elemendid (10 min)
**Põhiinfo**:
- Nimi ja pilt (aitab meeldejätta)
- Vanus, elukutse, haridus
- Tehnika kogemus ja oskused

**Kontekst ja keskkond**:
- Kus ja millal toodet kasutab
- Millised seadmed ja tehnoloogiad
- Ajaline koormus ja stress

**Eesmärgid ja motivatsioon**:
- Miks tahab toodet kasutada
- Millised on tema peamised eesmärgid
- Mis teda motiveerib või demotiveerib

**Frustatsioonid ja takistused**:
- Mis teda praegu segab
- Millised on tema peamised väljakutsed
- Milliseid vigu ei tohi teha

**Käitumismustrid**:
- Kuidas tavaliselt uusi tööriistasid omaks võtab
- Kui palju aega investeerib õppimisse
- Kas eelistab kiireid lahendusi või põhjalikku uurimist

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
"Kui [kasutaja tüüp], siis soovin ma [eesmärk/funktsioon], et [kasutaja väärtus/põhjus]."
```

**Näited**:
- "Kui tudeng, siis soovin ma näha kõiki oma kodutöid ühes kalendris, et ma ei unustaks ühtegi tähtaega."
- "Kui õppejõud, siis soovin ma saada ülevaadet tudengite progressist, et ma saaksin õigeaegselt abi pakkuda."

#### INVEST kriteeriumid (7 min)
Hea user story peab olema:

**I - Independent**: Sõltumatu teistest user story-dest  
**N - Negotiable**: Läbirääkitav, mitte fikseeritud spetsifikatsioon  
**V - Valuable**: Väärtuslik kasutaja või äri jaoks  
**E - Estimable**: Hinnatav - saab anda tööle mahuhinnagu  
**S - Small**: Piisavalt väike, et mahuks ühte sprint-i  
**T - Testable**: Testitav - saab kontrollida, kas on valmis  

#### Acceptance criteria (5 min)
**Definitsioon**: Tingimused, mis peavad olema täidetud, et user story oleks "valmis".

**Näide**:
```
USER STORY: Kui tudeng, siis soovin näha kõiki tähtaegu kalendrivaates.

ACCEPTANCE CRITERIA:
✅ Kasutaja näeb kõiki kodutöid kronoloogilises järjekorras
✅ Iga ülesande juures on näha tähtaeg ja õppeaine
✅ Võib filtreerida õppeainete kaupa
✅ Näitab ainult aktiivseid (mitte aegunud) ülesandeid
✅ Uuendub automaatselt Moodle-st andmete sünkroonimmisel
```

### 1.4 Kasutajateekond ja stsenaariumid (15 min)

#### Customer Journey Map (8 min)
**Definitsioon**: Visuaalne esitlus kasutaja kogemusest toote või teenusega.

**Elemendid**:
- **Puutepunktid (Touchpoints)**: Kus kasutaja tootega kohtub
- **Tegevused (Actions)**: Mida kasutaja teeb
- **Mõtted (Thoughts)**: Mis kasutaja mõtleb
- **Emotsioonid (Emotions)**: Kuidas kasutaja tunneb
- **Võimalused (Opportunities)**: Kus saab parendada

**Näide lühikesest kasutajateekonnast**:
```
ETAPP 1: Probleem tekib
- Tegevus: Meenutab, et täna on tähtaeg
- Mõtted: "Millal see oli? Kas mul on aega?"
- Emotsioon: 😰 Stress
- Võimalus: Varajane meeldetuletus

ETAPP 2: Otsib infot
- Tegevus: Kontrollib Moodle-t, emaile
- Mõtted: "Kus see info oli?"
- Emotsioon: 😤 Frustratsioon
- Võimalus: Keskne info koht

ETAPP 3: Leiab info
- Tegevus: Leiab ülesande ja tähtaja
- Mõtted: "Õnneks veel aega"
- Emotsioon: 😌 Kergendus
- Võimalus: Parem visualiseerimine
```

#### Stsenaariumide kirjutamine (7 min)
**Definitsioon**: Detailne kirjeldus sellest, kuidas kasutaja konkreetses olukorras tootega suhtleb.

**Stsenaariumi elemendid**:
- **Kontekst**: Kus ja millal
- **Kasutaja**: Kes (viide persoonale)
- **Eesmärk**: Mida tahab saavutada
- **Sammud**: Mida täpselt teeb
- **Tulemus**: Mida saavutab või mitte

**Näide stsenaariumist**:
```
STSENAARIUM: Tähtaja kontrollimine hommikul

KONTEKST: Mari istub trammi Ülemistelt Noblessneri kampusesse
KASUTAJA: Mari Mets (20a, rakendusinformaatika tudeng)
EESMÄRK: Kiire ülevaade päeva kohustustest

SAMMUD:
1. Avab telefonis tähtaegade rakenduse
2. Vaatab päevase vaate
3. Näeb 2 kodutööd: üks täna, teine homme
4. Kontrollib detaile - tänane on juba valmis
5. Lisab homme ülesandele meeldetuletuse õhtul

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

#### Mitte-funktsionaalsed nõuded (5 min)
**Definitsioon**: KUIDAS süsteem käitub - kvaliteedi ja jõudluse nõuded.

**Kategooriad ja näited**:

**Jõudlus**:
- Leht laadib 3 sekundi jooksul
- Toetab kuni 1000 samaegset kasutajat

**Kasutatavus**:
- Uus kasutaja õpib põhifunktsioonid 5 minutiga
- Töötab iOS Safari ja Android Chrome brauserites

**Turvalisus**:
- Parool peab olema vähemalt 8 märki
- Andmed krüpteeritakse ülekandmisel

**Skaleeruvus**:
- Süsteem peab toetama 10x kasutajate kasvu
- Võimalik lisada uusi õppeasutusi

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 minutit)

### 2.1 Persoonade loomine uurimistulemuste põhjal (20 min)

#### Uurimisandmete analüüs
**Aeg**: 5 minutit  
**Ülesanne**: Grupp vaatab üle eelmise kodutöö kasutajauuringute tulemused:
- Millised muutrid esinesid kõige sagedamini?
- Millised on peamised kasutajatüübid?
- Millised on erinevad vajadused ja motivatsioonid?

#### Persoonade töötuba
**Aeg**: 15 minutit  
**Ülesanne**: Iga tudeng (vastavalt oma rollile) loob ühe persoona:

**UX Designer**: Peamine kasutaja (põhiline sihtgrupp)  
**Product Owner**: Äriline kasutaja (kes otsustab ostu/kasutamise)  
**Technical Lead**: "Power user" (intensiivse kasutaja)  
**QA Lead**: "Edge case" kasutaja (erilised vajadused)  

**Template kasutamine**:
```markdown
# PERSOONA NIMI

"Quote - kasutaja peamine motivatsioon"

## Taustainfo
- Vanus, elukutse, kogemused

## Kontekst
- Millal, kus, kuidas kasutab

## Eesmärgid
- Mida tahab saavutada

## Frustatsioonid
- Mis teda häirib või takistab

## Käitumine
- Kuidas tehnoloogiaga suhtleb
```

### 2.2 Kasutajalugude töötuba (25 min)

#### Epic-ute ja user story-de hierarhia
**Aeg**: 10 minutit  
**Demonstratsioon**: Kuidas epic jaguneb user story-deks:

```
EPIC: Tähtaegade haldamine
├── USER STORY 1: Tähtaegade vaatamine
├── USER STORY 2: Meeldetuletuste seadistamine  
├── USER STORY 3: Tähtaegade filtreerimine
└── USER STORY 4: Kalendriga sünkroniseerimine
```

#### Kasutajalugude brainstorm
**Aeg**: 15 minutit  
**Ülesanne**: Grupitöö - looge 8-12 user story-t, mis katavad:
- **Core features** (4-5): Põhifunktsioonid, ilma milleta ei toimi
- **Important features** (3-4): Olulised, teevad kogemuse märksa paremaks  
- **Nice-to-have features** (1-3): Meeldivad lisad

**Iga user story kohta**:
1. Kirjutage INVEST kriteeriumite järgi
2. Lisage acceptance criteria (2-4 punkti)
3. Hinnake prioriteeti (Must/Should/Could/Won't)

### 2.3 Paberprototüüpide loomine (35 min)

#### Prototüüpimise põhimõtted
**Aeg**: 5 minutit  
**Põhimõtted**:
- **Kiirus > Täpsus**: Ei pea ilus olema, peab olema arusaadav
- **Fokus funktsioonidele**: Vorm tuleb hiljem
- **Iteratiivne**: Tee kiiresti, testi, paranda
- **Kaasahaarav**: Kõik saavad kaasa rääkida

#### Lo-fi wireframe-ide loomine
**Aeg**: 20 minutit  
**Ülesanne**: Igaüks joonistab 3-5 ekraani:

**Ekraanide jaotus rollidega**:
- **UX Designer**: Peamised user flow'd
- **Product Owner**: Dashboard ja overview ekraanid
- **Technical Lead**: Seadistused ja admin vaated
- **QA Lead**: Error state'd ja edge case'd

**Joonistamise reeglid**:
- Kasuta lihtsa pliiatsit ja paberit
- Tee suured kastid komponentidele
- Kirjuta tekstid väikeses kirjas
- Märgi clickable elemendid selgelt
- Näita navigatsiooni

#### Interaktiivsuse planeerimine
**Aeg**: 10 minutit  
**Ülesanne**: 
- Märgi prototüüpidele nooled üleminekuteks
- Kirjuta lühike kirjeldus, mis toimub klikkidel
- Planeeri kasutaja tee läbi peamiste funktsionode

### 2.4 Kasutajateekonna kaardistamine (10 min)

#### Journey map loomine
**Ülesanne**: Grupp loob visuaalse journey map põhifunktsiooni kohta:

```
ETAPP 1 → ETAPP 2 → ETAPP 3 → ETAPP 4
Tegevus:    Tegevus:    Tegevus:    Tegevus:
Mõtted:     Mõtted:     Mõtted:     Mõtted:
Emotsioon:  Emotsioon:  Emotsioon:  Emotsioon:
Puutepunkt: Puutepunkt: Puutepunkt: Puutepunkt:
Võimalus:   Võimalus:   Võimalus:   Võimalus:
```

**Fookus**: Vali üks põhiline kasutajateekond (näiteks "Esimest korda kasutama hakkamine")

---

## Kodutöö 4: täielik UI/UX disaini dokumentatsioon

### Ülesande kirjeldus
**Tähtaeg**: 1 nädal  
**Vorm**: GitHub repositoorium + individuaalne panus

### Grupi osa
- **Design system document**: Komponendid, värvid, fonts
- **Complete user journey**: 3-4 peamist kasutajateed
- **Integrated prototype**: Kõik ekraanid sidutud vooguks

### Rolli-põhised ülesanded

#### UX Designer
- **3 detailset persoonat**: Kvalitatiivsed ja kvantitatiivsed andmed
- **Complete user journey map**: Journey mapi peamiste kasutamise stsenaariumite kohta
- **Usability testing plan**: Kuidas prototüüpe testida

#### Product Owner  
- **Prioritized backlog**: Kõik user stories prioriteediga ja acceptance criteria
- **Business user stories**: Äriliselt olulised funktsioonid
- **Success metrics definition**: Kuidas edu mõõta

#### Technical Lead
- **Technical user stories**: Arhitektuuri ja jõudluse nõuded
- **System requirements**: Funktsionaalsed ja mitte-funktsionaalsed nõuded
- **Technical feasibility analysis**: Mis on tehniliselt võimalik

#### QA Lead
- **Edge case scenarios**: Erilised kasutamise juhud
- **Error handling design**: Kuidas käsitleda vigu  
- **Testing scenarios**: Test case-id kasutajaliidese jaoks

### Kõik kokku
- **Paper prototype digitization**: Kõik paberprototüübid pildistatud ja dokumenteeritud
- **Interactive flow documentation**: User flows ja click-through scenarios
- **Requirements specification**: Täielik nõuete dokument

### Esitamise vorm
- **GitHub repository**: Täielik disaini dokumentatsioon
- **Role-based contributions**: Iga roll oma eksperte ala
- **Cross-role validation**: Rollide vaheline ülevaatus
- **Integrated deliverable**: Kõik osad töötavad koos

### Hindamise kriteeriumid
- **User-centricity**: Kui hästi on kasutajate vajadused kaetud
- **Consistency**: Kas disain on järjepidev
- **Completeness**: Kas kõik olulised ekraanid on kaetud  
- **Feasibility**: Kas prototüüp on teostatav
- **Documentation quality**: Professionaalsus ja selgus

---

## Materjalid ja ressursid

### Kohustuslik lugemine
- [Design Thinking Bootleg](https://dschool.stanford.edu/resources/design-thinking-bootleg) - Stanford d.school
- [User Story Mapping](https://www.jpattonassociates.com/user-story-mapping/) - Jeff Patton

### Soovituslikud tööriistad
- **Prototype creation**: Paaber + pliiats, telefoni kaamera
- **Digital mockups**: Figma (tasuta), Sketch, Adobe XD
- **Journey mapping**: Miro, Mural
- **Documentation**: Notion, Confluence

### Template failid
- `persona-template.md`
- `user-story-template.md`
- `acceptance-criteria-template.md`
- `journey-map-template.md`
- `prototype-testing-template.md`

### Inspiratsioon ja näited
- [UI Patterns](http://ui-patterns.com/) - tavalisd UI mustrid
- [Mobile Patterns](https://www.mobile-patterns.com/) - mobiili UI näited
- [GoodUI](https://goodui.org/) - kasutajaliidese parimad tavad

---

## Järgmine seminar
**Seminar 5: arendamine** - kuidas disainidokument ja prototüübid muuta arendusülesanneteks ja hallata sprint-e.
