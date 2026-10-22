# Näidisõppija tööteekond Issue’st release’i kinnitamiseni

See näide jälgib pseudoõppija Mari Maasikat tema esimesest ülesandest seminari 2 release’i `v0.1.0` kontrollimiseni. Nimed ja ülesannete tulemused on õppematerjali jaoks väljamõeldud. Päris tiim teeb sama töövoo enda liikmete ja kogutud tõenditega.

## Kes mida teeb?

Selles näites loob õppejõud tiimile repositooriumi ja GitHub Projecti ning annab tiimiliikmetele ligipääsu. Tiimile jagatakse üks repositoorium. Iga õppija kloonib selle enda arvutisse ise, ühe korra.

Tiim lepib koos kokku, millised tööd tuleb teha. Probleemikandidaatide kaardistamiseks loob tiim igale õppijale eraldi Issue’i ja määrab selle sellele õppijale. Mari töötab ainult enda Issue’ga ning kirjutab enda kandidaadid eraldi faili. Teised õppijad teevad samal ajal sama ülesande enda Issue'ides, enda harudes ja enda failides. Pärast kõigi individuaalsete PR-ide ülevaatust ja ühendamist loob tiim eraldi Issue'id kandidaatide võrdlemiseks ning ühise probleemiotsuse koostamiseks.

| Inimene | Näite vastutus |
|---|---|
| Õppejõud | Loob tiimi repo ja Projecti või korraldab nende loomise ning annab ligipääsu. |
| Joonas | Aitab tiimil luua igale õppijale eraldi kaardistamise Issue'i. Mari Issue määratakse Marile; hiljem vaatab Joonas tema PR-i üle. |
| Mari | Kloonib repo ühe korra, teeb ainult enda kaardistamise Issue'i, avab PR-i, parandab tagasiside järgi ning vaatab hiljem üle kaaslase PR-i. |
| Liis | Teeb enda kaardistamise Issue'i ja aitab hiljem tiimil valitud probleemi kontrollida ning ühist otsust koostada. |
| Rasmus | Täidab release manageri rolli ja valmistab ette `v0.1.0` release’i. |

Päris kursusel määratakse rollid ja ülesannete vastutajad tiimis. Issue'i võib luua üks tiimiliige, aga iga õppija individuaalne kaardistamise Issue määratakse sellele õppijale. Joonas ei tee Mari Issue'i tööd tema eest. Issue looja, töö tegija ja PR-i ülevaataja võivad olla eri inimesed.

## 1. Saan ligipääsu ja kloonin repo

Õppejõud saadab tiimile GitHubi repositooriumi lingi. Ava link ja kontrolli, et näed repo sisu ning saad sellesse muudatusi teha. Kui mul pole ligipääsu, küsin selle enne töö alustamist.

Kui mul pole sellest repositooriumist veel kohalikku koopiat, vajutan GitHubis **Code**, kopeerin HTTPS-aadressi ning käivitan terminalis:

```bash
git clone <GitHubist kopeeritud repo URL>
cd <kloonitud repo kaust>
git status
```

- `git clone` laeb repositooriumi arvutisse ja seab GitHubi repo kaugühenduseks nimega `origin`.
- `cd` liigub kloonitud projekti kausta. Asenda nurksulgudes tekst enda repo kausta nimega.
- `git status` näitab, millises harus oled ja kas sul on salvestamata muudatusi.

Kui olin repo juba varem klooninud, ei klooni ma seda uuesti. Avan olemasoleva kausta VS Code’is ja kontrollin `git status` käsuga, et olen õiges repos.

Kontrollin Giti autoriandmeid:

```bash
git config user.name
git config user.email
```

Need käsud näitavad selles repos kasutatavat commit'i autori nime ja e-posti. Kui mõlemad on õiged, pole midagi muuta vaja.

Kui nimi või e-post puudub või on vale, seadistan selle ainult selles repos:

```bash
git config user.name "Mari Maasikas"
git config user.email "minu-GitHubi-kontoga-seotud-e-post"
```

Esimene käsk määrab commit'idele lisatava nime; teine määrab autori e-posti. Kasuta GitHubi kontoga seotud kinnitatud aadressi või GitHubi seadetes näidatud privaatset `noreply` aadressi.

Kloonimine on õppija isiklik ettevalmistus. Joonas ei klooni repo minu eest ja mina ei klooni eraldi koopiat iga Issue’i jaoks.

