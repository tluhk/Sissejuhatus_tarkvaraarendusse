<!-- loengud:konspekt osad=1,2 (automaatne; kui muudad käsitsi, kustuta see rida – siis tööriist seda üle ei kirjuta) -->
# Konspekt: Seminar 3: meeskond, tööviis ja süsteemi põhimõte

> Automaatne kokkuvõte seminari salvestusest (kõnetuvastus + keelemudel). Võib sisaldada ebatäpsusi – täpse sõnastuse leiad transkriptsioonist.

Seminari teema oli see, kuidas meeskond töötab ja millist süsteemi ta põhimõtteliselt kavandab. Esimene pool kulus suures osas kodutöö tagasisidele, kasutajalugude tutvustamisele ning pikemale arutelule selle üle, kuidas AI tarkvaraarendust muudab ja mis jääb inimesele. Arutelu käis üliõpilaste küsimuste järgi. Teises pooles vaadati üle tööviisid, loeti GOV.UK alpha-etapi juhendit, arutati tiimides riskantseid oletusi ja jagati uued rollid. Tööviisi valik, kasutajalood ja kontseptsioon said tunnis alguse. Backlog'i koostamisest ja ajahinnangutest tunnis eraldi ei räägitud ning merge-konflikti harjutus jäi kodutööks.

## Kodutöö tagasiside: release'i tegemine GitHubis [▶ 1. osa 0:02](https://youtu.be/Q9L00yUmicM?t=2)

Kodutööd olid üldiselt hästi tehtud: commit'e tehti, kaaslased vaatasid pull request'id (PR-id) üle ja töövoog toimis. Õppejõud rõhutas, et kui tekib takistus, küsige kõigepealt tiimikaaslastelt. Mõte on töötada tiimina, mitte nokitseda üksi oma nurgas.

Kõige sagedasem viga oli **release'i** tegemises. Osa tiime oli loonud release'i jaoks käsitsi kausta. See ei ole GitHubi mõttes release. Release tuleb teha repo „Releases“ jaotisest nupuga „Draft a new release“, sest siis tekib ka **tag** (versioonisilt). Kui release on tehtud käsitsi, ei saa masinad sellest aru: otsingud seda ei leia ja release'i juurde ei teki allalaaditavaid **artefakte** (assets), näiteks rakenduse kindlat versiooni.

Selles kursuses on toode „jutuline“ ja artefaktid pole nii olulised. Hiljem, näiteks teise kursuse mänguprojektis, saab release'i alt mängu enda kätte. Siis tuleb hästi esile ka versioonide mõte: igal versioonil (1, 2, 3 jne) on oma nimi ja oma allalaaditav sisu.

### Miks tähtajad on olulised [▶ 1. osa 7:56](https://youtu.be/Q9L00yUmicM?t=476)

Mõned tööd jõudsid kohale hiljem. Õppejõud ütles, et suurt karistust hilinemise eest ei tule, aga ühel hetkel hakkab hilinemine ise karistama. Kui sinu töö peab üle vaatama keegi teine, paned hilinedes tema raskesse olukorda, sest ka tema peab oma töö hiljem tegema. Päris töös võib kokkulepitust hilisem esitamine mõjutada ka tasu.

## IT ei pruugi olla parim lahendus [▶ 1. osa 9:16](https://youtu.be/Q9L00yUmicM?t=556)

Selle seminari kodutöö keskmes on **süsteemi kontseptsioon**: kuidas teie rakendus töötab, mida see teeb ja kuidas see probleemi lahendab. Õppejõud tegi enne seda olulise reservatsiooni. Kuigi te õpite rakendusinformaatikat ja teie tööriist on tõenäoliselt IT, ei tähenda see, et IT lahendab leitud probleemi kõige paremini.

Ta kasutas analoogiat: kui sul on haamer, ei pea kõike sisse taguma. Kui tunniplaani probleemi lahendab paremini vineertahvel või kriiditahvel, tasub sellest alustada. Te olete kliendi murede lahendajad. Kui säästate kliendi raha, saab ta selle anda teile mõne kasulikuma ülesande eest. Õppejõud lisas, et ideaalmaailmas võiks nii olla, päriselus alati ei ole.

## Tööviisid: Waterfall, iteratsioonid ja MVP [▶ 1. osa 11:55](https://youtu.be/Q9L00yUmicM?t=715)

Varasemates seminarides räägitud tööviise (Waterfall, agiilsed raamistikud nagu Scrum ja Kanban) ei ole mõtet võtta jäigalt ega töötada rangelt ühe raamistiku sees. Eesmärk on probleem lahendada. Teadke erinevaid töömeetodeid ja pange nendest kokku tööviis, mis teie olukorrale kõige paremini sobib.

**Waterfall ehk kosemudel**: alguses lepitakse kokku, mida tehakse, töö tehakse etappide kaupa ja klient saab valmis toote. Vahepeal sekkumist ei ole: „võta või jäta“. Oht on selles, et kui arendus kestab näiteks aasta ja maailm muutub, saab klient aasta tagasi kokku lepitud ja vahepeal vananenud süsteemi.

