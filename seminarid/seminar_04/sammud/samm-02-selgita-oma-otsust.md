# Seminar 4, samm 2: „Selgita oma otsust”

Kestus 25 minutit, arvutid kinni, välja arvatud üks kaardiarvuti tiimi kohta (vt „Teamsi kohandus”). Küsimused on jaotatud uute rollide järgi, mis lepiti kokku sammus 1.

Allikad: `understanding-XX.md` (diagnostilised küsimused ja head vastused), `ai-and-understanding.md`, `team-XX.md`.

## Miks

Kodutöö 3 põhjal sõnastas AI suure osa disainist, arhitektuurist, tööviisist ja release notes'ist. Kasutajalood ja tõendid on enamasti õppijate endi kirjutatud. Mida keerulisem mõiste, seda suurem on vahe ladusa dokumendi ja õppija enda seletuse vahel. Lihtsamad mõisted on omandatud: vajadus ja lahendus, tõend, merge-konflikt. Neid mõisteid ei seleta keegi oma sõnadega:
- WIP-piirang;
- hinnang ja tegelik aeg;
- arhitektuuri vastutused;
- risk ja kontrollimata eeldus;
- kompromiss.

Harjutus näitab enne `v0.3.0` tegemist, millest tiim päriselt aru sai. Lisaks on see eksami esitluse ja testi proov.

## Mida õppijatele öelda

„AI kasutamine on lubatud ja jääb lubatuks. Järgmises etapis peate oma otsuseid ise seletama, eksamil samuti. See harjutus näitab, kas oskate. Punkte see ei anna. Kui midagi seletada ei oska, on see leid, mitte viga: see läheb teie backlog'i.”

Ära ütle, et küsimused on tehtud AI-analüüsi põhjal. Ära nimeta, kelle tekst oli AI sõnastatud.

## Ettevalmistus

- Iga tiimi kohta Issue'i mustand „Selgita oma otsust”. Kehas on tiimi `003` kontseptsiooni kokkuvõte (teekond, lood, valitud suund, arhitektuuri osad) ja tiimi rollivahetuse küsimused (allpool), iga küsimuse juures vastaja nimi. Kokkuvõte on ainus mälutugi, repo faile ei avata.
- Postita Issue'd tiimide repodesse alles sammu 2 alguses, sest küsimused on tiimispetsiifilised.
- „Mis siis, kui” muutus (allpool) on valmis kommentaarina, mille postitad vooru 2 alguses.
- Kleepsud peavad klassis olemas olema. Lepi enne kokku, kes need tuppa toob.
- Slaid reeglite ja taimeriga on klassi ekraanil.

## Teamsi kohandus

Õpetaja ei kuule laudade arutelu ega näe pabereid. Seepärast:

- Igal tiimil on laua keskel lahti üks arvuti, kaardiarvuti. Sellel on avatud ainult tiimi „Selgita oma otsust” Issue. Muud arvutid ja telefonid on kinni. Kaardiarvuti eest vastutab projektijuht.
- Paberkaardi asemel kirjutab iga vastaja oma ühe lause Issue'sse kommentaarina. Need kommentaarid on õpetaja tõend kõigi tiimide kohta.
- Õpetaja jälgib Issue'sid. Kui tiim jääb kinni, kirjutab ta lihtsama küsimuse kommentaarina, mitte ei ütle seda klassi kõlarisse.
- Õpetaja kuuleb ainult seda, mis öeldakse klassi arvuti mikrofoni juures. Vooru 2 paaridest esitab üks (õpetaja valib) seal.

## Käik

### 0:00–2:00 Reeglid

- Arvutid ja telefonid on kinni.
- Küsimusele vastab tiimiliige, kelle uus roll (sammust 1) on kaardil küsimuse juures. Kokkuvõttes: uus arhitekt seletab `v0.2.0` arhitektuuri, uus disainer disainivalikut, uus projektijuht tööviisi ja uus release manager hinnangut ning tegelikku aega.
- Kui küsimus tabab vastaja enda kirjutatud teksti, vastab keegi teine.
- Esimesed 2 minutit räägib ainult vastaja. Seejärel võivad teised täiendada.

### 2:00–12:00 Voor 1: rollivahetus (10 min)

Igaüks vastab oma küsimusele: 2 minutit räägib, seejärel kirjutab kaardiarvutis Issue'sse ühe lause oma vastusega. Õpetaja ei kuule laudade vastuseid, seega on need kommentaarid tema ainus tõend.

