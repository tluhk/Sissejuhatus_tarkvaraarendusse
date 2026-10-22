# Tarkvaraarendus algusest kasutamiseni

Tarkvaraarendus on meeskonnatöö, mille käigus mõistetakse probleemi, kavandatakse sobiv muudatus, luuakse ja kontrollitakse lahendus ning hoolitsetakse selle eest ka pärast kasutuselevõttu. Programmeerimine on sellest üks osa.

See dokument annab üldise ülevaate tavalisest tarkvaraarendusprojektist, rollidest ja otsustest. See ei ole kohustuslik 13-sammuline retsept: tegevuste järjekord ja detailsus sõltuvad projektist ning osa tööst toimub paralleelselt või kordub tagasiside tõttu.

## Protsessi suur pilt

Tarkvaraarendust võib vaadelda viie omavahel seotud tegevusena:

| Tegevus | Põhiküsimus | Tüüpiline väljund |
|---|---|---|
| Probleemi mõistmine | Miks ja kellele on muudatust vaja? | Probleemikirjeldus, kasutajate vajadused ja tõendid |
| Vajaduse määratlemine | Millist tulemust soovime ja mis kuulub ulatusse? | Eesmärgid, nõuded, ärireeglid ja piirangud |
| Lahenduse kavandamine | Kuidas lahendus võiks toimida? | Kasutajateekonnad, prototüübid ja arhitektuurilised valikud |
| Teostamine ja kontrollimine | Kuidas lahendus valmis teha ja selle kvaliteeti kontrollida? | Tarkvara, testid, ülevaatused ja dokumentatsioon |
| Kasutamine ja edasiarendus | Kas lahendus loob soovitud väärtust? | Avaldatud teenus, tagasiside, mõõtmine ja hooldus |

Sageli nimetatakse neid töid ka discovery, definition, design, delivery ja operation. Need sõnad aitavad rääkida tegevuse eesmärgist, kuid ei tähista alati ametlikke ega rangelt järjestatud projekti etappe.

## 1. Probleemi ja kasutajate mõistmine

Projekt võib alata tellija soovist, näiteks: „Haapsalu Kolledž soovib tunniplaani veebilehte kaasaegsemaks muuta.” See ütleb, mida tellija soovib muuta, aga mitte veel seda, kellel on probleem, millises olukorras see tekib ega milline tulemus oleks parem.

Meeskond uurib:

- kes teenust kasutab või selle toimimise eest vastutab;
- mida inimesed püüavad teha ja kuidas nad seda praegu teevad;
- millised takistused, vead või viivitused esinevad;
- mis on takistuste mõju kasutajale ja organisatsioonile;
- millised olemasolevad süsteemid, andmed või tööprotsessid on asjaga seotud.

Uurimiseks võib kasutada vestlusi, vaatlust, olemasolevate dokumentide ja andmete analüüsi ning tugipöördumiste või tagasiside ülevaatamist. Meetod valitakse uurimisküsimuse järgi. Näiteks intervjuu aitab kuulda inimese kogemusest; vaatlus võib näidata, kuidas inimene päriselt ülesande täidab.

Oluline on eristada tõendit ja oletust. „Õppijatel on raske tänast tunniplaani telefonist kontrollida” on kontrollimist vajav väide, kuni seda toetavad kasutajate kogemused või muud usaldusväärsed andmed. Uurimise järel võib selguda, et probleem on mujal, vajalik on töökorralduse muutus või uut tarkvara pole vaja. Probleemi uurimise peatumine sellise järeldusega ei ole läbikukkumine.

## 2. Eesmärk, ulatus ja teostatavus

Kui probleemist on piisav esmane arusaam, lepitakse kokku, mida projektiga tahetakse saavutada. Eesmärk kirjeldab soovitud muutust kasutaja või organisatsiooni jaoks, mitte lihtsalt arendatavat funktsiooni.

Meeskond selgitab:

- milline tulemus näitaks, et olukord paranes;
- milliseid kasutajaid ja kasutusolukordi projekt käsitleb;
- mida esialgne versioon sisaldab ja mida jätab välja;
- millised on tähtajad, eelarve, õiguslikud või tehnilised piirangud;
- millised riskid või sõltuvused võivad tulemust mõjutada.

Teostatavuse hindamine ei tähenda, et kogu arhitektuur peab juba valmis olema. Varakult tuleb märgata suuri riske: näiteks kas tunniplaani andmeid saab soovitud viisil kasutada või kas mõni lahendus sõltub kolmanda osapoole teenusest. Ebakindlat küsimust saab kontrollida väikese katsega enne suurema töö alustamist.

