# Seminar 2: probleemi leidmine

## Eesmärk

Seminari lõpuks oskab õppija:

- eristada probleemi lahendusideest;
- leida probleeme inimeste tegevusest ja tööprotsessidest;
- võrrelda probleemikandidaate;
- kavandada kerge valideerimise;
- põhjendada meeskonna probleemivalikut;
- teha meeskonnatööd GitHubi Issue, haru ja pull request'i kaudu.

Kursus ei asenda kasutajauuringu ainet. Siin harjutame põhimõtet, et tarkvara arendamine algab kontrollimist vajavast probleemist.

## Põhiküsimus

> Kas tegeleme päris ja olulise probleemiga?

## Probleem ei ole puuduv rakendus

Nõrk algus:

> Meil on vaja sööklaäppi.

Probleemist lähtuv algus:

> Õppija ei tea enne sööklasse minekut, kas tema vajadustele sobiv toit on veel saadaval.

Esimene väide nimetab lahenduse. Teine kirjeldab inimest, olukorda ja takistust. Ühele probleemile võib olla mitu tarkvaralist või mittetarkvaralist lahendust.

## Kust probleeme leida?

Otsi olukordi, kus inimene:

- teeb korduvalt käsitööd;
- ootab põhjendamatult kaua;
- sisestab sama infot mitu korda;
- teeb puuduliku info tõttu vigu;
- kasutab ühe tegevuse jaoks mitut halvasti ühendatud kanalit;
- ei saa teenust kasutada ligipääsetavuse või oskuste tõttu;
- peab süsteemi piirangu tõttu looma ebamugava kõrvaltee.

Alusta tegevuse vaatlemisest. Ära alusta küsimusest „millise äpi võiksime teha?”.

## Esialgne probleemiväide

Kasuta struktuuri:

> **[Kellel]** on olukorras **[kontekst]** raske **[eesmärk]**, sest **[takistus]**. Selle tagajärg on **[mõju]**.

Näide:

> Õhtuses õppes osaleval õppijal on raske rühmatöö otsuseid hiljem taastada, sest need jäävad vestlustesse ja eri failidesse. Selle tagajärjel korratakse arutelusid ning varasemate valikute põhjused kaovad.

Probleemiväide on oletus, mitte veel tõestatud fakt.

## Probleemikandidaatide võrdlemine

Hinnake iga kandidaati skaalal 0–2:

| Küsimus | 0 | 1 | 2 |
|---|---|---|---|
| Kas inimene ja olukord on selged? | ei | osaliselt | jah |
| Kas mõju on märgatav? | teadmata | väike | oluline |
| Kas probleem kordub? | teadmata | harva | sageli |
| Kas saame seda kontrollida? | raske | võimalik | lihtne |
| Kas teema on kursuse jooksul hallatav? | ei | ebakindel | jah |

Kõrge skoor ei tõesta probleemi. See aitab otsustada, mida esimesena kontrollida.

## Kerge valideerimine

Valideerimise eesmärk on otsida sõltumatut infot, mis võib oletust kinnitada, täpsustada või ümber lükata.

Selle kursuse minimaalne kontroll on:

- vähemalt üks lühike vestlus inimesega, kes probleemi kogeb, **või**
- üks usaldusväärne andmeallikas koos selgitusega, kuidas see probleemi puudutab;
- lisaks meeskonna ühine analüüs, mida tõend muutis.

Ära küsi: „Kas sa kasutaksid meie äppi?”. Küsi praeguse tegevuse kohta:

- Räägi viimasest korrast, kui see juhtus.
- Mida sa siis teha püüdsid?
- Mis takistas?
- Kuidas sa olukorra lahendasid?
- Mis oli selle tagajärg?

Ära kogu tervise-, finants- ega muud tundlikku infot, mida ülesanne ei vaja.

## Pärisprojekti peegel: GOV.UK discovery

GOV.UK teenusekäsiraamat ütleb, et enne teenuse ehitamist tuleb mõista probleemi, kasutajat, konteksti ja piiranguid. Eelnevalt ette antud lahendus soovitatakse sõnastada ümber probleemiks. Discovery etapis ei alustata veel teenuse ehitamist.

Arutage:

1. Miks võib ette antud lahendus varjata tegelikku probleemi?
2. Millal oleks õige projekt pärast probleemi uurimist peatada?
3. Millist piirangut peab teie meeskond kontrollima?

Allikad:

- [How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)
- [User research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery)

## Meeskonnaprojekti alustamine

Projektirepositoorium asub organisatsioonis `TLUHK-RIF26`. Igal meeskonnal on üks repo.

Kõik liikmed kloonivad sama repo. Fork'i ei tehta, sest õppijad on selle ühise repo kaastöötajad. **Clone** loob repo töökoopia arvutisse; **fork** looks GitHubis eraldi repo, mida kasutatakse tavaliselt siis, kui algsesse reposse pole kirjutamisõigust.

Esimesed Issue'd:

1. iga liikme probleemikandidaadid;
2. kandidaatide võrdlus;
3. probleemivaliku otsus;
4. kerge valideerimine;
5. release `v0.1.0`.

Iga õppija teeb vähemalt ühe sisulise commit'i, avab pull request'i ja vaatab üle vähemalt ühe teise õppija muudatuse.

### Esimene meeskonnatöövoog VS Code'is

1. Klooni meeskonna repo käsuga **Git: Clone**.
2. Ava enda GitHub Issue ja võta see enda vastutusele.
3. Vali VS Code'i allservas haru nimi ning loo haru `issue-number-luhikirjeldus`.
4. Muuda faili ja vaata Source Control vaates muudatus üle.
5. Tee tähendusliku sõnumiga commit.
6. Vali **Publish Branch** või **Push**.
7. Ava GitHubis pull request ja seo see Issue'ga, näiteks `Closes #3`.
8. Määra ülevaatajaks teine meeskonnaliige.
9. Ülevaataja kommenteerib sisu ja valib **Approve** või **Request changes**.
10. Pärast vajalikku parandust ühendatakse PR peaharusse.

Kui samm ei tööta, ärge tehke sama faili muudatusi peaharus. Tehke tõrkest kuvatõmmis või kopeerige veateade Issue kommentaari ja küsige abi.

## Seminari praktiline töö

1. Kirjuta individuaalselt vähemalt kolm probleemikandidaati.
2. Sõnasta need probleemina, mitte lahendusena.
3. Võrrelge meeskonnas kandidaate.
4. Valige kontrollimiseks üks probleem.
5. Looge esimene otsus faili `decisions/001-probleemi-valik.md`.
6. Kirjeldage, millist infot valiku tegemiseks veel vajate.
7. Jagage valideerimise tegevused GitHub Issues'ena.

## Kontrollpunkt

Seminari lõpuks on:

- meeskonna repo kõigile ligipääsetav;
- valitud probleem esialgselt sõnastatud;
- otsuse mustand repos;
- valideerimise plaan ja vastutajad Issues'ena;
- igal õppijal järgmine tegevus teada.

## Kodutöö ja release

[Kodutöö 2: release `v0.1.0`](homework.md)

Kodutöö lõpetab probleemi kerge valideerimise ja esimese release'i. Release võib jätta küsimusi avatuks, kuid peab näitama, mida meeskond teab ja mida veel ei tea.
