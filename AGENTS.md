# AGENTS.md

See fail kirjeldab selle repositooriumiga töötamise kokkuleppeid. Täiendame seda kursuse arendamise käigus.

## Kursuse kontekst

- Kursus: **Sissejuhatus tarkvaraarendusse**.
- Sihtgrupp on tarkvaraarenduse algajad.
- Kursuse maht on 6 EAP.
- Kehtiv aine kood on `HKI5113.HK`.
- Kursuse keskne mõte on näidata terviklikku teekonda probleemist tarkvarani.
- Tarkvaraarendus ei võrdu ainult programmeerimisega. Kursuse fookuses on ka uurimine, nõuded, disain, planeerimine, meeskonnatöö, dokumenteerimine, testimine ja versioonihaldus.
- Git ja GitHub on kursuse läbivad töövahendid.
- Esimesel semestril tuleb eelistada algajasõbralikku graafilist töövoogu. Terminali kasutamine ei ole Giti õppimise eeldus.

Kehtiva aineinfo esmane masinloetav allikas on `metadata/data.json`. Kui see läheb vastuollu vanemate õppematerjalidega, ei tohi vastuolu vaikimisi lahendada: see tuleb välja tuua ja küsida vajaduse korral õppejõult kinnitust.

## Repositooriumi ülesehitus

- `README.md` on õppematerjalide avaleht ja sisukord.
- `metadata/data.json` sisaldab kehtiva kursuse põhiandmeid ja õpiväljundeid.
- `docs/` sisaldab aine ülddokumente, juhendeid, sõnastikku ja varasemaid slaidikavandeid.
- `concepts/` sisaldab mõistete ja teemade õppematerjale.
- `seminarid/` sisaldab seminaride slaide, ülesandeid ning õpetaja juhendeid.
- `course-draft-v2.md` on kursuse kavand, mitte automaatselt kehtiv kursuseprogramm.
- `slides.md` on slaidide muudetav lähtefail. `slides.html` on sellest genereeritud väljund.
- Seminari 1 peatükkide slaidide lähtefailid asuvad `seminarid/seminar_01/slaidid/` kaustas. HTML-esitlus genereeritakse käsuga `seminarid/seminar_01/export-slides.sh`; genereeritud `slides.html` faili ei muudeta käsitsi.
- `.bak`-failid on varukoopiad ega ole aktiivsed õppematerjalid.

## Töökorraldus

- Enne sisulist muutmist tuleb lugeda läbi aktiivne seminarimaterjal, sellega seotud kodutöö ja õpetaja juhend.
- Kui kasutaja küsib hinnangut, auditit või arutelu, ei muudeta faile ilma eraldi muutmispalveta.
- Suurema muudatuse korral esitatakse kõigepealt lühike hinnang ja kavand ning seejärel tehakse kokkulepitud muudatused.
- Olemasolevaid kasutaja muudatusi ei kirjutata üle ega pöörata tagasi.
- Muudatused peavad jääma kasutaja nimetatud seminari või materjalide piiresse, kui laiem muudatus pole vältimatult vajalik.
- Õppija materjal ja õpetaja juhend tuleb hinnata ning muuta eraldi.
- Genereeritud faili ei muudeta käsitsi, kui sama sisu pärineb muudetavast lähtefailist.

## Õppematerjalide põhimõtted

- Õppijale suunatud tekst on eesti keeles, lihtne ja algajasõbralik.
- Uut mõistet selgitatakse enne, kui õppija peab seda ülesandes kasutama.
- Ingliskeelse erialatermini võib lisada eestikeelse termini kõrvale, kui see aitab tööriista või dokumentatsiooni kasutada.
- Juhendid peavad sisaldama konkreetset eesmärki, tegevusi ja kontrollpunkti, mille järgi õppija saab tulemust kontrollida.
- Koodinäited ja failinäited peavad olema täielikud ning kopeeritavad, kui ülesanne eeldab nende kasutamist.
- Seminar peab jätma praktiliseks tööks ja ootamatuteks tehnilisteks probleemideks realistliku puhvri.
- Kodutöö peab põhinema seminaris tegelikult käsitletud oskustel.
- Iga seminari väljund peab toetama järgmise seminari alustamist.
- Ülesande juures tuleb eristada individuaalne ja rühmatöö ning kirjeldada esitamise viis.
- Õpetajale mõeldud märkused ei tohi sattuda selgitamata kujul õppija juhendisse.

## Seminaride omavaheline kooskõla

Seminari muutmisel kontrolli vähemalt järgmisi faile:

1. seminari slaidid;
2. seminari- või töötoa juhend;
3. kodutöö;
4. õpetaja juhend;
5. `docs/kursuseprogramm.md`;
6. `README.md` viited;
7. järgmise seminari eeldused ja tagasivaade.

Slaidide, kodutöö, õpetaja juhendi, failinimede, tähtaegade ja hindamiskriteeriumide vahel ei tohi olla varjatud vastuolusid.

## Esimese seminari suund

