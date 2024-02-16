---
marp: true
---
# Sissejuhatus tarkvaraarendusse

Martti Raavel
<martti.raavel@tlu.ee>

---

## Teine loeng

- [Meenutame eelmist loengut](../loeng_01/README.md)
- Koduste tööde tagasiside
- [.gitignore](../../../.gitignore)
- [Koodi kvaliteet](../../../concepts/koodikvaliteet/README.md)
- [Persoonad](../../../concepts/persoona/README.md)
- [Kasutajalood](../../../concepts/kasutajalugu/README.md)
- [Stsenaariumid](../../../concepts/stsenaarium/README.md)
- [Kasutaja teekond](../../../concepts/kasutajateekond/README.md)
- [Harjutus nõuete väljaselgitamiseks](files/harjutus.md)

---

## Eelmine loeng

- [Tarkvara](../../concepts/tarkvara/README.md)
- [Tarkvaraarendus](../../concepts/tarkvaraarendus/README.md)
- [Tarkvaraarenduse elutsükkel](../../concepts/SDLC/README.md)
- [Git](../../concepts/git/README.md)
- [Github](../../concepts/github/readme.md)
- [Github issue](../../concepts/githubIssue/readme.md)

---

## Kodustest töödest

---

## .gitignore

`.gitignore` on konfiguratsioonifail, mida Git kasutab, et määrata, millised failid ja kataloogid tuleks versioonihaldussüsteemist välja jätta.

---

![height:600](../../../concepts/koodikvaliteet/files/wtf.png)

---

## Koodi kvaliteet 2

Koodi kvaliteet viitab koodibaasi üldisele kvaliteedile ja hooldatavusele. See hõlmab koodi erinevaid aspekte, sealhulgas selle

- **loetavus** (*Readability*)
- **järjepidevus** (*Consistency*)
- **lihtsus** (*Simplicity*)
- **hooldatavus** (*Maintainability*)
- **töökindlus** (*Reliability*)

Kvaliteetset koodibaasi on aja jooksul lihtsam mõista, muuta ja hooldada, mis võib säästa arendusmeeskondade aega ja ressursse.

---

## Koodi loetavus (*Readability*)

Kood peaks olema kergesti loetav ja arusaadav. See peaks olema hästi struktureeritud ja organiseeritud, järjekindlate nimetamisreeglite, vahede ja taandega.

---

## Koodi järjepidevus (*Consistency*)

Kood peaks olema stiililt ja lähenemisviisilt ühtne. See hõlbustab teistel arendajatel koodi mõistmist ja muutmist.

---

## Koodi lihtsus (*Simplicity*)

Kood peaks olema lihtne ja arusaadav. See vähendab vigade tõenäosust ning muudab koodi aja jooksul muutmise ja hooldamise lihtsamaks.

---

## Hooldatavus (*Maintainability*)

Kood peaks olema aja jooksul hooldatav. See tähendab, et nõuete muutumisel peaks seda olema lihtne muuta, parandada ja värskendada.

---

## Töökindlus (*Reliability*)

Kood peaks olema töökindel ja prognoositav. See peaks töötama ootuspäraselt ja käsitlema vigu selliselt, et need ei põhjusta programmi töös tõrkeid.

---

## Kuidas koodi kvaliteeti tagada?

- Järjepidev koodi vormindamine
- Kommentaarid ja dokumentatsioon
- Ühiktestimine
- Koodiülevaatused
- Vigade käsitlemine
- Koodi refaktoreerimine

---

## Nõuete väljaselgitamine 1

Harjutame Programmeerimine I aines loodava rakenduse jaoks nõuete paikapanemist, prioritiseerimist ja disaini.

Kuidas me seda teeme?

---

## Nõuete väljaselgitamine 2

- [Persoona](../../../concepts/persoona/README.md)
- [Kasutajalood](../../../concepts/kasutajalugu/README.md)
- [Stsenaariumid](../../../concepts/stsenaarium/README.md)
- [Kasutaja teekond](../../../concepts/kasutajateekond/README.md)

---

## Persoona 1

- Näidis-kasutaja, tüüpilise lõppkasutaja arhetüüp, kes esindab konkreetset kasutajagruppi;
- Luuakse kliendi paremaks mõistmiseks – mis teda motiveerib, mis ärritab, mida ta vajab?
- Ei asenda kasutajauuringuid, vaid tugineb nendel!
- Aitab disaini loomisel silmas pidada lõppkasutaja vajadusi, nt eristada olulisi funktsionaalsusi ebaolulistest.

---

## Persoona 2

