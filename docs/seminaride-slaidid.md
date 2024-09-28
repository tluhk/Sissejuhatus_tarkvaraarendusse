# **Seminar 1: Sissejuhatus tarkvaraarendusse**

---

## **Slaid 1: Tarkvara ja tarkvaraarendus**

- **Mis on tarkvara?**
  - Programmid ja rakendused
  - Süsteemitarkvara vs rakendustarkvara
- **Tarkvara roll ühiskonnas**
  - Igapäevased rakendused
  - Tarkvara mõju erinevatele tööstusharudele

---

## **Slaid 2: Tarkvaraarenduse elutsükkel**

- **Peamised etapid:**
  - Nõuete kogumine
  - Disain
  - Arendus
  - Testimine
  - Implementatsioon
  - Hooldus
- **Lähenemised:**
  - Lineaarne (Waterfall)
  - Iteratiivne (Agile)

---

## **Slaid 3: Git**

- **Mis on Git?**
  - Versioonihaldussüsteem
- **Miks kasutada Git'i?**
  - Koodi ajaloo jälgimine
  - Koostöö hõlbustamine
- **Põhikäsud:** 
  - `git init`, `git add`, `git commit`, `git push`

---

## **Slaid 4: GitHub**

- **Mis on GitHub?**
  - Veebipõhine Git'i repositooriumide hostimine
- **Funktsioonid:**
  - Koostööprojektid
  - Koodide ülevaatused
  - Probleemide jälgimine (Issues)

---

## **Slaid 5: GitHubi organisatsioonid**

- **Organisatsiooni loomine:**
  - Samm-sammuline juhend
- **Eelised:**
  - Projektide parem haldamine
  - Tiimiliikmete õiguste haldamine
- **Koostöö võimalused:**
  - Ühine koodibaas
  - Projekti haldus

---

## **Slaid 6: GitHubi organisatsiooni vaated**

- **Miks luua organisatsiooni vaateid?**
  - Tööde organiseerimine
  - Tiimide koostöö parandamine
- **Kuidas luua?**
  - Projektide jaotamine
  - Õiguste seadistamine
- **Näited:**
  - Tiimipõhised repositooriumid
  - Projektipõhised vaated

---

## **Slaid 7: Markdown**

- **Mis on Markdown?**
  - Lihtne märgistuskeel tekstiformaadi kirjutamiseks
- **Kus kasutatakse?**
  - README failid
  - Dokumentatsioon
  - Kommentaarid GitHubis

---

## **Slaid 8: Markdown'i põhielemendid**

- **Pealkirjad:**
  - `#` Pealkiri tase 1
  - `##` Pealkiri tase 2
- **Teksti vormindamine:**
  - *Kursiiv*: `*tekst*`
  - **Rõhutatud**: `**tekst**`
- **Loendid:**
  - Numbriline: `1. Esimene`
  - Täppidega: `- Punkt`
- **Lingid ja pildid:**
  - Link: `[nimi](aadress)`
  - Pilt: `![alt tekst](pildi_aadress)`

---

# **Seminar 2: Tarkvaraarenduse meetodid ja koodi kvaliteet**

---

## **Slaid 1: Tarkvaraarenduse meetodid**

- **Traditsioonilised meetodid:**
  - **Veejuga (Waterfall):**  
    Lineaarne lähenemine, kus arendusetapid järgivad üksteist kindlas järjekorras. Muudatusi on raske hiljem teha, mis võib projekti edasi lükata, kui avastatakse vigu.

- **Agiilne metoodika:**
  - **Paindlik ja iteratiivne lähenemine:**  
    Agiilne arendus toimub väikeste sammudena, kus iga tsükli järel antakse tagasisidet ja tehakse vajalikud kohandused.
  - **Pidev tagasiside ja kohanemine:**  
    Agiilse meetodiga saab kiiremini kohaneda muutuvate nõuetega ja tagada parem kliendikogemus.

- **Scrum:**
  - **Raamistik agiilse rakendamiseks:**  
    Scrum on populaarne viis agiilse arenduse struktureerimiseks, kus tiimil on kindlad rollid (nt tooteomanik, Scrum-meister) ja regulaarsed koosolekud (nt igapäevased stand-up’id).
  - **Rollid, tseremooniad ja artefaktid:**  
    Scrum hõlmab tööjaotust, ajurünnakuid, pidevat tagasisidet ja edusammude jälgimist konkreetsete eesmärkide saavutamiseks.

---

## **Slaid 2: Rollid tarkvaraarenduses**

- **Analüütik:**  
  Vastutab nõuete kogumise ja analüüsi eest, et tagada projekti sobivus ärivajadustega.

