---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 4 – kvaliteet, riskid ja vastutus
---

# Seminar 4

## Kvaliteet, riskid ja vastutus

<!-- Seminar 3 vastas küsimusele, mida süsteem teeb: kasutajalood, kontrolltingimused ja süsteemi kontseptsioon. Täna küsime, kuidas me teame, et see kavand on piisavalt hea, ja mis võib meid alt vedada. Kvaliteet tähendab täna seda, et ebamäärane nõue muutub mõõdetavaks ja testitavaks. Risk tähendab kontrollimata eeldust, millel on mõju ja vastutaja. Alustame mitte uuest teooriast, vaid tiimide endi tööst. -->

---

## Kogu kursuse teekond: kus oleme?

Probleem → kasutajate ja vajaduste uurimine → nõuete kirjeldamine → töö
planeerimine → lahenduse disainimine → arendamine → **testimine ja tagasiside –
seminar 4** → avaldamine ja hooldus

- seminar 1: suur pilt ja töövahendite seadistamine
- seminar 2: kliendisoovist arendusülesandeni
- seminar 3: rollid, tööviisi valik ja süsteemi kontseptsioon
- **seminar 4: kvaliteet, riskid ja vastutus**
- seminar 5: kasutuselevõtt, tagasiside ja hooldus
- eksam: dokumenteeritud protsessi esitlus release'ide ajajoonena ja mõistete test

**Projekti tulemus:** dokumenteeritud arendusprotsess ja otsuste logi; töötavat rakendust ega klikitavat prototüüpi ei nõuta.

<!-- Teekonnal oleme jõudnud testimise ja tagasiside juurde, aga see ei ole eraldi etapp, mis tuleb alles lõpus. Testimine algab juba nõuetest: kontrolltingimus on sisuliselt test, mis kirjutatakse enne ehitamist. Kursusel me rakendust ei ehita, seega testime kavandit, mitte koodi. Kui kavand annab vastuse, on test läbitud. Kui kavand vastust ei anna, on test läbi kukkunud ja kavandis on auk. Sellest saab Issue. Sama kehtib päris projektides: kõige kallim viga on see, mis avastatakse pärast ehitamist, kõige odavam see, mis avastatakse kavandist. Eksamil on lisaks esitlusele lühike mõistete test; tänased mõisted on viimasel slaidil. -->

---

## Kodutöö 3: mis läks hästi

- kasutajalood räägivad vajadusest, mitte lahendusest
- süsteemi piir on kirjas: ametlik tunniplaan jääb andmeallikaks
- arhitektuur on kirjeldatud osade ja nende vastutuse kaudu
- mõni tiim eristas „täna loenguid pole” ja „andmed jäid laadimata”

Kui AI-d kasutate, laske tal kirjutada lühemalt ja nii, et te ise saate aru, mida ta teile kirjutab.

<!-- Kasutajalood räägivad vajadusest, mitte lahendusest: mitu ülevaatust märkas ise, et „teise värviga” on juba lahendus, mitte vajadus. Just seda oskust seminar 3 õpetas. Süsteemi piir on kõigil kirjas: ametlik tunniplaan jääb andmete allikaks ja tiim ehitab selle peale vaate, mitte uut tunniplaanisüsteemi. Arhitektuur on peaaegu kõigil kirjeldatud osade ja nende vastutuse kaudu, ilma raamistike nimedeta; see ongi kõrgtaseme arhitektuuri mõte. Neljas punkt on tänase päeva jaoks kõige olulisem: kasutajale tähendab „täna loenguid pole” hoopis muud kui „andmed jäid laadimata”. Kui süsteem neid ei erista, arvab õppija, et tund jäi ära. See mõte tuleb täna testjuhtumite juures tagasi. AI kohta: sisuline pool on kohati nii ladus, et on raske öelda, kas tiim saab ise aru, mida kirja pandud on. Sellepärast on tänane teine samm oma otsuste seletamine. -->

---

## Kodutöö 3: mida parandame

1. Valitud tööviisi tuleb ka järgida: kaardid liiguvad töö ajal, mitte viimasel õhtul.
2. Ajakulu kirja töö ajal: hinnang Issue'i loomisel, tegelik aeg sulgemisel.
3. Backlog tuleb tootest, mitte kodutöö sammudest.
4. Ülevaatus on rohkem kui „Korras”. PR-i ühendab ülevaataja, mitte autor.
5. Merge-konflikti kommentaar: fail, kelle muudatused, mis jäi alles.

Viis tiimi kuuest jättis lahtiseks: kas ja kuidas saab tunniplaani andmeid kätte? See on tänase päeva suurim risk.

<!-- Peaaegu kõik puudujäägid olid töö korralduses, mitte sisus. Esiteks Kanban: selle mõte on, et tahvlilt näeb, mis on pooleli ja kus töö seisab. Kui kaardid jõuavad kõik korraga Done'i viimasel õhtul, ei aidanud tahvel midagi otsustada ja tööviis oli ainult kirjas. Teiseks ajakulu: ainult üks tiim võrdles hinnangut ja tegelikku aega Issue'de kaupa. Ilma selleta on iga järgmine plaan sama arvamine. Kolmandaks backlog: paljudel koosnes see kodutöö sammudest nagu „kirjuta refleksioon”, aga backlog peaks näitama, mida toode vajab, näiteks „kontrolli, kas andmeallikas annab valikainete info”. Neljandaks ülevaatus: parimad ülevaatused küsisid midagi konkreetset ja selle peale tehti muudatus; üldine heakskiit ei aita autorit. Viiendaks merge-konflikt: enamikul õnnestus, aga kommentaar peab ütlema, millises failis konflikt tekkis, kelle muudatustega ja mis jäi alles, et teise tiimi lugeja kohe aru saaks. Ja kõige olulisem: viis tiimi kuuest ei kontrollinud, kas ja kuidas tunniplaani andmed päriselt kätte saab. See on kõigi lahenduste suurim kontrollimata eeldus ja täna alustame just sellest. -->

---

## Tänane päev

1. `v0.2.0` ja Projectsi tahvli läbivaatus, rollivahetus
2. „Selgita oma otsust”: iga tiim tutvustab oma otsuseid
3. Ebamäärasest mõõdetavaks
4. Testjuhtum oma kasutajaloost
5. Arendamise etapp: viga, silumine ja koodi ülevaatus
6. Riskid
7. Backlog tootest
8. Git: `log`, `diff`, `restore`
9. Kodutöö 4 ja release `v0.3.0`

**Põhiküsimus:** kuidas me teame, et kavand on piisavalt hea, ja mis võib meid alt vedada?

<!-- Päeval on loogika. Kaks esimest sammu vaatavad tagasi: kas tööviis oli päriselt kasutusel ja kas tiim saab oma otsustest aru. Sammud 3 ja 4 teevad kavandi kontrollitavaks: ebamäärasest kontrolltingimusest saab mõõdetav nõue ja sellest testjuhtum. Samm 5 on lühike pilk arendamise etappi, mida me kursusel ise ei tee. Samm 6 küsib, mis võib meid alt vedada, ja samm 7 paneb need leiud backlog'i. Samm 8 lisab kolm Giti käsku, mida kodutöös vaja läheb. Samm 9 on kodutöö. Põhiküsimus kehtib kõigi sammude kohta: iga samm lisab ühe viisi, kuidas teada saada, kas kavand on piisavalt hea. -->

---

## Kuhu jõuame

`v0.2.0` ütles, mida süsteem teeb. `v0.3.0` ütleb, kuidas me teame, et see on piisavalt hea.

**Seminari lõpuks tiimi repos:**

- läbivaatuse Issue uute rollidega ja Projectsi ajaväljad
- üks mõõdetav kontrolltingimus ja üks testjuhtum
- andmeallika risk ja 2–3 toote Issue'd

**Kodutöö lõpuks release `v0.3.0`:**

