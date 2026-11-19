# Sissejuhatus tarkvaraarendusse: konspekt

> [!IMPORTANT]
> Konspekt on koostamisel ja hakkab kehtima 2027/2028. õppeaastal. Seni kehtivad seminaride materjalid ja kaust [`concepts/`](../concepts/).

See konspekt koondab kursuse põhimõisted ja juhised ühte kohta. Osad järgivad seminaride järjekorda, sest iga seminar toetub eelmise seminari oskustele. Konspekt ei asenda seminari materjali: konkreetsed ülesanded, kodutööd ja tähtajad on seminaride kaustades.

## Kuidas konspekti kasutada

Loe osad läbi järjekorras. Iga osa algab ülevaatega, kus on kirjas osa põhiküsimus, mida sa õpid ja mida peaksid eelmisest osast juba oskama. Iga lehe lõpus on lingid eelmisele ja järgmisele lehele.

Iga lehe juures on märge, mis näitab, kuidas see leht seminariga seotud on:

| Märge | Tähendus |
|---|---|
| **Seminaris** | Teemat käsitletakse seminaris ja harjutatakse koos. Võid lehe läbi lugeda enne või pärast seminari. |
| **Enne seminari** | Loe leht enne seminari läbi. Seminar eeldab, et teema on sulle tuttav. |
| **Iseseisev** | Seminaris seda teemat ei käsitleta, kuid see kuulub kursuse põhimõistete hulka. Loe iseseisvalt. |

Ingliskeelsed erialaterminid on toodud eestikeelse termini kõrval, sest tööriistades ja dokumentatsioonis kohtad neid inglise keeles. Mõistete lühikesed selgitused leiad sõnastikust.

## Sisukord

### [1. Suur pilt ja töövahendid](01-big-picture-and-tools/README.md)

Põhiküsimus: mis on tarkvaraarendus ja milliste tööriistadega seda tehakse?

| Leht | Sisu | Märge |
|---|---|---|
| [Tarkvara ja tarkvaraarendus](01-big-picture-and-tools/01-software.md) | Mis on tarkvara, tarkvara tüübid, tarkvaraarendus ei võrdu programmeerimisega | Seminaris |
| [Tarkvaraarenduse elutsükkel ja AI](01-big-picture-and-tools/02-sdlc-and-ai.md) | Elutsükli etapid, Waterfall ja agiilne arendus, AI roll ja riskid | Seminaris |
| [IDE ja terminal](01-big-picture-and-tools/03-ide-and-terminal.md) | IDE, VS Code, terminal, käsukest, Git Bash | Seminaris |
| [Git ja GitHub](01-big-picture-and-tools/04-git-and-github.md) | Versioonihaldus, Giti ja GitHubi erinevus, HTTPS, GitHub CLI | Seminaris |
| [Markdown](01-big-picture-and-tools/05-markdown.md) | Süntaks ja miks Markdown sobib dokumentatsiooniks | Seminaris |
| [Arenduskeskkond](01-big-picture-and-tools/06-dev-environment.md) | Node.js, Docker ja arenduskeskkonna mõiste | Seminaris |
| [Giti oskus: esimene commit](01-big-picture-and-tools/07-git-first-commit.md) | `add`, `commit`, `push` | Seminaris |
| [Giti oskus: harud](01-big-picture-and-tools/08-git-branches.md) | Haru (branch), Issue → haru → pull request → ülevaatus, `.gitignore`, clone ja fork | Seminaris |

### [2. Kliendisoovist arendusülesandeni](02-from-request-to-task/README.md)

Põhiküsimus: kas tegeleme päris ja olulise probleemiga?

| Leht | Sisu | Märge |
|---|---|---|
| [Probleemi uurimine](02-from-request-to-task/01-problem-discovery.md) | Soov, probleem ja lahendusidee; probleemiväide; tõend, tõlgendus ja oletus; discovery; AI uurimises | Seminaris |
| [Rollid](02-from-request-to-task/02-roles.md) | Tarkvaraarenduse rollid ja vastutus, release manager | Seminaris |
| [Litsentsid](02-from-request-to-task/03-licences.md) | Litsents kui kasutusluba, MIT, GPL, Creative Commons, võõra materjali kontroll | Seminaris |
| [Lähteülesanne](02-from-request-to-task/04-project-brief.md) | Kandidaatide võrdlus, kontroll, huvipooled, lähteülesande osad | Seminaris |
| [Dokumenteerimine](02-from-request-to-task/05-documentation.md) | README, otsuste logi, dokumentatsioon repos | Seminaris |
| [Kanban ja ajahinnang](02-from-request-to-task/06-kanban-and-estimates.md) | Kanban, GitHub Projects, prioriseerimine, ajahinnang | Seminaris |
| [Giti oskus: pull ja release](02-from-request-to-task/07-git-pull-and-release.md) | Ühine repo, commit'i head tavad, `pull`, tag, release, semantiline versioonimine | Seminaris |

