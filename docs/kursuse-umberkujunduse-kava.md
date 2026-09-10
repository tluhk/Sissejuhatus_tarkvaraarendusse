# Kursuse ümberkujundamise kava

> **Staatus:** kinnitatud lähteplaan. Aktiivne õppijale suunatud ülevaade asub failis [kursuseprogramm.md](kursuseprogramm.md).

## 1. Ümberkujundamise eesmärk

Kursuse keskne tulemus on:

> Õppija mõistab tarkvaraarendust tervikliku meeskondliku protsessina, mitte ainult programmeerimisena.

Kursus ei korda põhjalikult kasutajauuringu, UX-disaini, programmeerimise, testimise ega arhitektuuri eraldi kursusi. Neid valdkondi käsitletakse nii palju, et õppija:

- näeb nende rolli tarkvaraarenduse tervikus;
- tunneb ära ametialased rollid ja nende vastutuse;
- oskab kaasata sobiva rolli vaatenurga;
- mõistab otsuste põhjuseid, riske ja kompromisse;
- oskab selgitada, kuidas uus info varasemaid otsuseid muudab.

## 2. Kursuse läbiv projekt

Seminaris 2 moodustatakse meeskonnad. Iga meeskond valib enda leitud pärisprobleemi ja töötab sama projektiga kursuse lõpuni.

Projekti tulemus ei ole töötav rakendus. Tulemus on dokumenteeritud tarkvaraarenduse protsess, mis näitab meeskonna mõtlemist.

Probleemi võib kursuse jooksul täpsustada. Projekti vahetamine on põhjendatud ainult siis, kui kogutud info näitab, et esialgne probleem ei ole tegelik või sobiv. Ka selline muutus dokumenteeritakse otsusena.

### Keskne artefakt

Keskne artefakt on otsuste logi. Skeem, süsteemikirjeldus või muu lisamaterjal luuakse ainult siis, kui see aitab otsust selgitada.

Iga oluline otsus vastab järgmistele küsimustele:

1. Milline probleem, vajadus või uus info otsuse põhjustas?
2. Milliseid variante me kaalusime?
3. Mida me valisime?
4. Miks me selle valisime?
5. Kellele ja millist väärtust see loob?
6. Millised riskid või kompromissid kaasnevad?
7. Milline uus info võiks otsust muuta?
8. Milliste ametialaste rollide vaatenurki arvestasime?

## 3. Git ja GitHub kui läbiv töökeskkond

Kogu projekt tehakse GitHubi repositooriumis. Git ja GitHub ei ole eraldi peatükk, vaid meeskonna igapäevane töökeskkond.

Õppijad kasutavad kursuse jooksul vähemalt järgmisi töövõtteid:

- repositooriumi kloonimine;
- Markdown-dokumentide muutmine;
- muudatuste ülevaatamine;
- sisuliste commit'ide tegemine;
- push ja pull;
- harud ning pull request'id;
- koodi või dokumentatsiooni ülevaatus;
- GitHub Issues tööülesannete jaoks;
- tag'id ja GitHub Releases;
- release notes.

Esimene seminar õpetab individuaalse commit'i ja push'i töövoogu. Meeskonnarepositoorium, harud, pull request'id ja release'id algavad seminaris 2 ning muutuvad sammhaaval iseseisvamaks.

### Meeskonnarepositooriumid

Projektirepositooriumid luuakse ühises `TLUHK-RIF26` organisatsioonis. Igal meeskonnal on üks ühine repositoorium. Repositoorium ei kuulu ühe õppija isiklikule kontole ega organisatsioonile.

Kõigil meeskonnaliikmetel on repositooriumis tööks vajalik ligipääs. Iga õppija:

1. kloonib meeskonna repositooriumi;
2. loob enda ülesande jaoks haru;
3. teeb enda muudatused ja commit'id;
4. push'ib haru GitHubi;
5. avab pull request'i;
6. osaleb vähemalt ühe teise õppija töö ülevaatuses;
7. parandab vajaduse korral enda tööd tagasiside põhjal.

Release manageri vastutus vahetub iga projektiseminari järel. Release manager kontrollib, et kokku lepitud muudatused on üle vaadatud ja ühendatud, release notes on valmis ning release viitab õigele commit'ile. Release manager ei kirjuta üksinda kogu release'i sisu.

