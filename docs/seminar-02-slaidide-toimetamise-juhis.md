# Seminari 2 slaidide ümbertegemise juhis

Kirjuta ümber `seminarid/seminar_02-toimetatud/slides.md`. Eesmärk on loogiline, algajale arusaadav seminar, mida õpetaja saab slaidide järgi läbi viia. Säilita sisulised teemad ja vajalikud selgitused. Liigne lühendamine on praegusest versioonist osa vajalikku sisu juba eemaldanud.

See on tööjuhis materjali toimetavale mudelile, mitte õppija juhend. Ära käivita teist mudelit ega muuda kursuse nõudeid.

## 1. Loe enne muutmist

Kõik allolevad teed on repositooriumi juure suhtes.

- `AGENTS.md`
- `seminarid/seminar_02-toimetatud/slides.md`
- `seminarid/seminar_02-toimetatud/00-opetaja-juhis.md`
- `seminarid/seminar_02-toimetatud/01-seminar.md`
- `seminarid/seminar_02-toimetatud/03-kodutoo.md`
- Kõik sama kausta `peatukid/` Markdown-failid.
- `docs/kursuseprogramm.md`
- `concepts/commit/README.md` ja `concepts/licence/README.md`.

Õpetaja juhisest võta kontakttunni ajakava, kodutööst nõuded ning peatükkidest selgitused ja näited. Slaidide praegune nappus ei ole põhjus teema väljajätmiseks.

## 2. Probleemid, mis tuleb lahendada

- Slaidid vahetavad juhuslikult selgitamise, aruteluküsimuse ja praktilise käsu vahel. Mõni ülesanne tuleb enne vajaliku mõiste selgitamist.
- Samad küsimused korduvad kliendisoovi, probleemi uurimise, discovery ja juhtumiarutelu juures. Kodutöö ning release'i tulemus on jagatud paljude slaidide vahel.
- Litsentside slaid küsib kontrollimist enne litsentsi mõiste selgitamist. Kanban on taandunud tahvli kasutamise käsuks. Giti põhiringu slaid ütleb „Näita läbi”, kuid ei anna õppijale enam käske.
- Õpetaja ja õppija hääl on segamini: „Näita läbi”, „Näitan” ja „koosta” esinevad samal tasemel.
- Mõni link lubab rohkem, kui sihtfail annab. Näiteks release'i loomise sammud on peatükis `08-tiimiprojekt-ja-toovoog.md`; peatükk `10-kodutoo-ja-release.md` annab peamiselt kodutöö kokkuvõtte.

## 3. Säilita need kokkulepped

- Kontaktaeg on kaks 90-minutilist osa. Säilita õpetaja juhise teemade ajamaht ja tehniline puhver. Kõiki tegevusi ei pea seminaris lõpetama.
- Esimene seminar on toimunud. Elutsükkel, Waterfall ja agiilne tööviis on lühike meenutus.
- Õppestsenaarium: „Haapsalu Kolledž soovib oma tunniplaani veebilehte muuta kaasaegsemaks.” Tegelikke kasutajaprobleeme ei tohi välja mõelda ega kinnitatud faktina esitada.
- Seminari 2 fookus on probleemi mõistmine ning kasutajate ja vajaduste uurimine. Kasutajalugude ja funktsionaalsete nõuete detailne koostamine jääb seminari 3.
- Iga õppija koostab vähemalt kolm enda probleemikandidaati oma Issue, haru, faili ja PR-i kaudu ning vaatab üle kaaslase PR-i. Tiim võrdleb kandidaate pärast individuaalsete tööde ülevaatamist ja ühendamist.
- Võrdlus, probleemi kontrollimine, ühine otsus, refleksioonid ning päris release `v0.1.0` valmivad kodutööna. Seminaris näidatakse release'i loomist.
- Organisatsioon on `TLUHK-RIF26`. Üks tiim kasutab üht ühist repot. Töövahendid on Git, GitHub, terminal ja VS Code; GitHub Desktopi ei kasutata.
- Harud ja commit'i sõnumid on inglise keeles. Säilita haruskeem `issue-<number>-<short-english-description>`.
- Release manager vahetub projektiseminaride vahel. Kursuse tulemus on dokumenteeritud arendusprotsess ja põhjendatud otsuste logi. Töötavat rakendust ega klikitavat prototüüpi ei nõuta.
- AI kasutamine vähemalt ühe olulise otsuse juures ning selle väljundi kontrollimine jäävad alles. AI väljund ei ole kasutajauuringu tõend.

## 4. Ehita üks läbiv tegevusjärjestus

Kasuta allolevat järjestust. Üks punkt ei pea tähendama üht slaidi. Orienteeruv maht on 24–30 slaidi; ära kärbi sisu üksnes selle arvu saavutamiseks.

