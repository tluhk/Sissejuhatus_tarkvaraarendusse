# Seminar 3: Sprint 1 - Planeerimine | Õpetaja juhend  
Slide 1

## Seminari üldinfo
- **Kestus**: 3 tundi (90 min teooria + 90 min praktikat)
- **Eesmärk**: Alustada Sprint 1, tutvustada arendusmetoodikaid ja organiseerida meeskonnatöö
- **Oluline**: See on esimene päris "sprint" - tudengid hakkavad aktiivselt töötama

## Ettevalmistus seminari eel

### Vajalikud materjalid:
- [ ] Näidis GitHub Projects repositoorium (demo jaoks)
- [ ] Papaber ja pliiatsid gruppidele (vajadusel)

### Eelkontroll:
- [ ] Kõik tudengid on läbinud Seminar 2 ja teinud kodutöö 2
- [ ] Igal tudengil on GitHub konto ja ligipääs
- [ ] Grupid on moodustatud (3-4 liiget)

---

## OSA 1: TEOORIA (90 minutit)
Slide 2

### 1.1 Arendusmetoodikate ülevaade (35 min)
[Iseseisvalt](../../concepts/arendusmeetodid/README.md)
Slide 4

#### Waterfall mudeli selgitamine (10 min)
Slide 5

**Selgitus:**
> "Alustame tarkvaraarenduse ajaloo algusest. Waterfall ehk kosk või kosemudel on üks vanimaid ja traditsioonilisemaid lähenemisviise. Kujutage ette, et ehitate maja - te ei saa katust teha enne, kui vundament on valmis? Täpselt sama loogika kehtis ka tarkvaraarenduses."

**Mõisted seletada:**
- **Waterfall** - lineaarne, sammhaaval mudel
- **Etapid** - eraldiseisvad, järjestikused töölõigud
- **Dokumentatsioon** - iga etapi lõpus põhjalik dokumenteerimine
- **Change resistance** - muudatused on rasked ja kallid

**Praktilised näited:**
> "Waterfall töötab hästi siis, kui nõuded on väga selged ja ei muutu. Näiteks valitsuse süsteemide puhul või panganduses, kus kõik peab olema ette planeeritud ja dokumenteeritud."

**Küsimused tudengitele:**
- "Mis juhtub, kui klient tahab Waterfall projektis midagi muuta?"
- "Milliseid projekte te ise teeksite, kus Waterfall sobiks?"

