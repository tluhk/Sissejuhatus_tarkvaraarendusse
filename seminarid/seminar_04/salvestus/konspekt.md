<!-- loengud:konspekt osad=1,2 (automaatne; kui muudad käsitsi, kustuta see rida – siis tööriist seda üle ei kirjuta) -->
# Konspekt: Seminar 4: kvaliteet, riskid ja vastutus

> Automaatne kokkuvõte seminari salvestusest (kõnetuvastus + keelemudel). Võib sisaldada ebatäpsusi – täpse sõnastuse leiad transkriptsioonist.

Seminari keskne küsimus oli, kuidas teada, et kavandatud lahendus on piisavalt hea ja vastutustundlik. Esimese tunni võttis kodutöö 3 tagasiside: tahvli kasutamine, ajaarvestus, issue'de päritolu, koodi ülevaatus ja lingid. Seejärel tegid tiimid harjutuse „Selgita oma otsust“. Kõigil tiimidel tuli välja sama kontrollimata eeldus: andmeallikas on teadmata ja tellijaga pole keegi rääkinud. Teine pool oli loeng kvaliteedist, testimisest, koodi ülevaatusest, riskidest ja kolmandatest osapooltest ning lõpus näidati Giti käske. Plaani loengu- ja demoosa jõuti läbi. Kvaliteedinõuete, testjuhtumi ja riskikaardi harjutusi seminaris ei tehtud, need on kodutöös 4.

## Kodutöö 3 tagasiside: automaatne hindamine ja AI kasutamine [▶ 1. osa 1:17](https://youtu.be/vHoLU588c7g?t=77)

Kodutööde sisuline osa oli üldiselt hea. Kasutajalood olid kirjas ja segasevõitu ülesandega saadi hakkama. Õppejõud vaatab töid osaliselt automaatselt üle, aga loeb need ka ise läbi. Automaatkontroll võib aga olla liiga punktuaalne ja sõnastada märkused karmimalt, kui asi väärib. **Kui tundub, et hinnang on ülekohtune või midagi on valesti loetud, kirjutage sellest kohe kommentaar.** Reeglid on selleks, et tööd hõlbustada. Kui need hakkavad tööd segama, on midagi valesti. Oluline on, et põhimõttest on aru saadud, isegi kui see on kirja pandud teiste sõnadega.

AI kasutamine oli lubatud. Eeldus on aga, et saate ise aru, mis kirja läks. AI toodab väga palju teksti ja seda on raske lugeda. Seepärast pange AI-le piirangud: ta peab rääkima asjast ja nii, et te sellest aru saate. Kui tulemusest ise aru ei saa, on asi halvasti.

### Miks tarkvaraarendus on endiselt tiimitöö [▶ 1. osa 5:44](https://youtu.be/vHoLU588c7g?t=344)

Väikese rakenduse võib üksi ja AI abiga valmis teha. Tellimustöös tekivad aga nõuded, mida AI võib küll lahendada, aga mis ei sobi. AI tugineb treeningandmetele, mis sobivad umbes 80% juhtudest, uue funktsionaalsuse puhul aga mitte. Siis tuleb otsustada koos, sest üks inimene ei saa seda teha.

Õppejõud tõi näite oma teisest tööst. Ühes AI-projektis lasti alguses ka analüüs ja otsustamine AI-l teha. Hiljem tekkis jälle suurem vajadus inimeste otsuste järele, sest tiimis olid erinevad arvamused. AI võib pakkuda variante, aga valiku teeb inimene. Seda osa AI teie eest ei tee: ühise aja leidmine, koos otsustamine, üksteisest arusaamine ja vastutuse jagamine.

## Tahvel, ajaarvestus ja issue'de väljad [▶ 1. osa 8:07](https://youtu.be/vHoLU588c7g?t=487)

Tööviisi valik (Kanban või Scrum) oli hästi põhjendatud, aga mitmel tiimil polnud seda tegelikult kasutusele võetud. **Kanbani puhul peab tahvel töö ajal liikuma.** Kaardid liiguvad veergude vahel ja iga kodutöö töö peaks järgmise korra alguseks olema veerus „Done“. Backlog'is võivad olla tulevased tööd ja „In progress“ veerus see, mida juba tehakse. Kui tahvlit ei peeta, siis Kanbanit tegelikult pole: te lihtsalt teete midagi ja see pole kuskil kirjas. Kanban on hea viis anda projektist ülevaade ja seepärast on see ka teiste tööviiside juures sageli vaikimisi kasutusel.

Tiim, kes valis **Scrumi**, peaks üle vaatama, mida Scrum tähendab, ja selle lühidalt kirja panema. Scrumil on kindlad reeglid ja neid tuleb järgida.

### Miks aega logida [▶ 1. osa 11:40](https://youtu.be/vHoLU588c7g?t=700)

Üks tiim oli lisanud issue'dele hinnangu ning algus- ja lõppkuupäeva. Järgmises kodutöös muutub see kohustuslikuks. Aega jälgitakse kahel põhjusel:

1. **Ajahinnang** (*estimate*): iga pileti hinnangutest summeerub projekti ajakava. Selle põhjal saab öelda, millal julgeb projekti valmimist lubada.
2. **Tegelik ajakulu**: selle jaoks lisage eraldi väli (juhendis on kirjas, kuidas). Hinnangut ja tegelikku aega võrreldes saab hinnata sarnaste projektide mahtu. See on hea alus järgmisele hinnapakkumisele, sest peamine kulu on inimtöö.

Hinnangu täpsust ei hinnata. Päris arenduses ei oska ka kogenud inimesed alati öelda, kui kaua miski aega võtab. Mõnes organisatsioonis hinnatakse puhta aja asemel töö kaalukust. Siin kasutame aega.

### Suurus, prioriteet, tüüp ja sildid [▶ 1. osa 15:15](https://youtu.be/vHoLU588c7g?t=915)

GitHubi projekti saab ise kujundada ning väljad ja sildid on organisatsiooni kokkulepe. Jiras ja ClickUpis on need lahendatud veidi teisiti.

