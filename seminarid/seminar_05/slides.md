---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 5 – kasutuselevõtt, käitus ja areng
---

# Seminar 5

## Kasutuselevõtt, käitus ja areng

---

# Millal tarkvaraarendus lõpeb?

---

## Release ei ole finiš

Päris kasutuses ilmnevad uued vajadused, vead ja kõrvalmõjud.

Süsteemi tuleb jälgida, toetada, muuta ja lõpuks ka lõpetada.

---

## Väljund, tulemus ja mõju

**Väljund:** mida valmis tegime?

**Tulemus:** mida inimene saab teisiti teha?

**Mõju:** kuidas algne probleem pikema aja jooksul muutub?

---

# Kas funktsiooni valmimine tõestab probleemi vähenemist?

---

## Ei

Mõju kontrollimiseks on vaja lähtetaset, sobivat märki ja päris tagasisidet.

---

## Kasutuselevõtu küsimused

- kes alustab ja millal?
- kuidas kasutaja muudatusest teada saab?
- millist tuge ta vajab?
- korraga või sammhaaval?
- millal peatame või pöördume tagasi?
- kes otsustab järgmise versiooni?

---

## Seire ühendab vaatenurgad

- süsteemi tehniline seis
- kasutaja edukus ja takistused
- toe pöördumised
- turbe- ja privaatsusjuhtumid
- mõju algsele probleemile

---

# Kas rohkem kasutajaid tähendab alati suuremat mõju?

---

## Edevusmõõdik või otsustusmõõdik?

Hea mõõdik aitab teha otsuse.

Küsi iga näitaja juures: mida me teeme teisiti, kui see muutub?

---

## Pärisprojekti peegel

MOJ digimeeskond läks tagasi juba toimiva teenuse juurde:

- kasutajad ja töökorraldus muutuvad
- varasem arusaam vananeb
- üksikute ekraanide asemel tuleb vaadata teenuse tervikut

[Allikas](https://mojdigital.blog.gov.uk/2026/03/18/what-we-learned-from-revisiting-a-live-service/)

---

# Milline teie projekti oletus võib aasta jooksul vananeda?

---

## Tehniline võlg

Tulevikku lükatud töö võib muuta järgmised muudatused raskemaks või riskantsemaks.

Otsetee hind ja tagasimaksmise vajadus peavad olema nähtavad.

---

# Millal tuleks süsteem lõpetada?

---

## Ka lõpetamine on arendusotsus

Arvestada tuleb kasutajate, andmete, asendusteenuse, lepingute ja sõltuvustega.

---

## Vabatahtlik AI-demo

Tehke ainult siis, kui see kontrollib olulist oletust.

Enne alustamist leppige kokku:

- küsimus ja tagasisideallikas
- maksimaalne ajakulu
- katkestamise tingimus
- väljundi kontroll

---

# Kas töötav demo on alati kasulik?

---

## Ainult siis, kui sellest õpitakse

Palju parandamist vajav või ebaoluline AI-väljund on kulu, mitte saavutus.

Dokumenteerige tegelik kasu.

---

## Release'ide ajajoon

```text
v0.1.0 probleem
  → v0.2.0 tööviis ja kontseptsioon
  → v0.3.0 kvaliteet ja riskid
  → v0.4.0 kasutuselevõtt ja areng
  → v1.0.0 protsessi tervik
```

---

# Kas ajajoon peab näitama kõiki commit'e?

---

## Ei

Valige sündmused, mis näitavad arusaamise, otsuse või põhjenduse muutumist.

---

## Tänane meeskonnatöö

1. Vahetage rollid.
2. Kavandage kasutuselevõtt ja tugi.
3. Valige otsustamiseks vajalikud märgid.
4. Kirjeldage hooldus ja lõpetamine.
5. Alustage release'ide ajajoont.

---

# Kodutöö

## `v0.4.0 – Kasutuselevõtu ja arengu plaan`

Iga õppija: sisuline panus, PR, ülevaatus ja refleksioon.

