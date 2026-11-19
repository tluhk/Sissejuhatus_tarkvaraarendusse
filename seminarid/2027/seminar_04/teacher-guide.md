# Õpetaja juhend: seminar 4 (2027/2028)

## Fookus

Seminar annab kvaliteedist ja vastutusest suure pildi ja jätab tiimile aega oma kavandit ise kontrollida. See ei asenda testimise, küberturbe, ligipääsetavuse ega õiguse erikursusi.

## Mis 2026. aastal juhtus ja mida sellest järeldada

Seminar läks loenguks. Esimeses osas kulus kodutöö tagasisidele umbes 30 minutit, „Selgita oma otsust” harjutusele 35 ja kvaliteedinõude teooriale 25. Teine osa oli ainult loeng ja Giti demo. Kvaliteedinõuete, testjuhtumi ja riskikaardi harjutused jäid tegemata ja läksid kodutöösse, mis kasvatas kodutöö mahtu.

Järeldus: tempot ei tõsteta, vaid teooria viiakse konspekti ja seminar jäetakse harjutustele. Iga teema saab kuni 10 minutit selgitust.

## Ajakava

Ajakava on [töökavas](seminar-plan.md). Pea kinni kolmest kellaajast: samm 3 harjutus algab hiljemalt 40. minutil, samm 5 harjutus hiljemalt II osa 10. minutil, samm 8 hiljemalt II osa 60. minutil. Kui jääd maha, jäta rääkimata teooria, mitte harjutus.

## Kodutöö 3 tagasiside

Saada kirjalik kokkuvõte enne seminari. Tunnis nimeta kolm asja, mida kodutöös 4 kindlasti teisiti tehakse, ja vasta küsimustele. 2026. aastal olid need: tahvel peab töö ajal liikuma, Issue'd tulevad tootest ja mitte kodutöö punktidest, ülevaatus on sisuline. Pikem jutt automaathindamisest, AI mahust ja linkidest kuulub kirjalikku tagasisidesse.

## „Selgita oma otsust”

Harjutus töötas 2026. aastal hästi ja jääb samaks: 10 minutit ettevalmistust, iga tiim vastab kolmele küsimusele, viimane on suurim kontrollimata eeldus. Küsi iga tiimi järel ühe küsimuse: kuidas te selle eelduse kontrolliksite ja kellelt? Vastus läheb kohe tahvlile Issue'na. Tagumise rea tiimid tulevad rääkima ette, muidu ei kuule keegi.

## Harjutused

Iga harjutuse ajal käi tiimid läbi ja küsi ühe asja:

- kontrolltingimus: kust see arv tuleb?
- testjuhtum: kas kavand annab igale sammule vastuse? Kui ei, kus on auk?
- riskikaart: kes on vastutaja ja mis on tema esimene tegevus?

Harjutuse tulemus commit'itakse seminari lõpuks, ka pooleli kujul. Nii on kodutöös millestki jätkata.

## Blokeerija

Näita mõlemat otsa: ootav Issue saab sildi `blocked` ja kommentaari; blokeeriv Issue võib saada sildi `blocker` või seose „blocked by” kaudu märke „Blocking”. Andmeallika Issue on peaaegu alati esimene blokeeritud kaart.

## Git

Demo terminalis, sama VS Code'i Source Control vaates. Igaüks käivitab `git log --oneline` tiimi repos ja vaatab, kas sõnumitest saab aru. `git restore` harjutus on konspektis ja jääb koju.

## Ohukohad

- „Kiire, turvaline ja mugav” jääb mõõtmata loosungiks. Küsi allikat.
- Arv pakutakse peast. Kui allikat pole, märgitakse piir eeldusena ja läheb riskikaardile.
- Riskitabel paisub AI abil, olulised riskid kaovad müra sisse.
- Vastutajaks märgitakse „meeskond”. Palu nimetada roll ja esimene tegevus.
- Riskikaart ei muuda ühtegi varasemat otsust. Siis on see tehtud kodutöö pärast.
