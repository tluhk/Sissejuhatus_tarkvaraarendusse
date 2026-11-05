# Näidis: probleemist kasutajalugudeni

See näide on väljamõeldud. See näitab, kuidas valideeritud probleemist saavad kasutaja teekond, mitu kasutajalugu ja backlog. Teie lood peavad lähtuma teie tiimi kogutud tõenditest, ärge kopeerige neid.

## 1. Probleem (`v0.1.0` lähteülesanne)

**Peamine kasutaja:** kolledži tudeng, kes otsib oma järgmise loengu infot.

**Olukord:** tudeng avab tunniplaani telefonis enne kooli tulekut või loengute vahel.

**Vajadus:** leida kiiresti järgmise loengu kuupäev, kellaaeg ja ruum ning olla kindel, et vaatab oma rühma tunniplaani.

**Takistus:** rühma ja ajavahemiku valimine nõuab mitut sammu ja telefonis ei ole valitud rühm pärast menüü sulgemist näha.

**Mida tiim ei vali veel:** kujundust ega konkreetset lahendust.

### Tõendid

| Tõend | Mida näitas | Tugevus |
|---|---|---|
| Vaatlus telefonis | Pärast menüü sulgemist ei ole valitud rühma nimi näha. Selle kontrollimiseks tuleb menüü uuesti avada. | Konkreetne ja korratav, kuid vaatles üks tiimiliige |
| Vestlused kolme tudengiga | Kaks pidasid rühma valimist tüütuks. Üks soovis, et tänased loengud oleksid kohe näha. Üks vaatab tunniplaani harva ja tal probleeme pole. | Väike valim, arvamused lähevad lahku |
| Ülikooli ametlik juhend | Oma rühma tunniplaanini jõudmiseks on vaja vähemalt nelja valikut. Valikained on teises süsteemis (ÕIS). | Usaldusväärne allikas, kuid kolledži lehe vastavus on kontrollimata |
| Teise ülikooli tunniplaani võrdlus | Seal näidatakse lisainfot: loengu keel ja tüüp ning link ainekavale. | Näitab võimalust, mitte meie kasutajate vajadust |

### Lahtised küsimused

- Mitu sammu ja kui palju aega kulub tudengil praegu järgmise loengu leidmiseks? Seda pole mõõdetud.
- Kas kolledži leht kasutab sama töövoogu, mida kirjeldab ülikooli juhend?
- Kui tihti tudengid tunniplaani vaatavad?

## 2. Kasutaja teekond

1. Avan tunniplaani.
2. Valin oma rühma.
3. Valin ajavahemiku või vaate.
4. Leian järgmise loengu aja ja ruumi.
5. Kontrollin, et vaatan oma rühma tunniplaani.

Lood kirjutatakse teekonna etappide kaupa, mitte süsteemi osade kaupa.

## 3. Kasutajalood

### Lugu 1: valitud rühm on telefonis nähtav

**Etapp:** 5 – kontroll

**Lugu:** Tudengina soovin telefonis kogu aeg näha, millise rühma tunniplaani vaatan, et ma ei peaks kahtlema, kas info on minu oma.

**Tõend:** vaatlus telefonis.

**Kontrolltingimus:** telefonivaates on pärast menüü sulgemist valitud rühma nimi nähtav ilma menüüd avamata.

**Autor:** Tiimiliige A (UX-disainer)

**Ülevaataja:** Tiimiliige B

**Märkus:** tõend on hea, sest see on konkreetne ja kontrollitav. Kas see segab ka teisi tudengeid, on kontrollimata.

### Lugu 2: järgmine loeng on kohe nähtav

**Etapp:** 4 – järgmise loengu leidmine

**Lugu:** Tudengina soovin pärast rühma valimist kohe näha oma järgmise loengu kuupäeva, kellaaega ja ruumi, et saaksin selle loengute vahel kiiresti üle vaadata.

**Tõend:** probleemisõnastuse vajadus ja ühe tudengi soov näha tänaseid loenguid kohe.

**Kontrolltingimus:** valitud rühma järgmise loengu kuupäev, kellaaeg ja ruum on nähtavad ilma lisavalikuta nii telefonis kui ka arvutis.