### [3. Meeskond, tööviis ja süsteemi põhimõte](03-team-and-system/README.md)

Põhiküsimus: kuidas meeskond töötab ja millist süsteemi põhimõtteliselt kavandab?

| Leht | Sisu | Märge |
|---|---|---|
| [Tööviisid](03-team-and-system/01-ways-of-working.md) | Waterfall, iteratiivne ja agiilne arendus, Scrumi põhimõisted, rollide vahetamine | Seminaris |
| [Kasutajalood ja nõuded](03-team-and-system/02-user-stories-and-requirements.md) | Kasutaja teekond, kasutajalugu, funktsionaalsed ja mittefunktsionaalsed nõuded | Seminaris |
| [Backlog](03-team-and-system/03-backlog.md) | Backlog'i koostamine ja hoidmine | Seminaris |
| [Süsteemi kontseptsioon](03-team-and-system/04-system-concept.md) | Eesmärk, osalised, piir, süsteemi osad ja sõltuvused, lahendussuunad | Seminaris |
| [Arhitektuuri põhimõisted](03-team-and-system/05-architecture-basics.md) | Klient-server, frontend ja backend, API, andmebaas, pilv | Iseseisev |
| [Giti oskus: merge-konflikt](03-team-and-system/06-git-merge-conflict.md) | Konflikti tekkimine ja lahendamine terminalis | Seminaris |

### [4. Kvaliteet, riskid ja vastutus](04-quality-and-risk/README.md)

Põhiküsimus: kuidas me teame, et kavand on piisavalt hea, ja mis võib meid alt vedada?

| Leht | Sisu | Märge |
|---|---|---|
| [Mõõdetav kvaliteet](04-quality-and-risk/01-measurable-quality.md) | Funktsioon ja kvaliteediomadus, ebamäärasest mõõdetavaks, kompromissid, turvalisus, privaatsus ja ligipääsetavus | Seminaris |
| [Testjuhtum](04-quality-and-risk/02-test-cases.md) | Testjuhtum kontrolltingimusest, erijuhtumid, testimise tasemed | Seminaris |
| [Vea silumine ja koodi ülevaatus](04-quality-and-risk/03-debugging-and-code-review.md) | Viga, silumine, vea kirjeldus, hea ülevaatuse kommentaar | Iseseisev |
| [Riskid](04-quality-and-risk/04-risks.md) | Risk ja eeldus, riskikaart, kolmandad osapooled ja sõltuvused | Seminaris |
| [Koodi kvaliteet](04-quality-and-risk/05-code-quality.md) | Loetavus, kokkulepped, linter, tehniline võlg | Iseseisev |
| [Giti oskus: ajalugu ja tagasivõtmine](04-quality-and-risk/06-git-history.md) | `git log`, `git diff`, `git restore` | Seminaris |

### [5. Kasutuselevõtt, käitus ja areng](05-deployment-and-evolution/README.md)

Põhiküsimus: mis juhtub süsteemiga pärast selle loomist? *Mustand: võib pärast seminari 5 esimest läbiviimist muutuda.*

| Leht | Sisu | Märge |
|---|---|---|
| [Kasutuselevõtt ja käitus](05-deployment-and-evolution/01-deployment-and-operations.md) | Keskkonnad, CI/CD, kasutuselevõtu otsused, seire, hooldus, süsteemi lõpetamine | Seminaris |
| [Tagasiside ja areng](05-deployment-and-evolution/02-feedback-and-evolution.md) | Väljund, tulemus ja mõju; mõõdikud; tagasiside; uuesti uurimine; demo | Seminaris |
| [Giti oskus: tag ja ajajoon](05-deployment-and-evolution/03-git-tag-and-timeline.md) | `git tag`, `git log` kahe versiooni vahel, release'ide ajajoon | Seminaris |

### [Sõnastik](glossary.md)

Kursuse põhimõisted tähestiku järjekorras koos linkidega lehtedele.

## Teemade kaupa

Kui otsid kindlat teemat, leiad selle siit.

| Teema | Osad |
|---|---|
| Git ja GitHub | 1, 2, 3, 4 ja 5: iga osa viimane leht |
| Arendusprotsess ja tööviisid | 1. Tarkvaraarenduse elutsükkel ja AI; 3. Tööviisid |
| Rollid ja meeskond | 2. Rollid; 3. Tööviisid |
| Nõuded | 2. Probleemi uurimine; 2. Lähteülesanne; 3. Kasutajalood ja nõuded |
| Töö planeerimine | 2. Kanban ja ajahinnang; 3. Backlog |
| Dokumenteerimine | 1. Markdown; 2. Dokumenteerimine |
| Kvaliteet ja testimine | 3. Kasutajalood ja nõuded; 4. Mõõdetav kvaliteet; 4. Testjuhtum; 4. Vea silumine ja koodi ülevaatus; 4. Koodi kvaliteet |
| Õigus ja eetika | 1. Tarkvaraarenduse elutsükkel ja AI; 2. Litsentsid; 4. Riskid |
