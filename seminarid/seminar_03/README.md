# Kolmas seminar – 
## Tagasiside kodutöödele
Üks olulisemaid osasid teie kodutöödes läbi kogu õpiaja hakkab olema *codereview*. See on asi, mida ma arvestan ka hindamisel. Mida põhjalikumalt on keegi kellegi teise koodi lugenud ja seejärel seda kommenteerinud, seda parem. Esialgu võib kodutööde all ka niisama lobiseda. Kui ei leia midagi sisulist.  
Siinjuures tõstan esile Pillet, Tanelit, Kasparit (Kiltmaad), Carli, kes leidis, kuidas ka hästi tehtud asja kommida, Silverit, ka Ervit. Helina oli kõvasti kommiteid teinud – kiidan.

## Commitite kirjutamine

[10 Essential Practices for Better Git Commits and Why They Matter](https://medium.com/@saeid/10-essential-practices-for-better-git-commits-and-why-they-matter-3cfc420bf53e)  
[Good Commit ✔ VS. Bad Commit ❌: Best Practices for Git](https://dev.to/sheraz4194/good-commit-vs-bad-commit-best-practices-for-git-1plc)

### Tähendusrikkad kommentaarid
Tähendusrikas kommentaar selgitab muudatuste eesmärki. Väldi ebamääraseid kommentaare nagu "Parandatud vead" või "Tehtud muudatused". Selle asemel kasuta lühidat ja kirjeldavat kommentaari, mis illustreerib commit-i eesmärki ja tulemust.

**Tee:**  
"Add user profile image upload functionality"  
"Fix broken navigation links in header menu"

**Ära tee:**  
"Updated code"  
"Typo fixes"

Soovitused:  
- Alusta suure tähega
- Kasuta käskivat kõneviisi ("Add" mitte "Added", "Change" mitte "Changed") 
- Piira pealkirja umbes 50 tähemärgini
- Kui on vaja rohkem detaile, eralda pealkiri tühja reaga ja lisa põhjalikum kirjeldus, murdepunktiga umbes 72 tähemärgi juures

**Miks peaks kasutama käskivat kõneviisi?**

Commiti kommentaarides on soovituslik kasutada käskivat kõneviisi ("lisa", "paranda", "uuenda") mitte minevikuvormi ("lisasin", "parandasin", "uuendasin") mitmel põhjusel:

Järjepidevus: Commit kirjeldab, mida see commit teeb koodiga, mitte mida sina tegid. See on nagu käsklus või samm-sammuline juhend.
Lühidus: Käskiv vorm on tavaliselt lühem.

```bash
docs: add correction  // 3 sõna
docs: added correction  // 3 sõna, aga pikem
```
Rahvusvaheline tava: See järgib Git'i enda dokumentatsiooni ja commiti stiili. Inglise keeles kirjutatakse "add", "fix", "update" mitte "added", "fixed", "updated".
Loetavus changelogides: Kui vaatad commit ajalugu või changelog'i, siis käskiv vorm loeb paremini:

- add authentication
- fix login error 
- update documentation  
**vs**  
- added authentication
- fixed login error
- updated documentation

**Aga see on siiski konventsioon - kui sinu tiim või projekt eelistab minevikuvormi, siis võib ka seda kasutada. Peamine on järjepidevus projekti piires.**

### Maini pileti numbrit
Kui kasutad ülesannete/piletite haldamise süsteemi (nagu GitHub või Jira), on kasulik viidata commitis pileti numbrile. See loob selge seose commit-i ja seotud pileti või vea vahel.

**Tee:**  
"Implement password reset functionality, resolves #234"  
"Add dark mode theme support, closes #567"

**Ära tee:**  
"Fixed annoying bug"  
"Fixed user interface"

**Soovitused:**  
- Kasuta standardset terminoloogiat nagu "fixes", "closes" või "resolves" ülesande numbrile viitamisel. Paljud platvormid nagu GitHub tunnevad need ära ja seovad automaatselt commit-id mainitud ülesannetega ning võivad need isegi sulgeda, kui commit liidetakse.

### Regulaarsed commit-id
Regulaarne commit-imine on oluline. See tagab, et muudatused on järkjärgulised ja hallatavad, võimaldades lihtsamat ülevaatust, vigade otsimist ja vajadusel tagasipööramist.

**Tee:**  
- Tee commit, kui oled lõpetanud ühe loogilise muudatuse, isegi kui see on väike.

**Ära tee:**  
- Oota, et koguda palju mitteseotud muudatusi ühte suurde commit-i.

**Soovitused:**
- Mõtle igast commit-ist kui peatükist loos. Iga peatükk peaks olema arusaadav iseseisvalt.
- Väldi mitme mitteseotud muudatuse lisamist ühte commit-i. See teeb keeruliseks iga muudatuse eesmärgi jälgimise ja raskendab protsessi, kui on vaja tagasi pöörata.
- Kui leiad end kasutamas "ja" commit-i pealkirjas, mõtle, kas sinu commit sisaldab mitteseotud muudatusi.

### Kasuta atomaarseid commit-e
Atomaarne commit tähendab, et üks commit esindab ainult ühte konkreetset muudatust. See ei tähenda, et muudetud on ainult üks fail või isegi üks rida, vaid pigem ühte "loogilist" muudatust. Atomaarsed commit-id teevad lihtsamaks muudatuste mõistmise, vigade otsimise ja võimalike probleemide tuvastamise.

**Soovitused:**
- Enne commit-i tegemist vaata muudatused üle käsuga `git diff`
- Kui muudatused hõlmavad mitut valdkonda või funktsionaalsust, kasuta käsku `git add -p` muudatuste tükkhaaval lisamiseks. Käsu kasutamine käib nii:

1. Sisesta käsk `git add -p`
2. Git näitab sulle esimest muudatuste tükki ja küsib, mida sellega teha
3. Sul on järgmised valikud:
   - `y` - lisa see tükk (yes)
   - `n` - jäta see tükk lisamata (no) 
   - `s` - jaga tükk väiksemateks osadeks (split)
   - `q` - välju, ära lisa rohkem tükke (quit)
   - `?` - näita kõiki võimalikke valikuid (help)
4. Vasta igale tükile kas `y` või `n`, kuni kõik muudatused on üle vaadatud
5. Seejärel saad teha commit-i ainult valitud muudatustega

See on eriti kasulik, kui oled teinud mitu erinevat muudatust samas failis, aga soovid need eraldi commit-idesse panna.

## Konventsionaalsete commit-ide kirjutamise reeglid:
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)  
[Conventional Commit Specification](https://pranaybathini.medium.com/conventional-commit-specification-ecd701b0bbb2)  
[Writing a Good Git Commit Message](https://www.gitkraken.com/learn/git/best-practices/git-commit-message)  

Üldine loogika on järgmine:  
Selmet kirjutada:
```Bash
git commit -m "fixed login error"
```
kirjuta arusaadavam kommentaar:
```Bash
git commit -m "fix(auth): improve login error handling"
```

### Peamised
#### Fix
Fix-tüüpi commit-e kasutatakse koodibaasis esinevate vigade või probleemide lahendamiseks.

```Bash
$ git commit -m "fix: resolve issue with form submission not triggering validation"
$ git commit -m "fix(login): improve login error handling"
```

#### Feat
Seda kasutatakse projektile lisatud uute funktsioonide jaoks.

```Bash
$ git commit -m "feat: introduce real-time notifications for new messages"
$ git commit -m "feat(css): add mobile view layout"
$ git commit -m "feat(styles): add modal window animations"
```

#### Breaking Change
Breaking change ehk väga oluline muudatus tähistab commit-i, mis muudab API-t või funktsionaalsust viisil, mis ei ole tagasiühilduv. Selliseid muudatusi saab tähistada kas hüüumärgiga (!) või BREAKING CHANGE: märkega commit-i kirjelduses.

Näited hüüumärgiga:
```Bash
$ git commit -m "feat!: remove support for IE11"
$ git commit -m "feat: remove support for IE11"
$ git commit -m "BREAKING CHANGE: remove support for IE11"
$ git commit -m "feat(api): remove support for IE11"
```

**Üldjuhul nendest peakski piisama.**

### Muud

#### Chore
Chore-tüüpi commit-e kasutatakse regulaarsete hooldustööde jaoks, nagu sõltuvuste uuendamine, paketihaldurite konfiguratsioonid või muud ülesanded, mis ei muuda lähtekoodi ega mõjuta rakenduse käitumist.

```Bash 
$ git commit -m "chore: clean up unused dependencies from package.json"
```

#### Docs
Commit-id, mis hõlmavad ainult dokumentatsiooni muudatusi, nagu README failide uuendamine, kommentaaride lisamine või funktsioonide või klasside dokumentatsiooni kirjutamine.

```Bash
$ git commit -m "docs: add auth service instructions to README"
```

#### Build
Seda tüüpi kasutatakse muudatuste jaoks, mis mõjutavad ehitussüsteemi või väliseid sõltuvusi. Näiteks kui uuendad teeki või muudad ehituse konfiguratsioone, kuulub see sellesse kategooriasse.

```Bash
$ git commit -m "build: update webpack configuration"
$ git commit -m "build: update Hive Maven dependency to version 3"
```

#### CI
Commit-id, mis on seotud pideva integratsiooni konfiguratsioonide või skriptidega. See hõlmab muudatusi automatiseerimiseks ja testimiseks kasutatavates tööriistades ja protsessides.

```Bash
$ git commit -m "ci: add vault stage to gitlab ci pipeline to fetch api secrets"
```

#### Performance
Commit-id, mis parandavad koodibaasi jõudlust ilma selle välist käitumist muutmata. Optimeerimisega seotud muudatused kategoriseeritakse jõudluse parendustena.

```Bash
$ git commit -m "perf: optimize guest misconduct database search by reservation for faster retrieval"
```

#### Refactor
Refaktoreerimise commit-id hõlmavad koodi muudatusi, mis ei paranda viga ega lisa funktsionaalsust. Refaktoreerimine on suunatud koodi struktuuri, loetavuse või hooldatavuse parandamisele ilma selle välist käitumist muutmata.

```Bash
$ git commit -m "refactor: simplify validation logic in user registration"
$ git commit -m "refactor(validation): improve user registration validation logic"
```

#### Revert
Revert-tüüpi commit-e kasutatakse varasemate muudatuste tagasipööramiseks. On oluline mainida commit-i kommentaaris tagasipööratavate muudatuste commit-i ID või pealkiri.

```Bash
$ git commit -m "revert: revert changes made in commit abc123"
```

#### Style
Commit-id, mis on seotud koodi stiili ja vormindamisega. See võib hõlmata taandamise muudatusi, koodi ümbervormindamist või muutujate ümbernimetamist koodistandardite järgimiseks.

```Bash
$ git commit -m "style: format code according to linting rules"
$ git commit -m "style(css): add header hover effect"
$ git commit -m "style(navbar): update button colors and borders"
```


#### Test
Commit-id, mis lisavad või muudavad teste. See hõlmab ühikteste, integratsiooniteste või mis tahes muud tüüpi automatiseeritud testimist.

```Bash
$ git commit -m "test: add unit tests for authentication service"
```
Nagu näed, siis ilme tüübi eesliiteta, soovitatakse alustada lauset suure algustähega, kuid  eesliite puhul kirjutatakse kõik väiksega. 
Tüübi eesliide (feat:, fix:, jne) annab juba struktuuri.  
Väiketähed säilitavad visuaalse ühtsuse eesliitega.  
See on osa formaalsest spetsifikatsioonist.  

**Tavaliste Git-i commit-ide puhul:**  
Suure algustähega alustamine järgib standardset eesti keele lauseehitust.  
See aitab eristada sõnumi algust.  
See on pikaajaline Git-i tava, mida näeb Git-i enda dokumentatsioonis ja paljudes suurtes projektides.  
Muudab sõnumi git log vaates paremini loetavaks.  

## Litsentsid
### Üldine autoriõguse loogika:
Kui teosel pole märgitud litsentsi, siis järelikult on ta litsentsitud kõige tugevamalt ja sa ei tohi teost jagada. Seega, kui sa tahad, et sinu materjal oleks kasutatav, pead lisama litsentsi.

### Litsentsid Githubis

Kõik GitHubis leiduvad populaarsed litsentsid on loodud selleks, et võimaldada tarkvara jagamist ja levitamist, kuid iga litsents seab sellele tegevusele erinevad tingimused.

#### Miks ei ole Githubis täielikult keelavaid litsentse?

- Avatud lähtekoodi põhimõtted: GitHub on platvorm, mis on loodud avatud lähtekoodiga projektide jaoks. Seetõttu ei ole seal koht litsentsidele, mis täielikult keelavad jagamise.
- Litsentside eesmärk: Litsentsid on loodud selleks, et määratleda, kuidas tarkvara võib olla kasutatav ja levitatav. Nende eesmärk ei ole keelata jagamist, vaid reguleerida seda.

#### Mida erinevad litsentsid reguleerivad?

- Muudatuste tegemine: Mõned litsentsid nõuavad, et kõik muudatused peavad olema samuti avalikult kättesaadavad (näiteks GPLv3).
- Kommertsialiseerimine: Mõned litsentsid seavad piirangud tarkvara kommertsialiseerimisele (näiteks GPLv3).
- Autorite õigused: Kõik litsentsid kaitsevad tarkvara autori intellektuaalomandit.

Kõik GitHubis leiduvad populaarsed litsentsid võimaldavad mingil määral tarkvara jagamist. Kui soovid täielikult keelata jagamise, siis GitHub ei ole selleks õige platvorm. Kui soovid täielikult keelata jagamise, siis hoia seda privaatsena.

#### Valik Githubi litsentse:

- Apache 2.0 - Lubab vabalt kasutada, muuta ja jagada tarkvara, kuid nõuab autoriõiguste märget. Kaitseb patendikasutust.

- GNU General Public License v3.0 - Tagab tarkvara vabaduse, nõuab et tuletatud teosed oleksid sama litsentsi all. Sisaldab patendikaitse ja DRM-i piiranguid.

- MIT License - Väga lihtne ja vaba litsents, mis lubab peaaegu kõike, nõudes vaid autoriõiguste säilitamist ja vastutusest loobumise märget.

- BSD 2-Clause "Simplified" License - Lihtne litsents, mis lubab vaba kasutust tingimusel, et säilitatakse autoriõiguste teade ja vastutusest loobumine.

- BSD 3-Clause "New" or "Revised" License - Sarnane 2-Clause versioonile, kuid lisab klausli, mis keelab kasutada autorite nimesid toodete reklaamimiseks.

- Boost Software License 1.0 - Lihtne ja vaba litsents, mis lubab kasutada lähtekoodi nii avatud kui suletud lähtekoodiga projektides.

- Creative Commons Zero v1.0 Universal - Loobub kõigist autoriõigustest võimalikult suures ulatuses, viies teose avalikku omandisse.

- Eclipse Public License 2.0 - Võimaldab kommertskasutust ja muutmist, kuid nõuab lähtekoodi avaldamist muudatuste korral.

- GNU Affero General Public License v3.0 - Sarnane GPLv3-le, kuid nõuab lähtekoodi avaldamist ka võrgupõhiste rakenduste puhul.

- GNU General Public License v2.0 - GPLv3 varasem versioon, mis tagab tarkvara vabaduse ja nõuab tuletatud teoste avaldamist sama litsentsi all.

- GNU Lesser General Public License v2.1 - Võimaldab linkida LGPL-tarkvaraga ka mittevaba tarkvara, säilitades teegi enda vabaduse.

- Mozilla Public License 2.0 - Võimaldab lähtekoodi kasutamist nii avatud kui suletud projektides, kuid nõuab MPL-koodi muudatuste avaldamist.

- The Unlicense - Loobub täielikult autoriõigustest ja viib teose avalikku omandisse, lubades piiranguteta kasutust.


#### [Kolm peamist litsentsi tüüpi GitHubis:](https://gist.github.com/nicolasdao/a7adda51f2f185e8d2700e1573d8a633#3-main-types-of-open-source-licenses)

**MIT License:**

Lihtne ja paindlik: See on kõige minimalistlikum litsents, mis võimaldab kasutajatel vabalt kasutada, muuta ja levitada tarkvara, ilma et nad peaksid oma muudatusi avaldama.
See on tüüpi "Tee minu asjadega, mida tahad, aga ära mind kohtusse kaeba".  
Tegemist on lubava vaba tarkvara litsentsiga.  
Vali see, kui kardad, et keegi ei hakka sinu tarkvara kasutama.  
MIT litsents on üldjoontes sarnane BSD ja ISC litsentsidega.  

**Apache License 2.0:**

Sama mis MIT litsents, aga rohkemate sõnadega. Suurepärane juristidele :)  
Tasakaal patentõiguste ja vaba tarkvara vahel: võimaldab kasutajatel vabalt kasutada, muuta ja levitada tarkvara, kaitstes samal ajal tarkvara autori intellektuaalomandit.  
Populaarne suurtes projektides, nt nagu Apache HTTP Server.
Vali see MIT litsentsi asemel, kui kardad patenditrollimist.

**GNU General Public License v3.0 (GPLv3):**

Karmim litsents: GPLv3 on üks karmimatest vabavaralitsentsidest, mis nõuab, et kõik tuletised peavad olema samuti vabavaralised.  
Populaarne vabavaralistes projektides: See litsents on populaarne vabavaralistes projektides, nagu GNU/Linux ja LibreOffice.  
Vali see, kui kardad, et inimesed kasutavad sinu tööd ebaausalt (nt kui sind häirib, et keegi võiks sinu arvelt raha teenida). Kui nad kasutavad sinu tarkvara, peavad nad kasutama sama litsentsi nagu sina (st tõenäoliselt muutma selle avatud lähtekoodiga tarkvaraks).
Lühidalt öeldes: kui keegi loob sinu tööst tuletatud teose ja levitab seda teatud tingimustel, peab ta avaldama lähtekoodi sama litsentsi alusel.
See on copyleft-litsents (vastandina copyright'ile).
Näiteks üks põhjustest, miks Apple'i Mac OS ei põhine Linuxil, on see, et Linux kasutab GPL litsentsi, mis tähendaks, et ka OSX oleks pidanud olema avatud lähtekoodiga.
Paljudele idufirmadele ei meeldi GPL litsents, kuna see võib väljumise ajal tõsiseid probleeme tekitada. Harva leidub investoreid, kes sooviksid osta midagi, mille nad on sunnitud avatud lähtekoodiga muutma.

#### Valiku kriteeriumid:

**Valides litsentsi oma projektile, tuleb arvestada järgmiste kriteeriumidega:**

- Vabadus: Kui soovid, et teised saaksid vabalt kasutada, muuta ja levitada su tarkvara, siis vali vaba litsents, nagu MIT, Apache või GPL.
- Intellektuaalomand: Kui soovid kaitsta oma intellektuaalomandit, siis vali litsents, mis võimaldab sul säilitada oma õigused, näiteks Apache License 2.0.
- Kasutajate vajadused: Mõtle, kuidas soovid, et teised kasutaksid su tarkvara. Kas soovid, et nad saaksid muuta ja levitada su tarkvara vabalt, või soovid piirata nende võimalusi?

Kui muu ei aita litsentsi valida, siis kasuta abimeest:  
https://choosealicense.com

