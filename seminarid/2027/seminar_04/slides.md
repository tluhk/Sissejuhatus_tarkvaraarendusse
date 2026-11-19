---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 4 – kvaliteet, riskid ja vastutus
---

# Seminar 4

## Kvaliteet, riskid ja vastutus

<!-- Seminar 3 vastas küsimusele, mida süsteem teeb: kasutajalood, kontrolltingimused ja süsteemi kontseptsioon. Täna küsime, kuidas me teame, et see kavand on piisavalt hea, ja mis võib meid alt vedada. Teooria on konspektis ja õppijad lugesid selle enne seminari. Täna selgitame iga teemat kuni 10 minutit ja ülejäänud aeg on tiimi oma kavandi kontrollimine. Kui harjutuse slaidini pole õigel ajal jõutud, jääb rääkimata teooria, mitte harjutus. -->

---

## Kogu kursuse teekond: kus oleme?

Probleem → kasutajate ja vajaduste uurimine → nõuete kirjeldamine → töö planeerimine → lahenduse disainimine → arendamine → **testimine ja tagasiside – seminar 4** → avaldamine ja hooldus

- seminar 1: suur pilt ja töövahendite seadistamine
- seminar 2: kliendisoovist arendusülesandeni
- seminar 3: rollid, tööviisi valik ja süsteemi kontseptsioon
- **seminar 4: kvaliteet, riskid ja vastutus**
- seminar 5: kasutuselevõtt, tagasiside ja hooldus
- eksam: protsessi esitlus release'ide ajajoonena ja mõistete test

<!-- Testimine ja tagasiside on elutsükli etapp, kus kontrollitakse, kas tehtu vastab vajadusele. Meil rakendust pole, seega kontrollime kavandit: kas nõuded on mõõdetavad, kas neid saab testida ja mis võib kavandi alt vedada. Sama kontroll käib päris projektides enne ehitamist ja selle ärajätmine on kõige kallim viga. -->

---

## Tänane päev

| | I osa | | II osa |
|---|---|---|---|
| 1 | Kodutöö 3: kolm punkti | 5 | Riskikaart ja harjutus |
| 2 | „Selgita oma otsust” | 6 | WIP-piirang ja blokeerija |
| 3 | Kvaliteedinõue ja harjutus | 7 | Git: `log`, `diff`, `restore` |
| 4 | Testjuhtum ja harjutus | 8 | Rollivahetus ja kodutöö 4 |

**Põhiküsimus:** kuidas me teame, et kavand on piisavalt hea, ja mis võib meid alt vedada?

Enne seminari loetud: [Mõõdetav kvaliteet](../../../handbook/04-quality-and-risk/01-measurable-quality.md) ja [Riskid](../../../handbook/04-quality-and-risk/04-risks.md).

<!-- Kaks esimest sammu vaatavad tagasi: kas tööviis oli kasutusel ja kas tiim saab oma otsustest aru. Sammud 3 ja 4 teevad kavandi kontrollitavaks, samm 5 küsib, mis võib alt vedada. Sammud 6 ja 7 on töövahendid: tahvel ja Git. Samm 8 on kodutöö. Igal harjutusel on fail tiimi repos ja see commit'itakse seminari lõpuks ka pooleli kujul, et kodutöö jätkaks sealt. Kui keegi ei ole konspekti lugenud, ei räägi me teooriat pikemalt: slaidil on põhimõte ja konspekti link, ülejäänu tuleb harjutuse käigus. -->

---

## Kuhu jõuame

`v0.2.0` ütles, mida süsteem teeb. `v0.3.0` ütleb, kuidas me teame, et see on piisavalt hea.

**Seminari lõpuks tiimi repos**, ka pooleli kujul:

- suurim kontrollimata eeldus Issue'na
- 3 mõõdetavat kontrolltingimust koos piiri allikaga
- 1 testjuhtum põhiloo kohta
- riskikaardi algus: eeldus, andmeallikas, üks kolmas osapool

