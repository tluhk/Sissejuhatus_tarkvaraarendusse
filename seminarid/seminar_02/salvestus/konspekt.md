<!-- loengud:konspekt osad=1,2 (automaatne; kui muudad käsitsi, kustuta see rida – siis tööriist seda üle ei kirjuta) -->
# Konspekt: Seminar 2: kliendisoovist arendusülesandeni

> Automaatne kokkuvõte seminari salvestusest (kõnetuvastus + keelemudel). Võib sisaldada ebatäpsusi – täpse sõnastuse leiad transkriptsioonist.

Seminari eesmärk oli jõuda ebamäärasest kliendisoovist konkreetsete, jälgitavate arendusülesanneteni ning panna tiimid tööle kursuse keskse projekti kallal. Plaanis olid slaidid, probleemikandidaatide harjutus ja tiimi töövoog. Tegelikult kulus seminari esimesest poolest suurem osa esimese kodutöö tagasisidele ja Giti töövoo kordamisele. Uue teemana jõuti tarkvaraarenduse meetodite, rollide ja kliendi probleemi mõistmiseni. Teises pooles moodustati tiimid, loodi repod ja Kanbani tahvlid ning alustati probleemikandidaatide ülesandega. Release'i ja epic'ute teema jäi põgusaks.

## Kodutöö tagasiside ja nimetamise kokkulepped [▶ 1. osa 0:04](https://youtu.be/bVmUyLJuX6I?t=4)

Esimese kodutöö pull request'i suutsid ära teha kõik, mida õppejõud pidas esimese korra kohta heaks tulemuseks. Õppejõud möönis, et kirjutas tagasisidet kiirustades. Kui keegi leiab, et kommentaar oli asjatu ja nõutud asi oli tegelikult olemas, tasub sellest julgelt teada anda.

Kõige olulisem tähelepanek puudutas **nimetamist**. Faili- ja kaustanimed peavad olema täpselt sellised, nagu ülesandes kokku lepitud. `kodutoo01`, `kodutoo_01` ja `kodutoo-01` on kolm eri nime, samuti on oluline suur- ja väiketäht. Praegu ei pruugi viga suuri tagajärgi tuua, kuid hiljem võib see saada määravaks. Näiteks Reactis on nimetamise konventsioonid kohustuslikud ja vale nimega komponendi korral võib rakenduse ehitamine ebaõnnestuda.

Üldreeglid:
- **ära kasuta täpitähti ega tühikuid**. Veebis asendatakse tühik kujul `%20` ja mitme tühikuga nimi muutub loetamatuks;
- **ära korda repo nime kaustana**. Kui ülesandes on tee kujul `repo-nimi/kaust/fail`, tähistab esimene osa repot ennast ja repo sisse ei ole vaja teha samanimelist kausta. Mitmel üliõpilasel oli selline lisakaust tekkinud ja see tuleb ära parandada.

Kokkulepped aitavad teha koodi loetavamaks ja selgemaks. Mõnes keeles on need paika pannud juba keele loojad.

## Markdowni koodiplokid peavad olema suletud [▶ 1. osa 7:02](https://youtu.be/bVmUyLJuX6I?t=422)

Paaristöödes tuli ette Markdowni viga. **Koodiplokk** algab kolme tagurpidi ülakomaga (*backtick*) ja peab samamoodi ka lõppema. Kui sulgevad märgid puuduvad, vormindatakse kogu ülejäänud dokument koodina. Avavate märkide järele võib kirjutada keele nime, näiteks `css` või `html`, ja siis oskab redaktor või GitHub koodi süntaksi järgi värvida.

Kui GitHubis ei paista dokument korralikult vormindatuna, vaid kogu tekst näeb ühesugune välja, on tõenäoliselt kuskil koodiplokk alanud, aga lõppemata jäänud. Sama põhimõte kehtib üldiselt: mis algab, peab ka lõppema. Seda tuntakse juba Pythonist.

## Reflektsioon kodutöös [▶ 1. osa 9:23](https://youtu.be/bVmUyLJuX6I?t=563)

Mitu tööd olid põhjalikult kommenteeritud ja neist oli näha, et materjal on läbi töötatud. Esimesed kodutööd on lihtsad, seega kaalub **reflektsioon** seal palju: mida sa tegid ja mida teada said. Näiteks tarkvaraarenduse meetodite videote puhul ei piisa linkidest. Kirja tuleb panna, mida videost teada saadi.

## Tarkvaraarenduse meetodid ja nende mõte [▶ 1. osa 11:54](https://youtu.be/bVmUyLJuX6I?t=714)

Kursus ei keskendu edaspidi meetoditele, kuid märksõnad **kosemudel** (*waterfall*), **agiilne arendus**, **Scrum** ja **Kanban** peavad olema tuttavad. Kui need tundusid uued, tasub need kodus järele vaadata. Kolme aasta pärast tööle minnes ei tohiks juhtuda, et keegi nimetab mõnda neist ja sa ei tea, millest jutt käib.