**Tiim 01**
- *Arhitekt (Meeri):* Õppija avab nädala ega näe ühtki tundi. Kuidas teie süsteem teab, kas tunde tõesti pole või jäid andmed laadimata? Milline osa selle eest vastutab ja mida kasutaja kummalgi juhul näeb?
- *Disainer (Helen):* Suunal A on plussiks ametlikud andmed ühes kohas. Miks te ikkagi valisite B ja mis peaks juhtuma, et läheksite tagasi A juurde?
- *Projektijuht (Marko):* Release notes ütleb, et Kanban „võimaldab ülesandeid paralleelselt täita”. Kas see on Kanbani mõte? Mida Kanban piirab ja miks?
- *Release manager (Kauri):* Release notes'i ainus arv on „etapp kestis 12 kalendripäeva”. Kuidas oleks pidanud välja nägema hinnangu ja tegeliku aja võrdlus ning mida pidi selleks tegema töö ajal?

**Tiim 02**
- *Arhitekt (Mariann):* Lugu 1 ütleb, et tudeng näeb järgmist koolipäeva ilma klõpsuta. Mis juhtub, kui ta avab lehe esimest korda uues telefonis? Kus on teie info liikumises brauser ja miks?
- *Disainer (Greete):* Teekonnas on probleem sammudes 1, 3, 4 ja 5, aga lood katavad kolme sammu. Millist sammu ükski lugu ei kata ja kas see oli teadlik otsus?
- *Projektijuht (Medlin):* Otsuses 002 on reegel „korraga kõige rohkem üks Issue olekus In progress”. Kas see täitus, kuidas seda kontrollida ja miks Kanban sellist piirangut tahab?
- *Release manager (Alison):* Peaaegu kõigi Issue'de hinnang oli 1 h. Miks see ei kirjeldanud tegelikku tööd ja mida oleks hinnang pidanud arvesse võtma?

**Tiim 04**
- *Arhitekt (Rico):* Mis juhtuks ilma reegliteta „ebaõnnestunud päringut ei tõlgendata ärajäämisena” ja „esimene edukas päring loob võrdlusaluse”?
- *Disainer (Artur):* Teie tõendid ütlevad „seni pole ma päris hilja teada saanud”. Miks siis B, mitte A? Mida B lisaks maksab?
- *Projektijuht (Matthias):* Tööviisi otsus lubab „üks Issue korraga” ja vahekontrolli etapi keskel. Mis oleks 16.11 õhtul olnud teisiti, kui te oleksite neid järginud?
- *Release manager (Mattias):* Rico loo hinnang oli 3 h, tegelik aeg 1 h. Mida see erinevus ütleb ja kuidas järgmisel korral teisiti hinnata?

**Tiim 07**
- *Arhitekt (Martin):* Arhitektuuris on kirjas, et kui loengut pole või andmed jäid laadimata, annab loogika vaatele eri tulemused. Miks peavad need kaks olukorda andma eri tulemuse ja milline kolmest osast otsustab, mida kasutaja näeb?
- *Disainer (Kristo):* Valisite suuna A. Milline uus info paneks teid valima B ja mis saab suuna A korral Martini valikainete loost?
- *Projektijuht (Tauri):* Teie tööviis on Kanban GitHub Projectsi tahvlil. Mida peaks tahvlilt nägema, et tööviis on päriselt kasutusel? Miks ei asenda seda Gantti diagramm?
- *Release manager (Kaspar):* Release notes'is on ajad tagantjärele hinnatud. Mida peab kodutöös 4 tegema teisiti, et võrdlus oleks päris?

**Tiim 08**
- *Arhitekt (Robin):* Teie osad on näiteks „Muudetud tundide visuaalne eristamine”. Mis vahe on funktsioonil ja süsteemi osal? Milline osa vastutab selle eest, et süsteem teab, mis muutus?
- *Disainer (Monika):* Te valisite A. B oleks olnud A pluss vana tabel. Mida oleks B maksnud ja milline tõend oleks pannud teid B kasuks otsustama?
- *Projektijuht (Aili):* Tööviisis lubasite veerud To do ja Review. Miks tahab Kanban eraldi Review veergu ja mida oleks see teie PR-ide juures muutnud?
- *Release manager (Thorian):* Backlog'is oli algul 17 h, viimasel õhtul 39 h. Mis vahe on hinnangul ja tegelikul ajal ning kuidas oleks tabel pidanud välja nägema?

