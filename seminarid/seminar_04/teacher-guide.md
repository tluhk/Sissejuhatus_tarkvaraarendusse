# Õpetaja juhend: seminar 4

## Fookus

Seminar annab kvaliteedist ja vastutusest suure pildi. See ei asenda testimise, küberturbe, ligipääsetavuse ega õiguse erikursusi.

## I osa, 90 minutit

| Tegevus | Aeg |
|---|---:|
| `v0.2.0` ülevaade ja rollivahetus | 15 min |
| Kvaliteet eri vaatenurkadest | 20 min |
| Funktsionaalsed ja mittefunktsionaalsed vajadused | 15 min |
| Turvalisus, privaatsus, ligipääsetavus, töökindlus | 20 min |
| Cloudflare'i juhtum | 15 min |
| Puhver | 5 min |

## II osa, 90 minutit

| Tegevus | Aeg |
|---|---:|
| Kvaliteedikriteeriumide valik | 15 min |
| Riskide ja vastutuse kaardistus | 15 min |
| Testjuhtum ja vea silumise lühiharjutus | 15 min |
| Kontrollimise põhimõte | 15 min |
| Litsentsid ja kolmandad osapooled | 10 min |
| Otsuse ning PR-i ülevaatus | 10 min |
| Kodutöö ja release | 10 min |

## Arutelu võti

Cloudflare'i juhtumit ei kasutata regex'i õpetamiseks. Eesmärk on näha, et rike tekib koodi, testide, levitusviisi, seire ja otsustusprotsessi koosmõjus.

Silumise näites palu õppijatel esmalt ennustada funktsiooni tulemus sisendiga `[2, 4, 6]`. Oodatud keskmine on `4`, kood tagastab `6`; vea põhjus on nimetaja `values.length - 1`. Arutage, milline test paljastab vea ja miks tuleb pärast parandust sama test uuesti käivitada.

## Ohukohad

- „Kiire, turvaline ja mugav” jääb mõõtmata loosungiks.
- Riskitabel paisub AI abil, kuid projekti olulised riskid kaovad müra sisse.
- Vastutajaks märgitakse „meeskond”. Palu nimetada roll ja esimene tegevus.
- Kontroll tähendab ainult lõpus testimist. Too sisse ennetus, varajane kontroll ja seire.

