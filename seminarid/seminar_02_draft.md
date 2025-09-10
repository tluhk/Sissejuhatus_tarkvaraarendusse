# Seminar 2: uurimine - probleemi analüüs ja kasutajate mõistmine

**Kestus**: 3h (90 min teooria + 90 min praktikat)  
**Fookus**: arendusprotsessi 1. etapp - probleemi defineerimine ja uurimine

## Eesmärgid
Kursuse lõpus tudeng:
- **Mõistab tarkvaraarenduse olemust** ja selle erinevust programmeerimisest
- Oskab defineerida ja analüüsida probleeme süstemaatiliselt
- Teab erinevaid kasutajauuringute meetodeid
- Oskab eristada funktsionaalseid ja mitte-funktsionaalseid nõudeid
- Oskab dokumenteerida uurimistulemusi professionaalselt
- Mõistab konkurentsianalüüsi tähtsust

---

## OSA 1: TEOORIA (90 minutit)

### 1.1 Mis on tarkvaraarendus? (15 min)

#### Tarkvara definitsioon
**Tarkvara** on juhiste kogum, mis ütleb arvutile, mida teha. See koosneb:
- **Koodist**: Programmeerimiskeeles kirjutatud juhised
- **Andmetest**: Informatsioon, mida tarkvara töötleb
- **Dokumentatsioonist**: Selgitused, kuidas tarkvara töötab ja kasutada

#### Tarkvaraarendus kui protsess
**Tarkvaraarendus** on süstemaatiline lähenemisviis tarkvara loomisele, mis hõlmab:

```
Probleem → Analüüs → Disain → Arendamine → Testimine → Juurutamine → Hooldus
    ↑                                                                      ↓
    └──────────────── Tagasiside ja täiustused ←────────────────────────────┘
```

**Põhietapid**:
1. **Probleemi mõistmine**: Mida me lahendame ja miks?
2. **Nõuete kogumine**: Mida tarkvara peab täpselt tegema?
3. **Disainimine**: Kuidas tarkvara töötab ja välja näeb?
4. **Arendamine**: Koodi kirjutamine ja süsteemi ehitamine
5. **Testimine**: Kas tarkvara töötab õigesti?
6. **Juurutamine**: Tarkvara kasutajatele kättesaadavaks tegemine
7. **Hooldus**: Vigade parandamine ja uute funktsioonide lisamine

#### Miks tarkvaraarendus on oluline?
- **Automatiseerimine**: Korduvate ülesannete automatiseerimine
- **Efektiivsus**: Protsesside kiirendamine ja lihtsustamine
- **Skaleeruvus**: Süsteemid, mis töötavad miljonite kasutajatega
- **Innovatsioon**: Uued võimalused ja lahendused
- **Kommunikatsioon**: Inimeste ühendamine üle kogu maailma

#### Tarkvaraarendus vs programmeerimine
| **Programmeerimine** | **Tarkvaraarendus** |
|---|---|
| Koodi kirjutamine | Kogu protsess probleemist lahenduseni |
| Tehniline oskus | Tehniline + äri + kasutaja mõistmine |
| Individuaalne töö | Meeskonnatöö ja koostöö |
| Lühiajaline | Pikajaline planeerimine ja hooldus |

### 1.2 Probleemi defineerimine (20 min)

#### Mis on "hea" probleem?
- **Selgelt defineeritud**: Konkreetne, mitte üldine
- **Mõõdetav**: Saab hinnata lahenduse edukust
- **Lahendatav**: Tehnilist lahendusvõimalust on olemas
- **Oluline**: Tegelik vajadus kasutajatel või turul

#### Probleemi analüüsi raamistik
```
1. PROBLEEM: Mis täpselt toimub valesti?
2. MÕJU: Kellele ja kuidas see mõjutab?
3. PÕHJUSED: Miks see probleem tekib?
4. KONTEKST: Millistes olukordades esineb?
5. PIIRANGUD: Millised on tehnilised/ressursi/aja piirangud?
```

#### Näited headest ja halbadest probleemi definitsioonidest
**✅ Hea näide**: "Haapsalu kolledži tudengitel on raske jälgida kodutööde tähtaegu, sest info on hajutatud mitmesse süsteemi (Moodle, e-mail, Discord), mistõttu 40% tähtaegadest unustatakse."

**❌ Halb näide**: "Tudengitel on raske õppida."

### 1.2 Kasutajate uurimise meetodid (25 min)

#### Kvalitatiivsed meetodid
- **Intervjuud**: Süvavestlused kasutajatega
  - Struktureeritud vs poolstruktureeritud vs vabad
  - Küsimuste koostamise tehnika
  - Aktiivsne kuulamine