**Tiim 10** (kolm liiget, kolm küsimust)
- *Arhitekt (Merilin):* Arhitektuur lubab uuendada baasandmeid allikast ja säilitada kasutaja kinnitatud valikud. Mis juhtub, kui tudeng kinnitas valikaine ja seejärel selle aeg muutub või aine kaob allikast?
- *Disainer ja release manager (Peep):* Suund C „ühendab A ja B eelised”. Mida C maksab? Mida teeb tudeng Alpha-versioonis, kui reegel näitab talle võõrast ainet?
- *Projektijuht (Ursula):* Teie WIP-piirang on 3 Issue't korraga kogu tiimi peale. Millal see piirang teid päriselt peataks? Milline väärtus oleks mõistlik?

Ursula oli haige, kui WIP-piirangu üle otsustati. Kui ta ei olnud otsuse juures, märgi vaatluslehele „polnud kohal”, mitte „ei oska”.

Head vastused (õpetajale) on failides `understanding-XX.md`, osas „Diagnostilised küsimused”. Tiimi 02 teine, tiimi 04 neljas, tiimi 07 kolmas ja neljas, tiimi 08 esimene ja kolmas ning tiimi 10 teine küsimus on uued. Nende hea vastus on lühidalt allpool.

### 12:00–22:00 Voor 2: „Mis siis, kui” (10 min)

Õpetaja postitab igale tiimile Issue'sse kommentaarina ühe muutuse, mis puudutab tiimi suurimat kontrollimata eeldust.

| Tiim | Muutus |
|---|---|
| 01 | Kalendriekspordist ei saa andmeid kursuse kaupa ja tulevasi kuupäevi seal pole. |
| 02 | Õppekorraldus ütleb, et olemasoleva tunniplaanilehe vaikevaadet ei saa muuta. |
| 04 | Kool hakkab ise saatma tunniplaani muudatuste teavitusi kalendrivoo kaudu. |
| 07 | Haapsalu tunniplaani andmed on saadaval ainult veebilehena, mitte masinloetaval kujul. |
| 08 | Andmeallikas ei näita, mis tunnis muutus. Näha on ainult praegune seis. |
| 10 | ÕIS-i andmeid ei tohi isikuandmete tõttu kasutada. |

Viie minutiga kirjutab tiim Issue'sse kolm rida:
1. millised kasutajalood enam ei täitu;
2. mis muutub disainis või arhitektuuris;
3. milline uus Issue tekib backlog'i.

Seejärel esitavad paarid teineteisele: 01 ja 02, 04 ja 08, 07 ja 10. Kumbki tiim räägib 2 minutit ja kuulaja tiim küsib ühe küsimuse. Ühe paari, kelle õpetaja valib, esitlus toimub klassi arvuti mikrofoni juures, et õpetaja seda kuuleks.

Ütle lõpus: „Need kolm rida on teie esimene risk kodutöö 4 riskikaardis. Arhitekt vastutab selle eest.”

### 22:00–25:00 Voor 3: üks lause (3 min)

Igaüks valib ühe mõiste ja kirjutab kleepsule ühe lause **oma projekti näitega**, nagu seletaks esimese kursuse sõbrale: „WIP-piirang on …, meie projektis …”.

Mõisted (kõige vähem omandatud on eespool):
- WIP-piirang;
- hinnang ja tegelik aeg;
- risk ja eeldus;
- kompromiss;
- sõltuvus;
- kontrolltingimus;
- süsteemi piir.

Kleepsud lähevad tiimi kaupa tahvlile. Projektijuht pildistab tiimi kleepsud ja lisab foto tiimi Issue'sse. Õpetaja sorteerib need kahte hunnikusse, „oma näide” ja „definitsioon”, ja loeb Teamsis ette kaks head näidet ilma nimedeta. Mõiste, millel on kõige rohkem definitsioone, on sammu 7 teema (kodutöö 3 põhjal tõenäoliselt WIP või hinnang).

### Pärast

Projektijuht paneb kodutöö 4 alguses kirja kolm lünka Issue'na: küsimused, millele tiim vastata ei osanud. Igal Issue'l on hinnang (h). Need on release'i `v0.3.0` backlog'is (vt `seminar-plan.md`).

## Uute küsimuste head vastused

