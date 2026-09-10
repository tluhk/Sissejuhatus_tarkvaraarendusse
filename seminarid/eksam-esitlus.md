# Eksam: dokumenteeritud tarkvaraarenduse protsessi esitlus

## Ülesanne lühidalt

Meeskond vormistab release'i `v1.0.0 – Tarkvaraarenduse protsessi tervik` ja esitleb oma projekti release'ide ajajoonena. Esitlus peab näitama, kuidas probleemist, tõenditest, rollide vaadetest ja riskidest kujunesid põhjendatud otsused.

Valmis rakendus ei ole nõutav. Hinnatakse arusaamist ja põhjendamist, mitte tehnilist keerukust, teksti hulka ega visuaalset efekti.

## Eksami eeldus

Meeskonnal on GitHubis release'id `v0.1.0` kuni `v0.4.0`, otsuste logi, release notes'id ja iga õppija refleksioonid. Puuduv või lõpetamata osa tuleb teha nähtavaks; seda ei tohi esitluses valmis tööna näidata.

## Lõplik release `v1.0.0`

Enne esitlust:

1. vaadake läbi kõik olulised otsused ja nende ajalugu;
2. parandage vastuolud või märkige need teadlikult avatuks;
3. lõpetage `releases/ajajoon.md`;
4. lisage `releases/v1.0.0.md`;
5. ühendage üle vaadatud PR-id;
6. looge tag `v1.0.0` ja GitHub Release pealkirjaga `Tarkvaraarenduse protsessi tervik`.

Release ei tähenda, et kavandatud süsteem on valmis. See fikseerib kursusel dokumenteeritud arendusprotsessi terviku.

## Esitluse struktuur

1. **Probleem ja algne arusaam** – kelle probleem, millises olukorras ja millise mõjuga?
2. **`v0.1.0`** – mida kontrolliti ja mida tõend muutis?
3. **`v0.2.0`** – kuidas valiti tööviis ja süsteemi kontseptsioon?
4. **`v0.3.0`** – millised kvaliteedi- ja riskivalikud muutsid kavandit?
5. **`v0.4.0`** – kuidas süsteem kasutusele jõuaks, areneks ja lõpeks?
6. **AI kasutamine** – millise otsuse juures, kuidas kontrolliti ja mis oli tegelik kasu?
7. **Tervik** – mida meeskond nüüd tarkvaraarendusest teisiti mõistab?

Ebaolulistest commit'idest ja väikestest muudatustest võib üle hüpata. Vähemalt ühe muutunud või tagasi võetud otsuse käsitlemine on oluline.

## Esitluskorraldus

- Soovituslik aeg: 15 minutit esitlust ja 10 minutit küsimusi meeskonna kohta.
- Iga õppija esitleb vähemalt üht release'i või olulist otsust.
- Iga õppija vastab enda rolli, panust ja refleksiooni puudutavatele küsimustele.
- Esitlus viitab repositooriumis olevatele otsustele ja release'idele.
- Demo on vabatahtlik ja peab jääma lühikeseks. See ei asenda protsessi selgitust.

## Hindamine

| Hinnatav osa | Osakaal |
|---|---:|
| Otsuste logi ja release'ide sisuline areng | 40% |
| Individuaalsed refleksioonid ning rollide mõistmine | 25% |
| Giti ja GitHubi läbipaistev koostöövoog | 15% |
| Lõpuesitlus ja küsimustele vastamine | 20% |
| **Kokku** | **100%** |

### Otsused ja release'id, 40%

Hinnatakse probleemist lähtumist, alternatiivide võrdlust, põhjendusi, tõendite kasutamist, kompromisse ning seda, kuidas uus info otsuseid muutis.

### Individuaalne arusaamine, 25%

Hinnatakse refleksioonide sisukust, eri rollide vastutuse mõistmist ja võimet selgitada enda panust. Tegevuste loend ilma õppimise analüüsita ei ole piisav.

### Koostöövoog, 15%

Hinnatakse Issues'e, harusid, sisulisi commit'e, PR-e, ülevaatusi, tag'e ja release'e kui meeskonna läbipaistvat tööprotsessi. Commit'ide arv üksi ei näita panuse kvaliteeti.

### Esitlus, 20%

Hinnatakse selget release'ide ajajoont, olulise eristamist ebaolulisest, põhjendatud enesekriitikat ning küsimustele vastamist. Kujundus toetab arusaamist, kuid visuaalne viimistlus ei ole eraldi eesmärk.

## AI kasutamise kontroll

Meeskond peab suutma näidata vähemalt üht olulist otsust, mille juures AI-d kasutati, ning vastata:

- miks AI-d kasutati;
- milline oli sisend;
- mida väljundist kasutati või tagasi lükati;
- kuidas väiteid ja sobivust kontrolliti;
- kas AI vähendas tööd või tekitas lisatööd;
- kes vastutab lõpliku otsuse eest.

Kontrollimata, korduv või ebaoluline AI-materjal vähendab töö selgust ja võib hinnet langetada.

## Enne esitamist

- [ ] `v1.0.0` release ja tag on olemas.
- [ ] Ajajoon näitab olulisi otsuseid ning muutusi.
- [ ] Iga esitluse väide on seostatav repo materjaliga.
- [ ] Iga õppija roll ja panus on nähtav.
- [ ] Iga õppija teab, millist osa ta esitleb.
- [ ] AI kasutus ja kontroll on läbipaistvad.
- [ ] Lahtisi küsimusi ei esitata lõplike faktidena.

