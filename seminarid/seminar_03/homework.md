# Kodutöö 3: tööviis, süsteemi kontseptsioon ja release `v0.2.0`

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](../../docs/projekti-tookorraldus.md).

## Ülesanne lühidalt

Põhjendage meeskonna tööviis ja süsteemi üldine kontseptsioon. Sõnastage vähemalt kaks kasutajalugu valideeritud vajaduse põhjal ning lisage kummalegi kontrolltingimus. Näidake rollide erinevaid vaatenurki, vaadake üksteise muudatused üle ning avaldage release `v0.2.0 – Tööviis ja süsteemi kontseptsioon`.

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

Täiendage ka README-s rollide ja töövoo osa. Skeem on vabatahtlik, kui selge tekst annab sama info edasi.

Lisage süsteemi kontseptsiooni juurde vähemalt kaks kasutajalugu, mis lähtuvad seminaris 2 kogutud tõendist. Lisage kummalegi üks kontrolltingimus. Kirjeldage kontseptsioonis ka kõrgtaseme arhitektuuri: süsteemi peamised osad, nende vastutus, süsteemi piir, info liikumine ning olulised välised sõltuvused. Skeem pole kohustuslik, kui samad seosed selgitab tekst. See ei nõua tehnoloogiapinu valimist. Kõiki nõudeid ei pea selles etapis ammendavalt loetlema.

## Tööjaotus, umbes 8 tundi õppija kohta

1. Release `v0.1.0` ja tagasiside analüüs – 1 h.
2. Rolli vaatenurgast vajaduste ja konfliktide sõnastamine – 1,5 h.
3. Tööviiside võrdlemine ja otsuse põhjendamine – 1,5 h.
4. Kasutajalugude ja süsteemi kontseptsiooni koostamine – 2 h.
5. Pull request, teise töö sisuline ülevaatus ja parandused – 1 h.
6. Individuaalne refleksioon ja release – 1 h.

Vähemalt üks sinu commit peab järgima seminari head tava: see teeb ühe
loogilise muudatuse ja sõnum kirjeldab tulemust (näiteks `Describe system
boundary`), mitte ainult tegevust (`update` või `fix`).

## Nõuded otsustele

Tööviisi otsus sisaldab vähemalt kolme võrreldud varianti. Selgitage, kuidas valik sobib just teie probleemi, ebakindluse ja meeskonnaga. Kui ühendate eri meetodite võtteid, nimetage iga võtte eesmärk.

Süsteemi kontseptsiooni otsus sisaldab vähemalt kaht kaalutud lahendussuunda ning põhjendab süsteemi piiri. Ärge valige tehnoloogiapinu lihtsalt sellepärast, et see on tuttav või AI pakkus seda.

Kasutajalugu seob kasutaja, vajaduse ja väärtuse. Kontrolltingimus peab olema piisavalt konkreetne, et meeskond saaks hiljem arutada, kuidas nõude täitmist kontrollida. Ärge tuletage kasutajalugu AI vastusest või lahendusideest ilma tõendita.

## Rollide vahetamine

Iga õppija dokumenteerib vähemalt ühe tähelepaneku enda selle etapi rollist. Järgmises seminaris rollid vahetuvad. Väikeses meeskonnas võib ühel õppijal olla kaks rolli, kuid vastutused peavad olema selgelt nimetatud.

## GitHubi töövoog

Iga õppija seob enda Issue, haru, sisulise commit'i ja pull request'i. Igaüks vaatab üle vähemalt ühe teise liikme PR-i. Ülevaatus peab kommenteerima põhjendust või riski, mitte ainult õigekirja.

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
- [ ] Süsteemi eesmärk, piir, osalised, suuremad osad, nende vastutus, seosed ja sõltuvused on arusaadavad.
- [ ] Vähemalt kaks kasutajalugu lähtuvad probleemi kohta kogutud tõendist ning neil on kontrolltingimus.
- [ ] Alternatiivid, kompromissid ja teadmatused on nähtavad.
- [ ] Rollide vaatenurgad mõjutasid vähemalt üht otsust.
- [ ] Igal õppijal on Issue, commit, PR, ülevaatus ja refleksioon.
- [ ] Release `v0.2.0` on avaldatud.

## Esitamine

Lisage kodutöö Issue kommentaari release'i, enda refleksiooni, enda PR-i ja tehtud ülevaatuse lingid.
