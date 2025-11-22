# Eksami küsimused: Sissejuhatus tarkvaraarendusse

## Küsimuste struktuur

**Kokku:** 40 valikvastustega küsimust
**Jaotus:**
- Sprint 1 (Uurimine): 12 küsimust
- Sprint 2 (Planeerimine): 14 küsimust
- Sprint 3 (Arendamine): 14 küsimust

**Õiged vastused** on märgitud **tärni sümbooliga (★)**

---

## SPRINT 1: UURIMINE (12 küsimust)

### 1. Mis on tarkvara õige definitsioon?

A) Ainult kood, mis käivitub arvutis
B) Programmeerimisvahendid ja IDE
C) Operatsioonisüsteem ja failid
**D) Kood + Andmed + Dokumentatsioon ★**

**Selgitus:** Tarkvara ei ole ainult kood, vaid hõlmab ka andmeid, millega see töötab, ja dokumentatsiooni, mis selgitab kasutamist ja hooldamist.

---

### 2. Milline on õige järjekord tarkvaraarenduse elutsüklis?

A) Disain → Probleemi analüüs → Arendamine → Testimine
B) Arendamine → Testimine → Disain → Probleemi analüüs
**C) Probleemi analüüs → Disain → Arendamine → Testimine ★**
D) Testimine → Arendamine → Probleemi analüüs → Disain

**Selgitus:** Iga projekt algab probleemi mõistmisega, seejärel disainitakse lahendus, arendatakse ja testitakse.

---

### 3. Mis eristab tarkvaraarendust programmeerimisest?

A) Tarkvaraarendus kasutab rohkem programmeerimiskeeli
**B) Programmeerimine on ainult üks osa tarkvaraarendusest ★**
C) Tarkvaraarendus ei nõua koodimist
D) Need on sama asi, lihtsalt erinevad terminid

**Selgitus:** Programmeerimine on koodi kirjutamine. Tarkvaraarendus hõlmab tervet protsessi: probleemi mõistmine, nõuete kogumine, disain, arendamine, testimine, juurutamine ja hooldus.

---

### 4. Milline on kvalitatiivsete uurimismeetodite eesmärk?

A) Koguda suuri andmekogumeid statistiliseks analüüsiks
**B) Mõista kasutajate motivatsioone, käitumist ja konteksti ★**
C) Testida hüpoteese numbriliste andmetega
D) Automatiseerida andmete kogumist

**Selgitus:** Kvalitatiivsed meetodid (intervjuud, vaatlused) aitavad mõista "miks" ja "kuidas", mitte ainult "kui palju".

---

### 5. Mis on persona eesmärk tarkvaraarenduses?

A) Andmebaasi kirjeldus kasutajate kohta
**B) Fiktiivne, aga realistlik kasutaja, kes esindab sihtrühma ★**
C) Arendaja profiil meeskonnas
D) Kliendi esindaja, kes tellib projekti

**Selgitus:** Persona on kasutajasegmendi esindaja, kes aitab hoida fookust kasutajate vajadustel disainiotsuste tegemisel.

---

### 6. Milline näide on funktsionaalne nõue?

A) Süsteem peab olema kättesaadav 99,9% ajast
**B) Kasutaja saab sisse logida e-posti ja parooli abil ★**
C) Rakendus peab töötama iOS ja Android platvormidel
D) Kõik lehed peavad laadima alla 2 sekundi jooksul

**Selgitus:** Funktsionaalne nõue kirjeldab, MIDA süsteem teeb. Teised variandid on mitte-funktsionaalsed nõuded (jõudlus, skaleeruvus, ühilduvus).

---

### 7. Mis on mitte-funktsionaalse nõude näide?

**A) Süsteem peab toetama 10,000 samaegset kasutajat ★**
B) Admin saab lisada uusi kasutajaid
C) Kasutaja saab broneerida mikrolaineahju
D) Süsteem saadab meeldetuletuse e-posti

**Selgitus:** Mitte-funktsionaalne nõue kirjeldab, KUIDAS süsteem käitub (jõudlus, skaleeruvus, turvalisus), mitte MIDA see teeb.

---

### 8. Milline intervjuu küsimus on kasutajate uurimiseks kõige parem?

A) "Kas teile meeldiks meie toode?"
**B) "Kirjelda viimast korda, kui sa seda probleemi kohtasid." ★**
C) "Millist värvi peaks meie rakendus olema?"
D) "Kas te ostaksite seda toodet?"