1. **Algus:** pealkiri, kursuse seminaride lühike teekond, tänane eesmärk ning vahe seminari lõpu ja kodutöö lõpu tulemuse vahel. Tutvusta kliendisoovi kogu päeva lähtekohana.
2. **Esimese seminari meenutus:** kus oleme elutsüklis ning kuidas Waterfall ja agiilne töö korraldamist mõjutavad. Väldi mitut samasisulist protsessiskeemi.
3. **Rollid:** miks eri vastutusi vaja on ja millise küsimuse iga roll selle kliendisoovi puhul esitab. Roll ei võrdu tingimata ühe inimesega. Ära käsitle tellijat ja tooteomanikku automaatselt sama vastutusena.
4. **Kliendisoovist probleemini:** erista soov, probleem ja lahendusidee ühe selge näite abil. Seejärel selgita probleemiväidet ning tõendi, tõlgenduse ja oletuse erinevust.
5. **Uurimise ettevalmistamine:** mida tegeliku kasutuskogemuse kohta küsida, kuidas AI aitab ning mida tuleb kontrollida. Näita, miks allika ja litsentsi kontroll on vajalik teiste materjalide kasutamisel. Selgita litsentsi enne kontrollküsimust. Kasuta discovery näidet selle tööviisi kinnitamiseks, mitte uue samasisulise teemaringina.
6. **Individuaalne harjutus:** kolm kandidaati ja esmane enesehindamine. Anna lühike ülesanne, oodatav väljund ning link töölehele. Ühist probleemi veel ei valita.
7. **Teise osa algus:** tiim, ühine repo, kloonimine, isiklik Issue ja Projects. Selgita Kanbani mõtet ning seo ajahinnang järgmise tegeliku ülesandega.
8. **Üks läbiv GitHubi töövoog:** enda Issue → haru → fail → commit → push → PR → kaaslase ülevaatus → parandused → merge → kohaliku peaharu uuendamine. Näited peavad kirjeldama sama ülesannet. Paiguta haru ja commit'i nimetamistavad nende kasutamise juurde.
9. **Seminari lõpetamine:** üks kontrollpunkt, release'i lühike näidis ning kodutöö järjestus: individuaalsete tööde lõpetamine → võrdlus → valideerimine → otsus ja lähteülesanne → refleksioonid ja release. Koonda vajalikud failid ning esitamise link ühte selgesse kohta.

## 5. Kirjuta slaidid ühetaoliselt

- Igal slaidil on üks eesmärk. Selgitus annab mõiste, näide teeb selle arusaadavaks ja harjutus laseb seda kasutada. Ära asenda kõiki selgitusi aruteluküsimustega.
- Slaid peab olema esmaseks mõistmiseks piisav. Peatükk lisab põhjenduse, täiendava näite või üksikasjalikud sammud. Lühike põhisõnum võib korduda, terve sama selgituse lugemine teist korda peab olema tarbetu.
- Säilita peamised kopeeritavad Giti käsud seal, kus õpetaja neid näitab. Kasuta üht läbivat näidisharu ja tegeliku kujuga failiteed. Selgita käsu eesmärki lühidalt; põhjalikum juhend jääb peatükki.
- Ära tee eraldi slaidi iga üleminekulause või üksiku küsimuse jaoks. Ühenda samasse tegevusse kuuluvad küsimused.
- Kirjuta nähtav tekst õppijale. Pane õpetaja tegevused Marpi HTML-kommentaaridesse. Näiteks „Näita läbi põhiring” kuulub õpetaja märkusse; slaidile kuuluvad põhiring ja selle eesmärk.
- Anna sisuline link teemaploki juures. Korda tööjuhendi linki praktilises töös siis, kui õppija vajab seda uuesti. Ära eemalda kasulikke linke üksnes linkide arvu vähendamiseks.
- Lingi olemasolevatele failidele. Väldi kohalike pealkirjaankrute kasutamist. Kontrolli, et lingi nimetus vastab sihtfaili sisule.

## 6. Muudatuse piirid ja lõpetamine

Muuda slaidide lähtefaili ning genereeri sellest uuesti sama kausta `slides.html`. Säilita Marpi päis ja slaidieraldajad. Ära muuda algset `seminarid/seminar_02/` kausta ega nummerda peatükke ümber. Teiste failide sisulised muutmisvajadused esita lõpus eraldi tähelepanekuna.

Enne lõpetamist kontrolli, et iga praktilise tegevuse eel on vajalik mõiste selgitatud, kõik punktis 3 loetletud kokkulepped on alles ning seminari ja kodutöö tulemused on eristatavad. Kontrolli kohalike linkide olemasolu, tühjade või ülekoormatud slaidide puudumist ja muudatuste diffi. Genereeri HTML käsuga:

```bash
marp seminarid/seminar_02-toimetatud/slides.md --output seminarid/seminar_02-toimetatud/slides.html
```

Lõpuks kirjuta lühidalt, millised kordused ühendasid, millised vajalikud selgitused taastasid ja kas mõni seotud juhend vajab kooskõlastamist. Ära väida visuaalset kontrolli tehtuks, kui kontrollisid ainult lähtefaili ja ekspordi õnnestumist.
