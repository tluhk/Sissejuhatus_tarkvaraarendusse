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

Lehtede lingid lisanduvad siis, kui leht valmib.

### [1. Suur pilt ja töövahendid](01-big-picture-and-tools/README.md)

Põhiküsimus: mis on tarkvaraarendus ja milliste tööriistadega seda tehakse?

| Leht | Sisu | Märge |
|---|---|---|
| [Tarkvara ja tarkvaraarendus](01-big-picture-and-tools/software.md) | Mis on tarkvara, tarkvara tüübid, tarkvaraarendus ei võrdu programmeerimisega | Seminaris |
| [Tarkvaraarenduse elutsükkel ja AI](01-big-picture-and-tools/sdlc-and-ai.md) | Elutsükli etapid, Waterfall ja agiilne arendus, AI roll ja riskid | Seminaris |
| [IDE ja terminal](01-big-picture-and-tools/ide-and-terminal.md) | IDE, VS Code, terminal, käsukest, Git Bash | Seminaris |
| [Git ja GitHub](01-big-picture-and-tools/git-and-github.md) | Versioonihaldus, Giti ja GitHubi erinevus, HTTPS, GitHub CLI | Seminaris |
| [Markdown](01-big-picture-and-tools/markdown.md) | Süntaks ja miks Markdown sobib dokumentatsiooniks | Seminaris |
| [Arenduskeskkond](01-big-picture-and-tools/dev-environment.md) | Node.js, Docker ja arenduskeskkonna mõiste | Seminaris |
| [Giti oskus: esimene commit](01-big-picture-and-tools/git-first-commit.md) | `add`, `commit`, `push` | Seminaris |
| [Giti oskus: harud](01-big-picture-and-tools/git-branches.md) | Haru (branch), Issue → haru → pull request → ülevaatus, `.gitignore`, clone ja fork | Seminaris |

### [2. Kliendisoovist arendusülesandeni](02-from-request-to-task/README.md)

Põhiküsimus: kas tegeleme päris ja olulise probleemiga?

| Leht | Sisu | Märge |
|---|---|---|
| [Probleemi uurimine](02-from-request-to-task/problem-discovery.md) | Soov, probleem ja lahendusidee; probleemiväide; tõend, tõlgendus ja oletus; discovery; AI uurimises | Seminaris |
| [Rollid](02-from-request-to-task/roles.md) | Tarkvaraarenduse rollid ja vastutus, release manager | Seminaris |
| [Litsentsid](02-from-request-to-task/licences.md) | Litsents kui kasutusluba, MIT, GPL, Creative Commons, võõra materjali kontroll | Seminaris |
| [Lähteülesanne](02-from-request-to-task/project-brief.md) | Kandidaatide võrdlus, kontroll, huvipooled, lähteülesande osad | Seminaris |
| [Dokumenteerimine](02-from-request-to-task/documentation.md) | README, otsuste logi, dokumentatsioon repos | Seminaris |
| [Kanban ja ajahinnang](02-from-request-to-task/kanban-and-estimates.md) | Kanban, GitHub Projects, prioriseerimine, ajahinnang | Seminaris |
| [Giti oskus: pull ja release](02-from-request-to-task/git-pull-and-release.md) | Ühine repo, commit'i head tavad, `pull`, tag, release, semantiline versioonimine | Seminaris |

### 3. Meeskond, tööviis ja süsteemi põhimõte

Põhiküsimus: kuidas meeskond töötab ja millist süsteemi põhimõtteliselt kavandab?

| Leht | Sisu | Märge |
|---|---|---|
| Tööviisid | Waterfall, iteratiivne ja agiilne arendus, Scrumi põhimõisted, rollide vahetamine | Seminaris |
| Kasutajalood ja nõuded | Kasutajalugu, funktsionaalsed ja mittefunktsionaalsed nõuded | Seminaris |
| Backlog | Backlog'i koostamine ja hoidmine | Seminaris |
| Süsteemi kontseptsioon | Kasutaja teekond, süsteemi osad, piirid ja sõltuvused | Seminaris |
| Arhitektuuri põhimõisted | Klient-server, frontend ja backend, API, andmebaas, pilv | Iseseisev |
| Giti oskus: merge-konflikt | Konflikti tekkimine ja lahendamine terminalis | Seminaris |

### 4. Kvaliteet, riskid ja vastutus

Põhiküsimus: kas kavand on piisavalt hea ja vastutustundlik?

| Leht | Sisu | Märge |
|---|---|---|
| Kvaliteediomadused | Kvaliteediomaduste valimine ja kontrollitavaks tegemine | Seminaris |
| Testimise alused | Testjuhtum, vea kordamine, järelkontroll, testimise tasemed | Seminaris |
| Koodi ülevaatus | Ülevaatuse eesmärk ja hea tagasiside | Seminaris |
| Koodi kvaliteet | Loetavus, kokkulepped, linter, tehniline võlg | Iseseisev |
| Riskid | Turvalisus, privaatsus, ligipääsetavus, töökindlus, kolmandad osapooled ja nende litsentsid | Seminaris |
| Giti oskus: ajalugu | `git log`, `git diff`, `git restore` | Seminaris |

### 5. Kasutuselevõtt, käitus ja areng

Põhiküsimus: mis juhtub süsteemiga pärast selle loomist?

| Leht | Sisu | Märge |
|---|---|---|
| Kasutuselevõtt ja käitus | Keskkonnad, CI/CD, tugi, seire, hooldus, süsteemi lõpetamine | Seminaris |
| Tagasiside ja areng | Tagasiside kogumine ja süsteemi edasiarendamine | Seminaris |
| Giti oskus: tag ja ajajoon | `git tag`, release'ide ajajoon Giti ajaloo põhjal | Seminaris |

### Sõnastik

Kursuse mõistete lühikesed selgitused.

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
| Kvaliteet ja testimine | 4. Kvaliteediomadused; 4. Testimise alused; 4. Koodi ülevaatus; 4. Koodi kvaliteet |
| Õigus ja eetika | 1. Tarkvaraarenduse elutsükkel ja AI; 2. Litsentsid; 4. Riskid |
