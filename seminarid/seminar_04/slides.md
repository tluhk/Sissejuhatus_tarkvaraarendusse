---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 4 – kvaliteet, riskid ja vastutus
---

# Seminar 4

## Kvaliteet, riskid ja vastutus

---

## Kogu kursuse teekond: kus oleme?

Probleem → kasutajate ja vajaduste uurimine → nõuete kirjeldamine → töö
planeerimine → lahenduse disainimine → arendamine → **testimine ja tagasiside —
seminar 4** → avaldamine ja hooldus

- seminar 1: suur pilt ja töövahendite seadistamine
- seminar 2: kliendisoovist arendusülesandeni
- seminar 3: rollid, tööviisi valik ja süsteemi kontseptsioon
- **seminar 4: kvaliteet, riskid ja vastutus**
- seminar 5: kasutuselevõtt, tagasiside ja hooldus
- eksam: dokumenteeritud protsessi esitlus release'ide ajajoonena

**Projekti tulemus:** dokumenteeritud arendusprotsess ja otsuste logi; töötavat rakendust ega klikitavat prototüüpi ei nõuta.

---

# Kui tarkvara töötab, kas see on kvaliteetne?

---

## Mitte tingimata

See võib olla aeglane, ebaturvaline, raskesti kasutatav, ligipääsmatu või kallis hooldada.

Kvaliteet tähendab sobivust päris kasutusolukorda.

---

## Funktsioon ja kvaliteediomadus

**Funktsioon:** mida süsteem võimaldab teha?

**Kvaliteediomadus:** kui hästi või millistel tingimustel peab see toimuma?

---

## Testjuhtum seob nõude kontrolliga

- eeldused või algseis
- tegevuse sammud
- oodatud tulemus

Test võrdleb oodatud ja tegelikku tulemust. Läbikukkumine näitab erinevust, mitte veel selle põhjust.

---

# „Süsteem peab olema kiire.”

Kas see on kontrollitav nõue?

---

## Muuda see konkreetseks

> Kasutaja saab tavapärase koormuse ajal otsingutulemuse kahe sekundi jooksul.

Kontrollimiseks on vaja konteksti, piiri ja mõõdupuud.

---

## Kvaliteeti nähakse eri moodi

- kasutaja: eesmärk, arusaadavus ja turvalisus
- organisatsioon: väärtus ja kohustused
- arendaja: muudetavus
- käitaja: märgatavus ja taastatavus
- ühiskond: mõju ja ligipääs

---

# Kas kõiki kvaliteediomadusi saab maksimeerida?

---

## Valikud sisaldavad kompromisse

Turvalisus võib lisada samme.

Töökindlus võib tõsta hinda.

Kiire tarne võib kasvatada hooldusvõlga.

---

## Risk ei ole lihtsalt ohtude loend

- mis võib juhtuda?
- kellele tekib mõju?
- kuidas ennetame või vähendame?
- kuidas märkame?
- kes reageerib?

---

## Pärisprojekti peegel

Cloudflare'i 2019. aasta katkestus:

- vigane muudatus
- kiire ülemaailmne levitamine
- suur mõju
- tagasipööramine
- testimise ja protsessi parandused

[Allikas](https://blog.cloudflare.com/cloudflare-outage/)

---

# Kas katkestuse põhjustas ainult vigane kood?

---

## Süsteemne vastus

Kood, testimine, levitamine, seire ja otsustusprotsess mõjutasid koos nii rikke tekkimist kui ka ulatust.

---

# Kuidas viga uurida?

## Silumise lihtne ring

1. Korda viga võimalikult väikese näitega.
2. Pane kirja oodatud ja tegelik tulemus.
3. Kitsenda võimalikke põhjuseid ja kontrolli hüpoteesi.
4. Pärast parandust korda testi ning lisa kontroll, et viga ei korduks.

Näide: keskmise arvutamise funktsioon jagab summa kirjete arvuga. Mis juhtub tühja loendiga? Kuidas seda viga korrata ja millist tulemust peaksime ootama?

Koodi lugemise näide: oodatud keskmine on `4`, tegelik vastus `6`. Katseta sisendiga `[2, 4, 6]`, jälgi arvutust ja leia vea põhjus.

```js
function average(values) {
  const total = values.reduce((sum, value) => sum + value, 0);
  return total / (values.length - 1);
}
```

---

## Turvalisus ja privaatsus

- kas andmeid on vaja?
- kellel on ligipääs?
- kui kaua neid hoitakse?
- mis juhtub lekke korral?
- kuidas inimene saab kasutusest aru?

---

## Ligipääsetavus

Mõelge nägemise, kuulmise, motoorika, keele, seadme, võrgu ja digioskuse erinevustele.

Ligipääsetavust kavandatakse algusest.

---

## Kolmandad osapooled

Teek, pilveteenus, andmestik, font või AI-mudel toob lisaks kasule:

- litsentsi ja tingimused
- andmete liikumise
- hinna ja jätkusuutlikkuse
- sõltuvuse ja asendatavuse küsimuse

---

## Tänane meeskonnatöö

1. Vahetage rollid.
2. Valige 4–6 kvaliteediomadust.
3. Tehke need kontrollitavaks.
4. Kaardistage riskid ja vastutus.
5. Vaadake varasemad otsused üle.

---

# Mida uus risk meie varasemas kavandis muudab?

---

## Muutus ei ole läbikukkumine

Kui uus info muudab otsust, on arendusprotsess oma eesmärki täitnud.

Dokumenteerige põhjus, mõju ja kompromiss.

---

# Kodutöö

## `v0.3.0 – Kvaliteedi- ja riskiplaan`

Iga õppija: sisuline panus, PR, ülevaatus ja refleksioon.

