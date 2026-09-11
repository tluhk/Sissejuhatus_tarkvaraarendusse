---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 1 – Git ja GitHub
---

# Mis vahe on Gitil ja GitHubil?

<!-- Arutelu: sõnastage esmalt paarides ühe lausega vastus. -->

---

## Git

Git on versioonihaldussüsteem.

Git aitab:

- näha failides tehtud muudatusi;
- salvestada seotud muudatused commit'ina;
- vaadata muudatuste ajalugu;
- töötada eri harudes;
- ühendada mitme inimese töö.

---

## GitHub

GitHub on veebiplatvorm, mis aitab Giti repositooriume hoida ja teistega koostööd teha.

GitHub lisab:

- kontod ja organisatsioonid;
- ligipääsuõigused;
- pull request'id ja ülevaatused;
- Issues ja Projects;
- automatiseerimise võimalused.

---

## Git ei ole GitHub

Git saab töötada sinu arvutis ilma GitHubita.

GitHub kasutab Giti, kuid lisab sellele veebipõhise hoiustamise ja koostöövahendid.

```text
Git = muudatuste ajalugu
GitHub = repositooriumid ja koostöö veebis
```

---

# Kus asuvad sinu projekti failid?

- Ainult GitHubis?
- Ainult sinu arvutis?
- Mõlemas kohas?

<!-- Arutelu: arutlege, mis võib kahes asukohas erineda. -->

---

## Kohalik ja kaug-repositoorium

```text
Sinu arvuti                         GitHub
┌────────────────┐   push        ┌────────────────┐
│ kohalik repo   │ ────────────► │ kaug-repo      │
│ muuda, commit  │ ◄──────────── │ teiste töö     │
└────────────────┘   pull        └────────────────┘
```

Muudatus ei ilmu GitHubi enne push'i.

---

## Põhimõisted

- **Repository** – projekti failid koos muudatuste ajalooga
- **Clone** – kaug-repositooriumi koopia loomine arvutisse
- **Fork** – teise GitHubi repositooriumi koopia loomine enda konto või organisatsiooni alla
- **Commit** – tähenduslik salvestatud muudatuste komplekt
- **Push** – kohalike commit'ide saatmine kaug-repositooriumi
- **Pull** – kaugmuudatuste toomine kohalikku repositooriumi

---

## Clone ja fork

**Clone** kopeerib repositooriumi GitHubist sinu arvutisse.

```text
GitHubi repo → sinu arvuti
```

**Fork** loob teise repositooriumi põhjal uue repositooriumi sinu GitHubi konto või organisatsiooni alla.

```text
Teise omaniku GitHubi repo → sinu GitHubi fork
```

---

## Forki kasutatakse koostööks

Fork on kasulik, kui sul pole algses repositooriumis kirjutamisõigust.

Tüüpiline töövoog:

1. loo GitHubis fork;
2. klooni enda fork arvutisse;
3. tee muudatus ja push enda forki;
4. paku muudatust algsele repositooriumile pull request'iga.

Kursuse meeskonnaprojektis kloonime ühise repo ja töötame selle harudes. Forki puhul piisab erinevuse mõistmisest.

---

## HTTPS ja SSH

GitHub pakub repositooriumi kloonimiseks kahte levinud ühendusviisi:

```text
HTTPS  https://github.com/omanik/repo.git
SSH    git@github.com:omanik/repo.git
```

**SSH** tähendab *Secure Shell Protocol*. SSH kasutab kasutaja tuvastamiseks tavaliselt avaliku ja privaatse võtme paari.

---

## Esimeses seminaris kasutame HTTPS-i

SSH kasutamiseks tuleb:

- luua võtmepaar
- kaitsta privaatset võtit
- lisada avalik võti GitHubi kontole
- vajaduse korral seadistada SSH agent

Me SSH-võtmeid täna ei seadista. Vali kloonimisel **HTTPS**.

[GitHubi SSH juhend](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)

---

## VS Code Source Control

VS Code'is saame graafiliselt:

- näha muudetud faile;
- võrrelda faili eelmist ja uut versiooni;
- valida commit'i kuuluvad muudatused;
- kirjutada commit'i sõnumi;
- teha pull'i ja push'i.

---

## GitHub Desktop

GitHub Desktop on eraldi graafiline Giti rakendus Windowsile ja macOS-ile.

See on lubatud alternatiiv, kuid kursuse põhiline graafiline töövoog toimub VS Code'is, kus projektifailid, Git ja terminal on ühes kohas.

---

## GitHub CLI

**GitHub CLI** ehk `gh` võimaldab GitHubi kasutada terminalist.

- `git` haldab versiooniajalugu;
- `gh` suhtleb GitHubi teenusega.

`gh` abil saab vaadata repositooriumi infot ja Issue'sid ning avada vastava vaate brauseris.

---

## GitHub CLI kontroll

```bash
gh --version
gh auth status
```

Kui `gh` puudub, saab selle paigaldada aadressilt [cli.github.com](https://cli.github.com/).

Sisselogimiseks:

```bash
gh auth login
```

Ära jaga autentimisvõtmeid ega muid sisselogimisandmeid.

---

## Repositooriumi ja Issue'de vaatamine

Käivita kloonitud repositooriumi kaustas:

```bash
gh repo view
gh issue list
gh issue view 2
```

Asenda `2` soovitud Issue numbriga. Need käsud ainult kuvavad infot.

---

## Kasulikud `gh` nipid

```bash
gh repo view --web
gh issue view 2 --web
gh issue list --state all
gh issue list --assignee @me
gh issue list --limit 50
```

- `--web` avab vaate brauseris
- `--state all` näitab ka suletud Issue'sid
- `@me` tähendab sisselogitud kasutajat
- `--limit` muudab tulemuste arvu

---

## Kui sa ei ole repo kaustas

```bash
gh issue list --repo ORGANISATSIOON/SJTA
gh issue list --help
```

- `--repo` määrab sihtrepositooriumi
- `--help` kuvab käsu abi

Enne muutva käsu käivitamist kontrolli sihtrepositooriumi.
