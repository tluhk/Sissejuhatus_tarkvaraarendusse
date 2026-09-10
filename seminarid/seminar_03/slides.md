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

# Kes otsustab, kuidas tarkvara tehakse?

---

## Meeskond otsustab

Eri rollid näevad sama otsuse eri mõju.

Hea otsus sünnib vaatenurkade ja tõendite võrdlemisest.

---

# Milliseid rolle te tarkvaraarenduses teate?

---

## Levinud rollid

- tootejuht või product owner
- projektijuht
- ärianalüütik
- UX-disainer ja kasutajauurija
- tarkvaraarhitekt ja arendaja
- testija või kvaliteedispetsialist
- DevOps- ja käitusspetsialist
- turbe- või andmekaitsespetsialist

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

# Milline arendusmeetod on kõige parem?

---

## Ühte alati parimat ei ole

Tööviis peab sobima probleemi, ebakindluse, piirangute ja meeskonnaga.

Meetodi nimi ei asenda põhjendust.

---

## Kosemudel

Etapid järgnevad valdavalt üksteisele.

Sobib paremini, kui tulemus ja piirangud on ette teada ning hiline muutus on kallis.

---

## Iteratiivne ja inkrementaalne

**Iteratsioon:** õpime korduva tsükliga.

**Inkrement:** tervik kasvab kasutatavate osade kaupa.

**MVP:** väikseim versioon, millega kontrollida olulist oletust.

---

## Scrum, Kanban ja Lean

- Scrum: ajaliselt piiratud sprindid ja kokkulepitud sündmused
- Kanban: nähtav töövoog ja poolelioleva töö piiramine
- Lean: väärtus, õppimine ja raiskamise vähendamine

Võtteid võib põhjendatult kombineerida.

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

## Süsteemi kontseptsioon

Kirjeldage:

- eesmärk ja osalised
- süsteemi piir
- suuremad osad või võimekused
- oluline info liikumine
- välised sõltuvused
- teadmatused

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
5. Kirjeldage süsteemi kontseptsioon.

---

## GitHubis

```text
Issue → haru → commit → PR → ülevaatus → merge
```

Ülevaatus küsib põhjenduse, riski või alternatiivi kohta.

---

# Kas tööviisi võib hiljem muuta?

---

## Jah

Ka algne valik peab olema põhjendatud.

Muutus dokumenteeritakse uue info, mõju ja kompromissiga.

---

# Kodutöö

## `v0.2.0 – Tööviis ja süsteemi kontseptsioon`

Iga õppija: sisuline panus, PR, ülevaatus ja refleksioon.

---

## Enne release'i

- Kas alternatiivid on nähtavad?
- Kas valik sobib meie olukorraga?
- Kas süsteemi piir on arusaadav?
- Kas rollide vaated mõjutasid otsust?
- Mis võib veel muutuda?

