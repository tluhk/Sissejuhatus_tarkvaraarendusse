# DevOps

**DevOps** - (**Dev**elopment and IT **Op**erations) on üldine termin, mis hõlmab kontseptsioone ja praktilisi meetodeid, mille eesmärk on parandada igasuguste IT-lahenduste arendus- ja rakendusprotsesse [1](https://arxiv.org/ftp/arxiv/papers/1907/1907.10201.pdf). Selle jaoks teevad arendajad ja süsteemiadministraatorid igas arendustsükli etapis tihedat koostööd tootlikkuse parandamiseks, infrastruktuuri automatiseerimiseks ja rakenduse jõudluse pidevaks mõõtmiseks. [5](https://techacute.com/what-is-devops/).

# Ajalugu

DevOps sai alguse aastal 2007, kui Patrick Debois sai aru, et siiamaani kasutusel olevad IT-lahenduse arendusmetoodikad ei saa tagada piisavat kommunikatsiooni arenduse ja rakendamise eest vastutavate üksuste vahel. Tema koos teistega hakkas mõtlema kuidas saab kõrvaldada tõkkeid, millega puutusid kokku IT meeskonnad ning kuidas tõhustada tiimidevahelist koostööd ja kommunikatsiooni.  
Aastal 2009 Patrick Debois korraldas esimest **DevOpsDays** konverentsi Belgias. Sealt sai DevOps oma nime.  
Aastal 2010 ilmus Jez Humble ja David Farley poolt kirjutatud raamat _Continuous Delivery_, kus nad sätestasid põhimõtted ja tehnilised võtted, mis võimaldavad kvaliteetsete ja väärtuslike uute funktsioonide kiiret järkjärgulist tarnimist kasutajatele.  
Aastal 2015 sai alguse startup nimega DORA (_DevOps Research and Assessment_), loodud Dr. Nicole Forsgren, Gene Kim, and Jez Humble poolt. Selle ülesandeks oli koostada kõige ulatuslikumad DevOpsi rakendamise uuringuid nimega _State of DevOps Report_.  
Aastal 2016 ilmus Gene Kim, Jez Humble, Patrick Debois ja John Willis poolt kirjutatud raamat _The DevOps Handbook_, millest sai praktiline juhend DevOps kontseptsioonide rakendamiseks. [2](https://www.coursera.org/lecture/intro-to-devops/brief-history-of-devops-vBgDl)  

# DevOps meetodid

Organisatsioonid kasutavad arendus ja tooteväljaannete kiirendamiseks ja täiustamiseks agiilseid meetodeid.
Kolm populaarsemat DevOps meetodit on:
* Scrum - Scrumis kasutatakse töövoogu, millel on spetsiifilised terminoloogiad, nagu sprint, standup (igapäevane koosolek), ja määratud rollid, nagu Scrum Master, tooteomanik jne.
* Kanban - Projekti progressi hinnatakse Kanban paneeli järgi.
* Agiilne - Mõned agiilse arenduse tavad on suurem reageerimine vajaduste ja nõuete muutustele, nõuete dokumenteerimine kasutajalugudena, standupid ja pidev suhtlus kliendiga.  [6](https://www.netapp.com/devops-solutions/what-is-devops/)

# Rakenduse elutsükli ülevaade

Traditsiooniliselt ühe IT-lahenduse teekond koosneb teatud etappidest, mis on enam-vähem samad sõltumata sellest, millega konkreetselt on tegu. Iga arendusprotsess algab planeerimisest ja lõppeb lahenduse üleandmisega kliendile/lõppkasutajale ning selle protsessi läbiviimiseks on olemas erinevaid lähenemisviise, näiteks _Waterfall_ või _Agile_.  
Olulised sammud eduka lahenduse elutsüklis on planeerimine (vajaduste/võimekuste/ressurside kaardistamine), arendus, testimine, valmisehitamine ja kasutuselevõtmine. Peale seda algab toe pakkumine, näiteks uute vigade parandus ja paranduste sisseviimine (versioonid), optimeerimine, monitoorimine jne. Üldiselt sellist pidevat protsessi nimetatakse _Continuous Development_, ehk pidev areng ning see lõppeb ainult siis, kui lahendust enam ei kasutata. DevOps-i ülesanne on tagada, et pidev arengu protsess oleks efektiivne, kiire ja tagaks võimalikult kõrget kvaliteeti. [3](https://youtu.be/0yWAtQ6wYNM)  

# Probleemid / teetõkked

Kõige sagedamini arendusprotsessi jagatakse kahe meeskonna vahel - arendajad (Development) ja rakendajad (Operations) ning igal meeskonnal on oma ülesanded: arendusmeeskonna peamine ülesanne on võimalikult kiiresti lisada rakendusele uued funktsionaalsused ja parandada vead ning rakendusmeekonna peamine ülesanne on tagada rakenduse stabiilset ja turvalist funktsioneerimist. Sellise meeskonna jaoks on väga oluline omavaheline kommunikatsioon, muidu vastasel juhul üks pool ei mõista seda, mis teeb teine pool ning arendusprotsessi on võimatu jälgida/planeerida ja uute paranduste sisseviimine võtab liiga palju aega. [3](https://youtu.be/0yWAtQ6wYNM)  

# DevOps plussid / eelised

DevOpsil on mitmeid ärilisi ja tehnilis eeliseid vanemate arendusmudelite ees. Näiteks:
* Kiirem ja parem toote turule toomine 
* Kiirem probleemide lahendamine 
* Suurem mastaapsus ja kättesaadavus
* Stabiilsem töökeskkond
* Parem ressursside kasutamine
* Automatiseerimine
* Süsteemi tulemuste läbipaistvus
* Suurem innovatsioon [6](https://www.netapp.com/devops-solutions/what-is-devops/)

# DevOps ülesanded / lahendused

DevOps-i põhimõte on rakendada meeskonnatöös erinevaid metoodikaid, printsiipe ja tööristaid, mis aitavad meeskonnaliikmetel teineteisest paremini aru saada ning automatiseerida teatuid protsesse, et neid kiirendada. Kuna DevOps on katusetermin, erinevad IT-ettevõtted rakendavad seda omamoodi. Mõned väljakujunenud tendentsidest on mikroteenuste kasutamine, pilvandmetöötlus, CI/DC (_Continuous Integration / Continuous Development_) ja muud teised. [3](https://youtu.be/0yWAtQ6wYNM)  
CI/CD on automatiseerimise protsess, mille tagajärjel iga jupp uut koodi saab kohe automaatselt testida ning koheselt ka kasutusele võtta, kui automaatsed kontrollid on läbitud. See võimaldab viia rakenduse sisse parandusi kasvõi mitu korda päevas ilma, et see ohustaks rakenduse pidevat funktsioneerimist. [4](https://circleci.com/continuous-integration/#continuous-integration-ci-vs-continuous-deployment-cd)

# DevOps meeskond ja meeskonnaliikmete rollid
## DevOps insener

DevOps insener vastutab õige infrastruktuuri kujundamise eest, et meeskond saaks tooteid luua ja neid tarnida. Alates toote loomisest, testimisest, juurutamisest ja jälgimisest integreerib insener kõik toote elutsükli igas etapis vajalikud ressursid ja funktsioonid, kaitstes samal ajal pilvearhitektuuri häkkimisrünnakute eest. Lisaks tegeleb insener meeskonna koosseisu, projektitegevustega, CI/CD pipelineide ja välisliideste protsesside määratlemise ja seadistamisega. [7](https://www.clickittech.com/devops/devops-team/)

## Release manager

Release manager vastutab kogu väljalaske elutsükli eest alates kavandamisest, ajakavast, automatiseerimisest ja pidevate tarnekeskkondade haldamisest. Väljalaskehaldurid keskenduvad enamasti operatsioonidele, kus nad kavandavad automatiseerimiskonveieri koodi sujuvaks edenemiseks tootmisse, jälgivad tagasisidet, aruandeid ja kavandavad järgmist väljalaset, töötades lõputu tsüklina. [7](https://www.clickittech.com/devops/devops-team/)

## DevOps arhitekt

DevOpsi arhitekti ülesanne on analüüsida olemasolevaid tarkvaraarendusprotsesse ja luua optimeeritud DevOps CI/CD torujuhe, et tarkvara kiiresti ehitada ja tarnida. Arhitekt analüüsib olemasolevaid protsesse ja rakendab parimaid tavasid protsesside sujuvamaks muutmiseks ja automatiseerimiseks, kasutades õigeid tööriistu ja tehnoloogiaid. Lisaks jälgib ja juhib ta tehnilisi toiminguid, teeb koostööd arendajate ja opsidega ning pakub vajadusel tuge. Samuti tegutseb ta vastavalt vajadusele juhina. [7](https://www.clickittech.com/devops/devops-team/)

## Turbe- ja vastavusinsener

Turva- ja vastavusinsener (SCE) vastutab DevOpsi keskkonna üldise turvalisuse eest. SCE teeb tihedat koostööd arendusmeeskondadega, et kavandada ja integreerida turvalisus CI/CD pipelinei, tagades, et andmete terviklikkust ja turvalisust ei ohustata toote elutsükli üheski etapis. Lisaks tagab SCE, et arendatavad tooted vastavad kehtivatele eeskirjadele ja vastavusstandarditele. [7](https://www.clickittech.com/devops/devops-team/)

## Tarkvara arendaja/testija

Kui tavaline tarkvaraarendaja kirjutab toote koostamiseks koodi, siis DevOpsi tarkvaraarendaja/testija on kaasatud kogu toote elutsükli jooksul. DevOpsi arendajate kohustuste hulka kuuluvad sellised ülesanded nagu koodi värskendamine, uute funktsioonide lisamine ja vigade lahendamine, selliselt, et rakendus vastab ärinõuetele. Lisaks viib arendaja läbi unit teste, lükkab koodi tootmisse ja jälgib selle toimivust. [7](https://www.clickittech.com/devops/devops-team/)

## DevOps evangelist

Tema juhib DevOpsi teekonda, tagades, et organisatsioonis toimub kultuuriline nihe, kõik on teadlikud oma rollidest ja vastutusest, leiavad viise protsesside optimeerimiseks ja tagab parimate tavade rakendamise kogu tootearenduse elutsüklis.
[7](https://www.clickittech.com/devops/devops-team/)

Credits: Tiina O. ja Pavel I.