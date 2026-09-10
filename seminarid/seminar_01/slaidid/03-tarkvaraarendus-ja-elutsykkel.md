---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 1 – tarkvaraarendus ja elutsükkel
---

# Mis on teie arvates tarkvaraarendus?

Nüüd teame, mis on tarkvara. Kuidas see sünnib?

Paku tegevusi, mis kuuluvad tarkvaraarenduse juurde.

<!-- Õppejõule: kogu vastused tahvlile. Ära veel anna definitsiooni ega hinda vastuseid. -->

---

## Mõtle veel

- Millest tarkvara loomine algab?
- Kes peale programmeerija selles osalevad?
- Mis toimub enne koodi kirjutamist?
- Mis toimub pärast koodi valmimist?
- Kas töötav, kuid valet probleemi lahendav programm on õnnestunud tarkvara?

<!-- Õppejõule: kasuta neid küsimusi ainult siis, kui arutelu vajab käivitamist. -->

---

# „Tarkvaraarendus on koodi kirjutamine”

---

# „Tarkvaraarendus on koodi kirjutamine”

See on õige...

...aga kirjeldab ainult ühte osa tervikust.

---

## Mis on tarkvaraarendus?

Tarkvaraarendus on protsess, mille käigus:

1. uuritakse probleemi;
2. kavandatakse lahendus;
3. ehitatakse tarkvara;
4. kontrollitakse selle kvaliteeti;
5. avaldatakse ja hooldatakse tulemust.

Programmeerimine on üks nendest tegevustest.

---

## Programmeerimine on üks arendustegevus

Tarkvaraarendus hõlmab:

- probleemi ja kasutajate mõistmist;
- nõuete kirjeldamist;
- lahenduse kavandamist;
- töö planeerimist;
- programmeerimist;
- testimist, avaldamist ja hooldamist.

---

# Millest tarkvaraarendus algab?

- Koodist?
- Tehnoloogia valimisest?
- Heast ideest?
- Probleemist?

<!-- Õppejõule: küsi enne järgmisele slaidile liikumist põhjendusi. -->

---

## Arendus algab probleemi mõistmisest

Enne lahenduse ehitamist peame teadma:

- kelle probleemiga tegeleme;
- milles probleem seisneb;
- miks tasub seda lahendada;
- kuidas kasutajad praegu toime tulevad;
- mille järgi tunneme ära hea lahenduse.

---

# Kes tarkvara arendavad?

<!-- Õppejõule: lase nimetada ameteid ja inimesi, mitte ainult arendajaid. -->

---

## Arendus on meeskonnatöö

- kasutajad ja tellija;
- tooteomanik ja projektijuht;
- analüütik;
- UX/UI disainer;
- arendaja;
- testija;
- süsteemi-, andme- ja turvaspetsialistid.

Üks inimene võib täita mitut rolli.

---

# Tarkvaraarendus on meeskonnatöö

Ka siis, kui suure osa koodist kirjutab AI.

<!-- Õppejõule: see on kursuse läbiv mõte. Tuleme selle juurde tagasi AI-peatükis ja GitHubi töövoo juures. -->

---

## Miks meeskonnatöö?

- keegi peab mõistma probleemi ja kasutajaid;
- keegi peab otsustama, mida ehitada;
- keegi peab tulemust kontrollima;
- keegi peab tulemuse eest vastutama.

Ka kursuse projekt on meeskonnatöö: jagame ülesandeid, vaatame üksteise tööd üle ja lepime kokku, kuidas asju teeme.

---

## Aga AI?

AI võib:

- kirjutada koodi;
- pakkuda lahendusi;
- koostada dokumentatsiooni.

AI ei otsusta, millist probleemi lahendame, ei lepi kokku meeskonna töökorraldust ega vastuta tulemuse eest.

Need jäävad inimestele.

---

## SDLC

**SDLC** – *Software Development Life Cycle*
**Tarkvaraarenduse elutsükkel**

See kirjeldab tegevusi, mida on vaja tarkvara loomiseks ja käigus hoidmiseks.

---

## Tarkvaraarenduse elutsükkel

![height:430px Tarkvaraarenduse elutsükkel](../images/software-development-life-cycle.svg)

Joonis: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Systems_development_life_cycle.svg), CC0 1.0.

---

## Lihtsustatud etapid

1. probleem ja vajadused;
2. planeerimine ja nõuded;
3. disain;
4. arendamine;
5. testimine;
6. avaldamine;
7. kasutamine ja hooldus;
8. tagasiside ning järgmine arendusring.

---

# Kas arendus liigub alati algusest lõpuni sirgjooneliselt?

<!-- Õppejõule: palu tuua olukordi, mille tõttu tuleb varasema etapi juurde tagasi minna. -->

---

## Päris arenduses liigutakse ka tagasi

- testimine võib näidata disainiviga;
- kasutaja võib nõudest teisiti aru saada;
- tehniline lahendus võib osutuda liiga kalliks;
- turvanõue võib muuta arhitektuuri;
- kasutamise käigus tekivad uued vajadused.

Tagasiside ühendab elutsükli etapid.

---

## Kosemudel

![height:370px Kosemudeli järjestikused etapid](../images/waterfall-model.svg)

Etapid läbitakse valdavalt kindlas järjekorras.
Joonis: Paul Smith / [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Waterfall_model_(1).svg), CC BY 3.0.

---

## Iteratiivne arendus

![height:400px Iteratiivse arenduse korduv tsükkel](../images/iterative-development-model.svg)

Lahendust arendatakse, hinnatakse ja parandatakse korduvate tsüklitena.
Joonis: Aflafla1 / [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Iterative_development_model.svg), CC0 1.0.

---

## Iteratiivne ja järkjärguline

- **Iteratiivne:** tuleme sama lahenduse juurde tagasi ja parandame seda.
- **Järkjärguline ehk inkrementaalne:** lisame töötavale lahendusele uusi võimalusi.

Sageli toimuvad mõlemad korraga.

---

## Näide: ülesannete haldamise rakendus

1. ülesannete nimekiri;
2. ülesannete lisamine;
3. tähtaegade määramine;
4. meeldetuletused;
5. rühmatöö võimalused.

Iga samm lisab kasutatavale lahendusele uue osa.

---

# Kas MVP on odav ja poolik toode?

**MVP** – *Minimum Viable Product*

<!-- Õppejõule: kogu esmased reaktsioonid. Rõhuta sõna viable tähendust alles järgmisel slaidil. -->

---

## MVP on väikseim elujõuline toode

MVP on väikseim kasutatav tervik, mis:

- lahendab päris probleemi;
- aitab kontrollida olulist oletust;
- võimaldab koguda kasutajatelt tagasisidet;
- annab aluse järgmisele versioonile.

MVP ei tähenda teadlikult katkist või ebaturvalist toodet.

---

## MVP arenguring

```text
MVP
 ↓
Kasutamine
 ↓
Tagasiside
 ↓
Parandused ja uued võimalused
 ↓
Järgmine versioon
```