- **Vaatlused**: Kasutajate käitumise jälgimine loomulikus keskkonnas
- **Fookusgrupi arutelud**: Grupidiskussioonid

#### Kvantitatiivsed meetodid
- **Küsitlused**: Suured andmekogumid
- **Analüütika**: Olemasolevate süsteemide kasutusstatistika
- **A/B testimine**: Erinevate lahenduste võrdlus

#### Kombineeritud lähenemised
- **Persona workshops**: Kvalitatiivsete andmete kvantifitseerimine
- **Card sorting**: Informatsiooni arhitektuuri testimine
- **Journey mapping**: Kasutajakogemuse kaardistamine

### 1.3 Nõuete tüübid (20 min)

#### Funktsionaalsed nõuded
- **Definitsioon**: Mida süsteem peab tegema
- **Näited**: 
  - "Kasutaja saab sisse logida e-posti ja parooliga"
  - "Süsteem saadab meeldetuletuse 24h enne tähtaega"
  - "Administraator saab lisada uusi kasutajaid"

#### Mitte-funktsionaalsed nõuded
- **Jõudlus**: Kiirus, läbilaskevõime, vastamisaeg
- **Skaleeruvus**: Kui palju kasutajaid süsteem peab toetama
- **Turvalisus**: Andmekaitse, autentimine, autorisatsioon
- **Kasutatavus**: Lihtne õppimine, intuitiivne kasutamine
- **Ühilduvus**: Toetatud brauserid, seadmed, OS-id
- **Töökindlus**: Uptime, vea taastamise aeg

#### Kvaliteedi kriteeriumid
- **Täpsus**: Nõue peab olema üheselt mõistetav
- **Täielikkus**: Kõik olulised aspektid kaetud
- **Järjepidevus**: Ei tohi olla vastuolulisi nõudeid
- **Teostatavus**: Tehniliselt ja ressursside poolest võimalik

### 1.4 Konkurentsianalüüs (15 min)

#### Miks konkurentsianalüüs on oluline?
- Mõista turu praegust seisu
- Tuvastada parimaid tavasid
- Leida innovatsiooni võimalusi
- Vältida juba tehtud vigu

#### Analüüsi raamistik
```
1. TUVASTAMINE: Kes on peamised konkurendid?
2. FUNKTSIOONID: Mida nad pakuvad?
3. KASUTAJALIIDES: Kuidas nad seda teevad?
4. EELISED: Mis on nende tugevused?
5. PUUDUSED: Kus on lüngad?
6. VÕIMALUSED: Mida saaks paremini teha?
```

### 1.5 Dokumenteerimise head tavad (10 min)

#### Uurimisraporti struktuuri
1. **Kokkuvõte**: Peamised järeldused
2. **Metoodika**: Kuidas uurimus läbi viidi
3. **Tulemused**: Kogutud andmed ja analüüs
4. **Soovitused**: Mida edasi teha
5. **Lisad**: Toetavad materjalid

#### Markdown dokumentatsiooni parimad tavad
- Selged pealkirjad ja struktuur
- Pildid ja diagrammid illustreerimiseks
- Linkid allikatele
- Kokkuvõtvad tabelid
- Version control läbi Git

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 minutit)

### 2.1 Probleemi valimine ja defineerimine (20 min)

#### Grupitöö: probleemi brainstorm
**Aeg**: 10 minutit  
**Ülesanne**: Iga grupp (3-4 tudengit) brainstormib probleeme järgmistest valdkondadest:
- Haridus ja õppimine
- Tudengite igapäevane elu
- Kohalik kogukond
- Keskkond ja jätkusuutlikkus

#### Probleemi evalueerimine ja valik
**Aeg**: 10 minutit  
**Ülesanne**: Kasutades probleemi analüüsi raamistikku, iga grupp:
1. Valib 3 kõige perspektiivsemat probleemi
2. Hindab neid raamistiku järgi
3. Valib ühe probleemi järgmisteks seminariteks

#### Tulemused GitHub-i
- Iga grupp loob oma repositooriumi
- Lisab `problem-definition.md` faili
- Dokumenteerib valitud probleemi

### 2.2 Kasutajate uurimise harjutus (30 min)

#### Intervjuu küsimuste koostamine
**Aeg**: 10 minutit  
**Ülesanne**: Grupp koostab 8-10 küsimust valitud probleemi kohta:
- 2-3 taustküsimust (demograafia, kontekst)
- 4-5 probleemi kohta (kuidas, millal, miks)
- 2-3 lahenduse kohta (mida proovitud, mis aitaks)