**Autor:** Tiimiliikmed B (analüütik) ja C (projektijuht), vt [ühendamine](#4-kattuvate-lugude-ühendamine)

**Ülevaataja:** Tiimiliige D

### Lugu 3: oma rühmani vähemate sammudega

**Etapp:** 2–3 – rühma ja vaate valimine

**Lugu:** Tudengina soovin jõuda oma rühma tunniplaanini vähemate valikutega, et ma ei peaks iga kord sama valikut uuesti tegema.

**Tõend:** kaks tudengit pidas rühma valimist tüütuks; ülikooli juhendi järgi on vaja vähemalt nelja valikut.

**Kontrolltingimus:** kasutajatestis jõuab tudeng oma järgmise loenguni vähemate sammudega kui praegu.

**Autor:** Tiimiliige C (projektijuht)

**Ülevaataja:** Tiimiliige A

**Märkus:** kontrolltingimus vajab lähtetaset. Enne tuleb mõõta, mitu sammu see praegu võtab.

### Lugu 4: tunniplaanis on ka valikained

**Etapp:** 4 – järgmise loengu leidmine

**Lugu:** Tudengina soovin näha oma valikaineid koos kohustuslikega, et mu tunniplaan oleks terviklik.

**Tõend:** ülikooli juhendi järgi näitab rühmavaade ainult kohustuslikke aineid ja valikained on ÕIS-is.

**Kontrolltingimus:** tudengi tunniplaanis on kõik tema õpingukavas olevad ained ja ainult need.

**Autor:** Tiimiliige D (arendaja)

**Ülevaataja:** Tiimiliige C

**Märkus:** lugu sõltub välisest süsteemist, mida tiim ei kontrolli. See ei sobi esimeseks tööks, kuid peab kontseptsioonis olema nähtav sõltuvuse ja riskina.

## 4. Kattuvate lugude ühendamine

Tiimiliikmed B ja C kirjutasid algul kaks lugu:

> **B:** Tudengina soovin, et tunniplaan avaneks tänase päeva peal, et ma ei peaks kerima.
>
> **C:** Tudengina soovin näha oma järgmist loengut ilma lisavalikuteta, et jõuaksin õigel ajal õigesse ruumi.

Mõlemad lähtuvad samast vajadusest ja tõendist. Kontrolltingimused kattusid suures osas. Tiimiliige D märkis ülevaatuses, et esimene lugu kirjeldab lahendust („avaneks tänase päeva peal”), teine aga vajadust.

**Otsus:** tiim ühendas need looks 2. Sõnastus võeti loost C, sest see kirjeldab vajadust. Loost B jäi alles nõue, et info peab olema nähtav ilma lisavalikuta. Ühendamine ja selle põhjus on kirjas PR-i kommentaaris ning loo 2 autori real.

Kui lood on vastuolus, näiteks üks tudeng tahab rohkem infot ja teine vähem, ei vali tiim ühte. Vastuolu läheb lahtiste küsimuste alla ja seda kontrollitakse kasutajatega.

## 5. Halvad näited

| Lugu | Mis on valesti |
|---|---|
| „Tudengina soovin moodsat kalendrivaadet.” | Kirjeldab lahendust, mitte vajadust. Tõendit ega kontrolltingimust pole. |
| „Tudengina soovin näha loengu keelt ja tüüpi.” | Tõend pärineb teise ülikooli lehelt, mitte meie kasutajatelt. |
| „Kasutajana soovin, et tunniplaan oleks parem.” | Pole teada, kes on kasutaja, mis on parem ja kuidas seda kontrollida. |

Need teemad lähevad lahtiste küsimuste alla, mitte backlog'i.

## 6. Mis edasi

1. **Lähtetase:** 2–3 tudengit leiavad telefonis ja arvutis oma järgmise loengu. Loetakse kokku sammud ja aeg. Ilma selleta ei saa lugude 2 ja 3 kontrolltingimusi hinnata.
2. **Jaotus:** iga tiimiliige kirjutab ühe loo ja vaatab PR-is üle kaaslase loo.
3. **Backlog:** lood 1–3 lähevad Projectsi Issue'dena koos ajahinnanguga. Lugu 4 jääb sõltuvuse taha.
4. **Süsteemi kontseptsioon:**
   - teekond tuleb punktist 2;
   - osalised on tudeng ja tunniplaani koostaja;
   - välised sõltuvused on tunniplaanisüsteem ja ÕIS;
   - piir: puudumisest teatamine jääb süsteemist välja.
5. **Seminar 4:** kontrolltingimustest saavad testjuhtumid ja lugu 4 läheb riskide alla.
