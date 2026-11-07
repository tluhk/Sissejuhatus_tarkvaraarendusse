# Seminar 3: meeskond, tööviis ja süsteemi põhimõte

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](../../docs/projekti-tookorraldus.md).

## Eesmärk

Seminari lõpuks õppija:

- tunneb tarkvaraarenduse levinud ametialaseid rolle;
- eristab rolli ametinimetusest ja konkreetsest inimesest;
- sõnastab valideeritud vajadusest kasutajaloo ja selle kontrolltingimuse ([näide](#näide-tõendist-kasutajalooni));
- võrdleb Waterfalli, iteratiivset ja agiilset tööviisi;
- valib meeskonnale sobiva tööviisi ning põhjendab valikut;
- koostab järgmise etapi backlog'i ning kasutab ajahinnangu võrdlusest saadud õppetundi;
- teab, kuidas kirjeldada süsteemi eesmärki, piiri, osalisi, suuremaid osi ja nendevahelisi seoseid kõrgtaseme arhitektuurina, ning teeb selle kodutöös;
- osaleb GitHubis otsuse ülevaatamises.

## Põhiküsimus

> Kuidas meeskond töötab ja millist süsteemi põhimõtteliselt kavandab?

## Kogu kursuse teekond ja meie koht

Kursusel vaatame tarkvaraarendust tervikuna:

```text
Probleem
  ↓
Kasutajate ja vajaduste uurimine
  ↓
Nõuete kirjeldamine  ← seminar 3: täpsustame vajadused kasutajalugudeks
  ↓
Töö planeerimine  ← seminar 3: koostame backlog'i
  ↓
Lahenduse disainimine  ← seminar 3: kirjeldame süsteemi kontseptsiooni
  ↓
Arendamine
  ↓
Testimine ja tagasiside
  ↓
Avaldamine ja hooldus
```

Seminar 3 seob valideeritud probleemi nõuete, töökorralduse ja süsteemi kontseptsiooniga.

- seminar 1: suur pilt ja töövahendite seadistamine;
- seminar 2: kliendisoovist arendusülesandeni;
- seminar 3: rollid, tööviisi valik ja süsteemi kontseptsioon;
- seminar 4: kvaliteet, riskid ja vastutus;
- seminar 5: kasutuselevõtt, tagasiside ja hooldus;
- eksam: dokumenteeritud protsessi esitlus release'ide ajajoonena.

Projekti tulemus on dokumenteeritud arendusprotsess ja otsuste logi; töötavat rakendust ega klikitavat prototüüpi ei nõuta.

## Kuidas AI arendust muudab?

Elutsükli etapid jäävad samaks, kuid muutub see, kes mida teeb ja kus töö kinni jääb. Loe [lühijuttu ja selle allikat](ai-native-sdlc-talk.md). Seminarides 3–5 küsime iga teema juures: millist tööd võiks teha AI, kuidas tulemust kontrollime ja kes vastutab?

## Päris töö rollid

Seminaris 2 nägime rolle tunniplaani näitel. Nüüd kasutame neid otsuste hindamisel. Roll kirjeldab vastutust ja vaatenurka. Ühel inimesel võib väikeses meeskonnas olla mitu rolli ning sama ametinimetus võib eri organisatsioonides tähendada erinevat tööd.

| Roll | Põhiküsimus |
|---|---|
| Tootejuht või product owner | Millist väärtust ja kellele loome? |
| Projektijuht | Kuidas hoiame töö, aja ja sõltuvused juhitavana? |
| Ärianalüütik | Mida on vaja mõista ja millised vajadused peavad olema täidetud? |
| UX-disainer või kasutajauurija | Kuidas inimene olukorda kogeb ja lahendust kasutab? |
| Tarkvaraarhitekt | Millised süsteemi osad ja piirid võimaldavad eesmärki täita? |
| Tarkvaraarendaja | Kuidas kavand teostatavaks tarkvaraks muuta? |
| Testija või kvaliteedispetsialist | Kuidas saame teada, et tulemus on piisavalt hea? |
| DevOps- või käitusspetsialist | Kuidas lahendus kasutusele jõuab ja töökindlana püsib? |
| Turbe- või andmekaitsespetsialist | Milliseid ohte, õigusi ja kohustusi peame arvestama? |

Kursuse meeskonnas rolle vahetatakse. Roll ei anna ainuotsustusõigust: see sunnib meeskonda vaatama sama otsust eri külgedest.

## Tööviisid ei ole usutunnistused

Mõisteid tutvustasime seminaris 1. Nüüd võrdleme, milline tööviis sobib just teie projektile.

- **Waterfall ehk kosemudel:** etapid järgnevad valdavalt üksteisele. Sobib paremini, kui tulemus ja piirangud on ette teada ning hiline muutus on kallis.
- **Agiilne lähenemine:** koostöö, sagedane tagasiside ja plaani kohandamine väikeste sammude kaupa. See ei tähenda planeerimise või dokumenteerimise puudumist.
- **Iteratiivne arendus:** lahendust täpsustatakse korduvate tsüklitega. Iga ring annab uut infot.
- **Inkrementaalne arendus:** tervik kasvab kasutatavate osade kaupa. MVP on väikseim versioon, millega saab olulist oletust kontrollida.
- **Scrum:** agiilne raamistik ajaliselt piiratud sprintide, kindlate vastutuste ja sündmustega.
- **Kanban:** töövoo meetod; nähtav töö ja poolelioleva töö hulga piiramine toetavad pidevat liikumist.
- **Lean:** keskendub väärtusele, õppimisele ja raiskamise vähendamisele.

Päris meeskond võib võtteid kombineerida. Oluline pole meetodi silt, vaid see, miks valitud töökorraldus aitab riske vähendada ja õppida.

Kursus paneb paika release'id, töövoo ja rollivahetuse. Tiim valib, kuidas töö etapi sees käib: kuidas ja kui tihti planeerite, kuidas tööd jagate, kui palju on korraga pooleli ja kuidas muudate plaani.

## Pärisprojekti peegel: GOV.UK alpha

GOV.UK teenusekäsiraamatu alpha-etapis katsetatakse kõige riskantsemaid oletusi, võrreldakse variante ja välditakse ühe lahenduse liiga varast lukustamist. Alpha ei pea andma valmis teenust; see peab andma meeskonnale tõendeid järgmise otsuse jaoks.

Arutage:

1. Milline on teie projekti kõige riskantsem oletus?
2. Mida peaks kontrollima enne detailse lahenduse kavandamist?
3. Milline teie senine otsus võib uue info tõttu muutuda?

Allikas: [How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works)

## Probleemist kontseptsioonini

Kasutajalood ja süsteemi kontseptsioon ei sünni eraldi. Mõlemad tulevad valideeritud probleemist:

```text
v0.1.0 probleem + tõendid
   ↓
kasutaja teekond: kuidas kasutaja praegu eesmärgini jõuab, kus takerdub
   ↓
kasutajalood: üks või mitu lugu igale sammule, kus probleem esineb
   ↓
kontseptsioon: osad, piir, info liikumine ja sõltuvused, mis on vajalikud,
et need lood saaksid täidetud
```

Teekond on sild probleemi ja lugude vahel. Kontseptsioon koondab lood süsteemiks. Töö käib edasi-tagasi: kui kontseptsiooni kirjutades selgub uus sõltuvus, võib sellest tekkida uus lugu või lahtine küsimus.

**Kui palju lugusid on vaja?** Kontseptsioon kirjeldab kogu süsteemi üldiselt. Kasutajalood katavad ainult neid teekonna samme, kus probleem esineb. Kogu rakendust ei pea lugudega katma.

Kontrollige:

1. Kas igal teekonna sammul, kus probleem esineb, on vähemalt üks lugu?
2. Kas iga lugu on seotud mõne teekonna sammuga? Kui ei ole, on see tõenäoliselt lahendusidee või hoopis teise probleemi lugu.
3. Kas iga kontseptsiooni osa on vajalik mõne loo või sõltuvuse jaoks? Kui ei ole, on see üleliigne või jääb süsteemi piirist välja.

Terviklik näide on failis [Näidis: probleemist kasutajalugudeni](user-stories-example.md).

## Valideeritud vajadusest kasutajaloona nõudeni

Probleem ja tõend kirjeldavad, miks muutust vaja on. **Kasutajalugu** aitab sõnastada, mida kindel kasutaja tahab teha ja miks:

Vaata vajadusel ka [kasutajaloo pikemat selgitust](../../concepts/kasutajalugu/README.md) ja [tunniplaani näidet](#näide-tõendist-kasutajalooni).

> Kasutajana soovin [tegevust või võimalust], et [saavutatav väärtus].

Näide: „Õppijana soovin näha lähenevaid tähtaegu ühes vaates, et saaksin oma tööd paremini järjestada.” See on funktsionaalne nõue: kirjeldab, mida süsteem peab võimaldama. Lisa iga loo juurde vähemalt üks lihtne kontrolltingimus, mille järgi saab hiljem hinnata, kas vajadus on täidetud.

Näiteks võib kontrolltingimus olla: „Tähtajad kuvatakse kuupäeva järjekorras ja iga tähtaja juures on näha kursuse nimi.”

### Näide: tõendist kasutajalooni

See näide on väljamõeldud. Teie lood peavad lähtuma teie tiimi kogutud tõenditest.

> **Tõend:** vestlustes ei saanud kasutajad aru, millal plaani viimati uuendati.
>
> **Kasutajalugu:** Tudengina soovin näha, millal mu rühma tunniplaani viimati uuendati, et teaksin, kas saan selle põhjal oma päeva planeerida.
>
> **Kontrolltingimus:** iga rühma plaani juures on näha viimase uuenduse kuupäev ja kellaaeg.

Halb näide: „Tudengina soovin mobiilirakendust, et tunniplaan oleks moodsam.” See eeldab lahenduse ette ega ütle, millist vajadust see täidab. Selle kohta ei saa ka kontrolltingimust kirjutada.

Terviklik näide probleemist kasutaja teekonna, mitme loo ja kattuvate lugude ühendamiseni on failis [Näidis: probleemist kasutajalugudeni](user-stories-example.md).

Kasutajalugu peab lähtuma seminari 2 tõendist ja kirjeldama vajadust, mitte eeldama ette konkreetset tehnilist lahendust. Kasutajalood ei kata kõiki nõudeid; kvaliteediomadusi, nagu turvalisus ja töökindlus, käsitleme seminaris 4.

## Töö planeerimine

**Backlog** on järjestatud nimekiri töödest, mida meeskond peab tegema. Teie GitHub Projectsi tahvlil on see olek `Backlog`. Hea backlog aitab otsustada, mida teha järgmisena ja mis võib oodata.

1. Jagage järgmise etapi töö väikesteks Issue'deks.
2. Järjestage need väärtuse, riski ja sõltuvuste järgi.
3. Määrake igale Issue'le vastutaja ja ajahinnang.
4. Vaadake seminari 2 kodutöös märgitud parandust: mida eelmisel korral hinnates arvestamata jätsite?

Ajahinnang on esialgne. Etapi lõpus võrdlete seda tegeliku ajakuluga ja märgite ühe paranduse järgmiseks etapiks.

## Süsteemi kontseptsioon ja kõrgtaseme arhitektuur

Süsteemi kontseptsioon on lühike kirjeldus sellest, mis süsteem see on, kellele see on mõeldud ja kuidas see põhimõtteliselt töötab. See ütleb, mida süsteem teeb, kuid mitte seda, millega see ehitatakse või kuidas see välja näeb.

Arhitektuur kirjeldab süsteemi suuremaid osi, nende vastutust ja omavahelisi seoseid. Selles kursuses teeme sellest lihtsa kõrgtaseme visandi, mitte detailset tehnilist arhitektuuri ega tehnoloogiapinu valikut. Kirjeldage piisavalt, et teine inimene mõistaks:

- süsteemi eesmärki;
- peamisi osalisi;
- mis jääb süsteemi sisse ja mis välja;
- kuidas kasutaja oma eesmärgini jõuab, kirjeldatuna lühidalt tekstina;
- suuremaid osi või võimekusi;
- olulist info liikumist (kodutöös valikuline, annab punkte);
- väliseid teenuseid või sõltuvusi;
- osade vastutust ja seda, kus vajalik info paikneb;
- kõige suuremaid teadmatusi.

Kontseptsiooni osad tulenevad kasutajalugudest ja sõltuvustest, vt [Probleemist kontseptsioonini](#probleemist-kontseptsioonini).

Skeem on kasulik ainult siis, kui see selgitab mõtet. Ilus, kuid põhjendamata kastide kogum ei ole eesmärk.

## Hea commit'i sõnum

Commit'i häid tavasid harjutasime seminaris 2. Kasutage neid nüüd otsuste töös: üks commit teeb ühe loogilise muudatuse ja sõnum ütleb, mida muudeti, näiteks `Describe system boundary`. Sõnumist `update` või `fix stuff` ei saa hiljem aru, miks otsus muutus. Commit'ide arv ei ole eesmärk. Täpsemad tavad ja näited on [commit'i sõnumite juhendis](../../concepts/commit/README.md).

## Merge-konflikt

Seni töötas igaüks oma failis. Nüüd kirjutate ühiseid otsusefaile, nii et kaks haru võivad muuta sama rida. Siis tekib merge-konflikt: Git ei tea, kumb muudatus jätta, ja otsuse teeb inimene. Täpsed käsud on [konfliktide lahendamise juhendis](../../concepts/mergeConflict/README.md).

## Seminari praktiline töö

1. Vaadake üle oma tiimi release `v0.1.0` (`https://github.com/TLUHK-RIF26/tiim-XX-tunniplaan/releases/tag/v0.1.0`, `XX` asemel tiimi number). Mis muutus teie arusaamas kasutaja probleemist, kui sellega kodutöös tegelesite? Nimetage üks asi.
2. Jagage selleks etapiks rollid. Iga õppija võtab uue vaatenurga. Vaja on vähemalt nelja rolli:
   - **projektijuht** – keegi peab vastutama kogu protsessi eest;
   - **release manager** – keegi peab release'i tegema;
   - **disainer** – vastutab süsteemi kontseptsiooni ja disaini põhimõtete eest;
   - **arhitekt** – mängib läbi, millistest osadest lahendus koosneb ja milline tehnoloogiline lahendus võiks sobida.

   Suuremas meeskonnas võib lisada tootejuhi (product owner) rolli. Väikeses meeskonnas võib ühel õppijal olla kaks rolli. Kirjutage rollid ja vastutajad README-sse.
3. Võrrelge vähemalt kolme tööviisi projekti ebakindluse, mahu ja meeskonna järgi.
4. Looge `decisions/002-tooviisi-valik.md`.
5. Koostage GitHub Projectsi tahvlile järgmise etapi backlog: Issue'd, järjekord, vastutajad ja ajahinnangud. Leppige kokku ka ülevaatajad.
6. Kirjeldage, kuidas kasutaja oma eesmärgini jõuab.
7. Iga tiimiliige sõnastab tunniplaani kohta kogutud tõendite põhjal vähemalt ühe kasutajaloo koos kontrolltingimusega ja vaatab läbi ühe kaaslase loo ([näide](#näide-tõendist-kasutajalooni)). Kokku on tiimil vähemalt kaks lugu.
8. Tekitage ja lahendage üks merge-konflikt terminalis.

Kasutaja teekond ja kasutajalood lähevad faili `decisions/003-susteemi-kontseptsioon.md`. Iga õppija lisab oma loo enda PR-iga; nii tekib ühises failis ka merge-konflikt. Kontseptsiooni ja lahendussuunad lisate samasse faili kodutöös.

## Kontrollpunkt

Seminari lõpuks on:

- rollid ja nende vastutus nähtavad;
- tööviisi valiku mustand koos alternatiividega;
- igal tiimiliikmel vähemalt üks tõendiga seotud kasutajalugu koos kontrolltingimusega ([näide](#näide-tõendist-kasutajalooni)), kokku vähemalt kaks;
- kasutaja teekond tekstina;
- järgmise etapi backlog koos järjekorra, vastutajate ja ajahinnangutega;
- vähemalt üks lahkarvamus või kompromiss otsusena talletatud;
- üks merge-konflikt lahendatud;
- igal õppijal Issue, haru ja ülevaatamise ülesanne.

## Kodutöö ja release

[Kodutöö 3: release `v0.2.0`](homework.md)
