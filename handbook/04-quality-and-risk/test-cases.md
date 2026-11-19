# Testjuhtum

**Märge:** Seminaris

**Testimine** võrdleb oodatud tulemust tegeliku tulemusega kindlates tingimustes. Testimine võib leida vea, aga ei selgita veel selle põhjust.

## Kontrolltingimusest testjuhtumini

Kasutajaloo **kontrolltingimus** ütleb, *mis* peab olema tõsi. **Testjuhtum** (*test case*) ütleb, *kuidas* seda kontrollida.

| Väli | Sisu |
|---|---|
| **Test** | lühike nimi ja number |
| **Lugu** | millise kasutajaloo kontrolltingimust see kontrollib |
| **Eeldused** | mis peab olema enne testi tõsi: seade, andmed, kasutaja olek |
| **Sammud** | täpsed tegevused järjekorras |
| **Oodatud tulemus** | mida peab nägema, kui kõik on korras |
| **Tegelik tulemus** | mida päriselt nähti; täidetakse testi tegemisel |

Testjuhtumi saab kirjutada enne, kui süsteemi on olemas. Nii tehakse ka päris projektides: test on valmis enne, kui arendaja tööd alustab, ja arendaja teab, mille järgi tema tööd kontrollitakse.

## Näide (väljamõeldud)

Lugu: „Õppijana soovin telefonis kogu aeg näha, millise rühma tunniplaani vaatan.”

| Väli | Sisu |
|---|---|
| **Test** | T1: valitud rühm on telefonis nähtav |
| **Eeldused** | Telefon, ekraani laius kuni 400 px. Kasutaja on valinud rühma A. |
| **Sammud** | 1. Ava tunniplaan. 2. Ava menüü ja vali rühm A. 3. Sulge menüü. 4. Keri lehte allapoole. |
| **Oodatud tulemus** | Rühma nimi A on kogu aeg nähtav ilma menüüd avamata. |
| **Tegelik tulemus** | *Täidetakse testimisel.* |

Kui süsteemi veel pole, võib sama testi proovida praeguse lahenduse peal. See näitab, kas probleem päriselt esineb.

## Testi ka seda, mis võib valesti minna

Hea testide komplekt ei kontrolli ainult tavalist olukorda. Mõtle ka erijuhtudele:

| Test | Eeldus | Oodatud tulemus |
|---|---|---|
| T2: tühi nädal | valitud nädalal tunde pole | kasutaja näeb teadet „sel nädalal tunde pole” ja järgmise koolipäeva kuupäeva |
| T3: andmed ei lae | andmeallikas ei vasta | kasutaja näeb teadet „andmeid ei õnnestunud laadida”, mitte tühja tunniplaani |

T2 ja T3 näevad kasutajale esmapilgul ühesugused välja: tunde pole näha. Tegelikult on need väga erinevad olukorrad. Kui süsteem neid ei erista, võib õppija arvata, et tund jäi ära.

## Testimise tasemed

*See lõik on iseseisvaks lugemiseks.*

| Tase | Mida kontrollib | Kes teeb |
|---|---|---|
| **Ühiktest** (*unit test*) | üht väikest koodiosa, näiteks ühte funktsiooni | arendaja, tavaliselt automaatselt |
| **Integratsioonitest** | kas osad töötavad koos, näiteks vaade ja andmeallikas | arendaja või testija |
| **Süsteemitest** | kogu süsteemi nõuete järgi | testija |
| **Vastuvõtutest** (*acceptance test*) | kas süsteem rahuldab kasutaja vajadust | kasutaja või tellija |

Kasutajaloo testjuhtum, mida kursusel kirjutame, on vastuvõtutest.

**Automaattest** on kood, mis kontrollib teist koodi. Seda saab käivitada iga muudatuse järel sekunditega. **Käsitsi test** tehakse inimese poolt sammude järgi. Mõlemat on vaja: automaattest on kiire ja korratav, käsitsi test leiab asju, mida keegi ette ei osanud kirjutada.

## Kontrolli ennast

1. Mis vahe on kontrolltingimusel ja testjuhtumil?
2. Miks saab testjuhtumi kirjutada enne, kui süsteemi on olemas?
3. Kirjuta testjuhtum oma ühe kasutajaloo kohta kõigi viie väljaga.
4. Mõtle oma loo kohta üks erijuhtum, mida tavaline test ei kata.

---

[← Mõõdetav kvaliteet](measurable-quality.md) | [Sisukord](../README.md) | [Järgmine: Vea silumine ja koodi ülevaatus →](debugging-and-code-review.md)