**Kodutöö lõpuks release `v0.3.0`:** kvaliteedinõuded, testjuhtumid, riskikaart, otsus `004`, backlog ja refleksioonid.

<!-- Seminaris tehakse igast asjast tiimi enda kavandi peal esimene versioon. Kodutöö laiendab seda kõigi lugude peale ja seob otsusega 004. Release võib sisaldada lahtisi küsimusi, näiteks kui andmeallika kohta pole veel vastust; oluline on, et hetkeseis ja järgmised sammud on kirjas. -->

---

## 1. Kodutöö 3: kolm asja, mida teeme teisiti

1. Tahvel liigub töö ajal: kaart In progress, kui alustad, Done, kui valmis.
2. Backlog tuleb tootest, mitte kodutöö punktidest.
3. Ülevaatus on sisuline küsimus. „Korras” ei ole ülevaatus. PR-i ühendab keegi teine kui autor.

Kirjalik tagasiside on Issue's. Küsimused nüüd.

<!-- Kolm punkti on vaikimisi need, mis 2026. aastal kodutööst 3 välja tulid. Asenda need enne seminari tegeliku kodutöö 3 kokkuvõtte põhjal, aga hoia arv kolmel: pikem loend ei jää meelde. Kõik muu, näiteks AI maht, linkide kuju ja hinnang automaathindamisele, on kirjalikus tagasisides, mille õppijad said enne seminari. Siin vastatakse ainult küsimustele. Kui ükski tiim ei küsi, mine edasi: aeg on harjutuste jaoks. -->

---

## Tahvel ja ajaväljad korda

| Väli | Millal täidetakse |
|---|---|
| Estimate | Issue'i loomisel |
| Tegelik (h) | Issue'i sulgemisel |

- puuduv väli: tahvli paremas servas `+` → New field → Number
- ühik on tund, täpsus pool tundi
- tabelivaade rühmitatud Statuse järgi näitab summad; release notes võrdleb neid

Projektijuht kontrollib praegu, et mõlemad väljad on tiimi Projectsis.

<!-- Hinnangu ja tegeliku aja vahest õpib tiim plaanima. Väärtus ei ole täpses hinnangus, vaid selles, et vahe on näha ja sellest saab järelduse: millist tööd alahindame. Hinnang pannakse loomisel, sest hiljem kaldub see tegeliku poole; tegelik aeg sulgemisel, sest release'i õhtul ei mäleta keegi. Kaks minutit: projektijuht avab Projectsi ja kontrollib väljad; kui puudub, lisab kohe. -->

---

## 2. Selgita oma otsust

10 minutit ettevalmistust, seejärel iga tiim 4 minutit kolmele küsimusele:

1. Mis probleemi te lahendate ja kellele?
2. Millise suuna valisite, mis oli alternatiiv ja miks just see?
3. Mis on teie **suurim kontrollimata eeldus**: millele lahendus toetub, aga mida keegi pole üle vaadanud?

Seletab see, kelle roll on teema juures; enda kirjutatud teksti ei seleta keegi. Punkte see ei anna.

Juhend: [Selgita oma otsust](sammud/01-selgita-oma-otsust.md)

<!-- v0.3.0 ehitatakse v0.2.0 otsuste peale, ja ehitada saab ainult sellele, millest aru saadakse. Seletamine oma sõnadega on ainus viis teada saada, kas mõiste on omandatud või ainult dokumenti kirjutatud. Kolmas küsimus on tänase päeva alus: 2026. aastal leidis iga tiim sama eelduse, et tunniplaani andmed saab kätte ja tellijaga pole räägitud. Pärast iga tiimi küsi ühe küsimuse: kuidas te selle eelduse kontrolliksite ja kellelt? Tagumise rea tiimid tulevad ette, muidu ei kuule keegi. Kui tiime on kuus, kulub 24 minutit; hoia 4 minutist kinni. -->

---

## Eeldus läheb kohe tahvlile

Iga tiim loob Issue: „Kontrolli eeldust: …”

