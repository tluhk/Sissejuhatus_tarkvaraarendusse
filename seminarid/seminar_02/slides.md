---
marp: true
theme: default
paginate: true
header: 'Sissejuhatus tarkvaraarendusse'
footer: 'Seminar 2: Uurimine - probleemi analüüs ja kasutajate mõistmine'
---

# Tagasiside esimesele seminarile
## Millised olid probleemid?
- Kas markdown sai selgeks?
- Kas git ja github on arusaadav?

NB! Esimsele semestril on täitsa ok kasutada GH Desktoppi. Ärge tekitage endas pinget terminaliga.
NB! NB! Ärge kasutage Githubi koodimuudatuste tegemise võimalust veebis! Vaid erandjuhtudel kui kindlalt teate, mida teete.

---

# Seminar 2: Uurimine
## Probleemi analüüs ja kasutajate mõistmine

**Kestus**: 3h (90 min teooria + 90 min praktikat)  
**Fookus**: arendusprotsessi esimene etapp - probleemi defineerimine ja uurimine

---

## Tänased eesmärgid 🎯

- ✅ **Mõista tarkvaraarenduse olemust**
- ✅ Defineerida ja analüüsida probleeme süstemaatiliselt
- ✅ Kasutada erinevaid kasutajauuringute meetodeid
- ✅ Eristada funktsionaalseid ja mitte-funktsionaalseid nõudeid
- ✅ Dokumenteerida uurimistulemusi professionaalselt
- ✅ Mõista konkurentsianalüüsi tähtsust

---

## OSA 1: TEOORIA (90 min)

### 1.1 Mis on tarkvaraarendus? 🤔
### 1.2 Probleemi defineerimine 🎯
### 1.3 Kasutajate uurimise meetodid 👥
### 1.4 Nõuete tüübid 📋
### 1.5 Konkurentsianalüüs 🔍

---

## 1.1 Mis on tarkvaraarendus?

### Tarkvara definitsioon
**Tarkvara** = juhiste kogum, mis ütleb arvutile, mida teha

📦 **Koosneb kolmest osast:**
- **Koodist**: Programmeerimiskeeles kirjutatud juhised
- **Andmetest**: Informatsioon, mida tarkvara töötleb  
- **Dokumentatsioonist**: Selgitused, kuidas töötab ja kasutada

---

## Tarkvaraarendus kui protsess

```
Probleem → Analüüs → Disain → Arendamine → Testimine → Juurutamine → Hooldus
    ↑                                                                      ↓
    └──────────────── Tagasiside ja täiustused ←────────────────────────────┘
```

**Süstemaatiline lähenemisviis** tarkvara loomisele

---

## Tarkvaraarenduse põhietapid

1. **🔍 Probleemi mõistmine**: Mida me lahendame ja miks?
2. **📝 Nõuete kogumine**: Mida tarkvara peab täpselt tegema?
3. **🎨 Disainimine**: Kuidas tarkvara töötab ja välja näeb?
4. **⚙️ Arendamine**: Koodi kirjutamine ja süsteemi ehitamine
5. **🧪 Testimine**: Kas tarkvara töötab õigesti?
6. **🚀 Juurutamine**: Tarkvara kasutajatele kättesaadavaks tegemine
7. **🔧 Hooldus**: Vigade parandamine ja uute funktsioonide lisamine

---

## Miks tarkvaraarendus on oluline?

- 🤖 **Automatiseerimine**: Korduvate ülesannete automatiseerimine
- ⚡ **Efektiivsus**: Protsesside kiirendamine ja lihtsustamine
- 📈 **Skaleeruvus**: Süsteemid, mis töötavad miljonite kasutajatega
- 💡 **Innovatsioon**: Uued võimalused ja lahendused
- 🌐 **Kommunikatsioon**: Inimeste ühendamine üle kogu maailma

---

## Tarkvaraarendus vs programmeerimine

