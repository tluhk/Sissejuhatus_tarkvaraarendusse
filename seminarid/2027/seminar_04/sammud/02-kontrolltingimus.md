# Harjutus 2: Kolm mõõdetavat kontrolltingimust

**Tegija:** tiim, kokku võtab disainer. **Aeg:** 20 minutit. **Fail:** `requirements/quality.md` tiimi repos.

## Eesmärk

Tiimi kasutajalugude kontrolltingimused sisaldavad kvaliteediomadusi ebamääraselt: „kiiresti”, „mugavalt”, „ilma liigse ajakuluta”. Harjutus teeb kolm neist mõõdetavaks ja paneb iga arvu juurde allika. Teooria: [Mõõdetav kvaliteet](../../../../handbook/04-quality-and-risk/01-measurable-quality.md).

## Tegevused

1. Avage oma kasutajalood. Märkige kontrolltingimused, milles on mõõtmata sõna.
2. Valige 3 kvaliteediomadust, mis teie lugudest tulenevad. Vähemalt üks ei ole kasutaja vaatenurgast: näiteks käitaja (kas märkame, kui andmed enam ei lae) või kool (kas andmeid tohib kasutada).
3. Kirjutage iga omadus mõõdetava kontrolltingimusena. Vastake kolmele küsimusele: kes ja mis olukorras, mida kontrollitakse, milline arv või tingimus näitab täitmist.
4. Kirjutage iga piiri juurde allikas. Kui allikat pole, märkige piir eeldusena.
5. Commit ja push seminari lõpuks, ka pooleli kujul.

## Faili näide

Näidisandmed on väljamõeldud; asendage oma lugude ja arvudega.

```markdown
# Kvaliteedinõuded

Seotud otsus: `decisions/004-kvaliteet-ja-riskid.md`. Vastutab: disainer.

| Nr | Omadus | Kontrolltingimus | Lugu | Piiri allikas |
|---|---|---|---|---|
| K1 | kasutatavus | Õppija leiab telefonis oma rühma järgmise loengu aja ja ruumi kuni 10 sekundiga ilma rühma uuesti valimata. | lugu 1 | mõõtsime praegusel lehel: 40 s (3 inimest, 2027-02) |
| K2 | töökindlus | Kui andmeallikas ei vasta, näeb õppija teadet „andmeid ei õnnestunud laadida”, mitte tühja tunniplaani. | lugu 3 | jah-ei tingimus, allikat ei vaja |
| K3 | andmete õigsus | Muutunud tund on märgitud nii värvi kui ka tekstiga „muutunud” hiljemalt 15 minutit pärast muutust allikas. | lugu 2 | **eeldus**: allika uuendussagedus on kontrollimata, vt riskikaart |
```

## Kontrollpunkt

Harjutus on valmis, kui iga rida vastab kolmele küsimusele ja ükski arv pole ilma allikata või eelduse märketa. Kodutöös lisab tiim neljanda nõude, kui lood seda vajavad.
