# Kasutajalood ja nõuded

**Märge:** Seminaris

Lähteülesanne ütleb, milline probleem lahendatakse. **Nõuded** ütlevad, mida süsteem peab tegema, et probleem saaks lahendatud. Sellel lehel jõuame kontrollitud probleemist kasutajalugudeni.

```text
probleem ja tõendid → kasutaja teekond → kasutajalood → süsteemi kontseptsioon
```

## Kasutaja teekond

**Kasutaja teekond** (*user journey*) kirjeldab samm-sammult, kuidas kasutaja praegu oma eesmärgini jõuab. Teekond on sild probleemi ja kasutajalugude vahel: see näitab, **millises sammus** probleem tekib.

Näide (väljamõeldud): õppija otsib oma järgmist loengut.

1. Avan tunniplaani.
2. Valin oma rühma.
3. Valin ajavahemiku.
4. Leian järgmise loengu aja ja ruumi.
5. Kontrollin, et vaatan oma rühma tunniplaani.

Tõendid näitasid, et raskused on sammudes 2–5. Sammus 1 probleemi ei leitud, seega selle kohta lugu ei kirjutata.

## Kasutajalugu

**Kasutajalugu** (*user story*) kirjeldab, mida kindel kasutaja tahab teha ja miks:

> [Kasutaja]na soovin [tegevust või võimalust], et [saavutatav väärtus].

Iga loo juurde kuulub **kontrolltingimus** (*acceptance criterion*): mille järgi saab hiljem kontrollida, kas vajadus on täidetud.

Näide (väljamõeldud):

> **Teekonna samm:** 5, kontroll
>
> **Lugu:** Õppijana soovin telefonis kogu aeg näha, millise rühma tunniplaani vaatan, et ma ei peaks kahtlema, kas info on minu oma.
>
> **Tõend:** vaatlus telefonis: pärast menüü sulgemist ei olnud valitud rühma nimi näha.
>
> **Kontrolltingimus:** telefonivaates on valitud rühma nimi nähtav ilma menüüd avamata.

Kasutajalugu on **funktsionaalne nõue**: see kirjeldab, mida süsteem peab võimaldama.

### Hea lugu

- lähtub tõendist, mitte arvamusest, AI vastusest või lahendusideest;
- kirjeldab vajadust, mitte valmis lahendust;
- on seotud teekonna sammuga, kus probleem esineb;
- on kontrollitav: kontrolltingimust saab päriselt kontrollida;
- on piisavalt väike, et mahtuda ühte Issue'sse.

### Halvad näited

| Lugu | Mis on valesti |
|---|---|
| „Õppijana soovin moodsat kalendrivaadet.” | kirjeldab lahendust, mitte vajadust; kontrolltingimust ei saa kirjutada |
| „Kasutajana soovin, et tunniplaan oleks parem.” | pole teada, kes on kasutaja, mis on parem ja kuidas seda kontrollida |
| „Õppijana soovin näha loengu keelt.” | tõend pärineb teise kooli lehelt, mitte meie kasutajatelt |

Sellised teemad lähevad lahtiste küsimuste alla, mitte backlog'i.

### Kattuvad ja vastuolulised lood

Kui kaks lugu lähtuvad samast vajadusest, **ühenda** need üheks. Jäta alles sõnastus, mis kirjeldab vajadust, mitte lahendust, ja märgi ühendamise põhjus PR-i kommentaari.

Kui lood on vastuolus, näiteks üks kasutaja tahab rohkem infot ja teine vähem, ära vali ühte oma äranägemise järgi. Pane vastuolu lahtiste küsimuste alla ja kontrolli seda kasutajatega.

### Kui palju lugusid on vaja?

Lood katavad ainult neid teekonna samme, kus probleem esineb. Kogu süsteemi ei pea lugudega katma. Kontrolli:

1. Kas igal sammul, kus probleem esineb, on vähemalt üks lugu?
2. Kas iga lugu on seotud mõne teekonna sammuga? Kui ei ole, on see tõenäoliselt lahendusidee.

## Funktsionaalsed ja mittefunktsionaalsed nõuded

| | Funktsionaalne nõue | Mittefunktsionaalne nõue |
|---|---|---|
| **Küsimus** | mida süsteem teeb? | kui hästi süsteem seda teeb? |
| **Näide** | õppija näeb oma järgmise loengu aega ja ruumi | leht avaneb telefonis alla 2 sekundiga |
| **Näide** | valitud rühm on kogu aeg nähtav | lehte saab kasutada ekraanilugejaga |

**Mittefunktsionaalsed nõuded** (*non-functional requirements*) ehk **kvaliteediomadused** on näiteks kiirus, turvalisus, töökindlus, kasutatavus, ligipääsetavus ja hooldatavus. Ka need peavad olema kontrollitavad: „kiire” ei ole nõue, „avaneb alla 2 sekundiga” on.

Kvaliteediomadusi käsitleme põhjalikumalt osas 4.

## Kontrolli ennast

1. Miks kirjutatakse lood teekonna sammude kaupa, mitte süsteemi osade kaupa?
2. Paranda lugu „Õppijana soovin push-teavitusi”: mis vajadus selle taga võiks olla?
3. Kirjuta üks kasutajalugu koos kontrolltingimusega oma igapäevase rakenduse kohta.
4. Kas „süsteem peab olema turvaline” on hea mittefunktsionaalne nõue? Kuidas seda parandada?

---

[← Tööviisid](ways-of-working.md) | [Sisukord](../README.md) | [Järgmine: Backlog →](backlog.md)
