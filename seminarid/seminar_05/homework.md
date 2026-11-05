# Kodutöö 5: kasutuselevõtu ja arengu plaan ning release `v0.4.0`

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](../../docs/projekti-tookorraldus.md).

## Ülesanne lühidalt

Kirjeldage, kuidas süsteem kasutusele jõuaks, kuidas selle toimimist ja mõju jälgitaks, kes vastutaks hoolduse eest ning millal tuleks lahendust muuta või lõpetada. Koostage release'ide ajajoone mustand ja avaldage `v0.4.0 – Kasutuselevõtu ja arengu plaan`.

## Maht

Arvestuslik maht on ligikaudu 8 tundi õppija kohta.

## Tulemus

Vähemalt:

```text
decisions/005-kasutuselevott-ja-areng.md
releases/ajajoon.md
releases/v0.4.0.md
reflections/oppija-nimi-v0.4.0.md
```

## Tööjaotus

1. Senise kvaliteedi- ja riskiplaani ülevaatus ning backlog'i uuendamine – 1 h.
2. Kasutuselevõtu, toe ja tagasipööramise plaan – 1,5 h.
3. Seire, tagasiside ning mõju hindamine – 1,5 h.
4. Hooldus, muutmine ja lõpetamine – 1 h.
5. Release'ide ajajoon ning oluliste otsuste valik – 1 h.
6. PR, ülevaatus ja parandused – 1 h.
7. Refleksioon ning release – 1 h.

## Minimaalsed nõuded

- kasutuselevõtu sihtrühm, viis, tugi ja vastutaja;
- vähemalt üks peatamise või tagasipööramise tingimus;
- 3–5 põhjendatud märki süsteemi seisundi, kasutaja tulemuse ja mõju kohta;
- tagasiside kogumise ning otsustesse jõudmise viis;
- hoolduse omanik, olulised sõltuvused ja tehnilise võla käsitlus;
- vähemalt üks olukord, kus süsteem tuleks oluliselt ümber mõelda või lõpetada;
- ajajoon, mis ühendab olulised otsused release'idega;
- `releases/v0.4.0.md` faili osas „Planeerimine” ajahinnangu ja tegeliku ajakulu võrdlus ning üks parandus järgmiseks etapiks.

## AI kasutamise nõue

Kui meeskond ei ole seni AI-d ühe olulise otsuse juures kasutanud, tuleb seda teha nüüd. Dokumenteerige sisend, väljundi kasutamine või tagasilükkamine, kontroll, kasu ja tekkinud müra.

Demo on vabatahtlik. Kui teete demo, piirake selleks kuluv meeskonna aeg enne alustamist ja kirjeldage, millist oletust see kontrollis. Demo visuaalne mulje ei anna hindamisel lisapunkte.

## GitHubi töövoog

Iga õppija teeb sisulise panuse enda haru ja PR-i kaudu, vaatab üle teise õppija töö ning lisab refleksiooni. Ajajoon peab sündima meeskonna valikutest, mitte ühe inimese tagantjärele kirjutatud loost.

## Release manager

Uus release manager loob tag'i `v0.4.0` ja avaldab release'i pealkirjaga `Kasutuselevõtu ja arengu plaan`.

## Valmis töö kontroll

- [ ] Plaan käsitleb kasutuselevõttu, tuge, seiret, hooldust ja lõpetamist.
- [ ] Mõõdikud aitavad otsustada, mitte ainult tegevust kokku lugeda.
- [ ] Ajajoon näitab arusaamise ja otsuste muutumist.
- [ ] Vähemalt ühe olulise otsuse juures on AI kasutus läbipaistvalt hinnatud.
- [ ] Hinnangu ja tegeliku ajakulu võrdlus on release notes'is.
- [ ] Igal õppijal on Issue, commit, PR, ülevaatus ja refleksioon.
- [ ] Release `v0.4.0` on avaldatud.

## Esitamine

Lisage kodutöö Issue kommentaari release'i, ajajoone, enda refleksiooni, enda PR-i ja tehtud ülevaatuse lingid. Eraldi esitamise PR-i pole vaja; PR-id teete töö käigus tiimi repos.

## Hindamiskriteeriumid

Hindan tiimi ühist tulemust repositooriumis ning iga õppija panust tema Issue'i, PR-i, ülevaatuse ja refleksiooni põhjal. Kokku on võimalik saada 100 punkti.

| Kriteerium | Punktid | Mida repositooriumist vaatan |
|---|---:|---|
| Kasutuselevõtt ja tugi | 15 | Kirjas on sihtrühm, viis, tugi ja vastutaja ning vähemalt üks peatamise või tagasipööramise tingimus. |
| Seire, tagasiside ja mõju | 20 | 3–5 põhjendatud märki kirjeldavad süsteemi seisundit, kasutaja tulemust ja mõju ning aitavad otsustada. Tagasiside kogumise ja otsustesse jõudmise viis on selge. |
| Hooldus, muutmine ja lõpetamine | 15 | Kirjas on hoolduse omanik, olulised sõltuvused ja tehnilise võla käsitlus ning vähemalt üks olukord, kus süsteem tuleks ümber mõelda või lõpetada. |
| Release'ide ajajoon | 10 | Ajajoon seob olulised otsused release'idega ja näitab arusaamise muutumist. |
| Töö planeerimine | 10 | Backlog on uuendatud. Release notes võrdleb ajahinnangut tegeliku ajakuluga ja nimetab järgmise etapi paranduse. |
| Tiimitöö ja iga õppija panus | 10 | Iga õppija panus on jälgitav Issue'i, commit'i ja PR-i kaudu ning igaüks on üle vaadanud teise õppija töö. Ajajoon on sündinud meeskonna valikutest. |
| Refleksioon ja AI kasutamise läbipaistvus | 10 | Iga õppija refleksioon kirjeldab tema panust ja õpitut. Vähemalt ühe olulise otsuse juures on AI sisend, väljundi kasutamine või tagasilükkamine, kontroll, kasu ja tekkinud müra kirjas. |
| Repositooriumi korrastatus ja release | 10 | Nõutud failid on leitavad, muudatused on jõudnud `main`-i PR-ide kaudu ning `v0.4.0` release on avaldatud. |

**Tulemuse tõlgendamine:** 90–100 punkti tähendab põhjendatud ja jälgitavat tööd; 75–89 punkti puhul on tulemus olemas, kuid mõni osa vajab täiendamist; 60–74 punkti puhul takistab oluline lünk järgmises seminaris jätkamist; alla 60 punkti korral ei ole kasutuselevõttu ja arengut piisavalt põhjendatud või panust ja otsuseid ei saa repo põhjal hinnata.

Kasutuselevõtu ning seire, tagasiside ja mõju eest peab saama kokku vähemalt poole nende kahe kriteeriumi punktidest. Korras ajajoon või release ei korva põhjendamata plaani. Demo eest lisapunkte ei anta. Töötava rakenduse, prototüübi ega dokumentide hulga eest eraldi punkte ei anta. AI puhul hinnatakse kasutamise eesmärki ja väljundi kontrollimist, mitte genereeritud teksti mahtu.
