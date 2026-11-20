<!-- loengud:konspekt osad=1 (automaatne; kui muudad käsitsi, kustuta see rida – siis tööriist seda üle ei kirjuta) -->
# Konspekt: Seminar 2: kliendisoovist arendusülesandeni

> Automaatne kokkuvõte seminari salvestusest (kõnetuvastus + keelemudel). Võib sisaldada ebatäpsusi – täpse sõnastuse leiad transkriptsioonist.

Seminari teema oli liikumine kliendi soovist konkreetse arendusülesandeni. Salvestatud osast suurem osa kulus aga esimese kodutöö tagasisidele ning Giti ja GitHubi töövoo kordamisele: nimetamine, commit'id, harud ja tõmbetaotlused. Seda tehti näidete ja otse ekraanil tehtud demoga. Seejärel jõudis õppejõud tarkvaraarenduse elutsüklini ja tutvustas kursuse keskset ülesannet, milleks on Haapsalu kolledži tunniplaani veebilehe uuendamine. Lõpuks käis ta läbi tarkvaratiimi rollid. Salvestus lõpeb pausiga. Plaanis olnud probleemikandidaatide harjutus ja tiimi töövoog jäid salvestusest välja.

## Esimese kodutöö tagasiside [▶ 0:04](https://youtu.be/bVmUyLJuX6I?t=4)

Kõik olid suutnud pull request'i ehk **tõmbetaotluse** ära teha. Õppejõu sõnul on see esimese korra kohta hea tulemus. Töö Giti ja GitHubiga (või mõne muu eemal asuva Giti halduriga) erineb tavapärasest arvutikasutusest, nii et küsimused on loomulikud. Tagasiside sai kirjutatud kiiruga. Kui keegi leiab, et kommentaar on vale ja asi oli tegelikult olemas, tasub sellest julgelt teada anda.

## Nimetamine täpselt nii, nagu on kokku lepitud [▶ 1:13](https://youtu.be/bVmUyLJuX6I?t=73)

Failide, kaustade ja muu nimed tuleb panna täpselt nii, nagu ülesandes kirjas. Praegu ei pruugi sellel suurt vahet olla, kuid hiljem võib vale nimi asja katki teha.

- **Ära kasuta täpitähti ega tühikuid.** Tühik on samuti märk. Näiteks veebiaadressis kodeeritakse see kujule `%20`, ja kui tühikuid on mitu, muutub nimi loetamatuks.
- **Kokkulepped on mõnes keskkonnas kohustuslikud.** Järgmisel aastal tuleb tõenäoliselt React, kus nimetamise konventsioonid on ette antud. Vale nime korral ei pruugi rakendus üldse kokku ehituda.
- **Iga märk loeb.** `kodutoo01`, `kodutoo_01` ja `kodutoo-01` on kolm eri nime. Ka suur- ja väiketähel on vahe.

Üks levinud viga oli **repo nime kordamine kausta nimes**. Kui ülesandes on tee kujul `repo-nimi/kaust/fail`, tähistab esimene osa repot ennast. Repo sisse ei ole vaja teha veel üht samanimelist kausta. Kaldkriipsudega tee tähendab, et üks asi asub teise sees.

Visual Studio Code'is on mugav kirjutada uue faili loomisel kogu tee, näiteks `kaust/alamkaust/fail.md`. Editor loob vajalikud kaustad siis ise.

## Markdown: koodiplokk tuleb ka sulgeda [▶ 5:46](https://youtu.be/bVmUyLJuX6I?t=346)

