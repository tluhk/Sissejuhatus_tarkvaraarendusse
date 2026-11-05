# Kodutöö 3: tööviis, süsteemi kontseptsioon ja release `v0.2.0`

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](../../docs/projekti-tookorraldus.md).

## Ülesanne lühidalt

Põhjendage meeskonna tööviis ja süsteemi üldine kontseptsioon. Süsteemi kontseptsioon on lühike kirjeldus sellest, mis süsteem see on, kellele see on mõeldud ja kuidas see põhimõtteliselt töötab. Iga tiimiliige sõnastab valideeritud vajaduse põhjal vähemalt ühe kasutajaloo koos kontrolltingimusega ([näide](seminar.md#näide-tõendist-kasutajalooni)) ja vaatab läbi ühe kaaslase loo. Kokku on tiimil vähemalt kaks lugu. Näidake rollide erinevaid vaatenurki, vaadake üksteise muudatused üle ning avaldage release `v0.2.0 – Tööviis ja süsteemi kontseptsioon`.

## Maht

Arvestuslik maht on ligikaudu 8 tundi õppija kohta. Teksti pikkus ei ole eesmärk; hinnatav on arusaamine ja põhjendamine.

## Meeskonna tulemus

Vähemalt:

```text
decisions/002-tooviisi-valik.md
decisions/003-susteemi-kontseptsioon.md
releases/v0.2.0.md
reflections/oppija-nimi-v0.2.0.md
```

Täiendage ka README-s rollide ja töövoo osa. Skeem on vabatahtlik, kui selge tekst annab sama info edasi. GitHub Projectsi tahvlil on etapi backlog: igal Issue'l on vastutaja ja ajahinnang.

Iga tiimiliige kirjutab vähemalt ühe kasutajaloo koos kontrolltingimusega ([näide](seminar.md#näide-tõendist-kasutajalooni)). Lugu peab lähtuma seminaris 2 kogutud tõendist. Iga tiimiliige vaatab läbi ka ühe kaaslase loo: kas see lähtub tõendist ja kas kontrolltingimust saab kontrollida? Ülevaatus käib kaaslase PR-is. Märkige iga loo juurde autor, tõend ja ülevaataja. Kokku peab kontseptsioonis olema vähemalt kaks kasutajalugu. Kui lood kattuvad või on vastuolus, ühendage või täpsustage need. Kirjeldage lühidalt tekstina, kuidas kasutaja oma eesmärgini jõuab; prototüüpi ega kujundust ei nõuta. Kirjeldage kontseptsioonis ka kõrgtaseme arhitektuuri: süsteemi peamised osad, nende vastutus, süsteemi piir, info liikumine ning olulised välised sõltuvused. Skeem pole kohustuslik, kui samad seosed selgitab tekst. See ei nõua tehnoloogiapinu valimist. Kõiki nõudeid ei pea selles etapis ammendavalt loetlema.

## Tööjaotus, umbes 8 tundi õppija kohta

1. Release `v0.1.0` ja tagasiside analüüs – 1 h.
2. Rolli vaatenurgast vajaduste ja konfliktide sõnastamine – 1 h.
3. Tööviiside võrdlemine ja otsuse põhjendamine – 1 h.
4. Backlog'i täpsustamine, töö järjestamine ja ajahinnangud – 1 h.
5. Kasutajalugude ([näide](seminar.md#näide-tõendist-kasutajalooni)) ja süsteemi kontseptsiooni koostamine – 2 h.
6. Pull request, teise töö sisuline ülevaatus ja parandused – 1 h.
7. Individuaalne refleksioon ja release – 1 h.

Vähemalt üks sinu commit peab järgima seminari head tava: see teeb ühe
loogilise muudatuse ja sõnum kirjeldab tulemust (näiteks `Describe system
boundary`), mitte ainult tegevust (`update` või `fix`).

## Nõuded otsustele

Kursus paneb paika release'id, töövoo ja rollivahetuse. Tiim valib, kuidas töö etapi sees käib: kuidas ja kui tihti planeerite, kuidas tööd jagate, kui palju on korraga pooleli ja kuidas muudate plaani. Valiku aluseks võrrelge [tööviise](seminar.md#tööviisid-ei-ole-usutunnistused): Waterfall, iteratiivne ja inkrementaalne arendus, agiilne lähenemine, Scrum, Kanban ja Lean. Pikem selgitus on [arendusmeetodite juhendis](../../concepts/arendusmeetodid/README.md).

Tööviisi otsus sisaldab vähemalt kolme võrreldud varianti. Selgitage, kuidas valik sobib just teie probleemi, ebakindluse ja meeskonnaga. Kui ühendate eri meetodite võtteid, nimetage iga võtte eesmärk.

Süsteemi kontseptsiooni otsus sisaldab vähemalt kaht kaalutud lahendussuunda ning põhjendab süsteemi piiri. Ärge valige tehnoloogiapinu lihtsalt sellepärast, et see on tuttav või AI pakkus seda.

### Näide süsteemi kontseptsioonist

**See näide on väljamõeldud.** See lähtub demorepo probleemist, et kasutaja ei saa aru, kas tunniplaani info on värske. Teie kontseptsioon peab lähtuma teie tiimi kontrollitud probleemist, ärge kopeerige seda.

> **Eesmärk:** tudeng näeb, kas tema tunniplaan on ajakohane ja mis on viimati muutunud.
>
> **Osalised:** tudeng vaatab, õppekorraldaja sisestab muudatusi.
>
> **Piir:** süsteem näitab tunniplaani ja muudatusi. Süsteem ei koosta tunniplaani ega broneeri ruume.
>
> **Teekond:** tudeng avab oma rühma plaani, näeb viimase uuenduse aega, märkab muutunud tundi ja saab sellest kohe aru.
>
> **Osad:** tunniplaani vaade, muudatuste kuvamine ja andmete uuendamine.
>
> **Info liikumine:** õppekorraldaja muudab plaani olemasolevas süsteemis, sealt jõuab info tunniplaani vaatesse koos ajatempliga.
>
> **Sõltuvus:** olemasolev tunniplaani andmeallikas.
>
> **Teadmatus:** kui kiiresti muudatus andmeallikast kohale jõuab?

Kaks kaalutud lahendussuunda võiksid selles näites olla: **A)** lisada ajatempel ja muudatuste märge olemasolevale lehele; **B)** luua eraldi rakendus, mis saadab teavitusi. Otsuses selgitage, kumb lahendab kontrollitud probleemi paremini, mis on selle hind ja mida valik välja jätab.

Nii ei tasu kirjutada: „Teeme Reacti ja PostgreSQL-iga moodsa veebirakenduse, kus on sinine menüü.” See nimetab tehnoloogia ja kujunduse, aga ei ütle, millist probleemi süsteem lahendab ega kus on selle piirid.

### Kasutajalood

Kasutajalugu seob kasutaja, vajaduse ja väärtuse ([näide](seminar.md#näide-tõendist-kasutajalooni)). Kontrolltingimus peab olema piisavalt konkreetne, et meeskond saaks hiljem arutada, kuidas nõude täitmist kontrollida. Ärge tuletage kasutajalugu AI vastusest või lahendusideest ilma tõendita. Terviklik näide koos autori, ülevaataja ja lugude ühendamisega on [näidisfailis](user-stories-example.md).

## Töö planeerimine

Hoidke backlog tahvlil ajakohasena. Etapi lõpus võrrelge ajahinnanguid tegeliku ajakuluga ja kirjutage `releases/v0.2.0.md` faili osasse „Planeerimine”, mida õppisite ja mida järgmises etapis teisiti hindate.

## Rollide vahetamine

Iga õppija dokumenteerib vähemalt ühe tähelepaneku enda selle etapi rollist. Järgmises seminaris rollid vahetuvad. Väikeses meeskonnas võib ühel õppijal olla kaks rolli, kuid vastutused peavad olema selgelt nimetatud.

## GitHubi töövoog

Iga õppija seob enda Issue, haru, sisulise commit'i ja pull request'i. Igaüks vaatab üle vähemalt ühe teise liikme PR-i. Ülevaatus peab kommenteerima põhjendust või riski, mitte ainult õigekirja. Kui ühises failis tekib merge-konflikt, lahendage see [konfliktide lahendamise juhendi](../../concepts/mergeConflict/README.md) järgi.

## AI kasutamine

Kursuse jooksul tuleb AI-d kasutada vähemalt ühe olulise otsuse juures. Kui teete seda selles etapis, dokumenteerige:

- mida AI-le sisendina andsite;
- millist vastust kasutasite või ei kasutanud;
- kuidas kontrollisite vastuse sobivust;
- milline oli tegelik kasu;
- millist ebaolulist või eksitavat materjali pidite eemaldama.

## Release manager

Release manageri roll läheb õppijale, kes ei teinud eelmist release'i. Ta kontrollib PR-e ja release notes'i, loob tag'i `v0.2.0` ning avaldab GitHub Release'i pealkirjaga `Tööviis ja süsteemi kontseptsioon`.

## Valmis töö kontroll

- [ ] Tööviisi valik võrdleb vähemalt kolme varianti.
- [ ] Valik lähtub projekti olukorrast, mitte meetodi populaarsusest.
- [ ] Backlog on järjestatud ning hinnangu ja tegeliku ajakulu võrdlus on release notes'is.
- [ ] Süsteemi eesmärk, kasutaja teekond, piir, osalised, suuremad osad, nende vastutus, seosed ja sõltuvused on arusaadavad.
- [ ] Iga tiimiliige on kirjutanud vähemalt ühe kasutajaloo ja vaadanud läbi ühe kaaslase loo; kokku on vähemalt kaks lugu ([näide](seminar.md#näide-tõendist-kasutajalooni)).
- [ ] Iga lugu lähtub tõendist ning selle juures on kontrolltingimus, autor, tõend ja ülevaataja.
- [ ] Alternatiivid, kompromissid ja teadmatused on nähtavad.
- [ ] Rollide vaatenurgad mõjutasid vähemalt üht otsust.
- [ ] Igal õppijal on Issue, commit, PR, ülevaatus ja refleksioon.
- [ ] Release `v0.2.0` on avaldatud.

## Esitamine

Lisage kodutöö Issue kommentaari release'i, enda refleksiooni, enda PR-i ja tehtud ülevaatuse lingid. Eraldi esitamise PR-i pole vaja; PR-id teete töö käigus tiimi repos.

## Hindamiskriteeriumid

Hindan tiimi ühist tulemust repositooriumis ning iga õppija panust tema Issue'i, PR-i, ülevaatuse ja refleksiooni põhjal. Kokku on võimalik saada 100 punkti.

| Kriteerium | Punktid | Mida repositooriumist vaatan |
|---|---:|---|
| Tööviisi valik | 15 | Vähemalt kolm varianti on võrreldud. Valik lähtub teie probleemist, ebakindlusest ja meeskonnast, mitte meetodi populaarsusest. |
| Kasutajalood ja kontrolltingimused | 15 | Igal tiimiliikmel on vähemalt üks kasutajalugu ja ühe kaaslase loo ülevaatus, kokku vähemalt kaks lugu ([näide](seminar.md#näide-tõendist-kasutajalooni)). Lood lähtuvad seminaris 2 kogutud tõendist ning igal lool on piisavalt konkreetne kontrolltingimus, autor, tõend ja ülevaataja. Kattuvad või vastuolulised lood on ühendatud või täpsustatud. |
| Süsteemi kontseptsioon | 25 | Kasutaja teekond, süsteemi piir, peamised osad ja nende vastutus, info liikumine ning välised sõltuvused on arusaadavad. Vähemalt kaks lahendussuunda on kaalutud. |
| Töö planeerimine | 10 | Backlog on järjestatud ning igal Issue'l on vastutaja ja ajahinnang. Release notes võrdleb ajahinnangut tegeliku ajakuluga ja nimetab järgmise etapi paranduse. |
| Tiimitöö ja iga õppija panus | 15 | Iga õppija panus on jälgitav Issue'i, commit'i ja PR-i kaudu. Ülevaatus kommenteerib põhjendust või riski. Rollide vaatenurgad mõjutasid vähemalt üht otsust. |
| Refleksioon ja AI kasutamise läbipaistvus | 10 | Iga õppija refleksioon kirjeldab tema panust, rolli ja õpitut. Kui AI-d selles etapis kasutati, on näha sisend, väljundi kasutamine, kontroll ja tegelik kasu. |
| Repositooriumi korrastatus ja release | 10 | README kirjeldab rolle ja töövoogu, nõutud failid on leitavad, muudatused on jõudnud `main`-i PR-ide kaudu ning `v0.2.0` release on avaldatud. |

**Tulemuse tõlgendamine:** 90–100 punkti tähendab põhjendatud ja jälgitavat tööd; 75–89 punkti puhul on tulemus olemas, kuid mõni osa vajab täiendamist; 60–74 punkti puhul takistab oluline lünk järgmises seminaris jätkamist; alla 60 punkti korral ei ole tööviisi ja kontseptsiooni piisavalt põhjendatud või panust ja otsuseid ei saa repo põhjal hinnata.

Tööviisi valiku ja süsteemi kontseptsiooni eest peab saama kokku vähemalt poole nende kahe kriteeriumi punktidest. Korras README või release ei korva põhjendamata otsuseid. Töötava rakenduse, prototüübi ega dokumentide hulga eest eraldi punkte ei anta. AI puhul hinnatakse kasutamise eesmärki ja väljundi kontrollimist, mitte genereeritud teksti mahtu.
