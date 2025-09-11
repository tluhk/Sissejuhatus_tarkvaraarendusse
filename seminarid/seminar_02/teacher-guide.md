# Seminar 2: õpetaja juhend
## Uurimine - probleemi analüüs ja kasutajate mõistmine

**Kestus**: 3h (90 min teooria + 90 min praktikat)  
**Kuupäev**: [Täita enne seminari]  
**Osavõtjaid**: [Täita enne seminari]

---

## SEMINARI ÜLEVAADE

### Peamine eesmärk
Tudengid mõistavad, mis on tarkvaraarendus ning õpivad arendusprotsessi esimest etappi - probleemi defineerimine ja kasutajate uurimine.

### Õpiväljundid
Seminari lõpuks tudeng:
- **Mõistab tarkvaraarenduse olemust** ja selle erinevust programmeerimisest
- Oskab defineerida ja analüüsida probleeme süstemaatiliselt
- Teab erinevaid kasutajauuringute meetodeid
- Oskab eristada funktsionaalseid ja mitte-funktsionaalseid nõudeid
- Oskab dokumenteerida uurimistulemusi professionaalselt
- Mõistab konkurentsianalüüsi tähtsust

---

## SEMINARI STRUKTUUR

| **Aeg** | **Tegevus** | **Kestus** | **Märkused** |
|---------|-------------|------------|---------------|
| 0:00-0:05 | Sissejuhatus ja ülevaade | 5 min | Slides 2-4 |
| 0:05-0:20 | 1.1 Mis on tarkvaraarendus? | 15 min | Slides 5-9, OLULINE! |
| 0:20-0:40 | 1.2 Probleemi defineerimine | 20 min | Slides 9-13, interaktiivne |
| 0:40-1:05 | 1.3 Kasutajate uurimise meetodid | 25 min | Slides 14-15, näited |
| 1:05-1:25 | 1.4 Nõuete tüübid | 20 min | Slides 16-18, praktiline |
| 1:25-1:40 | 1.5 Konkurentsianalüüs | 15 min | Slides 19-23 |
| **1:40-1:50** | **PAUS** | **10 min** | **Kohustuslik!** |
| 1:50-2:10 | 2.1 Probleemi valimine ja defineerimine | 20 min | Slides 25-26, grupitöö |
| 2:10-2:40 | 2.2 Kasutajate uurimise harjutus | 30 min | Slides 27, rollimäng |
| 2:40-3:05 | 2.3 Nõuete kogumine | 25 min | Slides 28-29, praktiline |
| 3:05-3:20 | 2.4 Konkurentsianalüüs | 15 min | Slide 30-31 |
| 3:20-3:30 | Dokumenteerimine ja kokkuvõte | 10 min | Slides 32-36 |

---

## OSA 1: TEOORIA (90 MINUTIT)

### 🎯 1.1 Mis on tarkvaraarendus? (15 min) - SLIDES 3-9

(5 min):
**Slide 3 - Mis üldse on tarkvaraarendus? Paljud arvavad, et see on lihtsalt programmeerimine, aga tegelikult on see palju laiem."**
Mis on teie arust tarkvara? Mis on tarkvaraarendus?
Millest ta koosneb?

**SLIDE 5 - Tarkvara definitsioon:**
- **RÕHUTA**: Tarkvara ei ole ainult kood! Kolm komponenti on võrdselt olulised.
- **Näide**: "Mõelge WhatsApp-ile. Kood võimaldab sõnumeid saata, andmed on teie vestlused, dokumentatsioon ütleb, kuidas rakendust kasutada."

**SLIDE 6 - Protsess:**
- **JOONISTA tahvlile**: Tsükliline protsess
- **Rõhuta**: "See on jätkuv tsükkel, mitte lineaarne"
- **Küsi tudengitelt**: "Miks on tagasiside oluline?"

ENNE 7 slaidi:
Pakkuge, millistest etappidest võiks tarkvara arendus koosneda?

**SLIDE 7 - Põhietapid:**
- **Läbi iga etapi**: Selgita igat sammavat
- **Rõhuta**: "Meie kursuses läbime iga etapi!"

Enne 8 slaidi:
Küsi tudengitelt, millised rakendused on teie elu muutnud? Et teada või juhtida tähelepanu, miks tarkvaraarendus on oluline – probleemide lahendamine.