## 2. Saan enda individuaalse Issue'i

Seminaris arutame läbi kliendisoovi:

> Haapsalu Kolledž soovib oma tunniplaani veebilehte muuta kaasaegsemaks.

Me ei eelda, et vaja on uut kujundust või kindlat funktsiooni. Tiim loob iga õppija jaoks eraldi Issue'i. Minu Issue'i pealkiri on näiteks **„Koosta Mari probleemikandidaadid”**. Kirjelduses on eesmärk ja valmisoleku tingimused ning mina olen vastutaja. Teistel õppijatel on samasuguse eesmärgiga, kuid enda nimele määratud Issue ja eraldi fail. Tiim lisab kõik need Issue'd Projecti tahvlile veergu `Backlog`.

Vaatan enda Issue'i läbi. Kui kirjeldus on ebaselge, küsin enne töö alustamist täpsustust. Liigutan enda kaardi `In progress` veergu. Näidisrepo [Issue #1](https://github.com/TLUHK-RIF26/tiim-demo-tunniplaan/issues/1) näitab ühe kaardistamisülesande kirjeldust. Päris tiimis loob meeskond sama töö jaoks iga õppija nimele eraldi Issue'i; see näidisrepo kaart ei asenda neid individuaalseid Issue'sid.

## 3. Teen ülesande oma harus

Enne haru loomist toon värske `main`-i:

```bash
git switch main
git pull --ff-only
git switch -c issue-1-mari-problem-candidates
```

- `git switch main` lülitab kohaliku töö `main`-harule.
- `git pull --ff-only` toob GitHubi `main`-haru värskeimad muudatused. Käsk peatub, kui harusid ei saa lihtsalt kokku viia.
- `git switch -c ...` loob uue haru ja lülitab töö sinna. Asenda `1` enda Issue'i numbriga.

Päris tiimis asendan `1` enda Issue numbriga. Haru nimi on inglise keeles ning seob haru minu isikliku ülesandega.

Kirjutan vähemalt kolm võimalikku kasutusolukorda. Igaühe juures märgin inimese, olukorra, eesmärgi, võimaliku takistuse ja mõju ning eristan teadaoleva oletusest. Ma ei esita oletust kasutajauuringu tulemusena ega vali veel lahendust. Salvestan kandidaadid enda faili `research/mari-maasikas-probleemikandidaadid.md`. Teised õppijad kirjutavad enda failidesse enda kandidaadid; mina ei muuda kaaslase faili. Nii saab igaüks oma töö eraldi harus esitada ja tiim saab kandidaate hiljem koos võrrelda.

Kontrollin, mida muutsin, ning vaatan muudatuse enne commit’i üle:

```bash
git status
git add research/mari-maasikas-probleemikandidaadid.md
git diff --cached
git commit -m "Describe timetable use cases"
git push -u origin issue-1-mari-problem-candidates
```

- `git status` näitab muudetud faile.
- `git add <fail>` valib faili järgmise commit'i jaoks.
- `git diff --cached` näitab täpselt, millised muudatused on commit'iks valitud. Kontrolli need enne salvestamist üle.
- `git commit -m "..."` salvestab valitud muudatused kohalikku Giti ajalukku ja lisab neile sõnumi.
- `git push -u origin <haru>` saadab haru GitHubi. `origin` on kloonimisel lisatud GitHubi repo nimi; `-u` seob kohaliku haru selle kaug-haruga. Asenda haru näide enda haru nimega.

Commit’i sõnum ütleb inglise keeles, mida muutsin. Kui muudatus vajab parandamist, teen uue commit’i samas harus.

Enne PR-i avamist lisan samasse harusse ka enda refleksiooni `reflections/mari-maasikas-v0.1.0.md`. Kirjeldan enda panust, õpitut ja saadud tagasisidet. Nii saab Joonas vaadata üle nii ülesande tulemuse kui ka refleksiooni.

```bash
git add reflections/mari-maasikas-v0.1.0.md
git diff --cached
git commit -m "Add individual reflection"
git push
```

Siin valib `git add` refleksioonifaili, `git diff --cached` võimaldab selle üle vaadata, `git commit` salvestab selle uue muudatusena ning `git push` saadab commit'i sama haru kaudu GitHubi. Kuna haru seos loodi eelmise `git push -u` käsuga, pole `origin` ega haru nime enam vaja korrata.

## 4. Saadan töö PR-ina ülevaatusele

