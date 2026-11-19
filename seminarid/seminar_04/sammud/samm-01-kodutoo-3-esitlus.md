# Seminar 4, samm 1: kodutöö 3 esitlus

Kestus umbes 30 minutit: 10 minutit ettevalmistust, seejärel iga tiim umbes 3 minutit. Esitlus toimub klassi arvuti mikrofoni ees, nii et õpetaja kuuleb Teamsi kaudu kõiki tiime. Järgmine samm on tahvli ja `v0.2.0` läbivaatus.

## Miks

Kodutöö 3 põhjal sõnastas AI suure osa disainist, arhitektuurist, tööviisist ja release notes'ist. Mida keerulisem mõiste, seda suurem on vahe ladusa dokumendi ja õppija enda seletuse vahel.

Ettevalmistus on **teine võimalus aru saada**, mitte kontroll. AI kasutamine on lubatud: kui tiim kasutab AI-d oma otsuse lahtiseletamiseks ja saab nüüd aru, on eesmärk täidetud. Arusaamist näitab õpetaja küsimus pärast esitlust, mitte ettevalmistuse viis. Lisaks on see eksami esitluse proov.

## Mida õppijatele öelda

„Iga tiim tutvustab oma kodutöö 3 otsuseid ja seda, kuidas te nendeni jõudsite. Teil on 10 minutit ettevalmistust, arvutid ja AI on lubatud. Kui midagi oli seni ebaselge, kasutage seda aega, et aru saada. Esitluses räägite oma sõnadega, mitte ei loe dokumendist. Punkte see ei anna. Kui mõnele küsimusele vastata ei oska, on see leid, mitte viga: see läheb teie backlog'i.”

Ära ütle, et küsimused on tehtud AI-analüüsi põhjal. Ära nimeta, kelle tekst oli AI sõnastatud.

## Ettevalmistus (õpetaja)

- Slaid ülesande, esitluse kolme küsimuse ja taimeriga on klassi ekraanil.
- Vali igale tiimile küsimuste pangast (allpool) üks küsimus.
- Vaatlusleht (allpool) on lahti.

## Käik

### 0:00–1:00 Ülesanne

Näita slaidil, mida esitlus peab vastama:

1. Mis probleemi te lahendate ja kellele?
2. Millise suuna valisite, mis oli alternatiiv ja miks valisite just selle?
3. Mis on teie suurim kontrollimata eeldus?

### 1:00–11:00 Ettevalmistus (10 min)

Arvutid lahti, AI lubatud. Esitleja nimetab õpetaja alles ettevalmistuse lõpus, seega valmistub igaüks. Vali esitlejaks keegi, kes ei kirjutanud kodutöö 3 kontseptsiooni suuremat osa.

### 11:00–32:00 Esitlused (umbes 3 min tiimi kohta)

Järjekord: 01, 02, 04, 06, 07, 08, 10.

- Esitleja räägib kuni 2 minutit klassi arvuti mikrofoni ees, ilma dokumenti ette lugemata.
- Õpetaja esitab Teamsis ühe küsimuse. Sellele vastab keegi teine tiimist kui esitleja.
- Kui tiim jääb kinni, küsi lihtsamini: „Mida kasutaja ekraanil näeb?” Märgi küsimus vaatluslehele lüngana ja liigu edasi.

**Gerli (tiim 06):** kontseptsiooni pole, seega räägib ta 1 minuti, mis probleemi ta lahendab ja mis on tema järgmine samm. Küsimust ei esitata.

## Küsimuste pank

Vali iga tiimi kohta üks küsimus. Avalikult klassi ees eelista **arhitektuuri** või **disaini** küsimust: need puudutavad otsuseid. Tööviisi ning aja ja release'i küsimused puudutavad protsessi vigu ja nendega tegeleb samm 2 tiimi enda tahvlil, mitte klassi ees.