## 3. Arendusviisi valimine

Tarkvaraarenduse elutsükkel kirjeldab, milliseid töid tehakse. Arendusviis kirjeldab, kuidas neid töid korraldatakse, millal otsuseid tehakse ja kuidas tagasisidet kasutatakse.

### Waterfall ehk koskmudel

Waterfalli puhul kavandatakse töö valdavalt järjestikuste etappidena: analüüs, kavandamine, arendus, testimine ja üleandmine. Nõudeid püütakse suuremas osas täpsustada enne ehitamise algust. Selline lähenemine võib sobida, kui nõuded on stabiilsed, muudatused vajavad formaalset kooskõlastust või üleandmine eeldab põhjalikku dokumentatsiooni.

Risk tekib siis, kui algne arusaam probleemist või nõuetest on vale ning viga selgub alles hilises etapis. Muudatused pole võimatud, kuid võivad vajada rohkem ümberplaneerimist.

### Agiilne ja iteratiivne töö

Agiilses töös antakse tulemus välja väiksemate, kontrollitavate osadena. Meeskond kogub tagasisidet, õpib ja täpsustab järgmisi samme. Kõike ei pea projekti alguses üksikasjalikult teadma.

Agiilne ei tähenda plaanita tööd, dokumentatsiooni puudumist ega seda, et kvaliteeti võib hiljem kontrollida. Plaani ja dokumentatsiooni ulatus valitakse vastavalt riskidele ja vajadusele. Samuti ei ole agiilne üks kindel metoodika.

**Scrum** on kindlate rollide, sündmuste ja töövahenditega raamistik. **Kanban** aitab visualiseerida tööd ja juhtida selle liikumist. Meeskond võib kasutada ka hübriidset lähenemist, näiteks fikseeritud tähtaega ja nõudeid, kuid korraldada teostust lühikeste tagasisidetsüklitena. Tööviisi valik pole kvaliteedimärk; sobivus sõltub projektist.