Individuaalne refleksioon asub meeskonna repositooriumis, kuid õppija lisab selle enda haru ja pull request'iga. Nii jäävad ühine projekt ja iga õppija panus samasse kontrollitavasse ajalukku.

## 4. Release'ide süsteem

Seminarid 2–5 lõppevad kodutööna vormistatud release'iga. Release tähistab kontrollitud hetkeseisu, mitte kogu teema lõplikku valmimist.

| Etapp | Tag | Release'i pealkiri | Põhiküsimus |
|---|---|---|---|
| Seminar 2 | `v0.1.0` | Probleem sõnastatud | Kas tegeleme päris ja olulise probleemiga? |
| Seminar 3 | `v0.2.0` | Tööviis ja süsteemi kontseptsioon | Kuidas meeskond töötab ja millist süsteemi põhimõtteliselt kavandab? |
| Seminar 4 | `v0.3.0` | Kvaliteedi- ja riskiplaan | Kas kavand on piisavalt hea ja vastutustundlik? |
| Seminar 5 | `v0.4.0` | Kasutuselevõtu ja arengu plaan | Mis juhtub süsteemiga pärast selle loomist? |
| Eksam | `v1.0.0` | Tarkvaraarenduse protsessi tervik | Kuidas meeskonna arusaam ja otsused arenesid? |

Iga release sisaldab vähemalt:

- etapi olulisi otsuseid;
- otsuste põhjendusi ja kaalutud alternatiive;
- uut infot ning sellest tulenenud muudatusi;
- lahtisi küsimusi ja järgmisi samme;
- release notes'i;
- iga õppija individuaalset refleksiooni.

## 5. Seminaride ülesehitus

Kõik seminarid kestavad kaks korda 90 minutit. Projektiseminaris jäetakse vähemalt 15 minutit tehnilisteks tõrgeteks ja töö lõpetamise korraldamiseks.

### Seminar 1: suur pilt ja töövahendid

**Staatus:** olemasolev 2026. aasta materjal jääb põhiosas kehtima.

**Eesmärk:** õppija mõistab tarkvaraarenduse suurt pilti ja saab tööle kursusel vajaliku arenduskeskkonna.

**Põhiteemad:**

- tarkvara ja tarkvaraarendus;
- tarkvaraarenduse elutsükkel;
- AI mõju arendusprotsessile;
- VS Code, terminal ja käsukest;
- Git, GitHub ja GitHub CLI;
- Markdown;
- Node.js ja Docker tervikpildi tasandil;
- esimene individuaalne commit ja push.

**Kodutöö:** individuaalne arenduskeskkonna dokumenteerimine. Esimeses seminaris release'i ei tehta.

### Seminar 2: probleemi leidmine

**Eesmärk:** meeskond leiab enda ümbrusest probleemi, eristab selle lahendusideest ja kontrollib probleemi vähemalt ühe sõltumatu tõendiga.

**Mida ei õpetata süvitsi:** kasutajauuringu tervikmetoodika, põhjalik intervjuutehnika ega konkurentsianalüüs.

**I osa, 90 minutit:**

| Tegevus | Aeg |
|---|---:|
| Eelmise seminari kontroll ja päeva eesmärk | 10 min |
| Probleem ja lahendusidee: eristamine näidete abil | 20 min |
| Kust probleeme leida: igapäevaelu, tööprotsessid, vead ja viivitused | 20 min |
| Päris juhtumiuuringu lühianalüüs | 15 min |
| Individuaalne probleemide kaardistus | 15 min |
| Puhver | 10 min |

**II osa, 90 minutit:**

| Tegevus | Aeg |
|---|---:|
| Meeskonnad, ligipääs ja repo kloonimine | 20 min |
| Probleemikandidaatide võrdlemine | 10 min |
| Valikukriteeriumid ja esimese otsuse vormistamine | 10 min |
| Kerge valideerimise kavand | 10 min |
| GitHubi töövoog: Project, Issue, haru, commit, PR, ülevaatus ja pull | 30 min |
| Kodutöö, refleksioon ja release `v0.1.0` | 10 min |

**Kodutöö maht õppija kohta:** ligikaudu 8 tundi.

- probleemide märkamine ja kirjeldamine: 2 h;
- meeskonna kandidaatide võrdlemine: 1 h;
- üks vestlus või muu sõltumatu kontroll: 2 h;
- tulemuste analüüs ja probleemi täpsustamine: 1 h;
- otsuste logi ja release notes: 1 h;
- individuaalne refleksioon: 1 h.

