# Lühijutt: kuidas AI tarkvaraarendust muudab

Umbes viieminutiline sissejuhatus seminari 3 algusesse. Etappide, rollide ja väidete kirjeldus pärineb allpool viidatud artiklist. Seosed kursusega on eraldi välja toodud.

## Jutt

Seminaris 1 vaatasime tarkvaraarenduse elutsüklit. Täna vaatame, kuidas seda kirjeldab 2026. aasta augustis avaldatud artikkel. Selle avaldas Anthropic, ettevõte, kes ise selliseid tööriistu müüb, ja see arvestab eelkõige suurte organisatsioonidega.

Artikkel jagab arenduse kuueks etapiks: planeerimine, disain, ehitamine, testimine, kasutuselevõtt ja hooldus. Traditsiooniliselt on igal etapil oma omanik. Tootejuhid kirjutavad nõuded, arhitektid teevad neist disaini ja arendajad ehitavad. Reguleeritud ettevõtetes kontrollivad tulemust kvaliteeditiimid, väljalasketiimid viivad selle kasutusse ja käitustiim jälgib töötavat süsteemi. Töö liigub edasi dokumentide, tööülesannete ja kinnituste kaudu.

Artikli väide on, et see korraldus loodi ajal, mil koodi kirjutamine oli kõige aeganõudvam ja kallim etapp. Nüüd kirjutavad agendid artikli järgi koodi palju kiiremini ja kitsaskoht liigub mujale: planeerimisse, ülevaatusse, testimisse ja kasutuselevõttu. Näiteks turvatiimi suurus on arvestatud inimeste töötempoga. Kui agendid kirjutavad palju rohkem koodi, kasvab ülevaatuse järjekord või jõuab kood kasutusse piisavalt läbi vaatamata.

Mida artikkel igas etapis teisiti kirjeldab?

**Planeerimine.** Ideega inimene ei pea olema arendaja. Ta kirjeldab probleemi oma sõnadega ja AI küsib seda, mida küsiks analüütik: ulatus, kasutajad, piirangud ja see, milline näeb välja edu. Tulemus salvestatakse failina `intent.md`. Tooteomanik vaatab selle üle ja parandab.

**Disain.** Nõuded ja disain tehakse ühes töösessioonis. AI koostab organisatsiooni reeglite põhjal kirjelduse `spec.md` ja märgib murekohad. Tooteomanik ei kirjuta kirjeldust ise, vaid vaatab selle üle, lahendab murekohad reegli omanikuga ja otsustab, kas töö liigub edasi. Kõrgema riski korral küsib ta nõu tehniliselt juhilt.

**Ehitamine.** Arendaja laseb AI-l koostada plaani `plan.md`: millised failid muutuvad, mis järjekorras töö käib ja millised testid tulemust tõendavad. Ta küsib, mida muudatus võib katki teha, ja kinnitab plaani enne koodi kirjutamist. Üks arendaja võib juhtida mitut töösessiooni korraga, nii et tema töö nihkub suunamisele ja ülevaatusele. Praktiline piir on see, kui mitut töövoogu suudab üks inimene korralikult üle vaadata.

**Testimine.** Agent saab võimaluse oma tööd kontrollida enne, kui inimene seda näeb: testid, build või ekraanipilt. Vea parandamisel kirjutatakse kõigepealt test, mis ebaõnnestub. Parandav agent ei tohi seda testi muuta.

**Kasutuselevõtt.** AI vaatab iga pull request'i läbi samade reeglite järgi ja järjestab leiud tõsiduse järgi. Inimene hindab, kas muudatus teeb seda, mis plaanis, ja kas risk on vastuvõetav. Koodi kirjutanud agent ei saa seda ise heaks kiita, kinnituse annab koodi omanik. Arenduskeskkonnas võib agent tulemust vabalt avaldada. Tootmises valmistab agent väljalaske ette ja selle lubab release manager.

**Hooldus.** Skript jälgib tootmist. Kui näitaja väljub lubatud vahemikust, käivitab skript AI, mis kirjutab oma diagnoosi uue `intent.md` failina. Teenuse omanik või valves olev arendaja otsustab: parandame kohe, planeerime hiljem või jätame kõrvale. Nii saab lineaarsest protsessist ring.

Iga etapp lõpeb failiga versioonihalduses ja järgmine algab selle lugemisega. See ahel näitab ka hiljem, kes mida küsis, mida agent tegi ja kes selle kinnitas.

Nüüd seos meie kursusega. Ka teie repos jätab iga etapp maha dokumendi. Aga artikkel paneb backlog'i, kasutajalood ja story point'id traditsioonilise töötava poolele ning hindamisrituaalid vana töökorralduse juurde. Meie kursusel neid harjutame, seega märgake seda erinevust.

Ja kolm hoiatust. Esiteks on see müüja tekst. Kiiruse kohta käivad väited on ootused, mõõdetud tulemusi artikkel ei esita. Teiseks ütleb artikkel ise, et enamik organisatsioone on kirjeldatud kahe äärmuse vahel. Kolmandaks kehtib meie kursusel seminarist 2 teada reegel: AI väljund ei ole tõend. Ka artikli järgi jäävad inimesed vastutama iga otsuse eest, mis nõuab hinnangut.

Seminarides 3–5 küsime iga teema juures: millist tööd võiks teha AI, kuidas tulemust kontrollime ja kes vastutab?

## Allikas

Louis Claxton, [The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), Anthropic, 21. august 2026. Ingliskeelne artikkel, lugemisaeg umbes 40 minutit; lugemine on vabatahtlik.