**Tiim 01**
- *Arhitektuur:* Õppija avab nädala ega näe ühtki tundi. Kuidas teie süsteem teab, kas tunde tõesti pole või jäid andmed laadimata? Milline osa selle eest vastutab ja mida kasutaja kummalgi juhul näeb?
- *Disain:* Suunal A on plussiks ametlikud andmed ühes kohas. Miks te ikkagi valisite B ja mis peaks juhtuma, et läheksite tagasi A juurde?
- *Tööviis:* Release notes ütleb, et Kanban „võimaldab ülesandeid paralleelselt täita”. Kas see on Kanbani mõte? Mida Kanban piirab ja miks?
- *Aeg ja release:* Release notes'i ainus arv on „etapp kestis 12 kalendripäeva”. Kuidas oleks pidanud välja nägema hinnangu ja tegeliku aja võrdlus ning mida pidi selleks tegema töö ajal?

**Tiim 02**
- *Arhitektuur:* Lugu 1 ütleb, et tudeng näeb järgmist koolipäeva ilma klõpsuta. Mis juhtub, kui ta avab lehe esimest korda uues telefonis? Kus on teie info liikumises brauser ja miks?
- *Disain:* Teekonnas on probleem sammudes 1, 3, 4 ja 5, aga lood katavad kolme sammu. Millist sammu ükski lugu ei kata ja kas see oli teadlik otsus?
- *Tööviis:* Otsuses 002 on reegel „korraga kõige rohkem üks Issue olekus In progress”. Kas see täitus, kuidas seda kontrollida ja miks Kanban sellist piirangut tahab?
- *Aeg ja release:* Peaaegu kõigi Issue'de hinnang oli 1 h. Miks see ei kirjeldanud tegelikku tööd ja mida oleks hinnang pidanud arvesse võtma?

**Tiim 04**
- *Arhitektuur:* Mis juhtuks ilma reegliteta „ebaõnnestunud päringut ei tõlgendata ärajäämisena” ja „esimene edukas päring loob võrdlusaluse”?
- *Disain:* Teie tõendid ütlevad „seni pole ma päris hilja teada saanud”. Miks siis B, mitte A? Mida B lisaks maksab?
- *Tööviis:* Tööviisi otsus lubab „üks Issue korraga” ja vahekontrolli etapi keskel. Mis oleks 16.11 õhtul olnud teisiti, kui te oleksite neid järginud?
- *Aeg ja release:* Rico loo hinnang oli 3 h, tegelik aeg 1 h. Mida see erinevus ütleb ja kuidas järgmisel korral teisiti hinnata?

**Tiim 07**
- *Arhitektuur:* Arhitektuuris on kirjas, et kui loengut pole või andmed jäid laadimata, annab loogika vaatele eri tulemused. Miks peavad need kaks olukorda andma eri tulemuse ja milline kolmest osast otsustab, mida kasutaja näeb?
- *Disain:* Valisite suuna A. Milline uus info paneks teid valima B ja mis saab suuna A korral Martini valikainete loost?
- *Tööviis:* Teie tööviis on Kanban GitHub Projectsi tahvlil. Mida peaks tahvlilt nägema, et tööviis on päriselt kasutusel? Miks ei asenda seda Gantti diagramm?
- *Aeg ja release:* Release notes'is on ajad tagantjärele hinnatud. Mida peab kodutöös 4 tegema teisiti, et võrdlus oleks päris?

**Tiim 08**
- *Arhitektuur:* Teie osad on näiteks „Muudetud tundide visuaalne eristamine”. Mis vahe on funktsioonil ja süsteemi osal? Milline osa vastutab selle eest, et süsteem teab, mis muutus?
- *Disain:* Te valisite A. B oleks olnud A pluss vana tabel. Mida oleks B maksnud ja milline tõend oleks pannud teid B kasuks otsustama?
- *Tööviis:* Tööviisis lubasite veerud To do ja Review. Miks tahab Kanban eraldi Review veergu ja mida oleks see teie PR-ide juures muutnud?
- *Aeg ja release:* Backlog'is oli algul 17 h, viimasel õhtul 39 h. Mis vahe on hinnangul ja tegelikul ajal ning kuidas oleks tabel pidanud välja nägema?

