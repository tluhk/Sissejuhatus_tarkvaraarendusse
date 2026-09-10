---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 1 – arendaja töövahendid
---

# Milliseid töövahendeid on tarkvara loomiseks vaja?

Kas ühest programmist piisab?

<!-- Õppejõule: lase nimetada töövahendeid, mida õppijad juba teavad. -->

---

## Erinevad töövahendid lahendavad erinevaid probleeme

| Töövahend | Ülesanne |
|---|---|
| VS Code | failide ja koodi muutmine |
| Terminal | programmide käivitamine tekstikäskudega |
| Git | muudatuste ajaloo haldamine |
| GitHub | repositooriumid ja koostöö veebis |
| GitHub CLI (`gh`) | GitHubi kasutamine terminalist |
| Markdown | dokumentatsiooni kirjutamine |
| Disainitööriistad (nt Figma) | kasutajaliidese ja kasutajakogemuse kavandamine |
| Projektihalduse tööriistad (nt GitHub Projects, Jira, ClickUp) | tööde ja edenemise korraldamine |
| Node.js | JavaScripti käivitamine väljaspool brauserit |
| Docker | korratava käituskeskkonna loomine |

---

## Töövahendid moodustavad arenduskeskkonna

```text
VS Code
├── projekti failid
├── Giti tööriistad
├── laiendused
└── terminal
    ├── Git
    ├── GitHub CLI
    ├── Node.js ja npm
    └── Docker
```

Töövahend sõltub rollist ja projekti etapist. Selles aines tegeleme piiratult
koodi loomise ning seda toetava Giti/GitHubi töövoo tarkvaraga. Disaini- ja
projektihalduse vahendeid nimetame, kuid siin eraldi ei õpeta.

---

## Alustame allalaadimist

Vajame täna:

1. [Giti](https://git-scm.com/downloads)
2. [Visual Studio Code'i](https://code.visualstudio.com/)
3. [Node.js-i](https://nodejs.org/)
4. ligipääsu GitHubi kontole

[GitHub CLI](https://cli.github.com/) on kasulik valikuline lisatööriist. Dockerit tutvustame, kuid selle paigaldamine pole täna kohustuslik.

<!-- Õppejõule: lase allalaadimistel pausi ajal jätkuda. -->

---

# Git tuleb arvutisse paigaldada

VS Code sisaldab Giti kasutajaliidest, kuid kasutab arvutisse paigaldatud Giti.

```bash
git --version
```

Kui näed versiooninumbrit, on Git olemas.

[Giti ametlik paigaldusjuhend](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## Git Windowsis

Laadi paigaldaja: [git-scm.com/install/windows](https://git-scm.com/install/windows)

Paigaldaja lisab Git Bashi ja Git Credential Manageri. Algaja võib üldjuhul jätta vaikevalikud.

```powershell
winget install --id Git.Git -e --source winget
```

Pärast paigaldamist sulge ja ava VS Code uuesti.

---

## Git macOS-is: Homebrew

[Homebrew](https://brew.sh/) on paketihaldur programmide paigaldamiseks ja uuendamiseks. Kursusel soovitame seda Maci arendustööriistade haldamiseks.

```bash
brew install git
git --version
```

Esmalt paigalda Homebrew ametliku juhendi järgi ja täida **Next steps**. Töötavat Giti ei pea ümber paigaldama.

[Giti ametlik macOS-i juhend](https://git-scm.com/install/mac)

---

## Giti muud paigaldusvõimalused

macOS-is sobib ka Apple'i Xcode Command Line Toolsi Git:

```bash
xcode-select --install
```

Ubuntu või Debian:

```bash
sudo apt update
sudo apt install git
```

[Giti juhend Linuxile](https://git-scm.com/install/linux)

---

## Levinud paigaldusprobleemid

**`git: command not found` või Git puudub VS Code'is**

- taaskäivita terminal ja VS Code
- proovi uuesti `git --version`
- Windowsis kontrolli Git for Windowsi paigaldust

**Esimene commit küsib nime ja e-posti**

```bash
git config --global user.name "Sinu nimi"
git config --global user.email "sinu@email.ee"
```

E-post võib muutuda commit'i avalikuks osaks. GitHub võimaldab kasutada privaatset `noreply` aadressi.

---

## Giti veaotsing VS Code'is

Ava käsupaletist:

```text
Git: Show Git Output
```

Vaata esimest veateadet. Eemalda enne logi jagamist kasutajanimed, privaatsed failiteed ja repositooriumide aadressid.

Kui paigaldusõigused puuduvad, küsi abi õppejõult või IT-toelt.

---

# Paus

## Jätka vajaduse korral programmide allalaadimist

Pärast pausi seadistame töövahendid koos.