- 3–4 kvaliteedinõuet, igaühe testjuhtum ja riskikaart
- uuendatud backlog, ülevaadatud PR-id ja refleksioon

<!-- Release v0.3.0 ehitatakse v0.2.0 peale: samad kasutajalood, sama süsteemi kontseptsioon, aga nüüd kontrollitaval kujul. Seminaris tehakse igast asjast üks näidis koos: üks ümberkirjutatud kontrolltingimus, üks testjuhtum, üks risk. Kodutöös laiendab tiim seda oma lugude peale. Release võib sisaldada lahtisi küsimusi, näiteks kui andmeallika kohta pole veel vastust. Oluline on, et hetkeseis ja järgmised sammud on dokumenteeritud, mitte et kõik oleks lahendatud. Eksamil esitleb tiim just seda: kuidas v0.3.0 kvaliteedi- ja riskivalikud kavandit muutsid. -->

---

## 1. `v0.2.0` läbivaatus: tahvel

Üks arvuti tiimi kohta. Looge Issue „`v0.2.0` läbivaatus” ja vastake sinna:

1. Mis on olekus Backlog või In progress? Kas päriselt pooleli või unustati liigutada?
2. Mitmel kaardil on ajahinnang? Mitmel on tegelik aeg?
3. Millal kaardid liikusid olekusse Done: töö ajal või lõpus korraga? Kas tahvel aitas midagi otsustada?

<!-- Kolm küsimust vaatavad sama asja kolmest küljest: kas tahvel oli töövahend või aruanne. Esimene küsimus näitab, kas tahvel peegeldab tegelikkust. Kui Backlog'is on kaart, mis on päriselt tehtud, siis tahvlit ei uuendatud ja keegi ei saa sellelt otsustada. Teine küsimus kirjeldab lähtekohta: aja jälgimist pole seni õpetatud, nii et tühi väli ei ole viga, vaid koht, kust täna alustame. Kolmas küsimus on kõige tähtsam. Kui kaardid liikusid Done'i korraga viimasel õhtul, siis ei näinud keegi töö ajal, kus asi seisab, ja tahvel ei aidanud ühtegi otsust teha. „Lõpus korraga” on aus vastus ja sisend sellele, mida kodutöös 4 teisiti teha. Tiim leiab need asjad ise oma tahvlilt; see on parem kui kuulda neid õpetajalt. -->

---

## Aja jälgimine Projectsis

| Väli | Millal täidetakse |
|---|---|
| Estimate | Issue'i loomisel, mitte hiljem |
| Tegelik (h) | Issue'i sulgemisel, mitte release'i õhtul |

- uus väli: tahvli paremas servas `+` → New field → Number
- võrdlus: tabelivaade (Table), rühmitatud Statuse järgi; rühma päises on summad
- ühik on tund, täpsus pool tundi; mitme tegija ajad liidetakse

<!-- Miks aega jälgida: hinnangu ja tegeliku aja vahest õpib tiim plaanima. Väärtus ei ole täpses hinnangus, keegi ei oska alguses täpselt hinnata. Väärtus on selles, et vahe on näha ja sellest saab järelduse teha: millist tööd me alahindame ja millist ülehindame. Kui kõigi Issue'de hinnang on 1 tund olenemata sisust, ei kirjelda see tööd, vaid malli. Estimate on GitHubi Kanbani mallis olemasolev numbriväli; see on lihtsalt lahter, ühikut väli ei tea, ühiku lepib tiim kokku ja meil on see tund. Tegeliku aja jaoks tuleb teha teine numbriväli. Tabelivaates on mõlemad veerud kõrvuti ja kui tabel rühmitada Statuse järgi, näitab Projects iga numbrivälja summat rühma päises. Nii on release notes'i võrdlus kohe olemas, seda ei pea käsitsi kokku arvutama. Hinnang pannakse Issue'i loomisel, sest hiljem on tulemus juba teada ja hinnang kaldub selle poole. Tegelik aeg pannakse sulgemisel, sest release'i õhtul ei mäleta enam keegi. -->

---

## Release manageri kontrollnimekiri

- [ ] iga väide release notes'is vastab failile
- [ ] topeltfaile ega kohatäiteid pole
- [ ] AI juhiseid ega malliteksti pole lõplikus failis
- [ ] README viitab uutele otsustele ja release'ile

Kopeerige nimekiri läbivaatuse Issue'sse ja märkige ära. Iga leitud puudus saab eraldi Issue koos hinnanguga.

Sama nimekiri tuleb läbida enne `v0.3.0` avaldamist.

<!-- Release notes on lubadus: see ütleb lugejale, mis repos olemas on. Kui seal on kirjas „teekond on kirjeldatud”, aga failis on ainult numbrid 1–4, siis lubadus ei pea ja lugeja ei saa reposid usaldada. Topeltfailid, näiteks sama otsus kahe nimega, näitavad, et merge tehti kontrollimata. Kohatäited ja malli juhised nagu „asenda allolevad märkused” näitavad, et faili ei loetud enne avaldamist üle. README on uue lugeja sissepääs: kui see ei viita uutele otsustele, ei leia keegi neid üles. Nimekiri on sama, mille release manager läbib enne v0.3.0 avaldamist, nii et täna harjutab iga tiim seda oma eelmise release'i peal. Iga leitud puudus saab eraldi Issue, sest nii läheb parandus backlog'i ja selle tegemine on nähtav. -->

---

## Rollivahetus

- igaüks saab uue rolli; `v0.2.0` release manager ei ole uuesti release manager
- vaikimisi ring: projektijuht → arhitekt → disainer → release manager → projektijuht

| Roll | Vastutab kodutöös 4 |
|---|---|
| Projektijuht | tahvel ja ajaväljad, otsuste lüngad Issue'na, merge-reegel |
| Disainer | kvaliteedinõuded tiimi lugudest, mõõdetavad kontrolltingimused |
| Arhitekt | andmeallika risk ja riskikaart |
| Release manager | kontrollnimekiri ja release `v0.3.0` |

Uued rollid kirjutab projektijuht läbivaatuse Issue'sse ühe reana.

<!-- Rollid vahetuvad, et iga õppija kogeks eri vaatenurki: projektijuht näeb tööd tervikuna, arhitekt süsteemi osade ja riskide kaudu, disainer kasutaja kaudu, release manager vastutab selle eest, et avaldatud tervik peab. Rollivahetusel on täna veel üks mõte. Järgmises sammus seletab iga uue rolli kandja osa, mille kirjutas eelmine: uus arhitekt seletab v0.2.0 arhitektuuri, uus disainer disainivalikut. Nii selgub, kas dokument on arusaadav ka sellele, kes seda ei kirjutanud. See on sama test, mille päris projektides teeb uus tiimiliige. Tabel ütleb, mille eest iga roll kodutöös 4 vastutab; see ei tähenda, et ta teeb seda üksi, vaid et tema võtab tulemuse kokku ja vastutab, et see release'is on. Kolmeliikmelises tiimis on ühel inimesel kaks rolli. Rollid kirjutatakse README-sse kodutöö esimeses PR-is. -->

---

## 2. Selgita oma otsust

Järgmine etapp ehitab teie otsuste peale. Seega peab tiim oskama oma disaini, arhitektuuri ja tööviisi ise seletada.

- 10 minutit ettevalmistust, seejärel tutvustab iga tiim oma otsuseid ja seda, kuidas need tehti
- seletab see, kelle **uus** roll on teema juures; enda kirjutatud teksti ei seleta keegi
- iga seletaja kirjutab tiimi Issue'sse „Selgita oma otsust” ühe lause oma vastusega

Punkte see ei anna. Mida seletada ei oska, on leid: see läheb backlog'i.

