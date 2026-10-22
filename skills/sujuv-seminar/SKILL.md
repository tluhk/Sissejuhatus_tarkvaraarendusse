---
name: sujuv-seminar
description: Koosta või toimeta kursuse Sissejuhatus tarkvaraarendusse seminari õppematerjalid kinnitatud seminar_02-sujuv eeskujul. Loo kokkuvõtvad Marp-slaidid ning neid avavad selged peatükid, praktiline töö ja kodutöö ühe läbiva järjekorrana.
---

# Sujuv seminar

Loo algajale arusaadav eestikeelne seminar, mille keskne fail on `slides.md`. Slaidilt avanev peatükk peab andma näite, põhjenduse või tööjuhise, mida slaidil pole. Kinnitatud eeskuju on selle kursuserepo `seminarid/seminar_02-sujuv/`.

## Lähtematerjal ja ulatus

Tööta kasutaja nimetatud kursuserepos. Kui seda ei ole avatud, lahenda skilli sümbollink pärisasukohaks ning leia repo sellest kaks kausta kõrgemalt; ära otsi selle asemel kogu kasutaja arvutist.

Loe enne kirjutamist:

1. Repo `AGENTS.md`, `metadata/data.json` ja `docs/kursuseprogramm.md` vastava seminari ning läbivate nõuete osa.
2. Muudetava seminari slaidid, õppija juhend, kodutöö ja õpetaja juhis. Loe nende lingitud peatükke selles ulatuses, mida seminaris kasutad.
3. Eelmise seminari lõpptulemus ja järgmise seminari alustamise eeldused.
4. Kinnitatud näitest `slides.md`, `peatukid/03-probleemi-uurimine.md` ja `peatukid/06-tiimi-toovoog.md`. Need näitavad slaidide nappust ning peatüki selgituste ja praktiliste sammude vajalikku põhjalikkust. Kodutöö koostamisel loe ka `peatukid/07-kodutoo-ja-release.md`; ajakava jaoks `opetaja-juhis.md`.

Eeskuju määrab esitamise viisi ja lihtsusastme. Uue seminari teemad ja nõuded võta kursuseprogrammist ning selle seminari materjalidest. Ära kanna seminari 2 harjutusi järgmisse seminari lihtsalt näidise jäljendamiseks. Kasutaja uus kokkulepe on esmane; olulist vastuolu aine põhiandmetega ära lahenda oletades.

Kui kasutaja sihtkausta ei määra, loo uus `seminarid/seminar_0N-sujuv/`. Ära kirjuta varasemat versiooni üle. Küsi täpsustust ainult siis, kui puuduv eesmärk või vastuolulised nõuded takistavad sisulist koostamist.

## Koosta üks läbiv järjekord

Anna alguses lühike hinnang ja kirjelda töö kavandit. Seejärel lõpeta töö sama ülesande raames.

Pane enda jaoks paika seminari põhiküsimus, seminaris valmiv tulemus ja kodutöö lõpptulemus. Järjesta mõisted, näited ja tegevused nii, et õppija mõistab uut mõistet enne selle kasutamist. Seo iga tegevus projekti järgmise tegeliku sammuga.

Määra igale selgitusele üks põhikoht. Näiteks:

| Sisu | Põhikoht |
|---|---|
| Kursuse seminaride teekond ja tänane koht | Üks slaid |
| Mõiste põhjendus ja sisuline näide | Vastav teemapeatükk |
| Täpne harjutus, tööleht ja valmimise tingimus | Harjutuse peatükk |
| Tööriista sammud ning käskude selgitused | Praktilise töö peatükk |
| Nõutavad failid, release ja esitamine | Üks kodutööpeatükk |
| Õpetaja ettevalmistus, ajakava ja puhver | Õpetaja juhis |

Ühenda samasse tegevusse kuuluvad killud. Discovery-taoline näide kuulub selgitatava töövõtte juurde; kodutöö kokkuvõte ei vaja omaette paralleelset juhendit. Üks lõpu kontrollpunkt on piisav.

## Kirjuta peatükid ja seejärel slaidid

### Peatükid

- Kirjuta rahulikult loetavad lühikesed lõigud. Ava mõte, selgita selle vajalikkust ja too vajaduse korral konkreetne näide. Väldi sama põhimõtte ümbersõnastamist mitmes lõigus.
- Säilita vajalikud vaheastmed. Lühendamine ei tohi jätta algajat oletama, kes tegutseb, mida ta muudab või kust töö jätkub.
- Kasuta läbivalt sama projektijuhtumit. Erista väljamõeldud näide, oletus ja päriselt kogutud tõend.
- Praktilises juhises nimeta tegija, eesmärk, tegevused, väljund ja kontrollpunkt. Erista individuaalne töö tiimi ühisest otsusest.
- Kasuta üht näidisõppijat, Issue numbrit, haru ja failinime terve näite vältel. Käsud peavad olema kopeeritavad ning nende ridade eesmärgid selgitatud. Märgi asendatavad näidisandmed.
- Eelista üht põhjalikku töövoogu. Graafilist alternatiivi võib kirjeldada lühidalt, kogu tegevusringi uuesti kirjutamata.
- Olemasolev `concepts/` materjal sobib lisalugemiseks. Seminari vajalik selgitus ei tohi koosneda ainult lausest „loe sealt”.