**Tiim 10** (kolm küsimust)
- *Arhitektuur:* Arhitektuur lubab uuendada baasandmeid allikast ja säilitada kasutaja kinnitatud valikud. Mis juhtub, kui tudeng kinnitas valikaine ja seejärel selle aeg muutub või aine kaob allikast?
- *Disain:* Suund C „ühendab A ja B eelised”. Mida C maksab? Mida teeb tudeng Alpha-versioonis, kui reegel näitab talle võõrast ainet?
- *Tööviis:* Teie WIP-piirang on 3 Issue't korraga kogu tiimi peale. Millal see piirang teid päriselt peataks? Milline väärtus oleks mõistlik?

Head vastused (õpetajale) on failides `understanding-XX.md`, osas „Diagnostilised küsimused”. Tiimi 02 teine, tiimi 04 neljas, tiimi 07 kolmas ja neljas, tiimi 08 esimene ja kolmas ning tiimi 10 teine küsimus on uued. Nende hea vastus on allpool.

### Uute küsimuste head vastused

- **02, disain:** samm 1 (lehe avamine ja vaate valik) või mõni teine samm jääb katmata. Hea vastus nimetab sammu ja ütleb, kas see on teadlik valik (tõend nõrk) või jäi märkamata.
- **04, aeg ja release:** 3 h vs 1 h tähendab, et lugu oli väiksem kui arvati või hinnati malli järgi, mitte töö sisu järgi. Järgmine kord tuleb hinnata Issue'de kaupa ja panna tegelik aeg kirja sulgemisel.
- **07, tööviis:** tahvlil liiguvad kaardid töö ajal, olekus In progress on piiratud arv kaarte ja Review veerus ootav töö on näha. Gantt näitab ajakava, aga ei piira pooleli olevat tööd ega näita ummikut.
- **07, aeg ja release:** hinnang pannakse Issue'le selle loomisel ja tegelik aeg sulgemisel, mitte release'i õhtul. Võrdlus tehakse Issue'de kaupa.
- **08, arhitektuur:** funktsioon on see, mida kasutaja näeb. Osa on süsteemi tükk, millel on vastutus, näiteks andmete lugemine või muudatuste tuvastamine. Muutuse teadmine on andmete lugemise või võrdlemise osa, mitte vaate osa. Kui allikas muutust ei näita, peab süsteem salvestama varasema seisu.
- **08, tööviis:** Review veerg näitab, et töö ootab teise inimese ülevaatust. Siis oleks olnud näha, et 14 PR-i 15-st ühendas autor ise.
- **10, disain:** C toob kaasa kasutaja tuvastamise ja valikute salvestamise. Alphas ei saa tudeng valet reeglit parandada, see on teadlik kompromiss lihtsuse kasuks.

## Pärast

Õpetaja postitab iga tiimi läbivaatuse Issue'sse (samm 2) küsimuse, millele tiim vastata ei osanud. Uus projektijuht paneb kodutöö 4 alguses selle ja teised lüngad kirja Issue'na koos hinnanguga (h).

## Õpetaja vaatlusleht

Punkte see ei anna. Ühe rea saab iga tiim.

| Tiim | Esitlus | Vastus küsimusele | Lünk backlog'i |
|---|---|---|---|
| | O / D / E | O / D / E | |

O – oma sõnadega, D – kordab dokumenti, E – ei oska seletada.

Kasutus:
- kodutöö 4 nõuete kohandamine tiimide kaupa;
- vestlus ilma süüdistuseta õppijatega, kelle kohta raportis on „arusaamise tõend puudub” ja kes ka siin vastata ei osanud.

## Ohukohad

- **Esitlus kui ettelugemine.** Kui esitleja loeb ekraanilt, palu tal ekraan sulgeda ja öelda üks lause oma sõnadega.
- **Avalik häbistamine.** Küsimus on otsuse kohta, mitte selle kohta, mis jäi tegemata. Tiimide puudusi ei loeta klassi ees ette.
- **Aeg.** Hoia 3 minutit tiimi kohta. Kui tiim läheb üle, lõpeta viisakalt ja jäta küsimus vahele: lünga saab tiim kirjalikult.