<!-- AI kasutamine on lubatud ja jääb lubatuks. Aga v0.3.0 ehitatakse v0.2.0 otsuste peale, ja ehitada saab ainult sellele, millest aru saadakse. Kui arhitektuur ütleb, et kolm osa annavad vaatele eri tulemuse, peab tiim oskama öelda, milline osa otsustab, mida kasutaja näeb, ja miks. Kui tööviis ütleb „üks Issue korraga”, peab tiim oskama öelda, mida see reegel päriselt piirab. Seletamine oma sõnadega on ainus viis teada saada, kas mõiste on omandatud või ainult dokumenti kirjutatud. Lihtsamad mõisted on tiimidel käes: vajadus ja lahendus, tõend, merge-konflikt. Keerulisemad, nagu WIP-piirang, hinnang ja tegelik aeg, arhitektuuri vastutused ja kompromiss, on sageli kirjas ladusamalt, kui neid seletada osatakse. Lünk ei ole viga, vaid leid: see läheb Issue'na backlog'i ja selle lahendamine on osa kodutööst. Sama harjutus on ka eksami proov, sest eksamil esitleb iga õppija vähemalt ühte otsust ja mõistete test küsib sama asja. -->

---

## Mis siis, kui …?

Õpetaja postitab igale tiimile ühe muutuse, mis puudutab tiimi suurimat kontrollimata eeldust. Kirjutage viie minutiga Issue'sse kolm rida:

1. millised kasutajalood enam ei täitu;
2. mis muutub disainis või arhitektuuris;
3. milline uus Issue tekib backlog'i.

Seejärel paarid: kumbki tiim räägib 2 minutit ja kuulaja tiim küsib ühe küsimuse.

Need kolm rida on teie esimene risk kodutöö 4 riskikaardis.

<!-- See on riskianalüüs praktikas, enne kui mõistet riskikaart üldse nimetame. Iga tiimi kavand toetub mõnele eeldusele, mida pole kontrollitud, enamasti andmeallika kohta: et kalendriekspordist saab andmed kursuse kaupa, et ÕIS-i andmeid tohib kasutada, et allikas näitab, mis muutus. Muutus, mille õpetaja postitab, on see eeldus vastupidi pööratuna. Kolm rida näitavad, kuidas kasutajalood, disain, arhitektuur ja backlog on omavahel seotud: kui eeldus ei pea, ei täitu mõni lugu, arhitektuuris muutub mõni osa ja backlog'i tekib töö, mida varem polnud. Just see seos on see, mida riskikaardi veerud „mõju” ja „maandus” hiljem küsivad. Paaris esitamine on vajalik, sest teise tiimi küsimus paljastab, mis seletuses puudu on. Kolm rida on kodutöö riskikaardi esimene rida, nii et see töö ei lähe kaduma. -->

---

## Üks lause oma projekti näitega

Vali üks mõiste ja kirjuta kleepsule üks lause, nagu seletaksid esimese kursuse sõbrale:

> „WIP-piirang on …, meie projektis …”

WIP-piirang · hinnang ja tegelik aeg · risk ja eeldus · kompromiss · sõltuvus · kontrolltingimus · süsteemi piir

<!-- Mõiste definitsiooni oskab iga AI. Oma projekti näidet oskab ainult see, kes on aru saanud. Sellepärast on lause kaheosaline: mis mõiste on ja mida see meie projektis tähendab. „WIP-piirang on see, et korraga on pooleli piiratud arv töid; meie projektis oli piirang 3 Issue't, aga see ei peatanud meid kordagi, sest kõik tööd olid korraga pooleli.” See lause ütleb rohkem kui definitsioon. Mõisted on järjekorras kõige vähem omandatust alates: WIP-piirang ja hinnang on need, mida kodutöös 3 keegi oma sõnadega ei seletanud. Eksami mõistete test küsib täpselt sama: seletus oma sõnadega ja seos oma projektiga. Mõiste, mille juures on kõige rohkem definitsioone ja kõige vähem näiteid, saab sammus 7 eraldi tähelepanu. -->

---

# 3. Kui tarkvara töötab, kas see on kvaliteetne?

<!-- Tavaline vastus on jah: kui süsteem teeb, mida kasutajalood nõuavad, on töö tehtud. Tunniplaani näide: süsteem näitab iga rühma tunniplaani ja kõik lood on täidetud. Aga telefonis tuleb iga kord rühm uuesti valida, leht laeb mobiilivõrgus kümme sekundit ja muutunud tund on märgitud ainult halli värviga. Kõik lood on täidetud ja ometi ei kasuta seda keegi. -->

---

## Mitte tingimata

See võib olla aeglane, ebaturvaline, raskesti kasutatav, ligipääsmatu või kallis hooldada.

Kvaliteet tähendab sobivust päris kasutusolukorda.

<!-- Töötamine ei võrdu kvaliteediga. Iga sõna sellel slaidil on omaette kvaliteediomadus: aeglane tähendab jõudlust, ebaturvaline turvalisust, raskesti kasutatav kasutatavust, ligipääsmatu ligipääsetavust ja kallis hooldada hooldatavust. Kvaliteet ei ole abstraktne „hea”, vaid sobivus konkreetsesse kasutusolukorda. Tunniplaani vaade, mida vaadatakse koridoris telefonist loengute vahel, peab olema kiire ja ühe käega kasutatav. Sama süsteem suurel ekraanil õppeosakonnas vajab hoopis muud. Sellepärast küsime enne kvaliteedi hindamist alati, kes ja mis olukorras süsteemi kasutab; see tuli kasutajalugudest ja personadest. -->

---

## Funktsioon ja kvaliteediomadus

**Funktsioon:** mida süsteem teeb? Näiteks õppija näeb järgmise loengu aega ja ruumi.

**Kvaliteediomadus** ehk mittefunktsionaalne nõue: kui hästi või millistel tingimustel? Näiteks telefonis, kuni 10 sekundiga, ilma rühma uuesti valimata.

<!-- Sama funktsiooni saab teha väga erineva kvaliteediga. „Õppija näeb järgmise loengu aega ja ruumi” on täidetud nii siis, kui see võtab kaks sekundit, kui ka siis, kui see võtab minuti ja kolm klõpsu. Funktsioon vastab küsimusele „mida”, kvaliteediomadus küsimusele „kui hästi” või „mis tingimustel”. Ingliskeelne termin on non-functional requirement ehk mittefunktsionaalne nõue; see nimi on veidi eksitav, sest nõue ei ole funktsioonita, vaid lisab funktsioonile tingimused. Levinumad omadused on kasutatavus, jõudlus, töökindlus, andmete õigsus, ligipääsetavus, turvalisus ja hooldatavus. Kasutajaloo kontrolltingimused sisaldavad sageli juba kvaliteediomadusi, ainult et ebamääraselt: „kiiresti”, „mugavalt”. Järgmine slaid vaatab, mis sellega teha. -->

---

# „Tudeng leiab järgmise loengu kiiresti.”

Kas see on kontrollitav?

<!-- Igaüks saab sellest lausest aru, aga igaüks saab aru erinevalt. Ühele on kiiresti kaks sekundit, teisele pool minutit. Kui testija ütleb, et leidis loengu 20 sekundiga, siis kas test õnnestus? Keegi ei oska vastata, sest lause ei ütle, mille järgi otsustada. Sama viga arutasime seminaris 3 sõna „moodne” juures: see on omadussõna, mille taga pole mõõdupuud. Kodutöö 3 kontrolltingimustes oli selliseid sõnu palju: „kiiresti”, „mugavalt”, „ilma liigse ajakuluta”. -->

---

## Ebamäärasest mõõdetavaks

| Enne | Pärast |
|---|---|
| Tudeng leiab järgmise loengu kiiresti. | Tudeng leiab telefonis oma rühma järgmise loengu aja ja ruumi kuni 10 sekundiga ilma rühma uuesti valimata. |

Küsi: **kes** ja mis olukorras, **mida** täpselt kontrollitakse, **milline arv või tingimus** näitab, et nõue on täidetud.

Nii kirjutatud kontrolltingimus on **kvaliteedinõue**: kvaliteediomadus koos mõõdetava piiriga. Arv tuleb mõõtmisest, mitte peast.