#### Agiilse tarkvaraarenduse manifesti tutvustamine (10 min)
[Agiilse arenduse manifest](https://agilemanifesto.org/iso/et/manifesto.html)
Slide 7

**Selgitus:**
> "2001. aastal otsustasid 17 tarkvaraarendajat, et traditsiooniline lähenemine ei toimi. Nad kirjutasid üles neli väga lihtsat värrtust, mis muutsid kogu tööstust."

**Väärtuste sügavam selgitus:**

1. **"Inimesed ja koostöö > protsessid ja tööriistad"**
   > "See ei tähenda, et protsessid pole olulised, vaid et inimesed on olulisemad. Parim tööriist maailmas ei aita, kui meeskond ei suhtle."

2. **"Töötav tarkvara > põhjalik dokumentatsioon"**
   > "Dokumentatsioon on vajalik, aga 200-leheküljeline spetsifikatsioon ei ole kasulik, kui tarkvara ise ei toimi."

3. **"Koostöö kliendiga > lepingu tingimused"**
   > "Leping on algusjoon, aga projekt edeneb koostöös kliendiga."

4. **"Reageerimine muudatustele > plaani järgimine"**
   > "Plaan on oluline, aga võime kohaneda on olulisem."

Agiilse arenduse raamistikud:
https://blog.twn.ee/et/scrumist-scrumbanini

#### Scrum raamistiku tutvustamine (15 min)
Slide 9-10

**Selgitus:**
> "Scrum on nagu jalgpalli mäng - on selged reeglid, rollid ja mänguperioodid. Aga iga mäng on erinev ja meeskond peab kohanema."

**Rollide detailne selgitus:**
*Slaididel pikemalt*  

**Product Owner:**
> "Kujutage ette, et Product Owner / tooteomanik on nagu filmi režissöör. Tal on visioon sellest, milline peaks lõpptulemus olema. Ta teab, mida kasutajad tahavad, ja suudab seda meeskonnale selgitada. Ta ei ütle KUIDAS midagi teha, vaid MIDA vaja on."

**Project Manager ehk projektijuht:**
> "Meie kasutame projektijuhti Scrum Master-i asemel, sest see on lihtsam mõista. Ta on nagu orkestri dirigent - hoiab kõike koos, lahendab probleeme ja aitab meeskonnal hästi töötada."

**Developer ehk arendaja:**
> "Arendaja on nagu meister, kes ehitab maja. Ta mõtleb läbi, kuidas asjad tehniliselt töötama saavad, millised on parimad lahendused ja kuidas kõik osad kokku sobivad."
> "Arendaja (developer) mõtleb kogu süsteemile ja lahendustele (sealhulgas kasutajakogemusele, dokumenteerimisele jne), programmeerija keskendub peamiselt koodimisele."
> "[Mis vahe on arendajal ja programmeerijal?](https://www.indeed.com/career-advice/finding-a-job/developer-vs-programmer)"


**UX/UI disainer:**
> "Disainer on nagu arhitekt - ta mõtleb, kuidas inimesed ruumi kasutavad, kuidas nad end tunnevad ja kuidas kõik välja peaks nägema. Loob välimuse ja käitumismudelid."

**Sprintide selgitamine:**
> "Sprint on nagu kooliprojekti etapp. Te teate, et teil on kaks nädalat aega millegi konkreetse valmissaamiseks. Sprindi lõpus on teile midagi töötavat näidata."

**Scrum sündmuste detailne selgitus:**

**Sprint Planning (2-4h):**
> "See on nagu nädala algus koolis - planeerite, mida teete. Valite backlog-ist ülesanded, hindate neid ja jagate tööd."

**Daily Scrum (15 min):**
> "Iga päev kokku saamine ja 3 küsimust: mida tegid eile, mida teed täna, mis sind takistab. Mitte probleemide lahendamine, vaid info jagamine."

**Sprint Review (1-2h):**
> "Sprindi lõpus näitate, mida tegite. Mitte powerpoint esitlus, vaid töötav tarkvara demonstreerimine."

**Sprint Retrospective (1h):**
> "Arutate, mis läks hästi, mis läks halvasti, mida järgmisel korral teisiti teeksite."

**Praktilised küsimused:**
- "Mis toimub, kui Sprindi ajal tuleb uus nõue?"
- "Kuidas jagate tööd neljaliikmelises meeskonnas?"

#### Kanban süsteemi tutvustamine (5 min)
Slide 12

**Selgitus:**
> "Kanban on nagu supermarketi riiulid - iga toode on oma kohas, ja kui midagi saab otsa, tellitakse uus. Töövoog on pidev, mitte nagu sprindid."

**Kanban põhimõtted:**
- **Visualiseerimine**: Kõik töö on nähtav tahvlil
- **WIP piiramine**: Work In Progress - maksimaalne tööde arv korraga
- **Töövoog**: Töö liigub vasakult paremale
- **Pidev parandamine**: Vaatame, kus on ummikud

**Praktiline näide:**
> "Kujutage ette, et teil on 3 inimese grupp. Kanban ütleb: maksimaalselt 2 tööd ühes staadiumis korraga. Kui 'In Progress' on juba 2 tööd, siis kolmas inimene peab ootama või aitama ülejäänud kahel."



### 1.2 Rollid tarkvaraarenduses (20 min)
Slide 13

**Selgitus:**
> "Nüüd räägime sellest, milliseid rolle teie projektides mängite. Need pole ametinimetused, vaid vastutusalad - see tähendab, et igaüks teist õpib ühte osa tarkvaraarenduse protsessist sügavamalt."

#### Waterfall projektide rollide selgitus (5 min)
Slide 14

**Selgitus:**
> "Waterfall projektides on rollid nagu etappide järgi jaotatud - iga inimene töötab ühes faasis ja siis annab töö edasi järgmisele. See on nagu võistluse teatejooks."

**Waterfall rollide eripära:**
- **Projektijuht**: Kogu projekti ülevalpidaja, ajakava ja eelarve
- **Süsteemianalüütik**: Kogub ja dokumenteerib kõik nõuded enne arendust
- **Süsteemiarhitekt**: Kujundab tehnilise arhitektuuri kõige enne
- **Arendajad**: Ehitavad alles pärast nõuete ja disaini lukku panekut
- **Testijad**: Testivad alles valmis tarkvara
- **Tehnilised kirjutajad**: Dokumentatsioon ja juhendid
- **IT/Operations**: Juurutamine pärast arendust

**Võrdlus Agile-iga:**
> "Waterfall: 'Relay race' - igaüks teeb oma osa ja annab edasi. Agile: 'Basketball' - kõik mängivad koos, kõik teavad kõike."

#### Agiilse arenduse rollide selgitus:
Slaid 16

**Product Owner rolli süvitsi:**
> "Tooteomanik on nagu tõlk kasutajate ja meeskonna vahel. Te peate mõistma, mida kasutajad tegelikult tahavad - mitte seda, mida nad ütlevad, et tahavad. Näiteks kui kasutaja ütleb 'Ma tahan kiiremat süsteemi', siis Product Owner küsib: 'Mis täpselt on aeglane? Millal? Miks see sind häirib?'"

**Praktilised ülesanded tooteomanikule:**
- Prioriseerida backlog-i (mis on kõige olulisem?)
- Kirjutada aktsepteerimiskriteeriumid (millal on ülesanne valmis?)
- Suhelda "kasutajatega" (klassikaaslased, õpetaja)

**Projektijuhi rolli süvitsi:**
> "Projektijuht on nagu juht, kes hoiab kõike liikumises. Jälgib ajakavu, märkab probleeme enne, kui need suureks kasvavad, ja aitavab kõigil oma tööga edasi jõuda."

**Praktilised ülesanded projektijuhile:**
- Planeerida sprinte (millal mis valmis saab?)
- Jälgida progressi (kas oleme graafikus?)
- Koordineerida koostööd (kes millal mida teeb?)

**Developer rolli süvitsi:**
> "Developer mõtleb süsteemi seest. Kuidas andmed liiguvad? Kuidas erinevad osad suhtlevad? Millised on tehnilised piirangud? Te peate olema nagu insener, kes planeerib, kuidas sild ehitada."

**UX/UI Designer rolli süvitsi:**
> "Designer paneb end kasutaja kingadesse. Te küsite: 'Kuidas kasutaja end tunneb? Mis on tema eesmärk? Kuidas ta mõtleb?' Te olete nagu psühholoog ja kunstnik koos."

### 1.3 Meeskonnatöö ja kommunikatsioon (15 min)
Slide 22

**Selgitus:**
> "Tarkvaraarendus on meeskonnasport. Isegi maailma parim programmeerija ei saa üksi suurt süsteemi ehitada. Seepärast peame õppima koostööd."

#### Psühholoogiline ohutus:

> "Google uuris, mis teeb meeskonna edukaks. Üllatusega avastati, et kõige olulisem pole see, KES meeskonnas on, vaid KUIDAS nad koos töötavad. Kõige tähtsam oli psühholoogiline ohutus."

**Mis see tähendab:**
- Võib öelda "Ma ei tea"
- Võib teha vigu ilma karistuseta
- Võib küsida "lollisid" küsimusi
- Võib olla erineval arvamusel

**Praktilised näpunäited:**
- "Alati öelge 'Ma ei saa aru' kui midagi pole selge"
- "Küsige abi ENNE, kui olete hätta jäänud"
- "Kritiseerige ideid, mitte inimesi"

#### Kommunikatsiooni vormid:
slaid 24

**Daily standup:**
> "Kujutage ette, et igal hommikul käib kogu pere kokku ja ütleb: mida ma eile tegin, mida ma täna teen, mis mulle takistab. See võtab 5 minutit, aga kõik teavad, mis toimub."

**Asünkroonne suhtlus:**
> "GitHub-is võite jätta kommentaare, küsimusi, linke. See on nagu chat, aga organiseeritum. Kõik info on alles ja hiljem leitav."

### 1.4 Backlog management ja prioriseerimine (20 min)
Slide 25

#### Epikute jagamine visuaalselt:
Slide 26

**Selgitus:**
> "Mõelge oma projektist kui raamatust. Raamat koosneb peatükkidest (epikud), peatükid lõikudest (User Story-d), lõigud lausetest (Task-id). Alustame suurtest asjadest ja jagame väiksemaks."

**Praktiliseks näiteks kasutage tudengite enda projekte:**
> "Võtame näiteks projekti 'Kooli Köök':
> - EPIK: Mikrolaineahjude broneerimissüsteem
>   - USER STORY: Kasutaja näeb vabade ahjude reaalajas olekut
>     - TASK: IoT sensorite andmete API
>     - TASK: Reaalajas kaardi komponendi loomine
>     - TASK: Mobile-responsive kujundus"

#### Story pointide selgitamine:
Slide 27

> "Story point-id pole tunnid või päevad - need on KEERUKUS. 1 punkt on nagu kooli maht-ülesanne matemaatikas - te teate kohe vastust. 5 punkti on nagu uurimistöö - peate uurima, katsetama, võib-olla mitut korda proovima."

**Kõigi ees näiteid hinnata:**
- "GitHub konto loomine" - 1 punkt (lihtne, teate kuidas)
- "README.md faili kirjutamine" - 2 punkti
- "Konkurentsianalüüs 5 firma kohta" - 5 punkti
- "Täielik prototüüp" - 8 punkti (liiga suur, peaks jagama)

#### MoSCoW prioritiseerimine:
Slide 28

**Praktiline harjutus klassiga:**
> "Võtame 'Kooli Köök' projekti ja kategoriseerime funktsioone:
> - **Must have**: Mikrolaineahjude reaalajas olek (ilma selleta ei ole projekt kasulik)
> - **Should have**: Push teavitused vabadest ahjudest (väga oluline, aga saab ka ilma)
> - **Could have**: Toidu jagamise funktsioon (tore lisa, kui aeg lubab)
> - **Won't have**: Täielik makselahendus (hetkel teadlikult välja jätame)"

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 minutit)
Slaid 29