**Release:** `v0.1.0 – Probleem sõnastatud`.

### Seminar 3: meeskond, tööviis ja süsteemi põhimõte

**Eesmärk:** õppija mõistab päris ametialaste rollide vastutust, võrdleb tööviise ning osaleb süsteemi üldise kontseptsiooni põhjendamises.

**Mida ei õpetata süvitsi:** ühe metoodika täielik rakendamine, detailne projektijuhtimine ega tehnoloogiapinu kavandamine.

**I osa, 90 minutit:**

| Tegevus | Aeg |
|---|---:|
| Release'i `v0.1.0` ülevaade | 15 min |
| Ametialased rollid ja vastutuse piirid | 20 min |
| Waterfall, iteratiivne arendus, Scrum, Kanban ja Lean | 25 min |
| Päris juhtumiuuringu lühianalüüs | 15 min |
| Rollide jagamine ja vaatenurkade harjutus | 10 min |
| Puhver | 5 min |

**II osa, 90 minutit:**

| Tegevus | Aeg |
|---|---:|
| Meeskonna tööviisi variantide võrdlemine | 20 min |
| Algse tööviisi valik ja põhjendus | 15 min |
| Süsteemi eesmärk, piir ja suuremad osad | 20 min |
| Rollide vaatenurkade konflikt ja kompromiss | 15 min |
| Otsuste logi ning GitHubi ülevaatus | 10 min |
| Kodutöö ja release `v0.2.0` | 10 min |

Meeskond võib tööviisi hiljem muuta. Nii algne valik kui ka muutmine peavad olema otsuste logis põhjendatud.

**Kodutöö maht õppija kohta:** ligikaudu 8 tundi. Põhirõhk on süsteemi kontseptsiooni, tööviisi ja rollidest tulenevate valikute põhjendamisel, individuaalsel refleksioonil ning release'i vormistamisel.

**Release:** `v0.2.0 – Tööviis ja süsteemi kontseptsioon`.

### Seminar 4: kvaliteet, riskid ja vastutus

**Eesmärk:** õppija mõistab, et töötav lahendus ei pruugi olla kvaliteetne, turvaline, õiglane ega jätkusuutlik.

**Mida ei õpetata süvitsi:** testide programmeerimine, turbeaudit, UX-testimise metoodika ega litsentsiõiguse detailid.

**I osa, 90 minutit:**

| Tegevus | Aeg |
|---|---:|
| Release'i `v0.2.0` ülevaade ja rollide vahetus | 15 min |
| Kvaliteet kasutaja, arendaja ja organisatsiooni vaates | 20 min |
| Funktsionaalsed ja mittefunktsionaalsed vajadused | 15 min |
| Turvalisus, privaatsus, ligipääsetavus ja töökindlus | 20 min |
| Päris juhtumiuuringu lühianalüüs | 15 min |
| Puhver | 5 min |

**II osa, 90 minutit:**

| Tegevus | Aeg |
|---|---:|
| Projekti kvaliteedikriteeriumide valik | 20 min |
| Riskide ja vastutuse kaardistus | 20 min |
| Kontrollimise põhimõte: kuidas saame teada, kas otsus töötab? | 15 min |
| Litsentside ning kolmandate osapoolte vara mõju | 10 min |
| Dokumentatsiooni või koodi ülevaatuse harjutus | 10 min |
| Kodutöö ja release `v0.3.0` | 10 min |
| Puhver | 5 min |

**Kodutöö maht õppija kohta:** ligikaudu 8 tundi. Meeskond põhjendab valitud kvaliteedikriteeriume, olulisemaid riske, kontrollimise viise ja vastutust. Iga õppija lisab rollipõhise refleksiooni.

**Release:** `v0.3.0 – Kvaliteedi- ja riskiplaan`.

### Seminar 5: kasutuselevõtt, muutused ja hooldus

**Eesmärk:** õppija mõistab, et tarkvaraarendus jätkub pärast esimese versiooni loomist ning hõlmab kasutuselevõttu, jälgimist, muutmist, hooldust ja kasutusest eemaldamist.

**Mida ei õpetata süvitsi:** pilveplatvormi seadistamine, CI/CD tehniline ehitamine ega monitooringutööriista kasutamine.

**I osa, 90 minutit:**

