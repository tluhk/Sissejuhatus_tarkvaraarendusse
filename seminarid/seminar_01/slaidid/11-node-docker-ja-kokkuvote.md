---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 1 – arenduskeskkond
---

# Miks ei piisa ainult VS Code'i paigaldamisest?

Kas koodiredaktor oskab ise kõiki programme käivitada?

<!-- Arutelu: seostage küsimus varem selgitatud töövahendite rollidega. -->

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

<!-- Arutelu: nimetage erinevaid versioone, seadistusi ja puuduvaid teenuseid. -->

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
    └── Git ja kaustades liikumine
```

Node.js, npm ja Docker lisanduvad vajaduse tekkimisel. Praegu on nende paigaldamine valikuline.

---

## Seminari lõpu kontroll

- [ ] GitHubi konto avaneb.
- [ ] VS Code ja terminal töötavad.
- [ ] Windowsis on valitud Git Bash.
- [ ] Git näitab versiooni ja oskan kontrollida töökataloogi.
- [ ] Repo on arvutisse kloonitud.
- [ ] README muudatus on commit'itud ja GitHubi push'itud.

---

# Mida tähendab nüüd „tarkvaraarendus”?

Vaata tagasi seminari alguses antud vastusele.

Mida sa sellele nüüd lisaksid või muudaksid?

<!-- Kokkuvõte: sõnastage seminari lõpus ühine definitsioon. -->

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
- Giti versioon;
- töövahendite rollide tabel;
- seitsme käsu terminalispikker;
- 5–8-lauseline refleksioon, sh salvestamise, commit'i ja push'i erinevus;
- selgitus, miks tarkvaraarendus pole ainult koodimine.

Node.js-i, npm-i, Dockerit ja GitHub CLI-d ei pea paigaldama.

---

## Loo Issue'st haru ja esita

1. Ava kodutöö Issue, vajuta **Development → Create a branch** ja käivita näidatud `git fetch` ja `git checkout` käsud.
2. Salvesta fail, vali see `git add` abil ning vaata üle `git diff --cached`.
3. Tee commit `Add development environment notes` ja `git push -u origin <haru>`.
4. Ava pull request, lisa `Closes #N` ja määra ülevaatajaks paariline.
5. Vaata üle paarilise pull request ja lisa pärast heakskiitu ülevaatajaks õppejõud.

Paarid: `student_pairs.md`. Täielik juhend: `seminarid/seminar_01/homework.md`

Takistuse korral lisa Issue kommentaari samm, veateade ja juba proovitud lahendused.