**SLIDE 8 - Miks oluline:**
- **Küsi tudengitelt**: "Millised rakendused on teie elu muutnud?"
- **Seo näidetega**: Uber (automatiseerimine), Facebook (kommunikatsioon)

Enne 9 slaidi:  
Interaktiivne hetk (5 min):
"Kes teab, mida teeb toote omanik tarkvaraarenduses?"
- Las tudengid mõtlevad paarides 2 minutit
- Kogu vastused tahvlile
- Selgita toote omaniku rolli
- Selgita toote omaniku rolli:  
  Toote omanik (product owner) on inimene, kes vastutab arendusmeeskonnas selle eest, et arendatav tarkvara vastaks kasutajate ja ärilistele vajadustele. Ta kogub ja prioriseerib nõudeid, suhtleb nii tellija kui ka arendajatega ning otsustab, millised funktsioonid ja muudatused on kõige olulisemad. Toote omanik on justkui sillaehitaja kasutajate, äripoole ja arendajate vahel ning tema ülesanne on tagada, et lõpptulemus lahendaks õigeid probleeme.

#### Kontrollküsimused (5 min):
1. "Mis vahe on tarkvaraarendusel ja programmeerimisel?"  
   **Vastus:** Tarkvaraarendus hõlmab kogu protsessi alates probleemi mõistmisest, nõuete kogumisest, disainist, koodimisest, testimisest kuni juurutamise ja hoolduseni. Programmeerimine (ehk koodimine) on vaid üks osa sellest protsessist – see tähendab koodi kirjutamist.

2. "Nimetage kolm tarkvara komponenti"  
   **Vastus:**  
   - Kood (programmeerimiskeeles kirjutatud juhised)  
   - Andmed (informatsioon, mida tarkvara töötleb)  
   - Dokumentatsioon (selgitused, kuidas tarkvara töötab ja kuidas seda kasutada)

3. "Miks on tarkvara arendamine tsükliline protsess?"  
   **Vastus:** Sest tarkvara arenduses saadakse pidevalt tagasisidet kasutajatelt ja äripoolelt, mille põhjal tuleb lahendust täiustada. Vajadused ja tehnoloogiad muutuvad, seega tuleb tarkvara regulaarselt uuendada ja parandada, et see vastaks kasutajate ootustele ja lahendaks õigeid probleeme.

**SLIDE 9 - Võrdlustabel:**
- **OLULINE MOMENT**: "Programmeerimine on ainult üks osa!"
- **Analoogia**: "Nagu maja ehitamine - see ei ole ainult telliste laduminem"


---


### 🎯 1.2 Probleemi defineerimine (20 min) - SLIDES 10-14

Mis on hea probleemi definitsioon?
Mis on halb probleemi definitsioonis 'Mul on igav'?

#### Õpetaja kõne (10 min):
**SLIDE 11 - Hea probleem:**
**"Kõik head tarkvaraprojektid algavad hästi defineeritud probleemiga. Vaadame, mis teeb probleemi 'heaks'."**

- **Selgelt defineeritud**: Küsi tudengitelt: "Mis on halb probleemi definitsioonis 'Mul on igav'?"
- **Mõõdetav**: "Kuidas me teame, et lahendus toimib?"
- **Lahendatav**: "Kas meil on ressursse ja oskusi?"
- **Oluline**: "Kas keegi tõesti vajab seda?"

**SLIDE 12 - Raamistik:**
**"Siin on süstemaatiline viis probleemi analüüsimiseks."**

**Näide tahvlil: "Tudengite kodutööde meeldetuletused"**

**Töötage läbi 5 punkti koos tudengitega:**

**1. PROBLEEM: Mis täpselt toimub valesti?**
- **Küsi tudengitelt**: "Mis on teie kogemus kodutöödega?"
- **Oodatavad vastused**: "Unustavad tähtajad", "Ei tea, mis on kodutöö", "Leiavad infot hilja"
- **Täpsusta**: "Tudengid ei saa õigeaegselt infot kodutööde kohta"