| Tegevus | Aeg |
|---|---:|
| Release'i `v0.3.0` ülevaade ja rollide vahetus | 15 min |
| Kasutuselevõtt ja muudatuste juhtimine | 20 min |
| Tagasiside, jälgimine ja mõju | 20 min |
| Päris juhtumiuuringu lühianalüüs | 15 min |
| Hooldus, tehniline võlg ja kasutusest eemaldamine | 15 min |
| Puhver | 5 min |

**II osa, 90 minutit:**

| Tegevus | Aeg |
|---|---:|
| Kasutuselevõtu ja toe plaan | 20 min |
| Mõõdikute ning tagasiside valik | 15 min |
| Hooldus- ja lõpetamisotsus | 15 min |
| Vabatahtliku AI-demo otsus | 10 min |
| Release'ide ajajoon | 15 min |
| Kodutöö, release `v0.4.0` ja eksamiks valmistumine | 15 min |

AI-demo ei ole hinnatav toode ega kohustuslik seminariosa. Meeskond otsustab, kas üliminimaalne demo aitaks mõnd olulist oletust kontrollida, ning piirab selle ajakulu enne alustamist.

**Kodutöö maht õppija kohta:** ligikaudu 8 tundi. Meeskond lõpetab kasutuselevõtu ja arengu plaani, hindab demo tulemust juhul, kui demo tehti, ning valmistab release'ide ajajoone lõpuesitluseks.

**Release:** `v0.4.0 – Kasutuselevõtu ja arengu plaan`.

### Eksam: dokumenteeritud protsessi esitlus

**Lõplik release:** `v1.0.0 – Tarkvaraarenduse protsessi tervik`.

Esitlus järgib release'ide ajajoont. Meeskond võib ebaolulistest sündmustest üle hüpata, kuid peab näitama:

- millest alustati;
- millised otsused olid kõige olulisemad;
- milliseid alternatiive kaaluti;
- milline uus info arusaama muutis;
- miks otsuseid muudeti;
- millise süsteemi kontseptsioonini jõuti;
- mida õpiti päris juhtumiuuringutega võrdlemisest;
- mida õpiti AI kasulikkusest ja piiridest.

Iga meeskonnaliige esitleb vähemalt ühte release'i või olulist otsust ning vastab enda panust puudutavatele küsimustele.

## 6. Rollide vahetamine

Kasutatakse päris ametinimetusi. Rolli selgitatakse vastutuse, mitte stereotüüpse ülesannete nimekirja kaudu.

Võimalikud rollid:

- Product Owner;
- projektijuht või Scrum Master;
- UX-disainer;
- tarkvaraarhitekt;
- arendaja;
- testija või QA spetsialist.

Rollid vahetuvad vähemalt iga projektiseminari järel. Kui meeskonnas on rolle rohkem kui liikmeid, võib üks õppija kanda kaht seotud rolli või jätta mõne rolli konkreetses etapis vaatleja rolliks.

Iga otsuse juures märgitakse, milliste rollide vaatenurki arvestati ja milline kompromiss erinevate vajaduste vahel tehti.

## 7. Individuaalne refleksioon

Iga õppija lisab iga release'i juurde lühikese individuaalse refleksiooni.

Refleksioon vastab vähemalt järgmistele küsimustele:

1. Millist rolli ma selles etapis täitsin?
2. Millist otsust ma mõjutasin ja kuidas?
3. Milline teise rolli vaatenurk muutis minu arvamust?
4. Mida ma selle etapi jooksul tarkvaraarendusest paremini mõistsin?
5. Mida teeksin järgmises etapis teisiti?

Refleksioon ei ole tegevuste päevik. Hinnatakse õppija arusaama muutumist ja võimet enda panust põhjendada.

## 8. AI kasutamise põhimõte

AI kasutamine on lubatud. Iga meeskond peab kasutama AI-d vähemalt ühe olulise otsuse juures ning analüüsima selle tegelikku kasu.

Kui AI mõjutas otsust, lisatakse otsuse juurde:

- milleks AI-d kasutati;
- milline sisend anti;
- mida tulemusest kasutati;
- mida jäeti kõrvale ja miks;
- kuidas tulemust kontrolliti;
- milline oli AI tegelik kasu;
- kas AI vähendas tööd või tekitas kontrollimise tõttu lisatööd.

AI väljundi maht ei näita kvaliteeti. Suur kogus kontrollimata, korduvat või ebaolulist materjali on puudus. Õppija peab suutma kogu esitatud sisu oma sõnadega selgitada.

## 9. Päris juhtumiuuringud

