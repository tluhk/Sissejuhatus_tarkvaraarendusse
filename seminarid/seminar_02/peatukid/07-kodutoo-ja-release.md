# Kodutöö ja release v0.1.0

Tiim valib tunniplaani kasutajaprobleemi, kontrollib seda sõltumatu infoga ning koostab arendustiimile põhjendatud lähteülesande. Töö maht on umbes 8 tundi õppija kohta.

## Sisukord


- [Kodutöö: probleemist lähteülesandeni](#kodutöö-probleemist-lähteülesandeni)
- [Release v0.1.0](#release-v010)
- [Valmis töö ja esitamine](#valmis-töö-ja-esitamine)

---

## Kodutöö: probleemist lähteülesandeni

Tarkvaraarenduse eesmärk on lahendada kasutaja probleem.

**Meie kursuse läbiv ülesanne on:** Haapsalu kolledž tellib oma tunniplaanirakenduse kaasajastamise.

### Kodutöö eesmärk

Tiim leiab ja valib tunniplaani kasutajaprobleemi, kontrollib seda sõltumatu infoga ning koostab arendustiimile põhjendatud lähteülesande. Töö maht on umbes 8 tundi õppija kohta, sealhulgas Giti koostöö ja refleksioon.

### Projekti seadistus

Kasutage õppejõu määratud ühist tiimirepositooriumi organisatsioonis `TLUHK-RIF26` ja sellega seotud GitHub Projectsi tahvlit. Ärge looge uut repositooriumi. Iga õppija loob oma ülesande jaoks Issue'i ja haru.

Kõik muudatused käivad [tiimi töövoo](06-tiimi-toovoog.md) järgi: ülesandel on Issue ja vastutaja, töö tehakse eraldi harus ning kaaslane vaatab PR-i üle. Iga õppija teeb vähemalt ühe sisulise commit'i (kuid kui suudate oma töö jaotada mitmeks, on parem), avab PR-i, vaatab üle kaaslase PR-i ja vastab enda töö tagasisidele.

### 1. Iga õppija koostab probleemikandidaadid (umbes 2 tundi)


Loo [enda kolm probleemikandidaati](05-probleemikandidaadid.md) ja enesehindamine. Lõpeta PR ning kaaslase ülevaatus. Tiim alustab võrdlemist siis, kui kõigi individuaalsed tööd on üle vaadatud ja ühendatud.

### 2. Võrrelge kandidaate (umbes 1 tund)

Looge võrdluseks eraldi Issue ja määrake tulemuse koondaja. Valige enesehindamise küsimuste abil üks probleem edasiseks uurimiseks. Valik on esialgne: järgmine samm võib seda muuta.

Alustage [otsuse malli](../../mallid/otsus.md) põhjal faili `decisions/001-probleemi-valik.md`. Kirjutage sinna valik, selle põhjus ja vähemalt üks kõrvale jäetud alternatiiv. Märkige ka osalenud rollid.

### 3. Kontrollige valikut (umbes 2 tundi)

Valideerimine tähendab oletuse kontrollimist sõltumatu info abil. Iga õppija panustab vähemalt ühte kontrollivasse tegevusse; jagage tegevused Issue'deks. Sobib vestlus kasutajaga, praeguse tööprotsessi vaatlus või usaldusväärse andmeallika analüüs. Tiimil peab olema vähemalt üks dokumenteeritud sõltumatu kontroll ja ühine järeldus selle kohta, mida see muutis. AI väljund üksi kontrolliks ei sobi.

Koondage otsuse faili, mida uurisite, kust info tuli, mida leidsite ning mis jäi ebakindlaks. Ärge avaldage osaleja nime ega tundlikku infot. Kui tõend valikut ei toeta, muutke probleemi sõnastust või valikut ja põhjendage seda.

Kasutage AI-d vähemalt ühe olulise otsuse juures [uurimise peatüki juhise järgi](03-probleemi-uurimine.md). Dokumenteerige otsuse malli AI osas ka väljundi kontroll ja kasu.

### 4. Koostage lähteülesanne (umbes 1 tund)

Määrake ühise otsuse täiendamiseks Issue ja koondamise eest vastutaja. Kinnitage tulemus tiimiga. Samas otsuse failis peab olema arendustiimile selge alguspunkt:

- peamine kasutaja, olukord, takistus ja mõju;
- kogutud tõendid ning valiku põhjendus koos alternatiivide ja kompromissidega;
- soovitud tulemus ja esialgne ulatus;
- piirangud, lahtised küsimused ja järgmised kontrollid.

Ärge valige põhjenduseta ette kujundust ega funktsioone. Nõuete ja kasutajalugude täpsustamine jätkub seminaris 3.

### 5. Refleksioonid ja avaldamine (umbes 2 tundi koos koostöövooga)


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

---

## Release v0.1.0

### Kuidas release luua?

**Tag** tähistab üht kindlat commit'i. **GitHub Release** lisab sellele versioonile avaldatud kirjelduse. Nii saab hiljem vaadata, milline oli dokumentatsioon just selle etapi lõpus.

Kursusel tähistame projektietappe versioonidega: seminar 2 `v0.1.0`, seminar 3 `v0.2.0`, seminar 4 `v0.3.0`, seminar 5 `v0.4.0` ja eksam `v1.0.0`. Kõigil tiimiliikmetel on ühine etapi versioon. See on kursuse kokkulepe; üksik PR ei vaja uut tag'i.

Release manager:

1. Kontrollib, et etapi PR-id on üle vaadatud ja ühendatud ning `main` sisaldab otsust, refleksioone ja release'i kirjeldust.
2. Avab repo **Releases** vaate ja vajutab **Draft a new release**.
3. Sisestab väljale **Choose a tag** `v0.1.0`, valib **Create new tag: v0.1.0 on publish** ja jätab sihiks `main`-haru.
4. Paneb pealkirjaks `Probleem sõnastatud`, lisab lühikese kokkuvõtte ja lingi failile `releases/v0.1.0.md`.
5. Vajutab **Publish release**. Mustandi salvestamine release'i ei avalda.
6. Avab avaldatud release'i ning kontrollib tag'i ja failide olemasolu.

Näide: [demorepo release notes `v0.1.0`](https://github.com/TLUHK-RIF26/tiim-demo-tunniplaan/blob/v0.1.0/releases/v0.1.0.md).

Avaldatud tag'i ei tõsteta järgmise töö juurde: see peab säilitama etapi ajaloo. Edasine töö käib uutes harudes ning järgmine etapp saab uue versiooni. Pärast `v0.1.0` uuendab igaüks kohalikku `main`-i; seminaris 3 algab uus Issue nõuete, tööviisi või süsteemi kontseptsiooni täpsustamiseks. Release manageri vastutus vahetub.

---

## Valmis töö ja esitamine

Töö on valmis, kui teine inimene saab otsusest aru, milline probleem valiti, mis seda toetab ja mida veel ei teata; iga liikme PR, ülevaatus ning refleksioon on leitavad ja `v0.1.0` on avaldatud. Lahtised küsimused võivad alles jääda, kui nende järgmine uurimissamm on kirjas.

Iga õppija lisab õppejõu antud kodutöö Issue kommentaari lingi release'ile, ühisele otsusele ja enda refleksioonile ning enda PR-i ja tehtud ülevaatuse numbrid. See on esitamise koht; tiimi töö-Issue'd jäävad projekti töö jälgimiseks.
