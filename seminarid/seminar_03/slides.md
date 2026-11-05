---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 3 – meeskond, tööviis ja süsteemi põhimõte
---

# Seminar 3

## Meeskond, tööviis ja süsteemi põhimõte

---

## Kogu kursuse teekond: kus oleme?

Probleem → kasutajate ja vajaduste uurimine → **nõuete kirjeldamine, töö
planeerimine ja lahenduse disainimine – seminar 3** → arendamine → testimine ja
tagasiside → avaldamine ja hooldus

- seminar 1: suur pilt ja töövahendite seadistamine
- seminar 2: kliendisoovist arendusülesandeni
- **seminar 3: rollid, tööviisi valik ja süsteemi kontseptsioon**
- seminar 4: kvaliteet, riskid ja vastutus
- seminar 5: kasutuselevõtt, tagasiside ja hooldus
- eksam: dokumenteeritud protsessi esitlus release'ide ajajoonena

**Projekti tulemus:** dokumenteeritud arendusprotsess ja otsuste logi; töötavat rakendust ega klikitavat prototüüpi ei nõuta.

---

## Kuidas AI arendust muudab?

Etapid jäävad samaks. Muutub see, kes mida teeb ja kus töö kinni jääb.

[Lühijutt ja allikas](ai-native-sdlc-talk.md)

<!-- Räägi lühijutt, umbes 2 minutit. Ajakavas on selle jaoks eraldi rida. -->

---

# Kes otsustab, kuidas tarkvara tehakse?

---

## Meeskond otsustab

Eri rollid näevad sama otsuse eri mõju.

Hea otsus sünnib vaatenurkade ja tõendite võrdlemisest.

---

# Milliseid rolle mäletate seminarist 2?

---

## Täna kasutame rolle vaatenurkadena

- tootejuht või product owner
- projektijuht
- ärianalüütik
- UX-disainer ja kasutajauurija
- tarkvaraarhitekt ja arendaja
- testija või kvaliteedispetsialist
- DevOps- ja käitusspetsialist
- turbe- või andmekaitsespetsialist

<!-- Tulevikus: tooteomanik võib AI koostatud kirjeldust üle vaadata, mitte seda ise kirjutada. Samaks jääb: keegi peab otsustama ja vastutama. -->

---

## Roll ei ole inimene

Roll kirjeldab vastutust ja vaatenurka.

Ühel inimesel võib olla mitu rolli. Üks roll võib olla jagatud mitme inimese vahel.

---

# Miks me kursusel rolle vahetame?

---

## Et näha tervikut

Rollivahetus aitab mõista, miks arhitekt, disainer, arendaja ja kvaliteedispetsialist võivad sama valikut erinevalt hinnata.

---

# Kuidas muutub tõend nõudeks?

---

## Kasutajalugu seob kasutaja, tegevuse ja väärtuse

> Kasutajana soovin [tegevust või võimalust], et [saavutatav väärtus].

Näide: „Õppijana soovin näha lähenevaid tähtaegu ühes vaates, et saaksin oma tööd paremini järjestada.”

See kirjeldab funktsionaalset nõuet: mida süsteem peab võimaldama.

Näiteks kontrollime, et tähtajad kuvatakse kuupäeva järjekorras ja iga tähtaja juures on kursuse nimi.

Teie enda lood tulevad tunniplaani kohta kogutud tõenditest.

<!-- Tulevikus: AI võib koostada soovi põhjal nõuete mustandi. Samaks jääb: nõue peab lähtuma kontrollitud vajadusest. -->

---

## Kontrolli iga kasutajaloo alust

- Milline seminaris 2 kogutud tõend seda vajadust toetab?
- Kes seda vajab ja mis muutub tema jaoks?
- Millise tingimuse järgi saame hiljem aru, et nõue on täidetud?

Kasutajalugu ei ole valmis lahenduse kirjeldus ega kata kvaliteediomadusi, nagu turvalisus ja töökindlus.

---

# Milline arendusmeetod on kõige parem?

---

## Ühte alati parimat ei ole

Tööviis peab sobima probleemi, ebakindluse, piirangute ja meeskonnaga.

Meetodi nimi ei asenda põhjendust.

---

## Meenutus: Waterfall ja agiilne lähenemine

**Waterfall ehk kosemudel:** valdavalt järjestikused etapid; sobib paremini stabiilsete nõuete ja piirangute korral.

**Agiilne lähenemine:** koostöö, sagedane tagasiside ja plaani kohandamine väikeste sammude kaupa.

Agiilne ei tähenda, et plaani ega dokumentatsiooni pole.

---

## Mida teie projekti kohta küsida?

- Kui kindlad on vajadused ja nõuded?
- Kui kallis oleks hiline muutus?
- Kui kiiresti saame kasutajatelt tagasisidet?
- Milline meeskond ja aeg meil on?