Teine võimalus on arendada iteratsioonide kaupa, alustades **MVP**-st (minimum viable product, minimaalne elujõuline toode). Õppejõud soovitas selliseid lühendeid aeg-ajalt korrata, et uues töökohas või seltskonnas teaksite, millest jutt käib.

Tunniplaani näide: esimeses etapis töötavad kõik funktsioonid. Saab sisestada tunniplaani andmed ja süsteem näitab neid kasutajale. Kasutajaliides võib olla kole ja asju ei pruugi kohe üles leida, aga toode toimib. Kas see on hästi lahendatud, on järgmiste iteratsioonide teema.

Kui hiljem küsiti, miks MVP-d vaja on, tõi õppejõud kaks põhjust. Kliendile saab võimalikult vara midagi anda ja meeskond näeb, et asi toimib ja sellega võib edasi minna.

## Kasutajalugu ja kontrolltingimus [▶ 1. osa 16:14](https://youtu.be/Q9L00yUmicM?t=974)

**Kasutajalugu** kirjeldab ühte toote funktsionaalsust inimkeeles. **Kontrolltingimus** aitab hiljem kontrollida, kas toode teeb seda, mida vaja. Levinuim kirjapanekuviis on:

> Kasutajana soovin [tegevust või võimalust], et [saavutatav väärtus].

Lihtsamalt öeldes: kellena soovin ma mida teha ja miks. Ühetaoline vorm on oluline, sest nii on igast loost selge, kes mida teeb. Õppejõu sõnul muudab AI selle lihtsamaks, sest kõike ei pea enam nii rangelt sõnastama.

### Näide: tunniplaani viimane uuendus [▶ 1. osa 18:00](https://youtu.be/Q9L00yUmicM?t=1080)

Õppejõud harutas lahti seminari materjalide näite: „Tudengina soovin näha, millal mu rühma tunniplaani viimati uuendati, et teaksin, kas saan selle põhjal oma päeva planeerida.“ Selles lauses on palju infot:

- kuskil peab olema tunniplaan ja sellel on UX-pool: kuidas see välja näeb, mis fondi ja mis keelt kasutatakse;
- uuendamise aeg peab olema kuskil talletatud ja nähtav;
- „minu rühm“ tähendab, et on vaja rühmade valikut ja andmebaasi, kus on rühmad ja õppeaastad;
- „tudeng“ tõstatab küsimuse, kas lahendus on kogu kolledžile või kitsamale rühmale.

Nii jaguneb suur probleem väiksemateks osadeks. Kasutajaloost saab teha töö**pileteid**: suured piletid ehk **epic'ud** katavad suurema funktsionaalsuse ja jagunevad alampiletiteks, millest igaüks on üks kindel töö.

Kontrolltingimus on lühike: „iga rühma plaani juures on näha viimase uuenduse kuupäev ja kellaaeg“. Selle täitmiseks võib vaja minna mitut piletit. Kuupäeva info peab kuidagi tekkima, keegi peab välja mõtlema arusaadava väljanägemise ja keegi peab selle kuvama.

### Halb näide [▶ 1. osa 22:35](https://youtu.be/Q9L00yUmicM?t=1355)

„Tudengina soovin mobiilirakendust, et tunniplaan oleks moodsam“ on halb kasutajalugu. Selles pole vajadust, sõna „moodsam“ ei ütle midagi ja lugu eeldab lahenduse ette. Sellele ei saa ka kontrolltingimust kirjutada. Seda, kas kuupäev ja kellaaeg on näha, saab kontrollida. Seda, kas tunniplaan on „moodne“, ei saa. Selle üle saab ainult vaielda.

Kasutajalood peavad lähtuma eelmise seminari tõenditest ja kirjeldama vajadust.

### Kursuse fookus [▶ 1. osa 23:40](https://youtu.be/Q9L00yUmicM?t=1420)

Õppejõud selgitas, et selles kursuses käsitletakse neid teemasid põgusalt. Peamiselt harjutatakse Giti ja GitHubi kasutamist, grupitööd ja suhtlust GitHubi kaudu. Kasutajalood ja projektitöö tulevad põhjalikumalt teistel kursustel ja praktikas, kus tehakse päris asju. Kui praegu jääb midagi segaseks, pole see probleem.

## Kodutöö maht ja ülesehitus [▶ 1. osa 24:48](https://youtu.be/Q9L00yUmicM?t=1488)

Kursuse mahu järgi on kodutööle ette nähtud umbes kaheksa kuni kümme tundi. Õppejõud aimab, et kõike täpselt nii tehes jääks aega pigem puudu. Ta ei anna kodutöö jaoks tunniarvu, sest siis tehtaksegi täpselt nii palju.

