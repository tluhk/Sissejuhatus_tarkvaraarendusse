# Merge-konflikti harjutus

**Merge-konflikt** tekib, kui kaks haru muudavad sama kohta failis. Git ei tea, kumb muudatus jätta, ja otsuse teeb inimene. Konflikt tekib PR-i ühendamisel, mitte push'imisel.

See harjutus on [kodutöö 3](homework.md) (`seminarid/seminar_03/homework.md`) samm 4 ja see tehakse kasutajalugude lisamise ajal.

Harjutus käib kasutajalugudega failis `decisions/003-susteemi-kontseptsioon.md`. Näide on 4-liikmelise tiimi kohta; suurema tiimi puhul jätkub ahel samamoodi.

1. Kõik tiimiliikmed loovad oma loo jaoks Issue ja haru **samast `main`-i seisust**, enne kui keegi on midagi ühendanud. Disainer loob kohe ka teise Issue ja haru lugude kokkuvõtte jaoks.
2. Igaüks lisab oma loo osa „Kasutajalood” lõppu, teeb commit'i, push'ib ja avab PR-i.
3. Disaineri loo PR ühendatakse esimesena. Konflikti ei teki.
4. Liikme 2 PR-is näitab GitHub teadet **This branch has conflicts that must be resolved**. Liige 2 lahendab konflikti, push'ib ja PR ühendatakse.
5. Liikmed 3 ja 4 teevad sama.
6. Lõpuks lisab disainer oma teises harus osa „Kasutajalood” lõppu lugude kokkuvõtte: millised lood kattusid ja kuidas need ühendati või täpsustati. Tema PR on nüüd konfliktis ja ta lahendab selle.

Disaineri teine haru jääb lahtiseks kuni ahela lõpuni. Päris töös hoitakse harud lühikesena, et konflikte oleks vähem; siin teeme vastupidi teadlikult, et konflikt tekiks.

Konflikti lahendamise käsud on [konfliktide lahendamise juhendis](../../concepts/mergeConflict/README.md) (`concepts/mergeConflict/README.md`). Lahendamisel jäävad alles kõigi lood; parandage vajadusel lugude numbrid.

**Kontrollpunkt:** failis pole märke `<<<<<<<`, `=======` ega `>>>>>>>`, kõik lood ja kokkuvõte on alles ning kõik PR-id on ühendatud.

Konflikti lahendaja kirjutab oma PR-i kommentaari:

- millises failis ja osas konflikt tekkis;
- kelle muudatustega see kokku puutus;
- mis jäi alles ja miks.