Tarkvaraarenduse ja kasutajakogemuse kujundamise kontekstis on **persoona** väljamõeldud tegelane, kes esindab teatud tüüpi kasutajat. **Persoona** luuakse uurimistöö ja andmete põhjal reaalsete kasutajate kohta ning neid kasutatakse abistamaks disaineritel ja arendajatel oma kasutajate mõistmiseks ja nende vajadustest, eesmärkidest ja käitumisest aru saamiseks.

---

## Persoona 3

**Persoona** sisaldab tavaliselt teavet kasutaja demograafia (näiteks vanus, sugu ja amet), samuti üksikasjad nende huvide, motivatsiooni ja käitumise kohta. **Persoona** võib sisaldada ka teavet kasutaja eesmärkide, pettumuste ja valupunktide kohta, samuti üksikasju nende eelistatud suhtlemismeetodite kohta tarkvara või rakendusega.

## Persoona 4

**Persoonasid** kasutatakse empaatia tekitamiseks ning disainerite ja arendajate abistamiseks, mis põhinevad kasutaja vajadustel ja eelistustel. Mõistes eri tüüpi kasutajate vajadusi ja käitumist, saavad disainerid luua liideseid ja kogemusi, mis on kohandatud nende sihtrühmale, mille tulemuseks on tarkvara, mis on kaasahaaravam, kasutatavam ja tõhusam.

---

## Persoona 5

Persoona loomiseks kogub meeskond tavaliselt teavet selliste uurimismeetodite abil nagu:

- küsitlused;
- intervjuud;
- reaalsete kasutajate vaatlus.

---

## Persoonade jaotumine

- **Proto-persoona**: ei tugine uutel uuringutel. Eesmärk on kiiresti luua visand või ülevaade olemasolevatest eeldustest!
- **Kvalitatiivne persoona**: tugineb väikesemahulistel uuringutel (nt intervjuu, vaatlus). Eesmärk on klientide süvitsi mõistmine!
- **Kvantitatiivne persoona**: tugineb laiaulatuslikel uuringutel (nt statistika, küsitlused). Eesmärk on andmete isikustamine!

---

## Kasutajalood 1

Kasutajalugu on lihtne ühelauseline tarkvararakenduse funktsiooni või funktsionaalsuse kirjeldus, mis on kirjutatud lõppkasutaja vaatenurgast. Kasutajalood on levinud tehnika, mida kasutatakse agiilses tarkvaraarenduses, et kirjeldada rakenduse nõudeid nii, et neid on lihtne mõista ja prioriteete seada.

---

## Kasutajalood 2

### Registreeritud kasutajana tahan oma parooli lähtestada, et saaksin parooli unustamise korral oma kontole tagasi juurdepääsu

---

## Kasutajalugude kirjutamisel

- **Tuvastage kasutaja**: alustage kasutaja või rolli tuvastamisest, kelle vaatenurgast lugu on kirjutatud. See võib olla konkreetne kasutaja või kasutajate rühm, kellel on sarnane vajadus.

- **Kirjeldage toimingut**. Järgmisena kirjeldage toimingut, mida kasutaja soovib teha. See peaks olema lihtne ja selge kirjeldus selle kohta, mida kasutaja teha tahab.

- **Nimetage kasu**: lõpuks märkige kasu, mida kasutaja saab selle toimingu sooritamisest. See peaks kirjeldama, miks kasutaja soovib toimingu sooritada ja mida ta loodab saavutada.

---

## Kasutajalood 3

1. Külaliskasutajana tahan, et saaksin tooteid sirvida, et leida midagi, mida osta.
2. Registreeritud kasutajana soovin, et saaksin oma ostukorvi tooteid lisada, et saaksin jälgida, mida osta tahan.
3. Registreeritud kasutajana soovin, et mul oleks võimalik oma kaupade eest tasuda, et saaksin ostu lõpule viia.
4. Registreeritud kasutajana soovin näha oma tellimuste ajalugu, et saaksin näha, mida olen varem ostnud.
5. Registreeritud kasutajana soovin, et saaksin kirjutada tootearvustusi, et saaksin oma kogemusi teiste kasutajatega jagada.
6. Registreeritud kasutajana soovin, et saaksin oma konto andmeid muuta, et saaksin oma andmed ajakohasena hoida.

---

## Stsenaarium 1

- Persoona-põhine kirjeldus toote/teenuse kasutamisest;
- Ei keskendu ärilistele või tehnoloogilistele nüanssidele ega disainile, vaid kirjeldab kasutajakogemust!
- Sisaldab:
  - tegija
  - motivatsioon
  - eesmärk või kavatsus
  - tegevus
  - tulemus või lahendus

---

## Stsenaarium 2