Kodutöö koosneb grupitööst (tööviisi valiku kirjeldus, süsteemi kirjeldus) ja individuaalsest osast (kasutajalood). Põhiasi on süsteemi kirjeldus, tööviis tuleb pigem selle järel. Lõpuks tehakse release ja dokumenteeritakse, kuhu jõuti: mis pidurdas, mis aitas, mida õpiti.

## Hiline tagasiside ja muutuvad otsused [▶ 1. osa 27:06](https://youtu.be/Q9L00yUmicM?t=1626)

Kursusel on kaks poolt: koolitöö oma tähtaegadega ja „päris asi“, mida luuakse. Kui eelmise seminari kõige väärtuslikum tagasiside tuli alles pärast tähtaega (ka siis, kui see tuli võõralt inimeselt, mitte grupikaaslaselt), tuleb seda kasutada. Praeguses etapis saab veel kõike muuta ja parandada.

Siin tuleb esile Waterfalli ja iteratiivse arenduse erinevus. Kui kosemudeli puhul tuleks väärtuslik tagasiside siis, kui toode on pooleldi valmis, oleks see halb, sest tagasi pöörata pole raha. Iteratiivse arenduse puhul saab uue info igal hetkel kasutusele võtta.

AI muudab ka seda. Kodeerimine oli varem arenduse üks kallimaid osi. Nüüd on see odav, sest AI teeb tagasiulatuvaid parandusi kiiresti.

### Persona [▶ 1. osa 32:46](https://youtu.be/Q9L00yUmicM?t=1966)

Küsimusele, kas hilisemat sisendit peab kasutama, vastates selgitas õppejõud mõistet **persona**. See on kliendiküsitluste põhjal loodud väljamõeldud sihtrühma esindaja profiil, tavaliselt pildi, nime, vanuse, moto ja lühikirjeldusega. Ühe toote kohta tehakse tavaliselt üks-kaks personat. Persona annab tiimile ettekujutuse, kellele toodet tehakse. Iga funktsionaalsuse puhul saab küsida, kas see inimene seda päriselt kasutaks. Toodet kõigile korraga on raske teha.

Kui hiljem saabunud info näitab, et persona või probleem oli valesti kirjeldatud, tuleb see arvesse võtta, ja mida varem, seda parem. Kõige kallim on olulise info eiramine. Kui hiline info on ebaoluline, võib selle kõrvale jätta. Muudatuse põhjus tuleb dokumenteerida („saabus info, selle tõttu muutsime …“), et ka klient saaks aru, miks algne plaan muutus.

## Dokumentatsioon AI ajastul [▶ 1. osa 37:10](https://youtu.be/Q9L00yUmicM?t=2230)

Selle kursuse „rakendus“ on praktiliselt ainult dokumentatsioon, nii et see on kursuse kõige olulisem osa. Õppejõud selgitas, kuidas dokumentatsiooni roll muutub:

- Varem kirjutati detailne dokumentatsioon inimesele: tuhanded piletid ja epic'ud, mis jagati nii väikesteks ja täpseteks alamülesanneteks, et arendaja sai need punktuaalselt ära teha.
- Kui lahenduse teeb AI, pole sellist üleandmist vaja, sest AI täidab ülesande ise ja saab olla korraga mitmes rollis. Osa dokumentatsioonist võib kokku pakkida või ära jätta.
- Dokumentatsioon võib olla ülesehitatud AI jaoks (ülesanded, piirangud, raamid) ja inimesele isegi raskesti arusaadav. Inimene peab aga saama oma agendilt küsida, mida tehakse, ja saama adekvaatse vastuse.
- Tulemus peab olema sama mis vanasti: töötav, kontrollitav ja inimesele sedavõrd arusaadav, et rikke korral saaks parandamist alustada.

Varem oli tarkvaraarendus jäikade raamistikega reguleeritud. Nüüd võib projekt olla „ühe jalaga Waterfall“, millel on sees iteratsioonid. Nimetust sellele veel pole.

## Kuidas AI arendust muudab [▶ 1. osa 42:08](https://youtu.be/Q9L00yUmicM?t=2528)

Õppejõud võttis aluseks seminari materjalides viidatud artikli AI-põhisest tarkvaraarenduse elutsüklist. Põhiväide: etapid jäävad samaks. Need on planeerimine (aja ja ressursside eraldamine), disain (probleemi mõistmine ning lahenduse kavandamine nii sisult kui väljanägemiselt), ehitamine, testimine, kasutuselevõtt ja hooldus.

**Testimise** kohta lisas ta, et toode tuleb enne avalikkuse ette viimist läbi testida. Kui saadad rakenduse otse kasutusse ja inimesed hakkavad kurtma, et see ei tööta, on ka see testimine, aga kallis: see kahjustab mainet ja kasutajad lähevad minema ega tule tagasi.

AI muudab järgmist:

- **Etapid käivad läbisegi.** Varem järgnes üks etapp teisele, nüüd võib korraga ehitada ja testida. Osa asju on katki, osa juba töötab ja agent arendab samal ajal uut funktsionaalsust.
- **Kiirus.** Mis varem võttis kuid või aastaid, võtab nüüd tunde või minuteid. Lihtsa veebilehe kirjutab AI valmis sekunditega.
- **Uued kombinatsioonid.** Iteratiivne arendus võib koosneda AI tehtud väikestest kosemudeli etappidest: tee valmis, testi, kui ei sobi, tee järgmine.
- **Disain promptimisega.** Varem tehti disain kujundustarkvaras ja testiti enne arendust. Nüüd saab disaini kohe valmis rakenduse peal promptida. Kood on tõeallikas ja AI testib ka osaliselt ise.

### Mis jääb inimesele? [▶ 1. osa 49:01](https://youtu.be/Q9L00yUmicM?t=2941)

Õppejõud palus üliõpilastel arutleda, mis tööd jääb lähiajal inimesele. Ta tunnistas, et oli arvanud nooremaid AI suurkasutajateks, aga sageli selgub, et ta kasutab seda ise rohkem.

Arutelus jõuti mitme mõtteni:

- **Kliendiga suhtlemine.** Klient võib ise teha rakenduse näiteks Lovable'iga, aga siis tulevad küsimused: kas sobib platvormi domeen, kust saada oma domeen, mis on kulud, kas saab odavamalt, kuidas on lood turvalisusega. Autoosade müüja tahab müüa autoosi, mitte sellega tegeleda. Nii tekib ikkagi vajadus inimese järele, keda saab usaldada.
- **Vastutus ja ülevaatamine.** Kui klient tellis sinult midagi, vastutad sina ja pead tulemuse üle vaatama. AI toodab palju ja kõik näib töötavat, nii et kiusatus üle mitte vaadata on suur. Enda projekti puhul võib see sobida („kuni häkkerid selle maha võtavad“), aga päris kliendi puhul oled kohustatud tulemuse inimesena üle vaatama. Selleks tuleb AI-le anda juhised, et ta selgitaks tehtut arusaadavalt ja mitte liiga pikalt.
- **Orkestreerija roll.** Inimene ütleb, mida tehakse, millal seda on vaja ja mis tingimustele see peab vastama.
- **Testimine päris inimestega**, kui toodet tehakse päris inimestele.

### AI hind ja tulevik [▶ 1. osa 28:28](https://youtu.be/Q9L00yUmicM?t=1708)

Õppejõud märkis, et praegu on AI väga odav. 100–250 eurot kuus võib katta mitut rolli (UI- ja UX-disainer, arhitekt, analüütik, arendaja), mille palgakulu oleks kümneid tuhandeid. See võib muutuda. AI võib minna kalliks, ressurss võib koonduda väheste kätte („tehnofeudalism“) või tulla riiklikud piirangud. Siis on inimesi jälle rohkem vaja. Õppejõud pidas teemat nii keeruliseks, et seda tasub edasi arutada tunnist väljaspool.

## Mida kodutöö probleemi kohta õpetas [▶ 1. osa 59:15](https://youtu.be/Q9L00yUmicM?t=3555)

Õppejõud küsis, kas kodutöö muutis arusaama digitoote loomisest. Tüüpiline viga on see, et probleemi ei uurita, vaid hakatakse kohe lahendama, sest „me ju teame, mis viga on“. Tegelikult tuleb probleemi uurida: kuidas, kelle käest tagasisidet saada ja mis probleem tegelikult on.

Ta tuletas meelde kliendi briifi: klient tahab „moodsat“ tunniplaani. Kliendi ebamäärane soov ei ole kliendi probleem. Teie ülesanne on välja uurida, mida „moodne“ tähendab ja mis praeguses lahenduses valesti on. Alles siis saab tööd osadeks jagada ja läbida planeerimise, disaini, ehitamise, testimise, juurutamise ja hoolduse. Kokkuvõtteks: alati, kui antakse selline ülesanne, tormatakse lahendama, aga kõigepealt on vaja leida, mida lahendada.

## Rollid kursuse projektis [▶ 1. osa 1:04:56](https://youtu.be/Q9L00yUmicM?t=3896)

Üliõpilased küsisid, kui tõsiselt rolle võtta ja kas rolli valik mõjutab midagi. Õppejõu vastus: väga tõsiselt mitte. Päris rakendust, kus kõik rollid oleks sisuliselt olemas, praegu ei tehta. Mõte on võtta roll, püüda selle ülesandeid töö käigus täita ja saada aru, millised rollid on olemas ja miks. Mõni roll on sõltuvalt ülesandest sisukam, mõni vähem. Projektijuht ja release manager saavad olla korraga ainult ühel inimesel.

Eelmise seminari eesmärk oli, et igaüks saaks PR-i teha ja üle vaadata. Kui ülevaatamise oleks teinud ainult üks inimene, poleks teised seda kogemust saanud. Seda harjutatakse veel mitu korda.

## „Kuidas me peame tegema?“ on vale küsimus [▶ 1. osa 1:12:31](https://youtu.be/Q9L00yUmicM?t=4351)