GitHubis avan enda haru põhjal pull request’i `main`-i. Panen pealkirjaks näiteks **Kaardista tunniplaani kasutusolukorrad** ning kirjeldan:

- mida lisasin ja miks;
- kuidas see vastab Issue’i valmisoleku tingimustele;
- lingi Issue’le reaga `Closes #1`;
- Joonase ülevaatajaks.

Seejärel liigub Projecti kaart `Review` veergu. Joonas vaatab muudatuse läbi ning kontrollib, kas ma eristasin fakte ja oletusi ning kas ülesanne on täidetud. Ta võib küsida täpsustusi või valida **Approve**.

Kui Joonas palub muudatust, loen kommentaari, parandan sama haru faili ja saadan uue commit’i:

```bash
git add research/mari-maasikas-probleemikandidaadid.md
git commit -m "Clarify timetable use case assumptions"
git push
```

`git add` valib parandatud faili, `git commit` salvestab paranduse eraldi muudatusena ning `git push` saadab selle olemasolevasse harusse. PR uueneb automaatselt.

Vastan Joonase kommentaarile, et ta teaks, mida muutsin. Ma ei kiida enda PR-i ise heaks.

Pärast Joonase heakskiitu vajutan **Merge pull request**. `Closes #1` sulgeb Issue’i ühendamisel automaatselt. Joonas või mina liigutame Projecti kaardi `Done` veergu.

## 5. Toon teiste muudatused enda arvutisse ja teen ülevaatuse

Pärast PR-i ühendamist värskendan kohalikku `main`-i:

```bash
git switch main
git pull --ff-only
```

`git switch main` viib tagasi põhiharule. `git pull --ff-only` uuendab selle GitHubis ühendatud muudatustega. Enne käsu käivitamist veendu `git status` abil, et sul pole pooleliolevaid muudatusi.

Pärast kandidaatide võrdlust saab iga õppija eraldi valideerimise Issue'i või konkreetse valideerimistegevuse. Mina saan ülesande kontrollida üht kasutajaolukorda vestluse või vaatlusega. Lepin tiimiga kokku, millist oletust kontrollin, teen tegevuse ja kirjutan tulemuse dokumentatsiooni. Teen selleks oma harus commit'i ning avan PR-i; kaaslane vaatab selle üle. Joonas teeb enda valideerimisülesande ja tema PR-i vaatan mina üle **Files changed** vaates. Kontrollin, kas tulemus eristab tegelikku infot oletustest ja kas piirangud on selgelt kirjas. Kui Joonas parandab tööd, vaatan muudatuse uuesti üle.

Liis koostab tiimi otsuse ja lähteülesande mustandi. Annan sellele tagasisidet tiimi kokkulepitud Issue’i või PR-i kaudu. Iga meeskonnaliige teeb oma töö eraldi harus ja saab vähemalt ühe kaaslase sisulise ülevaatuse.

## 6. Lisan refleksiooni ja aitan release’i üle kontrollida

Kontrollin, et minu refleksioonifail on minu PR-i kaudu `main`-i jõudnud. Teised õppijad lisavad samamoodi enda refleksioonifaili oma PR-iga; nii jõuavad kõik failid `main`-i enne release’i.

Rasmus on selle etapi release manager. Ta kontrollib, et:

- tiimi otsus `decisions/001-probleemi-valik.md` kirjeldab valitud probleemi, alternatiive, tõendeid ja lähteülesannet;
- `releases/v0.1.0.md` ütleb, mida teame, mida otsustasime, mis jäi lahtiseks ja mis on järgmine samm;
- iga õppija refleksioon on repos;
- vajalikud PR-id on üle vaadatud ja `main`-i ühendatud.

Rasmus lisab või uuendab faili `releases/v0.1.0.md` PR-i kaudu. Tiimikaaslane vaatab selle üle ning Rasmus ühendab heaks kiidetud PR-i `main`-i. Alles siis loob Rasmus GitHubis release'i:

1. Ava GitHubis tiimi repositoorium ja vali **Releases → Draft a new release**.
2. Vali **Choose a tag**. Sisesta `v0.1.0` ja vali **Create new tag**, sest see on selle repo esimene release.
3. Vali tag'i sihiks `main`. Nii märgib tag release'i ettevalmistamiseks ühendatud seisu. Kontrolli, et release notes'i PR ja kõik etapi tööd on `main`-i ühendatud.
4. Pane release'i pealkirjaks **Probleem sõnastatud**. Kirjeldusse lisa lühike kokkuvõte ning link failile `releases/v0.1.0.md`.
5. Vaata tag, siht ja tekst üle ning vajuta **Publish release**.
6. Ava avaldatud release uuesti ja kontrolli, et see kasutab tag'i `v0.1.0` ning viitab õigele otsuse- ja release notes'i failile.

