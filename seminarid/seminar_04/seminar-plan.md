# Seminar 4: töökava

Töödokument seminari 4 ülesehitamiseks. Täiendame seda samm-sammult. Kui kava on kinnitatud, saavad sellest seminari slaidid, peatükid, kodutöö ja õpetaja juhis. Seejärel see fail kustutatakse.

## Põhiidee

Seminar 3 vastas küsimusele „mida süsteem teeb?”. Seminar 4 küsib:

> Kuidas me teame, et kavand on piisavalt hea, ja mis võib meid alt vedada?

Alustame tiimide endi tööst, mitte uuest teooriast. Kodutöö 3 näitas kahte lõhet:

1. Kontrolltingimustes on mõõtmata sõnad, näiteks „kiiresti” või „ilma liigse ajakuluta”. Seminaris 3 arutati sama viga „moodsa” näitel.
2. Viis tiimi kuuest ei kontrollinud, kas ja kuidas tunniplaani andmed kätte saab.

Seega on kvaliteet ebamäärase nõude muutmine mõõdetavaks ja testitavaks. Risk on kontrollimata eeldus, millel on mõju ja vastutaja.

**Kitsendus võrreldes praeguse `seminar.md`-ga:** 3–4 kvaliteediomadust tiimi enda lugudest. Turvalisus, privaatsus ja ligipääsetavus on kontrollküsimused, mitte eraldi teemad. Cloudflare'i juhtum ja litsentside eraldi osa jäävad välja või lühenevad üheks slaidiks.

## Eesmärk

Tiim muudab oma kavandi kontrollitavaks: mõõdetavad kvaliteedinõuded, testjuhtum ja põhjendatud riskid. Töö käib päris Kanbani ja ülevaatuste reeglitega.

## Tulemus: release `v0.3.0`

Seminar ja kodutöö 4 lõpevad tiimi repos release'iga `v0.3.0`. Selles on:

- **Kvaliteedinõuded:** 3–4 tiimi enda lugudest tulnud kvaliteediomadust, igaüks mõõdetava kontrolltingimusena. Mõõtmata sõnu nagu „kiiresti” ei ole.
- **Testjuhtumid:** üks tiimi ühine testjuhtum seminarist ja iga õppija üks testjuhtum oma kasutajaloo kohta.
- **Riskikaart:** kohustuslik andmeallika risk ja vähemalt 5 muud riski, väiksemal tiimil vähem. Igal riskil on mõju, tõenäosus, kuidas märkame, maandus ja vastutav roll. Eeldused on riskidest eraldi välja toodud.
- **Backlog:** 2–3 tootest tulnud Issue'd ja kolm „Selgita oma otsust” lünka Issue'na. Igal Issue'l on hinnang (h) ja suletutel tegelik aeg (h).
- **Ülevaadatud PR-id:** iga PR-i ühendas keegi teine kui autor ja ülevaataja küsimusele on vastatud.
- **Iseseisev harjutus:** iga õppija vea kirjeldus ja ülevaatuse kommentaar oma Issue's.
- **Release'i kirjeldus:** release manageri kontrollnimekiri on läbitud ja hinnangu ning tegeliku aja võrdlus on kirjas. README viitab uutele otsustele.

## Seminari sammud

1. Projectsi tahvli ja `v0.2.0` läbivaatus, aja jälgimine kõigile tiimidele, rollivahetus (20 min, arvutid lahti).
2. „Selgita oma otsust” (25 min, arvutid kinni, üks kaardiarvuti tiimi kohta).
3. Ebamäärasest kontrolltingimusest mõõdetavaks kvaliteedinõudeks.
4. Testjuhtum ühest oma kasutajaloost.
5. Arendamise etapp: vea silumine ja koodi ülevaatus. Seminaris on lühike sissejuhatus, harjutus tehakse kodutöös iseseisvalt.
6. Riskid: andmeallika fakt, riskikaart, risk vs eeldus.
7. Backlog tootest: 2–3 Issue'd riskidest, ajahinnang kohe, blokeerijate märkimine.
8. Git: `git log`, `git diff`, `git restore`.
9. Kodutöö 4 ja release `v0.3.0`: merge-reegel, release manageri kontrollnimekiri, ajakulu logimine.

## Sammude selgitused

Iga sammu selgitus on eraldi failis kaustas `sammud/`:

1. [Projectsi tahvli ja `v0.2.0` läbivaatus, rollivahetus](sammud/samm-01-tahvel-ja-rollivahetus.md)
2. [„Selgita oma otsust”](sammud/samm-02-selgita-oma-otsust.md)
3. [Ebamäärasest mõõdetavaks](sammud/samm-03-moodetav-kvaliteet.md)
4. [Testjuhtum oma kasutajaloost](sammud/samm-04-testjuhtum.md)
5. [Vea silumine ja koodi ülevaatus](sammud/samm-05-silumine-ja-ulevaatus.md)
6. [Riskid](sammud/samm-06-riskid.md)
7. [Backlog tootest](sammud/samm-07-backlog.md)
8. [Git](sammud/samm-08-git.md)
9. [Kodutöö 4 ja release `v0.3.0`](sammud/samm-09-kodutoo-ja-release.md)

## Mõisted eksami testiks

Eksamil on lisaks esitlusele lühike test mõistete kohta. Mõiste peab olema seminaris või kodutöös tegelikult läbitud. Veerg „Kus” näitab, kus mõiste esimest korda põhjalikult käsitletakse.

| Mõiste | Kus |
|---|---|
| tarkvara, tarkvaraarendus, elutsükkel | seminar 1 |
| IDE, koodiredaktor, terminal, käsukest | seminar 1 |
| Git vs GitHub, repositoorium, kohalik ja kaug-repo | seminar 1 |
| commit, push, pull, branch, pull request, merge | seminarid 1–2 |
| Markdown | seminar 1 |
| MVP, iteratiivne ja inkrementaalne arendus | seminarid 1 ja 3 |
| Waterfall, agiilne arendus, Scrum, Kanban | seminarid 1–3 |
| Issue, backlog, ajahinnang | seminar 2 |
| probleem vs lahendus, tõend | seminar 2 |
| litsents | seminar 2 |
| tag, release, versioon | seminar 2 |
| rollid: projektijuht, tooteomanik, disainer, arhitekt, release manager | seminarid 2–3 |
| kasutaja teekond, kasutajalugu, kontrolltingimus | seminar 3 |
| süsteemi kontseptsioon, süsteemi piir | seminar 3 |
| merge-konflikt | seminar 3, kodutöö 3 |
| persona | seminar 3, ainult suuline selgitus; testi lisamine on lahtine |
| kvaliteediomadus ehk mittefunktsionaalne nõue | seminar 4 |
| testjuhtum | seminar 4, kodutöö 4 |
| risk, eeldus, maandus | seminar 4 |
| WIP-piirang, blokeerija | seminar 4 |
| `git log`, `git diff`, `git restore` | seminar 4 |
| viga, silumine, koodi ülevaatus | kodutöö 4, iseseisev harjutus |
| kasutuselevõtt, seire, hooldus, tagasiside | seminar 5 |

## Lahtised küsimused

- **Andmeallika fakt.** Kas tunniplaani andmed on kättesaadavad, näiteks kalendriekspordi või ÕIS-i kaudu? Kui fakti pole, saab ülesanne olla: „tiim kontrollib selle ise”.
- **Kontaktaeg.** Kas seminar on kaks 90-minutilist osa?
- **Persona.** Kas persona kuulub testi, kuigi seda selgitati ainult suuliselt?