Tarkvara arendamisel viitab stsenaarium konkreetsele kasutusjuhtumile või olukorrale, millega kasutaja tarkvaraga suheldes võib kokku puutuda. Stsenaariume kasutatakse selleks, et kirjeldada, kuidas kasutaja tarkvaraga suhtleb ja milliseid samme nad peavad konkreetse ülesande või eesmärgi täitmiseks tegema.

---

## Stsenaarium 3

Tüüpiline stsenaarium võib sisaldada kasutaja kirjeldust, nende eesmärke või samme, mida nad peavad nende eesmärkide saavutamiseks võtma, ja kogu asjakohast teavet tarkvara või keskkonna kohta, kus seda kasutatakse.

Näiteks võib e-kaubanduse veebisaidi stsenaarium kirjeldada kasutajat, kes soovib toodet osta, sealhulgas samme, mida nad vajavad toote leidmiseks, nende ostukorvi lisamiseks ja kassas protsessi lõpuleviimiseks.

---

## Näidis-stsenaarium

| Tegija | Tiina.. |
| --- | --- |
| Motivatsioon | ..soovib õppida, kuidas oma ettevõttele ise veebileht luua |
| Eesmärk | Ta tahab leida koolitust, mis sobiks hinnalt, oleks suunatud algajatele ja toimuks sobivatel kuupäevadel |
| Tegevus | Tiina valib koolituste nimekirjast talle sobiva kategooria, milleks on IT. Seejärel sorteerib ta koolitusi hinna ja toimumisaja alusel ning tutvub nende sisuga |
| Tulemus | Ta leiab nimistust sobiva koolituse ja registreerib osalejaks |

---

## Stsenaariumi loomisel

- Väldi tehnoloogia või disaini liigset kirjeldamist – stsenaariumi eesmärk on olla disaini inspiratsiooniks, mitte fikseeringuks!
- Ära kirjelda persoonat ja tema eesmärke ülemäärase detailsusega, keskendu vaid olulisele!

---

## Kasutaja teekond 1

- Alternatiiv / laiendus stsenaariumile, loob tervikliku ülevaate kasutajakogemusest.
- Esmalt määratakse persoona ja stsenaarium, samuti eesmärgid.
- Teisena on kaardistuse keskmes kogemuse visualiseering, mis jaotatakse mitmeks etapiks.
- Kolmanda osa moodustavad tähelepanekud ja võimalused edasiseks ning vastutajad.

---

## Kasutaja teekond 2

Kasutaja teekond, mida tuntakse ka kui kasutaja teekonnakaarti või kliendi teekonnakaarti, on tööriist, mida kasutatakse tarkvaraarenduses, et visualiseerida kasutaja kogemus toote või teenusega suheldes. See on sisuliselt kasutaja kogemuste samm-sammuline kaart, alates kasutaja esialgsest teadlikkusest tootest või teenusest, sellega suhtlemisest ja lõpuks otsuseni kasutamise jätkamisest või selle lõpetamisest.

---

## Tüüpiliselt võib sisaldada järgmiseid etappe

- **Teadlikkus**: kasutaja saab tootest või teenusest teada reklaami, sotsiaalmeedia või suusõnalise info kaudu.
- **Uuringud**: kasutaja viib läbi uuringuid toote või teenuse kohta lisateabe saamiseks, sealhulgas arvustusi lugedes, veebisaiti külastades või videot vaadates.
- **Registreerumine või ost**: kasutaja otsustab toote või teenuse kasutamise.
- **Onboarding**: kasutajat juhendatakse toote või teenuse kasutusele võtmisel.
- **Kasutamine**: kasutaja kasutab toodet või teenust regulaarselt, puutudes kokku kasutajakogemust paremaks muutvate omaduste ja funktsionaalsutega.
- **Tugi**: kasutajal võib tekkida toodete või teenusega probleeme või probleeme ning otsib arendaja või tugimeeskonna tuge.
- **Uuendamine või katkestamine**: kasutaja otsustab, kas jätkata toote või teenuse kasutamist, tellimuse uuendamist või kasutamise katkestamist.

---

## Kasutaja teekond 3

Kaardistades kasutaja teekonna sel viisil, saavad tarkvaraarendajad ja disainerid tuvastada valdkonnad, kus saab parandada kasutajakogemust, näiteks lihtsustades *onboardingu* protsessi, täiustades toote funktsioone või pakkudes paremat tuge.

---

## Moodustame grupid (võib ka individuaalselt)

[Harjutus](harjutus.md)

---

## Kodune töö

- [ESLint](../../../concepts/eslint/README.md) rakendamine Programmeerimine I kodutöödes