Küsiti, kas otsusefaile on üldse vaja. Õppejõud vastas, et otsuse tegemiseks on vaja lähteandmeid ja see paneb töö järjekorra paika. Kas lähteandmed tulevad kogemusest, küsitlusest või mujalt, sõltub olukorrast.

Laiemalt soovitas ta unustada küsimuse „kuidas me peame tegema?“ ja mõelda, mida on vaja teha, et tulemuseni jõuda. Õiget või valet lahendust selles mõttes pole. Õige on see, mis viib samm-sammult probleemi lahenduseni (seaduse piires). Kui hindamise tagasiside jääb segaseks või õppejõud näib endale vastu rääkivat, kirjutage kommentaar tagasiside juurde ja ta vaatab töö uuesti üle.

Kliendiuuringute kohta: lahendust ei tohi ehitada üksnes oma eelarvamuste ja ettekujutuse peale. Juba tiimisisene arutelu ja küsimine laiemalt ringilt näitavad sageli, et teised arvavad teisiti.

## Hindamine ja eksam [▶ 1. osa 1:18:14](https://youtu.be/Q9L00yUmicM?t=4694)

Hinne koosneb mitmest osast:

- **kohalkäimine** ja kaasamõtlemine seminaris;
- **aktiivsus GitHubis**: commit'id, PR-id ja ülevaatamised. Üks commit peaks olema üks loogiline tegevus. Miljon commit'i ei ole eesmärk;
- **parandused õppematerjalidesse**: kui leiate kirjavea, loogikavea või jaburuse, tehke PR-iga parandusettepanek. Sellest jääb jälg maha;
- **eksam**: dokumenteeritud protsessi esitlus ja tõenäoliselt ka test meetodite ja elutsükli kohta.

Eksam ei peaks olema selline, mille jaoks saab õhtu enne kaks tundi tuupida. See peaks näitama, et pool aastat aktiivset tööd on asjad kätte jätnud. Kui mõiste nimi ei tule meelde, aga oskate selgitada, mida see tähendab, on see piisav. Kursuse lõpuks peaksite oskama teha PR-i, töötada ühises repos ja selgitada, mis on MVP.

Üliõpilased küsisid täpsemat struktuuri, näiteks millised leheküljed läbi lugeda. Õppejõud ütles, et ei anna seda meelega. Tema filosoofia on, et peate ise välja mõtlema, kuidas asjad toimivad. Selle põhjenduseks tõi ta tööturu olukorra (vt allpool). Tal on hea meel, kui üliõpilased küsivad ja sekkuvad, kui eesmärk jääb segaseks.

## Kursuse teekond ja rollide ülevaade [▶ 1. osa 1:25:28](https://youtu.be/Q9L00yUmicM?t=5128)

Kursuse teekond on probleem, kasutajate vajaduste uurimine, nõuete kirjeldamine ja töö planeerimine (täna), seejärel lahenduse disain. Päriselus disainitaks ka tegelik lahendus. Siin piirdutakse kirjeldamisega, nii et praktiline disaineri roll jääb ära. Sama kehtib arendamise kohta. Varasematel aastatel mängiti arendust läbi pseudokoodiga, nüüd mitte. Testimist saab teha nii, et tiim tutvustab oma lahendust teisele grupile ja saab sealt tagasisidet.

Rollid üle käies tõi õppejõud esile järgmist:

- **Tootejuht (product owner)** ei ole klient, vaid teostaja tiimi liige, kes võtab kliendi mure enda peale. Kui tiim „läheb lendu“, ütleb tema: stopp, klient tahab seda, mitte seda, mida te pakute.
- **Projektijuht** vastutab, et asjad saaksid õigel ajal tehtud. See roll kipub ununema. Projektijuht peab võtma vastutuse ja vajadusel tiimi kokku võtma, olenemata sellest, kes tiimis on. Ilma projektijuhita asjad ei toimi.
- **Ärianalüütik** uurib, kuidas äri toimib ja mida selleks vaja on.
- **UX-disainer ja kasutajauurija**: asjad võivad olla ilusad, aga kui kõige tähtsam nupp on peidus, lahendus ei tööta.
- **Tarkvaraarhitekt** valib raamistikud, keeled ja komponendid, mis tagavad vajaliku, ning paneb kokku klotsid, millest süsteem koosneb. Selle põhjal valitakse arendaja.
- **Tarkvaraarendaja**: õppejõu hinnangul jäävad praegu tööst ilma eelkõige need, kes oskavad ainult üht asja ja ei näe suuremat pilti. Kes näeb suuremat pilti, suudab endale ka töö luua.
- **Testija** kontrollib, et tarkvara töötab kõikides olukordades. Suur osa testidest on automaattestid, osa tehakse inimestega.
- **DevOps ja turbespetsialist** vastutavad kasutuselevõtu, hoolduse ja turbe eest.

