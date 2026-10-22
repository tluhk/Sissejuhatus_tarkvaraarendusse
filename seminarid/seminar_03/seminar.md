# Seminar 3: meeskond, tööviis ja süsteemi põhimõte

Meeskonna ühine GitHubi töövoog on kirjas [projekti töökorralduse juhendis](../../docs/projekti-tookorraldus.md).

## Eesmärk

Seminari lõpuks õppija:

- tunneb tarkvaraarenduse levinud ametialaseid rolle;
- eristab rolli ametinimetusest ja konkreetsest inimesest;
- sõnastab valideeritud vajadusest kasutajaloo ja selle kontrolltingimuse;
- võrdleb järjestikust, iteratiivset ja voopõhist tööviisi;
- valib meeskonnale sobiva tööviisi ning põhjendab valikut;
- kirjeldab süsteemi eesmärki, piiri, osalisi, suuremaid osi ja nendevahelisi seoseid kõrgtaseme arhitektuurina;
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
Töö planeerimine
  ↓
Lahenduse disainimine
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

## Päris töö rollid

Roll kirjeldab vastutust ja vaatenurka. Ühel inimesel võib väikeses meeskonnas olla mitu rolli ning sama ametinimetus võib eri organisatsioonides tähendada erinevat tööd.

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

- **Waterfall ehk kosemudel:** etapid järgnevad valdavalt üksteisele. Sobib paremini, kui tulemus ja piirangud on ette teada ning hiline muutus on kallis.
- **Agiilne lähenemine:** koostöö, sagedane tagasiside ja plaani kohandamine väikeste sammude kaupa. See ei tähenda planeerimise või dokumenteerimise puudumist.
- **Iteratiivne arendus:** lahendust täpsustatakse korduvate tsüklitega. Iga ring annab uut infot.
- **Inkrementaalne arendus:** tervik kasvab kasutatavate osade kaupa. MVP on väikseim versioon, millega saab olulist oletust kontrollida.
- **Scrum:** agiilne raamistik ajaliselt piiratud sprintide, kindlate vastutuste ja sündmustega.
- **Kanban:** töövoo meetod; nähtav töö ja poolelioleva töö hulga piiramine toetavad pidevat liikumist.
- **Lean:** keskendub väärtusele, õppimisele ja raiskamise vähendamisele.

Päris meeskond võib võtteid kombineerida. Oluline pole meetodi silt, vaid see, miks valitud töökorraldus aitab riske vähendada ja õppida.

## Pärisprojekti peegel: GOV.UK alpha

GOV.UK teenusekäsiraamatu alpha-etapis katsetatakse kõige riskantsemaid oletusi, võrreldakse variante ja välditakse ühe lahenduse liiga varast lukustamist. Alpha ei pea andma valmis teenust; see peab andma meeskonnale tõendeid järgmise otsuse jaoks.

Arutage:

1. Milline on teie projekti kõige riskantsem oletus?
2. Mida peaks kontrollima enne detailse lahenduse kavandamist?
3. Milline teie senine otsus võib uue info tõttu muutuda?

Allikas: [How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works)

## Valideeritud vajadusest kasutajaloona nõudeni

Probleem ja tõend kirjeldavad, miks muutust vaja on. **Kasutajalugu** aitab sõnastada, mida kindel kasutaja tahab teha ja miks:

Vaata vajadusel ka [kasutajaloo pikemat selgitust](../../concepts/kasutajalugu/README.md).

> Kasutajana soovin [tegevust või võimalust], et [saavutatav väärtus].

Näide: „Õppijana soovin näha lähenevaid tähtaegu ühes vaates, et saaksin oma tööd paremini järjestada.” See on funktsionaalne nõue: kirjeldab, mida süsteem peab võimaldama. Lisa iga loo juurde vähemalt üks lihtne kontrolltingimus, mille järgi saab hiljem hinnata, kas vajadus on täidetud.

Näiteks võib kontrolltingimus olla: „Tähtajad kuvatakse kuupäeva järjekorras ja iga tähtaja juures on näha kursuse nimi.”

Kasutajalugu peab lähtuma seminari 2 tõendist ja kirjeldama vajadust, mitte eeldama ette konkreetset tehnilist lahendust. Kasutajalood ei kata kõiki nõudeid; kvaliteediomadusi, nagu turvalisus ja töökindlus, käsitleme seminaris 4.

## Süsteemi kontseptsioon ja kõrgtaseme arhitektuur

Arhitektuur kirjeldab süsteemi suuremaid osi, nende vastutust ja omavahelisi seoseid. Selles kursuses teeme sellest lihtsa kõrgtaseme visandi, mitte detailset tehnilist arhitektuuri ega tehnoloogiapinu valikut. Kirjeldage piisavalt, et teine inimene mõistaks:

- süsteemi eesmärki;
- peamisi osalisi;
- mis jääb süsteemi sisse ja mis välja;
- suuremaid osi või võimekusi;
- olulist info liikumist;
- väliseid teenuseid või sõltuvusi;
- osade vastutust ja seda, kus vajalik info paikneb;
- kõige suuremaid teadmatusi.

Skeem on kasulik ainult siis, kui see selgitab mõtet. Ilus, kuid põhjendamata kastide kogum ei ole eesmärk.

## Hea commit'i sõnum

Commit on üks tähenduslik muudatuste komplekt, mitte kogu päeva juhuslik
salvestus. Hea commit:

- teeb ühe loogilise asja;
- kasutab tegusõnalist ja arusaadavat sõnumit, näiteks `Describe system boundary`;
- ei sega kokku vorminduse, ümbernimetamise ja sisulise muudatuse eri eesmärke;
- lubab hiljem ajaloost aru saada ja vajaduse korral muudatuse üle vaadata.

Seminaris 2 harjutasime commit'i tegemist. Selles seminaris seome hea sõnumi
otsuse põhjendusega ning võrdleme halba sõnumit (`update`, `fix stuff`) sisulise
sõnumiga. Commit'i hea tava ei tähenda võimalikult suurt commit'ide arvu.

## Seminari praktiline töö

1. Vaadake üle release `v0.1.0` ja nimetage üks muutunud arusaam.
2. Jagage selleks etapiks rollid. Iga õppija võtab uue vaatenurga.
3. Võrrelge vähemalt kolme tööviisi projekti ebakindluse, mahu ja meeskonna järgi.
4. Looge `decisions/002-tooviisi-valik.md`.
5. Sõnastage vähemalt kaks valideeritud vajadusest lähtuvat kasutajalugu ja lisage kummalegi kontrolltingimus.
6. Kirjeldage, kuidas lood vastavad süsteemi eesmärgile, piirile ja suurematele osadele.
7. Looge `decisions/003-susteemi-kontseptsioon.md` ning näidake süsteemi peamisi osi, nende vastutust ja vähemalt üht olulist seost või info liikumist.
8. Avage töö GitHub Issues'ena ja leppige kokku ülevaatajad.

## Kontrollpunkt

Seminari lõpuks on:

- rollid ja nende vastutus nähtavad;
- tööviisi valiku mustand koos alternatiividega;
- vähemalt kaks tõendiga seotud kasutajalugu ja nende kontrolltingimused;
- süsteemi kontseptsiooni esimene versioon;
- kõrgtaseme arhitektuuri visand või selge tekstiline kirjeldus;
- vähemalt üks lahkarvamus või kompromiss otsusena talletatud;
- igal õppijal Issue, haru ja ülevaatamise ülesanne.

## Kodutöö ja release

[Kodutöö 3: release `v0.2.0`](homework.md)