**2. MÕJU: Kellele ja kuidas see mõjub?**
- **Küsi**: "Kes sellest kannatab ja kuidas?"
- **Oodatavad vastused**: 
  - Tudengid: stress, kehvad hinded, ajaplaneerimise raskused
  - Õpetajad: palju küsimusi, hilinenud tööd
  - Ülikool: õppekvaliteedi langus

**3. PÕHJUSED: Miks see probleem tekib?**
- **Küsi**: "Miks see juhtub?"
- **Oodatavad vastused**:
  - Info on hajutatud (e-mail, Moodle, WhatsApp)
  - Tudengid ei kontrolli regulaarselt kõiki kanaleid
  - Õpetajad lisavad infot viimasel hetkel

**4. KONTEKST: Millistes olukordades esineb?**
- **Küsi**: "Millal ja kus see probleem tekib?"
- **Oodatavad vastused**:
  - Semestri alguses (palju uut infot)
  - Enne tähtaegu (stress suureneb)
  - Erinevate ainete puhul (igal õpetajal oma süsteem)

**5. PIIRANGUD: Millised on tehnilised/ressursi/aja piirangud?**
- **Küsi**: "Millised on piirangud lahenduse leidmisel?"
- **Oodatavad vastused**:
  - Eelarve: tudengitel pole raha maksma
  - Tehnoloogia: peab töötama kõigil seadmetel
  - Aeg: lahendus peab olema kiiresti kasutatav
  - Õpetajad: ei taha rohkem tööd

**Õpetaja märkus**: Kirjuta kõik vastused tahvlile raamistiku järgi, et tudengid näeksid struktuuri!

**SLIDE 13 - Näited:**
**"Vaatame, mis vahe on heal ja halval probleemi kirjeldusel."**

#### Praktiline harjutus (10 min):
**Ülesanne**: Tudengid paarides (2 min mõtlemist):
1. **Halb näide**: "Kool on igav" → Kuidas seda paremini defineerida?
2. **Hea näide**: Las tudengid analüüsivad meie head näidet raamistiku järgi

**Arutelu**: Iga paar jagab oma tulemust (1 min paar)

---

### 🎯 1.3 Kasutajate uurimise meetodid (25 min) - SLIDES 14-16

#### Õpetaja kõne (15 min):
**"Probleem on defineeritud, aga kuidas me teame, mida kasutajad tegelikult vajavad?"**

**SLIDE 14 - Kvalitatiivsed meetodid:**
- **Intervjuud**: "Küsi 'Miks?' vähemalt 5 korda"
- **Näide**: Demos intervjuu tehnika - võta üks tudeng vabatahtlikuks
- **Vaatlused**: "Inimesed räägivad ühte, aga teevad teist"

