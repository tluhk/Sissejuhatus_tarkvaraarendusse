# Kodutöö 4: kvaliteedi- ja riskiplaan ning release `v0.3.0`
> Juhendi lingid viitavad kursuse reposse GitHubis täislinkidena, sest juhend kopeeritakse tiimi repo Issue'sse. Kui kopeerite lõike edasi, jäävad lingid tööle.

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/docs/projekti-tookorraldus.md).

Seminar 4 oli loeng ja üks tiimiülesanne: „Selgita oma otsust”. Kvaliteedinõuete, testjuhtumi ja riskikaardi harjutused jäid seminaris tegemata. Need teeb tiim nüüd ise. Iga teema juurde on konspekti leht koos näitega.

## Ülesanne lühidalt

`v0.2.0` ütles, mida süsteem teeb. `v0.3.0` ütleb, kuidas me teame, et kavand on piisavalt hea, ja mis võib meid alt vedada. Tiim muudab oma kavandi kontrollitavaks: mõõdetavad kvaliteedinõuded, testjuhtumid ja põhjendatud riskid.

Töö lõpeb release'iga `v0.3.0 – Kvaliteedi- ja riskiplaan`.

## Maht

Ligikaudu 8–10 tundi õppija kohta.

| Tegevus | Aeg |
|---|---:|
| Seminari ülesande vastus reposse, rollid README-s, Projectsi väljad | 1 h |
| Kvaliteedinõuded tiimiga koos | 2 h |
| Testjuhtumid: tiimi ühine ja enda oma | 1,5 h |
| Riskikaart | 2 h |
| Iseseisev harjutus: vea kirjeldus ja ülevaatus | 0,5 h |
| PR, kaaslase töö ülevaatus ja parandused | 1 h |
| Refleksioon ja release | 1 h |

Kui tiimi Issue'de hinnangute summa ületab selle eelarve, ärge pigistage kõike sisse. Jätke osa Issue'sid backlog'i ja kirjutage release notes'i, mis ja miks jäi tegemata. See on õige otsus, mitte puudus.

## Mis on release'is `v0.3.0`

Tiimi repos:

