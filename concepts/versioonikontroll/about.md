# Versioonikontrollisüsteem (Version Control System)

## Mis on versioonikontroll?

Versioonikontroll on süsteem, mis jälgib ja haldab aja jooksul failides tehtud muudatusi. See on tarkvaraarenduse põhikomponent, mis aitab arendajatel jälgida oma koodi muudatusi ja teha tõhusat koostööd teiste arendajatega.

Oma põhiolemuselt on versioonikontroll failide muudatuste haldamise viis. Iga kord, kui faili muudetakse, luuakse uus versioon, mis kajastab tehtud muudatusi. Need muudatused võivad hõlmata koodi muudatusi, uute funktsioonide lisamist või vigade parandamist. Versioonikontrollisüsteemid võimaldavad arendajatel hõlpsasti vaadata ja võrrelda faili erinevaid versioone, tuvastada, kes muudatused tegi ja millal muudatused tehti.

Versioonikontroll on oluline mitmel põhjusel.

1. **Koostöö:** versioonihaldus muudab arendajatel projektide kallal koostöö tegemise lihtsamaks. See võimaldab mitmel arendajal töötada sama koodibaasiga ja aitab vältida konflikte, mis võivad tekkida, kui sama faili kallal töötab mitu inimest.

2. **Ajalugu ja jälgimine:** versioonikontrollisüsteemid jälgivad failides aja jooksul tehtud muudatusi, pakkudes muudatuste ajalugu, mille abil saab mõista, kuidas kood on aja jooksul arenenud. See on oluline silumiseks, tõrkeotsinguks ja auditeerimiseks.

3. **Muudatuste tagasivõtmine:** versioonikontrollisüsteemid muudavad muudatuste tagasipööramise või ekslikult tehtud muudatuste tagasivõtmise lihtsaks. See võib olla väga oluline hetkel, kui koodibaasi siseneb kriitiline viga ja see tuleb kiiresti parandada.

4. **Hargnemine ja ühendamine:** versioonikontrollisüsteemid võimaldavad arendajatel töötada samaaegselt mitme koodibaasi versiooniga. Seda tehakse harude loomisega, mis on koodi iseseisvad koopiad, millega saab eraldi töötada. Kui harus tehtud muudatused on põhikoodibaasi lisamiseks valmis, saab need omavahel uuesti ühendada.

Üldiselt on versioonikontroll tänapäevase tarkvaraarenduse võtmetööriist, mis aitab meeskondadel tõhusamalt koostööd teha, koodi muudatusi hallata ning tarkvaraprojektide stabiilsust ja usaldusväärsust tagada.

## Versioonikontrolli tüübid

Versioonikontrollisüsteeme on kahte peamist tüüpi:

- tsentraliseeritud versioonikontroll;
- hajutatud versioonikontroll.

### Tsentraliseeritud versioonikontrollisüsteem (CVCS)

Tsentraliseeritud versioonihaldussüsteemil, nagu nimigi ütleb, on keskserver, mis salvestab kõik failid ja haldab erinevate kasutajate tehtud muudatusi. Kui kasutaja soovib faili kallal töötada, peab ta esmalt keskserverist faili koopia "välja võtma" (check out). See takistab mitmel kasutajal sama faili samaaegset muutmist, mis võib põhjustada konflikte. Tsentraliseeritud versioonihaldussüsteemide näideteks on CVS ja Subversion (SVN).

### Hajutatud versioonikontrollisüsteem (DVCS)

Hajutatud versioonihaldussüsteemis on igal kasutajal oma koopia kogu koodibaasist, sealhulgas selle ajaloost. See võimaldab kasutajatel töötada keskserverist sõltumatult ja hõlbustab võrguühenduseta või lahtiühendatud võrkudes töötamist. Iga kasutaja tehtud muudatused salvestatakse lokaalselt, kuni need on valmis teiste kasutajatega jagamiseks. Kui muudatused on jagamiseks valmis, lükatakse (`push`) need kesksesse hoidlasse (`repository`) või tõmmatakse (`pull`) need teiste kasutajate hoidlatest. Hajutatud versioonihaldussüsteemide näidete hulka kuuluvad Git ja Mercurial.

Viimastel aastatel on hajutatud versioonihaldussüsteemid, nagu Git, muutunud tarkvaraarendusmeeskondade seas populaarsemaks tänu nende paindlikkusele, kiirusele ja võimele toetada koostööl põhinevaid arendustöövooge. Kuid nii tsentraliseeritud kui ka hajutatud versioonihaldussüsteemidel on oma eelised ja kompromissid ning valik, millist süsteemi kasutada, sõltub konkreetse projekti konkreetsetest vajadustest ja piirangutest.