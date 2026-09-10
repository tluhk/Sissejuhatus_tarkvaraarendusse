# Seminar 3: meeskond, tööviis ja süsteemi põhimõte

## Eesmärk

Seminari lõpuks õppija:

- tunneb tarkvaraarenduse levinud ametialaseid rolle;
- eristab rolli ametinimetusest ja konkreetsest inimesest;
- võrdleb järjestikust, iteratiivset ja voopõhist tööviisi;
- valib meeskonnale sobiva tööviisi ning põhjendab valikut;
- kirjeldab süsteemi eesmärki, piiri, osalisi ja suuremaid osi;
- osaleb GitHubis otsuse ülevaatamises.

## Põhiküsimus

> Kuidas meeskond töötab ja millist süsteemi põhimõtteliselt kavandab?

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

- **Kosemudel:** etapid järgnevad valdavalt üksteisele. Sobib paremini, kui tulemus ja piirangud on ette teada ning hiline muutus on kallis.
- **Iteratiivne arendus:** lahendust täpsustatakse korduvate tsüklitega. Iga ring annab uut infot.
- **Inkrementaalne arendus:** tervik kasvab kasutatavate osade kaupa. MVP on väikseim versioon, millega saab olulist oletust kontrollida.
- **Scrum:** töö toimub ajaliselt piiratud sprintides, kindlate vastutuste ja sündmustega.
- **Kanban:** töö liigub nähtava voo kaudu ning poolelioleva töö hulka piiratakse.
- **Lean:** keskendub väärtusele, õppimisele ja raiskamise vähendamisele.

Päris meeskond võib võtteid kombineerida. Oluline pole meetodi silt, vaid see, miks valitud töökorraldus aitab riske vähendada ja õppida.

## Pärisprojekti peegel: GOV.UK alpha

GOV.UK teenusekäsiraamatu alpha-etapis katsetatakse kõige riskantsemaid oletusi, võrreldakse variante ja välditakse ühe lahenduse liiga varast lukustamist. Alpha ei pea andma valmis teenust; see peab andma meeskonnale tõendeid järgmise otsuse jaoks.

Arutage:

1. Milline on teie projekti kõige riskantsem oletus?
2. Mida peaks kontrollima enne detailse lahenduse kavandamist?
3. Milline teie senine otsus võib uue info tõttu muutuda?

Allikas: [How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works)

## Süsteemi kontseptsioon

Selles kursuses ei kavandata detailset tehnilist arhitektuuri. Kirjeldage piisavalt, et teine inimene mõistaks:

- süsteemi eesmärki;
- peamisi osalisi;
- mis jääb süsteemi sisse ja mis välja;
- suuremaid osi või võimekusi;
- olulist info liikumist;
- väliseid teenuseid või sõltuvusi;
- kõige suuremaid teadmatusi.

Skeem on kasulik ainult siis, kui see selgitab mõtet. Ilus, kuid põhjendamata kastide kogum ei ole eesmärk.

## Seminari praktiline töö

1. Vaadake üle release `v0.1.0` ja nimetage üks muutunud arusaam.
2. Jagage selleks etapiks rollid. Iga õppija võtab uue vaatenurga.
3. Võrrelge vähemalt kolme tööviisi projekti ebakindluse, mahu ja meeskonna järgi.
4. Looge `decisions/002-tooviisi-valik.md`.
5. Kirjeldage süsteemi eesmärk, piir, osalised ja suuremad osad.
6. Looge `decisions/003-susteemi-kontseptsioon.md`.
7. Avage töö GitHub Issues'ena ja leppige kokku ülevaatajad.

## Kontrollpunkt

Seminari lõpuks on:

- rollid ja nende vastutus nähtavad;
- tööviisi valiku mustand koos alternatiividega;
- süsteemi kontseptsiooni esimene versioon;
- vähemalt üks lahkarvamus või kompromiss otsusena talletatud;
- igal õppijal Issue, haru ja ülevaatamise ülesanne.

## Kodutöö ja release

[Kodutöö 3: release `v0.2.0`](homework.md)