1. **Seminari ülesande vastus.** Kolme küsimuse vastused, mille tiim seminaris esitas, lähevad faili `releases/v0.3.0.md` lõppu osana „Seminari ülesanne”. Küsimused on failis [kodutoo-esitlus.md](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/seminarid/seminar_04/kodutoo-esitlus.md). Kui vastus on juba Discordis või mujal kirjas, kopeerige see. Suurim kontrollimata eeldus läheb riskikaardi esimeseks reaks.
2. **Kvaliteedinõuded.** 3–4 kvaliteediomadust, mis tulenevad tiimi enda kasutajalugudest. Iga omadus on kirjas mõõdetava kontrolltingimusena: kes, mis olukorras, milline arv või tingimus. Mõõtmata sõnu nagu „kiiresti” või „mugavalt” ei ole. Arv ei tule peast: iga piiri juures on kirjas, kust see tuleb, näiteks kasutajaküsitlus, tehniline parameeter või teadaolev soovitus. Kui allikat veel pole, on piir märgitud eeldusena ja läheb riskikaardile. Juhend: [Mõõdetav kvaliteet](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/01-measurable-quality.md). Vastutab disainer.
3. **Testjuhtumid.** Tiim kirjutab koos ühe testjuhtumi oma põhilise kasutajaloo kohta. Lisaks kirjutab iga õppija ühe testjuhtumi oma kasutajaloo kohta. Vähemalt üks tiimi testjuhtumitest katab vea olukorda, näiteks andmed ei lae või sisend on tühi. Igal testjuhtumil on test, eeldused, sammud ja oodatud tulemus. Test tehakse kavandi peal: kui kavand annab vastuse, on test läbitud; kui ei anna, on kavandis auk ja sellest saab Issue. Juhend: [Testjuhtum](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/02-test-cases.md).
4. **Riskikaart.** Üks risk tunniplaani andmeallika kohta ja vähemalt 5 muud riski; kolmeliikmelisel tiimil vähemalt 3 muud. Üks rida on kolmanda osapoole kohta, millest lahendus sõltub, näiteks pilveteenus, andmeallikas, teek või AI-mudel, koos märkega, kas litsentsi või kasutustingimusi on kontrollitud. Igal riskil on mõju, tõenäosus, kuidas märkame, maandus ja vastutav roll. Vastutaja ei ole „meeskond”. Kontrollimata eeldused on riskidest eraldi kirjas. Kasutage [riskikaardi malli](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/seminarid/mallid/riskikaart.md); juhend: [Riskid](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/04-risks.md). Vastutab arhitekt.
5. **Otsus** `decisions/004-kvaliteet-ja-riskid.md`. Sisaldab kvaliteedinõuded ja riskikaardi või viitab nende failidele. Nimetab vähemalt ühe kompromissi ja vähemalt ühe varasema otsuse, mis uue analüüsi põhjal kinnitati, täpsustati või muudeti. Kui riskikaart ei muuda ega kinnita ühtegi varasemat otsust, on see tehtud kodutöö pärast, mitte projekti pärast.
6. **Backlog ja tahvel.** Kanbani tahvel on töö ajal kasutusel: kaardid liiguvad ja kodutöö Issue'd on järgmise seminari alguseks Done. Backlog'is on 2–3 toote Issue't, mis tulenevad lugudest või riskidest, ning Issue seminaris leitud eelduse kontrollimiseks: kellelt küsime ja millal. Issue'd ei ole kodutöö punktid, vaid toote vajadused. Igal Issue'l on hinnang, suletutel tegelik aeg. Vastutab projektijuht.
7. **Rollid.** Rollid vahetuvad kodutöö jooksul ja on kirjas README-s. `v0.2.0` release manager ei ole uuesti release manager. Kui tiim soovib, lisab ta testija rolli, kes vastutab testjuhtumite eest.
8. **Release notes** `releases/v0.3.0.md`. Osas „Planeerimine” on hinnangu ja tegeliku aja võrdlus Projectsi väljadest ning üks parandus järgmiseks etapiks. Lõpus on seminari ülesande vastus. README viitab failidele `004` ja `v0.3.0`. Vastutab release manager.

Iga õppija:

- enda Issue, haru ja PR tiimi repos ning ühe kaaslase PR-i ülevaatus vähemalt ühe sisulise küsimusega kontrolli, mõju või vastutuse kohta. „Korras” ei ole ülevaatus. Kui kaaslasel on midagi valesti, näidake, kuidas parandada, ärge tehke tema eest ära;
- iseseisev harjutus: [vea kirjeldus ja ülevaatuse kommentaar](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/03-debugging-and-code-review.md) enda Issue'sse, koodi kirjutama ei pea;
- refleksioon `reflections/eesnimi-perenimi-v0.3.0.md` enda `SJTA` repos. Lisaks malli küsimustele üks lõik seminari lõpuküsimusest: millist selle etapi tööd võiks teha AI, kuidas tulemust kontrolliksime ja kes vastutaks;
- vabatahtlik: konspekti lehe [Giti ajalugu ja tagasivõtmine](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/handbook/04-quality-and-risk/06-git-history.md) harjutus tiimi repos. Seda ei hinnata, aga `git restore` on parem proovida koolitöös kui päris projektis.

## Reeglid

