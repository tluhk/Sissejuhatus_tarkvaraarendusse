# Kodutöö 4: kvaliteedi- ja riskiplaan ning release `v0.3.0`

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](../../docs/projekti-tookorraldus.md).

## Ülesanne lühidalt

Koostage projekti põhjendatud kvaliteedi- ja riskiplaan. Siduge olulised kvaliteediomadused kontrollidega, määrake riskidele vastutus ning avaldage release `v0.3.0 – Kvaliteedi- ja riskiplaan`.

## Maht

Arvestuslik maht on ligikaudu 8 tundi õppija kohta.

## Tulemus

Tiimi repos on vähemalt:

```text
decisions/004-kvaliteet-ja-riskid.md
releases/v0.3.0.md
```

Iga õppija enda `SJTA` repos:

```text
reflections/oppija-nimi-v0.3.0.md
```

Riskitabel võib olla otsuse osa või eraldi fail, millele otsus viitab.

## Tööjaotus

1. Seniste otsuste ja rollivaate ülevaatus ning backlog'i uuendamine – 1 h.
2. Kvaliteediomaduste valik ja põhjendus – 1,5 h.
3. Kontrollitavate kriteeriumide koostamine – 1,5 h.
4. Riskide, mõju, maanduse ja vastutuse analüüs – 2 h.
5. PR, teise töö ülevaatus ja parandused – 1 h.
6. Refleksioon ning release – 1 h.

## Minimaalsed nõuded

- 4–6 projekti jaoks olulist kvaliteediomadust;
- iga omaduse juures põhjendus ja kontrollimise viis;
- vähemalt üks kasutajaloost või funktsionaalsest nõudest tuletatud lihtne testjuhtum (eeldused, sammud ja oodatud tulemus);
- vähemalt kuus eri tüüpi riski;
- iga olulise riski juures mõju, maandus, märkamine ja vastutaja;
- eraldi tähelepanu turvalisusele, privaatsusele ja ligipääsetavusele;
- vähemalt ühe kolmanda osapoole või litsentsi mõju;
- vähemalt üks varasema otsuse kinnitus, täpsustus või muutmine uue analüüsi põhjal;
- `releases/v0.3.0.md` faili osas „Planeerimine” ajahinnangu ja tegeliku ajakulu võrdlus ning üks parandus järgmiseks etapiks.

## AI kasutamine

AI võib aidata leida puuduvaid riskikategooriaid, kuid pikk üldine riskiloend ei ole väärtus. Meeskond peab eemaldama ebaolulise, kontrollima väited ja põhjendama, miks alles jäetud risk puudutab just nende projekti.

## GitHubi töövoog

Iga õppija töötab enda Issue ja haruga, avab PR-i, vaatab üle teise õppija sisulise panuse ning kirjutab refleksiooni. Ülevaataja küsib vähemalt ühe kontrolli, mõju või vastutuse kohta käiva küsimuse.

Kui seminaris jäi aega väheks, proovige terminalis väikese proovimuudatusega käske `git log --oneline`, `git diff` ja `git restore`. Selgitus on [töökorralduse juhendis](../../docs/projekti-tookorraldus.md#ajalugu-ja-muudatuse-tagasivõtmine).

## Release manager

Uus release manager kontrollib tervikut, loob tag'i `v0.3.0` ja avaldab release'i pealkirjaga `Kvaliteedi- ja riskiplaan`.

## Valmis töö kontroll

- [ ] Kvaliteedinõuded on kontrollitavad, mitte ainult omadussõnad.
- [ ] Vähemalt üks lihtne testjuhtum seob nõude eelduste, sammude ja oodatud tulemusega.
- [ ] Valikud lähtuvad projekti probleemist.
- [ ] Kompromissid on nähtavad.
- [ ] Riskidel on omanik ja reageerimisviis.
- [ ] AI-ga loodud üldsõnaline materjal on eemaldatud.
- [ ] Hinnangu ja tegeliku ajakulu võrdlus on release notes'is.
- [ ] Igal õppijal on Issue, commit, PR, ülevaatus ja refleksioon.
- [ ] Release `v0.3.0` on avaldatud.

## Esitamine

Lisage kodutöö Issue kommentaari release'i, enda `SJTA` repos oleva refleksiooni, enda PR-i ja tehtud ülevaatuse lingid. Eraldi esitamise PR-i pole vaja; PR-id teete töö käigus tiimi repos.

## Hindamiskriteeriumid

Hindan tiimi ühist tulemust repositooriumis ning iga õppija panust tema Issue'i, PR-i, ülevaatuse ja refleksiooni põhjal. Kokku on võimalik saada 100 punkti.

| Kriteerium | Punktid | Mida repositooriumist vaatan |
|---|---:|---|
| Kvaliteediomadused ja kontrollid | 25 | 4–6 projekti jaoks olulist omadust on põhjendatud ja kontrollitavad. Vähemalt üks testjuhtum seob kasutajaloo või nõude eelduste, sammude ja oodatud tulemusega. |
| Riskid ja vastutus | 25 | Kirjas on vähemalt kuus eri tüüpi riski. Olulistel riskidel on mõju, maandus, märkamine ja vastutaja. Käsitletud on turvalisust, privaatsust, ligipääsetavust ning vähemalt üht kolmanda osapoole või litsentsi mõju. |
| Seos varasemate otsustega ja kompromissid | 10 | Vähemalt üks varasem otsus on uue analüüsi põhjal kinnitatud, täpsustatud või muudetud. Kompromissid on nähtavad. |
| Töö planeerimine | 10 | Backlog on uuendatud. Release notes võrdleb ajahinnangut tegeliku ajakuluga ja nimetab järgmise etapi paranduse. |
| Tiimitöö ja iga õppija panus | 10 | Iga õppija panus on jälgitav Issue'i, commit'i ja PR-i kaudu. Commit'i sõnumid kirjeldavad tehtud muudatust. Ülevaataja on küsinud vähemalt ühe kontrolli, mõju või vastutuse kohta käiva küsimuse. |
| Refleksioon ja AI kasutamise läbipaistvus | 10 | Iga õppija refleksioon kirjeldab tema panust ja õpitut. Kui AI-d kasutati, on väited kontrollitud ja ebaoluline materjal eemaldatud. |
| Repositooriumi korrastatus ja release | 10 | Nõutud failid on leitavad, muudatused on jõudnud `main`-i PR-ide kaudu ning `v0.3.0` release on avaldatud. |

**Tulemuse tõlgendamine:** 90–100 punkti tähendab põhjendatud ja jälgitavat tööd; 75–89 punkti puhul on tulemus olemas, kuid mõni osa vajab täiendamist; 60–74 punkti puhul takistab oluline lünk järgmises seminaris jätkamist; alla 60 punkti korral ei ole kvaliteeti ja riske piisavalt analüüsitud või panust ja otsuseid ei saa repo põhjal hinnata.

Kvaliteediomaduste ja riskide eest peab saama kokku vähemalt poole nende kahe kriteeriumi punktidest. Pikk üldine riskiloend või korras release ei korva projektile kohandamata analüüsi. Töötava rakenduse, prototüübi ega dokumentide hulga eest eraldi punkte ei anta. AI puhul hinnatakse kasutamise eesmärki ja väljundi kontrollimist, mitte genereeritud teksti mahtu.
