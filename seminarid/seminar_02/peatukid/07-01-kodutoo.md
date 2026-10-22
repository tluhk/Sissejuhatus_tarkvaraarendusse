# Kodutöö: probleemist lähteülesandeni

**Eesmärk:** tiim valib tunniplaani kasutajaprobleemi, kontrollib seda sõltumatu infoga ning koostab arendustiimile põhjendatud lähteülesande. Arvestuslik maht on umbes 8 tundi õppija kohta, sealhulgas Giti koostöö ja refleksioon. Jätkake seminaris pooleli jäänud sammust.

Kõik muudatused käivad [tiimi töövoo](06-tiimi-toovoog.md) järgi: ülesandel on Issue ja vastutaja, töö tehakse eraldi harus ning kaaslane vaatab PR-i üle. Iga õppija teeb vähemalt ühe sisulise commit'i, avab PR-i, vaatab üle kaaslase PR-i ja vastab enda töö tagasisidele.

## 1. Lõpeta enda kaardistus, umbes 2 tundi

Täpsusta [enda kolm probleemikandidaati](05-probleemikandidaadid.md) ja enesehindamine. Lõpeta PR ning kaaslase ülevaatus. Tiim alustab võrdlemist siis, kui kõigi individuaalsed tööd on üle vaadatud ja ühendatud.

## 2. Võrrelge kandidaate, umbes 1 tund

Looge võrdluseks eraldi Issue ja määrake tulemuse koondaja. Valige enesehindamise küsimuste abil üks probleem edasiseks uurimiseks. Valik on esialgne: järgmine samm võib seda muuta.

Alustage [otsuse malli](../../mallid/otsus.md) põhjal faili `decisions/001-probleemi-valik.md`. Kirjutage sinna valik, selle põhjus ja vähemalt üks kõrvale jäetud alternatiiv. Märkige ka osalenud rollid.

## 3. Kontrollige valikut, umbes 2 tundi

Valideerimine tähendab oletuse kontrollimist sõltumatu info abil. Iga õppija panustab vähemalt ühte kontrollivasse tegevusse; jagage tegevused Issue'deks. Sobib vestlus kasutajaga, praeguse tööprotsessi vaatlus või usaldusväärse andmeallika analüüs. Tiimil peab olema vähemalt üks dokumenteeritud sõltumatu kontroll ja ühine järeldus selle kohta, mida see muutis. AI väljund üksi kontrolliks ei sobi.

Koondage otsuse faili, mida uurisite, kust info tuli, mida leidsite ning mis jäi ebakindlaks. Ärge avaldage osaleja nime ega tundlikku infot. Kui tõend valikut ei toeta, muutke probleemi sõnastust või valikut ja põhjendage seda.

Kasutage AI-d vähemalt ühe olulise otsuse juures [uurimise peatüki juhise järgi](03-probleemi-uurimine.md). Dokumenteerige otsuse malli AI osas ka väljundi kontroll ja kasu.

## 4. Koostage lähteülesanne, umbes 1 tund

Määrake ühise otsuse täiendamiseks Issue ja koondamise eest vastutaja. Kinnitage tulemus tiimiga. Samas otsuse failis peab olema arendustiimile selge alguspunkt:

- peamine kasutaja, olukord, takistus ja mõju;
- kogutud tõendid ning valiku põhjendus koos alternatiivide ja kompromissidega;
- soovitud tulemus ja esialgne ulatus;
- piirangud, lahtised küsimused ja järgmised kontrollid.

Ärge valige põhjenduseta ette kujundust ega funktsioone. Nõuete ja kasutajalugude täpsustamine jätkub seminaris 3.

## 5. Refleksioonid ja avaldamine, umbes 2 tundi koos koostöövooga

Iga õppija lisab [refleksiooni malli](../../mallid/individuaalne-refleksioon.md) põhjal oma faili. Tiim täiendab repo `README.md`-d projekti eesmärgi, liikmete ja sisuliste failide linkidega. Võrrelge Issue'de ajahinnanguid tegeliku ajakuluga ning märkige üks järgmise etapi planeerimise parandus.

Release manager koondab [release notes'i malli](../../mallid/release-notes.md) abil faili `releases/v0.1.0.md`: hetkeseis, olulisemad otsused, muutunud arusaam, kontrollitud info, lahtised küsimused ja iga liikme panus. Ka release'i kirjeldus ja refleksioonid peavad enne avaldamist olema PR-ide kaudu `main`-i ühendatud.

Tiimi repos on etapi lõpuks:

```text
README.md
research/eesnimi-perenimi-probleemikandidaadid.md  (igal õppijal oma fail)
decisions/001-probleemi-valik.md
reflections/oppija-nimi-v0.1.0.md                 (igal õppijal oma fail)
releases/v0.1.0.md
```
