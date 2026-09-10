# Seminar 4: kvaliteet, riskid ja vastutus

## Eesmärk

Seminari lõpuks õppija:

- mõistab kvaliteeti eri osaliste vaatenurgast;
- eristab funktsiooni kvaliteediomadusest;
- nimetab projekti olulised riskid ja vastutajad;
- seob kvaliteedivajaduse kontrollimise viisiga;
- arvestab turvalisuse, privaatsuse, ligipääsetavuse, töökindluse ja litsentsidega;
- dokumenteerib, kuidas risk muudab varasemat otsust.

## Põhiküsimus

> Kas kavand on piisavalt hea ja vastutustundlik?

## Töötamine ei võrdu kvaliteediga

Süsteem võib teha nõutud tegevuse, kuid olla aeglane, ebaturvaline, raskesti kasutatav, ligipääsmatu või kallis hooldada. Kvaliteet tähendab sobivust päris kasutusolukorda.

### Funktsioon ja kvaliteediomadus

- Funktsionaalne vajadus: mida süsteem võimaldab teha?
- Mittefunktsionaalne vajadus ehk kvaliteediomadus: kui hästi või millistel tingimustel peab see toimuma?

Nõrk: „Süsteem peab olema kiire.”

Kontrollitavam: „Kasutaja saab tavapärase koormuse ajal otsingutulemuse kahe sekundi jooksul.”

Kõike pole võimalik maksimeerida. Suurem turvalisus võib lisada samme, suurem töökindlus võib tõsta hinda ja kiirem tarne võib kasvatada hooldusvõlga. Kompromiss peab olema teadlik.

## Kvaliteedi vaatenurgad

- **Kasutaja:** kas saan eesmärgi turvaliselt ja arusaadavalt täita?
- **Organisatsioon:** kas tulemus loob väärtust ja vastab kohustustele?
- **Arendaja:** kas süsteemi saab mõista ja muuta?
- **Käitaja:** kas rikkeid saab märgata, piirata ja taastada?
- **Ühiskond:** kellele võib süsteem kahju teha või ligipääsu sulgeda?

## Risk kui otsustamise vahend

Risk ei ole pelgalt halbade asjade nimekiri. Kirjeldage:

1. mis võib juhtuda;
2. kellele ja milline mõju tekib;
3. kui tõenäoline ja tõsine see on;
4. kuidas riski ennetame või vähendame;
5. kuidas saame teada, et risk realiseerub;
6. kes vastutab reageerimise eest.

## Pärisprojekti peegel: Cloudflare'i 2019. aasta katkestus

Cloudflare kirjeldas avalikus järelanalüüsis, kuidas vigane tarkvaramuudatus põhjustas laialdase teenusekatkestuse. Probleemi mõju suurendas muudatuse kiire ülemaailmne levitamine. Ettevõte taastas teenuse tagasipööramisega ja nimetas protsessi ning testimise parandused.

Arutage:

1. Kas põhjus oli ainult ühes vigases reas?
2. Millised kontrollid oleksid mõju piiranud?
3. Kes vastutab, kui tehniliselt korrektne protsess võimaldab ohtliku muudatuse?

Allikas: [Cloudflare outage caused by bad software deploy](https://blog.cloudflare.com/cloudflare-outage/)

## Turvalisus ja privaatsus

Küsige enne andmete kogumist:

- kas neid andmeid on eesmärgi jaoks vaja;
- kellel on neile ligipääs;
- kui kaua neid hoitakse;
- mis juhtub lekke või vale ligipääsu korral;
- kuidas inimene saab aru, mida tema andmetega tehakse.

## Ligipääsetavus ja kaasavus

Ärge kirjeldage „keskmist kasutajat”. Mõelge nägemise, kuulmise, motoorika, keele, seadme, võrgu ja digioskuse erinevustele. Ligipääsetavust tuleb kavandada algusest, mitte lisada lõpus.

## Kolmandad osapooled ja litsentsid

Teek, pilveteenus, andmestik, font või AI-mudel võib kiirendada tööd, kuid toob kaasa sõltuvuse. Kontrollige vähemalt kasutustingimusi, litsentsi, andmete liikumist, hinda, jätkusuutlikkust ja asendatavust.

## Seminari praktiline töö

1. Vaadake üle `v0.2.0` ja vahetage rollid.
2. Valige projekti jaoks 4–6 tähtsaimat kvaliteediomadust.
3. Sõnastage iga omaduse juurde vähemalt üks kontrollitav kriteerium.
4. Koostage riskikaart: mõju, tõenäosus, ennetus, märkamine, vastutaja.
5. Vaadake üle varasemad otsused. Muutke vähemalt üht, kui riskianalüüs seda nõuab.
6. Looge `decisions/004-kvaliteet-ja-riskid.md`.

## Kontrollpunkt

- kvaliteedivalikud lähtuvad probleemist ja kasutusolukorrast;
- vähemalt üks oluline kompromiss on kirjas;
- riskidel on maandus, kontroll ja vastutaja;
- turvalisus, privaatsus ja ligipääsetavus pole unustatud;
- GitHub Issues ja PR-id näitavad iga õppija panust.

## Kodutöö ja release

[Kodutöö 4: release `v0.3.0`](homework.md)

