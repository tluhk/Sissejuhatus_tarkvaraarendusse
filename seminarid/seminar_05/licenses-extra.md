# Litsentsid tarkvaraarenduses (lisatund)

> **Märkus:** See materjal on mõeldud lisatunniks või iseseisvaks õppimiseks. Põhiseminar ei hõlma seda teemat ajapuuduse tõttu.

---

## Avatud ja suletud lähtekood

---

## Mis on avatud lähtekood?

**Avatud lähtekood** = tarkvara lähtekood on avalikult kättesaadav

**Peamised põhimõtted:**
- **Vaba juurdepääs**: igaüks saab koodi vaadata
- **Vaba levitamine**: koodi saab vabalt jagada
- **Vaba muudatus**: koodi saab muuta
- **Vaba kasutamine**: kasutada igal eesmärgil

---

## Avatud lähtekoodiga tarkvara näited

**Operatsioonisüsteemid:**
- Linux, Android

**Veebiserverid:**
- Apache, Nginx

**Programmeerimiskeeled:**
- Python, Java

**Andmebaasid:**
- MySQL, PostgreSQL

**Veebiprojekteerimise teegid:**
- React, Angular, Vue

---

## Miks valida avatud lähtekood?

**Eelised:**

✅ **Koostöö** - suur hulk inimesi saab koos töötada

✅ **Innovatsioon** - ideed levivad kiiresti

✅ **Kvaliteet** - rohkem inimesi leiab vigu

✅ **Turvalisus** - haavatavused avastatakse kiiremini

✅ **Kulude kokkuhoid** - sageli tasuta või odav

---

## Millal mitte valida avatud lähtekoodi?

❌ **Vajad täielikku kontrolli** - suletud lähtekood annab rohkem kontrolli

❌ **Vajad kiiret toetust** - professionaalne tugi võib olla keerulisem

❌ **Tundlikud andmed** - turvalisuse nõuded võivad piirata

❌ **Tahad toodet müüa** - avatud lähtekood võib piirata kommertsialiseerimist

---

## Autoriõiguse loogika

**Oluline reegl:**

```
Kui teosel pole litsentsi
    ↓
On litsentsitud kõige tugevamalt
    ↓
Keegi ei tohi seda kasutada!
```

**Seega:** Kui tahad, et sinu kood oleks kasutatav, **lisa litsents!**

---

## Litsentsid GitHubis

**Miks ei ole GitHubis "täielikult keelavaid" litsentse?**

- GitHub on loodud **avatud lähtekoodiga projektide** jaoks
- Litsentsid on loodud **reguleerima**, mitte keelama
- Kui tahad privaatsust → kasuta **privaatseid repositooriume**

**Litsentsid reguleerivad:**
1. Muudatuste tegemine
2. Kommertsialiseerimine
3. Autorite õiguste kaitse

---

## MIT License - Kõige vabam

```
"Tee minu asjadega, mida tahad,
 aga ära mind kohtusse kaeba."
```

**Lubab:**
✅ Vabalt kasutada, muuta ja levitada
✅ Kasutada kommertsiaalselt
✅ Ei nõua muudatuste avaldamist

**Nõuab:**
⚠️ Autoriõiguste märget

**Vali see:** Kui kardad, et keegi ei hakka sinu tarkvara kasutama

---

## Apache License 2.0 - Patendi kaitse

```
"Sama mis MIT, aga rohkemate sõnadega
ja patendikaitsega."
```

**Lubab:**
✅ Sama mis MIT
✅ Lisaks kaitseb patendikasutust

**Nõuab:**
⚠️ Autoriõiguste säilitamist
⚠️ Muudatuste dokumenteerimist

**Vali see:** Kui kardad patenditrollimist või soovid juriidilist selgust

---

## GNU GPL v3.0 - Copyleft

```
"Kui kasutad minu koodi,
peab su kood samuti avatud olema."
```

**Lubab:**
✅ Vabalt kasutada ja muuta

**Nõuab:**
⚠️ Kõik tuletised peavad olema sama litsentsi all
⚠️ Lähtekood peab olema kättesaadav

**Copyleft** = Kõik tuletised jäävad sama litsentsi alla

**Vali see:** Kui kardad, et keegi võiks sinu arvelt raha teenida