- **Disainer:**  
  Kujundab kasutajaliidese ja kasutajakogemuse, tagades, et tarkvara oleks nii funktsionaalne kui ka visuaalselt atraktiivne ja kasutajasõbralik.

- **Arendaja:**  
  Vastutab tarkvara funktsionaalsuse implementeerimise eest, töötades tihedalt koos analüütikute ja disaineritega.

- **Testija:**  
  Testija ülesanne on kontrollida tarkvara kvaliteeti, leida ja raporteerida vead ning tagada, et tarkvara vastab nõuetele.

- **Projektijuht:**  
  Projektijuht planeerib projekti ja koordineerib meeskonna tööd, jälgides ajakava, eelarvet ja riske, et tagada projekti edukas lõpuleviimine.

---

## **Slaid 3: Koodi kvaliteet**

- **Miks on oluline?**  
  Hea koodi kvaliteet tähendab, et kood on loetav, hooldatav ja usaldusväärne. See vähendab vigade tekkimise tõenäosust ja lihtsustab meeskonnatööd.

- **Koodistiili juhised:**  
  Kood peab olema ühtses stiilis, et seda oleks lihtne lugeda ja hooldada. Tihti kasutatakse erinevaid formaate koodistandardite jaoks:
  - **PascalCase:** Iga sõna algab suure tähega (nt `MyFunctionName`).
  - **camelCase:** Esimene sõna väiketähega, järgnevate sõnade esitähed suured (nt `myFunctionName`).
  - **snake_case:** Kõik sõnad kirjutatakse väiketähtedega ja eraldatakse alakriipsuga (nt `my_function_name`).
  - **kebab-case:** Sõnad eraldatakse sidekriipsuga ja kõik tähed on väikesed (nt `my-function-name`).
  
  Oluline on, et tiim lepiks kokku ühtse stiili kasutamises, et kood oleks järjepidev.

- **Parimad praktikad:**  
  - **Kommentaaride kasutamine:** Kommentaarid peavad olema selged ja kasulikud, et selgitada keerulisemaid kohti.
  - **Koodistruktuur:** Funktsioonid ja klassid peaksid olema loogiliselt üles ehitatud ning mitte liiga pikad, et oleks lihtsam mõista ja hooldada.

- **BEM (Block, Element, Modifier):**  
  BEM on CSS-i nimetamispraktika, mis aitab hoida stiilid modulaarsetena ja loogiliselt organiseerituna. See jaguneb:
  - **Blokk:** Iseseisev komponent (nt `.button`).
  - **Element:** Bloki osa, mis ei saa iseseisvalt eksisteerida (nt `.button__icon`).
  - **Modifikaator:** Muudab bloki või elemendi välimust või käitumist (nt `.button--large`).

---

## **Slaid 4: VSCode seadistamine**

- **Mis on Visual Studio Code?**  
  VSCode on populaarne koodiredaktor, mis toetab paljusid programmeerimiskeeli ja pakub mugavaid tööriistu, mis muudavad koodikirjutamise lihtsamaks.

- **Laienduste kasutamine:**  
  - **ESLint:** Tööriist koodi analüüsimiseks ja vigade leidmiseks.
  - **Prettier:** Automaatne koodi vormindamine, et järgida ühtseid koodistiili reegleid.

- **Seadistamine:**  
  Laiendused saab hõlpsasti installida otse VSCode'is. Pärast seda saab konfigureerida vastavad seadistusfailid, näiteks `.eslintrc` ja `.prettierrc`, et määrata reeglid, mida arendustiim järgib.

---

## **Slaid 5: .gitignore fail**

- **Eesmärk:**  
  **.gitignore** failis loetletakse failid ja kaustad, mida ei tohiks lisada Git repositooriumi. See aitab vältida suurte või tundlike failide, nagu kompileeritud failid või keskkonnamuutujad, kogemata jagamist.

- **Kasutamine:**  
  .gitignore fail sisaldab selliseid kirjeid nagu `node_modules/` ja `.env`, et need ei läheks repositooriumisse. Samuti võib sinna lisada näiteks IDE-seadistusfaile või muid kohalikus keskkonnas vajalikke faile.

- **Näited:**  
  - `node_modules/` – ei pea olema repositooriumis, kuna sõltuvused saab installida package.json failist.
  - `.env` – keskkonnamuutujate failid, mis sisaldavad tundlikku informatsiooni, nagu API võtmed.

---

## **Slaid 6: ESLint ja lintimise tööriistad**

- **Mis on ESLint?**  
  ESLint on JavaScripti ja TypeScripti lintimise tööriist, mis aitab leida koodivigu ja tagada, et kood järgib tiimi kokkulepitud reegleid.