### Slaidid

- Üks slaid annab ühe põhisõnumi, lühikese näite või ülesande. Orienteeruv maht on 20 slaidi; vali tegelik arv teemade ja kontaktaaja järgi.
- Hoia nähtav tekst enamasti umbes 25–60 sõna piires. See on toimetamise abivahend, mitte kohustuslik piir.
- Slaid selgitab esmast mõtet; peatükk lisab sisulist sügavust. Väike mõistekordus on loomulik, sama tabeli ja tervete lõikude kordamine ei anna lugejale uut infot.
- Säilita praktilise näitamise juures vajalik lühike käsuplokk. Pikemad sammud ja reahaaval selgitused jäävad lingitud peatükki.
- Kasuta sisulisi linke otse nummerdatud failidele, näiteks `peatukid/03-probleemi-uurimine.md`. Väldi kohalikke pealkirjaankruid ja üldist „loe juurde” linki, mille siht lubatud sisu ei anna.
- Kirjuta nähtav tekst õppijale. Õpetaja näitamis- ja ajamärkused pane Marpi HTML-kommentaaridesse.
- Ära lisa eraldi slaide pelgalt üleminekulausete jaoks ega korda eesmärki, tööjärjekorda ja tulemust mitme samasisulise kokkuvõttena.

## Failid ja kursuse jätkuvus

Loo vajadusele vastav väike failikomplekt:

```text
README.md                    lühike alustamisjuhis
slides.md                    seminari keskne Marp-lähtefail
slides.html                  lähtefailist genereeritud esitlus
peatukid/01-....md            järjestatud selgitused ja tööjuhised
peatukid/NN-kodutoo-ja-release.md
opetaja-juhis.md              ettevalmistus ja realistlik ajakava
```

Ära tekita eraldi seminari üldjuhendit, mis kordab slaide ja peatükke. Teemapeatükkide arv sõltub sisust, mitte eeskuju failide arvust. Peatükid peavad olema slaididelt leitavad.

Säilita kehtiv projektikorraldus: ühine repo organisatsioonis `TLUHK-RIF26`, enda Issue ja haru, sisuline commit, PR, kaaslase ülevaatus ja merge. Harud ning commit'i sõnumid on inglise keeles. Haru kuju on `issue-<number>-<short-english-description>` ja tahvli olekud `Backlog → In progress → Review → Done`. Kasutatakse terminali ja VS Code'i.

Iga projektietapp lõpeb individuaalsete refleksioonide ja ühise release'iga; release manager ning ametialased rollid vahetuvad. Versioonid on seminarides 2–5 vastavalt `v0.1.0` kuni `v0.4.0`, eksamil `v1.0.0`. AI-d kasutatakse vähemalt ühe olulise otsuse juures ning dokumenteeritakse selle kontroll ja kasu. Kursuse tulemus on põhjendatud otsuste logiga arendusprotsess; töötavat rakendust ega klikitavat prototüüpi ei nõuta.

Ära lisa järgmise seminari õppesisu enneaegseks kohustuseks. Kodutöö peab põhinema õpetatud oskustel ja valmistama ette järgmise etapi. Kasuta olemasolevaid `seminarid/mallid/` malle. Tähtaegu, toimunud tegevusi ega kasutajauuringu tulemusi ei tohi välja mõelda.

## Kontrolli tulemust

Loe valminud materjal läbi õppija tööjärjekorras: slaid, selle peatükk, harjutus, kodutöö. Kontrolli eraldi õpetaja juhise ajakava ja ettevalmistust. Kontaktaeg võta lähtematerjalist; kinnitatud seminaris 2 on kaks 90-minutilist osa koos tehnilise puhvriga.

Küsi iga osa kohta:

- Kas see annab uut vajalikku infot või kordab mõnda teist lõiku?
- Kas õppija saab aru, kes teeb mida, millises failis ja millal on töö valmis?
- Kas slaidi link pakub tõesti lubatud lisaselgitust?
- Kas kõik näited, failinimed, tööjärjekord ja esitamisnõuded sobivad kokku?
- Kas seminari lõpu ja kodutöö lõpu tulemused on eristatavad?

Käivita skilli tehniline kontroll repo juurkaustast:

```bash
python3 <skilli-kaust>/scripts/check_material.py seminarid/seminar_0N-sujuv
```

See kontrollib faililinke, koodiplokkide sulgemist, tühje slaide ja peatükkide leitavust. See ei hinda teksti sisulist kvaliteeti.

Genereeri esitlus repo käsuga `seminarid/export-marp.sh <sihtkaust>`. Vaata võimaluse korral ka renderdatud slaide, et sisu mahuks ära. Kui renderdust ei saa kontrollida, ütle seda. Vaata üle diff ja ära kirjuta kasutaja muudatusi üle.

Lõpus anna link `slides.md` failile ning ütle lühidalt, mida ühendasid ja mida kontrollisid. Ära väida odavama mudeli tulemust juba tõendatult samaväärseks: skilli struktuuri- ja failikontroll ei asenda õppesisu läbivaatust.