**Selgitus:** Head intervjuu küsimused keskenduvad kasutaja kogemusele ja käitumisele, mitte hüpoteetilistele olukorrale või oletustele.

---

### 9. Mis on konkurentsianalüüsi peamine eesmärk?

A) Kopeerida konkurentide funktsioone täpselt
**B) Tuvastada võimalusi innovatsiooniks ja eristumiseks ★**
C) Tõestada, et teie idee on ainulaadne
D) Leida odavaim lahendus turul

**Selgitus:** Konkurentsianalüüs aitab mõista, mis on juba olemas, kus on puudujäägid ja kuidas saab paremini teha.

---

### 10. Milline on probleemi hea defineerimine?

A) "Meie rakendus ei ole piisavalt innovaatiline"
**B) "Üliõpilased ei leia vabu rühmatöö ruume 80% juhtudest tipptundidel" ★**
C) "Meil on vaja paremaid funktsioone"
D) "Kasutajad ei ole piisavalt rahul"

**Selgitus:** Hea probleem on konkreetne, mõõdetav ja selgelt defineeritud. See kirjeldab tegelikku olukorda, mitte abstraktset soovi.

---

### 11. Milline meetod sobib KÕIGE VÄHEM kasutajate kvalitatiivseks uurimiseks?

A) Poolstruktureeritud intervjuud
B) Vaatlused kasutaja loomulikus keskkonnas
**C) Online küsitlus 1000 vastajale ★**
D) Fookusgrupi arutelu 6-8 inimesega

**Selgitus:** Online küsitlus on kvantitatiivne meetod, mis annab numbrilisi andmeid. Intervjuud, vaatlused ja fookusgrupp on kvalitatiivsed meetodid.

---

### 12. Mis on stakeholder'i roll tarkvaraarenduses?

A) Ainult inimene, kes maksab projekti eest
B) Ainult lõppkasutaja, kes toodet kasutab
**C) Igaüks, kes on projektist mõjutatud või mõjutab seda ★**
D) Ainult projektijuht ja arendajad

**Selgitus:** Stakeholder'id hõlmavad kõiki, kellel on huvi projekti vastu: kliendid, kasutajad, arendajad, investorid, juhtkond jne.

---

## SPRINT 2: PLANEERIMINE (14 küsimust)

### 13. Mis on Waterfall metoodika peamine omadus?

A) Iteratiivne ja paindlik lähenemine
**B) Lineaarne, sammhaaval protsess ★**
C) Töötav tarkvara on olulisem kui dokumentatsioon
D) Regulaarsed sprintid 2-nädala tsükliga

**Selgitus:** Waterfall on lineaarne mudel, kus iga etapp tuleb lõpetada enne järgmisele liikumist. Paindlikkus on piiratud.

---

### 14. Milline on Scrum Product Owner'i peamine vastutus?

A) Koodi kirjutamine ja tehniliste otsuste tegemine
B) Meeskonna koosolekute organiseerimine ja blocker'ite eemaldamine
**C) Toote visioon ja backlog prioritiseerimine ★**
D) Disaini loomine ja prototüüpide tegemine

**Selgitus:** Product Owner vastutab toote visiooni, kasutajate vajaduste eest ja otsustab, millised funktsioonid on prioriteedid.

---

### 15. Mis on Scrum Master'i roll?

A) Kirjutada koodi ja teha tehnilisi otsuseid
**B) Aidata meeskonnal järgida Scrum protsessi ja eemaldada takistusi ★**
C) Otsustada, millised funktsioonid arendatakse
D) Disainida kasutajaliidest ja prototüüpe

**Selgitus:** Scrum Master on protsessi hoidja, kes tagab, et meeskond järgib Scrum põhimõtteid ja eemaldab blocker'eid.

---

### 16. Kui pikk on tavaliselt Scrum sprint?

A) 1 päev
**B) 1-4 nädalat (tavaliselt 2 nädalat) ★**
C) 3-6 kuud
D) 1 aasta

**Selgitus:** Sprint on lühike ajaperiood (tavaliselt 2 nädalat), mille lõpuks peab olema töötav tulem.

---

### 17. Mis eristab Kanban'i Scrum'ist?

A) Kanban ei kasuta ülesannete visualiseerimist
B) Kanban ei võimalda meeskonnatööd
**C) Kanban on pideva voo mudel ilma sprintideta ★**
D) Kanban ei võimalda prioritiseerimist

