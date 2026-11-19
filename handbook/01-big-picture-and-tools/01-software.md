[← Osa ülevaade](README.md) | [Sisukord](../README.md) | [Järgmine: Tarkvaraarenduse elutsükkel ja AI →](02-sdlc-and-ai.md)

# Tarkvara ja tarkvaraarendus

**Märge:** Seminaris

Enne tarkvaraarendust tuleb teada, mis on tarkvara.

## Programm

**Programm** on arvutile antud käskude kogum, mille abil täidetakse mingit ülesannet. Programm võib näiteks arvutada kahe arvu summa, kuvada veebilehte, töödelda pilti, juhtida valgusfoori või otsida andmebaasist vajalikku teavet.

Programm kirjutatakse mõnes programmeerimiskeeles, näiteks JavaScriptis, Pythonis või Javas. Seda teksti nimetatakse **lähtekoodiks** (*source code*).

## Tarkvara

**Tarkvara** (*software*) on programmist laiem mõiste. See on kõik, mis paneb riistvara kasulikku tööd tegema. Tarkvara võib koosneda:

- ühest või mitmest programmist;
- lähtekoodist;
- andmetest;
- seadistustest;
- dokumentatsioonist;
- välistest teekidest ja teenustest.

Näiteks pangarakendus telefonis ei ole üks programm. Selle taga on telefoni rakendus, serverid, andmebaasid, makseteenuste ühendused, seadistused ja juhendid. Kasutaja näeb neist ainult väikest osa.

Tarkvara vajab töötamiseks **riistvara** (*hardware*): telefoni, sülearvutit, serverit, autot või mõnda väikest elektroonikaseadet. Seadmed erinevad protsessori, mälu ja ekraani poolest, seega tuleb tarkvara loomisel arvestada, kus see töötama hakkab.

## Tarkvara tüübid

Tarkvara saab jaotada selle järgi, mis ülesannet see täidab ja kus see töötab.

| Tüüp | Mida teeb | Näited |
|---|---|---|
| **Süsteemitarkvara** | Aitab seadmel töötada ja teistel programmidel jooksta | Windows, macOS, Linux, Android, seadmedraiverid |
| **Rakendustarkvara** | Aitab kasutajal mingit ülesannet täita | Tekstitöötlus, veebibrauser, pildiredaktor |
| **Veebirakendus** | Töötab brauseri kaudu, selle osad asuvad serverites | Veebipood, e-post brauseris, õppeinfosüsteem |
| **Mobiilirakendus** | Töötab telefonis või tahvelarvutis | Pangarakendus, sõidujagamise rakendus |
| **Sardtarkvara** (*embedded software*) | On ehitatud füüsilise seadme sisse ja juhib seda | Auto juhtplokk, pesumasin, nutikas termostaat |

Paljusid rakendusi ei paigaldata enam oma arvutisse, vaid neid kasutatakse internetiteenusena. Seda nimetatakse **SaaS**-iks (*Software as a Service*, tarkvara teenusena). Näiteks GitHub, mida kursusel kasutame, on SaaS-teenus.

Piirid ei ole alati selged. Üks tarkvaratoode koosneb sageli mitut tüüpi osadest: mobiilirakendus, veebirakendus ja serveris töötav süsteem võivad kõik kuuluda samale teenusele.

### Avatud ja suletud lähtekood

Tarkvara saab jaotada ka selle järgi, kas lähtekood on kõigile nähtav.

- **Avatud lähtekoodiga** (*open source*) tarkvara lähtekoodi saab igaüks vaadata. Litsentsi tingimustel saab seda ka muuta ja levitada. Näiteks VS Code'i alus, Git ja Linux.
- **Suletud lähtekoodiga** ehk omanduslikku (*proprietary*) tarkvara lähtekood kuulub omanikule ja kasutamist piirab litsents. Näiteks Microsoft Office ja paljud mängud.

Avatud lähtekood ei tähenda alati tasuta tarkvara ega suletud lähtekood alati tasulist. Kasutusõigused määrab **litsents**. Litsentsidest räägime täpsemalt osas 4.

## Tarkvara roll ühiskonnas

Tarkvara on osa peaaegu igast valdkonnast: suhtlus, haridus, pangandus, kaubandus, transport, tervishoid, avalikud teenused, tööstus ja teadus. Suur osa igapäevaelust sõltub tarkvarast, mida me ei näe.

Seetõttu on tarkvaral tagajärjed. Halvasti kavandatud või testitud tarkvara võib põhjustada andmekadu, rahalist kahju, privaatsuse rikkumist või ohtu inimese tervisele. Ei piisa sellest, et programm „minu arvutis töötab”.

Hea tarkvara vastab kasutaja vajadusele ning on oma kasutuskohas piisavalt töökindel, turvaline, arusaadav ja hooldatav.

## Tarkvaraarendus

**Tarkvaraarendus** (*software development*) on protsess, mille käigus uuritakse probleemi, kavandatakse lahendus, luuakse tarkvara, kontrollitakse selle kvaliteeti ning hooldatakse seda pärast kasutuselevõttu.

> [!IMPORTANT]
> Tarkvaraarendus ei võrdu programmeerimisega. Programmeerimine ehk koodi kirjutamine on üks osa tarkvaraarendusest.

Tarkvaraarendus hõlmab ka probleemi ja kasutajate vajaduste mõistmist, nõuete kirjeldamist, lahenduse kavandamist, töö planeerimist, testimist, avaldamist ja hooldamist. Programm, mis töötab, kuid ei lahenda kasutaja probleemi, ei ole õnnestunud tarkvara.

Tarkvara ei loo tavaliselt üks inimene. Arendusse panustavad kasutajad ja tellija, tooteomanik, analüütik, disainer, arendaja, testija ning süsteemi- ja turvaspetsialistid. Ühes projektis võib üks inimene täita mitut rolli, teises tegeleb iga rolliga terve meeskond. Rollidest räägime täpsemalt osas 3.

## Kontrolli ennast

Vali üks tarkvara, mida kasutad iga päev, ja vasta:

1. Millist probleemi see lahendab ja kes on selle kasutajad?
2. Mis tüüpi tarkvaraga on tegu? Kas see koosneb mitut tüüpi osadest?
3. Millest see koosneb lisaks nähtavale kasutajaliidesele?
4. Mis juhtuks, kui see töötaks valesti?
5. Kes peale programmeerija võisid selle loomises osaleda?

---

[← Osa ülevaade](README.md) | [Sisukord](../README.md) | [Järgmine: Tarkvaraarenduse elutsükkel ja AI →](02-sdlc-and-ai.md)
