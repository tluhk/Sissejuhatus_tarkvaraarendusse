# Kolmas seminar – 
## Tagasiside kodutöödele
Üks olulisemaid osasid teie kodutöödes läbi kogu õpiaja hakkab olema *codereview*. See on asi, mida ma siin arvestan ka hindamisel. Mida põhjalikumalt on keegi kellegi teise koodi lugenud ja seejärel seda kommenteerinud, seda parem. Esialgu võib seal kasama lällata.  
Siinjuures tõstan esile Pillet, Tanelit, Kasparit (Kiltmaad), Carli, kes leidis, kuidas ka hästi tehtud asja kommida, Silverit, ka Ervit. Helina oli kõvasti kommiteid teinud – kiidan.

## Commitite kirjutamine


https://medium.com/@saeid/10-essential-practices-for-better-git-commits-and-why-they-matter-3cfc420bf53e
https://dev.to/sheraz4194/good-commit-vs-bad-commit-best-practices-for-git-1plc

### Tähendusrikkad sõnumid
Tähendusrikas commit-sõnum selgitab muudatuste eesmärki. Väldi ebamääraseid sõnumeid nagu "Parandatud vead" või "Tehtud muudatused". Selle asemel kasuta lühidat ja kirjeldavat sõnumit, mis illustreerib commit-i eesmärki ja tulemust.

Tee:
"Add user profile image upload functionality"
"Fix broken navigation links in header menu"

Ära tee:
"Updated code"
"Typo fixes"

Soovitused:
- Alusta suure tähega
- Kasuta käskivat kõneviisi ("Add" mitte "Added", "Change" mitte "Changed") 
- Piira pealkirja umbes 50 tähemärgini
- Kui on vaja rohkem detaile, eralda pealkiri tühja reaga ja lisa põhjalikum kirjeldus, murdepunktiga umbes 72 tähemärgi juures

### Maini ülesande numbrit
Kui kasutad ülesannete haldamise süsteemi (nagu GitHub või Jira), on kasulik viidata commit-sõnumis ülesande numbrile. See loob selge seose commit-i ja seotud ülesande või vea vahel.

Tee:
"Implement password reset functionality, resolves #234" 
"Add dark mode theme support, closes #567"

Ära tee:
"Parandatud tüütu viga"
"Parandatud kasutajaliides"

Soovitused:
- Kasuta standardset terminoloogiat nagu "fixes", "closes" või "resolves" ülesande numbrile viitamisel. Paljud platvormid nagu GitHub tunnevad need ära ja seovad automaatselt commit-id mainitud ülesannetega ning võivad need isegi sulgeda, kui commit liidetakse.

### Regulaarsed commit-id
Regulaarne commit-imine on oluline. See tagab, et muudatused on järkjärgulised ja hallatavad, võimaldades lihtsamat ülevaatust, vigade otsimist ja vajadusel tagasipööramist.

Tee:
- Tee commit, kui oled lõpetanud ühe loogilise muudatuse, isegi kui see on väike.

Ära tee:
- Oota, et koguda palju mitteseotud muudatusi ühte suurde commit-i.

Soovitused:
- Mõtle igast commit-ist kui peatükist loos. Iga peatükk peaks olema arusaadav iseseisvalt.
- Väldi mitme mitteseotud muudatuse lisamist ühte commit-i. See teeb keeruliseks iga muudatuse eesmärgi jälgimise ja raskendab protsessi, kui on vaja tagasi pöörata.
- Kui leiad end kasutamas "ja" commit-i pealkirjas, mõtle, kas sinu commit sisaldab mitteseotud muudatusi.

### Kasuta atomaarseid commit-e
Atomaarne commit tähendab, et üks commit esindab ainult ühte konkreetset muudatust. See ei tähenda, et muudetud on ainult üks fail või isegi üks rida, vaid pigem ühte "loogilist" muudatust. Atomaarsed commit-id teevad lihtsamaks muudatuste mõistmise, vigade otsimise ja võimalike probleemide tuvastamise.

Soovitused:
- Enne commit-i tegemist vaata muudatused üle käsuga git diff
- Kui muudatused hõlmavad mitut valdkonda või funktsionaalsust, kaalu tükkide või üksikute failide lisamist käskudega git add -p või git add <failinimi>

## Konventsionaalsete commit-ide kirjutamise reeglid:
https://pranaybathini.medium.com/conventional-commit-specification-ecd701b0bbb2
https://www.conventionalcommits.org/en/v1.0.0/

### Peamised
#### Fix
Fix-tüüpi commit-e kasutatakse koodibaasis esinevate vigade või probleemide lahendamiseks. Kui commit käsitleb probleemi või viga, kuulub see sellesse kategooriasse.

```Bash
$ git commit -m "fix: resolve issue with form submission not triggering validation"
$ git commit -m "fix(login): improve login error handling"
```

#### Feat
Seda tüüpi kasutatakse projektile lisatud uute funktsioonide jaoks. Kui lisad uue funktsionaalsuse või võimalused, loetakse seda funktsiooniks.

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

Üldjuhul nendest peakski piisama.

### Muud

#### Build
Seda tüüpi kasutatakse muudatuste jaoks, mis mõjutavad ehitussüsteemi või väliseid sõltuvusi. Näiteks kui uuendad teeki või muudad ehituse konfiguratsioone, kuulub see sellesse kategooriasse.

```Bash
$ git commit -m "build: update webpack configuration"
$ git commit -m "build: update Hive Maven dependency to version 3"
```

#### Chore
Chore-tüüpi commit-e kasutatakse regulaarsete hooldustööde jaoks, nagu sõltuvuste uuendamine, paketihaldurite konfiguratsioonid või muud ülesanded, mis ei muuda lähtekoodi ega mõjuta rakenduse käitumist.

```Bash 
$ git commit -m "chore: clean up unused dependencies from package.json"
```

#### CI
Commit-id, mis on seotud pideva integratsiooni konfiguratsioonide või skriptidega. See hõlmab muudatusi automatiseerimiseks ja testimiseks kasutatavates tööriistades ja protsessides.

```Bash
$ git commit -m "ci: add vault stage to gitlab ci pipeline to fetch api secrets"
```

#### Docs
Commit-id, mis hõlmavad ainult dokumentatsiooni muudatusi, nagu README failide uuendamine, kommentaaride lisamine või funktsioonide või klasside dokumentatsiooni kirjutamine.

```Bash
$ git commit -m "docs: add auth service instructions to README"
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
Revert-tüüpi commit-e kasutatakse varasemate muudatuste tagasipööramiseks. On oluline mainida commit-i sõnumis tagasipööratavate muudatuste commit-i ID või pealkiri.

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