- kellelt küsime ja millal
- Estimate kohe
- kui vastus tuleb väljastpoolt tiimi, saab Issue hiljem sildi `blocked`

See on teie riskikaardi esimene rida.

<!-- Harjutuse tulemus ei tohi jääda jutuks. Issue on toote vajadus, mitte kodutöö samm: „kontrolli, kas kalendriekspordist saab andmed kursuse kaupa” on töö, mida toode vajab. Seda Issue't kasutame II osas blokeerija näitena. Projektijuht loob Issue ja paneb hinnangu, ülejäänud tiim läheb edasi. Kaks minutit. -->

---

## 3. Funktsioon ja kvaliteediomadus

**Funktsioon:** mida süsteem teeb? Õppija näeb järgmise loengu aega ja ruumi.

**Kvaliteediomadus** ehk mittefunktsionaalne nõue: kui hästi või mis tingimustel? Telefonis, kuni 10 sekundiga, ilma rühma uuesti valimata.

Töötamine ei võrdu kvaliteediga. Kvaliteet on sobivus päris kasutusolukorda.

<!-- Sama funktsiooni saab teha väga erineva kvaliteediga. „Õppija näeb järgmise loengu aega ja ruumi” on täidetud nii kahe sekundiga kui ka minuti ja kolme klõpsuga. Funktsioon vastab küsimusele „mida”, kvaliteediomadus küsimusele „kui hästi” või „mis tingimustel”. Levinumad omadused on konspekti tabelis: kasutatavus, jõudlus, töökindlus, andmete õigsus, ligipääsetavus, turvalisus, hooldatavus. Kasutajaloo kontrolltingimused sisaldavad neid sageli juba, ainult ebamääraselt: „kiiresti”, „mugavalt”. Kolm minutit. -->

---

## Ebamäärasest mõõdetavaks

| Enne | Pärast |
|---|---|
| Õppija leiab järgmise loengu kiiresti. | Õppija leiab telefonis oma rühma järgmise loengu aja ja ruumi kuni 10 sekundiga ilma rühma uuesti valimata. |

Küsi: **kes** ja mis olukorras, **mida** kontrollitakse, **milline arv või tingimus** näitab, et nõue on täidetud.

Arv ei tule peast. Iga piiri juures on kirjas allikas: mõõtmine, küsitlus või tehniline parameeter. Kui allikat pole, on piir **eeldus** ja läheb riskikaardile.

<!-- Kolm küsimust teevad lause kontrollitavaks: kes ja mis olukorras, mida kontrollitakse, mis arv või tingimus. Nüüd oskab testija öelda, kas test õnnestus. Arv peab tulema millestki: kui praegusel tunniplaanilehel kulub telefonis 40 sekundit, on 10 selge paranemine. Kui keegi pole mõõtnud, on 10 sekundit sama ebamäärane kui „kiiresti”, ja siis kirjutatakse piir eeldusena, mitte faktina. Kõik ei pea olema sekundites: „ilma rühma uuesti valimata” on jah-ei tingimus, „4 kasutajat 5-st täidavad ülesande ilma abita” on mõõdetav kasutatavuse nõue. Terminid: kvaliteediomadus on näiteks jõudlus; mõõdetava piiriga saab sellest kvaliteedinõue; kasutajaloo juures kannab seda kontrolltingimus. Kolm minutit. -->

---

## Kontrollküsimused iga kavandi juures

- **Kelle silmis?** Kasutaja, kool, arendaja, käitaja ja ühiskond näevad kvaliteeti erinevalt. Valige omadused vähemalt kahest vaatenurgast.
- **Millest loobume?** Turvalisus lisab samme, töökindlus tõstab hinda. Kompromiss on lubatud, kui see on kirjas.
- **Kas neid andmeid on vaja?** Mida vähem isikuandmeid, seda väiksem privaatsusrisk.
- **Kas info on ainult värviga?** Lisage tekst. Kontrollige väikest ekraani ja aeglast võrku.

Pikemalt: [Mõõdetav kvaliteet](../../../handbook/04-quality-and-risk/01-measurable-quality.md)