Õppejõud rõhutas, et päriselus järgitakse meetodeid täpselt peamiselt väga suurtes ja start-up'ilikes ettevõtetes. Sageli on need segamini. Meetodi järgimine ei ole aga eesmärk omaette. **Tarkvaraarenduse eesmärk on lahendada kellegi probleem** ja tarkvara on üks võimalik lahendus. Mõnikord teenib arendaja kliendi huve kõige paremini sellega, et soovitab tal tarkvara üldse mitte teha. Lühiajaliselt võib see tähendada raha kaotust, kuid rahulolev klient tuleb tagasi. Arendajal on vaja raha ja see tuleb kliendilt, seega peab kliendil olema hea meel seda maksta. Õppejõu sõnul peavad arendajad nägema maailma üha laiemalt, sest koodi kirjutamine on üha väiksem osa nende tööst.

### Kosemudel ja agiilne arendus [▶ 1. osa 15:46](https://youtu.be/bVmUyLJuX6I?t=946)

Kosemudelis lepitakse alguses kokku, mida tehakse, ning ehitatakse kõik valmis. Tulemus selgub alles lõpus, kui vajadused võivad olla juba muutunud. See muudab arenduse kalliks. Vastukaaluna tekkisid agiilsed meetodid. Tarkvaraarendajal tasub läbi lugeda **agiilse tarkvaraarenduse manifest** (*Agile Manifesto*).

Üliõpilased nimetasid agiilse lähenemise eelistena suhtlust ja paindlikkust. Õppejõud lisas **MVP** (*minimum viable product*) mõtte. Kõigepealt tehakse valmis minimaalne töötav tükk ja seejärel ehitatakse sellele juurde. Algusest peale on olemas midagi, mis töötab, vead tulevad kohe välja ja palju raha ei ole veel kulunud.

### Kus agiilne sobib ja kus mitte [▶ 1. osa 17:59](https://youtu.be/bVmUyLJuX6I?t=1079)

Õppejõud palus arutleda, kuhu agiilne lähenemine ei sobi, ja märkis, et ühte õiget vastust ei ole. Tema näide oli riigi e-teenus, kus taotletakse näiteks reisidokumenti. Selline teenus peab kohe arusaadavalt töötama. Poolik ja „ligadi-logadi“ mulje kahjustab usaldust ja mainet ning võib meelitada ligi pahatahtlikke, kes hakkavad otsima teisi pooleli jäänud kohti.

Start-up seevastu peab investorile kiiresti näitama, et idee toimib. Tal pole raha ehitada esmalt suurt valmislahendust ja siis avastada, et investor ei taha selle eest maksta. Kumbki lähenemine ei ole vale, tuleb mõelda, mis kuhu sobib.

### AI muudab koodi kirjutamise odavaks [▶ 1. osa 20:22](https://youtu.be/bVmUyLJuX6I?t=1222)

Agiilsed meetodid tekkisid suuresti seetõttu, et koodi kirjutamine oli kallis ja pidi kiiresti selguma, kas ideel on mõtet. Nüüd on **koodi kirjutamine odav**, kuigi tarkvaraarendus tervikuna ei ole. Ühe prompt'iga saab kiiresti teha kosemudeli moodi tervikliku lahenduse. Kui see kliendile ei sobi, saab kohe teha uue.

Seepärast ei saa enam öelda, et agiilne on lihtsalt moodsam. Sobiv lähenemine tuleb leida koos kliendiga. Tänapäeval saab ka poole pealt hobuseid vahetada: osa tehakse agiilselt valmis ja ülejäänu genereeritakse ühe korraga. Otsus tehakse tiimina ja **klient on osa tiimist**.

## Ülesanded, piletid ja issue'd [▶ 1. osa 21:37](https://youtu.be/bVmUyLJuX6I?t=1297)

Üks üliõpilane oli varem kasutanud Jirat. Õppejõud selgitas, et Jira on Atlassiani toode. Samasse perre kuuluvad ka Confluence ja Bitbucket. Eri süsteemides nimetatakse ühte tööülesannet erinevalt: GitHubis **issue**, Jiras **ticket** ehk **pilet**. Põhimõte on sama. Ülesanne peab olema võimalikult kompaktne, sellel on vastutaja ja tähtaeg ning seda saab jagada alamülesanneteks.

Kodutöö oli samamoodi üles ehitatud: issue tähtajaga, üliõpilane vastutajana, kaaslane ülevaatajana. Valmis töö haru liidetakse peaharuga. Mõnel oli tehtud mitu pull request'i. Õppejõud palus edaspidi ühega hakkama saada, siis on vähem sodi.

## Giti põhitöövoog ja commit'id [▶ 1. osa 24:59](https://youtu.be/bVmUyLJuX6I?t=1499)

Faili salvestamine ei tähenda veel midagi versioonihalduse mõttes. Töövoog on järgmine:

1. `git add`. Punkt lisab kõik muudatused, failinimi ainult selle faili. Failinime tasub kasutada siis, kui kõike ei taha versioonihaldusse panna. Väikestes projektides kasutab ka õppejõud punkti.
2. `git commit -m "..."` salvestab muudatuse koos **commit'i sõnumiga**, mis ütleb lühidalt ja arusaadavalt, mida tehti. Pikema muudatuse puhul võib pealkirjale lisada kirjelduse.
3. `git push` lükkab muudatused kohalikust masinast kaugrepoks. Kui kaugrepot pole, pole ka push'i vaja.

**Commit peaks olema üks kompaktne loogiline muudatus**, üks terviklik alamfunktsionaalsus, mitte üksik näpuliigutus ega hunnik sõltumatuid asju. Kui midagi läheb katki, saab sellise commit'i juurde tagasi minna ja mõjutatakse ainult seda funktsionaalsust. Õppejõud ütles, et järgmise semestri ainetes hindab ta tööd ka commit'ide arvu järgi. See näitab, et iga loogilise sammu jaoks on tehtud eraldi commit ja et tudeng on töösse süvenenud. Õppejõu sõnul peaks ka päris arendus täpselt nii käima.

Sõnum ei tohi olla suvaline, näiteks „uuendasin seisu“. Sõnumis võib viidata ka issue'le, näiteks märkida, et commit sulgeb konkreetse issue. Nii on hiljem lihtsam leida koht, kuhu vea parandamiseks tagasi minna.

### Git ja GitHub ei ole sama asi [▶ 1. osa 31:52](https://youtu.be/bVmUyLJuX6I?t=1912)

Üliõpilased küsisid, mis vahe on Gitil ja GitHubil. **Git** on versioonihaldussüsteem, mis võib asuda kus tahes: sinu arvutis või serveris. **GitHub** on üks teenus, kus Giti repot hoitakse kaugelt ligipääsetavas kohas ja millel on lisafunktsioone. Git on alus ja GitHub üks keskkond selle kasutamiseks. Kuna Git ja GitHub on kolm aastat õppetöö tugisammas, tasub need hästi selgeks saada. Kui midagi jääb segaseks, küsi otse, kirjuta või küsi kaaslastelt.

### Ligipääs ülevaatajale [▶ 1. osa 33:10](https://youtu.be/bVmUyLJuX6I?t=1990)

Ühel juhul ei pääsenud ülevaataja repole ligi. Võimalusi on kaks: teha repo avalikuks või anda ülevaatajale konkreetselt juurdepääs.

## Demo: kloonimine, terminal ja muudatuste tegemine [▶ 1. osa 36:42](https://youtu.be/bVmUyLJuX6I?t=2202)

Õppejõud näitas läbi, kuidas parandada vale nimega kausta pärast seda, kui ta oli kodutööd peaharuga liitnud.

**Kloonimine ja fork'imine.** Repo on lihtsam luua kõigepealt GitHubis ja seejärel kloonida. Arvutis loomise ja hiljem üleslaadimise juhendid on segasemad. **Kloonimisel** tehakse repost koopia oma masinasse, aga ökosüsteem jääb samaks ja muudatused saab pull request'iga algsesse reposse tagasi saata. **Fork** loob uue iseseisva koopia. Seda kasutatakse siis, kui tahetakse kellegi teise rakendusest teha oma versioon ja end algsest lahti siduda.