- **02, disainer:** samm 1 (lehe avamine ja vaate valik) või mõni teine samm jääb katmata. Hea vastus nimetab sammu ja ütleb, kas see on teadlik valik (tõend nõrk) või jäi märkamata.
- **04, release manager:** 3 h vs 1 h tähendab, et lugu oli väiksem kui arvati või hinnati malli järgi, mitte töö sisu järgi. Järgmine kord tuleb hinnata Issue'de kaupa ja panna tegelik aeg kirja sulgemisel.
- **07, projektijuht:** tahvlil liiguvad kaardid töö ajal, olekus In progress on piiratud arv kaarte ja Review veerus ootav töö on näha. Gantt näitab ajakava, aga ei piira pooleli olevat tööd ega näita ummikut.
- **07, release manager:** hinnang pannakse Issue'le selle loomisel ja tegelik aeg sulgemisel, mitte release'i õhtul. Võrdlus tehakse Issue'de kaupa.
- **08, arhitekt:** funktsioon on see, mida kasutaja näeb. Osa on süsteemi tükk, millel on vastutus, näiteks andmete lugemine või muudatuste tuvastamine. Muutuse teadmine on andmete lugemise või võrdlemise osa, mitte vaate osa. Kui allikas muutust ei näita, peab süsteem salvestama varasema seisu.
- **08, projektijuht:** Review veerg näitab, et töö ootab teise inimese ülevaatust. Siis oleks olnud näha, et 14 PR-i 15-st ühendas autor ise.
- **10, disainer:** C toob kaasa kasutaja tuvastamise ja valikute salvestamise. Alphas ei saa tudeng valet reeglit parandada, see on teadlik kompromiss lihtsuse kasuks.

## Õpetaja vaatlusleht

Punkte see ei anna. Ühe rea saab iga tiim.

| Tiim | Arhitekt | Disainer | Projektijuht | Release manager | „Mis siis, kui”: seos lugude, arhitektuuri ja backlog'iga | Kleepsud: oma näiteid |
|---|---|---|---|---|---|---|
| | O / D / E | O / D / E | O / D / E | O / D / E | jah / osaliselt / ei | x / y |

O – oma sõnadega, D – kordab dokumenti, E – ei oska seletada.

Õpetaja hindab kirjalike ühelauseliste vastuste põhjal. Suuliselt kuuleb ta ainult mikrofoni juures esinenud paari. Seepärast on D ja E märge esialgne, kuni seda kinnitab vestlus või kodutöö.

Kasutus:
- kodutöö 4 nõuete kohandamine tiimide kaupa;
- vestlus ilma süüdistuseta õppijatega, kelle kohta raportis on „arusaamise tõend puudub” ja kes ka siin vastata ei osanud.

## Gerli (tiim 06)

Gerlil on reposse tehtud ainult README ja kontseptsiooni ei ole. Voorus 1 on ta tiimi 10 juures kuulaja. Voorus 2 on ta tiimide 07 ja 10 paaris küsija. Voorus 3 teeb ta sama mis teised, kasutades oma projekti.

## Ohukohad

- **Kontrolltöö tunne.** Kui tiimi Issue's pole 3 minuti järel ühtegi vastust, kirjuta lihtsam küsimus kommentaarina: „Mida kasutaja ekraanil näeb?” Hinnatakse seletamist, mitte dokumendi kordamist.
- **Kaardiarvuti kui mälutugi.** Kui tiim avab kaardiarvutis repo faile, kordab ta dokumenti. Projektijuht hoiab ekraanil ainult Issue't.
- **Üks inimene räägib kõigi eest.** Kahe minuti reegel kehtib. Teised tohivad täiendada alles pärast seda.
- **Avalik häbistamine.** Ette loetakse ainult häid kleepse, ilma nimedeta. Vastused jäävad tiimi Issue'sse, mitte jagatud ekraanile ega Teamsi üldvestlusse.
- **Aeg.** Voor 2 on kõige väärtuslikum, sest annab riskikaardi sisendi. Kui aega jääb väheks, lühenda vooru 3, mitte vooru 2.

## Lahtine

- **Aeg.** Õpetaja juhise I osas on 90 minutist kasutatud ka samm 1 (18 min). Samm 2 lisab 25 minutit. Töökava järgi lüheneb Cloudflare'i juhtum (15 min) või kaob üldse, nii et aeg mahub ära.
- **Tiimi 08 rollid.** Monika on uus disainer ja disaini A-valiku lõik on tema kirjutatud. Kui ta vastab enda tekstist, vahetage disaineri ja arhitekti küsimused.