### Üldised juhised õpetajale praktiliseks osaks:

1. **Liikuge ringi**: Ärge istuge laua taga - minge gruppide juurde
2. **Kuulake**: Enne vastamist kuulake, mis on tegelik probleem
3. **Juhendage, ärge lahendage**: Küsige "Mis te arvate?" enne vastuse andmist
4. **Jälgige aega**: Kasutage timerit - tudengid kaotavad aja tunde

### 2.1 Rollide jaotamine (15 min)
Slide 30

#### Juhised tudengitele:

**Selgitus:**
> "Nüüd valite oma rolli järgmisteks kolmeks nädalaks. See on nagu teatris - igaüks mängib ühte rolli hästi. Te ei pea teadma kõike, aga peate oma ala hästi teadma."

**Rollide valiku juhendamine:**
- Küsige tudengitelt, mis neid huvitab
- Jaotage grupid nii, et kõik rollid oleksid esindatud
- Ärge laske ühel rollil domineerida (nt kõik tahavad olla Developer)

**Arutelu küsimused gruppidele:**
1. "Miks valisite just selle rolli?"
2. "Mida te selles rollis tegema hakkate?"
3. "Millest te kartate/muretsete?"

#### Rolli kirjelduse koostamine:

**Juhendage tudengeid kirjutama:**
```markdown
## Minu roll: [Product Owner]

### Minu vastutused:
- [konkreetsed ülesanded]

### Minu eesmärgid:
- [mida tahate saavutada]

### Kuidas mõõdan edu:
- [kuidas teate, et töö on hästi tehtud]
```