| **Programmeerimine** | **Tarkvaraarendus** |
|---|---|
| Koodi kirjutamine | Kogu protsess probleemist lahenduseni |
| Tehniline oskus | Tehniline + äri + kasutaja mõistmine |
| Individuaalne töö | Meeskonnatöö ja koostöö |
| Lühiajaline | Pikajaline planeerimine ja hooldus |

**💡 Programmeerimine on ainult üks osa tarkvaraarendusest!**

---

## 1.2 Probleemi defineerimine

---

### Mis on "hea" probleem? 🎯

- ✅ **Selgelt defineeritud**: Konkreetne, mitte üldine
- ✅ **Mõõdetav**: Saab hinnata lahenduse edukust
- ✅ **Lahendatav**: Tehnilist lahendusvõimalust on olemas
- ✅ **Oluline**: Tegelik vajadus kasutajatel või turul

---

## Probleemi analüüsi raamistik

```
1. PROBLEEM: Mis täpselt toimub valesti?
2. MÕJU: Kellele ja kuidas see mõjub?
3. PÕHJUSED: Miks see probleem tekib?
4. KONTEKST: Millistes olukordades esineb?
5. PIIRANGUD: Millised on tehnilised/ressursi/aja piirangud?
```

---

## Näited: hea vs halb probleemi definitsioon

### ✅ **Hea näide**:
*"Haapsalu kolledži tudengitel on raske jälgida kodutööde tähtaegu, sest info on hajutatud mitmesse süsteemi (Moodle, e-mail, Discord), mistõttu 40% tähtaegadest unustatakse."*

### ❌ **Halb näide**:
*"Tudengitel on raske õppida."*

**🤔 Mis teeb esimese näite paremaks?**

---

## 1.3 Kasutajate uurimise meetodid

### Kvalitatiivsed meetodid 🗣️

- **Intervjuud**: Süvavestlused kasutajatega
  - Struktureeritud vs poolstruktureeritud vs vabad
  - Küsimuste koostamise tehnika
  - Aktiivne kuulamine
- **Vaatlused**: Kasutajate käitumise jälgimine loomulikus keskkonnas
- **Fookusgrupi arutelud**: Grupidiskussioonid

---

## Kvantitatiivsed meetodid 📊

- **Küsitlused**: Suured andmekogumid
- **Analüütika**: Olemasolevate süsteemide kasutusstatistika
- **A/B testimine**: Erinevate lahenduste võrdlus

### Kombineeritud lähenemised 🔄
- **Persona workshops**: Kvalitatiivsete andmete kvantifitseerimine
- **Card sorting**: Informatsiooni arhitektuuri testimine
- **Journey mapping**: Kasutajakogemuse kaardistamine

---

## 1.4 Nõuete tüübid

### Funktsionaalsed nõuded ⚙️
**Definitsioon**: Mida süsteem peab tegema

**Näited**: 
- "Kasutaja saab sisse logida e-posti ja parooliga"
- "Süsteem saadab meeldetuletuse 24h enne tähtaega"
- "Administraator saab lisada uusi kasutajaid"

---

### Mitte-funktsionaalsed nõuded 🔧

- **Jõudlus**: Kiirus, läbilaskevõime, vastamisaeg
- **Skaleeruvus**: Kui palju kasutajaid süsteem peab toetama
- **Turvalisus**: Andmekaitse, autentimine, autorisatsioon
- **Kasutatavus**: Lihtne õppimine, intuitiivne kasutamine
- **Ühilduvus**: Toetatud brauserid, seadmed, OS-id
- **Töökindlus**: Uptime, vea taastamise aeg

---

## Kvaliteedi kriteeriumid ✅

- **Täpsus**: Nõue peab olema üheselt mõistetav
- **Täielikkus**: Kõik olulised aspektid kaetud
- **Järjepidevus**: Ei tohi olla vastuolulisi nõudeid
- **Teostatavus**: Tehniliselt ja ressursside poolest võimalik

