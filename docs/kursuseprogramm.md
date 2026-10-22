# Kursuseprogramm

## Mida kursusel teeme?

Seminaris 2 alustame meeskondades üht läbivat projekti. Kõik tiimid lähtuvad Haapsalu Kolledži tunniplaani veebilehe kohta antud kliendisoovist. Iga õppija uurib iseseisvalt võimalikke kasutajaprobleeme ning esitab oma kandidaadid pull request'iga. Pärast nende ülevaatamist ja ühendamist võrdleb tiim kandidaate, valib ühe probleemi ning kontrollib seda tõendite abil. Nii sõnastatakse arendustiimile selge ja piiritletud ülesanne.

Kursuse jooksul uurime tarkvaraarenduse tervikut:

```text
Probleem
  ↓
Kasutajate ja vajaduste uurimine
  ↓
Nõuete kirjeldamine
  ↓
Töö planeerimine
  ↓
Lahenduse disainimine
  ↓
Arendamine
  ↓
Testimine ja tagasiside
  ↓
Avaldamine ja hooldus
```

Projekti tulemus on dokumenteeritud arendusprotsess. Selle keskmes on otsuste logi: mida valisime, milliseid alternatiive kaalusime, miks nii otsustasime ja kuidas uus info meie arusaama muutis. Süsteemi põhimõtet selgitame kirjelduse või vajaduse korral skeemiga. Töötav rakendus ja klikitav prototüüp ei ole nõutavad.

Kursus koosneb viiest seminarist ja lõpuesitlusest:

1. seminar 1: suur pilt ja töövahendite seadistamine;
2. seminar 2: kliendisoovist arendusülesandeni;
3. seminar 3: rollid, tööviisi valik ja süsteemi kontseptsioon;
4. seminar 4: kvaliteet, riskid ja vastutus;
5. seminar 5: kasutuselevõtt, tagasiside ja hooldus;
6. eksam: dokumenteeritud protsessi esitlus release'ide ajajoonena.

Kursuse läbiv praktiline töö toimub GitHubis. Seminarist 2 kasutab iga meeskond üht ühist repositooriumi. Iga õppija teeb muudatusi enda harus ja vaatab üle kaaslase töö. Ametialased rollid vahetuvad ning iga projektiseminari järel kirjutab iga õppija refleksiooni.

Projektiseminaride kodutöö lõpeb GitHub Release'iga ehk avaldatud versiooniga, mis fikseerib dokumentatsiooni hetkeseisu ja olulised muutused. Kodutöö arvestuslik maht on umbes 8 tundi õppija kohta. Esimese seminari kodutöö on individuaalne; release'ide tegemist alustame meeskonnaprojektiga.

AI-d kasutame vähemalt ühe olulise otsuse juures ning selgitame selle kasu ja väljundi kontrollimist. Hindamisel on keskmes arusaamine ja põhjendamine.

## Seminar 1: suur pilt ja töövahendid

### Teemad

- mis on tarkvara ja tarkvaraarendus;
- tarkvaraarenduse elutsükkel ja AI mõju;
- IDE, VS Code, terminal ja käsukest;
- Git, GitHub, GitHub CLI, Markdown;
- Node.js, Docker ja arenduskeskkonna mõiste;
- esimene commit ja push.

### Materjalid

- [Seminari materjal](../seminarid/seminar_01/seminar.md)
- [HTML-slaidid](../seminarid/seminar_01/slides.html)
- [Kodutöö 1: minu arenduskeskkond](../seminarid/seminar_01/homework.md)

Toimunud seminari järel kinnistab kodutöö terminalis `add → commit → push` töövoogu ja sisaldab lühikest käsuspikrit. Node.js, npm, Docker ning GitHub CLI on valikulised. Kodutöö tehakse Issue'st loodud harus ja esitatakse pull request'iga; enne õppejõudu vaatab töö üle kaasõppija (paarid failis `student_pairs.md`). Pooleli jäänud sammust antakse teada ülesande Issue kommentaaris.

## Seminar 2: kliendisoovist arendusülesandeni

### Põhiküsimus

> Kas tegeleme päris ja olulise probleemiga?

Meeskonnad alustavad ühist projekti organisatsiooni `TLUHK-RIF26` repos ja GitHub Projectsis. Kõik lähtuvad kliendisoovist „Haapsalu Kolledž soovib oma tunniplaani veebilehte muuta kaasaegsemaks”. Seminaris loob iga õppija enda probleemikandidaatide Issue'i ja alustab iseseisvat tööd. Pärast individuaalsete pull request'ide ülevaatamist ja ühendamist võrdleb tiim kandidaate, valib kontrollimist vajava probleemi, valideerib selle kodutöö käigus ning koostab tõenditega põhjendatud ja piiritletud arendusülesande lähteülesande. Seminari õppematerjal koondab probleemi uurimise teooria ja tööjuhised slaidide järjekorda; teises osas tutvume ka Kanbani ja GitHub Projectsiga ning harjutame commit'i häid tavasid. Jira't ja ClickUpi nimetame samalaadsete töövahenditena.