### 2.2 Projektiplaani loomine (20 min)
Slide 31

#### Project Charteri/projektiplaani loomise juhendamine:

**Selgitus:**
> "Project Charter / projektiplaan on nagu lepingu lühiversioon meeskonna sees. Te lepite kokku, mida teete ja mida EI tee. See hoiab teid keskendunult."

**Juhendage gruppi täitma template-i samm-samult:**

1. **Projekti nimi** (2 min):
   > "Leidke nimi, mis on lühike ja meeldejääv. Ärge kasutage tehnilist žargooni."

2. **Probleemi kokkuvõte** (5 min):
   > "Üks-kaks lauset. Kirjutage nii, et teie vanaema mõistaks, mis probleem on."

3. **Lahenduse visioon** (5 min):
   > "Mitte detailid, vaid suur pilt. Kuidas maailm pärast teie lahenduest erinev on?"

4. **Eesmärgid** (5 min):
   > "3-5 konkreetset asja, mida soovite saavutada. Mitte 'teha hästi', vaid 'kasutaja leiab info 10 sekundi jooksul'."

5. **Edu kriteeriumid** (3 min):
   > "Kuidas teate, et õnnestsite? Mida saate mõõta?"

**Liikuge gruppide vahel ja küsige:**
- "Kas see on piisavalt konkreetne?"
- "Kas teie vanaema mõistaks?"
- "Kuidas te seda mõõdate?"