<!-- Kolm küsimust teevad ebamäärase lause kontrollitavaks. Kes ja mis olukorras: tudeng telefonis, mitte „kasutaja”. Mida kontrollitakse: järgmise loengu aja ja ruumi leidmist, mitte „tunniplaani kasutamist”. Milline arv või tingimus: kuni 10 sekundit ja ilma rühma uuesti valimata. Nüüd oskab testija öelda, kas test õnnestus. Arv ei tohi olla peast võetud. Kui praegusel tunniplaanilehel kulub telefonis järgmise loengu leidmiseks 40 sekundit, on 10 sekundit selge paranemine ja seda saab põhjendada. Kui keegi ei ole praegust olukorda mõõtnud, on 10 sekundit sama ebamäärane kui „kiiresti”. Kõik ei pea olema sekundites: „ilma rühma uuesti valimata” on tingimus, mida saab kontrollida jah-ei vastusega, ja „4 kasutajat 5-st täidavad ülesande ilma abita” on mõõdetav kasutatavuse nõue. Terminite seos: kvaliteediomadus on näiteks jõudlus; kui sellele lisada mõõdetav piir, saab sellest kvaliteedinõue; kasutajaloo juures kannab seda kontrolltingimus. -->

---

## Harjutus: teie oma kontrolltingimus

Valige oma lugudest üks kontrolltingimus, milles on mõõtmata sõna: „kiiresti”, „mugavalt”, „ilma liigse ajakuluta”. Kirjutage see ümber.

Seejärel valige **3–4** kvaliteediomadust, mis tulenevad teie lugudest. Kõiki omadusi katta ei ole vaja.

Juhend ja omaduste loend: [Mõõdetav kvaliteet](../../handbook/04-quality-and-risk/01-measurable-quality.md)

<!-- Kolm kuni neli omadust on teadlik piirang. Kui tiim üritab katta kõiki seitset levinud omadust, tekib loend, kus iga rida on üldine ja ükski ei tulene projektist. Kolm omadust, mis tulevad tiimi enda lugudest, ütlevad rohkem. Tunniplaani puhul tulevad lugudest enamasti kasutatavus telefonis, andmete õigsus ja ajakohasus ning töökindlus andmete laadimise tõrke korral. Turvalisus võib olla sellel projektil väike teema, kui süsteem isikuandmeid ei kogu; see on lubatud valik, kui see on põhjendatud. Disainer võtab tulemuse kokku, sest kvaliteedinõuded on tema vastutus kodutöös 4. Konspekti leht sisaldab omaduste tabelit koos mõõdetava nõude näitega iga omaduse kohta. -->

---

## Kvaliteeti nähakse eri moodi

- kasutaja: eesmärk, arusaadavus ja turvalisus
- organisatsioon: väärtus ja kohustused
- arendaja: muudetavus
- käitaja: märgatavus ja taastatavus
- ühiskond: mõju ja ligipääs

<!-- Kvaliteet sõltub sellest, kes küsib. Kasutaja küsib, kas ta saab eesmärgi täidetud turvaliselt ja arusaadavalt: kas ma leian loengu ja kas keegi ei näe minu andmeid. Organisatsioon ehk kool küsib, kas tulemus loob väärtust ja vastab kohustustele: kas õppijad jõuavad loengusse ja kas isikuandmete kasutamine on lubatud. Arendaja küsib, kas süsteemi saab mõista ja muuta: kui kool vahetab tunniplaanisüsteemi, kas meie vaade on kohandatav. Käitaja ehk see, kes süsteemi töös hoiab, küsib, kas rikkeid saab märgata ja taastada: kas keegi saab teada, kui andmed enam ei lae. Ühiskond küsib, kellele süsteem võib kahju teha või kelle ligipääsu sulgeda: kas ekraanilugeja kasutaja jääb tunniplaanist ilma. Üks ja sama süsteem võib olla kasutaja jaoks suurepärane ja käitaja jaoks õudusunenägu. Sellepärast valib tiim kvaliteediomadusi rollide vaatenurkadest, mitte ainult kasutaja omast. -->

---

## Valikud sisaldavad kompromisse

Turvalisus võib lisada samme. Töökindlus võib tõsta hinda. Kiire tarne võib kasvatada hooldusvõlga.

Kompromiss on lubatud, kui see on teadlik ja kirjas: millest loobume ja miks.

<!-- Kõiki omadusi ei saa korraga maksimeerida, sest need on omavahel vastuolus. Sisselogimine kaitseb isiklikke valikuid, aga lisab iga kasutuse juurde sammu ja tunniplaani vaatamine koridoris muutub aeglasemaks. Varukoopia ja teine server tõstavad töökindlust, aga ka hinda. Kiire valmimine tähendab sageli, et kood tehakse lihtsalt tööle ja korrastatakse hiljem; see „hiljem” on hooldusvõlg ehk tehniline võlg, mille intressi maksab iga järgmine muudatus. Kompromiss ei ole halb. Halb on kompromiss, mida keegi ei teinud teadlikult ja mis avastatakse siis, kui on hilja. Tunniplaani näide: tiim, kes otsustab, et vaade ei nõua sisselogimist, loobub isiklikest valikutest, aga võidab lihtsuse ja privaatsuse. See on hea otsus, kui see on otsuste logis kirjas koos põhjusega. Kodutöö nõuab vähemalt üht nähtavat kompromissi just sellepärast. -->

---

## Kontrollküsimused iga kavandi juures

**Turvalisus ja privaatsus:** kas neid andmeid on päriselt vaja? Kellel on ligipääs ja kui kaua neid hoitakse? Mis juhtub lekke korral?

**Ligipääsetavus:** kas info on edasi antud ainult värviga? Kas süsteem töötab ekraanilugeja, klaviatuuri, aeglase võrgu ja väikese ekraaniga?

Ühest konkreetsest reast piisab. Mida vähem isikuandmeid süsteem kogub, seda väiksem on privaatsusrisk.

<!-- Need kaks teemat ei ole eraldi peatükid, vaid küsimused, mis käivad iga kavandi juures. Turvalisus ja privaatsus algavad küsimusest, kas andmeid on üldse vaja. Tunniplaani vaade ilma sisselogimiseta ei kogu isikuandmeid ja privaatsusrisk on peaaegu null; see on disainivalik, mitte tehniline kaitse. Kui tiim tahab salvestada õppija valikaineid, tekib kohe küsimus, kellel on ligipääs, kui kaua andmeid hoitakse ja mis juhtub lekke korral. Ligipääsetavus tähendab, et süsteemi saavad kasutada ka need, kes näevad, kuulevad või liiguvad teisiti, ning need, kellel on aeglane võrk või vana telefon. Levinud viga on info andmine ainult värviga: muutunud tund on punane, aga värvipimedale või ekraanilugejale ei ütle see midagi. Lahendus on lisada tekst „muutunud”. Euroopa Liidus on avalike teenuste ligipääsetavus seadusega nõutud ja kooli tunniplaan on avalik teenus. Kavandisse piisab ühest konkreetsest reast iga teema kohta; pikk üldine peatükk ei anna midagi juurde. -->

---

## 4. Testjuhtum seob nõude kontrolliga

Kontrolltingimus ütleb, *mis* peab olema tõsi. Testjuhtum ütleb, *kuidas* seda kontrollida.

| Väli | Sisu |
|---|---|
| Test | T1: valitud rühm on telefonis nähtav (lugu 1) |
| Eeldused | telefon, ekraani laius kuni 400 px; valitud on rühm RIF26 |
| Sammud | 1. Ava tunniplaan. 2. Vali rühm RIF26. 3. Sulge menüü. 4. Keri alla. |
| Oodatud tulemus | rühma nimi on kogu aeg nähtav ilma menüüd avamata |

Testi saab kirjutada enne, kui süsteem on olemas.

