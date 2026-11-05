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
planeerimine → lahenduse disainimine → arendamine → **testimine ja tagasiside –
seminar 4** → avaldamine ja hooldus

- seminar 1: suur pilt ja töövahendite seadistamine
- seminar 2: kliendisoovist arendusülesandeni
- seminar 3: rollid, tööviisi valik ja süsteemi kontseptsioon
- **seminar 4: kvaliteet, riskid ja vastutus**
- seminar 5: kasutuselevõtt, tagasiside ja hooldus
- eksam: dokumenteeritud protsessi esitlus release'ide ajajoonena

**Projekti tulemus:** dokumenteeritud arendusprotsess ja otsuste logi; töötavat rakendust ega klikitavat prototüüpi ei nõuta.

---

## Arendamise etapp

Arendajad muudavad nõuded ja kavandi töötavaks tarkvaraks: kirjutavad koodi, teevad tehnilisi valikuid, vaatavad üksteise koodi üle ja parandavad vigu.

Sellel kursusel me rakendust ei ehita, sest eesmärk on näha kogu protsessi. Täna vaatame arendustööd väikese koodinäite kaudu.

<!-- Tulevikus: arendaja töö võib nihkuda kirjutamiselt suunamisele ja kontrollile. Samaks jääb: arendaja vaatab töö üle ja töövoogude arvu piirab see, kui palju ta suudab korralikult üle vaadata. -->

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

<!-- Tulevikus: reeglid võivad olla töövoogu sisse ehitatud, näiteks saladuste kaitse. Pelk juhis ei taga nende täitmist. Samaks jääb: reeglil on nimeline omanik. -->

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

---

## Koodi lugemise näide

Oodatud keskmine on `4`, tegelik vastus `6`. Katseta sisendiga `[2, 4, 6]`, jälgi arvutust ja leia vea põhjus.

```js
function average(values) {
  const total = values.reduce((sum, value) => sum + value, 0);
  return total / (values.length - 1);
}
```

<!-- Tulevikus: kontrollid võivad käia pidevalt ja viga kinnitatakse enne parandust ebaõnnestuva testiga. Samaks jääb: parandav agent ei tohi kontrolli nõrgendada ja PR-i vaatab üle koodi omanik. -->

---

## Koodi ülevaatus sama näitega

Kaaslane pakub pull request'is sellist parandust:

```js
function average(values) {
  const total = values.reduce((sum, value) => sum + value, 0);
  return total / values.length;
}
```

- Kas kood teeb seda, mida PR lubab?
- Mis juhtub tühja loendiga?
- Millise küsimuse sa ülevaatuses esitaksid?

<!-- 5 minutit. Sisend [2, 4, 6] annab nüüd 4, tühi loend annab NaN. Kommenteerime koodi, mitte inimest. -->

<!-- Tulevikus: AI võib teha esimese ülevaatuse ja järjestada leiud tõsiduse järgi. Samaks jääb: koodi kirjutanud agent ei saa seda heaks kiita, kinnituse annab inimene. -->

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

1. Vaadake Projectsi tahvlit: mis jäi pooleli ja kuidas hinnangud pidasid?
2. Vahetage rollid ja uuendage backlog'i.
3. Valige 4–6 kvaliteediomadust.
4. Tehke need kontrollitavaks.
5. Kaardistage riskid ja vastutus.
6. Vaadake varasemad otsused üle.

---

## Giti ajalugu ja tagasivõtmine

```bash
git log --oneline
git diff
git restore proov.md
```

- `log`: kas sõnumitest saab aru, mida tehti?
- `diff`: mis on veel commit'imata?
- `restore`: kustutab faili commit'imata muudatused. Neid ei saa tagasi.

<!-- Õppija muudab mõnda proovifaili, vaatab git diff väljundi ja võtab muudatuse tagasi. Näita sama ka VS Code'is. -->

---

# Mida uus risk meie varasemas kavandis muudab?

---

## Muutus ei ole läbikukkumine

Kui uus info muudab otsust, on arendusprotsess oma eesmärki täitnud.

Dokumenteerige põhjus, mõju ja kompromiss.

---

## Tuleviku küsimus

Millist tänase teema tööd võiks teha AI, kuidas tulemust kontrolliksime ja kes vastutaks?

---

# Kodutöö

## `v0.3.0 – Kvaliteedi- ja riskiplaan`

Iga õppija: sisuline panus, PR, ülevaatus ja refleksioon.

