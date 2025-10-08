# Seminar 4: disainimine - kasutajaliidese kavandamine ja prototüüpimine

**Kestus**: 3h (90 min teooria + 90 min praktikat)  
**Fookus**: arendusprotsessi 3. etapp - kasutajaliidese ja kasutajakogemuse disainimine

## Eesmärgid
Seminari ja kodutöö järel tudeng:
- mõistab design thinking metoodikat ja selle rakendamist
- loob persoonasid uurimistulemuste põhjal
- kirjutab kvaliteetseid kasutajalugusid
- kavandab ja loob paberprototüüpe
- Mõistab kasutaja teekonna kaardistamise tähtsust
- tstib prototüüpe kasutajatega

---

## OSA 1: TEOORIA (90 minutit)

### 1.1 Design thinking metoodika (25 min)

#### Design thinking ülevaade (10 min)
**Definitsioon**: inimesekeskne lähenemine innovatsioonile, mis integreerib inimeste vajadused, tehnoloogia võimalused ja äri nõudmised.

**5 etapit**:
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
- **Deliver**: parima lahenduse valjemine ja ellurakendamine

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

ACCEPTANCE CRITERIA/VASTUVÕTMISE KRITEERIUMID:
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

KONTEKST: Mari istub trammi Ülemistelt Noblessneri kampusesse
KASUTAJA: Mari Mets (20a, rakendusinformaatika tudeng)
EESMÄRK: kiire ülevaade päeva kohustustest

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

### 2.1 Persoonade loomine uurimistulemuste põhjal (20 min)

#### Uurimisandmete analüüs
**Aeg**: 5 minutit  
**Ülesanne**: Grupp vaatab üle eelnenud kodutöö kasutajauuringute tulemused:
- millised mustrid esinesid kõige sagedamini?
- millised on peamised kasutajatüübid?
- millised on erinevad vajadused ja motivatsioonid?

#### Persoonade töötuba
**Aeg**: 15 minutit  
**Ülesanne**: iga tudeng (vastavalt oma rollile) loob ühe persoona:

**UX Designer**: peamine kasutaja (põhiline sihtgrupp)  
**Product Owner**: äriline kasutaja (kes otsustab ostu/kasutamise)  
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
**Ülesanne**: grupitöö - looge 8-12 user story-t, mis katavad:
- **Core features** (4-5): põhifunktsioonid, ilma milleta ei toimi
- **Important features** (3-4): olulised, teevad kogemuse märksa paremaks  
- **Nice-to-have features** (1-3): meeldivad lisad

**Iga user story kohta**:
1. kirjutage INVEST kriteeriumite järgi
2. lisage acceptance criteria (2-4 punkti)
3. hinnake prioriteeti (Must/Should/Could/Won't)

### 2.3 Paberprototüüpide loomine (35 min)

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
- **Technical Lead**: seadistused ja admin vaated
- **QA Lead**: Error state'd ja edge case'd

**Joonistamise reeglid**:
- kasuta lihtsa pliiatsit ja paberit
- tee suured kastid komponentidele
- kirjuta tekstid väikeses kirjas
- märgi clickable elemendid selgelt
- näita navigatsiooni

#### Interaktiivsuse planeerimine
**Aeg**: 10 minutit  
**Ülesanne**: 
- märgi prototüüpidele nooled üleminekuteks
- kirjuta lühike kirjeldus, mis toimub klikkidel
- planeeri kasutaja tee läbi peamiste funktsionode

### 2.4 Kasutajateekonna kaardistamine (10 min)

#### Journey map loomine
**Ülesanne**: grupp loob visuaalse journey map põhifunktsiooni kohta:

```
ETAPP 1 → ETAPP 2 → ETAPP 3 → ETAPP 4
Tegevus:    Tegevus:    Tegevus:    Tegevus:
Mõtted:     Mõtted:     Mõtted:     Mõtted:
Emotsioon:  Emotsioon:  Emotsioon:  Emotsioon:
Puutepunkt: Puutepunkt: Puutepunkt: Puutepunkt:
Võimalus:   Võimalus:   Võimalus:   Võimalus:
```

**Fookus**: vali üks põhiline kasutajateekond (näiteks "Esimest korda kasutama hakkamine")

---

## Kodutöö 4: täielik UI/UX disaini dokumentatsioon

### Ülesande kirjeldus
**Tähtaeg**: järgmise seminarinädala esmaspäeva hommik  
**Vorm**: GitHub repositoorium + individuaalne panus

### Grupi osa
- **Design system document**: komponendid, värvid, fonts
- **Complete user journey**: 3-4 peamist kasutajateed
- **Integrated prototype**: kõik ekraanid sidutud vooks

### Rolli-põhised ülesanded

#### UX Designer
- **3 detailset persoonat**: kvalitatiivsed ja kvantitatiivsed andmed
- **Complete user journey map**: Journey mapi peamiste kasutamise stsenaariumite kohta
- **Usability testing plan**: kuidas prototüüpe testida

#### Product Owner  
- **Prioritized backlog**: kõik user stories prioriteediga ja acceptance criteria
- **Business user stories**: äriliselt olulised funktsioonid
- **Success metrics definition**: kuidas edu mõõta

#### Technical Lead
- **Technical user stories**: arhitektuuri ja jõudluse nõuded
- **System requirements**: funktsionaalsed ja mitte-funktsionaalsed nõuded
- **Technical feasibility analysis**: mis on tehniliselt võimalik

#### QA Lead
- **Edge case scenarios**: erilised kasutamise juhud
- **Error handling design**: kuidas käsitleda vigu  
- **Testing scenarios**: test case-id kasutajaliidese jaoks

### Kõik kokku
- **Paper prototype digitization**: kõik paberprototüübid pildistatud ja dokumenteeritud
- **Interactive flow documentation**: User flows ja click-through scenarios
- **Requirements specification**: täielik nõuete dokument

### Esitamise vorm
- **GitHub repository**: täielik disaini dokumentatsioon
- **Role-based contributions**: iga roll oma eksperte ala
- **Cross-role validation**: rollide vaheline ülevaatus
- **Integrated deliverable**: kõik osad töötavad koos

### Hindamise kriteeriumid
- **User-centricity**: kui hästi on kasutajate vajadused kaetud
- **Consistency**: kas disain on järjepidev
- **Completeness**: kas kõik olulised ekraanid on kaetud  
- **Feasibility**: kas prototüüp on teostatav
- **Documentation quality**: professionaalsus ja selgus

---

## Materjalid ja ressursid

### Kohustuslik lugemine
- [Design Thinking Bootleg](https://dschool.stanford.edu/resources/design-thinking-bootleg) - Stanford d.school
- [User Story Mapping](https://www.jpattonassociates.com/user-story-mapping/) - Jeff Patton

### Soovituslikud tööriistad
- **Prototype creation**: paber + pliiats, telefoni kaamera
- **Digital mockups**: Figma (tasuta), Sketch, Adobe XD
- **Journey mapping**: Figjam, Miro, Mural
- **Documentation**: Github, markdown failid

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