### 2.3 GitHub Projects seadistamine (25 min)
Slide 32

#### Praktilise demo ettevalmistus:

**Õpetaja demo (10 min):**
1. Avage näidis repositoorium
2. Minge Projects tab-ile
3. Looge uus Project (Table view)
4. Näidake custom field-e
5. Demonstreerige automation-e

**Jutt demole lisaks:**
> "GitHub Projects on nagu digitaalne Kanban tahvel. Saate ka filtreerida, sorteerida, automatiseerida. See on teie missiooni kontroll."

#### Custom field-e seadistamise juhendamine:

**1. Story Points field:**
```
Name: Story Points
Type: Number
Options: 1, 2, 3, 5, 8, 13
```
> "See aitab teil hinnata keerukust. Kasutage Fibonacci skaalat."

**2. Priority field:**
```
Name: Priority  
Type: Select
Options: Critical, High, Medium, Low
Colors: Red, Orange, Yellow, Green
```

**3. Component field:**
```
Name: Component
Type: Select  
Options: Research, Design, Documentation, Planning
```

**4. Sprint field:**
```
Name: Sprint
Type: Select
Options: Sprint 1, Sprint 2, Sprint 3
```

#### Views loomine (tudengid teevad kaasa):

**Sprint Board view:**
1. Create new view → Board
2. Group by: Status  
3. Filter: Sprint = "Sprint 1"
4. Layout: To Do | In Progress | Review | Done

**Backlog view:**
1. Create new view → Table
2. Sort by: Priority (High to Low), then Story Points (Low to High)
3. Show all items

#### Views ja workflows selgitus (5 min):

**Selgitus:**
> "GitHub Projects võimaldab teil luua erinevaid vaateid samade andmete jaoks. See on nagu erinevad aknad samasse ruumi - igaüks näeb asju oma nurga alt."

**Sprint Board view selgitus:**
> "See on klassikaline Kanban tahvel. Näete, mis tööde seisundis on. Filtreerite ainult praeguse sprindi ülesanded ja rühmitate tegijate järgi."

**Backlog Management view selgitus:**
> "See on nagu Excel tabel. Näete kõiki ülesandeid korraga, sorteerituna prioriteedi ja keerukuse järgi. Ideaalne planeerimiseks."

**Praktilised küsimused tudengitele:**
- "Millises vaates te planeeriksite järgmist sprinti?"
- "Millises vaates te jälgiksite igapäevast tööd?"
- "Kuidas kasutaksite erinevaid vaateid erinevates olukordades?"

### 2.4 Sprint 1 planeerimine (20 min)
Slide 34

#### Sprint Goal ehk sprindi eesmärkide väljatöötamine:

**Selgitus:**
> "Sprint Goal ehk sprindi eesmärk on nagu teie moto selleks nädalaks. Üks lause, mis ütleb, mida te korda saadate. Mitte nimekiri asjadest, vaid EESMÄRK."
> "Lühike ja selge kirjeldus, miks sprinti tehakse ja millist väärtust loodetakse saavutada."

**Näited headest Sprindi eesmärkidest:**
- ✅ „Luua kasutajale võimalus registreerida end e-posti teel, et suurendada uute klientide liitumist.“
- ✅ "Meeskond on valmis produktiivseks tööks"
- ✅ "Projekti skoop ja plaan on selge"
- ❌ "Teeme charter-i ja seadistame GitHub-i" (see on task-ide list)  
See on pigem tööülesannete loetelu, mitte eesmärk. Sprinti eesmärk peaks vastama küsimusele „Miks me seda teeme?“, mitte „Mida me täpselt teeme?“. Õigem oleks sõnastada näiteks:
👉 „Projekt on käivitamiseks valmis ja tehniline keskkond loodud.“