- **Kuidas see aitab?**  
  ESLint aitab vähendada süntaksivigu ja tagab, et kood on järjepidev. See muudab arenduse sujuvamaks ja lihtsustab vigade leidmist ja parandamist.

- **Integreerimine VSCode'iga:**  
  Kui ESLint on integreeritud VSCode'iga, saab arendaja reaalajas vigadest teada ja vajadusel rakendada automaatseid parandusi.

---

## **Slaid 7: Koodistandardid ja -konventsioonid**

- **Parimad praktikad:**  
  - Kood peab olema ühtlase struktuuriga ja järjekindel kogu meeskonna jaoks.
  - Kommentaarid peaksid olema selged ja aitama mõista keerulisemaid koodiosi.
  
- **Automatiseeritud tööriistad:**  
  Tööriistad nagu **Prettier** vormindavad koodi automaatselt, muutes selle stiili ühtlaseks. Lisaks saab kasutada **Stylelinti**, et kontrollida CSS-i stiilide ühtsust.

- **Tiimisiseste reeglite seadistamine:**  
  Tiimid peaksid looma ja järgima ühiseid stiilijuhendeid, mida kõik arendajad järgivad. Selleks kasutatakse tavaliselt konfiguratsioonifaile nagu `.eslintrc` ja `.prettierrc`.

---

## **Slaid 8: Koodi kvaliteedi tagamine**

- **Meetodid:**  
  Koodi kvaliteeti saab tagada mitmel viisil, sealhulgas:
  - **Koodireview'd:** Teised meeskonnaliikmed vaatavad koodi üle, et leida vigu ja parandada kvaliteeti.
  - **Automaatne testimine:** Testid, mis kontrollivad koodi töökindlust iga muudatuse järel.
  - **Pidev integreerimine (CI):** Koodi muutuste pidev testimine ja integreerimine, et vältida konflikte ja vigasid.

- **Tööriistad:**  
  Koodi kvaliteedi jälgimiseks ja testimiseks on palju tööriistu, näiteks:
  - **GitHub Actions**: Võimaldab automaatselt käivitada teste ja muid protsesse iga koodimuudatuse puhul.
  - **Testimisraamistikud**: Näiteks Jest (JavaScript) või PyTest (Python), mis aitavad automaatselt kontrollida, kas kood töötab ootuspäraselt.

- **Eesmärk:**  
  Kvaliteetne kood on stabiilne, usaldusväärne ja kergesti hooldatav, vähendades vigade esinemise riski ja tagades parema koostöö meeskonnas.

---

# **Seminar 3: Nõuete analüüs ja prototüüpimine**

---

## **Slaid 1: Nõuete analüüs**

- **Eesmärk:**
  - Määratleda, mida süsteem peab tegema
- **Nõuete tüübid:**
  - Funktsionaalsed nõuded
  - Mittefunktsionaalsed nõuded
- **Meetodid:**
  - Intervjuud
  - Küsitlused
  - Vaatlused

---

## **Slaid 2: Persoona**

- **Mis on persoona?**
  - Fiktiivne esindus sihtkasutajast
- **Miks kasutada?**
  - Parem arusaam kasutajate vajadustest
- **Komponendid:**
  - Demograafilised andmed
  - Eesmärgid ja motivatsioonid
  - Valupunktid

---

## **Slaid 3: Kasutajalood**

- **Struktuur:**
  - "Kasutajana soovin [funktsionaalsus], et saavutada [eesmärk]."
- **Eesmärk:**
  - Kirjeldada funktsionaalsust kasutaja vaatenurgast
- **Näide:**
  - "Kasutajana soovin filtreerida tooteid hinna järgi, et leida sobivaim pakkumine."

---

## **Slaid 4: Stsenaariumid ja kasutaja teekond**

- **Stsenaariumid:**
  - Detailsemad lood konkreetsetest kasutusjuhtudest
- **Kasutaja teekond:**
  - Visuaalne kaart kasutaja interaktsioonidest süsteemiga
- **Eesmärk:**
  - Tuvastada kasutajakogemuse parendusvõimalusi

---

## **Slaid 5: Prototüüpimine**

- **Mis on prototüüp?**
  - Esialgne mudel toote funktsionaalsuse demonstreerimiseks
- **Tüübid:**
  - Madala truudusega (paberprototüüp)
  - Kõrge truudusega (digitaalne mudel)
- **Eelised:**
  - Kiire tagasiside
  - Vigade varajane avastamine

---

## **Slaid 6: Prototüübi loomise sammud**