Waterfalli ning agiilse arenduse põhimõtete algallikateks on [Agile Manifesto põhimõtted](https://agilemanifesto.org/principles.html) ja [Scrum Guide](https://scrumguides.org/scrum-guide.html).

## 4. Nõuete analüüs

Nõuded muudavad vajadused kirjeldusteks, mida saab kavandada, teostada ja kontrollida. Need sünnivad koostöös tellija, kasutajate, analüütikute, disainerite ja tehnilise tiimiga.

- **Funktsionaalsed nõuded** kirjeldavad, mida süsteem peab tegema. Näiteks saab õppija vaadata tunniplaani kuupäeva ja õpperühma järgi.
- **Mittefunktsionaalsed nõuded** kirjeldavad kvaliteeti ja piiranguid. Näiteks peab teenus olema kasutatav mobiilseadmes, vastama kokkulepitud ligipääsetavuse nõuetele või reageerima kindla aja jooksul.
- **Ärireeglid** kirjeldavad organisatsiooni kokkuleppeid ja otsustusloogikat.
- **Vastuvõtutingimused** kirjeldavad, kuidas kindla nõude või töö valmimist kontrollida.

Hea nõue on piisavalt selge, et eri osapooled mõistaksid seda ühtemoodi, ja piisavalt kontrollitav, et selle täitmist hinnata. Nõuded täpsustuvad sageli projekti jooksul.

### Kasutajalood

Kasutajalugu on üks viis kasutaja vajaduse ja loodava kasu lühidalt kirjeldamiseks:

> Mina kui **[kasutajaroll]** soovin **[tegevus või võimalus]**, et **[saavutatav kasu]**.

Näiteks: „Mina kui õppija soovin vaadata tänase päeva tunniplaani, et teaksin, millises ruumis järgmine tund toimub.” See on arutelu algus, mitte kogu tehniline spetsifikatsioon. Kasutajaloole saab lisada vastuvõtutingimused, mis teevad selle kontrollitavaks.

Kasutajalood pole ainus sobiv nõuete kirjeldamise viis. Tehnilisi töid, andmete korrastamist ja turvanõudeid võib olla selgem kirjeldada ülesannete, reeglite või spetsifikatsioonidena.

## 5. Kasutajakogemuse ja lahenduse kavandamine

Enne lahenduse ehitamist selgitatakse, millise teekonna kaudu kasutaja oma eesmärgini jõuab ning millist infot ja tuge ta eri sammudes vajab. Selleks võib joonistada kasutajateekonna, visandada ekraane või teha lihtsa prototüübi.

Prototüüp aitab ideed kiiresti arutada ja kasutajatega kontrollida. See ei pea olema töötav tarkvara. Testimisel vaadeldakse, kas inimene mõistab lahendust ja saab ülesandega hakkama; ei piisa ainult küsimusest, kas lahendus talle meeldib.

## 6. Arhitektuur ja tehnilised valikud

Arhitektuur kirjeldab süsteemi olulisemaid osi, nende vastutusi, seoseid ja piiranguid. See pole sama mis programmeerimiskeele või raamistiku valimine. Tehnoloogia on üks vahend, mille sobivust hinnatakse vajaduste ja piirangute järgi.

Arhitektuurilisi otsuseid mõjutavad näiteks:

- mida süsteem peab tegema ja kui palju inimesi seda kasutab;
- millised on turvalisuse, ligipääsetavuse, töökindluse ja jõudluse nõuded;
- kust tulevad andmed ning milline süsteem on nende autoriteetne allikas;
- milliste teiste teenustega peab süsteem suhtlema;
- kes lahendust hooldab ja millised on organisatsiooni tehnilised piirangud.

Kõiki detaile ei pea alguses lõplikult lukustama. Suure mõjuga või hiljem kalli otsuse risk tuleks varakult nähtavaks teha; võimalusel tehakse selle kontrollimiseks väike katse. Olulise otsuse puhul võib kasutada **ADR-i** ehk arhitektuuriotsuse kirjet: kirjeldada probleemi, kaalutud variante, valikut, põhjendust ja tagajärgi.

## 7. Tööde planeerimine

Arendusmeeskond koondab vajalikud tööd järjestatud nimekirja ehk backlog'i. See võib sisaldada kasutajalugusid, tehnilisi ülesandeid, uuringuid, kvaliteeditöid ja veaparandusi. Töö järjestamisel arvestatakse kasutajale loodavat väärtust, riske, sõltuvusi, töömahtu ja õppimisvajadust.

Ülesanded jagatakse nii väikesteks, et tiim saab nende edenemist jälgida ja tulemusi üle vaadata. Ajahinnang on esialgne; valminud töö järel saab võrrelda hinnangut tegeliku ajakuluga ja planeerimist parandada.

Kanban-tahvel teeb töövoo nähtavaks. Näiteks:

```text
Backlog → In progress → Review → Done
```

Tiim lepib kokku, millal kaart ühest seisust teise liigub, kes vastutab järgmise sammu eest ja kui palju tööd võib korraga pooleli olla. Kui üks veerg kuhjub, uuritakse takistust. GitHub Projects, Jira ja teised töövahendid aitavad seda infot korraldada; need ei asenda tiimi kokkuleppeid.

## 8. Arendus, koodi ülevaatus ja silumine

Arendajad muudavad nõuded ja kavandi töötavaks tarkvaraks. Arendustöö sisaldab ka tehnilisi valikuid, koodi ülevaatust, vigade leidmist ja koostööd teiste rollidega.

Koodi ülevaatuses kontrollib kaaslane, kas muudatus on arusaadav, sobib projekti eesmärgiga ja ei tekita ilmseid probleeme. Silumisel korratakse viga, kogutakse infot, kitsendatakse võimalikke põhjuseid, tehakse paranduse katse ning kontrollitakse, kas viga kadus ega tekitanud uut tõrget. AI võib soovitada parandusi, kuid soovitused tuleb üle vaadata ja läbi kontrollida.

## 9. Testimine ja valideerimine

Testimine ei ole ainult viimane etapp. Kontrollimine algab nõuete täpsustamisel ja jätkub arenduse, kasutuselevõtu ning hoolduse ajal.

Kasulik eristus on:

- **Verifitseerimine:** kas ehitasime lahenduse kokkulepitud nõuete järgi?
- **Valideerimine:** kas ehitasime lahenduse, mida kasutajatel ja organisatsioonil päriselt vaja on?

Kontroll võib hõlmata koodi või komponendi automaattesti, süsteemi osade koostöö kontrolli, terve kasutajateekonna läbimist, turva- ja jõudluskontrolli, ligipääsetavuse hindamist ning kasutajatega proovimist. Kõiki kontrolle ei pea tegema sama inimene ega sama tööriistaga. Tulemused ja leitud vead annavad sisendi järgmisteks parandusteks.

## 10. Kasutuselevõtt ja hooldus

Arenduskeskkonnas töötav rakendus pole automaatselt valmis päris kasutajatele. Kasutuselevõtt võib nõuda tootmiskeskkonna seadistamist, andmete laadimist, ligipääsude kontrolli, juhendamist, seiret, varundamist ja tagasipöördumise plaani.

Pärast avaldamist jälgitakse, kas teenus töötab, kas kasutajad saavad hakkama ja kas seatud eesmärgid täituvad. Hooldus sisaldab vigade parandamist, turvauuendusi, sõltuvuste jälgimist, kasutajate tuge ja teenuse töökindluse hoidmist. Edasiarenduse otsused põhinevad tagasisidel ja mõõdetud tulemustel. Vahel tuleb teenus ka asendada või kasutusest eemaldada.

## Rollid tarkvaraarenduses

Rollid kirjeldavad töö vastutusi, mitte alati eraldi ametikohti. Väiksemas tiimis võib üks inimene täita mitut rolli ja vastutus võib projekti jooksul muutuda.

| Roll | Peamine vastutus | AI võib aidata | Inimeste otsus või vastutus |
|---|---|---|---|
| Tellija või äriline omanik | Probleemi, eesmärkide ja organisatsiooni vajaduse sõnastamine | Koostada lähteülesande mustandeid ja võrrelda võimalusi | Otsustada, kas muudatus on organisatsioonile vajalik ja millist väärtust taotletakse |
| Tootejuht või tooteomanik | Toote suund, prioriteedid ja tööde järjekord | Sünteesida tagasisidet ja pakkuda prioriseerimisvariante | Valida eesmärgid ja teha väärtuse, aja ning ulatuse kompromisse |
| Projektijuht | Ajakava, vahendid, riskid, sõltuvused ja suhtlus | Koostada kokkuvõtteid ja jälgida ülesannete seisu | Lahendada inimestevahelisi kokkuleppeid ja vastutada töö korralduse eest |
| Ärianalüütik | Vajaduste, protsesside, reeglite ja vastuolude selgitamine | Koostada märkmetest mustandeid ja leida vastuolusid | Kontrollida, kas kirjeldus kajastab tegelikku vajadust ning lahendada ebaselgusi osapooltega |
| UX-uurija või disainer | Kasutajate käitumise mõistmine ja kasutajakogemuse kavandamine | Pakkuda uurimisküsimusi, kokku võtta anonüümitud materjali ja luua ideekavandeid | Otsustada, mida kasutajatelt uurida ja kuidas lahenduse kasutatavust kontrollida |
| Arhitekt | Süsteemi olulised struktuuri-, andme- ja integratsiooniotsused | Võrrelda variante ja koostada esialgseid skeeme | Kontrollida piiranguid, riske, turvalisust ja pikaajalist mõju |
| Arendaja | Tehniline teostus, veakäsitlus ja koodi kvaliteet | Luua koodi- ja testikavandeid, selgitada vigu | Kontrollida, mõista ja hooldada loodud lahendust |
| Testija või kvaliteedispetsialist | Kvaliteediriskide hindamine ja lahenduse kontrollimine | Pakkuda testjuhtumeid ja analüüsida tulemusi | Valida vajalikud kontrollid ning hinnata, mida tulemus tõendab |
| Käituse või DevOpsi eest vastutaja | Teenuse avaldamine, seire, varundamine ja töökindlus | Koostada seadistuste või seire reeglite mustandeid | Tagada sobiv ligipääs, taastatavus ja toimiv käituskorraldus |

Rollid ei pea töötama eraldi järjekorras. Arendaja, testija, analüütik ja disainer võivad olla kaasatud eri etappides, sõltuvalt otsusest ja riskist.

## AI mõju arendustööle

AI-tööriistad võivad toetada mitut arendustegevust: otsida või kokku võtta infot, luua nõuete ja kasutajalugude mustandeid, võrrelda arhitektuurivariante, kirjutada koodi, teste ja dokumentatsiooni. See võib muuta tööjaotust ja vähendada mõne rutiinse ülesande mahtu.

AI kasutamine ei tähenda, et arendusprotsess muutub automaatselt agiilseks, ega tõenda, et mõni amet kaob. Väikeses tiimis võib üks inimene AI abil täita mitut vastutust; suuremas organisatsioonis jäävad vajalikuks eri oskused ja kontrollid. Mõju sõltub ülesandest, organisatsioonist ja sellest, kuidas tulemust kontrollitakse.

Meeskonnal tuleb endiselt:

- valida õige probleem ja kontrollida kasutajavajadusi;
- leppida kokku eesmärgid, piirangud ja otsustusõigus;
- hinnata arhitektuuri, turvalisust, privaatsust ja hooldatavust;
- kontrollida AI loodud koodi, analüüsi, teste ja dokumentatsiooni;
- otsustada, kas lahendus loob lubatud väärtust.

AI võib kiirendada mustandi loomist, kuid vigane eeldus võib kiirendada ka vale lahenduse ehitamist. Tööriista kasutamisel ei sisestata sinna isikuandmeid, saladusi ega konfidentsiaalset infot, kui selleks puudub selge luba ja sobiv kaitse. Olulise otsuse puhul talletatakse AI roll, kasutatud väljund, tehtud kontroll ja inimese otsus.

## Millised dokumendid on vajalikud?

Iga etapp ei vaja eraldi dokumenti. Dokumente luuakse selleks, et toetada arutelu, otsuseid, koostööd ja hilisemat hooldust. Väikeses projektis võivad vajalikud teemad asuda mõnes lühikeses failis:

| Dokumentatsiooni rühm | Millele vastab? | Näited |
|---|---|---|
| Probleem ja eesmärgid | Miks ja kellele lahendust tehakse? | Probleemikirjeldus, kasutajate vajadused, ulatus |
| Nõuded ja kokkulepped | Mida lahendus peab tegema? | Kasutajalood, ärireeglid, vastuvõtutingimused |
| Tehnilised otsused | Kuidas lahendus üles ehitatakse ja miks? | Arhitektuuriskeem, ADR, andmemudel |
| Töö ja kvaliteet | Kuidas ülesanded liiguvad ja tulemust kontrollitakse? | Backlog, testimisjuhis, vead ja ülevaatused |
| Kasutus ja hooldus | Kuidas süsteemi käivitada ning töökorras hoida? | README, juurutus- ja taastamisjuhised |

Dokumentatsioon peab olema piisav, et töö jätkaja saaks kontekstist aru. Pikk dokument pole eesmärk omaette; ka liiga vähene või aegunud info võib muuta süsteemi hooldamise keeruliseks.

## Üks näide kogu protsessi läbimiseks

Tunniplaani veebilehe juhtumis võiks meeskond liikuda näiteks nii:

1. **Uurib soovi:** kes kasutab tunniplaani, mis eesmärgil ja millal?
2. **Kontrollib probleemi:** küsitleb õppijaid ja õppejõude, vaatleb praegust kasutust ning uurib usaldusväärseid andmeid.
3. **Sõnastab eesmärgi:** näiteks millist kasutaja tegevust soovitakse lihtsamaks teha; eesmärk peab tulema tõenditest.
4. **Määratleb ulatuse ja nõuded:** kirjeldab kasutajarühmad, vajalikud tegevused, kvaliteediootused ja piirangud.
5. **Võrdleb lahendusi:** kontrollib, kas vaja on olemasoleva lehe muutmist, andmevoo parandamist või muud lahendust.
6. **Kavandab ja hindab riske:** vaatab üle kasutajateekonna, andmeallikad, ligipääsetavuse, turvalisuse ja hooldusvajaduse.
7. **Planeerib tööd ja teostab:** järjestab väiksed ülesanded, ehitab kontrollitavaid osi ning vaatab muudatused üle.
8. **Testib ja avaldab:** kontrollib nõudeid ja kasutatavust, teeb kasutuselevõtu plaani ning avaldab sobiva muudatuse.
9. **Mõõdab ja hooldab:** uurib tagasisidet, jälgib teenuse toimimist ning otsustab järgmised parandused.

See on üks võimalik teekond, mitte ainus õige järjekord. Uus info võib tiimi viia tagasi probleemi, nõuete või arhitektuuri juurde.

## Lisalugemine

- [GOV.UK: kuidas discovery-faasis töötatakse](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)
- [GOV.UK: kasutajauuring discovery-faasis](https://www.gov.uk/service-manual/user-research/user-research-in-discovery)
- [Agile Manifesto põhimõtted](https://agilemanifesto.org/principles.html)
- [Scrum Guide](https://scrumguides.org/scrum-guide.html)