<!-- Need neli küsimust asendavad 2026. aasta nelja slaidi: vaatenurgad, kompromissid, turvalisus ja privaatsus, ligipääsetavus. Pikem selgitus on konspektis. Tunniplaani näited: käitaja küsib, kas keegi saab teada, kui andmed enam ei lae; kool küsib, kas ÕIS-i andmeid tohib kasutada; vaade ilma sisselogimiseta loobub isiklikest valikutest, aga võidab privaatsuse; muutunud tund ainult punase värviga ei ütle ekraanilugejale midagi. Kaks minutit, siis harjutus. -->

---

## Harjutus: 3 kontrolltingimust (20 min)

Tiim kirjutab oma lugudest **3 kvaliteedinõuet** mõõdetava kontrolltingimusena. Iga piiri juures on allikas või märge „eeldus”.

- fail tiimi repos: `requirements/quality.md`
- vähemalt üks nõue ei ole kasutaja vaatenurgast
- kokku võtab disainer

**Valmis, kui** iga rida vastab kolmele küsimusele ja ükski arv pole ilma allikata.

Juhend ja näide: [Kontrolltingimus](sammud/02-kontrolltingimus.md)

<!-- Käi tiimid läbi ja küsi iga arvu juures: kust see tuleb? Kui vastus on „tundus mõistlik”, on see eeldus ja läheb riskikaardile; see on õige vastus, mitte viga. Tunniplaani puhul tulevad lugudest enamasti kasutatavus telefonis, andmete õigsus ja töökindlus laadimise tõrke korral. Turvalisus võib olla väike teema, kui süsteem isikuandmeid ei kogu; see on lubatud valik, kui põhjendatud. Kümnendal minutil ütle, et vähemalt üks rida peab olemas olema; kahekümnendal commit'itakse see, mis on. Pooleli fail on parem kui tühi. -->

---

## 4. Testjuhtum: kuidas nõuet kontrollida

Kontrolltingimus ütleb, *mis* peab olema tõsi. Testjuhtum ütleb, *kuidas* seda kontrollida.

| Väli | Sisu |
|---|---|
| Test | T1: valitud rühm on telefonis nähtav (lugu 1) |
| Eeldused | telefon, ekraani laius kuni 400 px; valitud on rühm A |
| Sammud | 1. Ava tunniplaan. 2. Vali rühm A. 3. Sulge menüü. 4. Keri alla. |
| Oodatud tulemus | rühma nimi on kogu aeg nähtav ilma menüüd avamata |

Test tehakse **kavandi peal**: kui kavand annab igale sammule vastuse, on test läbitud. Kui ei anna, on kavandis auk ja sellest saab Issue.

<!-- Eeldused ütlevad, mis peab enne testi tõsi olema; sammud on täpsed tegevused, et teine inimene saaks korrata; oodatud tulemus ütleb, mida peab nägema. Tegelik tulemus täidetakse testimisel. Rakendust meil pole, seega käiakse sammud läbi kasutaja teekonna ja arhitektuuri järgi: kas kavand ütleb, mis igal sammul juhtub? Kui kavand ei ütle, mis on ekraanil pärast kerimist, on test läbi kukkunud ja auk on leitud enne ehitamist. Just see on testi mõte. Kolm minutit. -->

---

## Testi ka seda, mis võib valesti minna

| Test | Eeldus | Oodatud tulemus |
|---|---|---|
| T2: tühi nädal | valitud nädalal tunde pole | teade „sel nädalal tunde pole” |
| T3: andmed ei lae | andmeallikas ei vasta | teade „andmeid ei õnnestunud laadida”, mitte tühi tunniplaan |

Kasutajale näevad need ühesugused välja. Kui süsteem neid ei erista, arvab õppija, et tund jäi ära.