- **1. Nõuete analüüs:**
  - Koguge kõik vajalikud nõuded
- **2. Visandamine:**
  - Joonistage esialgsed ekraanid ja kasutajaliidesed
- **3. Tagasiside kogumine:**
  - Esitage prototüüp kasutajatele või tiimile
- **4. Paranduste tegemine:**
  - Täiendage prototüüpi saadud tagasiside põhjal

---

## **Slaid 7: Prototüüpimise tööriistad**

- **Paber ja pliiats:**
  - Kiire ja lihtne viis ideede visualiseerimiseks
- **Digitaalsed tööriistad:**
  - **Figma**
  - **Adobe XD**
  - **Sketch**
- **Funktsioonid:**
  - Interaktiivsed prototüübid
  - Koostöö võimalused

---

## **Slaid 8: Nõuete väljaselgitamise harjutused**

- **Workshopid:**
  - Koostöö kasutajatega
- **Brainstorming:**
  - Ideede genereerimine tiimiga
- **Kasutajate tagasiside:**
  - Otsene suhtlus sihtgrupiga
- **Olulisus:**
  - Parema toote loomine
  - Kasutajakeskne arendus

---

# **Seminar 4: Dokumentatsioon ja koostöövahendid**

---

## **Slaid 1: Dokumentatsiooni tähtsus**

- **Miks dokumenteerida?**
  - Teabe säilitamine
  - Uute tiimiliikmete sisseelamine
  - Projekti hooldatavuse parandamine
- **Dokumentatsiooni tüübid:**
  - Kasutajajuhendid
  - Arhitektuuridokumendid
  - API dokumentatsioon

---

## **Slaid 2: README failide parimad praktikad**

- **Sisu:**
  - Projekti kirjeldus
  - Paigaldusjuhised
  - Kasutusjuhend
  - Autorid ja panustajad
- **Formaat:**
  - Selge ja struktureeritud
  - Markdown'i korrektne kasutamine
- **Näpunäited:**
  - Lisage ekraanipilte
  - Hoidke teave ajakohane

---

## **Slaid 3: Forkimine ja pull request'id**

- **Forkimine:**
  - Teise repositooriumi kopeerimine oma kontole
  - Võimaldab iseseisvat tööd ilma originaali mõjutamata
- **Pull request:**
  - Muudatuste ettepanek originaalrepositooriumile
- **Koostöö avatud lähtekoodiga projektides:**
  - Kaastöö tegemine
  - Kogukonna kaasamine

---

## **Slaid 4: Koodireview protsess**

- **Eesmärk:**
  - Kvaliteedi tagamine
  - Vigade leidmine
  - Teadmiste jagamine tiimis
- **Parimad praktikad:**
  - Konstruktiivne tagasiside
  - Fookus koodi, mitte isiku peale
  - Selged ja konkreetsed kommentaarid

---

## **Slaid 5: Mittefunktsionaalsed nõuded**

- **Mis need on?**
  - Süsteemi omadused, mis ei ole seotud konkreetse funktsionaalsusega
- **Näited:**
  - **Jõudlus:** Reaktsiooniajad, läbilaskevõime
  - **Turvalisus:** Andmete kaitse, autentimine
  - **Kasutatavus:** Lihtne ja intuitiivne kasutajaliides
- **Olulisus:**
  - Mõjutavad kasutajakogemust
  - Võivad määrata toote edu või ebaedu

---

## **Slaid 6: Testimine**

- **Miks testida?**
  - Vigade avastamine enne kasutajani jõudmist
  - Kvaliteedi tagamine
- **Testimise tüübid:**
  - **Üksusetestid:** Individuaalsete komponentide testimine
  - **Integreerimistestid:** Komponentide koos toimimise testimine
  - **Süsteemitestid:** Kogu süsteemi testimine reaalsetes tingimustes

---

## **Slaid 7: .gitignore fail**

- **Eesmärk:**
  - Vältida mittevajalike või tundlike failide jagamist
- **Kasutamine:**
  - Määrake failid ja kaustad, mida Git peaks ignoreerima
- **Näited:**
  - Konfiguratsioonifailid
  - Logifailid
  - Kohalikud andmebaasid

---

## **Slaid 8: Kuidas saab ideest tarkvara**

- **Protsessi etapid:**
  1. **Idee genereerimine**
  2. **Nõuete kogumine**
  3. **Disain ja prototüüpimine**
  4. **Arendus**
  5. **Testimine**
  6. **Käivitamine**
  7. **Hooldus ja täiustamine**
- **Koostöö tähtsus:**
  - Tiimitöö
  - Pidev suhtlus sidusrühmadega

---