**Selgitus:** Kanban on pideva voo süsteem, kus ülesanded liiguvad läbi töövoo ilma fikseeritud sprintideta. WIP (Work In Progress) on piiratud.

---

### 18. Milline on õige hierarhia tarkvaraarenduse ülesannetes?

**A) Projekt → Epic → User Story → Task ★**
B) Task → User Story → Epic → Projekt
C) User Story → Task → Projekt → Epic
D) Epic → Projekt → Task → User Story

**Selgitus:** Projekt koosneb suurtest funktsioonidest (Epic), mis jagunevad kasutajate vajadusteks (User Story), mis omakorda jagunevad konkreetseteks ülesanneteks (Task).

---

### 19. Mis on user story õige formaat?

A) "Kasutaja klikib nupule ja süsteem salvestab andmed"
**B) "Kui [kasutaja tüüp], siis soovin [funktsioon], et [väärtus]" ★**
C) "Meeskond arendab kasutajaliidese 5 päeva jooksul"
D) "Admin paneel peab olema valmis Sprint 2 lõpuks"

**Selgitus:** User story formaat keskendub kasutajale, nende vajadusele ja väärtusele, mida funktsioon pakub.

---

### 20. Mis tähendab MoSCoW prioritiseerimisel "Must have"?

**A) Kriitilised funktsioonid, ilma milleta toode ei toimi ★**
B) Nice-to-have funktsioonid, mis oleks toredad
C) Funktsioonid, mida me praegu kindlasti ei tee
D) Funktsioonid, mis võiksid olla, kui aega jääb

**Selgitus:** Must have on hädavajalikud funktsioonid. Should have on olulised, Could have on valikulised, Won't have on välistatud.

---

### 21. Miks kasutatakse story points'e aja asemel?

A) Aeg on liiga täpne, story points on ebamäärasemad
**B) Story points mõõdavad keerukust, mitte aega, ja on meeskonnale suhtelised ★**
C) Story points on lihtsamini arvutatavad
D) Story points on rahvusvaheliselt standardiseeritud

**Selgitus:** Story points mõõdavad töö keerukust ja ebakindlust. Iga meeskonna velocity on erinev, seega story points ei ole võrreldavad meeskondade vahel.

---

### 22. Milline Fibonacci number sobib keerulisele task'ile, mis võtab 2-3 päeva?

A) 1 SP
B) 2 SP
**C) 5 SP ★**
D) 13 SP

**Selgitus:** Fibonacci skaala: 1-2 SP (lihtne, 1-4h), 3 SP (keskmine, ~1 päev), 5 SP (keeruline, 2-3 päeva), 8+ SP (liiga suur, peaks jagama).

---

### 23. Mis on sprint retrospective eesmärk?

A) Demonstreerida sprindi tulemust kliendile
**B) Reflekteerida meeskonna protsessi ja leida parenduskohti ★**
C) Planeerida järgmist sprinti ja hinnata task'e
D) Vaadata üle backlog ja prioritiseerida user story-sid

**Selgitus:** Retrospective on meeskonna sisene reflektion, kus arutletakse, mis läks hästi, mis halvasti ja mida parandada.

---

### 24. Milline on efektiivse meeskonna kõige olulisem omadus?

A) Kiire koodikirjutamise oskus
B) Iga liige töötab iseseisvalt ilma häirimiseta
**C) Psühholoogiline ohutus - inimesed julgevad rääkida ja vigu teha ★**
D) Kõik liikmed elavad samas linnas

**Selgitus:** Google'i uuringu "Project Aristotle" järgi on psühholoogiline ohutus kõige olulisem tegur efektiivses meeskonnas.

---

### 25. Mis on GitHub Projects'i peamine eesmärk?

A) Koodi kirjutamine ja versioonihaldus
**B) Ülesannete visualiseerimine ja projekti juhtimine ★**
C) Dokumentatsiooni kirjutamine Markdown vormingus
D) Koodi automaatne testimine

**Selgitus:** GitHub Projects on ülesannete jälimine ja visualiseerimine (Kanban board, tabel), mitte koodi kirjutamine (see on repository).

---

### 26. Millal toimub Sprint Planning?

**A) Sprindi alguses, et otsustada, mida teha ja kuidas ★**
B) Sprindi keskel, et kontrollida progressi
C) Sprindi lõpus, et reflekteerida protsessi
D) Iga päev 15-minutilise koosolekuna

**Selgitus:** Sprint Planning toimub sprindi alguses. Seal määratakse sprint goal, valitakse user story-d ja jagatakse task'ideks.

---