GitHubi nupud võivad aja jooksul muutuda; [GitHubi ametlik juhend](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) kirjeldab sama release'i ja tag'i loomise voogu.

### Mille järgi tag'i nimi valida?

Tag on Giti märgis, mis osutab ajaloos kindlale commit'ile ehk kokkulepitud seisule. GitHub Release on selle tag'i juurde avaldatud pealkiri ja kirjeldus. Kursusel tehakse **üks tag iga lõpetatud etapi kohta**, mitte iga Issue'i, haru ega commit'i jaoks. Tag loob release manager pärast seda, kui etapi tööd ja release notes on PR-idega `main`-i ühendatud.

Meie kursuse lihtsustatud versiooninumbris (`vMAJOR.MINOR.PATCH`) tähendab alguse `v` versiooni. Esimene number püsib `0`, kuni kursuse projekt on pooleli; lõplikul eksamirelease'il muutub see `1`-ks. Keskmine number suureneb iga projektietapiga. Viimane number püsib `0`, kui avaldame etapi plaanitud release'i; eraldi parandatud väljaande korral suureneb see, näiteks `v0.1.1`.

Kasuta kursuse versioonijada:

| Etapp | Tag | Põhimõte |
|---|---|---|
| Seminar 2 | `v0.1.0` | Esimene projektietapp |
| Seminar 3 | `v0.2.0` | Järgmine seminar lisab ühe etapi versiooninumbrile |
| Seminar 4 | `v0.3.0` | Sama jada jätkub |
| Seminar 5 | `v0.4.0` | Sama jada jätkub |
| Eksam | `v1.0.0` | Kursuse terviklik lõppversioon |

Ära kasuta juba avaldatud tag'i uuesti ega liiguta seda teise commit'i peale. Kui avaldatud release vajab hiljem eraldi parandatud väljaannet, loo uus parandustag, näiteks `v0.1.1`, ja kirjelda parandust release notes'is.

## 7. Kinnitan, et release on olemas ja õige

Ma ei eelda, et töö lõppes nupule vajutamisega. Ava Rasmuse jagatud GitHub Release ning kontrolli:

- tag on `v0.1.0` ja release on avaldatud;
- release’i pealkiri on **Probleem sõnastatud**;
- release notes viitavad otsusefailile ja järgmisele etapile;
- otsusefail ning kõigi õppijate refleksioonid on `main`-is;
- Projecti seminari 2 töökaardid on lõpetatuna märgitud.

Kui midagi puudub või link ei tööta, annan sellest Rasmusele teada enne, kui tiim nimetab etapi lõpetatuks. Kui kontroll on korras, saan öelda: **„Olen kontrollinud, et meie `v0.1.0` release on avaldatud ja sisaldab kokkulepitud dokumente.”**

Release kinnitab dokumentatsiooni hetkeseisu. See ei tähenda, et tunniplaani uus veebileht oleks valmis või et kasutajaprobleem oleks täielikult lahendatud.

## Kes teeb mida kokkuvõtlikult?

| Tegevus | Kes teeb? |
|---|---|
| Tiimi repo loomine ja ligipääsu jagamine | Õppejõud või kursusel määratud repo haldaja |
| Repo kloonimine | Iga õppija enda arvutis, üks kord |
| Individuaalse kaardistamise Issue'i loomine ja määramine | Joonas koos tiimiga loob ühe igale õppijale; iga Issue määratakse selle õppijale |
| Mari kaardistamise Issue'i töö | Mari enda harus |
| Kandidaatide võrdlus ja ühine otsus | Kogu tiim eraldi Issue'ides; määratud vastutaja koondab dokumendi |
| PR-i avamine ja parandused | Mari |
| PR-i ülevaatus | Joonas |
| PR-i heakskiit ja merge | Joonas kiidab heaks; Mari ühendab pärast heakskiitu |
| Release notes, tag ja GitHub Release | Rasmus release managerina; kaaslane vaatab PR-i üle |
| Release’i olemasolu ja sisu kontroll | Mari ja ülejäänud tiim |
