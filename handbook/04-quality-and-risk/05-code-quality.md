[← Riskid](04-risks.md) | [Sisukord](../README.md) | [Järgmine: Giti oskus: ajalugu ja tagasivõtmine →](06-git-history.md)

# Koodi kvaliteet

**Märge:** Iseseisev

Kood loetakse palju rohkem kordi, kui see kirjutatakse. Hea kood ei ole ainult töötav kood, vaid kood, millest teine inimene aru saab ja mida ta julgeb muuta. Sellel lehel on põhimõtted, mida kohtad järgmistes ainetes.

## Loetavus

Võrdle:

```javascript
function f(a) {
  return a.filter(x => x.d > Date.now())[0];
}
```

```javascript
function findNextLecture(lectures) {
  const now = Date.now();
  return lectures.find(lecture => lecture.startTime > now);
}
```

Mõlemad teevad sama. Teisest saab aru ilma selgituseta, sest nimed ütlevad, mida asjad tähendavad.

- **Nimed** ütlevad, mis asi see on: `lectures`, mitte `a`.
- **Funktsioon teeb ühte asja** ja selle nimi ütleb, mida.
- **Kommentaar selgitab, miks**, mitte mida. Mida kood teeb, peab nägema koodist endast.

## Kokkulepped

Meeskond lepib kokku ühtse stiili: taanded, nimede kuju, failide paigutus. Kui kõik kirjutavad ühtemoodi, keskendub ülevaatus sisule, mitte tühikutele.

Tööriistad teevad selle automaatseks:

- **Vormindaja** (*formatter*), näiteks Prettier, muudab koodi kuju kokkulepitud stiiliks.
- **Linter**, näiteks ESLint, leiab tüüpilisi vigu ja halbu tavasid, näiteks kasutamata muutuja.

Mõlemad töötavad VS Code'i laiendusena ja märgivad probleemid kohe redaktoris.

## Tehniline võlg

**Tehniline võlg** (*technical debt*) tekib, kui valitakse kiire lahendus, mis tuleb hiljem ümber teha. Nagu laenu puhul, tuleb hiljem maksta ka intressi: iga uus muudatus on aeglasem, sest tuleb arvestada vana kiirlahendusega.

Võlg ei ole alati halb. Mõnikord on mõistlik kiiresti midagi proovida. Oluline on, et võlg on **teadlik ja kirja pandud**, näiteks backlog'is eraldi Issue'na.

## AI ja koodi kvaliteet

AI kirjutab kiiresti koodi, mis töötab. See ei tähenda, et kood on loetav, turvaline või meeskonna kokkulepetega kooskõlas. AI loodud kood läbib sama ülevaatuse ja samad tööriistad nagu inimese oma.

## Kontrolli ennast

1. Miks on loetavus oluline, kui kood niikuinii töötab?
2. Mis vahe on linteril ja vormindajal?
3. Too näide olukorrast, kus tehnilise võla võtmine on mõistlik.

---

[← Riskid](04-risks.md) | [Sisukord](../README.md) | [Järgmine: Giti oskus: ajalugu ja tagasivõtmine →](06-git-history.md)