AI-ga muutub see, et igal valdkonnal ei pea olema oma inimest. Disainer võib olla ka arhitekt ja AI abil nii klotsid valida kui programmeerida. Spetsiifilisi teadmisi võib siiski vaja minna. Rakendusinformaatika eelis on see, et saate kõigist neist asjadest aru.

## Õige ja vale on tiimi kokkulepe [▶ 2. osa 0:03](https://youtu.be/4NkG0hIlTbU?t=3)

Tarkvaraarendus on seni olnud liinitöö. Mis on õige ja mis vale, on suuresti tiimi kokkulepe. Rollid ja arendusmeetodid on olemas selleks, et ei peaks iga kord nullist alustama, aga õppejõud ei anna ette ainuõiget teed.

Dokumentatsioon ei ole õppejõu jaoks, vaid tiimi enda jaoks. Hea dokumentatsiooni lihtne test: kui kuuendas seminaris on vaja leida, miks mingi otsus tehti, leiate selle kiiresti üles. Kui ei leia, on dokumentatsioon halb.

## Tööviisid lühidalt üle [▶ 2. osa 3:24](https://youtu.be/4NkG0hIlTbU?t=204)

- **Kosemudel** on teatud olukordades hea, teatud olukordades kehvem. Ükski tööviis pole vananenud, kõik sõltub tiimist ja kliendiga kokkuleppest. Kui kliendil pole IT-projektide kogemust, ei pea temaga rääkima Waterfallist või agiilsusest. Selgitage lihtsalt, kuidas töö käib.
- **Iteratiivne arendus**: korduvate tsüklitega uuritakse, testitakse, tehakse uus plaan, pannakse parandused piletitesse ja toode muutub järjest paremaks.
- **Scrum** eeldab Scrum masterit, tavaliselt sertifikaadiga inimest, kes teab, kuidas protsessi läbi viia.
- **Kanban** on õppejõu sõnul hästi levinud ja mõnus süsteem ning seda tiimid oma GitHub Projectsi tahvlil juba kasutavad. Sealt on visuaalselt näha, mis on töös ja mis veel teha. Kui kellelgi läheb tööd liiga palju, saab pileteid ümber tõsta. Kanbanit saab kombineerida teiste tööviisidega. Kursusel kasutatakse seda edasi.

## Grupitöö: GOV.UK alpha ja riskantsed oletused [▶ 2. osa 8:42](https://youtu.be/4NkG0hIlTbU?t=522)

Tiimid lugesid GOV.UK teenusekäsiraamatu alpha-etapi juhendit (vajadusel tõlkija või AI kokkuvõtte abil, peaasi et põhipunktid saaksid selgeks). Seejärel arutati tiimis selle eeskujul läbi tahvlil olevad küsimused.

Keskne mõiste oli **riskantne oletus**: kõik see, mida tiim on lahenduse kohta oletanud ilma kontrollimata. Harjutuse mõte oli korraks „maha istuda“ enne töö jätkamist. Vaadake oma probleemi kirjeldus ja otsused üle ja küsige:

- kas siin on riskantseid oletusi;
- kas ja kuidas neid peaks kontrollima;
- kas oleme midagi valesti eeldanud.

Kui riske ei leita, võib selle dokumenteerida: esialgu ei paista riske olevat. Leiud või kinnituse võib lisada probleemi kirjeldava otsusefaili lõppu.

Arutelust tuli välja ka idee, et tunniplaani lahendus ei pea olema veebileht. Näiteks võiks tunniplaan olla nähtav Discordis, mida üliõpilased niikuinii kasutavad. Õppejõud pidas seda väga heaks näiteks: tema enda kogemuses on tunniplaani aadress iga kord meelest läinud.

## Uued rollid selleks etapiks [▶ 2. osa 36:37](https://youtu.be/4NkG0hIlTbU?t=2197)

Kõigepealt pidid tiimid kirja panema, kas arusaam kasutaja probleemist kodutöö käigus muutus. Seejärel jagati rollid. Eelmise korra projektijuht ei tohi uuesti projektijuht olla. Igaüks võtab uue vaatenurga.

Selles etapis on vaja:

- **projektijuhti**, kes vastutab, et kodutöö saaks tehtud. Tõenäoliselt täidab tema ka Kanbani tahvli ja tal on niigi palju tegemist;
- **release managerit** tehnilistel põhjustel: keegi peab release'i tegema;
- **disainerit**, kes mõtleb läbi, kuidas kasutaja lahenduses liigub, ja kirjeldab stsenaariumid. Teised aitavad, aga tema vastutab;
- **arhitekti**, kes uurib, millistest osadest lahendus koosneb, kuidas selliseid asju lahendatakse ja kus lahendus võiks elada (veebileht või hoopis Discord). Kuna tema roll on selles etapis väiksem, võib ta seda uurida „huvi pärast“, ka AI abil.

