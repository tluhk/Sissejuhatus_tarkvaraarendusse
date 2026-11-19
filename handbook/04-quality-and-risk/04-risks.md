# Riskid

**Märge:** Seminaris

**Risk** on võimalik sündmus, mis võib projekti või kasutajat kahjustada. Risk ei ole lihtsalt halbade asjade nimekiri. See on otsustamise vahend: millele tähelepanu pöörata, mida kontrollida ja kes reageerib.

## Risk ja eeldus

**Eeldus** on väide, mida peame tõeseks, kuigi pole seda kontrollinud. Iga kontrollimata eeldus on risk.

| | Näide |
|---|---|
| **Eeldus** | „Tunniplaani andmed on tõenäoliselt olemas ja neid saab kasutada.” |
| **Risk** | „Andmeallikas ei sisalda tulevasi kuupäevi või selle kasutamine pole lubatud. Siis ei saa me järgmist loengut näidata.” |
| **Maandus** | „Kontrollime enne kavandi jätkamist, millised väljad andmeallikas on ja kas neid tohib kasutada.” |

> [!IMPORTANT]
> Eeldus ei vähenda riski. „Andmed on tõenäoliselt olemas” ei ole maandus, vaid täpselt see, mida tuleb kontrollida.

Pane eeldused kavandis eraldi kirja. Siis on näha, mida veel ei teata.

## Riskikaart

Kirjelda iga riski kohta:

| Väli | Küsimus |
|---|---|
| **Mis võib juhtuda** | Mis sündmus? |
| **Mõju** | Kellele ja kui tõsine? (madal / keskmine / kõrge) |
| **Tõenäosus** | Kui tõenäoline? (madal / keskmine / kõrge) |
| **Kuidas märkame** | Mis märk näitab, et risk on realiseerumas? |
| **Maandus** | Mida teeme, et risk oleks väiksem või mõju väiksem? |
| **Vastutaja** | Milline roll reageerib? |

Vastutaja on **roll**, näiteks arhitekt või projektijuht. „Meeskond” ei ole vastutaja: kui kõik vastutavad, ei reageeri keegi.

### Näide (väljamõeldud)

| Mis võib juhtuda | Mõju | Tõenäosus | Kuidas märkame | Maandus | Vastutaja |
|---|---|---|---|---|---|
| Andmeallikas ei sisalda tulevasi kuupäevi | kõrge: põhiline lugu ei täitu | keskmine | testime andmeallikat näidispäringuga | kontrollime välju enne kavandi jätkamist | arhitekt |
| Laadimise tõrget tõlgendatakse kui tunni ärajäämist | kõrge: õppija jääb tunnist eemale | keskmine | testjuhtum T3 | eraldi teade „andmeid ei õnnestunud laadida” | arendaja |
| Muutunud tund on märgitud ainult värviga | keskmine: osa kasutajaid ei märka | kõrge | ligipääsetavuse kontroll | lisame tekstimärgi „muutunud” | UX-disainer |

Alusta riskidest, mille mõju **ja** tõenäosus on kõrged.

### Mida riskiga teha

- **Vältida:** muuta kavandit nii, et risk kaob, näiteks mitte koguda isikuandmeid.
- **Vähendada:** teha midagi, mis vähendab tõenäosust või mõju.
- **Üle kanda:** anda vastutus kellelegi teisele, näiteks teenusepakkujale lepinguga.
- **Aktsepteerida:** teadlikult jätta nii, kui maandamine on kallim kui võimalik kahju.

## Kolmandad osapooled

Teek, pilveteenus, andmestik, font või AI-mudel kiirendab tööd, kuid toob kaasa **sõltuvuse**. Iga sõltuvuse kohta kontrolli:

- kasutustingimused ja litsents (vt [Litsentsid](../02-from-request-to-task/03-licences.md));
- kuhu andmed liiguvad;
- hind praegu ja tulevikus;
- kas teenust arendatakse edasi;
- kas seda saab vajadusel asendada.

Näiteks 2019. aastal põhjustas üks vigane tarkvaramuudatus Cloudflare'i võrgus ülemaailmse katkestuse, mis viis maha tuhandeid neid kasutavaid veebilehti ([järelanalüüs](https://blog.cloudflare.com/cloudflare-outage/)). Need lehed ise ei teinud midagi valesti, kuid sõltusid ühest teenusest.

## Risk muudab otsust

Uus risk võib tähendada, et varasem otsus tuleb üle vaadata. See ei ole läbikukkumine, vaid see, milleks riskianalüüs on. Kirjuta otsuste logisse uus otsus: mis risk ilmnes, mida see muutis ja mida otsustasite.

## Kontrolli ennast

1. Mis vahe on riskil ja eeldusel?
2. Miks ei ole „meeskond” sobiv riski vastutaja?
3. Kirjuta oma projekti suurima kontrollimata eelduse kohta üks riskikaardi rida.
4. Too näide, kus riski saab vältida disaini muutes.

---

[← Vea silumine ja koodi ülevaatus](03-debugging-and-code-review.md) | [Sisukord](../README.md) | [Järgmine: Koodi kvaliteet →](05-code-quality.md)