Paaristöödes tuli välja üks Markdowni viga. **Koodiplokk** algab kolme tagurpidi ülakomaga (backtick'iga, `` ``` ``) ja peab samamoodi ka lõppema. Kui lõpumärk puudub, muutub kogu ülejäänud dokument koodiks.

Avamärgi järele kirjutatakse tavaliselt keel, näiteks `css`, `html` või `text`. Siis oskab redaktor või GitHub koodi süntaksi järgi värvida. Kui GitHubis kuvatakse kogu fail ühtlase, vormindamata tekstina, on suure tõenäosusega kuskil koodiplokk algamas, aga mitte lõppemas.

Sama põhimõte kehtib igal pool programmeerimises: kõik, mis algab, peab ka lõppema.

## Reflektsioon kodutöös [▶ 9:23](https://youtu.be/bVmUyLJuX6I?t=563)

Mitu tööd olid põhjalikult kommenteeritud ja reflektsioonist oli näha, et materjal oli läbi töötatud. Esimesed kodutööd on lihtsad ja just seepärast on **reflektsioon** neis oluline: mõtle läbi, mida tegid ja mida teada said.

Tarkvaraarenduse meetodite videote kohta lisasid osa üliõpilasi ainult lingid. Õppejõud ootas kirjeldust, mida videotest teada saadi.

## Tarkvaraarenduse meetodid ja nende mõte [▶ 11:54](https://youtu.be/bVmUyLJuX6I?t=714)

Need märksõnad peab tarkvaraarendaja teadma: **kosemudel** (waterfall), **agiilne arendus**, **Scrum** ja **Kanban**. Kui need tundusid uued, tasub kodus järele vaadata. Tööle minnes ei tohiks juhtuda, et keegi nimetab mõnda neist ja sa ei tea, millest jutt käib.

Suurtes ettevõtetes ja idufirmades järgitakse meetodeid sageli täpselt, näiteks Scrum oma rollide ja kindla raamistikuga. Päriselus on meetodid aga tihti segamini. Oluline on meeles pidada, et **eesmärk ei ole meetodi järgimine**. Tarkvaraarenduse eesmärk on lahendada kellegi probleem, ja tarkvara on selleks ainult üks võimalik vahend.

Õppejõud lisas, et vahel teenid kliendi huve kõige paremini, kui soovitad tal tarkvara üldse mitte arendada ja teha hoopis midagi muud. Lühiajaliselt võid nii rahast ilma jääda. Kui aga lahendad kliendi probleemi ausalt, tuleb ta järgmise asjaga tõenäoliselt tagasi. Raha on vaja, aga see tuleb kliendilt ja klient peaks seda andma meelsasti. Õppejõu sõnul peab tänane arendaja nägema maailma laiemalt kui veel paar aastat tagasi, sest koodi kirjutamine on üha väiksem osa tema tööst.

### Kosemudel ja agiilne arendus [▶ 15:46](https://youtu.be/bVmUyLJuX6I?t=946)

**Kosemudeli** puhul lepitakse alguses kokku, mida tehakse, ja tehakse kõik lõpuni valmis. Alles siis näeb, mis välja tuli. Selleks ajaks võib kõik juba muutunud olla, nii et see on kallis lähenemine.

Vastukaaluks tekkis **agiilne tarkvaraarendus**. Õppejõud soovitas lugeda **agiilse tarkvaraarenduse manifesti** (otsingusõna „agile manifesto“). Sealt selgub, miks see suund tekkis.

Õppejõud küsis, miks on agiilne arendus parem. Üliõpilased pakkusid suhtlust ja paindlikkust, ühe vastusena tuli ka **MVP** (minimum viable product). Õppejõud selgitas seda lähemalt: kõigepealt tehakse minimaalne töötav jupp ja sinna ehitatakse järk-järgult juurde. Töötav osa on olemas algusest peale, vead tulevad kohe välja ja selleks pole palju kulutatud.

### Kus agiilne arendus ei sobi [▶ 17:59](https://youtu.be/bVmUyLJuX6I?t=1079)

Õppejõud rõhutas, et sellele küsimusele pole üht õiget vastust. Näitena tõi ta riigi pakutava teenuse, näiteks reisidokumendi taotlemise. Selline keskkond peab kohe arusaadavalt töötama. Kui see jätab poolikuna mulje:

- kaob kasutajate usaldus,
- pahatahtlikud inimesed võivad oletada, et ka muu pole päris valmis, ja hakkavad turvaauke otsima,
- kannatab asutuse maine.

Idufirma jaoks on agiilne lähenemine seevastu loomulik. Investorile tuleb näidata, et asi töötab. Raha ei jätku, et ehitada kõigepealt suur süsteem ja kuulda alles siis, et investor selle eest maksta ei taha. Kumbki lähenemine pole vale, vaid tuleb valida olukorra järgi.

### Tehisintellekt muudab kaalutlusi [▶ 20:22](https://youtu.be/bVmUyLJuX6I?t=1222)

Agiilsed meetodid tekkisid osaliselt seetõttu, et **koodi kirjutamine** oli kallis ja taheti varakult teada saada, kas asjal üldse mõtet on. Tehisintellekti tõttu on koodi kirjutamine nüüd odav. Tarkvaraarendus tervikuna odavaks ei muutunud, odavaks muutus koodi kirjutamine.

Ühe prompt'iga saab kosemudeli moodi terve töötava lahenduse. Kui see kliendile ei sobi, saab poole minuti pärast uue. Seega ei saa ka öelda, et agiilne arendus oleks automaatselt moodsam. Lähenemist saab ka poole pealt vahetada: teha osa agiilselt ja ülejäänu korraga valmis. Õige tee leitakse töö käigus koos tiimiga, ja klient on samuti tiimi osa.

Hiljem lisas õppejõud, et meetodi valikut ei maksa üle tähtsustada. Kliendiga pole vaja arutada, kas tehakse agiilselt või kosemudeli järgi. Piisab küsimusest, kas teha kõigepealt üks jupp ja seda täiendada või teha kogu asi korraga valmis.

## Issue'd, piletid ja projektihaldus [▶ 21:37](https://youtu.be/bVmUyLJuX6I?t=1297)

Üks üliõpilane mainis, et on varem kasutanud Jirat ja GitHubi issue'd olid talle uued. Õppejõud selgitas, et **Atlassian** teeb projektihaldustarkvara: Jira, Confluence, Bitbucket jm. GitHubis nimetatakse üht tööülesannet **issue'ks**, Jiras ja paljudes teistes süsteemides **piletiks** (ticket).

Põhimõte on igal pool sama:

- ülesanne on võimalikult kompaktne,
- sellel on vastutaja ja tähtaeg,
- suurema ülesande saab jagada alamülesanneteks.

Esimene kodutöö toimis just nii. Issue'l oli tähtaeg ja vastutaja, lisati ülevaataja, töö tehti eraldi harus ning valmis töö liideti peaharuga.

Kodutöödes oli ka probleeme. Mõned tegid muudatusi otse peaharus ja mõned olid teinud sama töö kohta mitu tõmbetaotlust. Õppejõu palve: proovige ühega hakkama saada, siis on vähem segadust.

## Giti põhitöövoog [▶ 24:59](https://youtu.be/bVmUyLJuX6I?t=1499)

Faili salvestamine ja versioonihaldus on kaks eri asja. Salvestatud fail on alles, kuid versioonihalduse jaoks pole veel midagi juhtunud. Töövoog on järgmine:

1. **`git add`** märgib muudatused versiooni lisamiseks. `git add .` võtab kõik muudetud failid. Kui kõike ei taha lisada, kirjuta punkti asemel failinimi. Väikeses projektis kasutab ka õppejõud punkti.
2. **`git commit -m "sõnum"`** salvestab versiooni ehk teeb **commit'i**. Sõnumis kirjelda võimalikult lühidalt, mida tehti. Vajadusel lisa pealkirjale pikem kirjeldus.
3. **`git push`** saadab muudatused sinu masinast eemal asuvasse reposse, näiteks GitHubi. Kui eemal asuvat repot pole, pole seda sammu vaja. Giti saab kasutada ka ainult oma arvutis.

### Miks commit peab olema kompaktne [▶ 27:28](https://youtu.be/bVmUyLJuX6I?t=1648)

Üks commit võiks sisaldada **ühte loogilist, iseseisvat muudatust**. Põhjus on praktiline. Kui arenduses midagi katki läheb, saad selle commit'i juurde tagasi minna ja mõjutad ainult seda üht funktsionaalsust. Kõrvale ei satu juhuslikke muudatusi, mis võiksid samuti paigast nihkuda. Kui suur on üks loogiline muudatus, selle tunnetuse saab töö käigus.

Õppejõud ütles, et järgmise semestri ainetes hindab ta tööd ka **commit'ide arvu** järgi. Ta ei taha öelda, et mida rohkem, seda parem, kuid tegelikult see nii on. Paljud sisuka sõnumiga commit'id näitavad, et iga loogiline samm on eraldi tehtud. Koolitöös näitab see ka, kui palju oled õppimisse panustanud: kahekümne selgelt kirjeldatud commit'i järel on midagi kindlasti külge jäänud. Ka professionaalne arendus peaks käima täpselt nii.

### Hea commit'i sõnum [▶ 29:31](https://youtu.be/bVmUyLJuX6I?t=1771)

Sõnum peab ütlema, mis tegelikult muutus. „Uuendasin“ või „uuendasin seisu“ ei ütle midagi. Pikema muudatuse puhul kirjuta pealkiri ja eraldi sisu. Sageli piisab aga lühikesest sõnumist, mis viitab issue'le, näiteks „lahendasin selle ja sulgesin issue nr X“. Kui hiljem midagi ebaõnnestub, aitavad sellised sõnumid leida õige koha, kuhu tagasi minna.

Hiljem demo käigus (alates [▶ 44:32](https://youtu.be/bVmUyLJuX6I?t=2672)) täpsustas õppejõud kaht kohustuslikku reeglit:

- **Commit'i sõnum kirjutatakse inglise keeles.** Tarkvaraarendus ei oma rahvust. Järgmine sama rakenduse arendaja võib olla hoopis teisest riigist ja peab aru saama ilma tõlkimata. Tehisintellekt saab aru igast keelest, kuid korrektne keel ja stiil on endiselt hea tava.
- **Kasutatakse käskivat kõneviisi.** Ei kirjutata „lõin kausta“, vaid „loo kaust“, inglise keeles näiteks `Add sja folder`. Samamoodi „Create“, „Update“, „Remove“ jne. See on kõige levinum kokkulepe.

Pikemalt on see kirjas kursuse materjalide mõistete (concepts) all commit'ide peatükis. Seal on näited kujul „mida tee“ vs „mida tegid“ ja selgitus, mis on hea commit.

## Giti ja GitHubi erinevus [▶ 31:52](https://youtu.be/bVmUyLJuX6I?t=1912)

Üks üliõpilane küsis, mis vahe on Gitil ja GitHubil. **Git** on versioonihaldussüsteem, mis võib asuda ükskõik kus: sinu arvutis või serveris. **GitHub** on üks teenus, kus Giti repot hoitakse eemal nii, et sellele pääseb ligi igalt poolt. GitHubil on ka muid funktsioone, kuid põhiline on see: Git on alus ja GitHub üks keskkond, kus seda kasutada.

Git ja GitHub on järgmise kolme aasta õpingutes tugisammas, nii et need tasub korralikult selgeks saada. Kui midagi jääb segaseks, küsi kas otse, kirjalikult või kaaslastelt.

Lühidalt tuli juttu ka teistest Giti käskudest. Näiteks näitab **`git status`**, mis seisus repo on. Ülevaataja ligipääsu probleem oli lahendatud. Võimalusi on kaks: teha repo avalikuks või anda ülevaatajale konkreetne ligipääsuõigus.

## Demo: vea parandamine pärast liitmist [▶ 35:06](https://youtu.be/bVmUyLJuX6I?t=2106)

Kõik kodutöö harud olid peaharuga liidetud, ka need, kus kaust oli valesti nimetatud. Nüüd tuli nimi peaharus ära parandada. Õppejõud näitas seda ekraanil.

### Kloonimine ja fork'imine [▶ 36:42](https://youtu.be/bVmUyLJuX6I?t=2202)

Lihtsam on teha repo kõigepealt GitHubis ja siis oma masinasse kloonida. Teistpidi tee on olemas, kuid juhendid on segasemad.

- **Kloonimine** (`git clone`) teeb repost koopia sinu masinasse. Seotus jääb alles, nii et saad samasse ökosüsteemi teha tõmbetaotlusi.
- **Fork'imine** teeb repost uue, eraldiseisva koopia. See on vajalik siis, kui tahad kellegi teise rakendusest oma versiooni teha ja sellega omasoodu edasi minna.

Õppejõud kasutas VS Code'iga sarnast, kuid kergemat redaktorit. Nende ülesehitus on üldiselt sama: külgpaanil failide explorer ja laiendused, all terminal.

### Terminal ja failipuu ei ole seotud [▶ 40:20](https://youtu.be/bVmUyLJuX6I?t=2420)

Ühel üliõpilasel tuli see õppetund kodutöös välja: **terminal ja redaktori failipuu ei ole omavahel seotud**. Kui liigud failipuus mõnda kausta, jääb terminal ikka sinna, kus ta oli. Kontrolliks on kaks terminali (mitte Giti) käsku:

- **`pwd`** näitab, mis kaustas sa oled,
- **`ls`** näitab, mis selles kaustas on.

Asukoha kuvamiseks on olemas ka terminali pluginaid, neid võib ise otsida.

### Kloonimine olemasolevasse kausta [▶ 41:23](https://youtu.be/bVmUyLJuX6I?t=2483)

`git clone <url>` teeb praeguse kausta sisse uue alamkausta. Kui oled juba enda tehtud tühjas kaustas, tekib nii üks kaust liiga palju. Ilmselt oli see ka üks põhjus, miks mõnel tekkis topeltkaust. Lahendus: lisa käsu lõppu tühik ja punkt, `git clone <url> .`. Siis kloonitakse sisu otse praegusesse kausta.

Nool üles toob terminalis eelmise käsu tagasi ja nool alla järgmise. Nii saab varasemaid käske kiiresti uuesti kasutada.

### Alusta alati `git pull`'iga [▶ 42:24](https://youtu.be/bVmUyLJuX6I?t=2544)

Esimene asi enne tööle hakkamist on **`git pull`**. See tõmbab alla värskeima seisu, sest teised (praegu õppejõud liitmisega) võivad olla repot muutnud. Kui tekib **konflikt**, annab Git sellest teada ja see tuleb lahendada. Konflikte tuleb kursusel kindlasti ette ja nende lahendamist harjutatakse eraldi.

Liidetud kodutöö harud võib nüüd GitHubis ära kustutada, kui sa ei taha neid just ajaloo mõttes alles hoida.

Faile võib liigutada ja ümber nimetada ka Maci Finderis või Windowsi Exploreris. Git märkab muudatused, misjärel tuleb teha tavaline `add`, `commit` ja `push`.

### Tühja kausta Git ei jälgi [▶ 49:07](https://youtu.be/bVmUyLJuX6I?t=2947)

Demo käigus tuli välja, et tühja kausta Git ei salvesta. Alles siis, kui kaustas oli fail, läks commit läbi ja jõudis GitHubi.

Kustutamine käib samamoodi: kustuta, siis `git add .`, `git commit -m "Remove ... folder"` ja `git push`.

### Käskude ühendamine `&&`-ga [▶ 51:25](https://youtu.be/bVmUyLJuX6I?t=3085)

Mitu käsku saab kirjutada ühele reale, kui ühendad need kahe ampersandiga:

```
git add . && git commit -m "Remove sja folder" && git push
```

See on terminali ehk shell'i, mitte Giti võimalus. Teine variant on liikuda nooltega eelmise käsu juurde ja muuta ainult selle sisu. Mõlemad sobivad, vali see, mis tundub kiirem.

## Miks mitte muuta faile otse GitHubis [▶ 52:34](https://youtu.be/bVmUyLJuX6I?t=3154)

Õppejõud küsis, miks ei võiks muudatusi teha otse GitHubi veebiliideses. Tema vastus oli kahene:

- **Pedagoogiline põhjus.** Giti tuleb õppida kasutama nii, nagu see on mõeldud. Töö käib oma masinas ja muudatused lükatakse kesksesse hoidlasse. Ilus graafiline liides võib selle õppimise vahele jätta.
- **Praktiline põhjus.** Põhiliselt töötad oma arvutis. Kui teed vahepeal muudatusi veebis ja unustad enne kohalikku tööd `pull`'i teha, tekib segadus.

Õppejõud tunnistas ausalt, et vastus pole päris veenev, ja palus anda teada, kui keegi leiab parema põhjenduse. Erandjuhul võib veebiliidest kasutada.

## Versioonihaldus VS Code'is [▶ 56:11](https://youtu.be/bVmUyLJuX6I?t=3371)

Versioonihalduse mõte on, et valesti tehtu korral saab ajaloos tagasi minna. Peale terminali saab Gitiga töötada ka graafiliselt. VS Code'is on selleks **Source Control** paneel, kus näeb muu hulgas faili ajalugu ja saab liikuda vanemate commit'ide juurde.

Just seepärast on commit'i arusaadav pealkiri peaaegu kohustuslik. Ajaloost peab olema võimalik leida koht, kus mingi muudatus tehti, ja vajadusel sealt viga otsida.

## Harud ja nende mõte [▶ 59:41](https://youtu.be/bVmUyLJuX6I?t=3581)

**Haru** (branch) näide oli kodutöö ise. Peaharus oli algne seis, kodutöö tehti eraldi harus, paariline vaatas selle üle ning alles heakskiidetud töö liideti peaharuga.

Põhireegel: **peaharu peab alati töötama.** Sinna ei lähe poolikud ega üle vaatamata asjad. Peaharus ei katsetata. Paljudes projektides jõuavad peaharu muudatused automaatselt avalikku rakendusse, nii et katki tehtud peaharu tähendab kõigile nähtavat katkist rakendust.

Iga uue funktsiooni või paranduse jaoks tehakse eraldi haru. Haru nimi on tavaliselt selle funktsiooni või paranduse nimi. Harude nimetamise konventsioonid on samuti kursuse mõistete all kirjas.

### Näide: kaardimakse lisamine [▶ 1:02:59](https://youtu.be/bVmUyLJuX6I?t=3779)

Õppejõud kirjeldas tüüpilist harude elutsüklit:

1. Peaharus on töötav rakendus. Vaja on lisada kaardimakse. Kuna pole teada, kas ja kuidas see õnnestub, tehakse uus haru ingliskeelse nimega.
2. Arendus käib commit'ide kaupa. Kolleeg võib teha alamülesande jaoks oma haru, mis liidetakse kaardimakse haruga.
3. Haru testitakse kõigepealt oma masinas (rakendus lülitatakse selle haru peale), siis testserveris.
4. Kui kõik töötab, liidetakse haru peaharuga, kontrollitakse uuesti ja muudatus läheb live-serverisse.
5. Haru võib kustutada. Ajalugu jääb vaikimisi peaharusse alles, nii et hiljem on näha, mis kus muutus.
6. Kui hiljem leitakse viga, tehakse selle parandamiseks uus haru ja sama ring käiakse uuesti läbi.

Peaharu ära kustutada ei tasu, kuid tänu versioonihaldusele saaks ka selle taastada.

## Tarkvaraarenduse elutsükkel ja kasutaja mõistmine [▶ 1:06:17](https://youtu.be/bVmUyLJuX6I?t=3977)

Õppejõud meenutas eelmise seminari **tarkvaraarenduse elutsüklit**. Kursusel käiakse läbi selle põhipunktid, kuid mitte kõiki põhjalikult. **Kasutajauuringu** ja **persoonadega** siin peaaegu ei tegeleta, sest nende jaoks on eraldi aine.

See osa on aga tegelikult üks olulisemaid. Iga tarkvara tehakse kellegi probleemi lahendamiseks. Suur osa tööst on välja selgitada, mis see probleem on ja mida kasutaja vajab. Tarkvara ei ole vaja niisama, kasutaja on keskmes. Seda kipuvad arendajad unustama.

Ka **disain** ei tähenda õppejõu sõnul kunstinäitust. See on probleemide lahendamise distsipliin. Esteetika on inimestele oluline ja seetõttu peetakse seda sageli disaini kõige tähtsamaks osaks, kuid tavaliselt ei ole see kõige tähtsam.

## Kursuse keskne ülesanne: Haapsalu kolledži tunniplaan [▶ 1:09:33](https://youtu.be/bVmUyLJuX6I?t=4173)

Algselt pidi iga üliõpilane probleemi ise välja mõtlema. Õppejõud muutis plaani: kursuse keskne töö on **Haapsalu kolledži tunniplaani veebilehe** uuendamine. Kliendi soov on lühike: veebileht peab muutuma kaasaegsemaks.

See on tüüpiline ülilühike **kliendi briif**, mis tegelikult ei ütle peaaegu midagi. Mida tähendab „kaasaegsem“? Moeajakirja sirvides seda välja ei selgita. Briifist ei tule välja, milles probleem on. Arendaja ülesanne on kõigepealt uurida, mida klient tegelikult tahab ja mis on tema kasutajate probleem.

Õppejõud tuletas meelde ka seda, et üliõpilased on ise tunniplaani kasutajad, kuid igaüks on vaid **üks kasutaja**. See, mis sinu jaoks kõige rohkem häirib, ei pruugi olla kõige olulisem probleem.

Seminarid järgivad elutsüklit. Esimesel vaadati tööriistu ja suurt pilti, teisel liigutakse kliendi soovist arendusülesandeni. Praegu ollakse **probleemi ja kasutajavajaduste kaardistamise** etapis. Sellest kasvavad välja nõuded, kavandamine, teostus, kontroll, kasutajateni jõudmine ja hooldus. Kogu protsessi kohta käib pidev dokumenteerimine ning kursusel mängitakse läbi Gitis hallatav projekt.

## Tarkvaratiimi rollid [▶ 1:17:31](https://youtu.be/bVmUyLJuX6I?t=4651)

Tarkvaratiimis täidavad eri inimesed eri rolle. Tehisintellekti tõttu on piirid tugevalt hägustunud. Disainikalduvusega inimene peab hakkama rohkem koodiga tegelema ja programmeerija disaini paremini mõistma. Mõlemad peavad aru saama projektijuhtimisest ja projektijuht omakorda rohkemast kui ainult projektijuhtimisest. Kitsa ülesande jaoks inimesi enam ei palgata, sest selleks pole kellelgi raha. Õppejõu sõnul pole see keeruline, kuna tehisintellekt aitab.

Rollid jäävad alles ka siis, kui neid täidab vähem inimesi või osaliselt tehisintellekt:

- **Tellija ehk äriline omanik.** Klient, kes midagi tahab ja kellele lahendus müüakse.
- **Tootejuht ehk tooteomanik.** Teostaja poolel inimene, kes võtab vastutuse selle eest, et tehakse seda, mida telliti.
- **Projektijuht.** Jälgib tähtaegu, suhtleb kliendiga ja peab erinevaid asju meeles.
- **Äri- ja süsteemianalüütik.** Analüüsib, kuidas süsteem peab toimima.
- **UX/UI disainer.** Uurib, mida kasutajad tahavad, ja kujundab selle kasutatavaks. Ta lahendab **kasutajateekonnad**. Näiteks veebipoes: kuidas kasutaja poodi jõuab, toote leiab, korvi paneb ja maksab.
- **Tarkvaraarhitekt.** Kavandab süsteemi suured osad.
- **Tarkvaraarendaja.** Hindab ja teostab arhitekti kavandatut.
- **Testija.** Ükski korralik arendus ei tohiks minna töösse testimata. **Kasutajatest**, kus sihtrühma esindaja proovib lahendust enne avaldamist, on hea. Halb on, kui päris kasutajad avastavad vead pärast avaldamist oma nahal.
- **Käituse eest vastutaja.** Hoolitseb selle eest, et süsteem töötab ja seda hooldatakse.

### Mida tehisintellekt muudab [▶ 1:23:48](https://youtu.be/bVmUyLJuX6I?t=5028)

Selline tiim on väga kallis: kümme, viisteist või rohkemgi inimest. Seetõttu antakse üha rohkem tööd tehisintellektile. See saab testida, luua oma teadmiste põhjal kasutuskogemust ja teha disaini, mis näeb välja nagu enamik teisi saite. Ka analüütiku töös on tal taga tohutud teadmised.

Õppejõu sõnul võib tarkvaraarhitekti olla tehisintellektiga kõige lihtsam asendada, sest tarkvara on väga standardiseeritud. Varem kirjutas arhitekt arendajatele pikki kirjeldusi. Nüüd teeb tehisintellekt lahenduse kohe valmis ja sobimatuse korral uue, sest see on odav.

Inimest on endiselt vaja. Keegi peab tegema otsuseid ja hindama, kas tehisintellekt töötab hästi ja kas pakutu on see, mida tegelikult vaja on. Õppejõud tõi välja ka ohu: tehisintellekt võib pakkuda kõigile sama lahendust, ja siis puudub eristumine. Kursusel mängitakse rollid läbi, et oleks aru saada, mis igaüks neist on.

Seejärel algas paus. Salvestuse lõpus aitas õppejõud mõnda üliõpilast tõmbetaotluse uuesti avamisega. Takistus oli selles, et töö asus vales repos. Kui failid tõsta õigesse reposse, saab õppejõu uuesti ülevaatajaks määrata.

## Lisaks plaanile

- **Arendaja kui kliendi nõuandja** [▶ 13:10](https://youtu.be/bVmUyLJuX6I?t=790). Mõnikord on kliendile kõige kasulikum soovitada tarkvara mitte teha. Lühiajaliselt võib see rahast ilma jätta, kuid ausalt lahendatud probleem toob kliendi tagasi. Õppejõu sõnul kuulub see oskus pigem psühholoogia valdkonda, kuid arendaja peab tänapäeval nägema maailma laiemalt kui varem.
- **Tehisintellekt ja meetodite ümberhindamine** [▶ 20:22](https://youtu.be/bVmUyLJuX6I?t=1222). Agiilsus tekkis kalli koodikirjutamise vastu. Nüüd, kui kood on odav, saab ka kosemudeli moodi terviklahendusi kiiresti genereerida ja meetodit poole pealt vahetada.
- **Lisapunktid eksamil kursuse materjalide parandamise eest** [▶ 1:12:45](https://youtu.be/bVmUyLJuX6I?t=4365). Üks üliõpilane märkas, et materjalides on agiilne arendus eesti keeles, kuid waterfall inglise keeles. Õppejõud nõustus, et õigem oleks kasutada sõna **kosemudel**: „agiilne“ on eesti keelde juba sisse elanud, „waterfall“ mitte. Sellest kasvas välja üldine reegel. Kirjalikud ettepanekud kursuse materjalide parandamiseks (kirjavead, terminid jne) tõmbetaotluse või kommentaarina kursuse repos annavad eksamil plusspunkte. Suulised märkused ei lähe arvesse, kuigi aktiivne osalemine aitab üldiselt parema hindeni.
- **Mõtteline vastus küsimusele, miks mitte muuta faile GitHubis** [▶ 52:34](https://youtu.be/bVmUyLJuX6I?t=3154). Õppejõud tunnistas, et ei ole oma põhjenduses päris kindel, ja kutsus üliõpilasi paremat vastust pakkuma.

## Kodutöö ja järgmised sammud

- **Paranda eelmise kodutöö vead peaharus.** Tee kõigepealt `git pull`, siis paranda kaustade ja failide nimed (ilma topeltkaustata, kokkulepitud kujul) ning tee `add`, `commit` ja `push`.
- **Kustuta GitHubis liidetud kodutöö harud**, kui sa ei taha neid alles hoida.
- **Kirjuta commit'i sõnumid** inglise keeles ja käskivas kõneviisis, nagu kursuse mõistete all kirjas.
- **Vaata üle tarkvaraarenduse meetodid** (kosemudel, agiilne arendus, Scrum, Kanban) ja loe agiilse tarkvaraarenduse manifest.
- **Tutvu teise seminari materjalidega.** Õppejõud laadis üles uuendatud slaidid ja neist lingitud peatükid.
- **Hakka mõtlema Haapsalu kolledži tunniplaani probleemile.** Kursuse keskne töö algab sellest, et selgitad välja, milles kliendi tegelik probleem seisneb.
- Kirjalikud parandusettepanekud kursuse materjalidele annavad eksamil lisapunkte.

## Plaan ja tegelikkus

**Mis jõuti:** slaidide esimene osa, st tarkvaraarenduse elutsükli kordamine, meetodi valik, kursuse keskse ülesande (Haapsalu kolledži tunniplaan) tutvustus ja tarkvaratiimi rollid.

**Mis võttis plaanitust kauem:** esimese kodutöö tagasiside ja Giti töövoo kordamine võttis enne pausi umbes tunni ehk suurema osa salvestusest. Pikalt käsitleti nimetamist, Markdowni koodiplokke, commit'e, harusid ja kloonimist ning tehti terminali demo.

**Mis jäi salvestusest välja:** salvestus lõpeb pausiga. Ei ole teada, kas pärast pausi tehti probleemikandidaatide harjutus ja tiimi töövoog ning kui põhjalikult. Kodutöö (homework.md) täpseid tingimusi salvestatud osas läbi ei käidud.

**Üliõpilaste küsimused ja arusaamatused:**

- Giti ja GitHubi vahe.
- Kuidas parandada viga pärast seda, kui töö on juba peaharuga liidetud.
- Topeltkaustad, mis tekkisid repo nime kordamisest või `git clone` käsust ilma punktita.
- Arusaamatus, et terminal ja failipuu ei ole seotud.
- Muudatused otse peaharus ja mitu tõmbetaotlust sama töö kohta.
- Ülevaataja ligipääsuõigused.
- Tõmbetaotluse uuesti avamine, kui töö oli vales repos.
- Terminoloogia ebajärjekindlus materjalides (waterfall vs kosemudel).

**Õppetunnid järgmiseks korraks:**

- Planeeri esimese kodutöö tagasisidele ja Giti kordamisele seminari algusesse selgelt eraldi aeg (vähemalt 45–60 minutit). Teise võimalusena käi Giti põhitõed läbi juba enne esimest kodutööd.
- Lisa esimese kodutöö juhendisse näide õigest kaustastruktuurist ja `git clone <url> .` variant, et vältida topeltkaustu.
- Ühtlusta materjalides terminid (kosemudel) ja lae seminari materjalid üles enne seminari.
- Mõtle läbi veenev põhjendus, miks faile ei muudeta GitHubi veebiliideses. Sellele küsimusele polnud seekord head vastust.
- Kui keskne ülesanne asendab individuaalse probleemi valiku, anna sellest teada enne seminari, et jääks aega probleemikandidaatide harjutuseks.
