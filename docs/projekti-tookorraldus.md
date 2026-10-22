# Projekti töökorraldus

Seminarides 2–5 töötab iga tiim ühes GitHubi repositooriumis. Issue on GitHubi tööülesanne; pull request (PR) on muudatuse ülevaatamise ja ühendamise taotlus. Kasuta Giti terminalis või VS Code'i Source Control vaates.

## Töö käik lühidalt

**Issue → haru → muudatused ja commit'id → push → pull request → ülevaatus → merge → release**

1. **Tiim kasutab üht repositooriumi.** See asub organisatsioonis `TLUHK-RIF26` (näiteks `TLUHK-RIF26/tiim-01-tunniplaan`). Kõik tiimiliikmed töötavad samas repos; fork'i ei tehta. `main`-i muudatused käivad pull request'i kaudu.
2. **Klooni repo üks kord ja kontrolli Giti autoriandmeid.** GitHubi konto olemasolu ei tähenda, et Git sinu arvutis oleks seadistatud. Git lisab iga commit'i juurde autori nime ja e-posti; GitHub seostab commit'i sinu kontoga, kui e-post vastab sinu konto kinnitatud aadressile. Kui oled Giti varem kasutanud, võivad need seaded juba olemas olla.

   Klooni repo GitHubi lehelt kopeeritud URL-iga, ava kaust VS Code'is ja kontrolli terminalis väärtusi:

   ```bash
   git clone <GitHubis näidatud repo URL>
   cd <kloonitud repo kaust>
   git config user.name
   git config user.email
   ```

   Kui nimi või e-post puudub või on vale, seadista see selles repositooriumis:

   ```bash
   git config user.name "Ees Perenimi"
   git config user.email "sinu-GitHubi-kontoga-seotud-e-post"
   ```

   Need käsud muudavad ainult selle repo seadeid. Kasuta GitHubi kontol kinnitatud e-posti või GitHubi seadetes näidatud privaatset `noreply` aadressi.

3. **Tee töö nähtavaks GitHub Projectsis.** Igal ülesandel on Issue, selge kirjeldus, valmisoleku tingimus ja vastutaja. Liiguta kaart tahvlil vastavalt töö seisule: `Backlog` → `In progress` → `Review` → `Done`.
4. **Loo igale Issue'le eraldi haru.** Alusta ajakohasest `main`-ist:

   ```bash
   git switch main
   git pull --ff-only
   git switch -c issue-12-describe-user-groups
   ```

   Haru nimi on inglise keeles kujul `issue-<number>-<short-english-description>`.
5. **Salvesta väikesed, sisulised muudatused commit'idena.** Kirjuta sõnum inglise keeles, alusta tegusõnaga ja kirjelda üht muudatust, näiteks `Describe timetable user groups`. Väldi sõnumeid nagu `update` või `fix`.
6. **Saada haru GitHubi ja ava pull request (PR).**

   ```bash
   git push -u origin issue-12-describe-user-groups
   ```

   PR-is ütle lühidalt, mida muutsid ja miks. Seo Issue näiteks reaga `Closes #12` ning vali ülevaatajaks tiimikaaslane.
7. **Tiimikaaslane vaatab muudatuse üle.** Ta loeb PR-i muudatused läbi, kommenteerib ja valib **Approve** või **Request changes**. Vajadusel parandab autor sama haru ja saadab uued commit'id. Heaks kiidetud PR liidetakse `main`-i; seejärel uuenda kohalikku `main`-i käsuga `git pull --ff-only`.
8. **Release manager teeb etapi lõpus release'i.** Roll vahetub seminariti. Enne avaldamist kontrollib ta, et etapi muudatused on üle vaadatud ja ühendatud ning otsuse- ja release-failid on ajakohased. Seejärel loob GitHubis vastava tag'i ja release'i.

| Etapp | Release |
|---|---|
| Seminar 2 | `v0.1.0` |
| Seminar 3 | `v0.2.0` |
| Seminar 4 | `v0.3.0` |
| Seminar 5 | `v0.4.0` |
| Eksam | `v1.0.0` |

## Kolm kokkulepet

- Ära muuda `main`-i otse.
- Ära kiida enda pull request'i ise heaks.
- Iga õppija avab igas projektietapis vähemalt ühe PR-i ja vaatab üle vähemalt ühe tiimikaaslase PR-i.