---

## Meenutus: iteratiivne ja inkrementaalne

**Iteratsioon:** õpime korduva tsükliga.

**Inkrement:** tervik kasvab kasutatavate osade kaupa.

**MVP:** väikseim versioon, millega kontrollida olulist oletust.

---

## Scrum, Kanban ja Lean

- Scrum: agiilne raamistik ajaliselt piiratud sprintide ja kokkulepitud sündmustega
- Kanban: nähtav töövoog ja poolelioleva töö piiramine
- Lean: väärtus, õppimine ja raiskamise vähendamine

Võtteid võib põhjendatult kombineerida.

<!-- Tulevikus: etapid võivad liikuda kiiremini ja üleandmised automatiseeruda. Samaks jääb: tööviis peab sobima projekti riskidega. -->

---

## Pärisprojekti peegel

GOV.UK alpha:

- katseta riskantsemaid oletusi
- võrdle mitut varianti
- ära lukusta lahendust liiga vara
- kogu tõend järgmise otsuse jaoks

[Allikas](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works)

---

# Milline on teie projekti riskantseim oletus?

---

## Töö planeerimine: järgmise etapi backlog

**Backlog** on järjestatud tööde nimekiri.

- Jagage töö väikesteks Issue'deks.
- Järjestage väärtuse, riski ja sõltuvuste järgi.
- Määrake igale tööle vastutaja ja ajahinnang.
- Kasutage seminari 2 ajahinnangute võrdlusest saadud parandust.

<!-- Lühike selgitus, seejärel töötavad tiimid GitHub Projectsi tahvlil. Backlog'i olek on tahvlilt tuttav. -->

<!-- Tulevikus: AI võib enne muudatusi pakkuda kirjaliku plaani: failid, järjekord ja testid. Samaks jääb: inimene kinnitab plaani ja seab tähtsuse järjekorra. -->

---

## Süsteemi kontseptsioon ja kõrgtaseme arhitektuur

Arhitektuur näitab suuremaid osi, nende vastutust ja seoseid. Tehnoloogiapinu valimine pole eesmärk.

Seostage kontseptsioon vähemalt kahe kasutajalooga ja kirjeldage:

- eesmärk, osalised ja süsteemi piir
- kuidas kasutaja oma eesmärgini jõuab
- suuremad osad või võimekused
- oluline info liikumine
- välised sõltuvused ja teadmatused

<!-- Tulevikus: analüüs ja disain võivad toimuda ühes töösessioonis. Samaks jääb: süsteemi piiri ja kompromisse tuleb põhjendada. -->

---

# Kas süsteemikirjeldus vajab alati skeemi?

---

## Ainult siis, kui skeem aitab mõista

Selge tekst võib olla piisav.

Ilus kastide kogum ilma põhjendatud piiride ja seosteta ei ole arhitektuuriline mõtlemine.

---

## Tänane meeskonnatöö

1. Vaadake üle `v0.1.0`.
2. Vahetage rollid.
3. Võrrelge vähemalt kolme tööviisi.
4. Põhjendage valik otsuste logis.
5. Koostage Projectsi tahvlile järgmise etapi backlog.
6. Sõnastage vähemalt kaks tõendiga seotud kasutajalugu ja lisage kummalegi kontrolltingimus.
7. Kirjeldage süsteemi kontseptsioon ning seostage see kasutajalugudega.

---

## GitHubis

```text
Issue → haru → commit → PR → ülevaatus → merge
```

Üks commit on üks loogiline muudatus. Sõnum ütleb, mida muudeti, näiteks `Describe system boundary`.

Ülevaatus küsib põhjenduse, riski või alternatiivi kohta.

<!-- Tulevikus: suure osa muudatustest võib kirjutada agent. Samaks jääb: ajalugu peab näitama, mis muutus ja miks. -->

---

# Kas tööviisi võib hiljem muuta?

---

## Jah

Ka algne valik peab olema põhjendatud.

Muutus dokumenteeritakse uue info, mõju ja kompromissiga.

---

## Tuleviku küsimus

Millist tänase teema tööd võiks teha AI, kuidas tulemust kontrolliksime ja kes vastutaks?

---

# Kodutöö

## `v0.2.0 – Tööviis ja süsteemi kontseptsioon`

Iga õppija: sisuline panus, PR, ülevaatus ja refleksioon.

---

## Enne release'i

- Kas alternatiivid on nähtavad?
- Kas valik sobib meie olukorraga?
- Kas süsteemi piir on arusaadav?
- Kas backlog ja ajahinnangud näitavad tegelikku tööd?
- Kas kasutajalood lähtuvad tõendist ja väljendavad kasutaja väärtust?
- Kas rollide vaated mõjutasid otsust?
- Mis võib veel muutuda?
