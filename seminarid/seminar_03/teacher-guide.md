# Õpetaja juhend: seminar 3

## Fookus

Seminar ei ole Scrumi kiirkursus ega detailse tehnilise arhitektuuri harjutus. Tööviise ja rolle on seminarides 1–2 juba tutvustatud: ära õpeta neid uuesti, vaid lase õppijatel neid oma projektis rakendada. Õppijad teevad süsteemist kõrgtaseme arhitektuurikirjelduse. Fookus on sellel, kuidas rollid ja tööviis aitavad ebakindluse tingimustes põhjendatud otsuseid teha.

## I osa, 90 minutit

| Tegevus | Aeg |
|---|---:|
| Release `v0.1.0` ülevaade | 10 min |
| Ametialased rollid: meenutus ja vaatenurkade kasutamine | 10 min |
| Kasutajalood ja kontrollitavad funktsionaalsed nõuded | 15 min |
| Lühijutt: kuidas AI arendust muudab | 5 min |
| Waterfalli ja agiilse lähenemise meenutus; Scrum, Kanban, iteratiivsus ja Lean | 11 min |
| GOV.UK alpha juhtum | 14 min |
| Rollide jagamine ja vaatenurgad | 5 min |
| Tööviisi variantide võrdlus | 15 min |
| Puhver | 5 min |

## II osa, 90 minutit

| Tegevus | Aeg |
|---|---:|
| Valik ja põhjendus | 10 min |
| Töö planeerimine: backlog, järjestus, vastutajad ja ajahinnangud | 20 min |
| Kasutajalugude seos kasutaja teekonna, süsteemi eesmärgi, piiri ja kõrgtaseme arhitektuuriga | 15 min |
| Rollikonflikt ja kompromiss | 10 min |
| Merge-konflikti harjutus terminalis | 15 min |
| Otsuste logi, commit'i sõnum ja PR-i ülevaatus | 10 min |
| Kodutöö ja release | 10 min |

## Küsimused, millega meeskonda tagasi suunata

- Millist riski see valik vähendab?
- Mis peab olema tõsi, et otsus toimiks?
- Kes näeb seda otsust teise nurga alt?
- Miks jääb see osa süsteemi sisse või välja?
- Milline uus info paneks teid otsust muutma?

## Ohukohad

- Õppijad valivad Scrumi, sest nimi on tuttav. Küsi, millist konkreetset probleemi iga võte lahendab.
- Arhitektuur muutub tehnoloogiate loeteluks. Too arutelu tagasi eesmärgi, osaliste, piiri ja info liikumise juurde.
- Kasutajalugu muutub lahenduse reklaamiks või AI pakutud funktsiooniks. Küsi, milline seminaris 2 kogutud tõend seda vajadust toetab.
- Backlog jääb soovide nimekirjaks. Küsi, mis on järgmine töö, kes selle teeb ja kui kaua see võtab.
- Kasutaja teekonnast saab ekraanide kujundus. Too arutelu tagasi sammude juurde, mida kasutaja oma eesmärgi saavutamiseks teeb.
- Rollid muutuvad tiitliteks. Nõua igalt rollilt vähemalt üht sisulist küsimust või vastuväidet.
- Üks õppija kirjutab kõik. Kontrolli PR-ide ja ülevaatuste ajalugu.

## Merge-konflikti harjutus

Iga tiim teeb harjutuse ühe paariga, teised loevad käske ette ja jälgivad. Tiim loob ühe Issue'i (näites `#20`). Mõlemad õppijad loovad sellest haru, näiteks `issue-20-conflict-a` ja `issue-20-conflict-b`, ning muudavad README-s sama rida. Kui esimene PR on ühendatud, teeb teine slaidil olevad sammud ja tiim otsustab, milline tekst jääb. Seejärel vaatab esimene õppija teise PR-i üle ja see ühendatakse.

Kui aega jääb üle, vahetab järgmine paar. Täpne juhend õppijale on [projekti töökorralduses](../../docs/projekti-tookorraldus.md#kui-tekib-merge-konflikt).

## Tulevikumärkused

Slaidide õpetaja märkustes on rida „Tulevikus” ja „Samaks jääb”. Need tuginevad artiklile, mida [lühijutt](ai-native-sdlc-talk.md) tutvustab; iga märkuse jaoks on aega 20–30 sekundit ja ajapuuduse korral võib osa vahele jätta. Tööviisi, testimise ega kasutuselevõtu põhisõnumit need ei asenda. Seminari lõpu tuleviku küsimusele piisab ühest-kahest vastusest. Artikkel ei käsitle Waterfalli, agiilset arendust, litsentse, tehnilist võlga ega süsteemi lõpetamist.

## Kodutöö selgitamisel

Rõhuta, et meeskond võib tööviisi hiljem muuta. Muutmine ei ole viga, kui põhjus ja mõju dokumenteeritakse.
Kontrolli, et Waterfalli ja agiilset lähenemist võrreldaks projekti olukorra järgi ning et kasutajalood lähtuksid valideeritud probleemist.

