# Prooviülesanne: projektitöö esimesest release'ist järgmise etapi alguseni

See juhend näitab sammhaaval, kuidas tiim läbib seminari 2 projektitöö, avaldab esimese release'i `v0.1.0` ning alustab seejärel seminari 3 esimest ülesannet. See sobib ka siis, kui puudusid seminarist või teed töö iseseisvalt järele.

Kui soovid näha sama protsessi ühe õppija esimeses isikus, vaata [näidisõppija tööteekonda Issue’st release’i kinnitamiseni](naidisoppija-esimene-iteratsioon.md). Seal on selgitatud ka seda, kes loob Issue’i ja miks iga tiimiliige kloonib repo enda arvutisse eraldi.

Näide kasutab kursuse ühist õppestsenaariumi: **Haapsalu Kolledž soovib tunniplaani veebilehte kaasaegsemaks muuta.** Tiim peab ise leidma ja kontrollima kasutajaprobleemi. Ära võta juhendist ette valmis probleemi, kasutajalugu ega tõendit.

## Enne alustamist

Loe läbi [seminari 2 õppematerjal](../seminarid/seminar_02/01-seminar.md), [projekti töökorraldus](projekti-tookorraldus.md) ja [kodutöö 2](../seminarid/seminar_02/03-kodutoo.md). Seminari 3 etapi alguses kasuta [seminari 3 materjali](../seminarid/seminar_03/seminar.md) ja [kodutöö 3 juhendit](../seminarid/seminar_03/homework.md).

Vaja on tiimi GitHubi repositooriumi ja GitHub Projecti ligipääsu. Iga õppija kloonib repo enda arvutisse üks kord. Kui teed tööd omal käel, võid mustandid ise koostada, kuid päris kursuse töös peavad kaaslane sinu pull request'i üle vaatama ja sina vaatama üle kaaslase töö. Ära kiida enda pull request'i ise heaks.

Juhendis kasutatakse järgmisi mõisteid: **Issue** kirjeldab üht ülesannet; **haru** (*branch*) on selle ülesande jaoks eraldi tööliin; **commit** salvestab muudatuste komplekti Giti ajaloos; **push** saadab haru GitHubi; **pull request** (PR) palub kaaslasel muudatuse üle vaadata ja `main`-i ühendada; **merge** ühendab heaks kiidetud muudatuse `main`-iga. **Tag** märgib kindlat seisu Giti ajaloos ja **GitHub Release** avaldab selle versiooni pealkirja ning kirjeldusega. Vaata ka [projekti töökorralduse juhendit](projekti-tookorraldus.md) ja [ühe õppija näidet](naidisoppija-esimene-iteratsioon.md).

## Kuidas näidisrepo juhendit täiendab?