Valmis kasutajaprobleeme, funktsioone ega kujunduslahendusi ette ei anta. Meeskonnad võivad uurida eri kasutajate ja olukordade vaatenurki. GitHub Projectsis harjutatakse ülesannete järjestamist, töö jagamist ja realistliku ajahinnangu andmist. Markdowni, muudatuste kontrolli ja Giti põhiringi kinnistame projektitöö sees; kaaslase PR-i ühendamise järel harjutame `pull`-i ning kodutöö eel esimese release'i loomist.

### Materjalid

- [Seminari materjal](../seminarid/seminar_02/01-seminar.md)
- [Laiem taustalugemine: tarkvaraarendus algusest kasutamiseni](tarkvaraarenduse-tervikprotsess.md)
- [HTML-slaidid](../seminarid/seminar_02/slides.html)
- [Kodutöö 2](../seminarid/seminar_02/03-kodutoo.md)

**Release:** `v0.1.0 – Probleem sõnastatud`

## Seminar 3: meeskond, tööviis ja süsteemi põhimõte

### Põhiküsimus

> Kuidas meeskond töötab ja millist süsteemi põhimõtteliselt kavandab?

Õppijad vaatavad projekti päris ametialaste rollide kaudu, võrdlevad Waterfalli, iteratiivset ja agiilset tööviisi, tuletavad valideeritud vajadusest kasutajalood ning kontrollitavad funktsionaalsed nõuded ja kirjeldavad nende põhjal süsteemi üldist kontseptsiooni ning kõrgtaseme arhitektuuri: peamised osad, piirid, seosed ja välised sõltuvused. Rolle vahetatakse.

### Materjalid

- [Seminari materjal](../seminarid/seminar_03/seminar.md)
- [HTML-slaidid](../seminarid/seminar_03/slides.html)
- [Kodutöö 3](../seminarid/seminar_03/homework.md)

**Release:** `v0.2.0 – Tööviis ja süsteemi kontseptsioon`

## Seminar 4: kvaliteet, riskid ja vastutus

### Põhiküsimus

> Kas kavand on piisavalt hea ja vastutustundlik?

Õppijad valivad projekti olulised kvaliteediomadused ja teevad need kontrollitavaks. Lühidalt harjutatakse testjuhtumi koostamist ning vea kordamist, põhjuse kitsendamist ja paranduse järelkontrolli. Lisaks analüüsitakse turvalisuse, privaatsuse, ligipääsetavuse, töökindluse, litsentside ja kolmandate osapoolte riske.

### Materjalid

- [Seminari materjal](../seminarid/seminar_04/seminar.md)
- [HTML-slaidid](../seminarid/seminar_04/slides.html)
- [Kodutöö 4](../seminarid/seminar_04/homework.md)

**Release:** `v0.3.0 – Kvaliteedi- ja riskiplaan`

## Seminar 5: kasutuselevõtt, käitus ja areng

### Põhiküsimus

> Mis juhtub süsteemiga pärast selle loomist?

Õppijad kavandavad kasutuselevõtu, toe, seire, tagasiside, hoolduse ja süsteemi lõpetamise põhimõtted. Nad koostavad lõpuesitluse jaoks release'ide ajajoone. Üliminimaalne AI-demo on vabatahtlik ja peab kontrollima konkreetset oletust.

### Materjalid

- [Seminari materjal](../seminarid/seminar_05/seminar.md)
- [HTML-slaidid](../seminarid/seminar_05/slides.html)
- [Kodutöö 5](../seminarid/seminar_05/homework.md)

**Release:** `v0.4.0 – Kasutuselevõtu ja arengu plaan`

## Eksam: dokumenteeritud protsessi esitlus

Meeskond esitleb projekti release'ide ajajoonena. Iga õppija selgitab vähemalt üht olulist otsust või release'i ja vastab enda panust puudutavatele küsimustele.

- [Eksami juhend](../seminarid/eksam-esitlus.md)

**Lõplik release:** `v1.0.0 – Tarkvaraarenduse protsessi tervik`

## Läbivad nõuded

- üks meeskonnarepo kogu projekti jaoks;
- iga õppija töötab enda harus, teeb sisulise commit'i ja avab pull request'i;
- iga õppija vaatab igas projektietapis üle vähemalt ühe teise õppija pull request'i;
- release manager vahetub;
- iga õppija kirjutab pärast iga projektiseminari refleksiooni;
- AI-d kasutatakse vähemalt ühe olulise otsuse juures ning selle kasu ja kontroll dokumenteeritakse;
- hinnatakse arusaamist ja põhjendamist, mitte materjali hulka.

## Mallid

- [Otsus](../seminarid/mallid/otsus.md)
- [Release notes](../seminarid/mallid/release-notes.md)
- [Individuaalne refleksioon](../seminarid/mallid/individuaalne-refleksioon.md)
- [Pull request'i kontrollnimekiri](../seminarid/mallid/pull-request.md)