<!-- Erijuhud on kohad, kus süsteemid vigu teevad: tühi sisend, puuduvad andmed, katkenud võrk. T2 on päris olukord, T3 on rike, ja tähendus on vastupidine: ühel juhul võib koju jääda, teisel peaks kontrollima mujalt. Süsteem, mis mõlemal juhul näitab tühja tabelit, eksitab kasutajat kõige halvemal hetkel. Kodutöös peab üks tiimi testjuhtum katma vea olukorda. Kaks minutit. -->

---

## Harjutus: üks testjuhtum (15 min)

Tiim kirjutab **ühe testjuhtumi** oma põhiloo kohta ja proovib selle kavandi peal läbi.

- fail tiimi repos: `tests/test-cases.md`
- väljad: test, lugu, eeldused, sammud, oodatud tulemus, tegelik tulemus kavandi järgi
- kui kavand mõnele sammule vastust ei anna, loo Issue

**Valmis, kui** teine tiimiliige saab sammud lugeda ja öelda, mida kavandi järgi igal sammul juhtub.

Juhend ja näide: [Testjuhtum](sammud/03-testjuhtum.md)

<!-- Käi tiimid läbi ja küsi: kas kavand annab igale sammule vastuse? Kui ei, kus on auk? Levinud leid: kasutaja teekond ütleb „valib rühma”, aga mitte, kas valik jääb meelde järgmisel avamisel. See on auk ja sellest saab Issue, mitte häbi. Kodutöös kirjutab iga õppija ühe testjuhtumi oma loo kohta. Seminari lõpuks commit, ka pooleli. -->

---

# II osa

## 5. Mis võib meid alt vedada?

<!-- Esimene osa tegi kavandi kontrollitavaks. Teine osa küsib, mis võib kavandi alt vedada, ja paneb leiud tahvlile. Alustame sammus 2 leitud eeldusest. -->

---

## Risk ja eeldus

**Eeldus** on väide, mida peame tõeseks, kuigi pole kontrollinud. Iga kontrollimata eeldus on risk.

| | Näide |
|---|---|
| Eeldus | „Tunniplaani andmed on tõenäoliselt olemas.” |
| Risk | „Allikas ei sisalda tulevasi kuupäevi või seda ei tohi kasutada. Järgmist loengut ei saa näidata.” |
| Maandus | „Kontrollime enne jätkamist, millised väljad allikas on ja kas neid tohib kasutada.” |

„Tõenäoliselt olemas” ei ole maandus. See on see, mida tuleb kontrollida.

<!-- Risk ja eeldus on sama asja kaks külge: eeldus on see, mida peame tõeseks ilma kontrollimata; risk on see, mis juhtub, kui eeldus ei pea. Levinud viga on kirjutada eeldus maanduse veergu. Maandus on tegevus: kontrollime allikat näidispäringuga enne, kui kavandiga edasi läheme. Sellepärast on riskikaardil eeldused eraldi osas: siis on näha, mida tiim veel ei tea. Kolm minutit. -->

---

## Riskikaart

| Väli | Küsimus |
|---|---|
| Mis võib juhtuda | mis sündmus, mitte teema? |
| Mõju | kellele ja kui tõsine: madal / keskmine / kõrge |
| Tõenäosus | madal / keskmine / kõrge |
| Kuidas märkame | mis märk näitab, et risk realiseerub? |
| Maandus | mida teeme, et risk või mõju oleks väiksem? |
| Vastutaja | milline **roll** reageerib ja mis on tema esimene tegevus? |

„Meeskond” ei ole vastutaja: kui kõik vastutavad, ei reageeri keegi.

<!-- Mis võib juhtuda on konkreetne sündmus: „andmeallikas ei sisalda tulevasi kuupäevi”, mitte „andmete probleemid”. Tõenäosus kolmel astmel, täpsem petaks täpsusega, mida pole. Kuidas märkame unustatakse sageli; kui tiim ei oska öelda, saab ta riskist teada alles kasutaja kaebusest. Maandus võib olla ka kavandi muutmine: isikuandmete lekke riski saab vältida, kui andmeid ei koguta. Alustatakse ridadest, kus mõju ja tõenäosus on kõrged; pikk loend madala mõjuga riske on müra. Kolm minutit. -->

