# Seminar 4 (2027/2028): töökava

## Põhiidee

Seminar 3 vastas küsimusele „mida süsteem teeb?”. Seminar 4 küsib:

> Kuidas me teame, et kavand on piisavalt hea, ja mis võib meid alt vedada?

Kvaliteet on ebamäärase nõude muutmine mõõdetavaks ja testitavaks. Risk on kontrollimata eeldus, millel on mõju ja vastutaja.

Seminar algab tiimide endi tööst. 2026. aastal leidis iga tiim „Selgita oma otsust” harjutuses sama kontrollimata eelduse: andmeallikas ja see, et tellijaga pole räägitud. Sellest eeldusest algab riskikaart.

## Reegel, mis hoiab ajakava

Iga teema kohta on kuni 10 minutit selgitust ja seejärel harjutus. Kui harjutuse slaidini pole õigel ajal jõutud, jäetakse rääkimata ülejäänud teooria, mitte harjutus. Teooria on konspektis ja õppija loeb selle enne seminari.

## Enne seminari

Õppija loeb konspektist:

- [Mõõdetav kvaliteet](../../../handbook/04-quality-and-risk/01-measurable-quality.md)
- [Riskid](../../../handbook/04-quality-and-risk/04-risks.md)

Õpetaja saadab kodutöö 3 kirjaliku tagasiside enne seminari.

## Tulemus: release `v0.3.0`

Seminar ja kodutöö 4 lõpevad tiimi repos release'iga `v0.3.0 – Kvaliteedi- ja riskiplaan`:

- kvaliteedinõuded: 3–4 omadust tiimi lugudest, igaüks mõõdetava kontrolltingimusena koos piiri allikaga;
- testjuhtumid: tiimi ühine seminarist ja iga õppija üks oma loo kohta, üks katab vea olukorda;
- riskikaart: andmeallika risk, seminaris leitud eeldus ja vähemalt 5 muud riski; eeldused eraldi; vastutaja on roll;
- otsus `004`: kompromiss ja vähemalt üks varasem otsus, mis kinnitati või muudeti;
- backlog tootest, hinnang ja tegelik aeg igal Issue'l, blokeerija märgitud;
- iga õppija Issue, PR, sisuline ülevaatus, iseseisev silumisharjutus ja refleksioon.

## Ajakava, 2 × 90 minutit

### I osa

| Samm | Tegevus | Min |
|---|---|---:|
| 1 | Kodutöö 3 tagasiside: kolm punkti, küsimused. Tahvel ja ajaväljad korda. | 10 |
| 2 | „Selgita oma otsust”: 10 min ettevalmistust, iga tiim 4 min. Suurim kontrollimata eeldus kirja. | 30 |
| 3 | Kvaliteedinõue: 10 min selgitus, 20 min harjutus. Tiim kirjutab oma lugudest 3 kontrolltingimust koos piiri allikaga. | 30 |
| 4 | Testjuhtum: 5 min selgitus, 15 min harjutus. Tiim kirjutab ühe testjuhtumi oma põhiloo kohta ja proovib selle kavandi peal läbi. | 20 |

### II osa

| Samm | Tegevus | Min |
|---|---|---:|
| 5 | Riskikaart: 10 min selgitus, 25 min harjutus. Alustatakse sammus 2 leitud eeldusest, lisatakse andmeallikas ja üks kolmas osapool. | 35 |
| 6 | WIP-piirang ja blokeerija: demo sildiga `blocked`, seos „blocked by”, `blocker` teisest otsast. Andmeallika Issue märgitakse kohe. | 10 |
| 7 | Git: `git log --oneline`, `git diff`, `git restore` demo; igaüks käivitab `git log` tiimi repos. | 15 |
| 8 | Rollivahetus, kodutöö 4, mõisted eksami testiks, tuleviku küsimus. | 15 |
| 9 | Puhver tehnilistele tõrgetele ja küsimustele. | 15 |

Kokku 180 minutit.

## Mis jääb seminarist välja

Need teemad on konspektis või ühel slaidil ja neid ei räägita eraldi:

- kvaliteedi vaatenurgad ja kompromissid: slaidil „Kontrollküsimused iga kavandi juures”, pikemalt konspektis;
- turvalisus, privaatsus, ligipääsetavus: kontrollküsimused samal slaidil;
- arendamise etapp, viga, silumine, koodi ülevaatus: üks slaid, harjutus kodutöös iseseisvalt konspekti lehe järgi;
- Cloudflare'i juhtum: üks slaid kolmandate osapoolte juures, 3 minutit;
- AI ja projektijuhtimise kogemuslood: ainult kui puhver jääb kasutamata.

## Harjutuste väljund

Iga harjutuse tulemus commit'itakse seminari lõpuks tiimi reposse, ka pooleli kujul:

| Harjutus | Fail tiimi repos |
|---|---|
| Kontrolltingimused | `requirements/quality.md` või otsuse `004` osa |
| Testjuhtum | `tests/test-cases.md` |
| Riskikaart | `risks/risk-map.md` malli järgi |

Kodutöö jätkab neid faile, mitte ei alusta uusi.

## Mõisted eksami testiks

| Mõiste | Kus |
|---|---|
| kvaliteediomadus ehk mittefunktsionaalne nõue, kvaliteedinõue, kontrolltingimus | seminar 4 |
| testjuhtum | seminar 4, kodutöö 4 |
| risk, eeldus, maandus | seminar 4 |
| WIP-piirang, blokeerija | seminar 4 |
| `git log`, `git diff`, `git restore` | seminar 4 |
| viga, silumine, koodi ülevaatus | kodutöö 4, iseseisev harjutus |

## Lahtised küsimused

- Testija roll: kas lisada neljanda rollina või jätta tiimile vabatahtlikuks? 2026. aastal jäi vabatahtlikuks.
- Harjutuste failinimed ühtlustatakse konspekti ingliskeelsete nimedega (`decisions/004-quality-and-risks.md`), kui mallid on uuendatud.