<!-- Testimine võrdleb oodatud tulemust tegeliku tulemusega kindlates tingimustes. Testjuhtum on selle kirjeldus ette: eeldused ütlevad, mis peab enne testi tõsi olema, näiteks seade ja valitud rühm; sammud on täpsed tegevused järjekorras, nii et teine inimene saab sama testi korrata; oodatud tulemus ütleb, mida peab nägema, kui kõik on korras. Tegelik tulemus on viies väli, mis täidetakse alles testimisel. Näide on seminari 3 näidisloost: õppija soovib telefonis kogu aeg näha, millise rühma tunniplaani ta vaatab. Kontrolltingimus ütles, et rühma nimi on nähtav; testjuhtum ütleb, kuidas seda kontrollitakse, sealhulgas kerimine allapoole, mis on just see koht, kus nimi tavaliselt kaob. Testi saab kirjutada enne, kui süsteemi on olemas, ja päris projektides tehaksegi nii: test on valmis enne, kui arendaja tööd alustab, ja arendaja teab, mille järgi tema tööd kontrollitakse. Kuna meil süsteemi pole, võib sama testi proovida praeguse tunniplaanilehe peal. See näitab, kas probleem päriselt esineb, ja on ühtlasi tõend. Seda tüüpi testi nimetatakse vastuvõtutestiks: see kontrollib, kas süsteem rahuldab kasutaja vajadust. -->

---

## Testi ka seda, mis võib valesti minna

| Test | Eeldus | Oodatud tulemus |
|---|---|---|
| T2: tühi nädal | valitud nädalal tunde pole | teade „sel nädalal tunde pole” |
| T3: andmed ei lae | andmeallikas ei vasta | teade „andmeid ei õnnestunud laadida”, mitte tühi tunniplaan |

Kasutajale näevad need esmapilgul ühesugused välja. Kui süsteem neid ei erista, arvab õppija, et tund jäi ära.

**Harjutus:** tiim kirjutab ühe testjuhtumi koos. Kodutöös kirjutab igaüks ühe oma loo kohta. Juhend: [Testjuhtum](../../handbook/04-quality-and-risk/02-test-cases.md)

<!-- Hea testide komplekt ei kontrolli ainult tavalist olukorda, kus kõik läheb hästi. Erijuhud on kohad, kus süsteemid tavaliselt vigu teevad: tühi sisend, puuduvad andmed, katkenud võrk. T2 ja T3 on tunniplaani puhul kõige olulisem paar. Tühi nädal on päris olukord, näiteks vaheaeg. Andmete laadimise tõrge on rike. Mõlemal juhul ei näe õppija ühtegi tundi, aga tähendus on vastupidine: ühel juhul võib ta rahulikult koju jääda, teisel juhul peaks ta kontrollima mujalt. Süsteem, mis mõlemal juhul näitab tühja tabelit, eksitab kasutajat kõige halvemal hetkel. Lahendus on lihtne: eri olukorras eri teade. Just see erinevus oli kodutöös 3 mõnel tiimil juba arhitektuuris kirjas ja täna saab sellest testjuhtum. Harjutuses kirjutab tiim ühe testi koos, et väljad selgeks saaksid; kodutöös kirjutab iga õppija ühe testi oma kasutajaloo kohta, nii et kõigil lugudel on vähemalt üks test. -->

---

## 5. Arendamise etapp

Arendajad muudavad nõuded ja kavandi töötavaks tarkvaraks: kirjutavad koodi, teevad tehnilisi valikuid, vaatavad üksteise koodi üle ja parandavad vigu.

Sellel kursusel me rakendust ei ehita, sest eesmärk on näha kogu protsessi. Kaks arendaja oskust on kasulikud igas rollis: vea kirjeldamine ja ülevaatus.

<!-- Arendamise etapp on see, mida enamik inimesi tarkvaraarenduse all mõtleb: koodi kirjutamine. Kursuse esimesest seminarist peale on põhisõnum, et see on ainult üks osa. Arendaja töö ei ole ainult kirjutamine: ta teeb tehnilisi valikuid, näiteks kuidas andmed vahemällu salvestada; ta vaatab üle kaaslase koodi; ta otsib ja parandab vigu. Kursusel me rakendust ei ehita, sest siis kuluks kogu aeg koodile ja muud etapid jääksid nägemata. Programmeerimist õpitakse teistes ainetes. Kaks arendaja oskust on aga kasulikud igas rollis ja neid harjutame: vea kirjeldamine nii, et teine saab selle korrata, ja ülevaatus, kus kaaslane loeb muudatuse enne ühendamist läbi. Sama ülevaatuse põhimõtet kasutab tiim juba praegu dokumentide PR-ide juures. -->

<!-- Tulevikus: arendaja töö võib nihkuda kirjutamiselt suunamisele ja kontrollile. Samaks jääb: arendaja vaatab töö üle ja töövoogude arvu piirab see, kui palju ta suudab korralikult üle vaadata. -->

---

## Viga, silumine ja koodi ülevaatus

- **Viga** (*bug*): süsteem käitub teisiti, kui oodati. Põhjus võib olla ka nõudes või andmetes.
- **Silumine** (*debugging*): korda viga väikese näitega, kirjelda oodatud ja tegelik tulemus, kitsenda põhjust, kontrolli oletust, paranda ja korda testi.
- **Koodi ülevaatus** (*code review*): kas muudatus teeb seda, mida PR lubab? Kas sellest saab aru? Mis juhtub erijuhtudel?

Hea kommentaar on konkreetne küsimus koodi, mitte inimese kohta.

**Kodutöös iseseisvalt:** väikese näite vea kirjeldus ja ülevaatuse kommentaar oma Issue'sse. Koodi kirjutama ei pea.

<!-- Viga on olukord, kus süsteem käitub teisiti, kui oodati. Oluline on sõna „oodati”: kui ootus oli vale, on viga nõudes, mitte koodis. Tunniplaani puhul võib viga olla ka andmetes: allikas annab vale ruumi ja kood näitab seda õigesti. Silumine käib ringina. Kõigepealt korratakse viga võimalikult väikese näitega, sest viga, mida ei saa korrata, ei saa ka parandada. Siis pannakse kirja oodatud ja tegelik tulemus; see on sama paar, mis testjuhtumis. Seejärel kitsendatakse põhjust: milline osa võib vea tekitada. Oletust kontrollitakse enne parandamist, mitte ei parandata pimesi. Pärast parandust korratakse algset testi ja hea tava on lisada kontroll, et sama viga tagasi ei tuleks. Koodi ülevaatuses loeb kaaslane muudatuse enne ühendamist läbi ja küsib kolm asja: kas kood teeb seda, mida PR lubab; kas sellest saab aru ka keegi teine; mis juhtub erijuhtudel, näiteks tühja sisendiga. Hea kommentaar on konkreetne ja küsimuse vormis: „Mis juhtub, kui loend on tühi?” on parem kui „See on vale”, sest võib-olla oli autoril põhjus, mida ülevaataja ei näe. Kommenteeritakse koodi, mitte inimest. Kodutöös teeb iga õppija selle läbi väikese näitega konspekti juhendi järgi: ennustab tulemuse, kirjutab vea kirjelduse ja vaatab paranduse üle nagu PR-i. -->

<!-- Tulevikus: AI võib teha esimese ülevaatuse ja järjestada leiud tõsiduse järgi. Samaks jääb: koodi kirjutanud agent ei saa seda heaks kiita, kinnituse annab inimene. -->

---

# 6. Mis võib meid alt vedada?

<!-- Risk ei ole halbade asjade nimekiri, mille tiim kirjutab, sest kodutöö nõuab. See on otsustamise vahend: millele pöörata tähelepanu enne, kui on hilja, mida kontrollida ja kes reageerib. Tunniplaani projektis on kõige suurem risk juba teada: viis tiimi kuuest ei tea, kas andmed kätte saab. -->

---

## Risk ja eeldus

