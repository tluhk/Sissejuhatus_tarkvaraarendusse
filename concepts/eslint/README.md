# ESLint

ESLint on populaarne avatud lähtekoodiga tööriist JavaScripti koodi staatilise koodi analüüsimiseks. Seda kasutatakse levinud kodeerimisprobleemide leidmiseks ja parandamiseks ning ühtse koodistiili rakendamiseks kogu projektis.

ESLinti saab kasutada erinevates keskkondades, nagu Node.js, veebibrauserid ja React Native, ning see toetab erinevaid JavaScripti süntakseid.

ESLint on väga konfigureeritav ja seda saab kohandada vastavalt konkreetsetele projektinõuetele. See sisaldab eelmääratletud reegleid, mida saab lubada või keelata, ja see võimaldab ka kohandatud reeglite loomist. Reeglid hõlmavad paljusid parimaid kodeerimise tavasid, sealhulgas muutujate deklaratsioone, funktsioonide määratlusi, tingimuslauseid ja palju muud.

ESLint on sageli integreeritud koodiredaktorite ja ehitustööriistadega, nagu VS Code, Atom, Sublime Text ja Webpack, mis võivad anda reaalajas tagasisidet kodeerimisvigade kohta ja rakendada kodeerimisstandardeid.

## ESLint-i paigaldamine NodeJS projektile (VSCode)

Kõigepealt lisa VSCode-le (kui ei ole veel lisatud) ESLint psitikprogramm. Leiad selle pistikprogrammide alt või siis siit: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint

1. Paigalda ESLint arendussõltuvusena järgmiselt:

```bash
npm install eslint --save-dev
```

2. Käivita oma projekti juurkaustast ESLint seadistamine:

```bash
npx eslint --init
```
> Pööra tähelepanu - `npx`, mitte `npm`

> See käsk küsib juhiseid ESLinti konfigureerimiseks oma projekti jaoks küsimuste küsimisega. Saate valida stiilijuhise, mida soovite järgida, määrata failitüübid, mida soovite lintida, ja konfigureerida mõned reeglid.

> Programmeerimine I kursuse raames kasutame stiilijuhendina `Airbnb` stiilijuhiste komplekti.

Vasta küsimustele järgmiselt:

Küsimus: `? How would you like to use ESLint? ...`  
Valik: `> To check syntax, find problems, and enforce code style`

Küsimus:`? What type of modules does your project use? ...`  
Valik: `> CommonJS (require/exports)`

Küsimus: `? Which framework does your project use? ...`  
Valik: `> None of these`

Küsimus: `? Does your project use TypeScript? »`  
Valik: `No`

Küsimus: `? Where does your code run? ...`  
Valik: `> Node`

Küsimus: `? How would you like to define a style for your project? ...`  
Valik: `> Use a popular style guide`

Küsimus: `? Which style guide do you want to follow? ...`  
Valik: `> Airbnb: https://github.com/airbnb/javascript`

Küsimus: `? What format do you want your config file to be in? ...`  
Valik: `> JavaScript`

Küsimus sõltuvuste kohta: `? Would you like to install them now?`  
Valik: `Yes`

Küsimus: `? Which package manager do you want to use? ...`  
Valik: `npm`

Ja võibki hakata koodi kirjutama :smiley:

## Airbnb

Airbnb on üks populaarseim JavaScripti stiilijuhend. See on laialt levinud stiilijuhend, mis põhineb parimatel tavadel ja mille eesmärk on edendada koodi järjepidevust ja hooldatavust. Airbnb JavaScripti stiilijuhendit haldab Airbnb meeskond ning seda kasutavad paljud arendajad ja organisatsioonid üle maailma.

Airbnb JavaScripti stiilijuhend hõlmab JavaScripti kodeerimise tavade erinevaid aspekte, sealhulgas taande, muutujate nimetamist, funktsioonide deklaratsioone, tingimuslauseid ja palju muud. See on saadaval GitHubis ja seda hooldatakse aktiivselt, mis tähendab, et seda värskendatakse regulaarselt, et olla kursis JavaScripti ökosüsteemi muutustega.

JavaScripti jaoks on ka teisi populaarseid stiilijuhiseid, sealhulgas Google JavaScripti stiilijuhend ja standardne JavaScripti stiilijuhend. Nendel stiilijuhenditel on oma kokkulepped ja parimad tavad, nii et saate valida selle, mis sobib kõige paremini teie arendusvajaduste ja eelistustega. Oluline on märkida, et stiilijuhendi kasutuselevõtt võib aidata parandada koodi kvaliteeti, loetavust ja hooldatavust ning hõlbustada mitme arendaja tööd sama koodibaasiga.