---

## 1.5 Konkurentsianalüüs

---

### Miks konkurentsianalüüs on oluline? 🤔

- 📊 Mõista turu praegust seisu
- ⭐ Tuvastada parimaid tavasid
- 💡 Leida innovatsiooni võimalusi
- ⚠️ Vältida juba tehtud vigu

---

## Konkurentsianalüüsi raamistik

```
1. TUVASTAMINE: Kes on peamised konkurendid?
2. FUNKTSIOONID: Mida nad pakuvad?
3. KASUTAJALIIDES: Kuidas nad seda teevad?
4. EELISED: Mis on nende tugevused?
5. PUUDUSED: Kus on lüngad?
6. VÕIMALUSED: Mida saaks paremini teha?
```

---

## Dokumenteerimise head tavad 📝

### Uurimisraporti struktuur:
1. **Kokkuvõte**: Peamised järeldused
2. **Metoodika**: Kuidas uurimus läbi viidi
3. **Tulemused**: Kogutud andmed ja analüüs
4. **Soovitused**: Mida edasi teha
5. **Lisad**: Toetavad materjalid

---

### Markdown parimad tavad:
- Selged pealkirjad ja struktuur
- Pildid ja diagrammid illustreerimiseks
- Linkid allikatele
- Versioonihaldus läbi Giti

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 min)

### 2.1 Probleemi valimine ja defineerimine (20 min)
### 2.2 Kasutajate uurimise harjutus (30 min)
### 2.3 Nõuete kogumine (25 min)
### 2.4 Konkurentsianalüüs (15 min)
Praktiline töötuba on ettevalmistus kodutööks

---

## 2.1 Probleemi valimine ja defineerimine

### Grupitöö: probleemi ajurünnak 🧠
**Aeg**: 10 minutit  
**Valdkonnad**:
- 🎓 Haridus ja õppimine
- 👨‍🎓 Tudengite igapäevane elu (nt toitlustus)
- 🏘️ Kohalik kogukond
- 🌱 Keskkond ja jätkusuutlikkus

---

### Probleemi evalueerimine 📊
**Aeg**: 10 minutit  
Kasutades probleemi analüüsi raamistikku (slide 11)

---

## 2.2 Kasutajate uurimise harjutus

### Intervjuu küsimuste koostamine 📝
**Aeg**: 10 minutit  

- 2-3 taustküsimust (demograafia, kontekst)
- 4-5 probleemi kohta (kuidas, millal, miks)
- 2-3 lahenduse kohta (mida proovitud, mis aitaks)

### Rollimäng: kasutajate intervjuu 🎭
**Aeg**: 20 minutit  
Grupid modustavad paarid ja vahetavad rolle!

---

## 2.3 Nõuete kogumine

### Funktsionaalsed nõuded ⚙️
**Aeg**: 15 minutit  
- 5-7 peamist funktsionaalsed nõuet
- Vorm: "Süsteem peab võimaldama..."
- Prioritiseerimine: Must-have vs Nice-to-have

---

### Mitte-funktsionaalsed nõuded 🔧
**Aeg**: 10 minutit  
- Jõudluse nõuded (kiirus, kasutajate arv)
- Kasutatavuse nõuded (seadmed, oskused)
- Turvalisuse nõuded (andmed, ligipääs)

---

## 2.4 Konkurentsianalüüs

**Aeg**: 15 minutit  

**Ülesanne**: Leidke 2-3 olemasolevat lahendust
- 🔍 Otsing Google'ist, app store'idest
- 📊 Lühike analüüs iga konkurendi kohta
- ⚖️ Tugevused ja nõrkused
- 💡 Võimalused innovatsiooniks

---

## GitHub dokumentatsioon 📁