- **Suurus** näitab hinnangulist töö raskust ja aitab otsustada, millal tööga alustada.
- **Prioriteet** näitab, mida teha enne. Eriti olulised on **blokeerijad**: issue'd, mille taga ootab mitu teist piletit. Need tasub kiiremini ära teha.
- **Tüüp** eristab vea parandust (*bug*), uut funktsionaalsust (*feature*) ja tavalist ülesannet. Viga on sageli väike ja kiiresti parandatav, aga oluline. Feature on suurem arendus, mille puhul tormata pole vaja.
- **Sildid** (*labels*) aitavad töid kategoriseerida, näiteks eristada dokumentatsiooni ülesandeid. Nii saab üks arendaja võtta ette teatud tüüpi tööd ja jälgida, kuidas nendega on.

### Kogemus ajahindamisega [▶ 1. osa 21:48](https://youtu.be/vHoLU588c7g?t=1308)

Üks tiim kirjeldas, et aega oli raske hinnata ja tegeliku aja arvestamisel jäi osa tööd (näiteks parandused pärast tagasisidet) välja. Õppejõu sõnul tähendabki see, et tunnetus on tekkinud: ajaarvestus on keerulisem, kui tundub.

Õppejõud kasutab ise taimeriga ajaarvestussüsteemi, kus aeg salvestub projektide kaupa. Sobib ka telefoni kell või mõni muu vahend. Oluline on, et see võtaks võimalikult vähe vaeva. Teine nipp on lasta päeva lõpus AI-l GitHubi ja suhtlustarkvara (Discord, tööl tavaliselt Slack) jälgede põhjal kokku võtta, kui palju aega tegelikult kulus.

Õppejõud soovitas aega mõõta ka iseseisvate proovitööde puhul. Kui hakkavad tulema päris kliendid ja küsitakse, palju töö maksab, pole ilma ajaloota millegi põhjal hinda pakkuda. See on ettevõtte alustamisel üks keerulisemaid asju. Andmete põhjal teate vähemalt, kui palju te omahinnast allapoole lähete.

## Backlog tuleb tootest, mitte kodutöö nõuetest [▶ 1. osa 26:25](https://youtu.be/vHoLU588c7g?t=1585)

Ühes töös olid issue'd sõnastatud kodutöö nõuetena. Me ei tee kodutööd, vaid lahendame probleemi toote loomise kaudu. Seega peavad issue'd tulema toote kasutajalugudest. Kasutajalugu muudetakse piletiks, mis tuleb lahendada, ja selle alla tulevad vajadusel alamülesanded.

## Koodi ülevaatus, mergekonfliktid ja lingid [▶ 1. osa 27:30](https://youtu.be/vHoLU588c7g?t=1650)

**Ülevaatuste** (*review*) puhul harjutage sisulise tagasiside andmist. Kodutööd on praegu nii lihtsad, et midagi peale „korras“ võib olla raske öelda. Siiski leiab igast tööst midagi, mida võiks muuta.

**Mergekonflikti** lahendamise vaates on mõlema poole kattuvad muudatused näidatud noolestike vahel. Ebavajalik tuleb kustutada või kogu lõik üle kirjutada. Mõnes tiimis lahendas keegi konflikti teise eest. Parem on näidata, kuidas seda tehakse, sest siis on asjast rohkem kasu.

Sellest tuleb ka õppetund **väikeste commit'ide** kohta. Kui teete korraga suure muudatuse, mis hõlmab palju parandusi, ja tekib konflikt kaasarendaja tööga, tuleb otsida väga palju kohti.

### Suhtelised ja täislingid [▶ 1. osa 30:51](https://youtu.be/vHoLU588c7g?t=1851)

Automaatsed ja suhtelised lingid töötavad ainult samas repos, sest need näitavad asukohta selles repos või kaustas, kus parasjagu olete. Kui viitate tiimi repost isiklikule repole või vastupidi, on vaja **täislinki**. Kuvatav tekst võib olla lühike, aga selle taga peab olema päris link. Õppejõud ei lugenud seda tõsiseks veaks, sest seda ei olnud veel õpetatud.

Õppejõud selgitas ka, et kodutöö juhendid tehakse kursuse repos ja kopeeritakse sealt kodutöö malli. Linke ei muudeta, sest neid on liiga palju. Kui tahate lingitud materjale kasutada, avage need kursuse repost, mitte enda tehtud kodutöö koopiast.

### AI ja lõpueksam [▶ 1. osa 33:19](https://youtu.be/vHoLU588c7g?t=1999)

Selles seminaris on AI kasutamine lubatud. Lõpueksam koosneb aga grupitöö esitlusest ja väikesest mõistete testist, kus AI-d kasutada ei tohi. Üldmõisteid peab teadma, et saaksite aru, mida AI teile vastab.

## Harjutus: „Selgita oma otsust“ [▶ 1. osa 34:26](https://youtu.be/vHoLU588c7g?t=2066)

Tiimid said umbes 10 minutit, et valmistada ette vastused kolmele küsimusele ja need siis lühidalt ette kanda:

1. Mis probleemi te lahendate ja kellele?
2. Millise suuna valisite, mis oli alternatiiv ja miks valisite just selle?
3. Mis on teie suurim **kontrollimata eeldus**? Ehk mida tiim peab tõeks ja millele lahendus toetub, aga mida keegi pole tegelikult üle vaadanud?

