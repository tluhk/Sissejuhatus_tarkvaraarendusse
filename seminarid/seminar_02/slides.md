---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 2 · kliendisoovist arendusülesandeni
---

# Seminar 2

## Kliendisoovist arendusülesandeni

> Haapsalu Kolledž soovib oma tunniplaani veebilehte muuta kaasaegsemaks.

Uurime, kelle jaoks ja miks on muutust vaja.

<!-- Õppestsenaarium. Kogu enne selgitamist paar õppijate küsimust kliendile. -->

---

## Kus oleme kursusel?

- Seminar 1: suur pilt ja töövahendite seadistamine
- **Seminar 2: kliendisoovist arendusülesandeni**
- Seminar 3: rollid, tööviisi valik ja süsteemi kontseptsioon
- Seminar 4: kvaliteet, riskid ja vastutus
- Seminar 5: kasutuselevõtt, tagasiside ja hooldus
- Eksam: dokumenteeritud protsessi esitlus release'ide ajajoonena

Projekti tulemus on dokumenteeritud arendusprotsess ja põhjendatud otsuste logi. Töötavat rakendust ega klikitavat prototüüpi ei nõuta.

---

## Meenutus: elutsükkel ja tööviis

**Probleem ja kasutajate vajadused (täna)** → nõuded → kavandamine → teostus ja kontroll → kasutuselevõtt ja hooldus

Elutsükkel näitab arenduse töid. Tööviis määrab nende korralduse:

- **Waterfall:** valdavalt järjestikused etapid ja varased kokkulepped.
- **Agiilne tööviis:** väikesed sammud, sage tagasiside ja plaani täpsustamine.

[Selgitus: elutsükkel, Waterfall ja agiilne tööviis](peatukid/01-elutsukkel-ja-tooviis.md)

---

## Miks on arenduses erinevad rollid?

Hea otsus arvestab eri vaatenurki:

- tellija ja tootejuht: eesmärk ning väärtus;
- analüütik ja UX-uurija: tööprotsess ning kasutaja vajadus;
- arhitekt ja arendaja: teostatavus ning süsteemi seosed;
- testija: tulemuse kontrollimine.

Väikeses tiimis täidab üks inimene mitut rolli. Vastutus peab olema kokku lepitud.

[Selgitus: rollid ja nende koostöö](peatukid/02-rollid-ja-vastutused.md)

---

## Soov, probleem ja lahendusidee

**Soov** ütleb, millist muutust oodatakse.
**Probleem** kirjeldab kasutaja takistust ja selle mõju.
**Lahendusidee** pakub takistuse kõrvaldamise viisi.

„Teeme mobiiliäpi” nimetab lahenduse. Enne on vaja teada, mida inimene praegu teha püüab ja mis teda takistab.

[Selgitus ja probleemiväite näide](peatukid/03-probleemi-uurimine.md)

---

## Mida me teame ja mida oletame?

- **Tõend:** inimese kirjeldatud juhtum, vaatlus või kontrollitav allikas.
- **Tõlgendus:** järeldus, mille info põhjal teeme.
- **Oletus:** väide, mille kohta meil veel kinnitust pole.

Ühe inimese kogemus annab uurimiseks vihje. Järelduse ulatus peab vastama kogutud tõenditele.

[Näide: tõendi ja oletuse eristamine](peatukid/03-probleemi-uurimine.md)

---

## Uurimine algab päris kogemusest

Palu kasutajal kirjeldada viimast tunniplaani kasutamise korda. Uuri eesmärki, takistust ja seda, kuidas ta hakkama sai.

Sellist probleemi ja kasutajate uurimist nimetatakse ka **discovery**-etapiks. Tulemus võib olla otsus senist plaani muuta.

[Intervjuuküsimused ja GOV.UK discovery näide](peatukid/03-probleemi-uurimine.md)

---

## AI aitab uurimist ette valmistada

Kasuta AI-d võimalike kasutajarühmade või uurimisküsimuste leidmiseks.

Kontrolli otsust mõjutavat väljundit inimese, vaatluse või algallikaga. AI vastus ei tõenda kasutajaprobleemi olemasolu.

Pane kirja kasutamise eesmärk, tehtud kontroll ja tegelik kasu. Hoia isikuandmed ning konfidentsiaalne info AI-tööriistast väljas.

[Juhis: AI kasutamine ja riskid](peatukid/03-probleemi-uurimine.md)

---

## Litsents annab kasutusloa

Litsents määrab, kuidas võib koodi või muud materjali kasutada, muuta ja jagada.

- Võõra materjali puhul kontrolli allikat ning tingimusi.
- Oma materjalile märgi luba ka siis, kui soovid seda tasuta jagada.

Avalik GitHubi repo üksi üldist taaskasutusluba ei anna.

[Selgitus ja näited: litsentsid](peatukid/04-litsentsid.md)

---

## Harjutus: igaühe kolm probleemikandidaati

Kirjelda iseseisvalt vähemalt kolme võimalikku tunniplaani kasutusprobleemi eri kasutajate või olukordade kaudu.

Iga kandidaadi juures näita kasutajat, eesmärki, takistust, mõju ning teadaolevat ja oletatavat infot. Hinda, mida saaks järgmisena kontrollida.

[Tööleht ja enesehindamine](peatukid/05-probleemikandidaadid.md)

<!-- 14 minutit. Esimese osa lõpuks on individuaalsed märkmed. Ühist probleemi veel ei valita. -->

