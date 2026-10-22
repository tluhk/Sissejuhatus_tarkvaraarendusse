---
schema_version: 1
template_id: kodutoo-probleemist-lahteulesandeni
title: "Kodutöö: probleemist lähteülesandeni"
story_points: null
submission_strategy: direct
peer_review_enabled: false
labels:
  - Homework
requiredness: mandatory
learning_outcomes:
  - HKI5113.3
  - HKI5113.4
  - HKI5113.5
evidence_expected: []
---

**Esiteks** – puhastage oma olemasolev SJTA repo, kustutage tarbetuks muutunud haru.

## Uus osa
(kui mõned lingid ei tööta vms, siis vaata kodutöö juhendit [siit](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/seminarid/seminar_02/homework.md).    

Üldjuhul on tarkvraarenduse eesmärk lahendada mingi probleem. Olgu see siis mängukire lahendamine (arvutimängud), luulekire rahuldamine (Word) või näiteks bussigraafiku kuvamine internetis, et inimene jõuaks koju.

**Selle kodutöö eesmärk:** leida ja seejärel valida Haapsalu kolledži tunniplaani veebilehe kasutajaprobleem, kontrollida seda ning anda järgmisele seminarile põhjendatud lähtepunkt.

**Maht:** umbes 8 tundi õppija kohta, sealhulgas tiimitöö, GitHubi töövoog ja refleksioon.

**Töö algus:** kasutage seminaris määratud `TLUHK-RIF26` tiimirepositooriumi. Iga õppija töötab oma Issue'i ja haruga, avab pull request'i (PR) ning vaatab üle kaaslase PR-i.  
**NB!** Täpne töövoog on [tiimi töövoo juhendis](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/seminarid/seminar_02/peatukid/06-tiimi-toovoog.md).

Kodutöö koosneb esmalt individuaalsetest probleemikandidaatidest, seejärel tiimi ühisest uurimisest ja otsusest. Kõik tiimiliikmed ei lahenda sama esimest Issue't: igaüks loob oma kandidaadid, tiim valib nende seast ühise uurimissuuna.

## 1. Iga õppija koostab probleemikandidaadid

**Aeg: umbes 2 tundi.**

1. Looge koos tiimiga GitHubis Issued igale õppijale, määrake igaühele ja lisage valmisoleku tingimus.
2. Loo enda Issue numbri või nimega seotud haru. Näiteks Issue `12` haru nimi võiks olla `issue-12-problem-candidates`.
3. Kirjelda oma failis vähemalt kolme võimalikku tunniplaani kasutaja probleemi. Lisa igaühe juurde, keda see puudutab, mida sa praegu tead ja mida alles oletad.
4. Hinda kandidaate seminaris antud küsimuste abil ning märgi, millist neist tasuks lähemalt uurida.
5. Tee sisuline commit, lükka haru GitHubi ja ava PR. Vali ülevaatajaks tiimikaaslane.
6. Vaata üle teise õppija PR ja anna konkreetset tagasisidet. Paranda enda tööd saadud tagasiside põhjal.
7. Jätkake tiimi võrdlust alles siis, kui kõigi individuaalsed tööd on üle vaadatud ja `main`-harusse ühendatud.

Faili näidisnimi: `research/eesnimi-perenimi-probleemikandidaadid.md`.

## 2. Tiim võrdleb kandidaate ja teeb esialgse valiku

**Aeg: umbes 1 tund.**

1. Looge kandidaatide võrdlemiseks eraldi Issue ja määrake inimene, kes koondab ühise otsuse faili.
2. Võrrelge kõigi liikmete kandidaate: kelle probleemiga on tegu, kui oluline see paistab ja mida on vaja kontrollida?
3. Valige üks kandidaat edasiseks uurimiseks. Valik on esialgne ja võib uue info põhjal muutuda.
4. Looge `decisions/001-probleemi-valik.md`. Kirjutage sinna valitud probleem, valiku põhjendus, vähemalt üks kõrvale jäetud alternatiiv ning osalenud rollid.

## 3. Tiim kontrollib probleemi sõltumatu infoga

**Aeg: umbes 2 tundi.**

Iga õppija teeb vähemalt ühe kontrolliva tegevuse. Jagage tegevused eraldi Issue'deks, et oleks selge, kes mida uurib. Näiteks võib õppija:

- vestelda tunniplaani kasutajaga;
- vaadelda, kuidas kasutaja praegust tunniplaani kasutab;
- analüüsida usaldusväärset andmeallikat või olemasolevat tööprotsessi.

Dokumenteerige ühises otsusefailis iga kontrolli allikas, mida leidsite, mida see muutis ja mis jäi ebakindlaks. Ärge lisage osalejate nimesid ega tundlikku infot. AI vastus üksi ei ole probleemi kohta sõltumatu tõend.

Kasutage AI-d vähemalt ühe olulise otsuse juures. Kirjeldage, milleks seda kasutasite, mida väljundist kontrollisite, mida kasutasite või kõrvale jätsite ning millist kasu sellest oli.

Kui uurimine valitud probleemi ei toeta, muutke probleemi sõnastust või valige teine suund. Põhjendage muudatust otsusefailis.

## 4. Tiim sõnastab arendustöö lähteülesande

**Aeg: umbes 1 tund.**

Täiendage sama otsusefaili nii, et järgmine arendustiim saaks aru:

- kes on peamine kasutaja ja mis olukorras ta on;
- milline takistus või vajadus ilmnes ja mis mõju sel on;
- millised tõendid valikut toetavad ning miks see suund valiti;
- milline tulemus on soovitud ja mis kuulub esialgsesse ulatusse;
- millised piirangud, lahtised küsimused ja järgmised kontrollid on teada.

Kirjeldage probleemi ja soovitud tulemust. Ärge määrake tõenditeta ette konkreetset kujundust või funktsioone. Nõuete ja kasutajalugude täpsustamine toimub seminaris 3.

## 5. Iga õppija kirjutab refleksiooni; tiim valmistab ette avaldamise

**Aeg: umbes 2 tundi koos tiimitööga.**

Iga õppija lisab oma refleksiooni faili, kasutades [refleksiooni malli](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/seminarid/mallid/individuaalne-refleksioon.md). Refleksioonis kirjelda enda panust, õpitut, raskusi ja seda, mida järgmises etapis teisiti teeksid.

Tiim teeb samal ajal järgmist:

1. Täiendab `README.md`-d projekti eesmärgi, liikmete ja oluliste failide linkidega.
2. Võrdleb Issue'de ajahinnanguid tegeliku ajakuluga ja märgib ühe paranduse järgmise etapi planeerimiseks.
3. Koostab faili `releases/v0.1.0.md`, kasutades [release notes'i malli](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/seminarid/mallid/release-notes.md). Kirjeldab seisu, olulisi otsuseid, muutunud arusaama, kontrollitud infot, lahtisi küsimusi ja liikmete panust.
4. Viib kõik muudatused eraldi harude ja PR-ide kaudu `main`-harusse. PR-id vaatavad üle tiimikaaslased.

Release manager (määrate endi seast) koordineerib avaldamist. See roll ei tähenda, et ta teeb üksi kogu tiimi töö.

## 6. Release manager avaldab versiooni `v0.1.0`

Tag on projektiajaloo kindlat seisu tähistav silt. GitHub Release lisab sellele seisule pealkirja ja kokkuvõtte. Seminar 2 lõpeb ühise versiooniga `v0.1.0`.

Release manager kontrollib, et vajalikud PR-id on `main`-harusse ühendatud, ning loob release'i [peatüki 07 juhise](https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/blob/master/seminarid/seminar_02/peatukid/07-kodutoo-ja-release.md#release-v010) järgi.

Mustand ei ole avaldatud release. Pärast avaldamist jääb tag tähistama seda etapi seisu. Järgmine etapp jätkub uute Issue'de ja harudega ning saab uue versiooni. Release manageri roll vahetub.

## 7. Iga õppija esitab töö

Iga õppija lisab õppejõu antud kodutöö Issue'sse enda kommentaari. PR-i pole kodutöös vaja teha. 
Kommentaari sisu:

- link oma tiimi avaldatud `v0.1.0` release'ile;
- ühise otsusefaili link;
- enda refleksiooni link;
- enda PR-i number ja kaaslase PR, mille üle vaatasid.

## Valmis töö kontrollnimekiri

- [ ] Iga õppija probleemikandidaatide fail on PR-iga üle vaadatud ja ühendatud.
- [ ] Tiim on kandidaate võrrelnud ning valiku ja alternatiivid dokumenteerinud.
- [ ] Iga õppija on teinud vähemalt ühe probleemi kontrolliva tegevuse.
- [ ] Otsusefail kirjeldab tõendeid, ebakindlust, lähteülesannet ja AI kasutamise kontrolli.
- [ ] Igal õppijal on refleksioon ning tiimikaaslase PR-i ülevaatus.
- [ ] Tiimi README ja release notes kirjeldavad etapi tulemust.
- [ ] `v0.1.0` on GitHubis avaldatud ja selle failid kontrollitud.
- [ ] Iga õppija on lisanud oma kodutöö Issue kommentaari lingi tiimi release'ile, otsusele ja enda refleksioonile ning PR-numbrid.

Töötavat rakendust ega klikitavat prototüüpi ei nõuta. Lahtised küsimused võivad alles jääda, kui järgmine uurimissamm on kirjas.

## Hindamiskriteeriumid

Hindan tiimi ühist tulemust repositooriumis ning iga õppija panust tema Issue'i, PR-i, ülevaatuse ja refleksiooni põhjal. Kokku on võimalik saada 100 punkti.

| Kriteerium | Punktid | Mida repositooriumist vaatan |
|---|---:|---|
| Probleemikandidaadid ja valik | 15 | Iga õppija on esitanud kandidaadid. Tiim on neid võrrelnud ning põhjendanud valitud probleemi ja vähemalt üht alternatiivi. |
| Probleemi uurimine | 25 | Tiim on kontrollinud probleemi sõltumatu infoga. Allikad, leiud ja ebakindlus on kirjas; AI väljundit ei esitata tõendina. |
| Lähteülesande selgus ja põhjendatus | 20 | Otsusefailist selguvad kasutaja, probleem ja selle mõju, soovitud tulemus ning järgmised uurimisküsimused. Järeldused toetuvad kogutud infole. |
| Tiimitöö ja iga õppija panus | 20 | Iga õppija panus on jälgitav Issue'i ja PR-i kaudu. Igaüks on sisuliselt üle vaadanud kaaslase PR-i, panustanud uurimisse või dokumenteerimisse ning lisanud kodutöö Issue kommentaari lingi tiimi release'ile. |
| Refleksioon ja AI kasutamise läbipaistvus | 10 | Iga õppija refleksioon kirjeldab tema panust ja õpitut. Repo näitab, milleks AI-d olulise otsuse juures kasutati, kuidas väljundit kontrolliti ja mis sellest kasu oli. |
| Repositooriumi korrastatus ja release | 10 | README ja olulised failid on leitavad, muudatused on jõudnud `main`-i PR-ide kaudu ning `v0.1.0` release on avaldatud. |

**Tulemuse tõlgendamine:** 90–100 punkti tähendab põhjendatud ja jälgitavat tööd; 75–89 punkti puhul on tulemus olemas, kuid mõni osa vajab täiendamist; 60–74 punkti puhul takistab oluline lünk järgmises seminaris jätkamist; alla 60 punkti korral ei ole probleemi piisavalt uuritud või panust ja otsuseid ei saa repo põhjal hinnata.

Probleemi uurimise ja lähteülesande eest peab saama kokku vähemalt poole nende kahe kriteeriumi punktidest. Korras README või release ei korva tõendamata probleemi. Töötava rakenduse, prototüübi ega dokumentide hulga eest eraldi punkte ei anta. AI puhul hinnatakse kasutamise eesmärki ja väljundi kontrollimist, mitte genereeritud teksti mahtu.
