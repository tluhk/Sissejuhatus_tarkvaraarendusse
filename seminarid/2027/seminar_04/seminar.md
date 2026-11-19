# Seminar 4: kvaliteet, riskid ja vastutus

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](../../../docs/projekti-tookorraldus.md). Slaidid: [slides.md](slides.md).

## Eesmärk

Seminari lõpuks õppija:

- eristab funktsiooni kvaliteediomadusest ja kirjutab ebamäärase nõude mõõdetava kontrolltingimusena koos piiri allikaga;
- koostab testjuhtumi ja proovib selle kavandi peal läbi;
- eristab riski ja eeldust ning täidab riskikaardi rea, millel on vastutav roll;
- märgib tahvlil blokeeritud töö mõlemast otsast;
- kasutab `git log`, `git diff` ja `git restore` käske oma töö kontrolliks.

## Põhiküsimus

> Kuidas me teame, et kavand on piisavalt hea, ja mis võib meid alt vedada?

## Enne seminari

Loe konspektist [Mõõdetav kvaliteet](../../../handbook/04-quality-and-risk/01-measurable-quality.md) ja [Riskid](../../../handbook/04-quality-and-risk/04-risks.md). Seminaris on teooriat iga teema kohta kuni 10 minutit, ülejäänud aeg on harjutused tiimi oma kavandi peal.

Vaata üle õpetaja kirjalik tagasiside kodutööle 3.

## Seminari käik

Iga harjutuse tulemus commit'itakse tiimi reposse seminari lõpuks, ka pooleli kujul. Kodutöö jätkab neid faile.

| Samm | Tegevus | Harjutuse juhend | Fail tiimi repos |
|---|---|---|---|
| 1 | Kodutöö 3 tagasiside, tahvli ajaväljad korda | | |
| 2 | „Selgita oma otsust”: kolm küsimust tiimi kohta, suurim kontrollimata eeldus Issue'na | [01](sammud/01-selgita-oma-otsust.md) | Issue |
| 3 | Kvaliteedinõue: 3 mõõdetavat kontrolltingimust | [02](sammud/02-kontrolltingimus.md) | `requirements/quality.md` |
| 4 | Testjuhtum põhiloo kohta kavandi peal | [03](sammud/03-testjuhtum.md) | `tests/test-cases.md` |
| 5 | Riskikaardi algus: eeldus, andmeallikas, kolmas osapool | [04](sammud/04-riskikaart.md) | `risks/risk-map.md` |
| 6 | WIP-piirang ja blokeerija: eelduse Issue märgitakse | | Issue silt |
| 7 | Git: `log`, `diff`, `restore`; igaüks vaatab tiimi repo logi | [konspekt](../../../handbook/04-quality-and-risk/06-git-history.md) | |
| 8 | Rollivahetus, kodutöö 4 | | README |

Arendamise etapp, viga, silumine ja koodi ülevaatus on ühel slaidil; harjutus on kodutöös iseseisvalt konspekti lehe [Silumine ja koodi ülevaatus](../../../handbook/04-quality-and-risk/03-debugging-and-code-review.md) järgi.

## Kontrollpunkt

Seminari lõpuks on tiimi repos:

- Issue seminaris leitud eelduse kontrollimiseks, hinnanguga;
- `requirements/quality.md` vähemalt ühe mõõdetava reaga, millel on piiri allikas või eelduse märge;
- `tests/test-cases.md` ühe testjuhtumiga, mis on kavandi peal läbi proovitud;
- `risks/risk-map.md` vähemalt kolme reaga, igal vastutajaks roll.

Pooleli fail on parem kui tühi: kodutöö jätkab sealt, kus seminar pooleli jäi.

## Kodutöö ja release

Kodutöö 4 viib seminari failid lõpuni ja lõpeb release'iga `v0.3.0 – Kvaliteedi- ja riskiplaan`. Juhend: [homework.md](homework.md).