## SPRINT 3: ARENDAMINE (14 küsimust)

### 27. Mis on epic tarkvaraarenduses?

A) Väike ülesanne, mille 1 inimene saab 1 päevaga valmis
**B) Suur funktsioon, mis koosneb mitmest user story'st ★**
C) Kasutaja vajadus, mille saab kirjeldada 1 lausega
D) Konkreetne töö, mida developer teeb

**Selgitus:** Epic on suur funktsioon (nt "Kasutaja registreerimine"), mis jaguneb user story'deks (nt "Kui uus kasutaja, soovin luua konto e-postiga").

---

### 28. Milline on õige task'i suurus?

A) Üks task peaks võtma 2-3 nädalat
**B) Üks task peaks olema 1-3 päeva töö 1 inimesele ★**
C) Üks task peaks hõlmama tervet epicut
D) Üks task peaks olema maksimaalselt 1 tund

**Selgitus:** Task peaks olema piisavalt väike, et 1 inimene saaks selle mõne päevaga valmis. Liiga suured task'id tuleb jagada väiksemateks.

---

### 29. Mis on Planning Poker eesmärk?

A) Meeskonna lõbustamine ja stressimaandamine
B) Arendajate võistlus kiirusega estimating'us
**C) Kollektiivne ülesannete hindamine konsensuse saavutamiseks ★**
D) Project Manager'i aitamine ajakava koostamisel

**Selgitus:** Planning Poker aitab meeskonnal kokku leppida story points'ides läbi arutelu. Ekstreemsed hinnangud arutletakse läbi.

---

### 30. Mis on velocity Scrum'is?

A) Kiirus, millega developer koodi kirjutab
**B) Meeskonna poolt sprindi jooksul lõpetatud story points ★**
C) Aeg, mis kulub ühe task'i tegemiseks
D) Koosolekute arv nädalas

**Selgitus:** Velocity on meeskonna töömaht (story points), mille nad sprindi jooksul valmis said. Seda kasutatakse tulevaste sprintide planeerimiseks.

---

### 31. Mida näitab burndown chart?

A) Meeskonnaliikmete tootlikkust individuaalselt
B) Projekti eelarve kulutamise kiirust
**C) Kui palju tööd on veel jäänud vs ideaalne tempo ★**
D) Kasutajate rahulolu toote kvaliteediga

**Selgitus:** Burndown chart näitab graafiliselt, kui palju story points on veel teha (Y-telg) aja jooksul (X-telg). Aitab varakult probleeme märgata.

---

### 32. Mis on blocker tarkvaraarenduses?

A) Meeskonnaliige, kes ei tee oma tööd
**B) Takistus, mis peatab või aeglustab töö edenemist ★**
C) Klient, kes muudab pidevalt nõudeid
D) Bug, mis leitakse testimise käigus

**Selgitus:** Blocker on mis tahes takistus: dependency (ootab teist tööd), teadmiste puudus, ressursi puudumine või väline viivitus.

---

### 33. Mis on daily standup eesmärk?

A) Detailselt lahendada tehnilisi probleeme
B) Project Manager annab ülesandeid meeskonnale
**C) Kiire info jagamine: mida tegid, mida teed, mis takistab ★**
D) Koodi review ja kvaliteedi kontrollimine

**Selgitus:** Daily standup (15 min) on lühike sünkroniseerimise koosolek. Pikemad arutelud võetakse eraldi.

---

### 34. Millised on daily standup kolm küsimust?

A) Mis läks hästi? Mis halvasti? Mida parandada?
**B) Mida eile tegin? Mida täna teen? Mis mind takistab? ★**
C) Mis on sprint goal? Mis on velocity? Mis on burndown?
D) Kes on Product Owner? Kes on Scrum Master? Kes on Developer?

**Selgitus:** Daily standup keskendub lühikesele ülevaatele: mida tehtud, mis plaanis, millised blocker'id.

---

### 35. Mis on Continuous Integration (CI)?

A) Kord kuus kogu meeskond kohtub ja arutab progressi
**B) Automaatne koodi kokku panemine ja kontrollimine iga commit'i korral ★**
C) Developer'id integreerivad oma koodi käsitsi
D) Kliendid annavad pidevat tagasisidet toote kohta

**Selgitus:** CI tähendab, et iga kord, kui keegi commit'ib koodi, käivituvad automaatsed testid ja kontrollid. Probleemid märgatakse kohe.

---

### 36. Mis on pseudokoodi eesmärk?