**Eeldus** on väide, mida peame tõeseks, kuigi pole seda kontrollinud. Iga kontrollimata eeldus on risk.

| | Näide |
|---|---|
| Eeldus | „Tunniplaani andmed on tõenäoliselt olemas.” |
| Risk | „Allikas ei sisalda tulevasi kuupäevi või seda ei tohi kasutada. Järgmist loengut ei saa näidata.” |
| Maandus | „Kontrollime enne jätkamist, millised väljad allikas on ja kas neid tohib kasutada.” |

„Tõenäoliselt olemas” ei ole maandus. See on just see, mida tuleb kontrollida.

<!-- Risk ja eeldus on sama asja kaks külge. Eeldus on see, mida peame tõeseks ilma kontrollimata; risk on see, mis juhtub, kui eeldus ei pea. Kodutöö 3 kontseptsioonides oli andmeallika kohta sageli lause „andmed on tõenäoliselt kalendriekspordist saadaval”. See on eeldus. Sellele toetub kogu arhitektuur: kui allikas ei anna tulevasi kuupäevi, ei saa näidata järgmist loengut, ja see on peaaegu iga tiimi põhiline lugu. Levinud viga on kirjutada eeldus riskikaardi maanduse veergu. „Andmed on tõenäoliselt olemas” ei vähenda riski; see on täpselt see väide, mida tuleb kontrollida. Maandus on tegevus: kontrollime allikat näidispäringuga enne, kui kavandiga edasi läheme. Sellepärast nõuab kodutöö, et eeldused oleksid riskidest eraldi kirjas. Siis on näha, mida tiim veel ei tea, ja iga eeldus saab kas kontrollitud või muutub riskiks koos maandusega. -->

---

## Riskikaart

| Väli | Küsimus |
|---|---|
| Mis võib juhtuda | mis sündmus? |
| Mõju | kellele ja kui tõsine: madal / keskmine / kõrge |
| Tõenäosus | madal / keskmine / kõrge |
| Kuidas märkame | mis märk näitab, et risk realiseerub? |
| Maandus | mida teeme, et risk või mõju oleks väiksem? |
| Vastutaja | milline **roll** reageerib? |

„Meeskond” ei ole vastutaja: kui kõik vastutavad, ei reageeri keegi.

<!-- Riskikaart on tabel, kus iga rida on üks risk ja iga veerg üks küsimus. Mis võib juhtuda on konkreetne sündmus, mitte teema: „andmeallikas ei sisalda tulevasi kuupäevi”, mitte „andmete probleemid”. Mõju ütleb, kellele ja kui tõsine: kõrge, kui põhiline lugu ei täitu; keskmine, kui osa kasutajaid ei märka muudatust. Tõenäosus on hinnang skaalal madal, keskmine, kõrge; täpsemat ei ole vaja ja see petaks täpsusega, mida pole. Kuidas märkame on veerg, mis sageli unustatakse: milline märk näitab, et risk on realiseerumas. Kui tiim ei oska seda öelda, saab ta riskist teada alles siis, kui kasutaja kaebab. Maandus on tegevus, mis vähendab tõenäosust või mõju, ja see võib olla ka kavandi muutmine: isikuandmete lekke riski saab vältida, kui andmeid ei koguta. Vastutaja on roll, näiteks arhitekt või projektijuht, mitte inimese nimi ja mitte „meeskond”. Kui kõik vastutavad, ei reageeri keegi, sest igaüks arvab, et teine tegeleb. Alustatakse ridadest, kus mõju ja tõenäosus on mõlemad kõrged; pikk loend madala mõjuga riske on müra, milles oluline kaob. -->

---

## Harjutus: teie riskikaart

- kohustuslik: üks risk tunniplaani **andmeallika** kohta; sisend on „Mis siis, kui” kolm rida
- lisaks vähemalt 5 muud riski, väiksemal tiimil vähem
- eeldused eraldi kirja: siis on näha, mida veel ei teata
- alustage riskidest, mille mõju ja tõenäosus on kõrged

[Riskikaardi mall](../mallid/riskikaart.md) · [Juhend: Riskid](../../handbook/04-quality-and-risk/04-risks.md)

<!-- Andmeallika risk on kohustuslik, sest see on kõigi tiimide suurim kontrollimata eeldus ja „Mis siis, kui” harjutus andis selle jaoks juba sisendi: millised lood ei täitu, mis muutub arhitektuuris, mis Issue tekib. Need kolm rida on mõju, maandus ja backlog'i kirje. Viis muud riski tulevad tiimi enda kavandist: laadimise tõrget tõlgendatakse ärajäämisena, muutunud tund on märgitud ainult värviga, kool vahetab tunniplaanisüsteemi, tiimiliige haigestub enne release'i. Riskid võivad olla ka töökorralduse kohta, mitte ainult tehnilised. Eeldused kirjutatakse eraldi, et oleks näha, mida tiim veel ei tea; kodutöö jooksul saab osa eeldusi kontrollitud ja need kaovad, osa muutub riskiks. Kui andmeallika kohta pole võimalik täna vastust saada, on see lubatud: siis tekib Issue, mis ootab infot väljastpoolt, ja sammus 7 vaatame, kuidas sellist ootavat tööd märkida. Arhitekt võtab riskikaardi kokku, sest see on tema vastutus kodutöös 4. Mall mallide kaustas annab tabeli valmis veergudega ja ühe näidisreaga. -->

<!-- Tulevikus: reeglid võivad olla töövoogu sisse ehitatud, näiteks saladuste kaitse. Pelk juhis ei taga nende täitmist. Samaks jääb: reeglil on nimeline omanik. -->

---

## Kolmandad osapooled

Teek, pilveteenus, andmestik, font või AI-mudel toob lisaks kasule sõltuvuse: litsents ja tingimused, andmete liikumine, hind, jätkusuutlikkus ja asendatavus.

Näide: Cloudflare'i 2019. aasta katkestus viis maha tuhandeid veebilehti, mis ise midagi valesti ei teinud. [Allikas](https://blog.cloudflare.com/cloudflare-outage/)

<!-- Peaaegu iga süsteem toetub millelegi, mida tiim ise ei tee: teek, mis joonistab kalendrit; pilveteenus, kus leht jookseb; andmestik, millest tunniplaan tuleb; font; AI-mudel. Iga selline asi kiirendab tööd ja toob kaasa sõltuvuse. Viis küsimust iga sõltuvuse kohta: mis litsents ja tingimused sellel on ja kas me tohime seda nii kasutada, nagu plaanime; kuhu meie või kasutaja andmed liiguvad; mis see maksab praegu ja mis siis, kui kasutajaid on rohkem; kas seda arendatakse edasi või on see juba hääbumas; kas seda saab vajadusel asendada või oleme lukus. Tunniplaani projekti suurim sõltuvus on kooli andmeallikas, ja see ongi andmeallika risk. Cloudflare on näide sõltuvuse mõjust: 2019. aasta juulis lisas Cloudflare oma veebitulemüüri ühe reegli, milles oli vigane regulaaravaldis. Reegel levitati sekunditega kogu maailma serveritesse, protsessorid jooksid täis ja Cloudflare'i kaudu töötavad veebilehed olid umbes pool tundi maas. Need lehed ise ei teinud midagi valesti; nad sõltusid ühest teenusest. Cloudflare'i enda järelanalüüs ütleb, et põhjus ei olnud ainult üks vigane rida, vaid see, et testimine ei püüdnud viga kinni, levitamine oli liiga kiire ja ülemaailmne ning kaitsemehhanism, mis oleks pidanud muudatuse tagasi võtma, oli ise sama rikke all. Rike tekib koodi, testimise, levitamise ja seire koosmõjus, mitte ühes reas. -->

---

# Mida uus risk meie varasemas kavandis muudab?

<!-- Kui riskikaart on valmis ja ükski varasem otsus ei muutu, siis on tõenäoliselt riskikaart tehtud kodutöö pärast, mitte projekti pärast. Riskianalüüsi mõte ongi leida enne ehitamist kohad, kus kavand ei pea. -->

