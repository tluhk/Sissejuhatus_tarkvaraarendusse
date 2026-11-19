# Arenduskeskkond

**Märge:** Seminaris

**Arenduskeskkond** on tööriistade, programmide ja seadistuste kogum, millega tarkvara arendatakse ja kontrollitakse. Sellel lehel tutvume kahe tööriistaga, mida kohtad peaaegu igas veebiprojektis: Node.js ja Docker. Siin on oluline mõista, milleks neid kasutatakse. Paigaldamist kursusel ei nõuta.

## Node.js ja npm

JavaScript loodi brauseris töötamiseks. **Node.js** võimaldab JavaScripti käivitada ka väljaspool brauserit: terminalis ja serveris.

Koos Node.js-iga tuleb **npm** (*Node Package Manager*). Selle abil:

- lisatakse projekti teiste loodud koodipakette ehk **sõltuvusi**;
- käivitatakse projekti käske, näiteks `npm run build`;
- kirjeldatakse projekti seadistust failis `package.json`.

Kui kloonid veebiprojekti ja näed failis `package.json`, vajab see projekt tõenäoliselt Node.js-i.

## Docker

Rakendus võib töötada ühe arendaja arvutis, kuid mitte teise omas, sest programmide versioonid või seadistused erinevad.

**Docker** pakendab rakenduse koos kõige vajalikuga **konteinerisse**. Konteiner töötab igas arvutis ühtemoodi. Nii saavad arendaja, testija ja server kasutada täpselt sama keskkonda.

Docker ei asenda Giti, VS Code'i ega Node.js-i. See lahendab teist probleemi: kuidas keskkond korratavaks teha.

## Kuidas tööriistad kokku sobivad

```text
VS Code
├── projekti failid
├── Giti tööriistad
├── laiendused
└── terminal
    ├── Git
    ├── GitHub CLI (gh)
    ├── Node.js ja npm
    └── Docker
```

VS Code on koht, kus töötad. Terminalist käivitad programme. Iga programm täidab oma ülesannet.

## Kursuse arenduskeskkond

Kursusel piisab sellest:

- VS Code koos integreeritud terminaliga;
- Git (Windowsis koos Git Bashiga);
- GitHubi konto;
- arvutis eraldi kaust kursuse projektide jaoks.

Node.js, npm, Docker ja GitHub CLI on valikulised. Need muutuvad vajalikuks järgmistes erialaainetes. Kui need on sul juba olemas, kontrolli versioone:

```bash
node --version
npm --version
docker --version
```

## Kontrolli ennast

1. Mis probleemi lahendab Node.js ja mis probleemi Docker?
2. Mille järgi tunned ära, et projekt vajab Node.js-i?
3. Millised tööriistad on sinu arvutis olemas? Kontrolli seda terminalis.

---

[← Markdown](05-markdown.md) | [Sisukord](../README.md) | [Järgmine: Giti oskus: esimene commit →](07-git-first-commit.md)