A) Kirjutada koodi, mis töötab kohe
**B) Kirjeldada algoritmi loogikat lihtsas keeles enne koodimist ★**
C) Testida programmi jõudlust
D) Dokumenteerida kasutajaliidese disaini

**Selgitus:** Pseudokood kirjeldab loogikat (nt "KUI kasutaja on sisse logitud, SIIS näita dashboardi") ilma spetsiifilise programmeerimiskeeleta.

---

### 37. Milline on Definition of Done (DoD) eesmärk?

A) Määrata, millal projekt on täielikult lõpetatud
**B) Määrata, millal user story või task loetakse valmis ★**
C) Määrata, millal meeskonnaliige võib puhkusele minna
D) Määrata, millal klient hakkab maksma

**Selgitus:** DoD on kriteeriumite loetelu, mis peavad täidetud olema, et user story või task oleks valmis (nt "Kood kirjutatud, testitud, reviewed, merged, dokumenteeritud").

---

### 38. Mis juhtub, kui Sprint Planning'us võetakse liiga palju tööd?

A) Meeskond töötab lihtsalt kiiremini
B) Velocity suureneb automaatselt
**C) Meeskond ei jõua kõike valmis, mis mõjutab velocity'd ja moraali ★**
D) Scrum Master eemaldab automaatselt ülesanded

**Selgitus:** Scope creep ja üle-kommitimine viib selleni, et meeskond ei jõua kõike valmis, mis mõjutab velocity't ja meeskonna motivatsiooni.

---

### 39. Milliseid viise saab kasutada asünkroonseks kommunikatsiooniks meeskonnas?

A) Daily standup videokõne iga päev
B) Sprint retrospective koosolek
**C) GitHub Discussions, Issues kommentaarid, dokumentatsioon ★**
D) Sprint planning koosolek

**Selgitus:** Asünkroonne kommunikatsioon ei nõua, et kõik oleksid samal ajal kohal. GitHub kommentaarid, Discord sõnumid, dokumentatsioon on asünkroonsed.

---

### 40. Miks on sprint retrospective oluline?

A) Klient saab näha, mida meeskond tegi
**B) Meeskond õpib vigadest ja parandab pidevalt protsessi ★**
C) Planeeritakse järgmist sprinti ja valitakse user story-sid
D) Vaadatakse üle koodi kvaliteeti ja bug'e

**Selgitus:** Retrospective on meeskonna õppimise ja pideva parendamise vahend. Start-Stop-Continue meetod aitab tuvastada, mida muuta.

---

## Lisaküsimused (valikuline keerulisem sektsioon)

### 41. Milline on põhiline erinevus funktsionaalse ja mitte-funktsionaalse nõude vahel?

A) Funktsionaalne nõue on raskem implementeerida
**B) Funktsionaalne nõue kirjeldab "mida", mitte-funktsionaalne "kuidas" ★**
C) Mitte-funktsionaalsed nõuded ei ole testida
D) Funktsionaalsed nõuded on alati prioriteetsemad

**Selgitus:** Funktsionaalne = mida süsteem teeb. Mitte-funktsionaalne = kuidas käitub (jõudlus, turvalisus, skaleeruvus).

---

### 42. Miks on kasutajate intervjuud paremad kui oletused?

A) Intervjuud on kiiremad ja odavamad
**B) Intervjuud paljastavad tegelikud vajadused ja käitumismustrid ★**
C) Intervjuud ei nõua planeerimist
D) Kasutajad teavad alati täpselt, mida nad tahavad

**Selgitus:** Kasutajad ei pruugi teada, mida nad tahavad, aga intervjuud paljastavad nende tegelikud valupunktid ja käitumismustrid, millele lahendust luua.

---

### 43. Milline on Sprint Review peamine erinevus Retrospective'ist?

**A) Review näitab toodet stakeholder'itele, Retrospective on meeskonna sisene ★**
B) Review toimub enne Retrospective'i, järjekord ei ole oluline
C) Review on ainult Product Owner'ile, Retrospective kõigile
D) Review on vabatahtlik, Retrospective kohustuslik

**Selgitus:** Sprint Review = demo stakeholder'itele (mis valmis sai). Sprint Retrospective = meeskonna sisene reflektion (kuidas parandada protsessi).

---

### 44. Miks kasutatakse personasid disainiotsuste tegemisel?

A) Personad on andmebaasi tabelite mudel
**B) Personad aitavad hoida fookust kasutajate vajadustel ja vältida oletusi ★**
C) Personad on kohustuslikud Scrum metoodikas
D) Personad asendavad vajaduse kasutajate testimise järele

