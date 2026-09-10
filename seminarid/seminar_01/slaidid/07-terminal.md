---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 1 – terminal
---

# Kas terminal, Git ja GitHub on sama asi?

<!-- Õppejõule: kogu vastused enne mõistete eristamist. -->

---

## Need on erinevad asjad

- **Terminal** – kasutajaliides tekstikäskude sisestamiseks.
- **Käsukest (*shell*)** – programm, mis käske tõlgendab.
- **Git** – versioonihalduse programm.
- **GitHub** – veebiplatvorm Giti repositooriumidele ja koostööle.

Git on üks programmidest, mida saab terminalis käivitada.

---

## Levinud käsukestad

- **Bash** – levinud Linuxis ja Git Bashis;
- **Zsh** – macOS-i vaikimisi käsukest;
- **PowerShell** – Windowsi käsukest;
- **Git Bash** – annab Windowsis Bashile sarnase keskkonna.

Kursuse käsureanäited kasutavad Bashile sobivat kuju.

---

## Windows: vali Git Bash

1. Ava VS Code'is terminal.
2. Vajuta terminalipaneelil profiili valiku noolele.
3. Vali **Select Default Profile**.
4. Vali **Git Bash**.
5. Ava uus terminal.

Kui valik puudub, kontrolli Giti paigaldust ja taaskäivita VS Code.

---

## Esimesed ohutud käsud

```bash
pwd
ls
git --version
node --version
npm --version
```

`pwd` näitab asukohta ja `ls` aktiivse kausta sisu.

---

# Mida teeb `--version`?

<!-- Õppejõule: lase pakkuda enne vastuse näitamist. -->

---

## Kontrollime paigaldust

`--version` palub programmil näidata oma versiooni.

Kui näed versiooninumbrit, leidis terminal programmi üles.

Kui näed teadet „command not found” või sarnast viga, pole programm paigaldatud või terminal ei leia seda.

---

## Ohutus terminalis

> Ära käivita tundmatut käsku enne, kui mõistad, mida see teeb.

- Kontrolli käsku ja aktiivset kausta.
- Ära jaga terminali kuvatõmmisel salasõnu ega võtmeid.
- Veateade on info: loe see enne uue käsu proovimist läbi.