## Realõpud LF vs CRLF

Kui kasutad arendamiseks MS Windows operatsioonisüsteemiga arvutit, siis peale ESLint-i paigaldust Airbnb stiilijuhendiga näed, et ESLint näitab vigu ridade lõpus. Põhjus on selles, et Windows kasutab CRLF reavahetust, kuid Airbnb nõuab LF reavahetust.

LF ja CRLF on kaks erinevat realõpumärki, mida kasutatakse tekstifailides. LF tähistab "reavahetust" ja CRLF tähendab "carriage return", millele järgneb "reavahetus".

LF-i ja CRLF-i erinevus seisneb selles, kuidas nad tekstifailides reavahetusi kujutavad. LF tähistab ühte reavahetust, mida kasutatakse Unixi, Linuxi ja macOS-i operatsioonisüsteemides. CRLF tähistab kahte märki, "carriage return" ja reavahetust ning seda kasutatakse Windowsi operatsioonisüsteemides.

Rea lõpu märgi valik on oluline, kuna see võib mõjutada tekstifaili tõlgendamist erinevate programmide poolt. Näiteks kui loote tekstifaili CRLF-i realõpudega Windowsi masinas ja edastate selle seejärel Linuxi masinasse, ei pruugi mõned Linuxi masina programmid realõppe õigesti tõlgendada, mis võib põhjustada vigu või ootamatut käitumist.

Samamoodi, kui loote tekstifaili, kasutades Unixi või Linuxi masinas LF-i realõpusid, ja edastate selle seejärel Windowsi masinasse, ei pruugi mõned Windowsi masina programmid realõppe õigesti tõlgendada.

Realõpumärkidega seotud probleemide vältimiseks on soovitatav valida sobiv realõpumärk vastavalt kasutatavale operatsioonisüsteemile või tekstiredaktorile ning kasutada kogu failis ühtset realõpumärki. Mõnel tekstiredaktoril ja versioonihaldussüsteemil (nt Git) on sätted realõpude automaatseks teisendamiseks sobivasse vormingusse, kui töötate erinevate operatsioonisüsteemide failidega.

## Realõppumärgi seadistamine VSCode koodiredaktoris

Windowsi VS-koodi vaikerealõpude LF-i määramiseks toimige järgmiselt.

1. Avage VS Code ja minge menüüsse `Settings`, klõpsates akna vasakus alanurgas hammasrattaikooni.
2. Sisestage seadete otsinguribale `files.eol` ja vajutage sisestusklahvi. See peaks kuvama sätte `End of Line`.
3. Klõpsake valiku `End of Line` kõrval olevat rippmenüüd ja valige `LF` või `/n`, et määrata rea vaikelõpuks `LF`.

Nüüd, kui loote VSCode koodieditoris uue faili, kasutab see vaikimisi `LF` realõppe.

> Kui teil on juba fail, mis kasutab `CRLF` realõppe, saate selle faili realõppe muuta klõpsates VSCode akna alumises paremas nurgas nuppu `CRLF/LF` ja valides `LF`.

## Tühikute arvu seadistamine

VSCode vaikimisi tühikute arv (kui vajutad `TAB` klahvi) on neli tühikut. Airbnb reeglistik näeb ette kahte tühikut. Selleks, et seadistada VSCode kasutama nelja tühiku asemel kahte, tuleb teha järgmist:

1. Ava VSCode.
2. Klõpsa vasakus alanurgas hammasratta ikoonil, et avada Seadete menüü.
3. Vali nimekirjast "Seaded" (Settings).
4. Seadete vahekaardi ülaosas asuvas otsinguribas kirjuta "indent", et kuvada taandega seotud seaded.
5. "Editor: Tab Size" alt saad muuta tabulaatori pikkust ehk mitut tühikut tabulaator kasutab. Vaikimisi on see seatud väärtusele 4 - see tuleks seadistada 2-ks.
6. Edaspidi kasutatakse taanete jaoks 4 tühiku asemel 2-te.

Lisaks saad olemasolevat taanet (nt tabulaatoritest tühikuteks muuta) järgides neid samme:

1. Ava fail, mida soovid redigeerida, VSCode'is.
2. Klõpsa VSCode'i akna paremas alanurgas "Spaces" või "Tab Size" nupul. See avab väikese kontekstimenüü.
3. Kui soovid muuta taandesuurust, klõpsa "Indent Using Spaces" (Taanda tühikute kasutamisega) ja vali loendist soovitud number.
4. Ära unusta oma muudatusi salvestada.