---

## Tiimitöö ühises repositooriumis

Tiim kasutab üht repot organisatsioonis `TLUHK-RIF26`.
Iga liige **kloonib** sellest töökoopia enda arvutisse.

Iga õppija loob oma tööülesande ehk **Issue** ning lisab kandidaadid eraldi faili. Muudatused käivad enda haru ja kaaslase ülevaatuse kaudu.

[Alustamine: ligipääs, kloonimine ja enda Issue](peatukid/06-tiimi-toovoog.md#1-ühine-repo-ja-töökoopia)

<!-- Teise 90-minutilise osa algus. Kontrolli ligipääse enne harjutuse jätkamist. -->

---

## Kanban näitab töö seisu

GitHub Projectsis liigub Issue vastavalt töö seisule:

**Backlog → In progress → Review → Done**

Igal tööl on vastutaja, lõpetamise tingimus ja ajahinnang. Hoidke pooleliolevate tööde hulk väike ning aidake takerdunud töö lõpuni.

[Juhis: tahvel ja aja planeerimine](peatukid/06-tiimi-toovoog.md#2-enda-issue-ja-projectsi-tahvel)

---

## Enda ülesande haru

Haru eraldab sinu töö peaharust `main`.

```bash
git switch main
git pull --ff-only
git switch -c issue-12-map-problem-candidates
```

Haru nimi on kujul `issue-<number>-<short-english-description>`.
Näites on ülesande number 12.

[Käskude selgitused ja läbiv näidis](peatukid/06-tiimi-toovoog.md#3-haru-ja-tööfail)

---

## Muudatuse salvestamine

```bash
git status
git add research/mari-tamm-probleemikandidaadid.md
git diff --cached
git commit -m "Add timetable problem candidates"
```

**Commit** salvestab valitud muudatuse Giti ajalukku.
Vaata valik enne üle. Ingliskeelne sõnum algab tegusõnaga ja nimetab konkreetse muudatuse.

[Tööjuhend ja commit'i sõnumite head tavad](peatukid/06-tiimi-toovoog.md#4-commit-ja-push)

---

## Haru saatmine ja pull request

```bash
git push -u origin issue-12-map-problem-candidates
```

**Push** saadab commit'id GitHubi.
**Pull request (PR)** palub muudatuse üle vaadata ja peaharuga ühendada.

PR-i kirjeldusse lisa töö sisu ja `Closes #12`.
Määra ülevaatajaks tiimikaaslane.

[Juhis: PR-i avamine](peatukid/06-tiimi-toovoog.md#5-pull-request-ülevaatus-ja-merge)

---

## Ülevaatus ja ühendamine

Kaaslane kontrollib muudatust Issue eesmärgi järgi:

- **Approve:** töö sobib ühendamiseks.
- **Request changes:** autor parandab sama haru ja saadab uued commit'id.

Pärast heakskiitu ühendab autor PR-i peaharuga ehk teeb **merge**'i. Iga õppija vaatab üle vähemalt ühe kaaslase töö.

[Juhis: sisuline ülevaatus ja merge](peatukid/06-tiimi-toovoog.md#5-pull-request-ülevaatus-ja-merge)

---

## Kohaliku peaharu uuendamine

Kui sinu töö on salvestatud ja töökaust puhas:

```bash
git switch main
git pull --ff-only
```

**Pull** toob GitHubis ühendatud töö sinu arvutisse.
Järgmise ülesande haru loo uuendatud `main`-ist.

[Juhis: pull ja järgmise töö alustamine](peatukid/06-tiimi-toovoog.md#6-uuendamine-ja-järgmine-ülesanne)

---

## Kodutöö: kandidaatidest ühise otsuseni

1. Igaüks lõpetab oma PR-i ja kaaslase ülevaatuse.
2. Tiim võrdleb ühendatud kandidaate ning valib uuritava probleemi.
3. Igaüks osaleb probleemi kontrollimises.
4. Tiim dokumenteerib põhjendatud lähteülesande; igaüks lisab refleksiooni.

Kasuta AI-d vähemalt ühe olulise otsuse juures ja dokumenteeri väljundi kontroll.

[Kodutöö nõuded, failid ja esitamine](peatukid/07-kodutoo-ja-release.md#kodutöö-probleemist-lähteülesandeni)

---

## Esimene avaldatud versioon: `v0.1.0`

**Tag** märgib kindla commit'i.
**GitHub Release** avaldab selle versiooni koos muutuste kirjeldusega.

Kodutöö lõpus avaldab release manager versiooni **„Probleem sõnastatud”**. Release manager vahetub järgmises projektietapis.

[Juhis: tag'i valimine ja release'i avaldamine](peatukid/07-kodutoo-ja-release.md#release-v010)

<!-- Näita loomise samme näidisrepos. Tiimide päris v0.1.0 valmib kodutöö lõpus. -->

---

## Seminari lõpu kontrollpunkt

- [ ] Pääsen tiimi repole ja Projectsi tahvlile ligi.
- [ ] Mul on oma Issue, eraldi tööfail ja alustatud haru.
- [ ] Tean, kes minu PR-i üle vaatab ja kelle tööd mina kontrollin.
- [ ] Tean oma järgmist sammu kodutöös.

[Pooleli jäänud töö jätkamine ja kodutöö juhend](peatukid/07-kodutoo-ja-release.md#valmis-töö-ja-esitamine)
