# Kodutöö 3: tööviis, süsteemi kontseptsioon ja release `v0.2.0`

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](../../docs/projekti-tookorraldus.md).

## Ülesanne lühidalt

Põhjendage meeskonna tööviis ja süsteemi üldine kontseptsioon. Süsteemi kontseptsioon on lühike kirjeldus sellest, mis süsteem see on, kellele see on mõeldud ja kuidas see põhimõtteliselt töötab. Iga tiimiliige sõnastab valideeritud vajaduse põhjal vähemalt ühe kasutajaloo koos kontrolltingimusega ([näide](seminar.md#näide-tõendist-kasutajalooni)) ja vaatab läbi ühe kaaslase loo. Kokku on tiimil vähemalt kaks lugu (juhul kui lood langevad kokku). Näidake rollide erinevaid vaatenurki, vaadake üksteise muudatused üle ning avaldage release `v0.2.0 – Tööviis ja süsteemi kontseptsioon`.

## Maht

Arvestuslik maht on ligikaudu 8 tundi õppija kohta. Teksti pikkus ei ole eesmärk; hinnatav on arusaamine ja põhjendamine.

## Failid repos etapi lõpus

Selles etapis lisandub või muutub tiimi repos:

```text
README.md                                 täiendatud: selle etapi rollid, töövoog ja lingid uutele failidele
decisions/002-tooviisi-valik.md           ühine, alustate seminaris
decisions/003-susteemi-kontseptsioon.md   ühine: kasutaja teekond, kasutajalood ja kontseptsioon
releases/v0.2.0.md                        ühine
reflections/oppija-nimi-v0.2.0.md         igal õppijal oma fail
```

Seminari 2 failid (`research/`, `decisions/001-probleemi-valik.md`, `reflections/…-v0.1.0.md`, `releases/v0.1.0.md`) jäävad alles ja neid üle ei kirjutata. Kui arusaam probleemist muutus, põhjendage muutust failis `003` ja release notes'i osas „Mis muutus pärast eelmist release'i?”.

Seminaris 2 töötas igaüks esmalt oma failis. Nüüd kirjutate ühiseid faile. Iga õppija panus on näha loo autori ja ülevaataja väljadest, PR-ide ajaloost ja refleksioonist.

Skeem on vabatahtlik, kui selge tekst annab sama info edasi. GitHub Projectsi tahvlil on etapi backlog: igal Issue'l on vastutaja ja ajahinnang.

## Faili `003` koostamine

Faili `decisions/003-susteemi-kontseptsioon.md` alustate seminaris kasutaja teekonna ja kasutajalugudega. Kodutöös lisate kontseptsiooni ja kaalutud lahendussuunad.

Kontseptsiooni koostage skeemi „probleem → kasutaja teekond → kasutajalood → kontseptsioon” järjekorras ([selgitus](seminar.md#probleemist-kontseptsioonini)):

**1. Kasutaja teekond.** Kirjeldage lühidalt tekstina, kuidas kasutaja praegu oma eesmärgini jõuab ja millistel sammudel ta takerdub. Prototüüpi ega kujundust ei nõuta.
Vastutaja: projektijuht

**2. Kasutajalood.** Lood teevad probleemist konkreetsed vajadused, mille täitmist saab kontrollida. Neist saavad backlog'i Issue'd ja seminaris 4 testjuhtumid. Iga tiimiliige kirjutab vähemalt ühe loo sammu kohta, kus probleem esineb ([mall](../mallid/kasutajalugu.md), [näide](user-stories-example.md)). Lugu lähtub seminari 2 tõendist ja sellel on kontrolltingimus. Kokku on vähemalt kaks lugu. Kogu süsteemi ei pea lugudega katma.
Vastutajad: projektijuht, disainer

**3. Ülevaatus.** Iga tiimiliige vaatab kaaslase PR-is läbi ühe loo: kas see lähtub tõendist ja kas kontrolltingimust saab kontrollida? Märkige iga loo juurde autor, tõend ja ülevaataja. Kattuvad või vastuolulised lood ühendage või täpsustage.

**4. Kontseptsioon ja arhitektuur.** Kirjeldage süsteemi peamised osad ja nende vastutus (milleks iga osa on vajalik) ning välised sõltuvused. Iga osa peab olema vajalik mõne loo või sõltuvuse jaoks. Info liikumise kirjeldus (kust info tuleb ja millise osani see jõuab) on valikuline, kuid annab punkte. Sobib skeem või tekst, kui see seoseid selgitab. Võite valida ka tehnoloogiapinu (stack).
Vastutajad: disainer, arhitekt.

## Tööjaotus, umbes 8 tundi õppija kohta

1. Release `v0.1.0` ja tagasiside analüüs – 1 h. Tulemus läheb `releases/v0.2.0.md` osasse „Mis muutus pärast eelmist release'i?”.
2. Rolli vaatenurgast vajaduste ja konfliktide sõnastamine – 1 h. Vähemalt üks lahkarvamus ja selle lahendus on kirjas failis `002` või `003`.
3. Tööviiside võrdlemine ja otsuse põhjendamine – 1 h.
4. Backlog'i täpsustamine, töö järjestamine ja ajahinnangud – 1 h.
5. Kasutajalugude ([näide](seminar.md#näide-tõendist-kasutajalooni)) ja süsteemi kontseptsiooni koostamine – 2 h.
6. Pull request, teise töö sisuline ülevaatus, merge-konflikti lahendamine ja parandused – 1 h.
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

Lood ja kontseptsioon tulevad samast probleemist: probleem → kasutaja teekond → kasutajalood → kontseptsioon ([selgitus](seminar.md#probleemist-kontseptsioonini)).

Kasutajalugu seob kasutaja, vajaduse ja väärtuse ([näide](seminar.md#näide-tõendist-kasutajalooni)). Kontrolltingimus peab olema piisavalt konkreetne, et meeskond saaks hiljem arutada, kuidas nõude täitmist kontrollida. Ärge tuletage kasutajalugu AI vastusest või lahendusideest ilma tõendita. Terviklik näide koos autori, ülevaataja ja lugude ühendamisega on [näidisfailis](user-stories-example.md).

## Töö planeerimine

Hoidke backlog tahvlil ajakohasena. Etapi lõpus võrrelge ajahinnanguid tegeliku ajakuluga ja kirjutage `releases/v0.2.0.md` faili osasse „Planeerimine”, mida õppisite ja mida järgmises etapis teisiti hindate.

## Rollide vahetamine

Selle etapi rollid on:

- **projektijuht** vastutab kogu protsessi eest: töö, aja ja sõltuvuste juhitavuse eest;
- **release manager** koordineerib release'i ja avaldab selle;
- **disainer** vastutab süsteemi kontseptsiooni ja disaini põhimõtete eest;
- **arhitekt** mängib läbi, millistest osadest lahendus koosneb ja milline tehnoloogiline lahendus võiks sobida.

Rollid ja nende vastutajad on kirjas README-s. Iga õppija dokumenteerib vähemalt ühe tähelepaneku enda selle etapi rollist. Järgmises seminaris rollid vahetuvad. Väikeses meeskonnas võib ühel õppijal olla kaks rolli, kuid vastutused peavad olema selgelt nimetatud.

## GitHubi töövoog

Iga õppija seob enda Issue, haru, sisulise commit'i ja pull request'i. Igaüks vaatab üle vähemalt ühe teise liikme PR-i. Ülevaatus peab kommenteerima põhjendust või riski, mitte ainult õigekirja. Ühises failis tekkivad merge-konfliktid lahendage [konfliktide lahendamise juhendi](../../concepts/mergeConflict/README.md) järgi. Üks konflikt tuleb kodutöös teadlikult läbi teha, vt järgmist osa.

## Merge-konflikt ühises failis

Seminaris lahendas iga tiim ühe konflikti. Kodutöös lahendab konflikti iga õppija, kes seminaris seda ise ei teinud.

**Olukord.** Kaks tiimiliiget lisavad oma kasutajaloo faili `decisions/003-susteemi-kontseptsioon.md` samal ajal ja samasse kohta: osa „Kasutajalood” lõppu.

1. Mõlemad loovad oma haru samast `main`-i seisust, enne kui kumbki PR on ühendatud.
2. Mõlemad lisavad oma loo osa „Kasutajalood” viimase loo järele, teevad commit'i, push'ivad ja avavad PR-i.
3. Esimene PR vaadatakse üle ja ühendatakse `main`-i.
4. Teise PR-i juures näitab GitHub teadet **This branch has conflicts that must be resolved**.
5. Teise PR-i autor lahendab konflikti terminalis [konfliktide lahendamise juhendi](../../concepts/mergeConflict/README.md) järgi: toob `main`-i uue seisu oma harusse, parandab faili, märgib konflikti lahendatuks, teeb commit'i ja push'ib. Lühiversioon on [projekti töökorralduse juhendis](../../docs/projekti-tookorraldus.md).
6. Tavaliselt jäävad alles mõlemad lood. Parandage loo numbrid. Kui lood kattuvad, ühendage need koos teise autoriga.

**Kontrollpunkt:** failis pole märke `<<<<<<<`, `=======` ega `>>>>>>>`, mõlemad lood on alles ja PR on ühendatud.

**Kajastamine.** Konflikti lahendaja lisab oma PR-i kommentaari:

- millises failis ja osas konflikt tekkis;
- kelle muudatused kokku puutusid (PR-ide numbrid);
- mis jäi alles ja miks;
- konflikti lahendava commit'i link.

Lisage selle kommentaari link ka oma kodutöö Issue kommentaari.

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
- [ ] Iga lugu on seotud teekonna sammuga ja iga kontseptsiooni osa on vajalik mõne loo või sõltuvuse jaoks.
- [ ] Alternatiivid, kompromissid ja teadmatused on nähtavad.
- [ ] Rollide vaatenurgad mõjutasid vähemalt üht otsust.
- [ ] Igal õppijal on Issue, commit, PR, ülevaatus ja refleksioon.
- [ ] Iga õppija, kes seminaris konflikti ise ei lahendanud, on kodutöös lahendanud ühe merge-konflikti ja kirjeldanud seda oma PR-i kommentaaris.
- [ ] Release `v0.2.0` on avaldatud.

## Esitamine

Lisage kodutöö Issue kommentaari release'i, enda refleksiooni, enda PR-i ja tehtud ülevaatuse lingid. Kui lahendasite kodutöös merge-konflikti, lisage ka konflikti kirjeldava PR-i kommentaari link. Eraldi esitamise PR-i pole vaja; PR-id teete töö käigus tiimi repos.

## Hindamiskriteeriumid

Hindan tiimi ühist tulemust repositooriumis ning iga õppija panust tema Issue'i, PR-i, ülevaatuse ja refleksiooni põhjal. Kokku on võimalik saada 100 punkti.

| Kriteerium | Punktid | Mida repositooriumist vaatan |
|---|---:|---|
| Tööviisi valik | 15 | Vähemalt kolm varianti on võrreldud. Valik lähtub teie probleemist, ebakindlusest ja meeskonnast, mitte meetodi populaarsusest. |
| Kasutajalood ja kontrolltingimused | 15 | Igal tiimiliikmel on vähemalt üks kasutajalugu ja ühe kaaslase loo ülevaatus, kokku vähemalt kaks lugu ([näide](seminar.md#näide-tõendist-kasutajalooni)). Lood lähtuvad seminaris 2 kogutud tõendist ning igal lool on piisavalt konkreetne kontrolltingimus, autor, tõend ja ülevaataja. Kattuvad või vastuolulised lood on ühendatud või täpsustatud. |
| Süsteemi kontseptsioon | 25 | Kasutaja teekond, süsteemi piir, peamised osad ja nende vastutus ning välised sõltuvused on arusaadavad. Vähemalt kaks lahendussuunda on kaalutud (kokku kuni 20 p). Valikuline: info liikumine osade vahel on kirjeldatud (kuni 5 p). |
| Töö planeerimine | 10 | Backlog on järjestatud ning igal Issue'l on vastutaja ja ajahinnang. Release notes võrdleb ajahinnangut tegeliku ajakuluga ja nimetab järgmise etapi paranduse. |
| Tiimitöö ja iga õppija panus | 15 | Iga õppija panus on jälgitav Issue'i, commit'i ja PR-i kaudu. Ülevaatus kommenteerib põhjendust või riski. Rollide vaatenurgad mõjutasid vähemalt üht otsust. Merge-konflikt on lahendatud ja PR-i kommentaaris kirjeldatud. |
| Refleksioon ja AI kasutamise läbipaistvus | 10 | Iga õppija refleksioon kirjeldab tema panust, rolli ja õpitut. Kui AI-d selles etapis kasutati, on näha sisend, väljundi kasutamine, kontroll ja tegelik kasu. |
| Repositooriumi korrastatus ja release | 10 | README kirjeldab rolle ja töövoogu, nõutud failid on leitavad, muudatused on jõudnud `main`-i PR-ide kaudu ning `v0.2.0` release on avaldatud. |

**Tulemuse tõlgendamine:** 90–100 punkti tähendab põhjendatud ja jälgitavat tööd; 75–89 punkti puhul on tulemus olemas, kuid mõni osa vajab täiendamist; 60–74 punkti puhul takistab oluline lünk järgmises seminaris jätkamist; alla 60 punkti korral ei ole tööviisi ja kontseptsiooni piisavalt põhjendatud või panust ja otsuseid ei saa repo põhjal hinnata.

Tööviisi valiku ja süsteemi kontseptsiooni eest peab saama kokku vähemalt poole nende kahe kriteeriumi punktidest. Korras README või release ei korva põhjendamata otsuseid. Töötava rakenduse, prototüübi ega dokumentide hulga eest eraldi punkte ei anta. AI puhul hinnatakse kasutamise eesmärki ja väljundi kontrollimist, mitte genereeritud teksti mahtu.
