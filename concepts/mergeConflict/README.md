# Giti konfliktide lahendamine

**Merge-konflikt** tekib, kui kaks haru muudavad sama rida või üks haru kustutab faili, mida teine muudab. Git ei tea, kumb muudatus jätta, ja peatab ühendamise, kuni inimene otsustab.

Konflikt ei ole viga ega märk halvast tööst. See tavaline olukord näitab, et kaks inimest töötasid sama koha kallal. Kui muudatused on samas failis, kuid eri kohtades, ühendab Git need tavaliselt ise.

## Kuidas konfliktist teada saad?

- GitHubi pull request'is on teade **This branch has conflicts that must be resolved**.
- Terminalis näitab `git merge` rida `CONFLICT` ja selle faili nime, kus konflikt on.

## Lahendamine terminalis

Näites on sinu haru `issue-12-describe-user-groups`. Asenda see enda haru nimega.

### 1. Salvesta oma töö

Kontrolli, et commit'imata muudatusi ei oleks:

```bash
git status
```

Kui on, tee neist enne jätkamist commit.

### 2. Too `main`-i uus seis enda harusse

```bash
git switch main
git pull --ff-only
git switch issue-12-describe-user-groups
git merge --no-edit main
```

Kui konflikti ei teki, on `main` juba sinu harus. Jätka sammust 6.

### 3. Vaata, millised failid on konfliktis

```bash
git status
```

Konfliktis failid on loetelus **Unmerged paths**.

### 4. Paranda fail

Ava fail. Konfliktne koht näeb välja nii:

```text
<<<<<<< HEAD
Meie tiim teeb tunniplaani mobiilis loetavaks.
=======
Meie tiim parandab tunniplaani otsingut.
>>>>>>> main
```

- `<<<<<<< HEAD` ja `=======` vahel on sinu haru tekst.
- `=======` ja `>>>>>>> main` vahel on `main`-i tekst.

Otsusta, milline tekst jääb. Võid valida ühe, ühendada mõlemad või kirjutada uue. Kui muudatus pole sinu oma, räägi selle autoriga. Kustuta kõik kolm märgirida. Tulemus võib olla näiteks:

```text
Meie tiim teeb tunniplaani otsingu mobiilis mugavaks.
```

### 5. Märgi konflikt lahendatuks ja tee commit

```bash
git add README.md
git commit -m "Resolve conflict in README"
```

Asenda `README.md` enda faili nimega. Kui konfliktis oli mitu faili, paranda ja lisa need kõik.

### 6. Saada tulemus GitHubi

```bash
git push
```

Pull request uueneb ise ja konfliktiteade kaob. Muudatuse vaatab üle tiimikaaslane nagu tavaliselt.

## Lahendamine VS Code'is

Terminali asemel võid kasutada VS Code'i. Samm 2 on sama. Seejärel:

1. Ava **Source Control** vaade. Konfliktis failid on jaotises **Merge Changes**.
2. Ava fail. Konfliktse koha kohal on valikud:
   - **Accept Current Change** jätab sinu haru teksti;
   - **Accept Incoming Change** jätab `main`-i teksti;
   - **Accept Both Changes** jätab mõlemad.
3. Vajaduse korral paranda tekst käsitsi ja salvesta fail.
4. Vajuta faili juures **+** (**Stage Changes**), kirjuta sõnum ja vajuta **Commit**.
5. Vajuta **Sync Changes**.

## Kui läks segaseks

Kui sa pole veel commit'i teinud, saad ühendamise katkestada ja alustada uuesti:

```bash
git merge --abort
```

Failid lähevad tagasi sellesse seisu, mis neil oli enne `git merge` käsku. Kui vaja, küsi tiimikaaslaselt abi.

Ära kasuta käsku `git push --force`. See võib kustutada teiste tööd.

## Kuidas konflikte vähendada?

- Alusta iga uut tööd ajakohasest `main`-ist.
- Tee väikeseid pull request'e ja ühenda need kiiresti.
- Lepi tiimiga kokku, kes millist ühist faili parajasti muudab.
- Too `main` enda harusse, kui su töö kestab mitu päeva.

## Kontroll enne push'i

- [ ] Failides pole märke `<<<<<<<`, `=======` ega `>>>>>>>`. Käsk `git diff --check main` annab märkidest teada.
- [ ] Alles jäänud tekst on selline, milles tiim on kokku leppinud.
- [ ] `git status` ei näita enam **Unmerged paths**.

## Vaata ka

- [Projekti töökorraldus](../../docs/projekti-tookorraldus.md)
- [Uuenda peaharu enne järgmist ülesannet](../mergemain/README.md)
- [Commit'i sõnumid ja head tavad](../commit/README.md)
- [Git: Basic Merge Conflicts](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts)
