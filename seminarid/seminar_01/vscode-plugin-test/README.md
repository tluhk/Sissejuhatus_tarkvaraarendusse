# VS Code extensionite test

Projekt on mõeldud nende extensionite proovimiseks:

- Prettier (`esbenp.prettier-vscode`) – vormindus
- Oxlint / Oxc (`oxc.oxc-vscode`) – linter
- Error Lens (`usernamehw.errorlens`) – hoiatused otse koodirea juures
- Live Server (`ritwickdey.LiveServer`) – lokaalne server ja automaatne uuestilaadimine
- Live Share (`ms-vsliveshare.vsliveshare`) – koodi jagamine ja ühine redigeerimine reaalajas
- Code Spell Checker (`streetsidesoftware.code-spell-checker`) – õigekirjakontroll
- Code Spell Checker Estonian (`streetsidesoftware.code-spell-checker-estonian`) – eesti keele sõnastik
- Nu-Minify (`emapco.nu-minify`) – CSS/JS/HTML minifitseerimine, Prettieri vastand
- EditorConfig (`editorconfig.editorconfig`) – taande ja reavahetuste ühtlustamine
- HTML CSS Support (`ecmel.vscode-html-css`) – CSS-klasside automaatlõpetus HTML-is
- Auto Rename Tag (`formulahendry.auto-rename-tag`) – avava ja sulgeva tagi sünkroonne muutmine
- GitLens (`eamodio.gitlens`) – git-ajalugu rea kaupa

ESLinti ei ole tahtlikult lisatud, sest see dubleeriks Oxlinti hoiatusi.

## 0. Laienduste paigaldus

Kausta avamisel pakub VS Code soovitatud laiendusi ise (`.vscode/extensions.json`).
Kui teadet ei tule, ava Extensions paneel ja otsi `@recommended`.

`.vscode/settings.json` seab Prettieri vaikevormindajaks ja lisab Code Spell Checkerile eesti keele.
`formatOnSave` on tahtlikult väljas, et **Format Document** demo enne–pärast oleks näha.

## 1. Live Server

Ava `index.html` ja käivita **Open with Live Server**.

## 2. Prettier

Ava `index.html`, `styles.css` või `script.js` ja vali **Format Document**.
Failides on tahtlikult ebaühtlane vormindus.

## 3. Oxlint

Terminalis:

```bash
npm install
npm run lint
```

`script.js` sisaldab tahtlikult näiteks kasutamata muutujat ja `var` kasutust.

## 4. Error Lens

Kui Oxlinti VS Code extension on aktiivne, peaks Error Lens näitama lintimise hoiatusi otse koodirea juures.

## 5. Code Spell Checker

`script.js` sisaldab tahtlikku kirjaviga:

```js
"Greetting shown"
```

Spell checker peaks sõna `Greetting` ära märkima.

## Märkus

Kõik vead pole süntaksivead. Osa neist on teadlikult stiili-, kvaliteedi- või õigekirjaprobleemid, et extensionite erinevust näha.
