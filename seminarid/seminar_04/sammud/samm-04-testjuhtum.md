# Seminar 4, samm 4: Testjuhtum oma kasutajaloost

**Mis see on:** testjuhtum kirjeldab ette, kuidas kontrollida, et kasutajaloo kontrolltingimus on täidetud. Kontrolltingimus ütleb, *mis* peab olema tõsi. Testjuhtum ütleb, *kuidas* seda kontrollida: eeldused, sammud ja oodatud tulemus. Rakendust meil ei ole, seega kirjutame testi enne ehitamist. Nii tehakse ka päriselus: test on valmis enne, kui arendaja tööd alustab.

**Näide** seminari 3 näidisloost 1 (`seminar_03/user-stories-example.md`):

| Väli | Sisu |
|---|---|
| Test | T1: valitud rühm on telefonis nähtav |
| Lugu | Lugu 1 |
| Eeldused | Telefon, ekraani laius kuni 400 px. Kasutaja on valinud rühma RIF26. |
| Sammud | 1. Ava tunniplaan. 2. Ava menüü ja vali rühm RIF26. 3. Sulge menüü. 4. Keri lehte allapoole. |
| Oodatud tulemus | Rühma nimi RIF26 on kogu aeg nähtav ilma menüüd avamata. |
| Tegelik tulemus | Täidetakse, kui süsteem on olemas. Praegu võib testi proovida praeguse tunniplaani lehe peal: see näitab, kas probleem päriselt esineb. |

**Seminaris:** iga tiim kirjutab ühe testjuhtumi koos. Kodutöös kirjutab iga õppija ühe testjuhtumi enda kasutajaloo kohta.
