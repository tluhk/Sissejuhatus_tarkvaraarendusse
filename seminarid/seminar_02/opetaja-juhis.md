# Seminari 2 läbiviimine

Kasuta tunnis [slaide](slides.md). Ava lingitud peatükk siis, kui vajate näidet, töölehte või täpseid samme; kogu peatükki pole vaja slaidi järel uuesti ette lugeda. Iseseisvalt õppija saab sama järjekorda järgida koos peatükkidega.

## Enne tundi

Valmista organisatsioonis `TLUHK-RIF26` ette tiimirepod koos `main`-i ja esialgse README-ga. Anna liikmetele ligipääs ning seadista võimaluse korral peaharu kaitse PR-i ja kaaslase heakskiidu nõudega. Kontrolli, et tiim saaks GitHub Projectsi tahvlit muuta. Varu näidisrepo release'i loomise näitamiseks.

Loe läbi [tööleht](peatukid/05-probleemikandidaadid.md), [tiimi töövoog](peatukid/06-tiimi-toovoog.md) ning [kodutöö ja release'i juhend](peatukid/07-kodutoo-ja-release.md). Eraldi ettevalmistavat kodutööd ei ole. GitHubi ja VS Code'i kõrval kasutatakse juba tuttavat terminalitöövoogu.

## Esimene osa, 90 minutit

| Aeg | Tegevus |
|---:|---|
| 8 min | Kursuse koht, kliendisoov, elutsükli ja tööviiside meenutus |
| 12 min | Rollide vastutus ja koostöö tunniplaani näitel |
| 15 min | Soovi, probleemi ja lahendusidee eristamine |
| 18 min | Tõendid, kasutajauuring, AI ning litsentsid |
| 8 min | Discovery-näide ja suunda muutva tõendi arutelu |
| 14 min | Individuaalsed kandidaadid ja enesehindamine |
| 5 min | Töölehe ülevaatus ning üleminek tiimitööle |
| 10 min | Aja- ja tehniline puhver |

Esimese osa väljund on iga õppija iseseisvad märkmed. Hoia valmis lahendusideed uurimist vajavate oletustena.

## Teine osa, 90 minutit

| Aeg | Tegevus |
|---:|---|
| 15 min | Tiimid, vastutused, repo ligipääs ja kloonimine |
| 10 min | Iga õppija enda Issue ja ülevaataja kokkuleppimine |
| 10 min | Projects, Kanban ja ajahinnang |
| 25 min | Haru ning tööfail; kandidaatide täpsustamine |
| 15 min | Commit, push, PR ja kaaslase ülevaatus |
| 10 min | Kodutöö järjekord ja release'i loomise näidis |
| 5 min | Tehniline puhver ja igaühe järgmine samm |

Kasuta Giti sammude näitamisel slaidide ja töövoopeatüki sama näidet. Õppija asendab selle enda andmetega. Kui töö jääb pooleli, las ta märgib Issue kommentaari, kuhu jõudis ja milline on takistus. Seminari lõpu kontrollpunkt on viimasel slaidil.

Tiimi ühine probleemivalik, valideerimine ja päris `v0.1.0` avaldamine jäävad kodutöösse. Järgmine seminar saab alata selle versiooni tõenditest ja lahtistest küsimustest.

## Esitluse genereerimine

Käivita repo juurkaustas:

```bash
seminarid/export-marp.sh seminarid/seminar_02-sujuv
```

Käsk loob `slides.md` põhjal sama kausta `slides.html`-i. Kohalikuks lugemiseks ava Markdown-peatükid VS Code'is või GitHubis; Markdown-lingid ei muutu ekspordis automaatselt HTML-lehtedeks.
