# Kodutöö 3: süsteemi kontseptsioon, tööviis ja release `v0.2.0`

## Eesmärk

Seminaris 2 leidsite ja kontrollisite tunniplaani kasutaja probleemi. Nüüd otsustate, milline süsteem probleemi lahendab ja kuidas tiim tööd teeb.

## Ülesanne

**Alustage seminari materjali läbilugemisega** (`seminarid/seminar_03/seminar.md`). Seejärel lugege tabel läbi. Kõik tiimiliikmed osalevad igas sammus. Igal sammul on üks vastutaja, kes võtab tulemuse kokku. Rollide jagamine on esimene samm.

| # | Samm | Vastutab | Tulemus | Kus |
|---|---|---|---|---|
| 1 | Jagage rollid | projektijuht | Projektijuht, release manager, disainer ja arhitekt koos nimedega. Release manager on keegi, kes ei teinud `v0.1.0` release'i. Kui tiimis on üle nelja liikme, lisandub tooteomanik. | `README.md`, osa „Rollid” |
| 2 | Kirjeldage kasutaja teekonda | projektijuht | Sammud eesmärgini ja kohad, kus kasutaja takerdub | `decisions/003-susteemi-kontseptsioon.md`, osa „Kasutaja teekond” |
| 3 | Kirjutage kasutajalood | disainer, tooteomaniku olemasolul tooteomanik | Igaühelt vähemalt üks lugu tõendi, kontrolltingimuse, autori ja ülevaatajaga. Lood lisatakse faili sammu 4 merge-konflikti harjutuse järgi. | `decisions/003-susteemi-kontseptsioon.md`, osa „Kasutajalood” |
| 4 | Lahendage merge-konflikt harjutuse järgi: [`seminarid/seminar_03/merge-conflict-exercise.md`](merge-conflict-exercise.md) | disainer | Iga tiimiliige on lahendanud ühe konflikti ja kirjeldanud seda PR-i kommentaaris | PR-i kommentaar |
| 5a | Kontseptsioon: disain | disainer | Eesmärk, osalised, piir, kaks lahendussuunda ja valik | `decisions/003-susteemi-kontseptsioon.md`, osa „Disain” |
| 5b | Kontseptsioon: arhitektuur | arhitekt | Osad, nende vastutus ja sõltuvused; info liikumine on valikuline | `decisions/003-susteemi-kontseptsioon.md`, osa „Arhitektuur” |
| 6 | Valige tööviis ja planeerige töö | projektijuht | Kolm võrreldud tööviisi ja valik; backlog'i Issue'del on vastutaja ja ajahinnang | `decisions/002-tooviisi-valik.md`, Projectsi tahvel |
| 7 | Avaldage release `v0.2.0` | release manager | Release notes koos planeerimise võrdlusega, tag ja Release | `releases/v0.2.0.md` |
| 8 | Kirjutage refleksioon | iga õppija ise | Igaühe refleksioon | oma `SJTA` repos `reflections/oppija-nimi-v0.2.0.md` |

Vastutaja ei tee kogu tööd üksi. Ta koondab teiste panuse ja hoolitseb, et samm saaks tehtud.

**Tooteomanik** hoiab silma peal, et toode vastaks kasutaja vajadustele ja looks talle väärtust.

**Kasutajalood** muudavad probleemi konkreetseteks vajadusteks, mille täitmist saab kontrollida. Selles kodutöös tuleneb neist süsteemi kontseptsioon ja backlog'i Issue'd.

Iga muudatus käib tiimi repos sama töövoo järgi: Issue → haru → commit → push → pull request → ülevaatus → merge. Kasutaja teekond (samm 2) peab olema `main`-is enne, kui loote harud kasutajalugude jaoks.

Abimaterjal iga sammu kohta on seminari materjali lõpus, osas „Kodutöö 3 abimaterjal” (`seminarid/seminar_03/seminar.md`).

## AI kasutamine

Kursuse jooksul tuleb AI-d kasutada vähemalt ühe olulise otsuse juures, näiteks lahendussuundade või tööviiside võrdlemisel. Kui kasutate AI-d selles etapis, täitke selle otsuse failis osa „AI kasutamine”. AI vastus ei ole kasutajaloo tõend.

## Esitamine

Iga õppija lisab õppejõu antud kodutöö Issue'sse kommentaari, kus on lingid:

- release'ile `v0.2.0`;
- oma refleksioonile `SJTA` repos;
- oma PR-ile ja tehtud ülevaatusele;
- PR-i kommentaarile, kus kirjeldasid lahendatud merge-konflikti.

Maht ja hindamine: [kodutöö 3 hindamine](homework-grading.md) (`seminarid/seminar_03/homework-grading.md`).
