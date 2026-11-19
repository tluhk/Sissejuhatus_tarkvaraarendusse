# Seminar 4, samm 2: Projectsi tahvli ja `v0.2.0` läbivaatus, rollivahetus

Kestus 20 minutit, arvutid lahti. Õpetaja on Teamsi kaudu klassi ekraanil, ei liigu laudade vahel ega näe paberit. Seepärast kirjutab tiim kõik vastused GitHubi, kus õpetaja neid reaalajas näeb. Õpetaja juhendis on see rida „`v0.2.0` ülevaade, Projectsi tahvli läbivaatus, rollivahetus ja backlog'i uuendamine”. Eelmine samm on kodutöö 3 esitlus, järgmine on „Ebamäärasest mõõdetavaks”.

## Eesmärk

Tiim näeb ise, kas tööviis ja plaan olid päriselt kasutusel, ning parandab selle enne kodutööd 4. Õpetaja ei loe ette, mis oli valesti. Tiim leiab selle oma tahvlilt ja release'ist.

Tulemus seminari lõpuks:
- uued rollid `v0.3.0` jaoks on kokku lepitud;
- igal tiimil on Projectsis väljad Estimate ja „Tegelik (h)” ning tabelivaade, kus hinnangut ja tegelikku aega saab võrrelda;
- `v0.2.0` läbivaatusest on tekkinud vähemalt üks Issue koos hinnanguga;
- igal tiimil on Issue „`v0.2.0` läbivaatus”, kus on tahvliküsimuste vastused ja kontrollnimekirja tulemus.

## Ettevalmistus (õpetaja, enne seminari)

- Küsi tiimilt 02 luba näidata nende tahvlit aja jälgimise näitena. Ava see oma brauseris valmis, et jagada Teamsis ainult seda akent.
- Tee endale proovitahvel ja kontrolli, et menüüd (`+` → New field, tabelivaade, rühmitamine Statuse järgi) vastavad GitHubi praegusele kasutajaliidesele. Sellel tahvlil näitad plokis „Aja jälgimine” väljade lisamist.
- Pane kolm tahvliküsimust ja release manageri kontrollnimekiri slaidile, mis on sammu ajal klassi ekraanil. Postita sama tekst ka Teamsi vestlusesse, et tiimid saaksid selle kopeerida.
- Ava eraldi aknas kõigi tiimide repode Issues-lehed. Sealt näed, kes on vastuseid kirjutamas.
- Hoia endal vihjete leht (allpool). Seda õppijatele ei jagata ega näidata jagatud ekraanil.

## Käik

### 0:00–1:00 Sissejuhatus

Ütle umbes nii: „`v0.3.0` ehitame `v0.2.0` peale. Enne vaatame, kas see, mida me tööviisi kohta kirjutasime, oli tahvlil ka näha. Kõigil tiimidel on midagi parandada, ka neil, kellel läks hästi.”

Üks arvuti tiimi kohta: lahti on Projectsi tahvel ja `v0.2.0` release'i leht. Tiim loob kohe Issue „`v0.2.0` läbivaatus” ja kirjutab sinna kõik selle sammu vastused. Klassi ekraanil on taimer.

### 1:00–6:00 Tahvel (5 min)

Tiim vastab Issue'sse kolmele küsimusele:

1. Mis on olekus Backlog või In progress? Kas see on päriselt pooleli või unustati tahvlil liigutada?
2. Mitmel kaardil on ajahinnang? Mitmel on tegelik aeg? Vihje: veeru päises olev „Estimate: …” on selle veeru hinnangute summa.
3. Millal kaardid liikusid olekusse Done: töö ajal või lõpus korraga? Kas tahvel aitas teil midagi otsustada?

Kolmas küsimus on kõige tähtsam. Kui vastus on „lõpus korraga”, ei ole see viga, mida karistatakse. See on sisend küsimusele, mida kodutöös 4 teisiti teha.

Teine küsimus kirjeldab lähtekohta, mitte ei otsi süüdlast. Aja jälgimist ei ole seni õpetatud, see tuleb järgmises plokis.

### 6:00–12:00 Aja jälgimine (6 min)

Ütle ausalt: „Eelmises etapis ma aja jälgimist ei õpetanud, seega see ei ole teie viga. Nüüd teeme seda koos.” Seekord õpivad seda kõik tiimid, mitte ainult need, kes selle ise üles leidsid.

**Miks:** hinnangu ja tegeliku aja vahest õpib tiim plaanima. Ilma selleta on iga järgmine plaan sama arvamine.

**Näide:** jaga tiimi 02 tahvlit. Kaartidel on väljad „Hinnang (h)” ja „Tegelik aeg (h)”, release notes'is on lause „peaaegu kõigi Issue'de hinnang oli 1 h, olenemata töö sisust”. Rõhuta, et väärtus ei ole täpses hinnangus. Väärtus on selles, et vahe on näha ja sellest saab järelduse teha.