#### Capacity planning harjutus:

**Juhendage tudengeid:**
1. "Mitu tundi nädalas te selle kursuse peale kulutate?" 
2. "Jagades läbi 4 (kuna 1 story point ≈ 2-4h), kui palju story point-e te nädalas võtate?"
3. Keskmiselt: 2-4 story point-i tudeng/nädal

#### Task-ide väljatöötamine Sprint 1 jaoks:
Slaid 35

**Juhendage gruppi looma konkrettseid task-e:**

**Must-have task-id:**
- [ ] Project charter dokument valmis (3 SP)
- [ ] Kõigi rollide kirjeldused (2 SP)
- [ ] GitHub Projects seadistatud (2 SP)  
- [ ] Risk assessment tehtud (3 SP)
- [ ] Communication plan kokku lepitud (1 SP)

**Küsimused kontroliks:**
- "Kas see on konkreetne?"
- "Kas sellel on selge definition of done?"
- "Kes selle eest vastutab?"

### 2.5 Daily workflow seadistamine (10 min)
Slide 36

#### Daily standup protokolli ülespanek:

**Selgitus:**
> "Te ei saa iga päev füüsiliselt kokku, seega kasutage GitHub Discussions-i. Aga oluline on REGULAARSUS."

**Seadistage grupiga:**
1. Looge repositooriumis Discussions tab
2. Tehke pinned post: "Daily Standups"
3. Template:
```markdown
## Daily Standup [Date]

**Nimi:** [Teie nimi]
**Roll:** [Teie roll]

### ✅ Eile tegin:
- 

### 🎯 Täna teen:  
- 

### ❌ Mind takistab:
- 
```

**Kokkuleppide tegemine:**
- Millal postitavad? (nt iga päev kell 9:00)
- Kui sageli? (vähemalt 3 korda nädalas)
- Kuidas abi küsivad?

---

## Slide 37: Kodutöö selgitamine

**Rõhutage tudengitele:**
- See ei ole individuaalne töö - see on ühine projekt
- Iga roll peab oma osa tegema
- GitHub workflow on oluline - kasutage branche
- Küsimused võib esitada GitHub Discussions-is

**Kodutöö ülesanded:**
- `project-charter.md` - projekti kirjeldus ja eesmärgid
- `team-roles.md` - rollide kirjeldused ja vastutused  
- `project-timeline.md` - ajakava ja milestoneid
- `risk-analysis.md` - riskide analüüs ja leevendamise strateegiad
- `communication-plan.md` - meeskonna suhtluse protokollid
- `sprint-1-plan.md` - Sprint 1 eesmärgid ja ülesanded
- `sprint-1-review.md` - Sprint 1 tulemused ja analüüs

**Rolli-põhised ülesanded:**
- **Product Owner**: `product-backlog.md`
- **Project Manager**: `project-management-plan.md`
- **Developer**: `technical-architecture.md`
- **UX/UI Designer**: `design-strategy.md`

---

## Slide 33-34: Kokkuvõte ja järgmised sammud

**Mida õppisime:**
- ✅ Erinevaid arendusmetoodikaid
- ✅ Meeskonna rolle ja vastutusi
- ✅ GitHub Projects advanced kasutamist
- ✅ Sprint planeerimise põhimõtteid
- ✅ Meeskonnatöö alused

**Mis järgmiseks:**
> "Järgmine seminar: **Sprint 2 - Disainimine**. Te loote kasutajaid, joonistage prototüüpe ja planeerite kasutajakogemust."

---

## Slide 35: Küsimused?

**Edu Sprint 1-ga! 🚀**

---

## Pedagoogilised märkused

### Keerulised hetked ja kuidas nendega toime tulla:

#### "Me ei tea, mida teha"
**Probleem:** Tudengid on ülekoormatud infoga
**Lahendus:** 
- Alustage väiksemast: "Valige ainult üks asi ja tehke see valmis"
- Näidake oma ekraanilt, kuidas alustada

#### "GitHub on keeruline"
**Probleem:** Tehniline hirmutus
**Lahendus:**
- Tehke koos, samm-sammult
- Kasutage ainult GUI-d, mitte terminali
- "See on normaalne, et alguses segane tundub"

