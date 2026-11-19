# Kodutöö 4: kvaliteedi- ja riskiplaan ning release `v0.3.0`

> Juhendi lingid viitavad kursuse reposse GitHubis täislinkidena, sest juhend kopeeritakse tiimi repo Issue'sse. Kui kopeerite lõike edasi, jäävad lingid tööle.

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/docs/projekti-tookorraldus.md).

Seminaris alustas tiim kolme faili: kvaliteedinõuded, testjuhtumid ja riskikaart. Kodutöö jätkab neid faile, mitte ei alusta uusi. Iga teema juurde on konspekti leht koos näitega.

## Ülesanne lühidalt

`v0.2.0` ütles, mida süsteem teeb. `v0.3.0` ütleb, kuidas me teame, et kavand on piisavalt hea, ja mis võib meid alt vedada. Tiim muudab oma kavandi kontrollitavaks: mõõdetavad kvaliteedinõuded, testjuhtumid ja põhjendatud riskid.

Töö lõpeb release'iga `v0.3.0 – Kvaliteedi- ja riskiplaan`.

## Maht

Ligikaudu 8 tundi õppija kohta.

| Tegevus | Aeg |
|---|---:|
| Rollid README-s, eelduse Issue ja ajaväljad korda | 0,5 h |
| Kvaliteedinõuded lõpuni tiimiga koos | 1,5 h |
| Testjuhtumid: tiimi ühine lõpuni ja enda oma | 1,5 h |
| Riskikaart lõpuni | 1,5 h |
| Otsus `004` ja backlog | 1 h |
| Iseseisev harjutus: vea kirjeldus ja ülevaatus | 0,5 h |
| PR, kaaslase töö ülevaatus ja parandused | 1 h |
| Refleksioon ja release | 0,5 h |

Kui tiimi Issue'de hinnangute summa ületab selle eelarve, ärge pigistage kõike sisse. Jätke osa Issue'sid backlog'i ja kirjutage release notes'i, mis ja miks jäi tegemata. See on õige otsus, mitte puudus.

## Mis on release'is `v0.3.0`

Tiimi repos:

1. **Kvaliteedinõuded** failis `requirements/quality.md`. Seminari kolmele reale lisandub neljas, kui lood seda vajavad; kokku 3–4 omadust tiimi enda kasutajalugudest. Iga omadus on mõõdetav kontrolltingimus: kes, mis olukorras, milline arv või tingimus. Mõõtmata sõnu nagu „kiiresti” või „mugavalt” ei ole. Iga piiri juures on allikas, näiteks mõõtmine praegusel lahendusel, kasutajaküsitlus või tehniline parameeter. Kui allikat pole, on piir märgitud eeldusena ja on riskikaardil. Juhend: [Mõõdetav kvaliteet](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/01-measurable-quality.md). Vastutab disainer.
2. **Testjuhtumid** failis `tests/test-cases.md`. Seminari ühine testjuhtum on lõpuni tehtud: kavandi augud on Issue'dena kirjas. Lisaks kirjutab iga õppija ühe testjuhtumi oma kasutajaloo kohta ja proovib selle kavandi peal läbi. Vähemalt üks tiimi testjuhtumitest katab vea olukorda, näiteks andmed ei lae või sisend on tühi. Juhend: [Testjuhtum](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/02-test-cases.md). Vastutab testija, kui tiim selle rolli lisas, muidu disainer.
3. **Riskikaart** failis `risks/risk-map.md`. Seminari kolmele reale lisandub vähemalt 5 muud riski; kolmeliikmelisel tiimil vähemalt 3 muud. Igal riskil on mõju, tõenäosus, kuidas märkame, maandus ja vastutav roll. Vastutaja ei ole „meeskond”. Kontrollimata eeldused on riskidest eraldi kirjas; kodutöö jooksul kontrollitud eeldus kustutatakse või muutub riskiks. Juhend: [Riskid](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/04-risks.md), mall: [riskikaart](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/seminarid/mallid/riskikaart.md). Vastutab arhitekt.
4. **Otsus** `decisions/004-kvaliteet-ja-riskid.md`. Viitab kolmele failile, nimetab vähemalt ühe kompromissi ja vähemalt ühe varasema otsuse, mis uue analüüsi põhjal kinnitati, täpsustati või muudeti. Kui riskikaart ei muuda ega kinnita ühtegi varasemat otsust, on see tehtud kodutöö pärast, mitte projekti pärast.
5. **Backlog ja tahvel.** Tahvel on töö ajal kasutusel: kaardid liiguvad ja kodutöö Issue'd on järgmise seminari alguseks Done. Seminaris loodud eelduse Issue on kas suletud vastusega või märgitud sildiga `blocked` ja kommentaariga, kellelt ja millal vastust oodatakse. Backlog'is on lisaks 2–3 toote Issue't lugudest, testjuhtumite aukudest või riskidest. Issue'd ei ole kodutöö punktid, vaid toote vajadused. Igal Issue'l on hinnang, suletutel tegelik aeg. Vastutab projektijuht.
6. **Rollid** on README-s kodutöö esimesest PR-ist alates. `v0.2.0` release manager ei ole uuesti release manager. Testija roll on vabatahtlik.
7. **Release notes** `releases/v0.3.0.md`. Osas „Planeerimine” on hinnangu ja tegeliku aja võrdlus Projectsi väljadest ning üks parandus järgmiseks etapiks. README viitab failidele `004` ja `v0.3.0`. Vastutab release manager.

