# Koodi kvaliteet

Koodi kvaliteet viitab koodibaasi üldisele kvaliteedile ja hooldatavusele. See hõlmab koodi erinevaid aspekte, sealhulgas selle loetavust, järjepidevust, lihtsust, hooldatavust ja usaldusväärsust. Kvaliteetset koodibaasi on aja jooksul lihtsam mõista, muuta ja hooldada, mis võib säästa arendusmeeskondade aega ja ressursse.

![WTF-s in minute](files/wtf.png)  
[Pildi allikas](http://zpalexander.com/content/images/2017/09/wtf.png)

Siin on mõned tegurid, mis võivad koodi heale kvaliteedile kaasa aidata.

- **Loetavus** (*Readability*): kood peaks olema kergesti loetav ja arusaadav. See peaks olema hästi struktureeritud ja organiseeritud, järjekindlate nimetamisreeglite, vahede ja taandega.
- **Järjepidevus** (*Consistency*): kood peaks olema stiililt ja lähenemisviisilt ühtne. See hõlbustab teistel arendajatel koodi mõistmist ja muutmist.
- **Lihtsus** (*Simplicity*): kood peaks olema lihtne ja arusaadav. See vähendab vigade tõenäosust ning muudab koodi aja jooksul muutmise ja hooldamise lihtsamaks.
- **Hooldatavus** (*Maintainability*): kood peaks olema aja jooksul hooldatav. See tähendab, et nõuete muutumisel peaks seda olema lihtne muuta, parandada ja värskendada.
- **Töökindlus** (*Reliability*): kood peaks olema töökindel ja prognoositav. See peaks töötama ootuspäraselt ja käsitlema vigu selliselt, et need ei põhjusta programmi töös tõrkeid.


## Kuidas tagada koodi kvaliteeti?

Järgnevalt mõned punktid, kuidas tagada koodi kvaliteeti:

- **Järjepidev koodi vormindamine** (*Consistent Code Formatting*): koodivormingu järjepidevus muudab arendajatel koodibaasi mõistmise ja hooldamise lihtsamaks. Kasutage koodibaasi ühtse stiili jõustamiseks koodilinterit või vormindustööriista, nagu Prettier või [ESLint](../eslint/about.md).

**Kommentaarid ja dokumentatsioon** (*Code Comments and Documentation*): koodibaasi dokumenteerimine kommentaaride, dokumentatsiooni ja tekstisiseste märkustega on hea tava tagamaks, et arendajad saavad koodist aru ja seda muuta.

**Ühiktestimine** (*Unit Testing*): koodi automaattestide kirjutamine aitab tagada, et see toimib ootuspäraselt ja et koodibaasi muudatused ei too kaasa uusi vigu ega probleeme. Javascripti ühiktestide kirjutamiseks ja käitamiseks saab kasutada näiteks selliseid tööriistu nagu [Jest](https://jestjs.io/) või [Mocha](https://mochajs.org/).

**Koodiülevaatused** (*Code Reviews*): Koodide ülevaatused teiste arendajate poolt võib olla väärtuslik tööriist, mis tagab koodi kõrge kvaliteedi. Koodiülevaatused võimaldavad teistel arendajatel koodimuudatusi üle vaadata, täiustusi soovitada ning vigu või probleeme tabada.

**Vigade käsitlemine** (*Error Handling*): vigade korrektne käsitlemine koodis võib aidata tagada selle töökindluse ja prognoositavuse. Veenduge, et vigu käsitletakse kogu koodibaasis järjepidevalt ning et veateated on arendajatele informatiivsed ja abistavad.

**Kaasaegsete JavaScripti funktsioonide kasutamine** (*Use of Modern JavaScript Features*): kaasaegsete JavaScripti funktsioonide (nt noolefunktsioonid, destruktureerimine ja malliliteraalid) kasutamine võib aidata parandada koodi kvaliteeti. Need funktsioonid võivad muuta koodi kokkuvõtlikumaks ja hõlpsamini loetavaks.

**Koodi refaktoreerimine** (*Code Refactoring*): Refaktoreerimine on olemasoleva koodi täiustamise protsess, muutmata selle käitumist. Refaktoreerimine võib aidata parandada koodi kvaliteeti, muutes selle loetavamaks, hooldatavamaks ja skaleeritavamaks.

Neid tavasid järgides saate tagada, et teie JavaScripti kood on kvaliteetne ja aja jooksul hõlpsasti hooldatav.

Allikad ja lisalugemist:
- https://blog.cleancoder.com/
- https://github.com/jnguyen095/clean-code/blob/master/Clean.Code.A.Handbook.of.Agile.Software.Craftsmanship.pdf
- https://github.com/ryanmcdermott/clean-code-javascript