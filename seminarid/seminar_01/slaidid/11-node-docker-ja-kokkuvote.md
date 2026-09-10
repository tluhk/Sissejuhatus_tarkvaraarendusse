---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 1 – arenduskeskkond
---

# Miks ei piisa ainult VS Code'i paigaldamisest?

Kas koodiredaktor oskab ise kõiki programme käivitada?

<!-- Õppejõule: seo küsimus varem selgitatud töövahendite rollidega. -->

---

## Koodiredaktor ei ole käituskeskkond

VS Code aitab faile muuta ja töövahendeid ühendada.

Koodi käivitamiseks võib projekt vajada eraldi:

- brauserit;
- programmeerimiskeele käituskeskkonda;
- kompilaatorit;
- andmebaasi;
- serverit või konteinerit.

---

## Node.js

Node.js võimaldab JavaScripti käivitada väljaspool veebibrauserit.

Seda kasutatakse muu hulgas:

- arendustööriistade käivitamiseks;
- veebiserverite loomiseks;
- projektide ehitamiseks ja testimiseks;
- automatiseerimiseks.

---

## npm

**npm** – Node Package Manager

npm aitab:

- lisada projekti teiste loodud pakette;
- hallata sõltuvusi;
- käivitada projektikäske;
- kasutada projekti kirjeldust failis `package.json`.

---

# Miks töötab projekt ühes arvutis, aga teises mitte?

<!-- Õppejõule: lase nimetada erinevaid versioone, seadistusi ja puuduvaid teenuseid. -->

---

## Arenduskeskkonnad võivad erineda

- operatsioonisüsteem;
- programmide versioonid;
- paigaldatud sõltuvused;
- keskkonnamuutujad;
- võrgu- ja ligipääsuseaded;
- vajalikud taustateenused.

„Minu arvutis töötab” ei tõesta, et lahendus töötab mujal.

---

## Docker

Docker aitab pakendada rakenduse ja selle käituskeskkonna **konteinerisse**.

See aitab muuta keskkonna:

- korratavaks;
- jagatavaks;
- erinevates arvutites sarnasemaks;
- lihtsamini käivitatavaks.

Dockerit me täna paigaldama ei pea.

---

## Meie algne arenduskeskkond

```text
VS Code
├── projekti failid ja Markdown
├── Source Control → Git
├── GitHub → kaug-repositoorium ja koostöö
└── terminal
    └── Node.js ja npm
```

Docker lisandub siis, kui projekt vajab korratavat konteinerkeskkonda.

---

## Seminari lõpu kontroll

- [ ] GitHubi konto avaneb.
- [ ] VS Code ja terminal töötavad.
- [ ] Windowsis on valitud Git Bash.
- [ ] Git, Node.js ja npm näitavad versiooni.
- [ ] Repo on arvutisse kloonitud.
- [ ] README muudatus on commit'itud ja GitHubi push'itud.

---

# Mida tähendab nüüd „tarkvaraarendus”?

Vaata tagasi seminari alguses antud vastusele.

Mida sa sellele nüüd lisaksid või muudaksid?

<!-- Õppejõule: lõpeta seminar uue ühise definitsiooniga. -->

---

# Kodutöö 1

## Minu arenduskeskkond

Täienda oma olemasolevat `SJTA` repositooriumi.

Uut repositooriumi ega organisatsiooni pole vaja luua.

---

## Loo üks Markdown-fail

```text
SJTA/
└── seminar-01/
    └── arenduskeskkond.md
```

Kirjelda selles oma arvutit, töövahendeid ja õpitut.

---

## Mida fail peab sisaldama?

- operatsioonisüsteem, redaktor ja terminal;
- `git`, `node` ja `npm` versioonid;
- töövahendite rollide tabel;
- 3–5-lauseline refleksioon;
- selgitus, miks tarkvaraarendus pole ainult koodimine.

Dockerit ei pea paigaldama.

---

## Salvesta ja esita

1. Vaata muudatus **Source Controlis** üle.
2. Tee commit `Lisa esimese seminari kodutöö`.
3. Tee push.
4. Kontrolli faili GitHubis.
5. Lisa ülesande issue kommentaari link valmis failile.

Täielik juhend: `seminarid/seminar_01/homework.md`