Iga projektiseminar sisaldab võimaluse korral 10–15-minutilist pärisprojekti peeglit.

Sobiv juhtum:

- kirjeldab tegelikku probleemi ja konteksti;
- näitab vähemalt üht tehtud otsust;
- toob välja raskuse, riski või kompromissi;
- seostub seminari põhiküsimusega;
- on lühendatav 10–15-minutiliseks aruteluks;
- põhineb kontrollitaval allikal.

Kõik näited ei pea pärinema erinevatest projektidest. Ühte hästi dokumenteeritud projekti võib jälgida mitmes seminaris. Kui algallikas on liiga pikk, valmistab õppejõud ette lühikese kokkuvõtte ja viitab originaalallikale.

Juhtumiuuringud tuleb järgmises tööetapis alles leida ja sobivust hinnata.

## 10. Soovituslik repositooriumi struktuur

```text
projekt/
├── README.md
├── decisions/
│   ├── 001-probleemi-valik.md
│   ├── 002-tooviisi-valik.md
│   └── ...
├── releases/
│   ├── v0.1.0.md
│   ├── v0.2.0.md
│   ├── v0.3.0.md
│   └── v0.4.0.md
├── reflections/
│   ├── oppija-nimi-v0.1.0.md
│   └── ...
├── diagrams/
└── final-presentation/
    └── README.md
```

Failistruktuur peab jääma lihtsaks. Uut faili ei looda ainult selleks, et dokumentide arv oleks suurem.

## 11. Hindamine

Hindamise keskmes on arusaamine ja põhjendamine.

| Hinnatav osa | Osakaal |
|---|---:|
| Meeskonna otsuste logi ja release'ide sisuline areng | 40% |
| Individuaalsed refleksioonid ja rollide mõistmine | 25% |
| GitHubi ja Giti läbipaistev koostöövoog | 15% |
| Lõpuesitlus ja küsimustele vastamine | 20% |
| **Kokku** | **100%** |

Kõigis osades hinnatakse eelkõige:

- probleemist lähtumist;
- valikute põhjendamist;
- alternatiivide ja kompromisside kaalumist;
- uue info põhjal õppimist;
- rollide vastutuse mõistmist;
- esitatud töö oma sõnadega selgitamist.

Dokumentide arv, teksti pikkus, tehniline keerukus, AI väljundi maht ega esitluse visuaalne viimistlus ei asenda sisulist arusaamist.

## 12. Seos kehtivate õpiväljunditega

| Õpiväljund | Kuidas kavand seda toetab |
|---|---|
| Tarkvara, arhitektuuri ja arendusprotsesside põhimõtete selgitamine | Suur pilt, SDLC, tööviiside võrdlus, rollid ja süsteemi üldine kontseptsioon |
| Tarkvara litsentsimise mõju kirjeldamine | Litsentside ning kolmandate osapoolte vara mõju kvaliteedi- ja vastutusetapis |
| Versioonihalduse kasutamine meeskonnatöös | Läbiv meeskonnatöö GitHubis, harud, pull request'id, ülevaatused, tag'id ja release'id |
| Heade arendustavade rakendamine | Dokumenteerimine, ülevaatus, kvaliteedikriteeriumid, riskid ja jätkusuutlikkus |
| Enda töövoo planeerimine ja juhtimine | Meeskonna tööviisi valik, Issues, ülesannete jaotus, vahe-eesmärgid ning release'ide tähtajad |

## 13. Edasiseks täpsustatavad korraldusküsimused

1. Mitu õppijat on tavaliselt ühes meeskonnas?
2. Milline on meeskonnarepositooriumide lõplik nimetamise reegel organisatsioonis `TLUHK-RIF26`?
3. Millised seminaride ja eksami kuupäevad lisatakse õppijate materjalidesse?
4. Kas valikuline AI-demo mahub rühmade tegeliku töötempo juures seminariaega?

## 14. Rakendatud materjalid

- [Seminar 2](../seminarid/seminar_02/seminar.md) ja `v0.1.0`
- [Seminar 3](../seminarid/seminar_03/seminar.md) ja `v0.2.0`
- [Seminar 4](../seminarid/seminar_04/seminar.md) ja `v0.3.0`
- [Seminar 5](../seminarid/seminar_05/seminar.md) ja `v0.4.0`
- [Eksam](../seminarid/eksam-esitlus.md) ja `v1.0.0`
- [Ühised mallid](../seminarid/mallid/README.md)