Arendajat selles etapis vaja pole. Viieliikmelises tiimis võib lisada **tooteomaniku**, kes vaatab tööd tellija ehk õppejõu silmadega: kas seda kõike on vaja, kas tiim ehitab liiga suurt lahendust. Selleks tuleb õppejõult aeg-ajalt küsida. Leiud tasub dokumenteerida ja jagada.

Arhitekti kohta tegi õppejõud huvitava tähelepaneku: suurema IT-kogemusega inimene võib selles rollis olla isegi kehvemas seisus. Ta kipub pakkuma lahendusi, mida ta tunneb, mitte neid, mida on vaja. Vähem kogenud inimene vaatab probleemi avatumalt.

## Tööviisi otsus ja failid [▶ 2. osa 40:14](https://youtu.be/4NkG0hIlTbU?t=2414)

Tööviisi valikul mõelge, kuidas lahendus valmis teha, kuigi tegelikult seda ei ehitata, ja pange see kirja. Failinimesid ei pea orjalikult järgima. Kui eelmisel korral tehti juba sarnane fail, võib selle järjestust kohandada. Oluline on, et dokumentatsioon oleks loogilises järjekorras ja faili pealkiri kajastaks selle sisu.

## Kasutaja teekonnast kasutajalugudeni [▶ 2. osa 41:30](https://youtu.be/4NkG0hIlTbU?t=2490)

Õppejõud tunnistas, et lugude ja kontseptsiooni omavaheline seos on keerulisem osa, ja soovitas järgmist järjekorda:

1. Mõelge läbi süsteemi üldine kontseptsioon: kuidas süsteem töötab ja kellele see on mõeldud.
2. Kirjeldage tekstina **kasutaja teekond** ülesande põhjal. Näide: kasutaja peab neljapäeval sõitma Haapsallu tundi ja tahab teada, millal tund algab. Ta tuleb keskkonda (kui sisselogimist pole, seda kirja ei panda), valib oma vaate, filtreerib oma rühma ja päeva ning ongi korras. Väljanägemise peale ei pea veel mõtlema.
3. Leidke teekonnalt kohad, kus kasutaja takerdub, ja kirjutage kasutajalugu igale sammule, kus probleem esineb.