Iga õppija:

- enda Issue, haru ja PR tiimi repos ning ühe kaaslase PR-i ülevaatus vähemalt ühe sisulise küsimusega kontrolli, mõju või vastutuse kohta. „Korras” ei ole ülevaatus. Kui kaaslasel on midagi valesti, näidake, kuidas parandada, ärge tehke tema eest ära. Kelle PR-i üle vaatate, on kirjas failis [student_pairs.md](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/student_pairs.md) (rida `A -> B`: A vaatab üle B töö);
- iseseisev harjutus: [vea kirjeldus ja ülevaatuse kommentaar](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/03-debugging-and-code-review.md) enda Issue'sse, koodi kirjutama ei pea;
- refleksioon `reflections/eesnimi-perenimi-v0.3.0.md` enda `SJTA` repos. Lisaks malli küsimustele üks lõik: millist selle etapi tööd võiks teha AI, kuidas tulemust kontrolliksime ja kes vastutaks;
- vabatahtlik: konspekti lehe [Giti ajalugu ja tagasivõtmine](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/06-git-history.md) harjutus tiimi repos. Seda ei hinnata, aga `git restore` on parem proovida koolitöös kui päris projektis.

## Reeglid

- **Aeg.** Hinnang pannakse välja Estimate Issue'i loomisel, tegelik aeg välja „Tegelik (h)” Issue'i sulgemisel. Ühik on tund, täpsus pool tundi.
- **Merge.** PR-i ühendab keegi teine kui autor. Ülevaataja küsimusele vastatakse enne ühendamist.
- **Blokeerija.** Kui Issue ootab infot väljastpoolt tiimi, saab see sildi `blocked` ja kommentaari: mida ootame, kellelt ja millal kontrollime uuesti. Kui takistus on teine Issue, märkige seos „Mark as blocked by”; blokeeriv Issue võib saada sildi `blocker`. Kumbki silt ei asenda teist.
- **Lingid.** Teise repo failile või Issue'le viidates kasutage täislinki. Suhteline link ja pelk `#54` töötavad ainult sama repo sees.
- **AI.** Lubatud. Pange AI-le piirid: see kirjutab lühidalt ja asjast. Pikk üldine riskiloend ei ole väärtus: eemaldage ebaoluline ja kontrollige väited. Tiim peab oma otsuseid ise seletama, ka eksamil, kus mõistete test tehakse ilma AI-ta.
- **Release manager** kontrollib enne avaldamist: iga väide release notes'is vastab failile; topelt- ja kohatäitefaile pole; AI juhiseid ega malliteksti pole; README viitab uutele otsustele. Seejärel loob ta tag'i `v0.3.0` ja GitHub Release'i pealkirjaga `Kvaliteedi- ja riskiplaan`.

## Esitamine

Lisage kodutöö Issue kommentaari lingid: release, enda PR, tehtud ülevaatus, harjutuse vastus ja refleksioon. Kasutage täislinke või kuju `ORGANISATSIOON/tiim-XX-tunniplaan#54`; pelk `#54` teises repos ei toimi. Eraldi esitamise PR-i pole vaja.

## Hindamine

Hindan tiimi ühist tulemust ja iga õppija panust. Kokku on 100 punkti.

| Kriteerium | Punktid | Mida vaatan |
|---|---:|---|
| Kvaliteedinõuded ja testjuhtumid (punktid 1–2) | 25 | Omadused tulenevad lugudest, on mõõdetavad ja piiril on allikas või eeldus. Testjuhtumid on olemas, kavandi peal läbi proovitud ja üks katab vea olukorda. |
| Riskikaart (punkt 3) | 25 | Seminaris leitud eeldus, andmeallikas ja kolmas osapool on kirjas. Riskidel on kõik väljad ja vastutajaks on roll. Eeldused on eraldi. |
| Otsus ja seos varasemaga (punkt 4) | 10 | Kompromiss ja varasema otsuse muutus või kinnitus on põhjendatud. |
| Planeerimine (punktid 5–7) | 10 | Tahvel on kasutusel, eelduse Issue on lahendatud või blokeerituks märgitud, backlog tuleb tootest, hinnangu ja tegeliku aja võrdlus on release notes'is. |
| Iga õppija panus | 10 | Issue, PR, sisuline ülevaatus ja harjutuse vastus on repost leitavad. PR-i ühendas keegi teine. |
| Refleksioon ja AI | 10 | Refleksioon kirjeldab panust, õpitut ja AI küsimust. AI väited on kontrollitud. |
| Release ja repo korrastatus | 10 | Kontrollnimekiri on läbitud, failid on õiges kohas ja release `v0.3.0` on avaldatud. |

Kuni 5 lisapunkti saab tiim, kes jätab hinnangute summa tõttu Issue'sid teadlikult backlog'i ja põhjendab seda release notes'is.

**Tulemuse tõlgendamine:** 90–100 tähendab põhjendatud ja jälgitavat tööd; 75–89 puhul vajab mõni osa täiendamist; 60–74 puhul takistab oluline lünk järgmises seminaris jätkamist; alla 60 ei ole kvaliteeti ja riske piisavalt analüüsitud või panust ei saa repo põhjal hinnata.

Kvaliteedinõuete ja riskikaardi eest peab saama kokku vähemalt 25 punkti. Dokumentide hulga, tehnilise keerukuse ega rakenduse eest eraldi punkte ei anta.