**Selgitus:** Personad on sünteesitud uurimisandmetest ja esindavad tüüpilisi kasutajaid. Aitavad vastata küsimusele "Kas [persona nimi] vajaks seda funktsiooni?"

---

### 45. Mis on WIP (Work In Progress) piiramine Kanban'is?

A) Meeskonnaliikmed tohivad töötada ainult 40 tundi nädalas
**B) Piiratud arv ülesandeid "In Progress" veerus, et vältida multitasking'ut ★**
C) Projekti eelarve on piiratud
D) Sprint kestus on fikseeritud

**Selgitus:** Kanban'is piiratakse, kui palju task'e saab olla samaaegselt töös, et keskenduda vähestele asjadele korraga ja lõpetada need kiiremini.

---

### 46. Milline on õige viis dependency blocker'i käsitlemiseks?

A) Oodata vaikselt, kuni teine töö on valmis
**B) Kommunikeerida takistust daily standup'is ja prioriseerida dependency ★**
C) Alustada uut task'i ja tagasi tulla hiljem
D) Kustutada takistatud task backlog'ist

**Selgitus:** Blocker'id tuleb avatud kommunikeerida standup'is. Scrum Master või PM aitab prioritiseerida dependency't või leida alternatiive.

---

### 47. Miks on parem kirjutada väikseid task'e suure task'i asemel?

A) Väiksed task'id on kiiremini kirjeldatavad
**B) Väiksed task'id on lihtsamini jälgitavad ja annavad sagedasemat progress tunnet ★**
C) Suuri task'e ei saa GitHub Projects'i lisada
D) Väiksed task'id ei vaja testing'ut

**Selgitus:** Väiksemad task'id (1-3 päeva) on lihtsam hinnata, jälgida ja lõpetada. Annavad meeskonnale sagedasemat saavutuste tunnet.

---

### 48. Milline on pseudokoodi eelis võrreldes kohe koodi kirjutamisega?

A) Pseudokood töötab kiiremini
**B) Pseudokood aitab mõelda läbi loogikat enne tehniliste detailide kallale minemist ★**
C) Pseudokood ei vaja testimist
D) Pseudokood asendab vajaduse dokumentatsiooni järele

**Selgitus:** Pseudokood võimaldab keskenduda loogilisele voolule enne, kui tegeleda tehniliste detailide (süntaks, tüübid, raamistikud) kallale.

---

### 49. Mis on Sprint Goal?

A) Meeskonna aasta eesmärk
**B) Lühike (1 lause) kirjeldus, mida sprint peaks saavutama ★**
C) Iga üksiku task'i kirjeldus
D) Product Owner'i isiklik eesmärk

**Selgitus:** Sprint Goal (nt "Broneerimise funktsionaalsus on töötav ja testitud") aitab meeskonnal fokuseerida ja mõista, miks need user story'd valiti.

---

### 50. Miks on GitHub Pull Request workflow oluline?

A) Tagab, et kõik commit'id on sama formaadiga
**B) Võimaldab peer review'd, parandab koodi kvaliteeti ja jagab teadmisi ★**
C) Asendab vajaduse dokumentatsiooni järele
D) Ainult projektijuht saab koodi muuta

**Selgitus:** Pull Request workflow tagab, et keegi teine vaatab koodi üle enne merge'i. See parandab kvaliteeti, jagab teadmisi ja vältib vigu.

---

## Kokkuvõte

**Kokku 50 küsimust:**
- Sprint 1 (Uurimine): 12 küsimust
- Sprint 2 (Planeerimine): 14 küsimust
- Sprint 3 (Arendamine): 14 küsimust
- Lisaküsimused (keerulisemad): 10 küsimust

**Hindamine:**
- 40/50+ õiget: Suurepärane arusaam tarkvaraarendusest
- 30-39 õiget: Hea arusaam, mõned valdkonnad vajavad süvendamist
- 20-29 õiget: Põhilised kontseptsioonid on selged, kuid detailid vajavad täpsustamist
- <20 õiget: Soovitus kursusematerjali uuesti üle vaadata

**Kasutamine eksamil:**
- Võite valida 30-40 küsimust sõltuvalt eksami pikkusest
- Soovitame segada küsimuste järjekorda
- Võite lisada avatud küsimusi (nt "Selgita oma sõnadega, mis on...") valikvastuste kõrvale

Edu eksamil!
