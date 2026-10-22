# Commit'i sõnumid ja head tavad

Commit salvestab valitud muudatuste komplekti Giti ajalukku. Hea commit on väike terviklik samm, mida tiimikaaslane saab üle vaadata, ajaloost leida ja vajaduse korral eraldi tagasi pöörata. Commit jääb esialgu sinu arvutisse; teistega jagamiseks saadetakse see haru GitHubi käsuga `git push`.

## Tee üks terviklik muudatus korraga

Üks commit peaks kirjeldama üht loogilist muudatust. See võib puudutada mitut faili, kui need kõik toetavad sama eesmärki. Ära pane ühte commit'i kokku omavahel seostamata töid, näiteks kasutajagruppide kirjeldust ja README kujunduse muutmist.

Enne commit'i vaata valitud muudatused üle:

```bash
git status
git add research/oppija-nimi-probleemikandidaadid.md
git diff --cached
git commit -m "Describe timetable user groups"
```

- `git status` näitab, millised failid on muutunud.
- `git add <fail>` valib faili järgmise commit'i jaoks.
- `git diff --cached` näitab täpselt, mida oled commit'i valinud.
- `git commit -m "..."` salvestab valiku Giti ajalukku koos lühikese sõnumiga.

Asenda näite failitee enda muudetud failiga. Kui töötad VS Code'i Source Control vaates, vaata enne commit'i samamoodi üle, millised muudatused on valitud.

## Kirjuta lühike ja konkreetne pealkiri

Commit'i pealkiri vastab küsimusele: **mida see muudatus teeb?** Kursusel kirjutame sõnumid inglise keeles, alustame tegusõnaga ja kirjeldame üht konkreetset muudatust.

| Hea näide | Miks see aitab? |
|---|---|
| `Describe timetable user groups` | Ütleb selgelt, mida commit lisab. |
| `Add interview questions` | Nimetab ühe konkreetse muudatuse. |
| `Clarify problem statement` | Näitab, millist osa täpsustati. |

Väldi ebamääraseid või autori tegevust kirjeldavaid sõnumeid:

- `update`, `fix`, `changes` – ei ütle, mida muudeti;
- `I added some stuff` – kirjeldab kirjutajat, mitte tulemust;
- `Added interview questions` – minevikuvormi asemel kasuta kokkulepitud tegusõna algvormi `Add`.

Hoia pealkiri lühike. Git'i juhend soovitab üldjuhul üht lühikest esimest rida; umbes 50 tähemärki on soovituslik piir, mitte Giti tehniline nõue. Lõppu pole punkti vaja panna.

## Lisa selgitus, kui pealkirjast ei piisa

Kui muudatuse põhjus pole ilmne, jäta pealkirja ja lisaselgituse vahele tühi rida. Kirjelda lühidalt, miks muudatus vajalik oli või millist otsust see toetab.

```text
Clarify timetable access issue

Interview notes showed that evening students often check room changes
from a phone while travelling to campus.
```

Pealkiri ütleb, mida muudeti; lisatekst selgitab vajaduse korral, miks.

## Issue'i number lisa pull request'i

Kursusel seome töö Issue'ga pull request'i kirjelduses, näiteks `Closes #12`. Nii jäävad ülesande eesmärk ja üle vaadatud muudatus GitHubis kokku. Issue numbrit ei pea iga commit'i sõnumisse kordama.

## Conventional Commits on eraldi kokkulepe

Mõnes projektis kasutatakse vormi `type(scope): description`, näiteks `docs(readme): describe setup`. Seda nimetatakse **Conventional Commits**-iks. See aitab automatiseerida versioonide ja muudatuste kokkuvõtteid, kuid nõuab meeskonnalt kindlat tüübi- ja vormingukokkulepet.

Kursusel me seda vormingut ei nõua. Kasutame lihtsat kuju `Verb + concrete change`, näiteks `Add interview questions`. Ära lisa `feat:`, `fix:` või muud eesliidet, kui tiim pole seda eraldi kokku leppinud.

## Kiirkontroll enne commit'i

- [ ] Valisin ainult ühe loogilise tööga seotud muudatused.
- [ ] Vaatasin valitud muudatused `git diff --cached` abil üle.
- [ ] Sõnum on inglise keeles, algab tegusõnaga ja kirjeldab tulemust.
- [ ] Sõnum on piisavalt konkreetne, et seda hiljem `git log`-ist ära tunda.

## Lisalugemine

- [Git'i juhend: commit'i pealkiri ja lisaselgitus](https://git-scm.com/docs/git-commit#_discussion)
- [Git'i juhis paranduste esitamiseks: lühike ja käskivas kõneviisis sõnum](https://git-scm.com/docs/SubmittingPatches)
- [Conventional Commits'i spetsifikatsioon](https://www.conventionalcommits.org/en/v1.0.0/)