Harjutusel oli kaks eesmärki: tiimiliikmed saavad ühiselt üle vaadata, mida nad tegid, ja teised tiimid näevad, kuidas samale ülesandele läheneti. Vastused tuli lühidalt kirja panna tiimi repos, näiteks tänase kodutöö kokkuvõtte lõppu märkusega, et see on seminari töö [▶ 1. osa 45:51](https://youtu.be/vHoLU588c7g?t=2751).

### Mis esitlustest välja tuli [▶ 1. osa 53:00](https://youtu.be/vHoLU588c7g?t=3180)

Kõik tiimid tegelesid kooli tunniplaani probleemiga, aga eri nurga alt:

- **Olemasoleva süsteemi täiustamine** uue asemel. Kontrollimata eeldus: tiim ei tea, mis toimub back-end'is. Võib selguda, et vana süsteem on nii kehv, et uue tegemine on kiirem. Õppejõud nimetas seda väga heaks leiuks. Kui hinnapakkumine on juba tehtud ja siis selgub, et vanal süsteemil on piirangud, võib juhtuda, et lubatut ei saagi teha.
- **Lähinädalate tundide parem ülevaade.** Õppejõud küsis, kas tiim teab, kellega selles projektis rääkida. Selgus, et tellijaga (siin õppejõuga) ei olnud keegi rääkinud. Päris projektis peab see tehtud olema. Võite selle ka ausalt kirja panna: me ei tea, mida tellija tahab ega teab, ja me ei tea süsteemi piiranguid ega võimalusi.
- **Automaatsed teavitused tunniplaani muudatustest.** Alternatiiv oli näidata muudatusi tunniplaanis endas, kuid siis peab tudeng ikka ise igapäevaselt vaatamas käima. Õppejõu sõnul tuleb mõlema variandi mõju läbi mõelda või testida ja dokumenteerida, mis juhtub ühel või teisel juhul.
- **Kalendrivaade** tabelivaate täiustamise asemel, et vähendada kerimist. Kontrollimata eeldus: kas kasutajad üldse eelistavad kalendrit või on harjunud tabeliga. Lahendus on küsitlus või kasutajatestid, ehk eeltöö.
- **Isiklik tunniplaan**, mis koondab rühma ja valikained. Kontrollimata eeldus: kas andmed on kättesaadavad ja milline on süsteemi back-end. See langes kokku esimese tiimiga.
- **Eraldi ülevaade olemasoleva tunniplaani andmete põhjal.** Olemasoleva süsteemi muutmine eeldaks administraatori õigusi. Üks tiimiliige oli juba teinud lehe, mis saab andmed kätte. Õppejõud küsis: kuidas tagate, et andmevoog jätkub? Näiteks võib kooli juhtkond otsustada, et vana süsteemi pole enam vaja, ja selle kinni panna. Siis lõpeb ka andmevoog. See ongi kontrollimata eeldus: eeldatakse, et miski toimib, aga ei teata, kuidas.

Õppejõu kokkuvõte [▶ 1. osa 1:11:33](https://youtu.be/vHoLU588c7g?t=4293): hea, et kõigil tuli midagi välja. Kui kõik oleks juba põhjalikult lahendatud, oleks harjutus luhta läinud. Väikese vaevaga ilmnes, mida me eeldame, kuigi tegelikult ei tea. Õppejõud möönis, et sõna „kodutöö“ ja ajapiirang panevad tegutsema teisiti kui päris projekt ega soodusta laia vaadet. Just seepärast on kasulik selline punkt korraks läbi teha.

## Kus me kursusel oleme ja mida see seminar küsib [▶ 1. osa 1:12:46](https://youtu.be/vHoLU588c7g?t=4366)

Harjutus juhatas sisse riskide teema: mis juhtub, kui need eeldused ei pea paika, näiteks kui andmevoog järsku suletakse? Projekt peab olema mitmest küljest läbi mõeldud. Alguses ei tule kõigele lihtsalt mõelda. Tiim aitab, sest seal on rohkem erinevaid kogemusi.

Seni on leitud probleem, uuritud, milles see seisneb, ja kavandatud lahendus. Nüüd tegeleme sellega, et toode oleks kvaliteetne ja valmis ootamatusteks. Järgmine seminar räägib kasutuselevõtust, tagasisidest ja hooldusest.

Kui versioon 2 kirjeldas, **mida** süsteem teeb, siis versioon 3 vastab küsimusele, **kuidas me teame, et see on piisavalt hea**. Õppejõud mainis, et rollivahetuses võiks seekord mängu tuua testija rolli, aga jättis selle veel lahtiseks.

## Töötamine ei võrdu kvaliteediga [▶ 1. osa 1:20:28](https://youtu.be/vHoLU588c7g?t=4828)

Kas töötav tarkvara on kvaliteetne? Selle kindlakstegemiseks on testimine. Näide: tunniplaani süsteem näitab iga rühma tunniplaani ja kõik kasutajalood on täidetud. Telefonis tuleb aga rühm iga kord uuesti valida ja mobiilivõrgus laeb leht kümme sekundit. Tulemus: kasutajalood on täidetud, aga keegi ei kasuta süsteemi, sest seda pole võimalik mõistlikult kasutada.

Põhjusi on mitu: mobiilivaade jäi lahendamata või lahendati halvasti, mõne seadmega ei arvestatud jne. Testija ülesanne on kontrollida näiteks kiirust ja seda, kuidas süsteem käitub eri ekraanilaiustel. Süsteem võib olla aeglane, ebaturvaline või raskesti kasutatav. Kui sisestatud andmed lekivad, ei kasuta inimene seda enam kunagi. Kui lahendus on nii kallis, et koolil pole selleks raha, ei saa seda samuti kasutada.

### Funktsionaalne ja mittefunktsionaalne nõue [▶ 1. osa 1:22:55](https://youtu.be/vHoLU588c7g?t=4975)

- **Funktsionaalne nõue**: mida süsteem teeb.
- **Mittefunktsionaalne nõue** ehk **kvaliteediomadus**: kui hästi ja millistel tingimustel süsteem seda teeb.

Kvaliteediomadused on näiteks kasutatavus, jõudlus, töökindlus, andmete õigsus (näidatakse kindlasti sinu tunniplaani, mitte teise eriala oma) ja hooldatavus.

### Ebamäärasest mõõdetavaks [▶ 1. osa 1:24:11](https://youtu.be/vHoLU588c7g?t=5051)

„Süsteem peab töötama kiiresti“ või „mugavalt“ ei ütle midagi. Mõõdetav on näiteks see, et vaade laeb kolme sekundi jooksul või et lahendus vastab konkreetsetele UX-reeglitele. Mugavus on eri inimestele erinev ja subjektiivne. Kasutatavuse ja kasutajamugavuse jaoks on aga olemas konkreetsed reeglid, mida õpite teistes ainetes.

Üks üliõpilane märkis, et kiirus sõltub olukorrast. Õppejõud nõustus, aga kui sõltuvuse parameetreid pole kirja pandud, pole sellega midagi peale hakata. Kodutöös 3 oli palju selliseid sõnastusi nagu „kiirelt“, „mugavalt“ või „ilma liigse ajakuluta“. Õppejõu sõnul polnud see etteheide, vaid tänase seminari mõte.

**Nõue peab olema selline, et testija saab selle põhjal tabelisse linnukese panna: jah, on täidetud.** Kui tulemus sõltub sellest, milline tudeng või testija juhuslikult satub, pole nõudega võimalik edasi minna.

Näide ebamäärasest ja mõõdetavast nõudest:

- Nõrk: „Tudeng leiab järgmise loengu kiiresti.“
- Mõõdetav: „Tudeng leiab telefonis oma rühma järgmise loengu aja ja ruumi kuni kümne sekundiga ilma rühma uuesti valimata.“

Kvaliteedinõue on seega kvaliteediomadus koos mõõdetava piiriga. Piiri ei pakuta puusalt. Õppejõud kirjeldas olukorda, kus koosolekul arutatakse, mis on „kiire“, ja tiimis see, kes tahab kõigile meeldida, ütleb mingi numbri ning kõik on nõus. Nii ei tohi. Piir peab tulema eeluuringust (näiteks küsite sihtrühmalt, mis on nende jaoks kiire), uurimustest või tehnilistest parameetritest [▶ 1. osa 1:28:49](https://youtu.be/vHoLU588c7g?t=5329).

### Mida saab kontrollida [▶ 2. osa 0:02](https://youtu.be/mxerCtuT7-c?t=2)

Mida ei saa kontrollida, seda ei saa nõudeks seada, sest seda pole võimalik hinnata. Muu on pigem kliendi meeleolu või soovidega arvestamine. Tehnilisi asju on lihtsam kontrollida. Ka „vastab turvanõuetele“ ei ole ebamäärane: turvalisuse kohta on kindlad sertifikaadid ja parameetrid. Suur osa tehnilistest testidest tehakse automaatselt ja nii oli see juba enne AI-d. Automaatselt saab teha ka suure osa disainitestidest, näiteks kontrollida, kas elemendid mahuvad mobiilivaatesse.

## Kvaliteedi vaatenurgad ja kompromiss [▶ 2. osa 2:24](https://youtu.be/mxerCtuT7-c?t=144)

Kvaliteedi tähendus sõltub sellest, kes küsib:

- **Kasutaja**: kas saan oma eesmärgi turvaliselt ja arusaadavalt täidetud? Kas leian oma loengu ja kas keegi teine ei näe minu andmeid?
- **Organisatsioon** (kool): kas tulemus loob väärtust ja vastab kohustustele? Kooli jaoks pole oluline lihtsalt see, mida tudengid tahavad, vaid see, et nad jõuaksid loengusse ja lõpetaksid kooli.
- **Arendaja**: kas süsteemi saab mõista ja muuta? Mis juhtub, kui back-end vahetatakse või front-end viiakse mujale? Kas süsteem kukub kokku, kui mõnda muutujat muuta?
- **Käitaja**, ehk see, kes süsteemi töös hoiab: kas ta saab rikete korral teavituse ja kas ta saab teada, kui midagi ära kukub?
- **Ühiskond**: kas süsteem on kellelegi kahjulik ja kas see sulgeb kellelegi ligipääsu? Riigi jaoks on oluline, et ka erivajadustega inimesed, näiteks vaegnägijad, pääseksid õppima.

Õppejõud tõi analoogia: võite teha lõppkasutajale suurepärase lahenduse, mis näeb välja nagu tipptasemel arvutimäng, kuid käitajale on see õudusunenägu, sest tal pole ressurssi seda käigus hoida [▶ 2. osa 5:53](https://youtu.be/mxerCtuT7-c?t=353). Kui arendate ühte osapoolt silmas pidades ja eeldate, et „tänapäeval on kõigil kiire internet“, võib see risk realiseeruda. Mõni üliõpilane elab kehva ühendusega kohas ja tal oleks vaja lihtsamat lahendust, näiteks API-t, mille kaudu andmed kätte saab.

### Kompromiss peab olema kokkulepe [▶ 2. osa 8:02](https://youtu.be/mxerCtuT7-c?t=482)

Kõigi osapoolte maksimumsoove ei saa korraga täita. Käitaja eelistaks ehk süsteemi, mis ei tee midagi ega anna seetõttu ka vigu, aga siis jääb kasutaja vajadus täitmata. Turvalisus muudab asja aeglasemaks ja ebamugavamaks ning võib tõsta hinda. Kompromiss on vältimatu ja see pole halb. See ei tohi aga tekkida kogemata. See peab olema teadlik kokkulepe.

Näide: tiim otsustab, et vaade ei nõua sisselogimist. Ta loobub isiklikest valikutest, aga võidab lihtsuse ja privaatsuse. Kui see on otsuste logis koos põhjendusega kirjas, on kõik korras. Kodutöös peaks üks selline kompromiss kirja saama.

### Turvalisus, privaatsus ja ligipääsetavus [▶ 2. osa 10:16](https://youtu.be/mxerCtuT7-c?t=616)

Disaini juures tuleb osata küsida õigeid küsimusi. Ei tasu kõike pimesi turvaliseks muuta, aga ka mitte vastupidi. Küsige:

- milliseid andmeid on kellelgi päriselt vaja;
- kui kaua on ligipääsu vaja;
- mis juhtub lekke korral.

Sellest sõltub, kui keeruliselt kaitse lahendada. Kui lekivad andmed, mida kellelgi vaja pole, on see üks olukord. Kui lekivad andmed, millega saab kedagi välja pressida, on see hoopis teine.

**Ligipääsetavuse** puhul küsige: kas süsteem töötab ekraanilugejaga, kas saab liikuda Tab-klahviga, mis juhtub aeglase võrgu või väikese ekraani korral? Kirjandeid pole vaja kirjutada, siin kehtib sama hoiatus AI kohta: asi peab olema konkreetne ja kergesti hallatav.

Kooli veebilehe puhul tuleb arvestada ka seadusandlusega. Eraettevõtte lehe puhul on nõuded vabamad, avalik-õigusliku asutuse puhul aga kehtivad kindlad tingimused, mis tuleb üle kontrollida.

## Testimine ja testjuhtum [▶ 2. osa 13:06](https://youtu.be/mxerCtuT7-c?t=786)

**Testimine** võrdleb oodatud tulemust tegelikuga kindlates tingimustes. Testjuhtum kirjeldab samme (mine sinna, ava see, vajuta OK) ja seda, mida jälgitakse. Veebis tehakse see eri tingimustes, näiteks nii lauaarvutis kui ka mobiilis. Kõik ei pea igal ekraanil nähtav olema, kuid peab olema kirjeldatud, mis peab nähtav olema. Ülesanne peab olema sooritatav, aga kitsal ekraanil ei pruugi kõik elemendid vajalikud olla.

Näide: ava tunniplaan, vali rühm, sulge menüü, keri alla. Kui rühma nimi on kogu aeg nähtav ilma menüüd avamata, on test läbitud.

Testida saab ka siis, kui rakendust veel pole: prototüübi või **wireframe'ide** peal. UX-teste on tehtud lihtsate valikutega enne arendust, et mitte raisata raha arendusele. Õppejõu sõnul on koodi kirjutamine nüüd nii odavaks läinud, et prototüüp võib olla peaaegu sama, mis lõpplahendus, ja seda saab juba päriselt testida.

Kursusel testite oma kirjeldusi: mängite kasutajalood läbi nagu testi („lähen sinna, liigun sinna“), et näha, kas need töötavad. See on osaliselt mäng, aga aitab mõista, mida testjuhtum tähendab. Testida saab ka praegust tunniplaani lahendust, mida osaliselt juba tegite, kui oma probleemi otsisite.

Testjuhtumid peavad katma ka olukorrad, kus süsteem võib vigu teha: katkenud võrk, tühi sisend, andmed ei lae.

### Kes testib [▶ 2. osa 17:51](https://youtu.be/mxerCtuT7-c?t=1071)

Paljud testjuhtumid põhinevad kogemusel. Seepärast on testijad sageli spetsialistid, kes teavad, kus asjad tavaliselt katki lähevad. Valmis testiülesandeid võib läbi mängida igaüks. Suur osa testidest tehakse automaatselt, sest inimtöö on kallis. Siiski on olukordi, kus ei AI ega muud automaattestid hakkama ei saa, ja lõpuks peab testima inimene, sest **vastutuse võtab inimene**. Kliendile ei saa öelda, et viga tegi masin.

## Arendamise etapp ja koodi ülevaatus [▶ 2. osa 18:54](https://youtu.be/mxerCtuT7-c?t=1134)

Enamik inimesi mõtleb arenduse all koodi kirjutamist, aga see on vaid üks osa. Arendamise etappi kuuluvad ka disain, arhitektuur ja tehnilised valikud, näiteks kuhu andmeid salvestada. Lisaks oma koodi kirjutamisele vaatab arendaja üle kaasarendajate töö.

Seepärast ei ole **PR-ide ülevaatus** tüütu kohustus, vaid osa tööst. Suhtuge sellesse sama tõsiselt kui oma töösse. „Korras“ või „hästi“ ei ole hea tagasiside. Lugege teise töö päriselt läbi. Juba see, kui märkate, et keegi tegi midagi teisiti kui teie, aitab teid edasi, ja kui ütlete seda talle, aitab see ka teda.

Kursusel koodi ei kirjutata, seda tehakse teistes ainetes. Suur osa kursusest on aga **Giti ja GitHubiga sõbraks saamine**. Ka näiliselt imelikud harjutused on koostöö harjutamine. Kirjeldage vigu tagasisides nii, et teine saab neid korrata ja neist aru saada.

### Arendaja roll AI ajastul [▶ 2. osa 22:21](https://youtu.be/mxerCtuT7-c?t=1341)

Õppejõu hinnangul jääb kitsa spetsialiseerumisega arendajaid vähemaks ja olulisemaks muutub laiem oskus juhtida kogu tarkvaraprotsessi: mõista koodi, arhitektuuri, disaini ja projektijuhtimist. Tiimi on siiski veel vaja, sest kõik pole ühtviisi suhtlejad. Kuidas see edasi areneb, ei tea keegi. Üks kodutöö punkt palubki kirjeldada oma arvamust selle kohta.

Õppejõu kogemus praegusest AI-projektist: AI toodab sekunditega tohutus koguses materjali ja töö on palju kiiremaks läinud, aga keegi ei jaksa seda enam üle lugeda. Vastutus kliendi ees on siiski inimesel. Väikese rakenduse puhul pole see probleem. Suure müügiks mõeldud lahenduse puhul aga ei tea sa enam, mille eest vastutad: kood töötab, aga sa ei tea, miks töötab ja mis augud sinna jäid. Kui hakkad kõike üle kontrollima, tekib küsimus, miks sa seda kohe ise ei teinud.

## Vea silumine [▶ 2. osa 25:35](https://youtu.be/mxerCtuT7-c?t=1535)

Kui süsteem käitub teisiti, kui oodati, on kaks võimalust. Kui ootus oli vale, on viga nõudes. Kui ootus oli õige, on viga tõenäoliselt koodis. Viga võib olla ka andmetes: tunniplaan näitab vale ruumi mitte koodivea pärast, vaid sellepärast, et keegi sisestas andmed valesti.

**Silumise** (*debugging*) sammud:

1. korda viga ja taasta olukord;
2. dokumenteeri see;
3. kitsenda põhjust, kuni viga leitakse;
4. kontrolli oletusi, mitte ära tee midagi pimesi. Testkeskkonnas saab proovida ka hiljem uuesti;
5. lisa kontroll, et sama viga tagasi ei tuleks.

Tavaliselt pole see pikk protsess, aga keerulisemate vigade puhul võib olla.

### Hea ülevaatus [▶ 2. osa 27:57](https://youtu.be/mxerCtuT7-c?t=1677)

Koodi ülevaatus aitab vigu vähendada. Ülevaataja saab küsida, mis juhtub erijuhtudel, näiteks kui mõni väli on täitmata. Ta saab ka anda konkreetse kommentaari: see osa on täitmata või vale just sellel põhjusel. Ainult „see on vale“ ei ütle midagi.

Õppejõud korraldab ülevaatused meelega nii, et paariline vahetub kogu aeg. Siis ei vaata sõber sõbra tööd üle ja näete, kuidas teised teevad. Kes teeb midagi hästi, sellelt saab õppida.

AI-d võib kasutada esmase ülevaatajana, aga oma tööd peate ise tundma. AI pakub sageli üle: vajate väikest funktsionaalsust, AI aga keevitab kokku terve rakenduse. Kui soovitusest aru ei saa, ei pruugi seda vaja olla.

## Risk kui otsustamise vahend [▶ 2. osa 30:11](https://youtu.be/mxerCtuT7-c?t=1811)

Üksi ja vähese kogemusega ei tule kõigele mõelda. Tormatakse hurraaga peale ega teata, mis alt võib vedada. Tiimi eelis on see, et rohkem inimesi näeb asju eri nurga alt. AI aitab, eriti kui töövoog on seadistatud alati küsima „kas kontrollisid ka seda ja seda?“. Ka AI ise võib aga alt vedada. Kasvav risk on jätta kogu otsustamine AI-le ja hiljem avastada, et see tegi midagi valesti või et tema vaade oli meie oludes liiga kitsas (lahendus sobis Ameerikasse, aga mitte Eestisse).

**Riskide nimekiri on töövahend.** Agiilses arenduses saab seda kogu aeg täiendada. Riskid tulevad välja tellija ja sihtrühmaga rääkides ning oma kogemuse põhjal.

Tänane näide: eeldame, et tunniplaani andmed on olemas. See on väga inimlik eeldus, sest näeme andmeid oma silmaga. Aga kuidas need tegelikult tekivad? Võib-olla on töös uus süsteem, võib-olla neid ei tohi kasutada või pakub andmeteenust keegi teine. Maandus on lihtne: enne jätkamist kontrollime, kas andmeid tohib kasutada ja kas need on kättesaadavad. **Eeldused ja riskid tuleb kirja panna eraldi.**

### Riskikaart [▶ 2. osa 35:13](https://youtu.be/mxerCtuT7-c?t=2113)

Riskikaardi veerud:

- **mis võib juhtuda** (näiteks andmevoog lõpeb);
- **mõju**: kui tõsine see on. Selle järgi saab töid prioritiseerida ja otsustada, kas teadmata asjaga võib edasi minna või tuleb see enne lahendada;
- **tõenäosus**;
- **kuidas märkame**, et risk realiseerub;
- **maandus**: mida teha, et mõju oleks väiksem;
- **vastutaja**.

Skaala on iga tiimi või organisatsiooni enda otsus, aga madal, keskmine ja kõrge on täiesti piisav.

### Vastutaja on roll [▶ 2. osa 37:47](https://youtu.be/mxerCtuT7-c?t=2267)

Projektitöös peab alati keegi vastutama, muidu lähevad asjad käest. Vastutaja on pigem roll kui inimene: arhitekt, disainer jne. Inimene võib vahetuda, aga roll jääb. Üks inimene võib kanda mitut rolli. **Kui kõik vastutavad, ei vastuta keegi**, sest kõik arvavad, et keegi teine tegeleb asjaga.

## Lisaks plaanile

### Lugu: AI-projektijuht, kelle kanal vaigistati [▶ 2. osa 38:53](https://youtu.be/mxerCtuT7-c?t=2333)

Õppejõu ühes AI-projektis ei ole projektijuhti ja see osa kannatab. Esmalt tehti AI-projektijuht, kes postitas iga pileti Slacki. AI toodab aga nii kiiresti, et kanal ummistus ja kõik tiimiliikmed vaigistasid selle. Õppejõud nimetas seda tagantjärele halvaks ideeks.

Uus mõte on, et AI analüüsib tehtud ja tehtavat tööd ning postitab ainult siis, kui on midagi öelda. Näiteks teeb ta kord nädalas sprindi moodi kokkuvõtte ja annab teada, kui piletid seisavad või neil pole vastutajat. Õppejõud tunnistas ka, et AI osa projektis on väsitav, sest enam ei tea, kas suhtled inimesega või mitte. Seetõttu on näiteks reede õhtused tiimikohtumised muutunud jälle inimlikumaks ja huvitavamaks.

### Sõltuvus AI-st kui risk [▶ 2. osa 46:14](https://youtu.be/mxerCtuT7-c?t=2774)

Hiljuti oli suur Microsofti katkestus ja umbes samal ajal oli maas ka AI-teenus, mida õppejõud kasutab. Kuna töövood olid suures osas AI peale ehitatud, tekkis hetkeks tunne, et ei mäletagi enam, kuidas varem tehti. Katkestus kestis üle poole päeva ja algne ootus, et teenus tuleb kohe tagasi, ei täitunud.

Tarkvaraarenduse turul on viimase aasta jooksul toimunud tugev hinnalangus. Mõned pakkumised on 80–90% odavamad kui aasta tagasi ja pakkujate seas on nüüd ka firmasid, kes pole varem IT-ga tegelenud. See loob teile võimalusi, aga on ka risk: kui pakkumine eeldab, et AI teeb kõik ära, ja päev enne tähtaega on mudelid maas, ei saa tellimust täita.

Õppejõud küsis, kuidas seda riski maandada. Pärast naljakaid vastuseid jõuti selleni, et kõige kindlam maandus on osata tööd ka ise teha. Tähtaja nihutamine on küll võimalik, aga kogemus näitab, et üks-kaks päeva jääb alati puudu.

## Kolmandad osapooled ja litsentsid [▶ 2. osa 41:12](https://youtu.be/mxerCtuT7-c?t=2472)

Teie süsteem ei toetu ainult teie enda ressurssidele. Üliõpilased tõid tunniplaani näitel välja **pilveteenuse pakkujad**, kus asuvad tõenäoliselt server, andmebaas, API ja front-end. Ka võrguinfrastruktuur, mida mööda andmed liiguvad, kuulub kellelegi teisele.

**Litsentsid**: tarkvara peab alati olema litsentseeritud, isegi kui olete ise autor. Kui te pole autor, on asi veel keerulisem. Selgus, et litsentside teema oli varasemas kodutöös iseseisvaks tööks ja ei jäänud hästi meelde, seega tuleb see ilmselt uuesti ette võtta. Kolmandate osapoolte hulka kuuluvad ka andmeallikad.

### Cloudflare'i 2019. aasta katkestus [▶ 2. osa 45:00](https://youtu.be/mxerCtuT7-c?t=2700)

2019. aastal lisas Cloudflare oma tulemüürile reegli, milles oli vigane regulaaravaldis. Cloudflare'i teenuseid kasutatakse väga laialt ja muudatus levis sekunditega üle maailma. Õppejõud mäletas, et suur osa veebist oli selleks ajaks maas. Plaanis olnud arutelu küsimuste üle (kas põhjus oli ühes reas, millised kontrollid oleks mõju piiranud, kes vastutab) seminaris eraldi ei peetud.

## Riskianalüüs peab otsuseid muutma [▶ 2. osa 50:40](https://youtu.be/mxerCtuT7-c?t=3040)

**Kui riskikaart on valmis ja ükski varasem otsus ei muutu, olete selle tõenäoliselt teinud sellepärast, et kodutöö nõuab, mitte selleks, et riske ette näha.** Riskianalüüsi mõte on leida kohad, kus kavand ei pea. Riskiks on ka see, et keegi teine on sama asja juba teinud või konkurent pakub paremini.

Õppejõud kirjeldas protsessi kahe otsana. Kavandamisel kaardistatakse olukorrad, mis on näha. Riskianalüüs toob juurde puuduvad osad. Midagi jääb alati katmata ja ka ettenägematuteks olukordadeks peab valmis olema. Täiesti kindlat lahendust pole olemas, aga kui riskidega ei tegele, hakkavad nemad teiega tegelema, ja see on valusam.

### Vigadest õppimine ja muutuste logi [▶ 2. osa 53:17](https://youtu.be/mxerCtuT7-c?t=3197)

Õppejõud küsis: kas õpid rohkem siis, kui teed asju õigesti, või siis, kui teed valesti? Teada on, et vigadest õpitakse paremini, ja ka pedagoogika soovitab vigu teha. Koolisüsteemis tajutakse hindamist aga karistusena ja õpitakse vigu kartma, mis takistab õppimist. Õppejõud rõhutas, et ta ei süüdista selles kedagi.

Projektis tähendab see, et **otsuse muutmine ei ole läbikukkumine**. See näitab, et teil on uus info ja saate paremini otsustada. **Muutuste logi** peab näitama, miks muutus tekkis: ilmnes uus risk või tõendid muutsid arusaama probleemist. **Vanu otsuseid ei kirjutata üle, uus otsus viitab vanale.** Nii on näha otsustamise loogika ja välditakse olukorda, kus kord parandatud viga hiljem tagasi tuuakse, sest kellelgi pole ülevaadet. Eksamil tahab õppejõud kuulda vähemalt ühest muutunud otsusest.

Õppejõud tuletas meelde ka seda, et backlog tuleb toote vajadustest, mitte kodutöö ülesannetest. Te ei täida kodutööd, vaid loote toodet, millel on oma nõuded. Kui need on täidetud ja testitud, on tarkvara valmis [▶ 2. osa 57:25](https://youtu.be/mxerCtuT7-c?t=3445).

## WIP-piirang ja blokeerijad [▶ 2. osa 58:31](https://youtu.be/mxerCtuT7-c?t=3511)

Kursuse projektides on nii vähe issue'sid, et need mõisted ei tule hästi esile, aga päris töös on need olulised.

**WIP-piirang** (*work in progress*): tiim suudab teatud aja jooksul lahendada ainult kindla hulga ülesandeid. Kõike korraga tööle panna pole realistlik. Siin tuleb mängu ajahinnang. Näide: kodutööle on ette nähtud umbes kümme tundi inimese kohta, tiimis on neli inimest, aga piletite hinnangute summa on 50 tundi. Midagi on valesti. Võib-olla hindasite valesti, võib-olla andis õppejõud liiga mahuka kodutöö. Ülekoormus tähendab ebareaalseid ootusi ja lubadusi, mida tahvli põhjal ilmselgelt täita ei saa.

Õppejõud lubas lisapunkte tiimile, kes hindab töö ära ja ütleb põhjendatult, et rohkem ta võtta ei saa, sest see näitab, et protsessist on aru saadud. See on tähtsam kui üksiku pileti täitmine.

**Blokeerija**: õppejõud näitas, kuidas GitHubis luua silt `blocker` (Labels, New label). Sildi värviks sobib punane, sest see viitab ohule. Pileti juurde tasub kirjutada, mida see blokeerib, näiteks millised piletid ootavad selle järel. Kui ühe pileti taga ootab mitu teist, tõuseb selle prioriteet. Õppejõud märkis, et tema töökohas on blokeerijad lahendatud teisiti ja GitHubi võimalused tuleb tal veel üle kontrollida.

## Giti ajalugu ja tagasivõtmine: demo [▶ 2. osa 1:06:58](https://youtu.be/mxerCtuT7-c?t=4018)

Õppejõud näitas terminalis kursuse repo näitel:

- **`git log --oneline`** näitab commit'ide ajalugu, iga commit ühel real. Õppejõud näitas ka oma halbu commit-sõnumeid, nagu „muuda kolmanda seminari“, mis ei ütle sisuliselt midagi. Ta tunnistas, et kuna repot haldab ainult tema, lubab ta endale seda, mida üliõpilastele ei luba. Logist väljumiseks vajutage `q`.
- **`git diff`** näitab muudatusi, mis on tehtud, aga veel commit'imata. Siit on hästi näha, miks väikesed commit'id on paremad: hiigelsuurt muudatust on väga ebamugav lugeda.
- **`git restore <fail>`** taastab algse seisu ja kustutab commit'imata muudatused jäädavalt. Olge sellega ettevaatlik. Kooliprojektis on aga kasulik seda mitu korda proovida.

Seejärel näitas õppejõud VS Code'i **Source Control** vaadet, kus on graafiline commit'ide ajalugu. Seal saab vana commit'i välja võtta (*checkout*), et vaadata tolle aja seisu, teha sellest uue haru, lisada tag'i või võrrelda versioone. Terminali käskude harjutamine on kõige parem, aga VS Code'i graafiline liides on kiirem ja täiesti okei. Õppejõud loodab, et keegi ei kirjuta enam faile otse GitHubi veebis, kuigi mõnikord on see vajalik. GitHubi enda graafilist töölauarakendust ta ei soovita, sest see ajab segadusse.

## Kodutöö ja järgmised sammud [▶ 2. osa 1:13:49](https://youtu.be/mxerCtuT7-c?t=4429)

Kodutöö 4 (release `v0.3.0`) juhend on olemas. Seminaris tegemata jäänud harjutused tuleb teha seal:

- **Mõõdetavad kvaliteedinõuded.** Nõuded olid teil juba olemas, nüüd peavad need olema mõõdetavad. „Mugav“ või „ilus“ ei ole mõõdetav. Mugavus võib nõudena jääda, aga tuleb kirjeldada, kuidas seda mõõta. Piir ei tohi olla välja mõeldud: see peab tulema uuringutest, kasutajatestidest või muust põhjendatud allikast.
- **Testjuhtumid**: igaüks koostab vähemalt ühe ja osa tuleb välja mõelda koos.
- **Riskikaart**: umbes viis riski on hea, veidi vähem on ka okei, kaks on liiga vähe. Igal riskil peavad olema maandus, märkamise viis ja vastutaja.
- **Otsused**: vähemalt üks teadlik kompromiss ja otsus, mida risk muutis, otsuste logis koos viitega varasemale otsusele.
- Issue'dele **ajahinnang** ja eraldi väli **tegeliku aja** jaoks.
- Uuendatud backlog (toote vajadustest), sisuliselt üle vaadatud PR-id ja refleksioon. Refleksioonis võib kirjeldada ka oma arvamust selle kohta, kuhu arendaja roll liigub.
- Seminari harjutuse vastused lühidalt tiimi repos.

Õppejõud on korrastanud kursuse repot ja lisanud **handbook'i**, kus seminaride materjalid on konspekti kujul ja näidetega [▶ 2. osa 1:16:31](https://youtu.be/mxerCtuT7-c?t=4591). Peatükid 1–4 on tema sõnul juba korras (4. peatükk on selle seminari teemad: mõõdetav kvaliteet, testjuhtum, vea silumine, koodi ülevaatus, riskid). Peatükid 5–6 on veel mustandid. Järgmine kohtumine on ülejärgmisel nädalal. Õppejõud pakkus, et võib siis lühidalt näidata oma AI-põhist tööprotsessi.

## Plaan ja tegelikkus

**Mis jõuti:** kodutöö 3 tagasiside, harjutus „Selgita oma otsust“ koos kõigi tiimide esitlustega, loeng (funktsioon ja kvaliteediomadus, ebamäärasest mõõdetavaks, vaatenurgad ja kompromiss, testjuhtum, vea silumine, arendamise etapp ja koodi ülevaatus, risk ja eeldus, riskikaart, vastutaja, kolmandad osapooled, muutuste logi, WIP-piirang, blokeerija) ning Giti demo (`git log --oneline`, `git diff`, `git restore`, VS Code'i Source Control).

**Mis jäi tegemata või lükkus edasi:** kvaliteedinõuete, testjuhtumi ja riskikaardi harjutused jäid kodutöösse 4. Cloudflare'i juhtumit mainiti ainult lühidalt ja plaanis olnud kolme arutelu küsimust ei käsitletud. Turvalisus, privaatsus ja ligipääsetavus said põgusa ülevaate. Litsentsid tuleb ilmselt uuesti läbi võtta, sest varasem iseseisev töö ei jäänud meelde.

**Ajakasutus:** kodutöö tagasiside võttis umbes 35 minutit, ettevalmistus koos esitlustega umbes 40 minutit. Loeng algas alles esimese tunni lõpus ja jätkus teises pooles. Ka testija rolli lisamine rollivahetusse jäi lahtiseks.

**Mis üliõpilastel segaseks jäi:**
- Kanbani ja Scrumi valik oli põhjendatud, aga tahvlit ega Scrumi reegleid päriselt ei kasutatud.
- Issue'd sõnastati kodutöö nõuete, mitte toote vajaduste järgi.
- Teise reposse viidati suhteliste linkidega.
- Konflikte lahendati teise eest.
- Ülevaatused piirdusid sõnaga „korras“.
- Kvaliteedinõuded olid ebamäärased („kiirelt“, „mugavalt“) ja üks üliõpilane küsis, kas kiirus ei sõltu lihtsalt olukorrast.
- Ajahinnangu ja tegeliku aja eristamine oli keeruline.
- Kõik tiimid eeldasid, et andmed on kättesaadavad, ja keegi polnud tellijaga rääkinud.

**Õppetunnid järgmiseks korraks:**
- Harjutus „Selgita oma otsust“ toimis väga hästi ja tõi kontrollimata eeldused kiiresti esile. Seda tasub korrata ja kasutada sissejuhatusena riskide teemasse.
- Kodutöö tagasiside võiks olla lühem, et vähemalt üks harjutus (näiteks ebamäärase nõude muutmine mõõdetavaks) jõutaks teha seminaris.
- Tellijaga suhtlemine peaks olema nõutud juba varasemas etapis.
- Automaathindaja sõnastust tuleb pehmendada.
- Kodutööde linke tasub kontrollida, et need viitaksid kursuse reposse.
- Litsentside teema vajab seminaris eraldi aega.
- Ruumi tagaosas ja veebis osalejaid on raske kuulda, seega tuleks esitlejad kutsuda ette.
