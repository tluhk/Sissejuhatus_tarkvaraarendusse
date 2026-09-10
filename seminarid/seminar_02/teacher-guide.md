# Seminari 2 õpetaja juhend

## Enne seminari

- Vaata esimese kodutöö Issue kommentaaridest üle kloonimise, commit'i ja push'i takistused. Paku neile sihitud abi; ära eelda salvestuse põhjal, et kõik said kogu töövoo iseseisvalt tehtud.

- Loo organisatsiooni `TLUHK-RIF26` meeskonnarepositooriumid.
- Anna kõigile liikmetele vajalik ligipääs.
- Lisa repodesse või jaga lingina kursuse mallid.
- Valmista ette GOV.UK discovery juhtumi lühikokkuvõte.
- Ära saada meeskondadele valmis probleemide nimekirja. Varunimekiri on ainult neile, kes ei leia pärast juhendatud vaatlust ühtegi kandidaati.

## Ohukohad

- Õppijad hakkavad kohe rakendust kavandama. Küsi: „Millist praegust tegevust või takistust see lahendab?”
- Isiklik kogemus esitatakse faktina. Küsi: „Kuidas keegi teine seda kinnitaks või ümber lükkaks?”
- Valitakse väga suur ühiskondlik probleem. Aidake leida üks konkreetne inimene, olukord ja mõju.
- Üks tehniliselt tugev õppija teeb kogu GitHubi töö. Kontrolli enne lõppu iga liikme Issue ja haru olemasolu.
- Valideerimine muutub mahukaks uurimistööks. Selle kursuse eesmärk on põhimõtte mõistmine, mitte uurimismeetodi täielik õpetamine.

## Ajaplaan

### I osa, 90 minutit

| Tegevus | Aeg |
|---|---:|
| Uue projekti töökorraldus ja päeva probleemiküsimus | 10 min |
| Probleem ja lahendusidee | 20 min |
| Probleemide leidmine | 20 min |
| GOV.UK discovery juhtum | 15 min |
| Individuaalne kaardistus | 15 min |
| Puhver | 10 min |

### II osa, 90 minutit

| Tegevus | Aeg |
|---|---:|
| Meeskonnad, ligipääs ja repo kloonimine | 20 min |
| Kandidaatide võrdlus | 10 min |
| Valik ja esimene otsus | 10 min |
| Kerge valideerimise kava | 10 min |
| Issue, haru, commit, PR, ülevaatus ja pull | 30 min |
| Kodutöö, refleksioon ja release | 10 min |

Kui tehniline seadistus võtab kauem:

1. säilita probleemikandidaatide võrdlus;
2. säilita esimese otsuse mustand;
3. anna valideerimise küsimuste viimistlemine kodutööks;
4. ära kiirusta pull request'i ühendamist ilma ülevaatuseta.

Õppijad kloonivad kõik sama meeskonnarepo. Selles töövoos fork'i ei tehta. Näita esimene haru ja PR projektoril ning lase igal õppijal enda harus vähemalt proovimuudatus push'ida.

## Esimese seminari järel: oskused töö sees

Alusta probleemide leidmise teemaga. Esimese kümne minuti sees kuluta kuni viis minutit uue projekti tulemusele: otsuste logi, rollivahetus, refleksioonid ja release'id. Ära tee eraldi esimest seminari kordavat loenguosa.

- Probleemikandidaatide kirjapanekul meenuta Markdowni pealkirju, loendeid ja linke. Lase õppijatel samal ajal kandidaate esialgselt võrrelda.
- Repo avamisel kontrolli õiget kausta ja repot. Esimeses seminaris kulus just sellele palju abi.
- Esimese otsuse salvestamisel korda `git status → git add → git diff --cached → git commit → git push`. Peamine kordus järgib tunnis kasutatud terminalitöövoogu; Source Control sobib tuttava alternatiivina.
- Pärast kaaslase PR-i ühendamist näita, miks kohalik koopia vajab `pull`-i. Harjuta seda puhta töökaustaga peaharus.
- Viimases kümnes minutis näita tag'i, GitHub Release'i ja release notes'i erinevust ning esimese release'i loomist. Kodutöös korratakse sama protsessi.

Node.js, npm, Docker, GitHub CLI ja SSH ei ole selle seminari eeldused. Arendusmeetodite kordus sobib seminari 3 tööviisi valiku juurde; käituskeskkonnad tulevad tagasi vajaduse tekkimisel. Kui tehniline abi võtab puhvrist kauem, vähenda juhtumi ühise arutelu aega, säilitades probleemivaliku ning iga õppija koostööharjutuse.

## Aruteluküsimused

- Millist infot me teame ja mida ainult oletame?
- Kas probleem kaoks ka ilma uue tarkvarata?
- Kelle jaoks võib meie valitud lahendus tekitada uue probleemi?
- Mis paneks meid projektist loobuma?

## Tagasiside fookus

Hinda probleemist lähtumist ja põhjendust. Ära hinda ideede tehnilist efektsust ega dokumentide pikkust.

Hea tulemus näitab:

- lahenduse ja probleemi eristamist;
- alternatiivide tegelikku kaalumist;
- ausat ebakindlust;
- tõendi mõju sõnastusele;
- iga õppija nähtavat panust.

## Seminari lõpp

Kontrolli iga meeskonnaga:

- repo ja ligipääs;
- probleemiväite mustand;
- otsuse fail;
- valideerimise Issue'd;
- rollid ja vastutajad;
- kodutöö ning release'i tähtaeg.
