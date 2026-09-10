---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 2 – probleemi leidmine
---

# Seminar 2

## Probleemi leidmine

Meeskonnaprojekti algus

---

# Kas tarkvaraarendus algab ideest?

---

## Tarkvaraarendus algab probleemist

Idee on üks võimalik vastus.

Enne lahenduse valimist tuleb mõista inimest, olukorda ja takistust.

---

# Kumb kirjeldab probleemi?

„Meil on vaja sööklaäppi.”

„Õppija ei tea enne sööklasse minekut, kas sobiv toit on saadaval.”

---

## Puuduv äpp ei ole probleem

Esimene väide valib lahenduse.

Teine väide jätab avatuks mitu võimalikku lahendust.

---

## Kust probleeme leida?

- korduv käsitöö
- ootamine ja viivitused
- sama info korduv sisestamine
- puudulikust infost tekkivad vead
- halvasti ühendatud kanalid
- ligipääsetavuse takistused
- ebamugavad kõrvalteed

---

## Probleemiväite struktuur

> **[Kellel]** on olukorras **[kontekst]** raske **[eesmärk]**, sest **[takistus]**. Selle tagajärg on **[mõju]**.

---

## Näide

> Õhtuses õppes osaleval õppijal on raske rühmatöö otsuseid hiljem taastada, sest need jäävad vestlustesse ja eri failidesse. Selle tagajärjel korratakse arutelusid.

See on veel oletus.

---

# Kuidas probleemi kontrollida?

---

## Kerge valideerimine

- üks lühike vestlus inimesega, kes probleemi kogeb
- või üks sõltumatu usaldusväärne andmeallikas
- meeskonna analüüs, mida uus info muutis

AI vastus ei ole probleemi olemasolu tõend.

---

## Küsi praeguse tegevuse kohta

- Räägi viimasest korrast, kui see juhtus.
- Mida sa teha püüdsid?
- Mis takistas?
- Kuidas olukorra lahendasid?
- Mis oli tagajärg?

Ära küsi: „Kas kasutaksid meie äppi?”

---

## Pärisprojekti peegel

GOV.UK discovery põhimõte:

- mõista probleemi enne ehitamist
- sõnasta ette antud lahendus ümber probleemiks
- uuri kasutajat, konteksti ja piiranguid
- discovery võib lõppeda otsusega mitte ehitada

[Allikas](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)

---

# Millal on projekti peatamine hea otsus?

---

## Kui tõend muudab arusaama

Ebaõnnestunud oletus ei ole läbikukkumine.

Kontrollimata oletuse põhjal ehitamine võib raisata palju rohkem aega.

---

## Kandidaatide võrdlemine

Hinnake 0–2:

- inimene ja olukord
- mõju
- korduvus
- kontrollitavus
- kursuse jaoks hallatav ulatus

Skoor aitab valida kontrollimise järjekorra. See ei tõesta probleemi.

---

## Individuaalne töö

Kirjuta vähemalt kolm probleemikandidaati.

Iga kandidaadi juures nimeta:

- inimene
- olukord
- takistus
- mõju
- oletus

---

## Meeskonna valik

1. Võrrelge kandidaate.
2. Valige üks probleem.
3. Dokumenteerige ka kõrvale jäetud variant.
4. Kirjutage valiku põhjendus.
5. Nimetage puuduv info.

---

# Meeskonnaprojekt GitHubis

Üks repo organisatsioonis `TLUHK-RIF26`

Kõigil liikmetel on ühine ajalugu ja eraldi nähtav panus.

---

## Clone, mitte fork

Kõik liikmed kloonivad sama meeskonnarepo.

**Clone** teeb töökoopia arvutisse. **Fork** looks GitHubis eraldi repo ja seda pole kaastöötajana vaja.

---

# Kus meeskond tööd korraldab?

## GitHub Projects

- Issue kirjeldab tööd.
- Projecti tahvel näitab olekut ja vastutajat.
- Näiteks: **Backlog → In progress → Review → Done**.

Jira ja ClickUp on samalaadsed projektihalduse tööriistad. Sellel kursusel
kasutame GitHub Projectsi.

---

# Litsents enne kasutamist

Kontrolli enne võõra koodi, pildi, fondi, andmete või AI-väljundi kasutamist:

- allikas ja litsents;
- mida tohib muuta ja jagada;
- milline viide tuleb alles jätta.

Seminaris piisab lingist, litsentsi nimetusest ja lühikesest põhjendusest.

---

## Iga õppija töövoog

```text
Issue → haru → muudatus → commit → push
→ pull request → ülevaatus → merge
```

VS Code'is muudame faili; terminalis kasutame Giti käske.

GitHub: pull request → ülevaatus → merge

---

## Tuttav põhiring uues harus

`git status` → faili salvestamine → `git add` → `git diff --cached` → `git commit` → `git push`

Kontrolli enne õiget repot ja töökataloogi.

Uue haru esimene saatmine vajab haru seostamist GitHubiga. Täpne näide on seminarijuhendis.

---

# Kaaslase PR on ühendatud. Kas minu arvutis on uus sisu?

---

## Kohalik koopia vajab uuendamist

Kui enda töö on salvestatud, commit'itud ja push'itud ning töökaust puhas:

```bash
git switch main
git pull --ff-only
```

Kui peaharu nimi on `master`, kasuta seda. Kontrolli kaaslase muudatust oma arvutis.

---

## Tag, release ja release notes

- **Tag** märgib kindla commit'i.
- **GitHub Release** avaldab selle versiooni koos kirjeldusega.
- **Release notes** selgitab muutusi, kontrolle ja lahtisi küsimusi.

Harjutame esimese release'i loomist enne kodutööd.

---

## Esimene otsus

```text
decisions/
└── 001-probleemi-valik.md
```

[Otsuse mall](../mallid/otsus.md)

---

## Otsus peab näitama mõtlemist

- probleem või uus info
- kaalutud variandid
- valik ja põhjendus
- mõju ning kompromiss
- kontrollimise viis
- otsuse muutmise tingimus

---

## Seminari kontrollpunkt

- [ ] Repo on kõigile ligipääsetav.
- [ ] Probleem on esialgselt sõnastatud.
- [ ] Otsuse mustand on repos.
- [ ] Valideerimine on jagatud Issue'deks.
- [ ] Igal liikmel on järgmine tegevus.

---

# Kodutöö

## Release `v0.1.0 – Probleem sõnastatud`

Kontrollige probleemi, täiendage otsust ja lisage individuaalsed refleksioonid.

---

## Release ei tähenda lõplikku vastust

Release näitab:

- mida teame
- mida otsustasime
- mis muutus
- mis jäi lahtiseks
- mida kontrollime järgmisena

---

## Valmis tulemus

- otsus `001-probleemi-valik.md`
- release notes `v0.1.0.md`
- iga liikme refleksioon
- iga liikme pull request ja ülevaatus
- avaldatud GitHub Release `v0.1.0`

Täielik juhend: [homework.md](homework.md)
