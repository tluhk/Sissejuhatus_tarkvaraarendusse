# Teine seminar – Tarkvaraarenduse meetodid ja koodi kvaliteet

Teise loengu eesmärk on teoreetilise poole pealt tutvuda tarkvaraarenduse meetoditega ja praktilise poole pealt seadistada VSCode ning teha praktiliselt läbi paar koodi kena kirjutamise harjutust.

[Teise loengu slaidid](https://gamma.app/docs/Tarkvaraarenduse-meetodid-ja-koodi-kvaliteet-6hyvvauxa5dckj4)


[Teise loengu salvestus](https://youtu.be/2GWtP4dUIcQ?si=L2aPjk4xkmN9kOqE)



## Tunni kirjeldus

## Sisukord

- [Slaid 1: Tarkvaraarenduse meetodid](#slaid-1-tarkvaraarenduse-meetodid)
- [Slaid 2: Rollid tarkvaraarenduses](#slaid-2-rollid-tarkvaraarenduses)
- [Slaid 3: Koodi kvaliteet](#slaid-3-koodi-kvaliteet)
- [Slaid 4: VSCode seadistamine](#slaid-4-vscode-seadistamine)
- [Slaid 5: .gitignore fail](#slaid-5-gitignore-fail)
- [Slaid 6: ESLint ja lintimise tööriistad](#slaid-6-eslint-ja-lintimise-tööriistad)
- [Slaid 7: Koodistandardid ja -konventsioonid](#slaid-7-koodistandardid-ja--konventsioonid)
- [Slaid 8: Koodi kvaliteedi tagamine](#slaid-8-koodi-kvaliteedi-tagamine)


---

## **Slaid 1: Tarkvaraarenduse meetodid**

**Traditsioonilised meetodid: Veejuga (Waterfall)**

Veejoa metoodika on üks esimesi ja klassikalisemaid tarkvaraarenduse meetodeid, mida kasutatakse peamiselt siis, kui nõuded on algusest peale väga selged ja neid ei ole vaja protsessi käigus muuta. Selle meetodi peamine puudus seisneb selle jäikuses. Näiteks, kui projekt on liikunud edasi arenduse faasi ja avastatakse, et mõned nõuded olid valesti mõistetud, on tagasimineku ja vigade parandamise kulud väga suured.

**Näide:** Kujutage ette, et ehitate maja ja alustate katusest, enne kui vundament on valmis. Kui te hiljem avastate, et vundament vajab kohandusi, peate katuse maha võtma, et teha vajalikud parandused – täpselt see juhtub veejoa meetodiga, kui hiljem ilmnevad probleemid varasemates etappides.

**Agiilne metoodika**

Agiilne on vastupidine veejoale – see on loodud olema paindlik ja iteratiivne. Agiilsetes projektides toimub töö väikestes tsüklites (sprindid) ja iga tsükli järel antakse tagasisidet ning vajadusel tehakse kohandusi. See võimaldab projektidel areneda ja kohanduda vastavalt kliendi vajadustele.

**Näide:** Kui arendate mobiilirakendust, võite esimeses iteratsioonis luua lihtsa kasutajaliidese ja baastöövood, seejärel saada kasutajatelt tagasisidet ja seejärel täiendada funktsioone järgmistes iteratsioonides.

**Scrum**

Scrum on konkreetne raamistik agiilse metoodika rakendamiseks. Scrum jagab projektid lühikesteks sprintideks, tavaliselt 2-4 nädalat, mille järel tiim esitleb tööd, saab tagasisidet ja määratleb järgmise sprindi ülesanded. Olulised rollid Scrumi puhul on tooteomanik, kes määrab prioriteedid, ja Scrum-meister, kes aitab tiimil takistusi kõrvaldada.

**Näide:** Kui arendate veebi e-poodidele, võib üks sprindi eesmärk olla toote kataloogi loomine, samas kui järgmise sprindi eesmärk võib olla maksesüsteemi lisamine.

Videotutvustused:
Agiilse arenduse manifest:https://agilemanifesto.org/iso/et/manifesto.html

Videod

Scrum vs Agiilne: https://www.youtube.com/watch?v=K7YMEFjh724

Mis on scrum: https://www.youtube.com/watch?v=iJ_sl6J8PRg

Scrum vs Kanban: https://www.youtube.com/watch?v=F5QIqFEDv2k

Agile vs waterfall: https://www.youtube.com/watch?v=x2LE3FKGEkA

5 meetodit (sh waterfall): https://www.youtube.com/watch?v=ID2KvYvuN3Y

DevOps vs Agile: https://www.youtube.com/watch?v=MSjr6sCUniE

Waterfall vs Agile: https://www.youtube.com/watch?v=5RocT_OdQcA

### Tunniharjutus 1: [Grupitöö slaidile 1](tunniharjutus_1.md)

---

## **Slaid 2: Rollid tarkvaraarenduses**

Tarkvaraarenduse projektides on vaja erinevate oskustega inimesi, sest keerukate süsteemide loomine nõuab palju teadmisi ja kogemusi erinevates valdkondades.

**Analüütik:**

Analüütiku töö on esmapilgul lihtne – koguda ja analüüsida kliendi nõudeid. Tegelikkuses on see aga keerukas roll, mis nõuab head suhtlemisoskust ja ärimõtlemist, sest analüütik peab mõistma, kuidas ärinõuded ja tehnilised lahendused kokku viia.

**Näide:** Kui kliendil on nõue "kasutaja peab saama registreeruda oma e-posti ja parooliga," peab analüütik mõtlema ka sellele, millised turvalisuse meetmed ja valideerimisprotsessid on vajalikud, et see funktsioon oleks ohutu ja töökindel.

**Disainer:**

Disainerid vastutavad kasutajaliidese ja kasutajakogemuse eest. Nende ülesanne on muuta keerulised süsteemid kasutajasõbralikeks ja visuaalselt meeldivateks. Hea disain on sageli see, mis eristab häid ja suurepäraseid rakendusi.

**Näide:** Kujutage ette, et arendate rakendust, kus kasutaja peab sisestama mitu isiklikku detaili. Disainer võib soovitada jagada sisestusvormid mitmeks väiksemaks sammuks, et kasutaja ei tunneks end ülekoormatuna ja kasutajaliides oleks selgem.

**Arendaja:**

Arendajad on tihti projekti tehniline tuum, sest nemad kirjutavad koodi, mis realiseerib ärinõuded. Arendajad peavad tihedalt töötama nii analüütikute kui ka disaineritega, et luua tehniliselt korrektne ja kasutajasõbralik lahendus.

**Testija:**

Testija ülesanne on kontrollida, kas loodud tarkvara töötab ootuspäraselt ja kas see vastab esitatud nõuetele. Testijad teevad käsitsi ja automaatseid teste, et leida vigu ja tagada kvaliteet. See on hädavajalik, sest ilma korraliku testimiseta võivad väiksed vead kasvada suuremateks probleemideks.

**Projektijuht:**

Projektijuht on meeskonna koordinaator. Ta jälgib tiimi tööd ja ajakava, tagades, et projekt liigub edasi ja et iga tiimiliige on teadlik oma ülesannetest. Hea projektijuht oskab vältida takistusi ja lahendada probleeme enne, kui need muutuvad suureks.

### Tunniharjutus 2: [Grupitöö slaidile 2](tunniharjutus_2.md)

---

## **Slaid 3: Koodi kvaliteet**

**Miks on oluline?**

Koodi loetavus on eriti oluline, kui projekt kestab pikemat aega või töötab selle kallal rohkem inimesi. Halvasti kirjutatud kood muutub ajapikku raskesti hooldatavaks ja võib muutuda tehniliseks võlaks. Loetav ja hästi struktureeritud kood vähendab vigu ja muudab arendajate töö lihtsamaks.

**Näide:** Kui projektis töötab 5-10 arendajat, peavad kõik neist olema võimelised mõistma üksteise koodi. Halvasti dokumenteeritud ja loetamatuks muutunud kood võib põhjustada palju segadust, kui uus arendaja peab selles muudatusi tegema.

**Koodistiili juhised:**

Koodistiilide puhul tuleb sageli mängu PascalCase, camelCase, snake_case ja kebab-case. Iga stiili kasutatakse erinevates kontekstides ja tiimides.

- **PascalCase:** Kasutatakse tihti klasside nimedes, näiteks `CustomerAccount`.
- **camelCase:** Funktsioonide ja muutujate nimetamiseks, näiteks `calculateTotalPrice`.
- **snake_case:** Kasutatakse tihti konstandite ja andmebaasiväljade nimedes, näiteks `user_name`.
- **kebab-case:** Kõige sagedamini kasutatakse CSS-klassi nimedes, näiteks `.menu-item`.

Oluline on, et meeskond lepiks kokku ühtse koodistiili kasutamises. Näiteks kui tiimis on kokku lepitud, et kasutatakse camelCase'i muutujate jaoks, siis peaksid kõik tiimiliikmed sellest reeglist kinni pidama.

**BEM (Block, Element, Modifier):**

BEM-mudeli kasutamine CSS-is aitab hoida stiilid korras ja vältida segadust, mis tekib siis, kui klassinimed muutuvad keerukaks. BEM aitab hoida komponendid ja nende elemendid selgelt eristatavatena ning lihtsustab hilisemat hooldamist.

**Näide:** Kui teil on nupp, millel on ikoon, ja te soovite, et see nupp oleks teatud juhtudel suurem, saate kasutada BEM-mudelit: `.button`, `.button__icon`, `.button--large`. Selline süsteem muudab stiilide loomise ja muutmise lihtsamaks.

---

## **Slaid 4: VSCode seadistamine**

**Mis on Visual Studio Code?**

IDE (Integrated Development Environment) ehk integreeritud arenduskeskkond on tarkvarapakett, mis koondab endas mitmeid arendaja tööks vajalikke tööriistu. Tavaliselt sisaldab IDE koodiredaktorit, kompilaatorit või interpretaatorit, silumistööriistu (debugger), versioonihalduse integratsiooni ja muid arendust lihtsustavaid funktsioone. IDE eesmärk on muuta arendusprotsess sujuvamaks ja produktiivsemaks, pakkudes kõik vajalikud tööriistad ühes keskkonnas.

Visual Studio Code on üks kõige populaarsemaid koodiredaktoreid maailmas, kuna see on tasuta, avatud lähtekoodiga ja laiendatav. Üks selle suurimaid eeliseid on laiendused, mis aitavad arendajatel koodi kirjutada efektiivsemalt ja vähendada vigu.

**Näide:** Kui te töötate JavaScripti projektiga ja soovite tagada, et teie kood järgib kindlaid stiilireegleid, saate installida **ESLint** laienduse, mis hoiatab teid kohe, kui koodis on stiilivead või vead, mis võivad põhjustada funktsionaalsuse probleeme.

---

## **Slaid 5: .gitignore fail**

**Eesmärk:**

.gitignore fail aitab arendajatel vältida mittevajalike failide lisamist Git repositooriumi. See on eriti oluline, kuna tarkvaraarenduse käigus tekivad sageli ajutised failid, süsteemispetsiifilised failid või suured kaustad, mida pole vaja teistega jagada.

**Näide:** Kui töötate Node.js projektiga, paigaldatakse kõik vajalikud teegid `node_modules` kausta, kuid seda kausta ei ole mõistlik Git repositooriumi lisada, sest sõltuvused saab uuesti installida `package.json` põhjal.

---

## **Slaid 6: ESLint ja lintimise tööriistad**

**Mis on ESLint?**

ESLint on JavaScripti ja TypeScripti lintimise tööriist, mis aitab leida koodivigu ja tagada, et kood järgib tiimi kokkulepitud reegleid.

**Kuidas see aitab?**

ESLint aitab vähendada süntaksivigu ja tagab, et kood on järjepidev. See muudab arenduse sujuvamaks ja lihtsustab vigade leidmist ja parandamist.

**Integreerimine VSCode'iga:**

Kui ESLint on integreeritud VSCode'iga, saab arendaja reaalajas vigadest teada ja vajadusel rakendada automaatseid parandusi.

---

## **Slaid 7: Koodistandardid ja -konventsioonid**

**Parimad praktikad:**

- Kood peab olema ühtlase struktuuriga ja järjekindel kogu meeskonna jaoks.
- Kommentaarid peaksid olema selged ja aitama mõista keerulisemaid koodiosi.

**Automatiseeritud tööriistad:**

Tööriistad nagu **Prettier** vormindavad koodi automaatselt, muutes selle stiili ühtlaseks. Lisaks saab kasutada **Stylelinti**, et kontrollida CSS-i stiilide ühtsust.

**Tiimisiseste reeglite seadistamine:**

Tiimid peaksid looma ja järgima ühiseid stiilijuhendeid, mida kõik arendajad järgivad. Selleks kasutatakse tavaliselt konfiguratsioonifaile nagu `.eslintrc` ja `.prettierrc`.

---

## **Slaid 8: Koodi kvaliteedi tagamine**

**Meetodid:**

Koodi kvaliteeti saab tagada mitmel viisil, sealhulgas:
- **Koodireview'd:** Teised meeskonnaliikmed vaatavad koodi üle, et leida vigu ja parandada kvaliteeti.
- **Automaatne testimine:** Testid, mis kontrollivad koodi töökindlust iga muudatuse järel.
- **Pidev integreerimine (CI):** Koodi muutuste pidev testimine ja integreerimine, et vältida konflikte ja vigasid.

**Tööriistad:**

Koodi kvaliteedi jälgimiseks ja testimiseks on palju tööriistu, näiteks:
- **GitHub Actions**: Võimaldab automaatselt käivitada teste ja muid protsesse iga koodimuudatuse puhul.
- **Testimisraamistikud**: Näiteks Jest (JavaScript) või PyTest (Python), mis aitavad automaatselt kontrollida, kas kood töötab ootuspäraselt.

**Eesmärk:**

Kvaliteetne kood on stabiilne, usaldusväärne ja kergesti hooldatav, vähendades vigade esinemise riski ja tagades parema koostöö meeskonnas.


## Kodutöö

- [Kodune töö 1](../../docs/kodusedtood/kodune_02.md)