[Tiim-demo-tunniplaani näidisrepo](https://github.com/TLUHK-RIF26/tiim-demo-tunniplaan) näitab, milline võib tiimi töö välja näha seminari 3 alguses. Repo on privaatne ja selle vaatamiseks on vaja `TLUHK-RIF26` organisatsiooni ligipääsu. Vaata sealt eelkõige [otsust](https://github.com/TLUHK-RIF26/tiim-demo-tunniplaan/blob/main/decisions/001-probleemi-valik.md), [uurimise näidist](https://github.com/TLUHK-RIF26/tiim-demo-tunniplaan/blob/main/research/vaatlus-ja-kontroll.md), [release'i `v0.1.0`](https://github.com/TLUHK-RIF26/tiim-demo-tunniplaan/releases/tag/v0.1.0) ja [seminari 3 alustavat Issue't](https://github.com/TLUHK-RIF26/tiim-demo-tunniplaan/issues/5).

Näidisrepo aitab mõista allpool kirjeldatud väljundeid, kuid ei asenda töö samme. Selle pseudoõppijate nimed, vestlused, vaatlused ja tulemused on väljamõeldud. Need näitavad dokumentide kuju, mitte päris tõendeid. Päris tiim kogub ise kontrollitava info ning teeb töö oma Issue'de, harude, commit'ide, pull request'ide ja kaaslaste ülevaatustega. Näidisrepo on ühe hetke seis; seal ei ole pseudoõppijate nimel tehtud PR-ide ajalugu.

## Osa 1: probleemi uurimine ja release `v0.1.0`

### 1. Vaata üle kliendisoov

Lähtepunkt on soov muuta tunniplaani veebileht „kaasaegsemaks”. See ei ütle veel, kellel on probleem, millises olukorras see tekib ega mida tuleks ehitada. Alusta praeguse tunniplaani kasutamisest, mitte kujunduse või tehnoloogia valimisest.

### 2. Pane kirja võimalikud probleemid

**Iga õppija teeb selle osa eraldi.** Tiim loob iga liikme jaoks oma Issue'i ja määrab selle sellele liikmele. Seega ei vali kogu tiim üht esimest Issue't, mida ainult üks inimene lahendab. Iga õppija kirjeldab enda Issue'i harus vähemalt kolm võimalikku kasutusolukorda, paneb tulemuse enda faili ning avab oma töö kohta PR-i. Kaaslane vaatab PR-i üle.

Iga kandidaadi kohta märgi:

- kes seda kasutab ja millal;
- mida inimene püüab teha;
- mis võib teda takistada;
- mis tagajärg võib tekkida;
- mida tead ja mida alles oletad.

Kasuta alguses näiteks sellist mustandit:

```text
Kasutaja ja olukord:
Eesmärk:
Võimalik takistus:
Võimalik mõju:
Teada / oletus:
Mida tuleks kontrollida:
```

Täida iga rida oma kandidaadi kohta: kes ja millises olukorras tegutseb, mida ta tahab teha, mis võib segada, mis tagajärg võib olla, mis on fakt või oletus ning millist infot on vaja juurde koguda.

Need on esialgsed kandidaadid, mitte kinnitatud probleemid. Ära kirjuta välja mõeldud kasutajakogemust faktina. Hoidke iga õppija tulemus eraldi failis, näiteks `research/oppija-nimi-probleemikandidaadid.md`; nii saab igaüks teha oma PR-i sama faili muutmata.

### 3. Jaga töö Issue'deks ja võrdle kandidaate

Iga õppija kaardistamise Issue on eraldi, kuid kõigil on sama eesmärk ja igaüks vastutab enda töö eest. Kui kõigi õppijate PR-id on üle vaadatud ja ühendatud, looge kandidaatide võrdlemiseks **uus, eraldi meeskonna Issue**.

Seejärel jagage ülejäänud tööd eraldi Issue'deks. Näiteks:

1. kandidaatide võrdlus;
2. valitud probleemi kontrollimine (jagage tegevused õppijate vahel eraldi Issue'deks või määrake igale tegevusele vastutaja);
3. otsuse ja lähteülesande mustand;
4. release'i ettevalmistus.

Igal Issue'l olgu arusaadav pealkiri, kirjeldus, vastutaja ja valmisoleku tingimus. Lisa tahvlile esialgne ajahinnang ning liigu töö käigus `Backlog` → `In progress` → `Review` → `Done`.

Võrrelge tiimis kandidaate: kas inimene ja olukord on selged, kas võimalik mõju on oluline, kas probleem võib korduda, kas seda saab kontrollida ja kas teema mahub kursuse projekti. Valige üks kandidaat, mida edasi uurida. Pange kirja vähemalt üks kõrvalejäetud variant ja valiku põhjus.

### 4. Kontrolli probleemi sõltumatu infoga

Iga õppija vastutab vähemalt ühe kontrolliva tegevuse eest. Jagage tegevused eraldi Issue'deks või märkige iga tegevuse juurde vastutaja. Tehke näiteks lühike vestlus tunniplaani kasutajaga, vaadelge praegust kasutusolukorda või uurige asjakohast usaldusväärset allikat. Küsi inimese tegeliku tegevuse kohta: „Räägi viimasest korrast, kui tunniplaani kasutasid. Mida püüdsid teha? Mis juhtus? Kuidas edasi tegutsesid?”

Kirjuta tulemus üles:

```text
Kontrollitav oletus:
Keda või mida kontrollisime:
Mida küsisime või vaatasime:
Mida teada saime:
Mis jäi teadmata:
Kuidas see muudab meie probleemi kirjeldust:
```

Ära kogu tarbetuid isikuandmeid ega kirjuta vestluspartneri nime avalikku faili. AI võib aidata küsimusi või alternatiivseid tõlgendusi leida, kuid AI vastus ei ole tõend. Kursuse jooksul kasuta AI-d vähemalt ühe olulise otsuse toetamiseks ning dokumenteeri kasutus, kontroll ja tegelik kasu. Kui see pole veel juhtunud, vali sobiv otsus seminaris 2 või 3. Ära sisesta isikuandmeid ega konfidentsiaalset infot.

Kui võtad kasutusele võõra koodi, pildi, fondi või andmed, lisa Issue juurde allika link, litsentsi nimi ja lühike põhjendus, miks kasutamine on lubatud. Ära kasuta materjali enne, kui tingimused on arusaadavad.

### 5. Kirjuta esimene otsus

Kui tiim on kandidaate võrrelnud ja tõendeid arutanud, määrake üks Issue vastutajale, kes koondab ühise otsuse faili `decisions/001-probleemi-valik.md`, kasutades [otsuse malli](../seminarid/mallid/otsus.md). Lisa vähemalt:

- kliendisoovi tõlgendus;
- valitud probleem ja peamine kasutaja;
- kontrollimise viis ja tegelik tulemus;
- kaalutud alternatiivid ning valiku põhjus;
- arendustiimile lähteülesande mustand: kasutaja, probleem, tõendid, soovitud tulemus, esialgne ulatus ja lahtised küsimused.

Probleemiväite vorm:

> **[Kellel]** on olukorras **[kontekst]** raske **[eesmärk]**, sest **[takistus]**. Selle tagajärg on **[mõju]**.

Jäta tõendamata funktsioonid ja kujundusvalikud järgmisse etappi. Kui tulemus infot ei kinnita või muudab probleemi, uuenda otsust ja ütle seda selgelt.

### 6. Tee muudatus oma harus ja ava pull request

Iga õppija teeb enda Issue'ga seotud muudatuse eraldi harus. Alusta värskest `main`-ist ja kasuta enda Issue numbrit ning ingliskeelset kirjeldust:

```bash
git status
git switch main
git pull --ff-only
git switch -c issue-<number>-<short-english-description>
```

- `git status` kontrollib, millises repos ja harus oled ning kas sul on salvestamata muudatusi.
- `git switch main` lülitab töö peaharule.
- `git pull --ff-only` toob GitHubist peaharu viimased muudatused; käsk peatub, kui ajalugu ei saa lihtsalt edasi viia.
- `git switch -c ...` loob uue haru ja lülitab töö sinna. Asenda nurksulgudes osad enda Issue numbri ja lühikese ingliskeelse kirjeldusega.

Individuaalse kaardistamise Issue puhul muuda enda probleemikandidaatide faili, näiteks `research/eesnimi-perenimi-probleemikandidaadid.md`. Ära lisa selle Issue tööna tiimi ühist otsusefaili. Ühise otsuse faili muudab eraldi Issue vastutaja; ülejäänud tiimiliikmed annavad talle oma tõendid ja tagasiside.

Vaata enda faili muudatus enne commit'i üle:

```bash
git status
git add research/eesnimi-perenimi-probleemikandidaadid.md
git diff --cached
git commit -m "Describe timetable use cases"
git push -u origin issue-<number>-<short-english-description>
```

- `git status` näitab muudetud faile.
- `git add <fail>` valib faili, mille muudatused lähevad järgmisse commit'i. Kasuta enda tegelikku failiteed.
- `git diff --cached` näitab valitud muudatusi, et saaksid need enne salvestamist üle vaadata.
- `git commit -m "..."` salvestab valitud muudatused Giti ajalukku. Sõnum on inglise keeles, algab tegusõnaga ja kirjeldab üht sisulist muudatust.
- `git push -u origin <haru>` saadab haru GitHubi. `origin` on GitHubi repo nimi sinu arvutis; `-u` seob kohaliku haru GitHubi haruga. Asenda haru näide enda haru nimega.

Ava GitHubis haru põhjal pull request. Kirjelda, mida muutsid ja miks, lisa `Closes #<number>` ning vali tiimikaaslane ülevaatajaks. Kasuta [pull request'i kontrollnimekirja](../seminarid/mallid/pull-request.md). Ülevaataja kontrollib sisu ja põhjendust. Kui ta palub muudatusi, paranda sama harus, tee uus commit ja push'i uuesti. Pärast heakskiitu ühendatakse PR `main`-i.

Pärast kaaslase muudatuse ühendamist uuenda enda kohalikku peaharu ja loo järgmine haru selle värskest seisust:

```bash
git switch main
git pull --ff-only
```

`git switch main` lülitab sind tagasi peaharule; `git pull --ff-only` toob sinna kaaslase ühendatud muudatused. Enne seda veendu `git status` abil, et sul pole pooleliolevat tööd.

Korda seda iga enda ülesande puhul. Ära tee muudatusi otse `main`-i. Iga käsu tähenduse kohta vaata selle sammu selgitusi ja [näidisõppija tööteekonda](naidisoppija-esimene-iteratsioon.md).

### 7. Valmista ette ja avalda `v0.1.0`

Tiimi repositooriumis peavad enne release'i olema vähemalt:

```text
decisions/001-probleemi-valik.md
releases/v0.1.0.md
reflections/oppija-nimi-v0.1.0.md
README.md
```

Iga õppija kirjutab enda refleksiooni [refleksiooni malli](../seminarid/mallid/individuaalne-refleksioon.md) järgi ja lisab oma Issue, pull request'i ning tehtud ülevaatuse viited. Vahetuv release manager kasutab [release notes'i malli](../seminarid/mallid/release-notes.md), kontrollib ülevaatused ja ühendatud muudatused ning kirjeldab hetke teadmisi, olulisi otsuseid, kontrollitud infot, lahtisi küsimusi ja järgmist sammu.

Refleksioon on iga õppija isiklik töö. Lisa see enda Issue'i ja PR-i kaudu `main`-i; prooviülesande näites lisab õppija selle enda tööharu PR-i. Release manager kontrollib, et kõik refleksioonid on avaldamise ajaks ühendatud.

Kui vajalikud PR-id on ühendatud:

1. Ava GitHubi repositooriumis **Releases → Draft a new release**.
2. Vali **Choose a tag**, sisesta `v0.1.0` ja vali **Create new tag**. Vali sihiks `main`; nii märgib tag viimast kokkulepitud ja ühendatud projektiseisu. Tee seda alles pärast release notes'i PR-i ühendamist.
3. Pane release'i pealkirjaks **Probleem sõnastatud**. Kirjelda lühidalt, mis valmis ja mis jäi lahtiseks, ning lisa link failile `releases/v0.1.0.md`.
4. Kontrolli tag'i, sihti ja kirjeldust ning vajuta **Publish release**.
5. Ava avaldatud release uuesti ja kontrolli, et tag on `v0.1.0` ning otsusefail, release notes ja iga õppija refleksioon on repos olemas.

Tag on Giti märgis kindlale commit'ile; GitHub Release on sellele lisatud avaldatud pealkiri ja kirjeldus. Tag'i loob ainult release manager pärast seda, kui etapi tööd ja release notes on PR-idega `main`-i ühendatud. Kursusel tehakse üks tag iga lõpetatud etapi kohta, mitte iga Issue'i, haru ega commit'i jaoks.

Kasuta kursuse lihtsustatud versioonijada (`vMAJOR.MINOR.PATCH`): `v` tähistab versiooni, esimene number püsib `0` kuni kursuse lõpurelease'ini, keskmine number suureneb iga projektietapiga ja viimane number püsib plaanitud etapi release'il `0`-na. Etappide tag'id on `v0.1.0` (seminar 2), `v0.2.0` (seminar 3), `v0.3.0` (seminar 4), `v0.4.0` (seminar 5) ja `v1.0.0` (eksam). Kui avaldatud etappi tuleb eraldi parandatud väljaandena uuesti avaldada, loo uus parandustag, näiteks `v0.1.1`, ning kirjelda muudatust release notes'is. Ära kasuta vana tag'i uuesti ega liiguta seda teise commit'i peale.

GitHubi nupud võivad muutuda; vaata vajadusel [GitHubi ametlikku release'i loomise juhendit](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

Release fikseerib selle etapi dokumentatsiooni hetkeseisu. See ei tähenda, et valmis veebirakendus oleks ehitatud või et kõik küsimused oleks lahendatud.

### `v0.1.0` kontrollnimekiri

- [ ] Valitud probleem kirjeldab inimest, olukorda, takistust ja mõju.
- [ ] Vähemalt üks sõltumatu kontroll on dokumenteeritud; oletused on faktidest eristatud.
- [ ] Otsusefail sisaldab valikut, alternatiivi, põhjendust ja lähteülesande mustandit.
- [ ] Iga õppija on teinud vähemalt ühe sisulise commit'i ja avanud enda PR-i.
- [ ] Iga õppija on üle vaadanud vähemalt ühe kaaslase PR-i ja vastanud enda töö kommentaaridele.
- [ ] Release notes ja individuaalsed refleksioonid on ühendatud `main`-i.
- [ ] GitHub Release `v0.1.0` on avaldatud.

## Osa 2: alusta järgmist etappi

Kui `v0.1.0` on avaldatud, algab seminari 3 töö, mille lõpptulemus on `v0.2.0`. Ära ava veel `v0.2.0` release'i: tee kõigepealt järgmise etapi esimene ülesanne.

### 8. Vaata üle, mida `v0.1.0` muutis

Loe `releases/v0.1.0.md` ja `decisions/001-probleemi-valik.md`. Märgi tiimiga:

- mida algul arvasite;
- milline tõend või tagasiside teie arusaama muutis;
- mis on endiselt teadmata ja miks see järgmise otsuse jaoks loeb.

Ära muuda varem tehtud otsust märkamatult. Kui uus info muudab probleemi, lisa muudatuse põhjus otsuste logisse.

### 9. Loo seminari 3 esimene Issue ja tee see läbi

Loo GitHub Projecti Issue pealkirjaga näiteks **Vaata üle `v0.1.0` ja jaga seminari 3 rollid**. Määra vastutaja, kirjuta valmisoleku tingimus ja lisa Issue Projecti tahvlile.

Ülesanne on valmis, kui tiim on:

- vaadanud üle `v0.1.0` ja pannud kirja ühe muutunud arusaama ning ühe lahtise küsimuse;
- vahetanud rollid nii, et õppijad võtavad uue professionaalse vaatenurga;
- lisanud `README.md`-sse tiimi praegused rollid ja vastutused;
- avanud muudatuse jaoks pull request'i ning saanud selle kaaslaselt ülevaatuse.

Võta Issue endale, loo uus haru kujul `issue-<number>-review-v010-and-assign-roles`, tee muudatus, kontrolli diff'i, commit'i ingliskeelse sisulise sõnumiga, push'i haru ja ava PR. Näiteks commit'i sõnum: `Add team role assignments`. Lase tiimikaaslasel üle vaadata ja ühenda alles pärast heakskiitu.

Selle ülesande järel on seminari 3 järgmised tööd tööviisi võrdlus, kasutajalood ja süsteemi kontseptsioon. Need koostatakse eraldi Issue'dena ning neist kujuneb `v0.2.0`. Vaata täpseid nõudeid [kodutöö 3 juhendist](../seminarid/seminar_03/homework.md).

## Kui jäid seminarist eemale

Tee kõigepealt iseseisvalt probleemikandidaatide ja otsuse mustand, kuid ära esita väljamõeldud tõendeid päris leidudena. Leppige tiimiga kokku päris kontrolliv tegevus ja vastutaja. Küsi tiimikaaslaselt ligipääsu repositooriumile ja projekti tahvlile, seejärel tee enda töö eraldi harus ja saada PR ülevaatuseks. Kui ligipääs, tõendusallikas või ülevaataja puudub, märgi takistus Issue kommentaari ja lepi õppejõuga kokku, kuidas see lõpetada.
