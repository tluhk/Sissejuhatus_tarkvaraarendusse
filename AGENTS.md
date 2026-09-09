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

- Esimese seminari 2026. aasta täpne sisu ja ajakava tuleb veel kokku leppida.
- Tuleb otsustada, kas projektirühmad ja ühine projektirepositoorium luuakse esimeses või teises seminaris.
- Tuleb kinnitada 2026. aasta GitHubi organisatsiooni nimi.
- Vanemates failides leiduvad 4 EAP, aine kood `HKI5086.HK`, `RIF25` ja märge „juba toimunud” ei ole vaikimisi kehtiv info.
- Aktiivsete ja arhiveeritavate kursusekavandite staatus tuleb veel täpsustada.
