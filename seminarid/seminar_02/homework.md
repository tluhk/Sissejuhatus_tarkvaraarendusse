# Kodutöö 2: probleem ja release `v0.1.0`

## Ülesanne lühidalt

Kontrollige meeskonna valitud probleemi vähemalt ühe sõltumatu tõendiga, täpsustage probleemiväidet ja avaldage GitHub Release `v0.1.0 – Probleem sõnastatud`. Iga õppija teeb nähtava GitHubi panuse ja kirjutab individuaalse refleksiooni.

## Maht

Arvestuslik maht on ligikaudu 8 tundi õppija kohta. Võimekam õppija võib jõuda nõutud tulemuseni kiiremini. Teksti ei ole vaja kunstlikult pikendada.

## Meeskonna tulemus

Repositooriumis peavad olema vähemalt:

```text
decisions/001-probleemi-valik.md
releases/v0.1.0.md
reflections/oppija-nimi-v0.1.0.md
README.md
```

Kasutage [otsuse](../mallid/otsus.md), [release notes'i](../mallid/release-notes.md) ja [refleksiooni](../mallid/individuaalne-refleksioon.md) malli.

## Sammud

### 1. Individuaalne probleemide vaatlus, umbes 2 tundi

- Kirjelda vähemalt kolme märgatud probleemi.
- Lisa iga probleemi juurde inimene, olukord, takistus ja mõju.
- Märgi, milline osa on vaatlus ja milline oletus.

### 2. Meeskonna valik, umbes 1 tund

- Võrrelge kandidaate seminaris kasutatud küsimustega.
- Valige üks läbiv probleem.
- Dokumenteerige ka vähemalt üks kõrvale jäetud variant ja selle põhjus.

### 3. Kerge valideerimine, umbes 2 tundi

Iga õppija panustab vähemalt ühte kontrollivasse tegevusse. Sobib näiteks lühike vestlus, olemasoleva tööprotsessi vaatlus või usaldusväärse andmeallika analüüs.

Dokumenteerige:

- mida tahtsite teada;
- kellelt või millisest allikast info tuli;
- mida teada saite;
- mis jäi ebakindlaks;
- kuidas info probleemiväidet muutis.

Ärge avaldage osaleja nime ega tundlikku infot. Vajaduse korral kirjeldage allikat üldistatult.

### 4. Otsuse täiendamine, umbes 1 tund

Täiendage faili `decisions/001-probleemi-valik.md`. Otsus peab näitama valikut, alternatiive, tõendit ja kompromisse.

### 5. GitHubi koostöövoog, umbes 1 tund

Iga õppija:

1. töötab enda harus;
2. teeb vähemalt ühe sisulise commit'i;
3. avab pull request'i;
4. seob pull request'i enda Issue'ga;
5. vaatab sisuliselt üle vähemalt ühe teise õppija pull request'i;
6. vastab enda töö tagasisidele.

Kasutage [pull request'i kontrollnimekirja](../mallid/pull-request.md).

Järgige [seminari terminalitöövoogu](seminar.md#esimene-meeskonnatöövoog-vs-codeis). Pärast kaaslase PR-i ühendamist harjutab iga õppija ka uuendatud peaharu toomist oma arvutisse [pull-juhise järgi](seminar.md#kaaslase-muudatuste-toomine-pull).

### 6. Refleksioon ja release, umbes 1 tund

Iga õppija lisab faili `reflections/oppija-nimi-v0.1.0.md`.

Vahetuv release manager:

1. kontrollib, et vajalikud pull request'id on üle vaadatud ja ühendatud;
2. lõpetab koos meeskonnaga faili `releases/v0.1.0.md`;
3. loob tag'i `v0.1.0`;
4. avaldab GitHub Release'i pealkirjaga `Probleem sõnastatud`;
5. lisab release'i kirjeldusse lingi `releases/v0.1.0.md` failile.

Kasuta seminaris näidatud [esimese release'i juhist](seminar.md#esimene-release).

## AI kasutamine

AI kasutamine on lubatud, kuid selle väljund ei ole probleemi olemasolu tõend. Kui AI mõjutas probleemivalikut või sõnastust, täitke otsuse malli AI osa ning selgitage, kuidas kontrollisite väiteid sõltumatu allikaga.

## Valmis töö kontroll

- [ ] Probleem kirjeldab inimest, olukorda, takistust ja mõju.
- [ ] Probleem ei ole sõnastatud puuduva rakendusena.
- [ ] Vähemalt üks sõltumatu kontroll on dokumenteeritud.
- [ ] Otsuste logis on valik, alternatiiv ja põhjendus.
- [ ] Lahtised küsimused on nähtavad.
- [ ] Igal õppijal on commit, pull request, ülevaatus ja refleksioon.
- [ ] Release notes kirjeldab hetkeseisu ja järgmist sammu.
- [ ] GitHub Release `v0.1.0` on avaldatud.

## Esitamine

Lisage kodutöö Issue kommentaari:

- link GitHub Release'ile;
- link meeskonna otsusele;
- link enda refleksioonile;
- enda pull request'i ja tehtud ülevaatuse numbrid.