**SLIDE 15 - Kvantitatiivsed meetodid:**
- **Küsitlused**: "Suured numbrid, aga miks-küsimustele ei vasta"
- **Analüütika**: "Google Analytics näitab, mida inimesed teevad"
- **Persoonade loomine**: "Kasutajate vajaduste hindamine" [persona workshop](https://miro.com/persona/how-to-run-a-persona-workshop/)  
- **Card sorting**: "Informatsiooni arhitektuuri testimine" [card sorting](https://youtu.be/6RhFN6cul3w)  
[card sorting by NN](https://www.nngroup.com/articles/card-sorting-definition/)
- **Journey mapping**: "Kasutajakogemuse kaardistamine" – see on meetod, mille abil kaardistatakse kasutaja teekond läbi süsteemi või teenuse. Eesmärk on mõista, milliseid samme kasutaja läbib, millised on tema kogemused, emotsioonid ja võimalikud takistused igas etapis. Journey mapping aitab tuvastada kitsaskohti ja võimalusi kasutajakogemuse parandamiseks.
[Journey mapping](https://youtu.be/A2LFJF1SUBg)

- **Rõhuta**: "Parim tulemus tuleb kombinatsioonist"

#### Praktiline näide (10 min):

1. **Halvad küsimused**: "Kas teile meeldiksid kodutööde meeldetuletused?"
2. **Head küsimused**: "Kuidas te praegu kodutöid meeles peate?"

**Demo**: Õpetaja intervjueerib ühte tudengit "kodutööde haldamise" kohta

- Demonstreeri halbu ja häid küsimusi
- Tudengid märgivad erinevust

**Halvad küsimused** (miks need on halvad):
- "Kas teile meeldiks, kui oleks olemas äpp, mis saadab kodutööde meeldetuletusi?"  
  *Põhjus: suunav küsimus, eeldab juba lahendust, ei anna infot tegeliku vajaduse kohta.*
- "Kas te kasutaksite sellist lahendust?"  
  *Põhjus: hüpoteetiline, inimesed kipuvad viisakusest nõustuma, ei näita tegelikku käitumist.*
- "Kas teil on tihti kodutöödega probleeme?"  
  *Põhjus: üldine, ei aita mõista konkreetset olukorda ega tausta.*

**Head küsimused** (miks need on head):
- "Kuidas te praegu kodutööde tähtaegu meeles peate?"  
  *Põhjus: uurib olemasolevat käitumist, annab infot tegeliku olukorra kohta.*
- "Räägi viimasest korrast, kui unustasid kodutöö tähtaja – mis juhtus?"  
  *Põhjus: konkreetne kogemus, aitab mõista probleemi tausta ja emotsioone.*
- "Milliseid tööriistu või süsteeme sa praegu kasutad kodutööde jälgimiseks?"  
  *Põhjus: selgitab, millised lahendused on juba kasutusel ja mis nende juures töötab/ei tööta.*

**Arutelu**: Palu tudengitel märkida, miks üks küsimus on halb ja teine hea – rõhuta, et head küsimused keskenduvad kasutaja kogemusele ja olemasolevale käitumisele, mitte lahenduse pakkumisele.

---

### 🎯 1.4 Nõuete tüübid (20 min) - SLIDES 16-18

#### Õpetaja kõne (10 min):
**"Kasutajate uurimine on tehtud. Nüüd peame selle tõlkima konkreetseteks nõueteks."**

**SLIDE 16-18 - Funktsionaalsed vs mitte-funktsionaalsed:**
- **Analoogia**: "Auto võimekused (kiirus, kütusekulu) vs Auto funktsionaalsused (käigukast, rool)"
- **Näited WhatsApp-ist**:
  - Funktsionaalne: "Kasutaja saab saata sõnumeid"
  - Mitte-funktsionaalne: "Sõnum peab jõudma alla 2 sekundi"

#### Interaktiivne harjutus (10 min):
**Grupiharjutus** (4 inimesed grupis):
1. **5 minutit**: Instagram näitel - kirjutage 3 funktsionaalset ja 3 mitte-funktsionaalset nõuet
2. **5 minutit**: Grupid esitavad tulemusi

**Õpetaja feedback**: Paranda ja täienda tudengite vastuseid

[Nõuete näide](https://wiki.twn.ee/spaces/REFERENTS/pages/83919369/3.+N%C3%B5uete+kaardistamine)  

KAsutatakse ka tähistusi, nt:  
- FN or FR - functional need või functional requirement
- UC - use case
jms.
nt FN-UC01.1-4  



---



### 🎯 1.5 Konkurentsianalüüs (15 min) - SLIDES 18-22
#### Õpetaja kõne (10 min):
Küsimus:  
**"Miks peaksime vaatama, mida teised juba teevad?"**

**SLIDE 19 - Miks oluline:**
- **Näide**: "Tesla ei leiutanud elektriautot, aga tegi seda paremini"
- **Rõhuta**: Innovatsioon ≠ täiesti uus asi

**SLIDE 20 - Raamistik:**
- **Praktiline näide**: Vaatame koos Spotify vs Apple Music
  - Läbida kõik 6 punkti

#### Lühike arutelu (5 min):
**Küsimus klassile**: "Milliseid rakendusi te kasutate järgmisteks tegevusteks?"
- Transpordi tellimiseks
- Toidu tellimiseks  
- Raha ülekandmiseks

**Analüüsi**: Miks valite just neid?

**SLIDE 21 - Dokumentatsioon** 

---

## Vaheaeg ☕

---

## OSA 2: PRAKTILINE TÖÖTUBA (90 MINUTIT)

Eesmärk teha kodutöö jaoks vajalikud "soojendused", et oskaks kodutöö lõpuni teha.

### 🛠️ 2.1 Probleemi valimine ja defineerimine (20 min) - SLIDES 25-26

#### Ülesande seadistamine (5 min):
**"Nüüd teeme päris tööd! Valime probleemi, millega töötame järgmiste seminariteni."**

**Gruppide moodustamine**:
- 3-4 tudengit grupis
- töövahendite seadistamine – tunni repo/kaust, md file

#### Brainstorm (10 min):
**SLIDE 25 - Valdkonnad:**
**Juhendid gruppidele**:
1. **5 min**: Brainstorming - iga valdkonna kohta vähemalt 2 probleemi
2. **Kasuta seminar-01 kausta**: 
- `problem-definition.md` - valitud probleem
- `user-research.md` - intervjuu tulemused
- `requirements.md` - funktsionaalsed ja mitte-funktsionaalsed nõuded
- `competitive-analysis.md` - konkurentide analüüs
- `README.md` - projekti ülevaade


Korralik vormistus, grupiliikmete nimed. 
Kirjutage kõik ideed üles
3. **Ära kritiseeri**: Kõik ideed on lubatud!

**Õpetaja ülesanne**: Käi gruppide vahel ringi, küsi täpsustavaid küsimusi

#### Evalueerimine ja valik (5 min):
**SLIDE 26 - Evalueerimine:**
1. **Vali 3 parimat**: Kasutades kriteeriumeid slide-lt 10
2. **Vali üks**: Millega jätkate

**Tulemuste dokumenteerimine**:
- Iga grupp räägib 1 minut oma valitud probleemist
- Märgi tahvlile kõik grupid ja nende probleemid

---

### 🛠️ 2.2 Kasutajate uurimise harjutus (30 min) - SLIDES 27

#### Intervjuu küsimuste koostamine (10 min):
**SLIDE 27:**
**"Nüüd valmistame ette intervjuu oma probleemi kohta."**

**Juhendid**:
- **Struktuuri järgimine**: 2-3 tausta + 4-5 probleemi + 2-3 lahenduse küsimust
- **Näited head küsimused**:
  - "Kuidas te praegu [probleem] lahendateb?"
  - "Millal viimati see probleem esines?"
  - "Mis tunne teil sellest tekib?"

**Õpetaja ülesanne**: Kontrolli iga grupi küsimusi, anna tagasisidet

#### Rollimäng: intervjuud (20 min):
**SLIDE 27:**
**"Nüüd testite oma küsimusi!"**

**Juhendid**:
1. **Gruppide paaristamine**: Grupp A intervjueerib gruppi B
2. **10 min esimene voor**: A küsib, B vastab (nende probleemi kontekstis)
3. **10 min teine voor**: Rollide vahetus

**Õpetaja ülesanne**:
- Jälgi intervjuude kvaliteeti
- Anna näpunäiteid ("Küsi 'miks?'")
- Märgi üles häid küsimusi/vastuseid

---

### 🛠️ 2.3 Nõuete kogumine ja dokumenteerimine (25 min) - SLIDES 28-29

#### Funktsionaalsed nõuded (15 min):
**SLIDE 28:**
**"Nüüd tõlgime intervjuu tulemused konkreetseteks nõueteks."**

**Juhendid gruppidele**:
1. **Analüüsige vastuseid**: Mida kasutajad ütlesid?
2. **5-7 funktsionaalset nõuet**: "Süsteem peab võimaldama..."
3. **Prioritiseerimine**: Must-have vs Nice-to-have

**Näited tahvlil**:
- "Kasutaja peab saama lisada kodutöö"
- "Süsteem peab saatma meeldetuletusi"

#### Mitte-funktsionaalsed nõuded (10 min):
**SLIDE 29:**
**"Ära unusta kvaliteedi nõudeid!"**

**Juhendid**:
1. **Kiirus**: Kui kiire peab olema?
2. **Kasutajad**: Kui palju kasutajaid?
3. **Seadmed**: Millised seadmed toetatud?

**Õpetaja ülesanne**: Aita gruppidel konkretiseerida ("3 sekundit" vs "kiire")

---

### 🛠️ 2.4 Konkurentsianalüüs (15 min) - SLIDE 30

#### Praktilne uurimistöö (15 min):
**"Leidke 2-3 olemasolevat lahendust oma probleemile."**

**Juhendid**:
1. **Google otsing**: "problem name" + "app" / "solution"
2. **App Store otsing**: Otsige märksõnadega
3. **Lühike analüüs**: Tugevused ja nõrkused

**Tööriist**: Telefon, arvuti
**Tulemus**: Iga konkurent 2-3 lausega

**Õpetaja ülesanne**: Aita gruppidel otsingumärksõnu leida

---

### 🛠️ 2.5 Dokumentatsiooni vormistamine (10 min) - SLIDE 31

#### GitHub seadistamine:
**"Nüüd paneme kõik GitHub-i!"**

**Samm-sammult**:
1. **Grupi liider loob repo**: [organisatsioon]/[grupi-nimi]-project
2. **Lisab tiimiliikmed**: Collaborators
3. **Loob failid**:
   - `problem-definition.md`
   - `user-research.md` 
   - `requirements.md`
   - `competitive-analysis.md`
   - `README.md` (projekti kirjeldus)

**Template failid**: Anna linkid template-idele

---

## KOKKUVÕTE JA KODUTÖÖ (10 min) - SLIDES 32-35

### Seminari kokkuvõte (5 min):
**"Mis me täna õppisime?"**
- Tarkvaraarendus vs programmeerimine
- Probleemi defineerimine
- Kasutajate uurimise meetodid
- Nõuete tüübid
- Konkurentsianalüüs

### Kodutöö selgitamine (5 min):
**SLIDE 33-34 - Kodutöö:**

**Grupi osa**:
- **Süvaanalüüs**: Täiendavad allikad, statistika
- **3 päris intervjuud**: Päris inimestega!
- **5+ konkurenti**: Põhjalik analüüs
- **Stakeholder analüüs**: Kes on kõik huvitatud osapooled?

**Individuaalne osa** - iga tudeng valib rolli:
- **Kasutajate uurija**: Intervjuud ja andmeanalüüs
- **Turu-analüütik**: Konkurendid ja ärimudel  
- **Tehnoloogia uurija**: Tehnilised lahendused
- **Nõuete analüütik**: Detailsed nõuded

**Tähtaeg**: 1 nädal
**Esitamine**: GitHub PR workflow

---

## ÕPETAJA MÄRKMED

### Kriitilised hetked:
1. **"Mis on tarkvaraarendus"** - See on uus mõiste paljudele
2. **Probleemi defineerimine** - Tudengid kipuvad olema liiga üldised
3. **Intervjuu harjutus** - Vajab aktiivset juhendamist
4. **GitHub seadistamine** - Tehniline osa, kus on abi vaja

### Tavalised küsimused:
- **"Kas me peame kodeerima?"** → EI! Ainult Markdown
- **"Kui palju inimesi intervjueerida?"** → Vähemalt 3 päris isikut
- **"Mis siis, kui keegi ei vasta intervjuule?"** → Kasutage tuttavaid, pereliikmeid

### Ajahaldus:
- **Kui mahe hilineb**: Lühenda teoreetilisi osi
- **Kui praktiline osa võtab kauem**: Jäta dokumenteerimine kodutööks
- **Alati hoia kinni pausist**: Tudengid on väsinud 90 min järel

### Järgmiseks korraks:
- **Kontrolli kodutöid**: GitHub-is peer review
- **Valmista ette Seminar 3**: Projektijuhtimine
- **Gruppide edukus**: Millised grupid vajavad täiendavat abi?

---

## LISARESSURSID

### Lugemist:
- [The Mom Test](http://momtestbook.com/) - intervjuu tehnikad
- [Jobs to be Done](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) - kasutajate motivatsioon

### Tööriistad:
- **Miro** - kollaboratiivne whiteboard
- **Google Forms** - küsitluste tegemine
- **Notion** - märkmete hoidmine

### Template failid:
- [problem-definition-template.md](link)
- [user-research-template.md](link)
- [requirements-template.md](link)
- [competitive-analysis-template.md](link)

---

## TAGASISIDE VORM TUDENGITELE

Seminari lõpus (vabatahtlik 2 min):
1. **Mis oli selge?** 😊
2. **Mis jäi ebaselgeks?** 🤔
3. **Mis oli kasulik?** ⭐
4. **Mida muudaksid?** 💡

**Digital form**: [Google Forms link]