---

## Kolmandad osapooled

Teek, pilveteenus, andmestik, font või AI-mudel toob lisaks kasule sõltuvuse: litsents ja tingimused, andmete liikumine, hind, jätkusuutlikkus, asendatavus.

Näide: Cloudflare'i 2019. aasta katkestus viis maha tuhandeid veebilehti, mis ise midagi valesti ei teinud. [Allikas](https://blog.cloudflare.com/cloudflare-outage/)

Riskikaardil on vähemalt üks rida kolmanda osapoole kohta koos märkega, kas litsents või tingimused on kontrollitud.

<!-- Tunniplaani projekti suurim sõltuvus on kooli andmeallikas, ja see ongi andmeallika risk. Cloudflare: 2019. aasta juulis lisati veebitulemüüri reegel vigase regulaaravaldisega, see levitati sekunditega kogu maailma ja Cloudflare'i kaudu töötavad lehed olid umbes pool tundi maas. Põhjus ei olnud üks rida, vaid testimine, mis viga kinni ei püüdnud, liiga kiire levitamine ja kaitsemehhanism, mis oli ise sama rikke all. Rike tekib koodi, testimise, levitamise ja seire koosmõjus. Kolm minutit, mitte rohkem. -->

---

## Harjutus: riskikaart (25 min)

Tiim alustab riskikaarti [malli](../../mallid/riskikaart.md) järgi:

1. sammus 2 leitud eeldus: eelduste osas ja riskina
2. tunniplaani andmeallika risk
3. üks kolmanda osapoole risk koos litsentsi või tingimuste kontrolliga
4. nii palju muid riske, kui jõuate; kodutöös kokku vähemalt 5

Fail tiimi repos: `risks/risk-map.md`. Kokku võtab arhitekt.

**Valmis, kui** igal real on kõik väljad ja vastutajaks on roll.

Juhend: [Riskikaart](sammud/04-riskikaart.md)

<!-- Käi tiimid läbi ja küsi: kes on vastutaja ja mis on tema esimene tegevus? Kui vastus on „meeskond”, palu nimetada roll. Riskid võivad olla ka töökorralduse kohta: tiimiliige haigestub enne release'i, PR-id ootavad ülevaatust. Kui riskikaart ei muuda ühtegi varasemat otsust, küsi, kas see on tehtud kodutöö pärast. Viieteistkümnendal minutil ütle, et kolm esimest rida peavad olemas olema; kahekümne viiendal commit. -->

---

## Mida uus risk varasemas kavandis muudab?

Kui riskikaart on valmis ja ükski varasem otsus ei muutu, oli see tehtud kodutöö pärast, mitte projekti pärast.

Kodutöös: otsus `004` nimetab vähemalt ühe kompromissi ja ühe varasema otsuse, mis kinnitati, täpsustati või muudeti. Muutus ei ole läbikukkumine.

<!-- Algajad tajuvad otsuse muutmist vea tunnistamisena. Päris projektides on vastupidi: otsus, mis uue info peale ei muutu, on kahtlane. Uus otsus ei kirjuta vana üle, vaid viitab sellele: otsus 003 valis suuna B; risk, et andmeallikas ei anna kursuse kaupa andmeid, muudab suuna B kalliks; otsus 004 täpsustab suunda. Kinnitus on ka lubatud, kui see on põhjendatud riskikaardiga. Üks minut. -->

---

## 6. WIP-piirang ja blokeerija

**WIP-piirang** (*work in progress*): mitu kaarti võib korraga olla In progress. Sunnib lõpetama, mitte uut alustama.

**Blokeerija**: takistus, mille tõttu Issue'iga ei saa edasi. Blokeeritud kaart näeb tahvlil välja nagu tavaline pooleliolev töö, seepärast märgitakse see eraldi.

| Ots | Kuidas märkida |
|---|---|
| Ootav Issue | silt `blocked` + kommentaar: mida ootame, kellelt, millal kontrollime |
| Blokeeriv Issue | seos „Mark as blocked by” või silt `blocker`: tee see enne ära |

