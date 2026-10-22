# Kuidas kursus seminarist seminarini kulgeb

Kursusel ei alustata igas seminaris uut projekti. Esimeses seminaris valmistud tööks, seejärel tegutseb meeskond seminarides 2–5 ühe projekti kallal. Iga kodutöö viib sama projekti järgmisse etappi. Nii saab jälgida, kuidas probleemi mõistmine ja meeskonna otsused aja jooksul muutuvad.

## Kursuse töötsükkel

Igas projektietapis toimub sama põhirütm:

1. Seminaris vaadatakse üle eelmise etapi tulemus ja selle kohta saadud tagasiside. Seminaris 2 vaadatakse selle asemel üle esimese kodutöö töövoog.
2. Meeskond õpib järgmise etapi teemasid ning alustab tööd ühise projekti kallal.
3. Seminaride vahel täiendatakse projekti dokumente, põhjendatakse otsuseid ja tehakse koostööd GitHubis.
4. Iga õppija esitab oma muudatused pull request'iga, vaatab kaaslase töö üle ja kirjutab individuaalse refleksiooni.
5. Meeskond koondab etapi tulemuse release'iks. Release fikseerib hetkeseisu; see ei tähenda, et kogu süsteem oleks valmis.

Meeskonnal on üks ühine repositoorium. Tööülesanded tehakse GitHub Issue'dena, muudatused eraldi harudes ning enne ühendamist vaadatakse need pull request'is üle. Release manageri roll vahetub. Oluliste otsuste logi aitab näidata, miks meeskond ühe valiku tegi ja kuidas uus info seda muutis.

## Seminarid ja kodutööd

| Etapp | Seminaris | Kodutöö tulemus |
|---|---|---|
| 1. Ettevalmistus | Tarkvaraarenduse suur pilt, elutsükkel, AI ning kursuse töövahendid. Harjutatakse Giti ja GitHubi põhivoogu. | **Individuaalne kodutöö:** õppija kirjeldab arenduskeskkonda, kinnistab GitHubi töövoogu ja reflekteerib õpitut. Meeskonnaprojekti veel ei ole. |
| 2. Kliendisoovist arendusülesandeni | Meenutatakse elutsüklit ning Waterfalli ja agiilset tööviisi, tutvutakse rollidega ning uuritakse kliendisoovi „Haapsalu Kolledž soovib tunniplaani veebilehte kaasaegsemaks muuta”. Harjutatakse probleemi kontrollimist, Kanbani ja tööde ajahindamist. | Iga õppija uurib tunniplaani kasutamise võimalikke probleeme. Meeskond täpsustab ühe probleemi tõendite põhjal, koostab arendustiimile lähteülesande ning avaldab `v0.1.0 – Probleem sõnastatud`. |
| 3. Tööviis ja kontseptsioon | Vaadatakse projekti eri rollide kaudu. Võrreldakse Waterfalli, iteratiivset ja agiilset lähenemist ning seostatakse kasutajavajadused kasutajalugude ja funktsionaalsete nõuetega. Kavandatakse süsteemi osad, piirid ja seosed kõrgtasemel. | Meeskond põhjendab tööviisi ja süsteemi kontseptsiooni ning lisab vähemalt kaks tõenditel põhinevat kasutajalugu koos kontrolltingimustega. Avaldatakse `v0.2.0`. |
| 4. Kvaliteet ja riskid | Arutatakse kvaliteeti ja riske ning tehakse lühike koodi testimise ja vea põhjuse leidmise harjutus. | Meeskond kirjeldab kontrollitavaid kvaliteediomadusi, lisab vähemalt ühe testjuhtumi ning analüüsib riske, maandamist ja vastutajaid. Avaldatakse `v0.3.0`. |
| 5. Kasutuselevõtt ja areng | Vaadatakse, mis saab süsteemist pärast kavandamist: kasutuselevõtt, tugi, seire, hooldus ja lõpetamine. | Meeskond koostab kasutuselevõtu ja arengu plaani ning release'ide ajajoone. Avaldatakse `v0.4.0`. |
| Eksam | Esitletakse meeskonna arendusprotsessi ja põhjendatakse olulisi valikuid. | Koostatakse terviklik ajajoon ning lõplik protsessirelease `v1.0.0`. Iga õppija selgitab vähemalt üht olulist otsust või release'i. |

## Mida tähendab „sama projekti edasiarendamine“?

Meeskond ei pea kursuse jooksul valmis programmeerima töötavat rakendust. Projekt areneb dokumenteeritud otsuste ja kavandite kaudu:

**probleem ja tõendid → kasutajalood ning nõuded → süsteemi kontseptsioon ja kõrgtaseme arhitektuur → kvaliteet, testimine ja riskid → kasutuselevõtt ning areng.**

Varasem töö jääb alles. Hilisemas etapis võib meeskond varasemat otsust kinnitada, täpsustada või muuta, kui uus tõend seda põhjendab. Muudatus dokumenteeritakse, et oleks näha, kuidas meeskonna arusaam kujunes.

Seminaride 2–5 kodutööde arvestuslik maht on ligikaudu 8 tundi õppija kohta. Iga õppija panustab ühisesse projekti, kuid tema enda töö, ülevaatus ja refleksioon peavad olema nähtavad. Hindamisel loeb põhjendatud arusaamine, mitte dokumentide hulk ega projekti tehniline keerukus.

## Seos teiste juhenditega

- [Aktiivne kursuseprogramm](kursuseprogramm.md) kirjeldab seminaride sisu ja põhitulemusi.
- [Seminaride ja projektietappide üksikasjalik kava](kursuse-umberkujunduse-kava.md) kirjeldab kavandatud õppetegevusi ja ajakavasid.
- Iga seminari kodutöö juhendis on täpsed ülesanded, väljundid ja esitamise nõuded.