#### Rollimäng: kasutajate intervjuu
**Aeg**: 20 minutit  
**Ülesanne**: 
- **Grupid paaristavad**: Üks grupp = intervjueerijad, teine = kasutajad
- **10 min intervjuu**: Praktiline intervjuu läbiviimine
- **Rollide vahetus**: Teine 10 minutit vastupidises rollis
- **Märkmed**: Kõik vastused dokumenteeritakse

### 2.3 Nõuete kogumine ja dokumenteerimine (25 min)

#### Funktsionaalsete nõuete määratlemine
**Aeg**: 15 minutit  
**Ülesanne**: Intervjuu tulemuste põhjal grupp määratleb:
- 5-7 peamist funktsionaalsed nõuet
- Iga nõue vormistatud: "Süsteem peab võimaldama..."
- Prioritiseerimine: Must-have vs Nice-to-have

#### Mitte-funktsionaalsete nõuete tuvastamine
**Aeg**: 10 minutit  
**Ülesanne**: Grupp määratleb:
- Jõudluse nõuded (kui kiire, kui palju kasutajaid)
- Kasutatavuse nõuded (mis seadmed, oskused)
- Turvalisuse nõuded (millised andmed, kes ligipääs)

### 2.4 Konkurentsianalüüs (15 min)

#### Konkurentide tuvastamine ja analüüs
**Ülesanne**: Grupp leiab 2-3 olemasolevat lahendust või konkurenti:
- Otsing Google'ist, app store'idest
- Lühike analüüs iga konkurendi kohta
- Tugevused ja nõrkused
- Võimalused innovatsiooniks

### 2.5 Dokumentatsiooni vormistamine ja esitlus (10 min)

#### GitHub repositooriumi täiendamine
**Ülesanne**: 
- `user-research.md` - intervjuu tulemused
- `requirements.md` - funktsionaalsed ja mitte-funktsionaalsed nõuded
- `competitive-analysis.md` - konkurentide analüüs
- README.md uuendamine projekti kirjeldusega

#### Lühikeesitlused (vabatahtlik aeg lubades)
**Aeg**: 2-3 minutit grupi kohta  
**Sisu**: Probleem + üks huvitav leid uurimusest

---

## Kodutöö 2: süvauurimine valitud probleemi kohta

### Ülesande kirjeldus
**Tähtaeg**: 1 nädal  
**Vorm**: Grupi repositoorium + individuaalne panus

### Grupi osa
- **Probleemi süvaanalüüs**: Täiendavad allikad, statistika
- **Laiendatud kasutajate uurimine**: Vähemalt 3 päris intervjuud
- **Detailne konkurentsianalüüs**: 5+ konkurenti
- **Stakeholder analüüs**: Kes on kõik osapooled?

### Individuaalne osa
Iga tudeng keskendub ühele aspektile (vastavalt huvidele):
- **Kasutajate uurija**: Täiendavad intervjuud ja andmeanalüüs
- **Turu-analüütik**: Konkurendid ja ärimudel
- **Tehnoloogia uurija**: Tehnilised lahendused ja teostatavus
- **Nõuete analüütik**: Detailsed nõuded ja prioritiseerimine

### Esitamise vorm
- **GitHub repositoorium**: Täielik dokumentatsioon
- **Pull request workflow**: Iga tudeng teeb oma osa eraldi branch-is
- **Peer review**: Gruppikaaslaste ülevaatus ja kommentaarid
- **Lõplik merge**: Õpetaja heakskiit

### Hindamise kriteeriumid
- **Põhjalikkus**: Kui sügavalt probleemi uuriti
- **Metodoloogia**: Kas kasutati õigeid uurimismeetodeid
- **Dokumentatsioon**: Selgus ja professionaalsus
- **Koostöö**: GitHub workflow ja peer review kvaliteet

---

## Materjalid ja ressursid

### Kohustuslik lugemine
- [The Mom Test](http://momtestbook.com/) - küsimuste koostamine
- [Jobs to be Done](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) - kasutajate motivatsiooni mõistmine

### Soovituslikud tööriistad
- **Intervjuude salvestamine**: Zoom, Teams (luba küsida!)
- **Märkmete tegemine**: Notion, Obsidian, Markdown
- **Analüüs**: Miro, Figma (tasuta)
- **Küsitlused**: Google Forms, Typeform

### Template failid
- `problem-definition-template.md`
- `interview-questions-template.md`
- `requirements-template.md`
- `competitive-analysis-template.md`

---

## Järgmine seminar
**Seminar 3: planeerimine** - kuidas probleemi ja uurimuste põhjal planeerida projekti ja organiseerida meeskonnatööd.