#### "Rollid on ebaselged"
**Probleem:** Tudengid ei tea, mida oodatakse
**Lahendus:**
- Andke konkreetseid näiteid: "Product Owner küsitlaks 3 klassikaaslast"
- Rõhutage: "Te õpite seda rolli, ei pea kohe ekspert olema"

#### "Meie grupp ei tööta koos"
**Probleem:** Kommunikatsiooni probleemid
**Lahendus:**
- Istuge grupiga maha ja kuulake kõiki pooli
- Tehke ühine kokkulepe: "Mis reeglid me endale seame?"

### Tähelepanekud tudengite käitumisele:

**Hästi toimiv grupp:**
- Kõik räägivad
- Küsivad teineteiselt küsimusi
- Jagavad tööd loomulikult
- Naeravad ja on vabalt

**Probleemne grupp:**
- Üks inimene domineerib
- Vaikus või kohmakas olek
- Kõik töötavad eraldi
- Stress või frustratsioon

### Ajalise planeerimise nipid:

1. **Alustage õigel ajal:** Ärge jätke praktilist osa lühikeseks
2. **Peatuse märgid:** Andke teada 5 min enne ülesande lõppu
3. **Paindlikkus:** Kui grupp vajab rohkem aega, kohandage
4. **Energia jälgimine:** 90 min järel on inimesed väsinud

---

## Kokkuvõte ja järgmised sammud

### Seminari lõpu checklist:

- [ ] Kõik grupid on rollid jaotanud
- [ ] Project charter on alustatud
- [ ] GitHub Projects on seadistatud
- [ ] Sprint 1 goal on määratletud
- [ ] Daily standup protokoll on kokku lepitud
- [ ] Kodutöö ülesanded on selged

### Kodutöö selgitamine (5 min):

**Rõhutage:**
- See ei ole individuaalne töö - see on ühine projekt
- Iga roll peab oma osa tegema
- GitHub workflow on oluline - kasutage branche
- Küsimused võib esitada GitHub Discussions-is

### Järgmise seminari eelvaade:

> "Järgmine kord alustame Sprint 2-ga, mis keskendub disainile. Te loote kasutajaid, joonistage prototüüpe ja planeerite kasutajakogemust. Aga kõik see toimub jätkuvalt Sprindi raamistikus."

---

## FAQ - Korduma kippuvad küsimused

### Tehnilised küsimused:

**K: "Mis on story point?"**
V: "Keerukuse mõõt. 1 punkt = lihtne, 5 punkti = keeruline. Mitte aeg, vaid raskusaste."

**K: "Kuidas GitHub Projects toimib?"**
V: "Nagu digitaalne kleebislapid tahvel. Saate liigutada, filtreerida, sorteerida."

### Organisatoorsed küsimused:

**K: "Mis juhtub, kui keegi ei tee oma osa?"**
V: "Sprint review ajal arutatakse, mis edasi. Võib-olla jagate tööd ümber."

**K: "Kas võime rolle vahetada?"**
V: "Mitte selle kursuse jooksul. Õppige üht rolli hästi."

### Kontseptuaalsed küsimused:

**K: "Miks me ei alusta koodi kirjutamisega?"**
V: "Sest 80% tarkvaraarendust on planeerimine, mõtlemine ja koostöö. Kood on ainult 20%."

**K: "Kas see on nagu päris töökohas?"**
V: "Jah! Need protsessid ja tööriistad on samad, mida kasutavad päris ettevõtted."

---

## Lisaressursid õpetajale

### Soovituslikud materjalid täiendavaks lugemiseks:
- Agile Manifesto: https://agilemanifesto.org/
- Scrum Guide: https://scrumguides.org/
- GitHub Projects dokumentatsioon: https://docs.github.com/en/issues/planning-and-tracking-with-projects

### Motiveerivad tsitaadid:
> "The best architectures, requirements, and designs emerge from self-organizing teams." - Agile Manifesto

> "It's not the strongest of the species that survives, nor the most intelligent, but the one most responsive to change." - Darwin (agile kontekstis)

### Lõpumärkused:
Pidage meeles, et tudengid õpivad esimest korda päris projektijuhtimist. Olge kannattavad, julgustage eksperimenteerimist ja rõhutage, et vigade tegemine on normaalne osa õppimisprotsessist.