- Esimese seminari kontaktaeg on kaks 90-minutilist osa. Ajakavas tuleb arvestada praktilise töö, paigaldamise, sisselogimise ja tehniliste tõrgete ajakuluga.
- Esimene seminar annab õppijale ülevaate kursusest ja sellest, mida kursuse jooksul tehakse.
- Kursuse ülevaade algab avatud küsimusega „Mis on tarkvaraarendus?”. Õppijate vastused kogutakse enne definitsiooni andmist ning programmeerimist käsitletakse õige, kuid ainult ühe osana laiemast arendusprotsessist.
- Esimese osa sisuline raam on tarkvara: mis see on, milline on selle roll ühiskonnas, kuidas tarkvara arendatakse ja millistest etappidest koosneb tarkvaraarenduse elutsükkel.
- Esimese osa põhisõnum on, et tarkvaraarendus ei võrdu programmeerimisega ning arendus algab probleemist ja kasutaja vajadusest, mitte tööriista või koodi valimisest.
- AI mõju käsitletakse kogu arendusprotsessi läbiva muutusena: AI võib toetada uurimist, nõuete täpsustamist, kavandamist, programmeerimist, testimist ja dokumenteerimist, kuid tulemust tuleb kontrollida ning vastutus jääb inimesele ja meeskonnale.
- AI käsitluses tuleb nimetada vähemalt privaatsuse, autoriõiguse, turvalisuse, kallutatuse, vigaste vastuste ja konfidentsiaalse info sisestamise riske.
- Seminari põhisisu on tarkvaraarenduse tööriistade tutvustamine ning õppija töövahendite ja arenduskeskkonna seadistamine.
- Tööriistade käsitluse keskmes on Git ja GitHub ning nende omavaheline erinevus.
- GitHub CLI-d (`gh`) tutvustatakse valikulise käsureatööriistana GitHubi repositooriumide ja Issue'de vaatamiseks. See ei asenda esimese seminari VS Code'i graafilist Giti põhivoogu.
- GitHubi ühendusviisidest nimetatakse HTTPS-i ja SSH-d, kuid esimeses seminaris kasutatakse HTTPS-i. SSH-võtmeid selles etapis ei seadistata.
- Põhiline koodiredaktor on VS Code. Alternatiive võib lühidalt tutvustada ja paluda neid tundvatel õppijatel oma kogemust jagada.
- Selgitada tuleb mõistet IDE, selle ingliskeelset nimetust `Integrated Development Environment` ja erinevust lihtsa tekstiredaktoriga.
- Tutvustada tuleb terminali, käsukesta ja graafiliste tööriistade suhet. GitHub Desktop on alternatiiv, kuid kursuse eelistatud graafiline Giti töövoog toimub VS Code'is.
- Windowsis kasutatakse kursuse käsureanäidetes PowerShelli asemel Git Bashi.
- Markdowni puhul tuleb lisaks süntaksile selgitada, miks see sobib dokumentatsiooni ja GitHubi töövoogu.
- Node.js-i, Dockerit ja arenduskeskkondi tutvustatakse esmalt tervikpildi tasandil. Enne paigaldamist või praktilist kasutamist peab olema selge, milleks tööriista kursusel vaja läheb.
- Võimaluse korral säilitatakse olemasolevate esimese seminari materjalide loogiline järjekord, kuid puuduvaid vaheastmeid ei jäeta lisamata.

## Failide ja mõistete vormistus

- Markdown-failides kasutatakse selget pealkirjahierarhiat.
- Failiteed ja käsud märgitakse koodivormingus.
- GitHub kirjutatakse suure `H`-ga.
- Git tähendab versioonihaldustarkvara; GitHub tähendab seda kasutavat veebiplatvormi. Neid ei käsitleta sünonüümidena.
- `commit`, `push`, `pull request`, `branch` ja `merge` tuleb esmakordsel kasutamisel õppijale lahti seletada.
- Eelistada tuleb lühikesi, tähendusrikkaid ja järjepidevaid failinimesid.
- Uute failide nimetamisel kasutatakse võimaluse korral väiketähti ja sidekriipse, kui olemasoleva kausta stiil ei nõua teisiti.

## Kontroll enne töö lõpetamist

- Kontrolli, et kohalikud Markdown-lingid ja pilditeed osutaksid olemasolevatele failidele.
- Kontrolli, et aine kood, EAP, õppeaasta, rühma nimi ja kuupäevad oleksid kehtivad või selgelt näidetena tähistatud.
- Kontrolli, et seminari ajakava osade summa vastaks tegelikule kontakttunni pikkusele.
- Kontrolli, et õppija ei peaks kodutöös kasutama töövoogu, mida seminaris pole õpetatud ega harjutatud.
- Kontrolli, et näidis ja nõutav väljund kasutaksid samu failinimesid ja struktuuri.
- Kontrolli muudatuste järel `git diff` ja võimaluse korral Markdowni või slaidide renderdust.

## Praegu teadaolevad lahtised küsimused

- Esimese seminari 2026. aasta täpne ajakava ja praktilised kontrollpunktid tuleb veel kokku leppida.
- Tuleb otsustada, kas projektirühmad ja ühine projektirepositoorium luuakse esimeses või teises seminaris.
- Tuleb kinnitada 2026. aasta GitHubi organisatsiooni nimi.
- Vanemates failides leiduvad 4 EAP, aine kood `HKI5086.HK`, `RIF25` ja märge „juba toimunud” ei ole vaikimisi kehtiv info.
- Aktiivsete ja arhiveeritavate kursusekavandite staatus tuleb veel täpsustada.
