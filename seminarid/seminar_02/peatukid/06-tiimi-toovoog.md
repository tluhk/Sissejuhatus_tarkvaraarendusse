# Tiimi töövoog

**Eesmärk:** iga õppija lisab oma probleemikandidaadid ühisesse reposse ning vaatab üle kaaslase muudatuse. Kasutage VS Code'i terminali või Source Control vaadet; Windowsis valige terminaliks Git Bash.

Läbiv näide kasutab õppija Mari Tamme ja Issue numbrit 12. Asenda näites nimi, number ja repo aadress enda omadega.

## Sisukord

- [1. Ühine repo ja töökoopia](#1-ühine-repo-ja-töökoopia)
- [2. Enda Issue ja Projectsi tahvel](#2-enda-issue-ja-projectsi-tahvel)
- [3. Haru ja tööfail](#3-haru-ja-tööfail)
- [4. Commit ja push](#4-commit-ja-push)
- [5. Pull request, ülevaatus ja merge](#5-pull-request-ülevaatus-ja-merge)
- [6. Uuendamine ja järgmine ülesanne](#6-uuendamine-ja-järgmine-ülesanne)

---

## 1. Ühine repo ja töökoopia
Õppejõud loob või määrab tiimi repo organisatsioonis `TLUHK-RIF26` ning annab liikmetele ligipääsu. Iga liige võtab kutse vastu ja kloonib **sama repo** oma arvutisse. Kloonimine teeb kohaliku töökoopia; eraldi GitHubi repo ehk fork pole tiimiliikmena vajalik. Üksikuid Issue'sid ei kloonita.

Kopeeri repo lehelt **Code → HTTPS** aadress. Järgmises näites on repo nimeks `tiim-01-tunniplaan`:

```bash
git clone https://github.com/TLUHK-RIF26/tiim-01-tunniplaan.git
cd tiim-01-tunniplaan
git config user.name
git config user.email
```

Esimene rida laeb repo arvutisse, teine avab selle kausta terminalis. Kaks viimast näitavad commit'ide autoriandmeid. GitHubi konto olemasolu ei seadista kohalikku Giti automaatselt. Kui nimi või e-post on vale või puudu, paranda need selles repos:

```bash
git config user.name "Mari Tamm"
git config user.email "sinu-GitHubi-kontoga-seotud-e-post"
```

Esimene rida määrab autori nime, teine e-posti. Kasuta enda GitHubi kontol kinnitatud aadressi või seadetes näidatud `noreply` aadressi. Kui andmed olid õiged, pole neid vaja uuesti määrata. Ava kloonitud kaust VS Code'is.

---

## 2. Enda Issue ja Projectsi tahvel
Iga õppija loob repo **Issues → New issue** kaudu oma kaardistusülesande, määrab selle endale ning lisab valmisoleku tingimuse. Mari näide:

```markdown
Pealkiri: Mari probleemikandidaadid

Eesmärk: kirjeldada vähemalt kolme võimalikku tunniplaani kasutusprobleemi.
Fail: research/mari-tamm-probleemikandidaadid.md
Valmis, kui: kandidaadid ja enesehindamine on kirjas ning kaaslane on PR-i üle vaadanud.
Ajahinnang: 1 tund täpsustamiseks pärast seminari.
Tähtaeg: tiimiga kokkulepitud kuupäev.
```

Näites saab see Issue numbri 12. Kaaslastel on oma Issue'd ja oma failid.

Tiim kasutab **GitHub Projectsi** tahvlit, mis on ülesannete ühine vaade. Üks liige loob vajaduse korral Board-vaate ja annab tiimile muutmisõiguse. Lisage sinna repo Issue'd ning seadistage olekud `Backlog`, `In progress`, `Review`, `Done`. Issue saab lisada selle külgpaneeli **Projects** valikust.

Kanban aitab töö liikumist jälgida. Ülesannet alustades vali `In progress`, PR-i ülevaatust oodates `Review` ja pärast ühendamist `Done`. Leppige kokku, kui palju töid korraga pooleli hoiate. Kui midagi takerdub, aidake see lõpetada enne uue alustamist. Jira ja ClickUp on teised samalaadsed töövahendid; kursusel kasutame GitHub Projectsi.

Jaga suurem töö väikesteks Issue'deks, arvesta nende sõltuvustega ning märgi ajahinnang ja tähtpäev. Lõpus võrdle hinnangut tegeliku ajakuluga, et järgmine plaan oleks realistlikum.

---

## 3. Haru ja tööfail
Kontrolli terminalis, et oled repo kaustas ja töökaust on puhas:

```bash
pwd
git status
git switch main
git pull --ff-only
git switch -c issue-12-map-problem-candidates
mkdir -p research
```

- `pwd` näitab praegust kausta; `git status` näitab haru ja salvestamata muudatusi. Kui sul on varasem töö pooleli, lõpeta see enne haru vahetamist.
- `git switch main` viib peaharusse.
- `git pull --ff-only` toob sinna GitHubi muudatused. Lahknenud ajaloo korral käsk peatub: küsi abi.
- `git switch -c ...` loob ja avab enda ülesande haru. Kasuta ingliskeelset kuju `issue-<number>-<short-english-description>`.
- `mkdir -p research` loob tööfailide kausta, kui seda veel pole.

Loo VS Code'is fail `research/mari-tamm-probleemikandidaadid.md`, lisa enda kandidaadid ja salvesta. Peaharu `main` muudetakse ainult PR-ide kaudu.

---

## 4. Commit ja push
```bash
git status
git add research/mari-tamm-probleemikandidaadid.md
git diff --cached
git commit -m "Add timetable problem candidates"
git push -u origin issue-12-map-problem-candidates
```

- `status` näitab muutunud faile.
- `add` valib nimetatud faili järgmise commit'i jaoks.
- `diff --cached` näitab valitud muudatusi. Kontrolli sisu enne jätkamist.
- `commit` salvestab valiku kohalikku ajalukku.
- `push` saadab haru GitHubi; `-u` seob kohaliku haru kaugemas repos oleva haruga. Hiljem piisab samas harus käsust `git push`.

Üks commit olgu üks loogiline muudatus. Ingliskeelne sõnum algab tegusõnaga ja ütleb, mida muudeti. Näiteks `Clarify problem impact` annab rohkem infot kui `update`. Põhjenduse saab vajaduse korral lisada pikemasse sõnumisse. Lisalugemine: [commit'i sõnumite head tavad](../../../concepts/commit/README.md).

---

## 5. Pull request, ülevaatus ja merge
Ava GitHubis saadetud haru juures **Compare & pull request**. Siht on `main`. Kirjelda muutust ja lisa `Closes #12`, mis seob PR-i ülesandega ning sulgeb selle peaharusse ühendamisel. Vali ülevaatajaks tiimikaaslane ja vii kaart tahvlil olekusse `Review`.

Ülevaataja loeb vahekaardil **Files changed** muudatused läbi. Ta kontrollib, kas kõik kandidaadid on arusaadavad ning tõendid ja oletused eristatud. Seejärel valib ta **Approve** või põhjendatud **Request changes**. Pelk „korras” ei näita veel sisulist kontrolli; kasuta vajaduse korral [PR-i kontrollnimekirja](../../mallid/pull-request.md).

Autor parandab vajaduse korral sama faili samas harus, teeb uue commit'i ja push'i. PR uueneb automaatselt. Pärast kaaslase heakskiitu ühendab autor muudatuse nupuga **Merge pull request**, kustutab GitHubis haru ja märgib töö `Done`. Enda PR-i ise heaks ei kiideta.

---

## 6. Uuendamine ja järgmine ülesanne
Kui sinu töö on commit'itud ja push'itud ning `git status` näitab puhast töökausta:

```bash
git switch main
git pull --ff-only
```

Esimene rida avab peaharu, teine toob ühendatud muudatused arvutisse. Kontrolli failidest, et näed ka kaaslaste töid. Järgmise Issue jaoks loo uuendatud `main`-ist uus haru. Kui näed konflikti või arusaamatut veateadet, lisa see Issue kommentaari ja küsi abi.

**Kontrollpunkt:** sinu töö on peaharus, oled kaaslase PR-i sisuliselt üle vaadanud ja kohalik koopia on ajakohane. Kui seminaris jääb mõni samm pooleli, jätka samast kohast [kodutöös](07-kodutoo-ja-release.md).

VS Code'i Source Control vaates vastavad neile sammudele haru valimine, muudatuste ülevaatus ja **Stage Changes**, sõnumiga **Commit** ning **Publish Branch** või **Push**. PR ja selle ülevaatus toimuvad GitHubis.