**Terminal ja failipuu ei ole seotud** [▶ 1. osa 40:20](https://youtu.be/bVmUyLJuX6I?t=2420). Üks kodutöö-õppetund oli see, et VS Code'i failipuus liikumine ei muuda terminali asukohta. Asukohta näitab `pwd` ja kausta sisu `ls`. Need on terminali käsud, mitte Giti omad. Asukoha näitamiseks saab terminalile lisada ka plugina. Noolega üles ja alla saab liikuda eelmiste käskude vahel.

**`git clone <url> .`** [▶ 1. osa 42:24](https://youtu.be/bVmUyLJuX6I?t=2544) Kui oled juba enda loodud kaustas, loob tavaline `git clone` sinna veel ühe alamkausta. Võimalik, et sealt tekkiski mõnel üleliigne kaust. Kui lõppu lisada tühik ja punkt, kloonitakse sisu otse praegusesse kausta, eeldusel et see on tühi.

**Enne töö alustamist tee `git pull`** [▶ 1. osa 43:28](https://youtu.be/bVmUyLJuX6I?t=2608). Õppejõud on muudatusi peaharuga liitnud, seega pole kohalik seis enam värske. Kui tekib konflikt, annab Git sellest teada. Konfliktide lahendamiseni jõutakse hiljem. Pärast liitmist võib kodutöö harud GitHubis kustutada, kui neid just mälestuseks alles hoida ei taha.

Faile võib ümber nimetada ja liigutada ka Finderis või Exploreris. Seejärel tehakse tavaline `git add`, `commit` ja `push`. Õppejõu demos ei läinud tühi kaust commit'i ja tulemuse andis alles siis, kui kaustas oli sisu [▶ 1. osa 49:07](https://youtu.be/bVmUyLJuX6I?t=2947).

### Commit'i sõnumi vorm [▶ 1. osa 44:32](https://youtu.be/bVmUyLJuX6I?t=2672)

Commit'i sõnumid kirjuta **inglise keeles**. Tarkvaraarendusel ei ole rahvust ja järgmine arendaja võib olla teisest riigist. AI saab küll igast keelest aru, kuid korrektne keel ja stiil on endiselt hea tava. Sõnum kirjutatakse **käskivas kõneviisis**: mitte „lõin kausta“, vaid „loo kaust“, ehk inglise keeles *Add folder*, *Remove folder*. See on kursusel kohustuslik. Täpsemad juhised ja põhjendused, miks see nii on, leiab kursuse materjalide mõistete (*concepts*) osast commit'ide alt.

### Käskude aheldamine [▶ 1. osa 51:25](https://youtu.be/bVmUyLJuX6I?t=3085)

Käske saab kirjutada ühele reale: `git add . && git commit -m "Remove folder" && git push`. `&&` ei ole Giti, vaid shell'i süntaks ja tähendab „ja siis järgmine käsk“. Märke on kaks, et neid ei aetaks segi muus tähenduses kasutatava üksiku märgiga (sarnaselt Pythoni `==`-ga). Teine võimalus on noolega eelmise käsu juurde liikuda ja selle sisu muuta.

### Miks mitte muuta faile GitHubi veebis? [▶ 1. osa 52:34](https://youtu.be/bVmUyLJuX6I?t=3154)

Õppejõud küsis, miks ei tasu teha muudatusi otse GitHubi veebiliideses, ja tunnistas, et päris kindlat vastust tal pole. Põhjusi on kaks. Pedagoogiline põhjus: tuleb õppida Giti kasutama nii, nagu see on mõeldud. Töö käib oma masinas ja muudatused lükatakse kesksesse hoidlasse. Graafiline liides on mugav, kuid nii jääb Git selgeks õppimata. Praktiline põhjus: kui töötad peamiselt oma arvutis ja muudad vahepeal midagi veebis, ununeb kergesti `pull` ja seisud lähevad lahku. Veebis muutmine on lubatud erandjuhul.

### Graafiline source control [▶ 1. osa 56:11](https://youtu.be/bVmUyLJuX6I?t=3371)

VS Code'il ja enamikul sellel põhinevatel redaktoritel on **Source Control** paneel. Seal näeb commit'ide ajalugu ja saab liikuda varasemate seisude juurde. Seepärast on arusaadavad commit'i pealkirjad praktiliselt kohustuslikud, sest muidu ei leia õiget kohta üles.

## Harud: miks peaharus ei arendata [▶ 1. osa 59:41](https://youtu.be/bVmUyLJuX6I?t=3581)

Kodutöös oli peaharus algne seis ja töö tehti eraldi harus. Valmis haru vaatas paariline üle ja kiitis heaks või leidis vigu. Alles seejärel liideti see peaharuga.

**Peaharu (`main`) peab alati olema töötav ja valmis.** Sinna ei liideta poolikut ega heaks kiitmata tööd. Kui peaharus katsetada, võib midagi katki minna. Kui peaharu muudatused jõuavad automaatselt avalikku rakendusse, läheb katki kõigile nähtav rakendus.

Õppejõu näide [▶ 1. osa 1:02:59](https://youtu.be/bVmUyLJuX6I?t=3779): rakendusse on vaja kaardimakset. Arendaja teeb uue haru (nimi inglise keeles, nt kaardimakse kohta) ja arendab seal commit'ide kaupa. Vahepeal võib lisanduda kolleeg, kes teeb alamosa omas harus. Peaharus käib samal ajal muu töö edasi. Valmis haru kontrollitakse esmalt oma masinas (rakendus lülitatakse selle haru peale), siis testserveris, seejärel liidetakse peaharuga, kontrollitakse uuesti ja lükatakse live-serverisse. Pärast liitmist võib haru kustutada. Haru nimi on tavaliselt funktsionaalsuse või paranduse nimi ja harude nimetamise konventsioonid on samuti mõistete all kirjas.

Vaikimisi liidetakse peaharusse ka haru ajalugu, seega on hiljem näha, kus mida muudeti. Kui kuskil tekib viga, tehakse parandamiseks uus haru. Kui peaharu kogemata kustub, saab selle versioonihalduse abil tagasi.

## Tarkvara elutsükkel ja probleemi keskne roll [▶ 1. osa 1:06:17](https://youtu.be/bVmUyLJuX6I?t=3977)

Eelmisel korral vaadati **tarkvaraarenduse elutsüklit**. Kursus käib selle põhietapid läbi, aga mitte kõiki põhjalikult. **Kasutajauuringu** ja persoonade jaoks on eraldi aine. Õppejõud rõhutas siiski, et see on üks olulisemaid osi. Tarkvara ei ole vaja niisama, see peab lahendama kellegi konkreetse probleemi. Seega on suur osa tööst probleemi ja kasutaja vajaduste väljaselgitamine, mitte koodi kirjutamine. See ununeb arendajatel kergesti.

**Disain** ei tähenda kunstinäitust, vaid probleemide lahendamise distsipliini. Esteetika on inimestele oluline ja seetõttu peetakse seda sageli disaini peamiseks osaks, kuid tavaliselt see seda ei ole. Implementeerimisest, testimisest ja töösse laskmisest räägitakse kursusel põgusalt.

Praegu ollakse elutsüklis **probleemi ja kasutajavajaduste kaardistamise** etapis. Sellest kasvavad välja nõuded, kavandamine, teostus, kontroll ja kasutusse andmine.

## Kursuse keskne töö: Haapsalu kolledži tunniplaan [▶ 1. osa 1:09:33](https://youtu.be/bVmUyLJuX6I?t=4173)

Algne plaan oli, et igaüks mõtleb ise probleemi välja. Õppejõud muutis seda: kogu kursuse keskne töö on nüüd **Haapsalu kolledži tunniplaan**. Kliendi soov on, et tunniplaani veebileht muutuks kaasaegsemaks.

See on tüüpiline ülilühike **kliendi bríif**: see ei ütle praktiliselt midagi. Mida tähendab „kaasaegsem“? Kas vaadata moeajakirjast, mis on moes? Milles on tegelik probleem? Arendaja ülesanne on kõigepealt välja selgitada, mida klient tegelikult tahab. Üliõpilased on ise tunniplaani kasutajad, kuid igaüks neist on vaid üks kasutaja ja see, mis just teda häirib, ei pruugi olla kõige olulisem probleem. Kursusel mängitakse see protsess põgusalt läbi ja dokumenteeritakse kõik Giti projektis.

## Rollid tarkvaraarenduses [▶ 1. osa 1:17:31](https://youtu.be/bVmUyLJuX6I?t=4651)

Rollide piirid on AI tõttu tugevalt hägustunud. Disainikaldega inimene peab rohkem koodiga tegelema, programmeerija peab disaini paremini mõistma, projektijuht peab tehnikast rohkem aru saama ning disainer ja arendaja projektijuhtimisest. Kedagi ei võeta enam tööle kitsa ülesande jaoks, sest selleks pole kellelgi raha. Õppejõu sõnul ei ole see keeruline ja AI aitab.

Klassikalise tiimi rollid:
- **tellija** ehk äriline omanik – klient, kes midagi tahab;
- **tootejuht / tooteomanik** – teostaja poolel, võtab enda kanda selle, mida tellija tahab, ja kontrollib, mida tegelikult telliti;
- **projektijuht** – jälgib tähtaegu, suhtleb kliendiga, vastutab;
- **äri- ja süsteemianalüütik** – analüüsib, kuidas süsteem peab toimima;
- **UX- ja UI-disainer** – sageli üks inimene. Selgitab välja, mida kasutajad tahavad, kujundab **kasutajateekonnad** (nt veebipoes: kuidas kasutaja kauba leiab, korvi paneb ja maksab) ning nende välimuse;
- **tarkvaraarhitekt** – kavandab süsteemi suured osad;
- **tarkvaraarendaja** – hindab ja teostab;
- **testija** – korralik arendus ei lähe töösse testimata. **Kasutajatest** (sihtgrupi esindaja proovib enne live'i minekut) on teine asi kui see, et päris kasutaja peab vigu „omal nahal“ kogema;
- **käitaja** – vastutab, et süsteem töötab ja seda hooldatakse.

Selline tiim, kümme kuni viisteist inimest või rohkemgi, on väga kallis. Seetõttu võtab AI suure osa tööst üle: testimise, tüüpilise UX-i, disaini (enamik saite näeb nagunii sarnane välja), analüüsi ja eriti arhitektuuri, sest tarkvara on hästi standardiseeritud. Varem kirjutas arhitekt arendajatele pikki kirjeldusi. AI ei pea iseendale kirjeldama, ta teeb kohe valmis ja vajadusel uuesti. Rollid jäävad siiski alles. Keegi peab otsuseid langetama ja hindama, kas AI pakutu on see, mida on vaja. Muidu pakub AI kõigile sama ja eristumist ei teki.

## Tiimide moodustamine ja repo loomine [▶ 2. osa 1:08](https://youtu.be/K8tL1OkOjDA?t=68)

Üliõpilased jagunesid **3–4-liikmelisteks tiimideks** ja valisid tiimile numbri kujul `tiim01`, `tiim02` jne, nii et numbrid ei korduks. Kursuse GitHubi organisatsiooni alla loodi tiimi repo. Tekkis tehnilisi takistusi: osa linke oli vananenud ja üks repo tuli vale nime tõttu kustutada või ümber nimetada.

## Esimene tiimiülesanne: probleemikandidaadid [▶ 2. osa 11:11](https://youtu.be/K8tL1OkOjDA?t=671)

Ülesanne:
1. Sisusta repo: kirjuta **README**, mis selgitab, mis projektiga on tegu.
2. Iga liige pakub välja **kolm probleemikandidaati**: mis on praeguses tunniplaanis halvasti.
3. Töö käib nagu kodutöös: igaühel on oma issue, sellest tehtud haru, pull request ja kaaslase ülevaatus, seejärel liitmine peaharuga.

Näidiseks on organisatsioonis **TeamDemo tunniplaani** repo [▶ 2. osa 14:47](https://youtu.be/K8tL1OkOjDA?t=887). See ei pea olema üks-ühele sama. README peab andma ülevaate projektist: kes on tiimis, mis toimub ja kuidas asju kasutatakse. Midagi ei ole vaja välja mõelda. Täna piisab, kui on kirjas **projektijuht** ja tiimiliikmed. Vaja on ka **release manager'it**, sest iga kodutöö lõpeb release'iga. Rolle võib kodutööde kaupa vahetada ja muutused jäävad ajalukku näha.

## Kanbani tahvel GitHub Projectsis [▶ 2. osa 18:07](https://youtu.be/K8tL1OkOjDA?t=1087)

Issue'd loodi läbi **GitHub Projectsi** tahvli. **Kanban** pärineb Toyotast, kus see oli algselt seinal post-it lehtedega. Nüüd on see digitaalne. See on agiilse arenduse tehnika, mille juures on hästi näha, kes mida teeb ja kui kaugel töö on.

Tüüpilised veerud:
- **Backlog** – tööd, mis tuleb millalgi teha;
- **In progress** – keegi tegeleb sellega;
- **In review** – tegija on lõpetanud ja määranud ülevaataja;
- **Done** – ülevaatus on läbitud.

Projekt luuakse menüüst *New project* ja mallide hulgast sobib Kanban hästi. Jälgi, et projekt oleks seotud tiimi repoga. Vaadet saab vahetada (tabel, tahvel, roadmap) [▶ 2. osa 23:34](https://youtu.be/K8tL1OkOjDA?t=1414). Veerge võib lisada või eemaldada. Kas kasutada *Backlog* või *To do* veergu, on tiimi kokkuleppe asi. *To do* sobib näiteks järgmise etapi tööde jaoks. Ainult „teha“ ja „tehtud“ on liiga vähe, sest siis ei ole näha, kus keegi vahepeal on.

## Ülesannete jagamine ja piletite kirjeldamine [▶ 2. osa 26:08](https://youtu.be/K8tL1OkOjDA?t=1568)

Igaüks pakub oma kolm probleemikandidaati iseseisvalt, ilma omavahel arutamata. Päriselus muidugi arutataks. Pärast valitakse kõigi kandidaatide hulgast ühisosa, millest saab edasi liikuda.

Piletite nimed peaksid tiimis olema ühtse kujuga ja sisaldama liikme nime ning ülesannet, näiteks „Koosta [nimi] probleemikandidaadid“, et igaüks leiaks oma pileti kiiresti. Pilet lisatakse tahvlil *Add item* kaudu, misjärel määratakse vastutaja (*Assignee*). Õppejõud märkis, et lisamise riba on kergesti märkamatu.

Õppejõud rõhutas **kirjelduse** tähtsust [▶ 2. osa 28:15](https://youtu.be/K8tL1OkOjDA?t=1695). Näitekirjeldus: leia kolm probleemi, mis praeguses tunniplaanis on halvasti; kasuta oma kogemust, küsi grupikaaslastelt ja küsitle tellijat. Pileti saaja peab kirjeldusest aru saama, mida temalt oodatakse. Mõistlik on kirjutada kõigile ühine põhi. Kui keegi läheb koju ja hakkab pool tundi enne tähtaega tegema tööd, mis peaks võtma kaheksa tundi, ei mäleta ta seminarist midagi. Seepärast tuleb arutelu tulemus kohe selgelt kirja panna. See on **dokumenteerimise** mõte. Silte (*labels*), prioriteete ja verstaposte (*milestones*) praegu ei kasutata.

**Epic'utest** räägiti vaid põgusalt [▶ 2. osa 32:01](https://youtu.be/K8tL1OkOjDA?t=1921). Suurema tiimiülesande võib jagada alampiletiteks. Seekord seda keerukuse pärast ei tehtud.

### Kaustastruktuur [▶ 2. osa 33:07](https://youtu.be/K8tL1OkOjDA?t=1987)

Tiim peab läbi mõtlema kaustade struktuuri. Õppejõu soovitus oli teha ülesande põhine kaust, näiteks `01-probleemid`. Number näitab järjekorda, nii et kaustad ei sorteeru tähestiku järgi segamini. Sõna ütleb, mida kaustas tehti. Iga liige paneb sinna oma Markdowni faili. Failinimede kuju lepitakse tiimis kokku: ilma tühikute ja täpitähtedeta, sõnad kriipsudega eraldatud.

## Tiimi töövoog: issue'st haruni ja tagasi [▶ 2. osa 35:19](https://youtu.be/K8tL1OkOjDA?t=2119)

1. Klooni tiimi repo oma arvutisse.
2. Ava oma pilet ja vali **Create branch for this issue**. Kontrolli, et lähteharu oleks `main`.
3. Tee arvutis `git pull` ja lülitu uuele harule. GitHub pakub selleks valmis käsu, mille saab terminali kopeerida. Haru vahetamiseks sobib `git checkout <haru>` või uuem `git switch <haru>` [▶ 2. osa 39:10](https://youtu.be/K8tL1OkOjDA?t=2350).
4. Tee töö oma harus nagu kodutöös.
5. Kui kolm probleemikandidaati on valmis, vaatab kaaslane pull request'i üle ja pärast kinnitamist liidetakse see peaharuga.

**Konfliktid** tekivad siis, kui mitu inimest muudab samal ajal sama faili. Kui igaüks töötab oma failiga, konflikte ei teki. Konfliktide lahendamist vaadatakse hiljem. Kui iga liige loob ühise kausta ise oma harus, võib sellest tekkida segadus. Seepärast soovitas õppejõud, et üks inimene loob kausta kohe peaharusse ja teised saavad selle kloonimisel kätte.

Õppejõud julgustas: kes saab asjast juba paremini aru, aidaku teisi, sest kaaslane seletab sageli lihtsamini [▶ 2. osa 40:11](https://youtu.be/K8tL1OkOjDA?t=2411). Midagi ei saa valesti teha. Ollakse alguses ja kui midagi läheb nässu, võib uuesti alustada.

### Demo ja lisanipid [▶ 2. osa 42:15](https://youtu.be/K8tL1OkOjDA?t=2535)

- Ära tee repot teise repo sisse. Alamrepod on võimalikud, aga tülikad ja tekitavad segadust.
- Töö allikas on organisatsiooni repo, mitte enda arvuti. Kohaliku koopia võib panna kuhu tahes, kuid mõistlik on hoida projekte ühes kohas.
- Õppejõud näitas uuesti `git clone <url> .` käsku, mis kloonib tühja kausta sisse ilma alamkaustata.
- **Giti repoga kausta võib vabalt liigutada**, sest Giti info asub peidetud failides kausta sees. Üksikuid faile kaustast välja tõstes see seos kaob.

## Ülesande kokkuvõte ja release [▶ 2. osa 1:01:14](https://youtu.be/K8tL1OkOjDA?t=3674)

Õppejõud lisas, et README tegemiseks peab olema ka eraldi pilet ja vastutaja, isegi kui seda tehakse koos. Tervikuna tuleb:
1. luua repo;
2. luua projekt (Kanbani tahvel);
3. luua ülesanded (piletid);
4. luua ülesande kaust;
5. kloonida repo oma arvutisse;
6. lahendada määratud ülesanded;
7. lasta ülesanded üle vaadata ja kinnitada;
8. luua release.

Töö käib Markdowni failides.

**Release** [▶ 2. osa 1:05:10](https://youtu.be/K8tL1OkOjDA?t=3910) on tarkvara hetkeseisu ehk versiooni salvestus. Release võib olla valmis või **release candidate**. Kursusel tehakse kohe valmis release'id. Release'ile lisatakse **tag** ehk versiooninumber, näiteks 0.1.0. Release tehakse siis, kui tiim on enne tähtaega üle vaadanud, et kõik on korras. Sellele lisatakse kirjeldus, mida tehti, ja lingid ülesannetele. Õppejõud lubas lisada eraldi release'i juhendi ja ütles, et selle pärast ei pea praegu muretsema.

## Lisaks plaanile

**Kas „waterfall“ või „kosemudel“?** [▶ 1. osa 1:12:45](https://youtu.be/bVmUyLJuX6I?t=4365) Üks üliõpilane küsis, miks materjalides on eestikeelne „agiilne“, aga ingliskeelne „waterfall“. Õppejõud nõustus, et korrektne oleks kasutada eesti terminit **kosemudel**. „Agiilne“ on eesti keelde juurdunud, „waterfall“ mitte. Sellest kasvas välja oluline kokkulepe: **ettepanekud kursuse materjalide parandamiseks annavad eksamil plusspunkte.** Need võivad olla kirjavead või sisulised ettepanekud. Arvesse lähevad ainult kirjalikud ettepanekud: pull request kursuse reposse või kommentaar. Suuline märkus jälge maha ei jäta. Aktiivne osalemine aitab muidugi ka muul moel.

**Töömeetodist kliendiga** [▶ 1. osa 1:16:04](https://youtu.be/bVmUyLJuX6I?t=4564). Kliendiga ei pea arutama, kas töö käib agiilselt või kosemudeli järgi, kuigi kliendid on tänapäeval üsna teadlikud. Piisab küsimusest, kas teha esmalt väike osa ja seda täiendada või teha kohe terviklik lahendus. Eesmärk on saada rakendus võimalikult väikese kuluga valmis.

**Inimtiim ja AI-agendid töötavad samamoodi** [▶ 2. osa 1:08:44](https://youtu.be/K8tL1OkOjDA?t=4124). Konventsioonid ja harude kaupa töötamine on vajalikud ka siis, kui tööd teevad mitu AI-agenti eri harudes. Muudatused peavad olema väikesed ja selged, mitte üks keeruline hunnik ühes kohas.

**Klient ei tea, mida „kaasaegne“ tähendab** [▶ 2. osa 1:10:10](https://youtu.be/K8tL1OkOjDA?t=4210). Õppejõud tegi selgeks, et ta on selles projektis klient: tal on soov, kuid ta ei ole spetsialist ega tea, mis on kõige parem. Tema arvates on praegune leht ilus, punane ja puhas. Tiimi ülesanne on aru saada, mis on tegelikult halvasti, ja jõuda kliendiga kokkuleppele enne, kui algab suur ja kallis töö. Tehniline lahendus on alles tagaplaanil. Teadmise allikad on oma kogemus, tiimikaaslased kui kasutajad ja klient, kellele võib kirjutada. Kõige lihtsam küsimus kliendile on: mida „kaasaegne“ tähendab?

Klassikaline protsess on järgmine: kliendi briifimine (pikk kohtumine, kus selgitatakse probleem ja sihtgrupp), **kasutajaintervjuud**, probleemide tuletamine, lahenduste pakkumine, prototüüpimine ja testimine. Alles seejärel algab programmeerimine. Tehniline osa on AI-ga palju lihtsamaks muutunud. Palju dokumentatsiooni kirjutati varem selleks, et teine inimene aru saaks. Nüüd kirjutab AI suure osa dokumentatsioonist, kuid sageli liiga palju ja mõttetult. Õppejõu sõnul ei ole see mustvalge: inimestele mõeldud dokumentatsiooni on endiselt vaja ja poole aasta pärast võib AI-ga töötamine olla jälle teistsugune.

**Tehnilised probleemid kodutöödega** [▶ 1. osa 1:27:23](https://youtu.be/bVmUyLJuX6I?t=5243). Pausi ajal selgus, et pull request'e ei saanud uuesti avada, kui töö asus valesti teises repos. Lahendus oli tõsta failid õigesse kohta ja teha uus pull request, määrates õppejõu ülevaatajaks.

## Kodutöö ja järgmised sammud

- Paranda esimese kodutöö vale nimega failid või kaustad. Tee seda oma arvutis: `pull`, muudatus, commit inglise keeles käskivas kõneviisis, `push`.
- Kustuta GitHubis kodutöö harud, mis on juba peaharuga liidetud.
- Vaata järele kosemudel, agiilne arendus, Scrum ja Kanban ning loe agiilse tarkvaraarenduse manifest.
- Tiimitöö: lõpeta README ja kirjuta igaüks oma kolm probleemikandidaati oma piletist tehtud harus. Seejärel kaaslase ülevaatus, liitmine peaharuga ja tiimi release koos kirjeldusega, mida tehti ja mis jäi segaseks. Keegi peab vastutama projektijuhtimise eest ja keegi release'i eest.
- Kliendilt (õppejõult) võib küsida, mida „kaasaegne“ tähendab.
- Kodutöö sammud on failis homework.md, taust kodutöö ja release'i peatükis. Õppejõud lubas lisada release'i juhendi.
- Plusspunktide jaoks tee kursuse materjalidesse kirjalikke parandusettepanekuid.

## Plaan ja tegelikkus

**Mis jõuti:** slaidide põhisisu (kliendisoov kui ebamäärane bríif, probleem keskmes, rollid), tiimide moodustamine, repode ja Kanbani tahvlite loomine ning probleemikandidaatide ülesande käivitamine koos töövooga issue'st haruni.

**Mis võttis plaanitust kauem:** esimene pool (umbes tund) kulus kodutöö tagasisidele ja Giti kordamisele: nimetamine, commit'id, kloonimine, harud. See oli vajalik, sest Giti ebakindlus oli selgelt tunda. Tiimi seadistamisel tekkisid takistused (vananenud lingid, repo nimed, organisatsiooni ligipääs), mis võtsid rühmatöö ajast suure osa.

**Mis jäi põgusaks või lükkus edasi:** release'i loomine (juhend lubati hiljem), epic'ud ja alampiletid, konfliktide lahendamine. Probleemikandidaatide ühisosa valimine jäi kodutööks. Tarkvaraarenduse meetoditest räägiti ainult kordamise ja arutelu korras.

**Üliõpilaste küsimused ja arusaamatused:** Giti ja GitHubi vahe; miks mitte muuta faile veebiliideses; mis on harude mõte; ülevaataja ligipääs; terminali asukoht vs failipuu; üleliigsed kaustad pärast kloonimist; mitu pull request'i ühe töö kohta; termin „waterfall“ vs „kosemudel“.

**Õppetunnid järgmiseks korraks:**
- Arvesta Giti kordamiseks eraldi aega ja tee see ühe demona läbi (`pwd`, `clone .`, `pull`, haru, commit, push).
- Kontrolli enne seminari organisatsiooni linke, ligipääse ja näidisrepot.
- Kanbani tahvli lisamise riba ja issue'st haru loomine vajavad samm-sammulist näitamist.
- Ühine ülesande kaust loo kohe peaharus, enne kui liikmed harusid teevad.
- Release'i juhend peaks olemas olema juba seminari ajal.
- Paranda materjalides termin „waterfall“ → „kosemudel“.