- **Aeg.** Hinnang pannakse välja Estimate Issue'i loomisel, tegelik aeg välja „Tegelik (h)” Issue'i sulgemisel. Ühik on tund, täpsus pool tundi. Kui tiimil välja „Tegelik (h)” veel pole, lisab projektijuht selle Projectsi seadetest.
- **Merge.** PR-i ühendab keegi teine kui autor. Ülevaataja küsimusele vastatakse enne ühendamist.
- **Blokeerija.** Kui Issue ootab infot väljastpoolt tiimi, saab see sildi `blocked` ja kommentaari: mida ootame, kellelt ja millal kontrollime uuesti. Kui takistus on teine Issue, märkige seos „Mark as blocked by”. Seminaris nägite silti `blocker` blokeeriva Issue peal; see on sama seose teine ots ja näitab, mis tuleb enne ära teha.
- **Lingid.** Teise repo failile või Issue'le viidates kasutage täislinki. Suhteline link ja pelk `#54` töötavad ainult sama repo sees.
- **AI.** Lubatud. Pange AI-le piirid: see kirjutab lühidalt ja asjast. Kui te ise ei saa aru, mis sinna kirja läks, on see halvem kui lühem oma tekst. Pikk üldine riskiloend ei ole väärtus: eemaldage ebaoluline ja kontrollige väited. Tiim peab oma otsuseid ise seletama, ka eksamil, kus mõistete test tehakse ilma AI-ta.
- **Release manager** kontrollib enne avaldamist: iga väide release notes'is vastab failile; topelt- ja kohatäitefaile pole; AI juhiseid ega malliteksti pole; README viitab uutele otsustele. Seejärel loob ta tag'i `v0.3.0` ja GitHub Release'i pealkirjaga `Kvaliteedi- ja riskiplaan`.

## Esitamine

Lisage kodutöö Issue kommentaari lingid: release, enda PR, tehtud ülevaatus, harjutuse vastus ja refleksioon. Kasutage täislinke või kuju `TLUHK-RIF26/tiim-XX-tunniplaan#54`; pelk `#54` teises repos ei toimi. Eraldi esitamise PR-i pole vaja.

## Hindamine

Hindan tiimi ühist tulemust ja iga õppija panust. Kokku on 100 punkti.

| Kriteerium | Punktid | Mida vaatan |
|---|---:|---|
| Kvaliteedinõuded ja testjuhtumid (punktid 2–3) | 25 | Omadused tulenevad lugudest, on mõõdetavad ja piiril on allikas või eeldus. Testjuhtumid on olemas, kontrollitavad ja üks katab vea olukorda. |
| Riskikaart (punkt 4) | 25 | Andmeallika risk ja seminaris leitud eeldus on kirjas. Riskidel on kõik väljad ja vastutajaks on roll. Eeldused on eraldi. |
| Otsus ja seos varasemaga (punkt 5) | 10 | Kompromiss ja varasema otsuse muutus või kinnitus on põhjendatud. |
| Planeerimine (punktid 1, 6–8) | 10 | Tahvel on kasutusel, backlog tuleb tootest, hinnangu ja tegeliku aja võrdlus ning seminari ülesande vastus on release notes'is. |
| Iga õppija panus | 10 | Issue, PR, sisuline ülevaatus ja harjutuse vastus on repost leitavad. PR-i ühendas keegi teine. |
| Refleksioon ja AI | 10 | Refleksioon kirjeldab panust, õpitut ja AI küsimust. AI väited on kontrollitud. |
| Release ja repo korrastatus | 10 | Kontrollnimekiri on läbitud, failid on õiges kohas ja release `v0.3.0` on avaldatud. |

Kuni 5 lisapunkti saab tiim, kes jätab hinnangute summa tõttu Issue'sid teadlikult backlog'i ja põhjendab seda release notes'is.

**Tulemuse tõlgendamine:** 90–100 tähendab põhjendatud ja jälgitavat tööd; 75–89 puhul vajab mõni osa täiendamist; 60–74 puhul takistab oluline lünk järgmises seminaris jätkamist; alla 60 ei ole kvaliteeti ja riske piisavalt analüüsitud või panust ei saa repo põhjal hinnata.

Kvaliteedinõuete ja riskikaardi eest peab saama kokku vähemalt 25 punkti. Dokumentide hulga, tehnilise keerukuse ega rakenduse eest eraldi punkte ei anta.