**Kuidas:** näita oma ekraanil, iga tiimi projektijuht teeb samal ajal oma tahvlil kaasa.

1. **Hinnang:** GitHubi Kanbani mallis on numbriväli Estimate. See on lihtsalt lahter, kuhu kirjutatakse hinnang. Ühikut väli ei tea, selle lepib tiim kokku. Meie ühik on tund. Kui tahvlil Estimate'i pole, lisa see: tahvli paremas servas `+` → New field, tüüp Number. Tiim 02 nimetas välja ümber „Hinnang (h)”-ks. Sisuliselt on see sama.
2. **Tegelik aeg:** lisa uus väli: `+` → New field, tüüp Number, nimi „Tegelik (h)”.
3. **Võrdlus:** lisa tahvlile tabelivaade (Table). Seal on mõlemad veerud kõrvuti. Kui rühmitad tabeli Statuse järgi, näitab Projects iga numbrivälja summat rühma päises. Release notes'i jaoks on hinnangu ja tegeliku aja kogusumma siis kohe olemas. Tahvlivaates näitab veeru päis samuti hinnangute summat.

**Kontrollpunkt:** iga tiimi tahvlil on väljad Estimate ja „Tegelik (h)” ning tabelivaade. Ava enne järgmist plokki iga tiimi tahvel ja vaata see üle.

**Reeglid kodutööks 4:**
1. Hinnang pannakse Issue'i loomisel, mitte hiljem.
2. Tegelik aeg pannakse Issue'i sulgemisel, mitte release'i õhtul.
3. Ühik on tund, täpsus pool tundi (0,5; 1; 1,5 …).
4. Kui tööd tegi mitu inimest, liidetakse nende ajad kokku.

### 12:00–15:00 `v0.2.0` läbivaatus (3 min)

Praegune release manager loeb kontrollnimekirja ette, tiim kontrollib oma repost:

- [ ] Iga väide release notes'is vastab failile (näiteks kui on kirjas „teekond on kirjeldatud”, on teekond failis olemas).
- [ ] Topeltfaile ega kohatäiteid pole.
- [ ] AI juhiseid ega malliteksti pole lõplikus failis.
- [ ] README viitab uutele otsustele (`002`, `003`, `releases/v0.2.0.md`).

Kontrollnimekiri kopeeritakse läbivaatuse Issue'sse ja märgitakse ära. Iga leitud puudus saab eraldi Issue. Kui tiimi Issue's pole 2 minuti jooksul ühtegi puudust, kirjuta vihjelehelt suunav küsimus kommentaarina selle tiimi läbivaatuse Issue'sse, mitte vastus. Ära ütle vihjet Teamsis valjult: klassi kõlaritest kuulevad seda kõik.

See on sama nimekiri, mille release manager peab kodutöös 4 enne `v0.3.0` avaldamist läbi tegema. Ütle seda.

### 15:00–18:00 Rollivahetus (3 min)

Reeglid:
- igaüks saab uue rolli;
- `v0.2.0` release manager ei ole uuesti release manager;
- kolmeliikmelises tiimis on ühel kaks rolli, üle neljaliikmelises tiimis on lisaks tooteomanik.

Rollide vastutus kodutöös 4:

| Roll | Vastutab kodutöös 4 |
|---|---|
| Projektijuht | tahvel ja väljad Estimate, „Tegelik (h)”; esitluse lüngad Issue'na; merge-reegli järgimine |
| Disainer | kvaliteedinõuded tiimi lugudest, mõõdetavad kontrolltingimused |
| Arhitekt | andmeallika risk ja riskikaart |
| Release manager | kontrollnimekiri ja release `v0.3.0` |

Kiireks otsuseks anna vaikimisi ettepanek: roll liigub ringiga **projektijuht → arhitekt → disainer → release manager → projektijuht**. Tiim võib seda muuta, kui reeglid jäävad täidetuks.

| Tiim | Projektijuht | Arhitekt | Disainer | Release manager |
|---|---|---|---|---|
| 01 | Marko | Meeri | Helen | Kauri |
| 02 | Medlin | Mariann | Greete | Alison |
| 04 | Matthias | Rico | Artur | Mattias |
| 07 | Tauri | Martin | Kristo | Kaspar |
| 08 | Aili | Robin | Monika | Thorian |
| 10 | Ursula | Peep | Merilin | Merilin (kaks rolli) |

Tiim 10: Ursula oli haige. Projektijuhi roll on kodutöös 4 korralduslik ja annab talle hea ülevaate. Kui ta seda ei soovi, vaheta Ursula ja Peep.

Rollid kirjutatakse README osasse „Rollid” kodutöö 4 esimeses PR-is, mitte seminaris.

### 18:00–20:00 Backlog'i uuendamine (2 min)