Kasutajalood kirjutavad probleemi lahenduse põhimõtteliselt lahti. Tunnis mängivad disainer ja arhitekt oma osa läbi ning see kattub, sest disaini tehakse koos. Ülejäänu jääb kodutööks. Pärast seminari täiendas õppejõud kodutöö juhendit, et kasutajateekonna ja lugude seos oleks selgem [▶ 2. osa 1:01:28](https://youtu.be/4NkG0hIlTbU?t=3688).

## Commit'i sõnum: pealkiri ja kirjeldus [▶ 2. osa 1:07:53](https://youtu.be/4NkG0hIlTbU?t=4073)

Grupitöö ajal küsiti, kas commit'il peab olema pikk kirjeldus. Vastus: tavaliselt piisab pealkirjast. Kirjeldus on lisa, mida kasutatakse siis, kui muudatus vajab pikemat selgitust.

## Kokkuvõte: ära kao detailidesse [▶ 2. osa 1:16:10](https://youtu.be/4NkG0hIlTbU?t=4570)

Lõpus kordas õppejõud põhimõtet. Seekord on vaja loodava rakenduse **kontseptsiooni** ehk kirjeldust selle olemusest: mis rakendus see on, mis küsimustele see vastab ja mis probleemid see lahendab. Seda täiendavad mõned kasutajalood, mis tulevad välja kohtadest, kus probleem ilmneb, ning rollide läbimängimine.

Juhendi punkte ei tasu täita punktuaalselt kui eesmärki omaette. Need peavad aitama põhiasja lahendada. Õppejõu sõnul hakkavad üliõpilased juhendeid sageli liiga täpselt täitma, aga see pole iseenesest eesmärk. Probleemi kirjeldust võib kogu aeg täiendada, see ei ole kivisse raiutud. Kui avastate midagi uut, on see hea.

## Lisaks plaanile

- **AI kui projektijuht.** Õppejõud katsetab oma töös varianti, kus AI on projektijuht. Iga tiimiliige salvestab õhtul oma tehtud töö AI-le loetavale kujule ja AI saadab igal hommikul Slacki kaudu tööülesanded.
- **Personaalagendid ja disain AI jaoks.** Suure osa infost saame juba praegu AI-lt küsides, ilma veebilehtedele minemata. Lähitulevik võib kuuluda personaalagentidele, mis toovad vastused, filtreerivad e-kirju ja eristavad AI toodetud „sodi“ päris kirjadest. Sellest tuleneb, et veebilehti ja rakendusi tuleks juba praegu teha ka AI jaoks: info AI-le sobival kujul, näiteks MCP-serveri kaudu, ning tekstid, mis algavad kokkuvõttega (nt KKK, artiklid).
- **Väikeettevõtja võimalused.** Õppejõu hinnangul ei võeta nooremarendajaid praegu kergesti suurtesse firmadesse tööle ja töötajaid koondatakse. Samas on AI andnud väikestele tegijatele palju võimalusi. Kolmeliikmeline tiim saab praegu odavalt ja lihtsalt osaleda konkurssidel ja pakkumistel, mis paar aastat tagasi oleks olnud väga raske. Parim tee võib olla ise või kambaga ettevõte luua.
- **IT kui haamer.** Lahendus ei pea olema IT-lahendus, kui midagi lihtsamat (näiteks kriiditahvel) lahendab probleemi paremini.
- **Lahendus väljaspool veebi.** Arutelust tulnud mõte panna tunniplaan Discordi näitab, et lahendus võib elada seal, kus kasutajad juba on.

## Kodutöö ja järgmised sammud

- **Kodutöö 3**: süsteemi kontseptsioon ja kõrgtaseme arhitektuur, kasutaja teekond, kasutajalood koos kontrolltingimustega (individuaalselt), tööviisi valik ja release `v0.2.0`. Põhirõhk on süsteemi kirjeldusel.
- **Merge-konflikt** tuleb kodus läbi mängida: kaks inimest muudavad sama faili, tekib konflikt ja see lahendatakse. Juhendid on materjalides. Kogemusi võib tiimis jagada.
- Rollid jagati uuesti, eelmine projektijuht ei jätka selles rollis. Rollid ja vastutajad pannakse README-sse.
- Riskantsete oletuste arutelu tulemus (või kinnitus, et riske ei leitud) dokumenteeritakse.
- Kui kodutöö probleemi kohta muutis arusaama, pannakse see kirja.
- Õppejõud täiendas seminari materjali ja kodutöö juhendit ning lükkas need GitHubi. Küsimused Discordis.

## Plaan ja tegelikkus

**Mis jõuti:**
- Rollid käidi läbi ja jagati selleks etapiks ümber (projektijuht, release manager, disainer, arhitekt, suuremas tiimis tooteomanik).
- Tööviisid (kosemudel, iteratiivne, Scrum, Kanban, MVP) vaadati üle ja seoti AI-ajastu muutustega.
- Kasutajalugu ja kontrolltingimust selgitati põhjalikult plaani näite (tunniplaani viimane uuendus) ja halva näite abil.
- GOV.UK alpha lugemine ja riskantsete oletuste arutelu tiimides toimus.
- Kasutaja teekonna ja lugude seost selgitati suuliselt ja kodutöö juhendis.
- „Kuidas AI arendust muudab“ sai plaanitust tunduvalt rohkem aega.

**Mis jäi tegemata või lükkus edasi:**
- Merge-konflikti tekitamine ja lahendamine tunnis jäi ära ja läks kodutööks.
- Backlog'i koostamisest, Issue'de järjestamisest ja ajahinnangute võrdlusest tunnis eraldi ei räägitud.
- Kolme tööviisi võrdlus projekti järgi ja `002`-otsus jäid suures osas tiimide ja kodutöö kanda.
- Kõrgtaseme arhitektuuri kirjeldamist (piir, osalised, info liikumine) sisuliselt ei käsitletud. See on kodutöö.
- Commit'i sõnumit puudutati vaid küsimuse peale.

**Ajakasutus:** Esimene osa (umbes poolteist tundi) kulus peaaegu täielikult kodutöö tagasisidele, AI-arutelule ja üliõpilaste küsimustele. Plaani praktilised sammud jäid teise poolde, millest suur osa oli grupitöö.

**Üliõpilaste küsimused ja arusaamatused:**
- Mis on ülesannete ja kogu projekti eesmärk ning miks on vaja otsusefaile.
- Kas pärast tähtaega tulnud tagasisidet peab arvestama.
- Kui tõsiselt rolle võtta ja kas rollil on hindele mõju.
- Kuidas hinnatakse ja milline on eksam; sooviti konkreetsemat struktuuri ja lugemismaterjali.
- Release'i tegemine GitHubis oli mitmele segane (käsitsi loodud kaust tag'i asemel).
- Kasutajateekonna, lugude ja kontseptsiooni järjekord tundus keeruline. Õppejõud ise nimetas seda segaseks osaks.

**Õppetunnid järgmiseks korraks:**
- Release'i tegemise („Draft a new release“, tag) juhis tasub anda juba seminaris 2, et viga ei korduks.
- Eesmärgi ja hindamise küsimused tulevad paratamatult. Neile võiks seminari alguses anda lühikese selge vastuse, et AI-arutelu ja praktiline töö ei jääks ajahätta.
- AI-teemaline arutelu on huvitav, aga kipub laiali valguma. Võiks seda ajaliselt piirata.
- Merge-konflikti harjutus vajab tunnis kindlat aega, muidu jääb see koju.
- Backlog ja ajahinnangud vajavad tunnis vähemalt lühikest praktilist osa, sest need on kontrollpunktis.
- Kasutaja teekonnast lugudeni tasub näidata tervikliku näite abil enne grupitööd, mitte alles kodutöö juhendis.