### Täna loome:
- `problem-definition.md` - valitud probleem
- `user-research.md` - intervjuu tulemused
- `product-description.md` - toote kirjeldus
- `requirements.md` - funktsionaalsed ja mitte-funktsionaalsed nõuded
    **Näidised funktsionaalsetest nõuetest:**
    - Kasutaja peab saama lisada uue kodutöö.
    - Süsteem peab saatma meeldetuletusi tähtaegade kohta.
    - Kasutaja peab saama vaadata kõiki varasemaid kodutöid.
    - Administraator peab saama muuta kasutajate õigusi.

    **Näidised mitte-funktsionaalsetest nõuetest:**
    - Süsteem peab reageerima kasutaja tegevusele maksimaalselt 3 sekundi jooksul.
    - Rakendus peab toetama vähemalt 1000 samaaegset kasutajat.
    - Andmed peavad olema kaitstud volitamata ligipääsu eest.
    - Lahendus peab töötama nii mobiilis kui arvutis.
- `competitive-analysis.md` - konkurentide analüüs
- `README.md` - projekti ülevaade

**🔄 Git workflow**: Issue → Branch → Changes → Commit → Push → PR → Review → Merge

---

## Kodutöö 2: süvauurimine

### Grupi osa 👥
- **Probleemi sügavam alüüs**: täiendage seminaris alatud probleemi analüüsi, kirjeldage probleemi nii, et oleks arusaadav, et tegemist on tõepoolest probleemiga.
- **Kasutajate uurimine**: seminaris alustasite küsimuste koostamist, lõpetage nende koostamine ning intervjueerige igaüks vähemalt 1 päris inimest. Koostage kokkuvõtted.
- **Detailne konkurentsianalüüs**: 3+ konkurenti, igaüks teeb ühe konkurendi kohta ülevaate.  
- **Stakeholder analüüs**: Kes on asjasse puutuvad osapooled?

---

### Individuaalne osa 👤
- **Kasutajate uurija**: intervjuu
- **Turu-analüütik**: konkurendid
- **Tehnoloogia uurija**: tehnilised lahendused ja teostatavus
- **Nõuete analüütik**: detailsed nõuded ja prioritiseerimine

---

### Tööde esitamine
- Kodutööde kohta saabub teile Github issue.
- Looge issuest haru/branch
- Tehke oma kodutöö
- Pushige oma töö
- Tee pull request
- Lisage grupikaaslane ülevaatajaks (VAADAKE TABELIST, KES PEAB TEIE TÖÖ ÜLE VAATAMA)
- Ülevaataja lisab oma arvamuse ja ettepaneku ja kui on kena, siis kiidab heaks ning lisab õppejõu ülevaatajaks
- Õppejõud kinnitab töö sobivusel

---

## Hindamise kriteeriumid 📊

- **Põhjalikkus**: kui sügavalt probleemi uuriti
- **Metodoloogia**: kas kasutati õigeid uurimismeetodeid
- **Dokumentatsioon**: selgus ja professionaalsus
- **Koostöö**: GitHub workflow ja peer review kvaliteet

**📅 Tähtaeg**: seminarinädala esmaspäeva hommikul kell 9.00  
**🔄 Protsess**: individual research → Issue → Branch → Changes → Commit → Push → PR → Review → Merge

---

## Kokkuvõte ja järgmised sammud

### Täna õpisime: ✅
- Mida tähendab tarkvaraarendus vs programmeerimine
- Kuidas defineerida ja analüüsida probleeme
- Kasutajate uurimise meetodeid
- Funktsionaalseid ja mitte-funktsionaalseid nõudeid
- Konkurentsianalüüsi tähtsust

### Järgmine seminar: **Planeerimine** 📋
Kuidas probleemi ja uurimuste põhjal planeerida projekti ja organiseerida meeskonnatööd.

---

## Küsimused? 🤔

**Tänan tähelepanu eest!** 

📧 Küsimused: Discordis 
📁 Materjalid: GitHub repositooriumis  
📅 Järgmine seminar: [kuupäev]