Kumbki silt ei asenda teist. Kaart jääb olekusse In progress.

<!-- Demo tiimi repos: sammus 2 loodud eelduse Issue saab sildi blocked, kui vastus tuleb väljastpoolt tiimi, ja kommentaari kolme vastusega. Kui blokeerija on teine Issue, märgi seos külgribalt; GitHub näitab siis ühel „Blocked by” ja teisel „Blocking”. Silt blocker tuleb Jira „Blocker” prioriteedist: see käib blokeeriva pileti peal ja ütleb, et see tuleb enne ära teha. Kui takistus kaob, eemaldatakse silt ja kirjutatakse, mis lahendas. Blokeeritud kaart võtab WIP-piirangust koha; see on õige, nii on põhjus takistus kõrvaldada. Kümme minutit koos demoga. -->

---

## 7. Git: kolm kontrolli oma töö kohta

Kvaliteet ja riskid kehtivad ka tiimi enda töö kohta.

```bash
git log --oneline
git diff
git restore proov.md
```

- `log`: kas sõnumitest saab aru, mida tehti? Eksami ajajoon tuleb siit.
- `diff`: mis on veel commit'imata? Vaata enne iga commit'i.
- `restore`: kustutab faili commit'imata muudatused. Neid ei saa tagasi.

Juba push'itud viga: ära muuda ajalugu, tee parandav commit. VS Code'is ja harjutus: [Giti ajalugu ja tagasivõtmine](../../../handbook/04-quality-and-risk/06-git-history.md)

<!-- git log on jälgitavus; git diff on oma töö test enne esitamist; git restore ja git revert on riski maandus. Demo terminalis ja sama VS Code'i Source Control vaates. Seejärel käivitab igaüks git log --oneline tiimi repos ja vaatab, kas tänastest sõnumitest saab aru, mida tehti. „update” ja „fix” ei ütle midagi; „Add quality requirements” ütleb. git restore on ainus ohtlik käsk täna: enne vaadatakse alati diff. Harjutus proovifailiga on konspektis ja jääb koju. Viisteist minutit. -->

---

## 8. Arendamise etapp ühel slaidil

Arendajad muudavad kavandi töötavaks tarkvaraks. Sellel kursusel rakendust ei ehitata. Kaks arendaja oskust on kasulikud igas rollis:

- **viga** (*bug*) ja **silumine** (*debugging*): korda viga väikese näitega, kirjelda oodatud ja tegelik tulemus, kontrolli oletust, paranda, korda testi;
- **koodi ülevaatus** (*code review*): kas muudatus teeb seda, mida PR lubab? Kas sellest saab aru? Mis juhtub erijuhtudel?

Kodutöös iseseisvalt konspekti järgi: [Silumine ja koodi ülevaatus](../../../handbook/04-quality-and-risk/03-debugging-and-code-review.md). Koodi kirjutama ei pea.

<!-- Programmeerimist õpitakse teistes ainetes. Siin piisab mõistest: oodatud ja tegelik tulemus on sama paar, mis testjuhtumis; hea ülevaatuse kommentaar on konkreetne küsimus koodi, mitte inimese kohta. Sama põhimõtet kasutab tiim juba dokumentide PR-ide juures. Harjutus on konspektis väikese näitega ja iga õppija teeb selle kodus. Kaks minutit. -->

---

## Rollivahetus

Igaüks saab uue rolli; `v0.2.0` release manager ei ole uuesti release manager. Vaikimisi ring: projektijuht → arhitekt → disainer → release manager → projektijuht.

| Roll | Vastutab kodutöös 4 |
|---|---|
| Projektijuht | tahvel ja ajaväljad, eelduse Issue, merge-reegel |
| Disainer | kvaliteedinõuded `requirements/quality.md` |
| Arhitekt | riskikaart `risks/risk-map.md` |
| Release manager | kontrollnimekiri ja release `v0.3.0` |