Uus projektijuht teeb, teised vaatavad:

1. Kontrollib, et väljad Estimate ja „Tegelik (h)” on olemas (need lisati plokis „Aja jälgimine”).
2. Loob läbivaatusest tulnud Issue'd ja paneb igaühele hinnangu kohe.
3. Sulgeb või liigutab kaardid, mis on vales olekus.

Toote Issue'd (lugudest ja riskidest) tulevad sammus 7. Kui aeg saab otsa, tehakse punkt 2 seal.

Uued rollid kirjutab projektijuht läbivaatuse Issue'sse ühe reana. Nii näeb õpetaja rollijaotust kohe, kuigi README uuendatakse alles kodutöös.

### Üleminek sammule 3

Uued rollid hakkavad kohe tööle: sammus 3 juhib kvaliteedinõuete ümberkirjutamist uus disainer, sammus 6 riskikaarti uus arhitekt. Esitluses tekkinud lüngad (samm 1) paneb uus projektijuht Issue'na kirja.

## Vihjete leht (ainult õpetajale)

Seis 18.11.2026. Anna vihje küsimusena.

| Tiim | Tahvel | `v0.2.0` | Vihje küsimusena |
|---|---|---|---|
| 01 | 37 kaarti, kõik Done; 24 on mustandid ilma repota; hinnanguid pole | `main`-is kaks `003` faili (`susteemi` ja `süsteemi`); README-s on ka 1. etapi rollid | „Mitu kontseptsioonifaili teil `decisions/` kaustas on?” |
| 02 | 34 kaarti, kõik Done; väljad hinnang ja tegelik aeg on enamikul | README ei viita failidele `002`, `003` ja `v0.2.0` | „Kust uus inimene README-st teie otsused leiab?” |
| 04 | 25 kaarti, kõik Done; hinnang 8 kaardil | release notes ütleb „Tiim on kirjeldanud kasutaja teekonna”, failis on ainult „1. 2. 3. 4.”; README viitab arhitektuurile failis `003`, tegelik on `004` | „Lugege oma teekonda ette.” |
| 07 | 35 kirjet, olek ainult 14-l; tahvlit muudeti 18.11 öösel | suurem osa jõudis `main`-i pärast tähtaega; README ei viita `002` ja `003` failidele | „Mis oli `main`-is 17.11 kell 9?” |
| 08 | 35 kaarti, kõik Done; hinnangu välja pole; lisaks 3 tühja vana tahvlit | release notes: „umbes 40 tunniga, kulus rohkem”; tööviisis lubatud veerge To do ja Review tahvlil pole | „Kus on teie tahvli veerg Review?” |
| 10 | 29 kaarti, 27 Done, 2 Backlog; Estimate ja Priority tühjad | release notes'is on jäänuk „Asenda allolevad märkused õigete linkidega” | „Lugege release notes'i viimane lõik ette.” |

**Tiim 06 (Gerli üksi):** reposse on tehtud ainult README, seega `v0.2.0` läbivaatust ei ole. Gerli loob tahvli koos väljadega Estimate ja „Tegelik (h)” ning 2–3 Issue'd järgmise sammu jaoks. Rollivahetus temale ei kehti, sest tal on kõik rollid.

## Õpetaja vaatlus

Märgi iga tiimi kohta üks rida. Punkte see ei anna. Kõik veerud on näha tiimi läbivaatuse Issue'st ja Projectsist, seega saab tabeli täita ka pärast seminari.

| Tiim | Tahvel töö ajal / tagantjärele | Hinnang ja tegelik aeg olemas | Leidsid `v0.2.0` puuduse ise / vihjega | Uued rollid |
|---|---|---|---|---|
| | | | | |

## Ohukohad

- **Häbistamine.** Klassi ekraan on sinu jagatud ekraan. Jaga ainult slaidi, taimeri või tiimi 02 tahvli akent, mitte kogu ekraani, kus on teiste tiimide repod või vihjete leht. Positiivse näitena näitad ainult tiimi 02, ja ainult nende loal.
- **Õpetaja ei näe klassi.** Kui mõne tiimi Issue's pole 3 minuti järel midagi, küsi Teamsis nimeliselt projektijuhilt, kas neil on küsimus. Ära oleta, et vaikus tähendab tööd.
- **Aja venimine.** Tahvliküsimustele on 5 minutit, mitte rohkem. Taimer on klassi ekraanil, sest kaugelt on raske arutelu katkestada. Pikem arutelu kuulub kodutöösse.
- **„Meil oli kõik korras.”** Küsi, kas tahvlilt on näha, mis järjekorras tööd tehti. Kui ei ole, siis tahvel ei aidanud otsustada.
- **Rollivahetus kui formaalsus.** Uus roll tähendab uut vastutust kodutöös 4 (tabel ülal). Kui keegi ei tea, mida tema roll teeb, loe tema rida tabelist ette.
