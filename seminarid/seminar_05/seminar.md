# Seminar 5: kasutuselevõtt, käitus ja areng

## Eesmärk

Seminari lõpuks õppija:

- mõistab, et tarkvaraarendus jätkub pärast esimest kasutuselevõttu;
- kavandab kasutuselevõtu, toe, tagasiside ja seire põhimõtted;
- eristab väljundit, tulemust ja mõju;
- mõistab hoolduse, tehnilise võla ja süsteemi lõpetamise rolli;
- koostab release'ide ajajoone ning valmistub protsessi esitama;
- hindab, kas minimaalne AI abil tehtud demonstratsioon loob õppimisele väärtust.

## Põhiküsimus

> Mis juhtub süsteemiga pärast selle loomist?

## Release ei ole finiš

Kasutuselevõtt muudab süsteemi päris keskkonna osaks. Siis ilmnevad uued vajadused, kasutusmustrid, vead ja kõrvalmõjud. Keegi peab süsteemi jälgima, toetama, parandama, uuendama ning lõpuks ka sulgema või asendama.

## Väljund, tulemus ja mõju

- **Väljund:** mida me valmis tegime või avaldasime?
- **Tulemus:** mida inimene saab nüüd teisiti teha?
- **Mõju:** kuidas muutub algne probleem pikema aja jooksul?

Funktsiooni valmimine ei tõesta, et probleem vähenes. Mõju kontrollimiseks on vaja lähtetaset, sobivat märki ja tagasisidet.

## Kasutuselevõtu otsused

Kavandage vähemalt:

- kes ja millal alustab kasutamist;
- kuidas kasutajad muudatusest teada saavad;
- millist juhendamist või tuge nad vajavad;
- kas kasutuselevõtt toimub korraga või sammhaaval;
- kuidas märgatakse probleeme;
- millal muudatus peatatakse või pööratakse tagasi;
- kes otsustab järgmise versiooni sisu.

## Seire ja tagasiside

Hea mõõdik aitab teha otsuse. Pelk külastuste arv võib olla edevusmõõdik, kui see ei näita, kas inimene saavutas eesmärgi.

Ühendage:

- süsteemi tehniline seis;
- kasutaja edukus ja takistused;
- toe pöördumised;
- turbe- ja privaatsusjuhtumid;
- mõju algsele probleemile.

## Pärisprojekti peegel: elava teenuse uuesti uurimine

Ühendkuningriigi justiitsvaldkonna digimeeskond kirjeldas 2026. aastal, miks juba toimiva teenuse juurde tagasi mindi: kasutajate ja töökorralduse vajadused muutuvad ning vana arusaam ei pruugi enam kehtida. Uus discovery aitas teenust vaadata tervikuna, mitte ainult parandada üksikuid ekraane.

Arutage:

1. Milline teie probleemi või kasutuskonteksti osa võib aasta jooksul muutuda?
2. Milline tagasiside ütleks, et lahendus enam ei sobi?
3. Millal tuleks süsteemi parandamise asemel selle eesmärk uuesti läbi mõelda?

Allikas: [What we learned from revisiting a live service](https://mojdigital.blog.gov.uk/2026/03/18/what-we-learned-from-revisiting-a-live-service/)

## Hooldus, tehniline võlg ja lõpetamine

Tehniline võlg on teadlikult või teadmatusest tulevikku lükatud töö, mis muudab järgmised muudatused raskemaks või riskantsemaks. Kõik otseteed pole valed, kuid nende hind ja tagasimaksmise vajadus peavad olema nähtavad.

Ka süsteemi sulgemine on arendusotsus. Tuleb läbi mõelda andmete säilitamine või kustutamine, kasutajate teavitamine, asendusteenus, lepingud ja sõltuvused.

## Vabatahtlik üliminimaalne AI-demo

Demo võib aidata kontrollida üht olulist oletust, kui see mahub väga väikesesse ajapiiri. See ei ole kohustuslik ega asenda süsteemi kontseptsiooni.

Enne alustamist vastake:

- millist oletust demo kontrollib;
- kellelt ja millist tagasisidet vajate;
- mis on maksimaalne ajakulu;
- millal töö katkestate;
- kuidas kontrollite AI väljundit.

Kui demo tekitab palju parandamist vajavat või ebaolulist materjali, on see tulemus, mida tuleb ausalt hinnata.

## Release'ide ajajoon

Koostage lugu olulistest muutustest:

```text
v0.1.0 probleem
   ↓ uus tõend
v0.2.0 tööviis ja kontseptsioon
   ↓ risk või kompromiss
v0.3.0 kvaliteedi- ja riskiplaan
   ↓ kasutuselevõtu küsimused
v0.4.0 kasutuselevõtu ja arengu plaan
   ↓ süntees
v1.0.0 dokumenteeritud protsess
```

Ajajoon ei pea kordama iga commit'i. Valige otsused, mis näitavad arusaama muutumist.

## Seminari praktiline töö

1. Vaadake üle `v0.3.0` ja vahetage rollid.
2. Koostage kasutuselevõtu, toe ja tagasipööramise plaan.
3. Valige 3–5 märki, mis näitavad kasutaja tulemust, süsteemi seisundit ja mõju.
4. Kirjeldage hoolduse omanik ning üks võimalik lõpetamise olukord.
5. Otsustage põhjendatult, kas minimaalne demo annaks vajalikku tõendit.
6. Alustage release'ide ajajoont.
7. Looge `decisions/005-kasutuselevott-ja-areng.md`.

## Kodutöö ja release

[Kodutöö 5: release `v0.4.0`](homework.md)