---

## Muutus ei ole läbikukkumine

Kui uus info muudab otsust, on arendusprotsess oma eesmärki täitnud.

Kirjutage otsuste logisse uus otsus: mis risk ilmnes, mida see muutis ja mida otsustasite.

<!-- Algajad tajuvad otsuse muutmist sageli vea tunnistamisena ja hoiavad vanast otsusest kinni. Päris projektides on vastupidi: otsus, mis uue info peale ei muutu, on kahtlane. Kogu kursuse protsess on ehitatud nii, et iga etapp annab uut infot: tõendid muutsid probleemi arusaama, kasutajalood muutsid kontseptsiooni ja riskid muudavad nüüd kavandit. Otsuste logi on just selleks, et muutus oleks nähtav ja põhjendatud. Uus otsus ei kirjuta vana üle, vaid viitab sellele: otsus 003 valis suuna B; risk, et andmeallikas ei anna kursuse kaupa andmeid, muudab suuna B kalliks; otsus 004 täpsustab suunda või läheb tagasi A juurde. Eksamil on vähemalt ühe muutunud või tagasi võetud otsuse käsitlemine oluline osa esitlusest, sest see näitab, et protsess töötas. Kodutöö nõuab vähemalt üht varasema otsuse kinnitust, täpsustust või muutmist; kinnitus on ka lubatud, kui see on põhjendatud riskikaardiga. -->

---

## 7. Backlog tuleb tootest

Looge 2–3 Issue'd oma lugudest või riskidest, mitte kodutöö sammudest.

- hea: „Kontrolli kalendriekspordi välju”, „Tee kontrolltingimusest testjuhtum”
- mitte: „Kirjuta refleksioon”, „Tee release”

Hinnang (Estimate) kohe loomisel. Lisaks kolm „Selgita oma otsust” lünka Issue'na.

<!-- Backlog on toote vajaduste loend, mitte kodutöö ülesannete loend. Erinevus on selles, kust Issue tuleb. „Kontrolli kalendriekspordi välju” tuleb riskist; „tee kontrolltingimusest testjuhtum” tuleb kasutajaloost. „Kirjuta refleksioon” tuleb kodutöö juhendist ja see ei ütle midagi selle kohta, mida toode vajab. Kodutöös 3 koosnes paljude backlog kodutöö sammudest ja sellepärast ei saanud tahvlilt näha, kuidas toode edeneb. Hinnang pannakse Issue'ile kohe loomisel, sest see on ainus hetk, kui hinnang on päriselt hinnang. Hiljem on töö juba tehtud ja number kaldub tegeliku poole. Hinnangu ja tegeliku aja vahe Issue'de kaupa on see, millest tiim õpib: kui „kontrolli kalendriekspordi välju” hinnati ühele tunnile ja kulus neli, siis andmete kontrollimist alahinnatakse ja järgmine kord tuleb seda arvestada. Kolm „Selgita oma otsust” lünka lähevad ka backlog'i: iga küsimus, millele tiim ei osanud vastata, on töö, mis tuleb teha enne, kui saab edasi ehitada. -->

---

## WIP-piirang ja blokeerija

**WIP-piirang** (*work in progress*): kui palju tööd võib korraga olla olekus In progress. Piirang sunnib pooleli oleva lõpetama, mitte uut alustama.

**Blokeerija** (*blocker*): takistus, mille tõttu Issue'iga ei saa edasi, kuigi tegija tahaks. Tavaliselt oodatakse kellegi vastust või infot.

Blokeeritud kaart näeb tahvlil välja nagu tavaline pooleliolev töö. Seepärast märgitakse see eraldi.

<!-- WIP tähendab work in progress ehk pooleli olevat tööd. WIP-piirang on Kanbani keskne reegel: olekus In progress tohib korraga olla ainult piiratud arv kaarte, näiteks kolm kogu tiimi peale. Mõte on selles, et pooleli olev töö ei loo väärtust; väärtus tekib, kui töö on valmis. Kui kõik on korraga pooleli, ei saa midagi valmis ja keegi ei näe, kus asi seisab. Piirang sunnib tiimi lõpetama enne, kui alustab uut, ja paljastab ummiku: kui piirang on täis ja keegi ei saa uut võtta, on põhjus kuskil, näiteks ootab kolm kaarti ülevaatust. Kodutöös 3 oli mõnel tiimil piirang kirjas, aga see ei peatanud kedagi, sest tahvlit ei kasutatud töö ajal. Blokeerija on takistus, mille tõttu tööga ei saa edasi, kuigi tegija tahaks: ootame õppeosakonna vastust, ootame kaaslase PR-i, ootame infot andmeallika kohta. Probleem on, et blokeeritud kaart näeb tahvlil välja nagu tavaline pooleli töö. Kui seda ei märgita, ei tea keegi peale tegija, et töö seisab, projektijuht ei saa aidata ja tähtaeg tuleb üllatusena. Blokeeritud kaart võtab WIP-piirangust ühe koha. See on õige: nii on tiimil põhjus takistus kõrvaldada, mitte lihtsalt uus töö võtta. -->

---

## Kuidas blokeerijat märkida

1. Kaart jääb olekusse In progress.
2. Issue saab sildi `blocked`.
3. Kommentaar: mida ootame, kellelt ja millal kontrollime uuesti.
4. Kui blokeerija on teine Issue, märgi seos „Mark as blocked by”.
5. Takistuse kadumisel eemalda silt ja kirjuta, mis selle lahendas.

Sama seose teine ots: blokeeriv Issue võib saada sildi `blocker`, et see enne ära teha. Kumbki silt ei asenda teist.

**Harjutus:** kui andmeallika Issue ootab infot väljastpoolt tiimi, märkige see blokeerituks.

<!-- Kaart jääb olekusse In progress ja eraldi veergu ei tehta, sest tahvli olekud on kogu kursuse jooksul samad: Backlog, In progress, Review, Done. Uus veerg iga erijuhu jaoks muudab tahvli loetamatuks. Silt blocked on nähtav nii tahvlil kui Issue'de nimekirjas, nii et projektijuht näeb ühe pilguga, mis seisab. Kommentaar vastab kolmele küsimusele: mida ootame, kellelt ootame ja millal kontrollime uuesti. Viimane on oluline, sest ilma kuupäevata jääb blokeeritud kaart ootama lõputult. Kui blokeerija on teine Issue, näiteks testjuhtumit ei saa teha enne, kui kontrolltingimus on ümber kirjutatud, saab seose märkida Issue'i külgribal ja GitHub näitab seda mõlemas Issue's. Kui takistus kaob, eemaldatakse silt ja kirjutatakse, mis selle lahendas; nii jääb ajalugu alles ja järgmine kord teab tiim, kui kaua selline ootamine võtab. Andmeallika Issue on tõenäoliselt esimene blokeeritud kaart, sest vastus tuleb väljastpoolt tiimi. Sama seost saab vaadata ka teisest otsast: Jiras on „Blocker” prioriteet, mis käib blokeeriva pileti peal ja ütleb, et see tuleb enne ära teha, sest teised seisavad selle taga. GitHubis võib sama märkida sildiga blocker. Kui seos on märgitud „blocked by” kaudu, näitab GitHub blokeerival Issue'l „Blocking” ja ootaval „Blocked by”, nii et eraldi silti blokeerijale pole vaja. Silt blocked jääb välise ootamise jaoks, kus teist Issue't pole. -->

---

## 8. Giti ajalugu ja tagasivõtmine

Kvaliteet ja riskid kehtivad ka tiimi enda töö kohta. Git annab kolm kontrolli:

```bash
git log --oneline
git diff
git restore proov.md
```

- `log`: kas sõnumitest saab aru, mida tehti?
- `diff`: mis on veel commit'imata?
- `restore`: kustutab faili commit'imata muudatused. Neid ei saa tagasi.