---

## GPL näide: Linux ja macOS

**Miks Apple'i macOS ei põhine Linuxil?**

```
Linux kasutab GPL litsentsi
    ↓
See tähendaks, et macOS peaks olema avatud lähtekoodiga
    ↓
Apple ei soovi seda
    ↓
macOS põhineb BSD-l (BSD litsents on vabam kui GPL)
```

---

## Teised olulised litsentsid

**BSD 2-Clause / 3-Clause**
- Sarnane MIT-le, lihtne ja vaba

**Creative Commons Zero (CC0)**
- Loobub kõigist autoriõigustest (avalik omand)

**Mozilla Public License 2.0**
- Võimaldab linkida MPL-koodiga mittevaba tarkvara

**The Unlicense**
- Loobub täielikult autoriõigustest

---

## React.js litsents

**React.js kasutab MIT litsentsi**

**Küsimus:** Kas saate React.js-iga luua täielikult kaitstud toote?

**Vastus:** ✅ JAH!

- React.js kood ise on avatud
- **AGA** teie rakenduse loogika ei muutu automaatselt avalikuks
- Te võite kaitsta oma rakenduse lähtekoodi
- React.js-i kasutamine ei kohusta teid oma koodi avaldama

**Näide:** Facebook kasutab React.js, aga ei jaga facebook.com koodi

---

## HTML, CSS ja JavaScript

**Need on standardid, mitte tarkvara**

```
HTML/CSS/JS ise = standardid (tasuta, nagu grammatika)
Teegid (React, jQuery) = tarkvara (omavad litsentse)
Sinu kood = sinu valik (vali litsents või hoia privaatsena)
```

**Kuid:**
⚠️ Kui kasutad teeke (jQuery, Bootstrap) → neil on litsentsid!
⚠️ Sinu loodud veebilehe disain ja sisu → võib olla autoriõigusega kaitstud

---

## Litsentsi valik - võrdlus

| Omadus | MIT | Apache 2.0 | GPL v3 |
|--------|-----|------------|--------|
| Vaba kasutamine | ✅ | ✅ | ✅ |
| Kommertsiaalne kasutus | ✅ | ✅ | ✅ |
| Muudatused privaatsed | ✅ | ✅ | ❌ |
| Patendi kaitse | ❌ | ✅ | ✅ |
| Copyleft | ❌ | ❌ | ✅ |

---

## Kuidas valida litsentsi?

**4 peamist küsimust:**

1. Kas tahan, et teised saaksid mu koodi **kasutada**?
2. Kas tahan, et teised saaksid mu koodi **muuta**?
3. Kas tahan, et teised saaksid mu koodiga **raha teenida**?
4. Kas tahan, et muudatused oleksid **samuti avatud**?

**Abimees:** https://choosealicense.com

---

## Litsentside dilemma - mäng

**Iga grupp saab ühe dilemma:**

1. **Idufirma** - tehisintellekti rakendus, investorid muretsevad
2. **Kogukonna projekt** - hariduslik platvorm koolidele
3. **Ettevõtte siseprojekt** - sismine tööriist, võib hiljem müüa
4. **Rahvusvaheline koostöö** - äri või avalik projekt?

**Aeg:** 10 min arutelu + 5 min esitlused

---

## Litsentside dilemma - küsimused

**Iga grupp peab vastama:**

- Milline litsents sobib?
- Mis on peamised eelised?
- Millised on potentsiaalsed riskid?
- Kuidas see mõjutab projekti tulevikuplaane?

---

## Litsentsid - kokkuvõte

**Peamised õppetunnid:**

✅ Kui teosel pole litsentsi → keegi ei tohi seda kasutada

✅ MIT = kõige vabam, sobib enamikule projektidele

✅ Apache 2.0 = MIT + patendi kaitse

✅ GPL = Copyleft, nõuab et tuletised oleksid avatud

✅ React.js (MIT) ei kohusta sind oma rakendust avaldama

✅ Litsentsi valik on strateegiline otsus!

---

## Lisalugemist

- [Choose A License](https://choosealicense.com)
- [Open Source Initiative](https://opensource.org/licenses)
- [GitHub Licensing Guide](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [TL;DR Legal](https://tldrlegal.com) - litsentsid lihtsas keeles