Uued rollid kirjutatakse README-sse kodutöö esimeses PR-is. Tiim võib lisada testija rolli testjuhtumite eest.

<!-- Rollid vahetuvad, et iga õppija kogeks eri vaatenurki. Tabel ütleb, kes võtab tulemuse kokku, mitte kes teeb üksi. Kolmeliikmelises tiimis on ühel kaks rolli. Testija roll on vabatahtlik: kui tiim selle lisab, vastutab testija selle eest, et igal lool on testjuhtum ja üks katab vea olukorda. -->

---

## Kodutöö: `v0.3.0 – Kvaliteedi- ja riskiplaan`

Kodutöö jätkab seminari faile, mitte ei alusta uusi:

- `requirements/quality.md`: 3–4 kvaliteedinõuet, igal piiril allikas või eeldus
- `tests/test-cases.md`: tiimi ühine + igaühe üks oma loo kohta; üks katab vea olukorda
- `risks/risk-map.md`: andmeallikas, eeldus ja vähemalt 5 muud riski
- otsus `004`, backlog tootest, `releases/v0.3.0.md`

Iga õppija: Issue, PR, sisuline ülevaatus, iseseisev silumisharjutus ja refleksioon oma `SJTA` repos.

[Kodutöö 4 juhend](homework.md)

<!-- Kõik kodutöö osad on seminaris alustatud. Kodutöö laiendab need kõigi lugude peale ja seob otsusega 004. Release notes võrdleb hinnangut tegeliku ajaga Projectsi väljadest. Kui Issue'de hinnangute summa ületab 8–10 tundi õppija kohta, jäetakse osa backlog'i ja kirjutatakse release notes'i, miks; see on õige otsus, mitte puudus. -->

---

## Reeglid kodutöös 4

- **Merge:** PR-i ühendab keegi teine kui autor. Ülevaataja küsimusele vastatakse enne.
- **Aeg:** hinnang loomisel, tegelik aeg sulgemisel. Release notes võrdleb summasid.
- **Blokeerija:** `blocked` ootaval, seos või `blocker` blokeerival Issue'l.
- **AI:** lubatud, aga lühidalt ja kontrollitult. Tiim seletab oma otsuseid ise, ka eksamil.
- **Lingid:** teise repo Issue'le täislink või `ORG/repo#54`; pelk `#54` ei toimi.

<!-- Merge-reegel teeb ülevaatuse päriseks. AI reegel: pikk üldine riskiloend ei ole väärtus; eemaldage ebaoluline ja kontrollige väited. Mõistete test eksamil tehakse ilma AI-ta. Linkide reegel on tehniline, aga ilma selleta ei leia hindaja tööd üles. -->

---

## Tuleviku küsimus refleksiooni

Millist tänase teema tööd võiks teha AI, kuidas tulemust kontrolliksime ja kes vastutaks?

Üks lõik refleksioonis.

<!-- AI oskab pakkuda riskikategooriaid, kirjutada testjuhtumi mustandi ja teha koodile esimese ülevaatuse. Küsimus ei ole, kas AI võib, vaid kuidas tulemust kontrollitakse ja kes vastutab. Riskiloend, mille AI pakub, on üldine; testjuhtum tuleb proovida läbi; koodi kirjutanud agent ei saa enda tööd heaks kiita. Vastutus jääb rollile. -->

---

## Tänased mõisted eksami testiks

kvaliteediomadus ehk mittefunktsionaalne nõue · kvaliteedinõue ja kontrolltingimus · testjuhtum · risk, eeldus ja maandus · WIP-piirang · blokeerija · `git log`, `git diff`, `git restore`

Kodutöös: viga, silumine ja koodi ülevaatus.

Test eeldab seletust oma sõnadega ja oma projekti näidet.

<!-- Test on lühike, individuaalne ja ilma AI-ta. Selles on ainult mõisted, mida on seminaris või kodutöös päriselt käsitletud. See küsib sama, mida täna harjutused: mis mõiste on oma sõnadega ja mida see teie projektis tähendas. -->
