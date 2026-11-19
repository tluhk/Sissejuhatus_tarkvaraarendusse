# Harjutus 3: Üks testjuhtum kavandi peal

**Tegija:** tiim koos. **Aeg:** 15 minutit. **Fail:** `tests/test-cases.md` tiimi repos.

## Eesmärk

Kontrolltingimus ütleb, mis peab olema tõsi. Testjuhtum ütleb, kuidas seda kontrollida. Rakendust pole, seega tehakse test kavandi peal: kui kavand annab igale sammule vastuse, on test läbitud; kui ei anna, on kavandis auk. Teooria: [Testjuhtum](../../../../handbook/04-quality-and-risk/02-test-cases.md).

## Tegevused

1. Valige oma põhiline kasutajalugu ja selle kontrolltingimus, võimaluse korral harjutuse 2 rida.
2. Täitke väljad: test, lugu, eeldused, sammud, oodatud tulemus.
3. Käige sammud läbi kasutaja teekonna ja arhitektuuri järgi. Kirjutage tegelikuks tulemuseks see, mida kavandi järgi igal sammul juhtub.
4. Kui kavand mõnele sammule vastust ei anna, looge Issue „Kavandis puudub: …” ja märkige test läbikukkunuks.
5. Commit ja push seminari lõpuks.

## Faili näide

Näide on väljamõeldud; asendage oma looga.

```markdown
# Testjuhtumid

Vastutab: tiim (või testija, kui roll on lisatud).

## T1: valitud rühm on telefonis nähtav

- **Lugu:** lugu 1, kontrolltingimus K1
- **Eeldused:** telefon, ekraani laius kuni 400 px; kasutaja on valinud rühma A
- **Sammud:**
  1. Ava tunniplaan.
  2. Ava menüü ja vali rühm A.
  3. Sulge menüü.
  4. Keri lehte allapoole.
- **Oodatud tulemus:** rühma nimi A on kogu aeg nähtav ilma menüüd avamata.
- **Tegelik tulemus kavandi järgi:** teekond ütleb sammud 1–3; samm 4 kohta kavand ei ütle, kas päis jääb kerimisel nähtavale. **Läbi kukkunud**, Issue #17.
```

## Kontrollpunkt

Harjutus on valmis, kui teine tiimiliige saab sammud lugeda ja öelda, mida kavandi järgi igal sammul juhtub. Kodutöös kirjutab iga õppija ühe testjuhtumi oma loo kohta ja vähemalt üks tiimi test katab vea olukorda, näiteks andmed ei lae.
