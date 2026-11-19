# Kodutöö 3 kokkuvõte õppijatele (seminar 4 algus, umbes 4–5 minutit)

Tagasiside on teil olemas: tiimi oma on tiimi repos Issue'na „Kodutöö 3 tagasiside” ja igaühe isiklik on tema kodutöö Issue's. Kui midagi on teie arvates valesti hinnatud, kirjutage samasse kohta vastus. Vaatan kõik üle.

Kõigepealt hea uudis. **Sisulise mõtlemisega saite hakkama paremini, kui ma ootasin.**

- Teie kasutajalood räägivad kasutaja vajadusest, mitte tehnilistest ülesannetest. Mitu ülevaatust märkas ise, et „teise värviga” on juba lahendus, mitte vajadus. Just seda oskust ma tahtsingi näha.
- Kõik tiimid panid kirja, mis jääb süsteemist välja. Ametlik tunniplaan jääb andmete allikaks ja teie ehitate selle peale vaate.
- Arhitektuuri kirjeldasite peaaegu kõik osade ja nende vastutuse kaudu, ilma frameworkideta.
- Mõnes töös oli eraldi läbi mõeldud, mis juhtub, kui andmed jäävad laadimata. Kasutajale tähendab „täna loenguid pole” hoopis muud kui „andmed jäid laadimata”. Selline mõtlemine on järgmises etapis väga vajalik.

Nüüd see, mis jäi kättesaamatuks. Peaaegu kõik puudujäägid olid **töö korraldamises**, mitte sisus.

1. **Valitud tööviisi tuleb ka järgida.** Enamik valis Kanbani. Kanbani mõte on see, et tahvlilt näeb, mis on pooleli ja kus töö seisab. Mitmes tiimis ei liikunud kaardid töö ajal või jõudsid kõik korraga Done'i viimasel õhtul. Kui tööviis on ainult kirjas, aga tahvlit ei kasutata, ei saa seda valikut lugeda tugevaks. Projectsi tahvli kasutamine on kursuse nõue. Leppige kokku, et iga kaart liigub Backlog → In progress → Review → Done siis, kui töö päriselt edeneb.

2. **Ajakulu pange kirja töö ajal, mitte tagantjärele.** Ainult üks tiim võrdles hinnangut ja tegelikku aega Issue'de kaupa. Lihtne viis on panna Projectsis hinnang välja Estimate ja lisada teine numbriväli „Tegelik (h)”. Hinnangu paned Issue'i loomisel, tegeliku aja sulgemisel. Siis on release notes'i võrdlus valmis ja te näete ise, millist tööd alahindate.

3. **Backlog tuleb tootest, mitte kodutööst.** Paljude backlog koosnes kodutöö sammudest: kasutajalugu, release, refleksioon. Ülesanne ütles, et backlog'i Issue'd tulenevad kasutajalugudest. Head näited on „kontrolli, kas tunniplaani andmeallikas annab valikainete info” või „tee kontrolltingimusest testjuhtum”. Sellised Issue'd näitavad, mida toode vajab.

4. **Ülevaatus on rohkem kui „Korras”.** Parimad ülevaatused küsisid midagi konkreetset ja selle peale tehti muudatus. Üldine heakskiit ei aita autorit. Teine asi: PR-i ei ühenda autor ise, seda teeb ülevaataja.

5. **Merge-konflikti harjutus õnnestus enamikul.** Kommentaaris pange kirja kolm asja: millises failis ja osas konflikt tekkis, kelle muudatustega ja mis jäi alles. Kui teises tiimis keegi seda kommentaari loeb, saab ta kohe aru.

Paar tehnilist asja, mis tulevad ka kodutöös 4:

- **Esitamiskommentaaris kasutage täislinke.** Teie isiklikus repos ei viita `#54` tiimi repo PR-ile, sest number seotakse selle repoga, kus kommentaar asub. Kasutage täis-URL-i või kuju `TLUHK-RIF26/tiim-XX-tunniplaan#54`.
- **Refleksioon käib faili `reflections/eesnimi-perenimi-v0.3.0.md`.** Kaust on väikese tähega ja faililaiend `.md`. Mõnel oli fail mujal või teise nimega. Sisu loeti ikkagi, aga palun pange see õigesse kohta.

Kõige olulisem asi järgmiseks korraks. Viis tiimi kuuest jätsid lahtiseks sama küsimuse: kas ja kuidas saab tunniplaani andmeid kätte ning millised väljad seal on. See on kõigi teie lahenduste suurim risk. Täna räägime kvaliteedist ja riskidest ning alustame just sellest.

Lõpetuseks AI-st. AI kasutamine on lubatud ja paljud kirjeldasid seda ausalt. Jätkake samamoodi. Pidage aga meeles, et järgmine etapp ehitab teie otsuste peale. Seega peab tiim oskama oma disaini, arhitektuuri ja tööviisi ise seletada. Tänane esimene harjutus ongi selline: seletate oma otsuseid arvutita.