Juba push'itud viga: ära muuda ajalugu, tee parandav commit. VS Code'is ja harjutus: [Giti ajalugu ja tagasivõtmine](../../handbook/04-quality-and-risk/06-git-history.md)

<!-- Terve seminar rääkis kavandi kvaliteedist ja riskidest. See slaid pöörab sama pilgu tiimi enda töövoole. git log on jälgitavus: release manager ja eksami ajajoon toetuvad sellele. git diff on oma töö test enne esitamist: oodatud muudatus võrreldes tegelikuga. git restore ja git revert on riski maandus, täpselt nagu Cloudflare'i tagasipööramine, ainult väiksemas mastaabis. Kolm käsku vastavad kolmele küsimusele. Mis on tehtud: git log näitab commit'ide ajalugu, uuemad eespool; --oneline paneb iga commit'i ühele reale koos lühitunnuse ja sõnumiga. Siit on hästi näha, miks head commit'i sõnumid on olulised: sõnumitest „update” ja „fix” ei saa aru, mida tehti, sõnumitest „Add risk map” ja „Clarify acceptance criterion” saab. Eksamil tehakse release'ide ajajoon just selle ajaloo põhjal. Mida ma praegu muutsin: git diff näitab muudatusi, mida pole veel commit'itud; miinusega read on eemaldatud, plussiga lisatud. Sama näitab VS Code, kui Source Control vaates failile klõpsata. Kuidas muudatusest loobuda: git restore koos failinimega viib faili tagasi viimase commit'i seisu. See on ainus käsk täna, mis on ohtlik: commit'imata muudatused kaovad jäädavalt ja neid ei saa tagasi. Sellepärast vaadatakse enne alati git diff väljund üle. VS Code'is on sama asi nool „Discard Changes” faili juures. Kui vale muudatus on juba commit'itud ja push'itud, ei muudeta ajalugu, sest teised on selle juba alla tõmmanud. Selle asemel tehakse uus commit, mis vea parandab; selleks on ka käsk git revert, mis loob automaatselt vastupidise commit'i. Harjutus on proovifailiga: muuda, vaata diff'i, võta tagasi, kontrolli git status'ega, et töökaust on puhas. -->

---

## 9. Kodutöö: `v0.3.0 – Kvaliteedi- ja riskiplaan`

Tiimi repos:

- kvaliteedinõuded: 3–4 omadust tiimi lugudest, igaüks mõõdetava kontrolltingimusena
- testjuhtumid: tiimi ühine seminarist ja igaühe üks oma loo kohta
- riskikaart: andmeallika risk ja vähemalt 5 muud; eeldused eraldi
- backlog: 2–3 toote Issue'd ja kolm „Selgita oma otsust” lünka, kõigil hinnang
- `decisions/004-kvaliteet-ja-riskid.md` ja `releases/v0.3.0.md`

Iga õppija: Issue, PR, teise töö ülevaatus, iseseisev silumisharjutus ja refleksioon `reflections/eesnimi-perenimi-v0.3.0.md` oma `SJTA` repos.

[Kodutöö 4 juhend](homework.md)

<!-- Kõik kodutöö osad on täna seminaris alustatud: kvaliteedinõuded sammust 3, testjuhtum sammust 4, riskikaart sammust 6, backlog sammust 7. Kodutöö laiendab seminari näidise tiimi kõigi lugude peale. Otsus 004 seob need kokku: see sisaldab või viitab kvaliteedinõuetele ja riskikaardile ning nimetab kompromissi ja varasema otsuse muutuse. Release notes teeb sama, mida v0.2.0 puhul, ja lisaks võrdleb hinnangut tegeliku ajaga Projectsi väljadest. Iga õppija panus on jälgitav tema Issue'i, PR-i ja ülevaatuse kaudu; see on sama töövoog kui eelmistes kodutöödes. Uus on iseseisev silumisharjutus, mille juhend on konspektis, ja igaühe oma testjuhtum. Refleksioon läheb enda SJTA reposse kausta reflections väikese tähega ja faililaiendiga .md; mõnel oli eelmine kord fail mujal või teise nimega. Arvestuslik maht on umbes 8 tundi õppija kohta ja kodutöö juhendis on see tundideks jagatud. -->

---

## Reeglid kodutöös 4

- **Merge:** PR-i ühendab keegi teine kui autor. Ülevaataja küsimusele vastatakse enne ühendamist.
- **Aeg:** hinnang Issue'i loomisel, tegelik aeg sulgemisel. Release notes võrdleb summasid.
- **Release manager** läbib kontrollnimekirja enne `v0.3.0` avaldamist.
- **Esitamine:** kodutöö Issue kommentaaris täislingid, mitte `#54`. Kuju `TLUHK-RIF26/tiim-XX-tunniplaan#54` toimib.

<!-- Merge-reegel teeb ülevaatuse päriseks. Kui autor ühendab oma PR-i ise, on ülevaatus formaalsus ja küsimusele ei pea vastama. Kui ühendab keegi teine, peab ta enne lugema ja küsimusele peab olema vastatud. Kodutöös 3 ühendas mõnes tiimis peaaegu kõik PR-id autor ise. Aja reegel on sama, mis sammus 1: hinnang loomisel, tegelik aeg sulgemisel, ühik tund. Release notes'i võrdlus tuleb siis Projectsi tabelivaatest kohe välja. Release manager vastutab, et avaldatud tervik peab; tema kontrollnimekiri on sama, mille tiim täna v0.2.0 peal läbi tegi. Esitamise reegel on tehniline, aga oluline: kui isiklikus SJTA repos kirjutada #54, seob GitHub selle sama repo Issue'ga number 54, mitte tiimi repo PR-iga. Toimib täis-URL või kuju organisatsioon/repo#number. -->

---

## Tuleviku (mis on juba käes) küsimused

- Millist tänase teema tööd võiks teha AI, kuidas tulemust kontrolliksime ja kes vastutaks?  
- Kui sa kasutaks vaid ai-d, kuidas sa selle probleemi lahendaks?

<!-- AI oskab tänastest asjadest päris palju: pakkuda riskikategooriaid, mida tiim ei märganud; kirjutada kontrolltingimusest testjuhtumi mustandi; teha koodile esimese ülevaatuse ja järjestada leiud. Küsimus ei ole, kas AI võib, vaid kuidas tulemust kontrollitakse ja kes vastutab. Riskiloend, mille AI pakub, on üldine; tiim peab eemaldama ebaolulise ja põhjendama, miks allesjäänud risk puudutab just nende projekti. Testjuhtum, mille AI kirjutab, tuleb proovida päriselt läbi. Ülevaatus, mille AI teeb, ei asenda inimese kinnitust: koodi kirjutanud agent ei saa enda tööd heaks kiita. Vastutus jääb rollile, mitte tööriistale. Kodutöös hinnatakse AI puhul kasutamise eesmärki ja väljundi kontrollimist, mitte genereeritud teksti mahtu. -->

---

## Tänased mõisted eksami testiks

kvaliteediomadus ehk mittefunktsionaalne nõue · testjuhtum · risk, eeldus ja maandus · WIP-piirang · blokeerija · `git log`, `git diff`, `git restore`

Kodutöös: viga, silumine ja koodi ülevaatus.

Test eeldab seletust oma sõnadega ja oma projekti näidet.

<!-- Eksami mõistete test on lühike ja individuaalne. Selles on ainult mõisted, mida on seminarides või kodutöödes päriselt käsitletud; tänased on sellel slaidil. Test ei eelda pähe õppimist ega definitsioone. See küsib sama, mida täna kleepsuharjutus: mis mõiste on oma sõnadega ja mida see teie projektis tähendas. Kes on seminarides ja kodutöödes kaasa töötanud, saab sellega hakkama. Viga, silumine ja koodi ülevaatus kuuluvad testi, sest kodutöö iseseisev harjutus käsitleb neid. -->
