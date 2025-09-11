# Kommentaarid vs mittekommentaarid koodis - jah või ei?

Loodud koodi kasutatakse ainult siis kui sihtrühm seda mõistab – seetõttu mängib stiil olulist rolli koodi kvaliteedis, sh kommentaarid. Kood ise on kõige tähtsam kommenteerimise ja dokumenteerimise vahend. Täiendavate kirjelduste lisamine segase koodi selgitamiseks muudab sellega töötamise veel keerulisemaks, mistõttu on oluline, et jälgitakse enne kommenteerimist ka koodi stiili. (Broad Institute)

Kommentaare tuleb kasutada ainult konteksti lisamiseks ja valikute selgitamiseks, kui seda pole võimalik selgitada läbi selge nimetamise, struktuuri või toimingute konteksti. Tuleb meeles pidada, et kommentaare kasutavad teised arendajad, kasutajad või teie ise.(Broad Institute)

Javascriptis on kaks süntaksi mida on võimalik kommentaaride kirjutamiseks kasutada (MDN Web Docs):
1.	Üherealine kommentaar kirjutatud topelt kaldjoonega //
```sh
// See on kommentaar
```

2.	Mitmerealine kommentaar kirjutatud kaldjoonte ja tärnide vahele /* ja */'
```sh
/*
See on ka
kommentaar
*/
```
 ## Kommentaarid: JAH!
 
Vajalik kommentaar, mis on täpne, informatiivne, heade kavatsustega ning õiges kohas võib mõjuda koodi lugemise ja ülesehitusele nagu täpp i peal, kuid kindlasti ei tasu sellega üle pingutada. Nagu on ka öelnud Nam Nguyen - kommentaaridega ei tuleks suhelda, vaid suhelda pigem läbi koodi. Läbi koodi suhtlemisel on kaks eesmärki: et seda mõistaksid inimesed kui ka masinad. 

Head kommentaarid selgitavad miks midagi tehakse ja kood ütleb kuidas. Kommentaaride kirjutamisel tuleks kasutada ainult vajalikul määral üksikasju samas vältides lühendeid - iga lugeja ei pruugi neist aru saada. Jälgida tuleb põhimõtet, et kood oleks arusaadav. Samuti tuleks kasutada kommentaare enne koodi - selgitus enne tegevusi. (Arunodi 2021)

Näiteid headest kommentaaridest (Ding 2022)

- Informatiivne kommentaar - See päises asuv kommentaar selgitab 14 rea sisu- see aitab lugejal mõista skripti töövoogu ja leida vajalikud skripti sammud
[![Informatiivne](https://app.works/wp-content/uploads/2022/04/image-5-1024x296.png)]()
- Kavatsust selgitav kommentaar
[![Kavatsus](https://app.works/wp-content/uploads/2022/04/Screen-Shot-2022-04-21-at-2.50.41-PM-768x90.png)]()
- Hoiatus tagajärgede eest
[![Tagajärg](https://app.works/wp-content/uploads/2022/04/Screen-Shot-2022-04-21-at-2.51.37-PM-768x56.png)]()
- (Muutuste) register
[![Register](https://app.works/wp-content/uploads/2022/04/Screen-Shot-2022-04-21-at-2.48.36-PM.png)]()


## Kommentaarid: EI!

Heade kommentaaridega ei tasu ka üle pingutada. Esimene mõte mis pähe tuleb seda lugedes on ilmselt see, et aga miks või kuidas võib kommenteerimine negatiivselt mõjuda ? See ju ainult lihtsustab sisu? Reaalsuses võib see aga oluliselt raskendada koodi lugemist ning tekitada palju mittevajaliku taustmüra. Näiteks olukorras, kus koodi muudetakse ja täiendatakse, kuid kommentaarid jäetakse alles ja vanad, siis see ei ole enam täpne antud sisu jaoks ning võib mõjuda eksitavalt. 

Näited mitte just kõige paremast kommenteerimisest, mis kõnelevad enda eest:

- Liigne kommenteerimine (Sourour 2017)
```sh
/*set the value of the age integer to 32*/
int age = 32; 
```

[![Liiga palju](https://app.works/wp-content/uploads/2022/04/Screen-Shot-2022-04-21-at-2.47.21-PM-768x57.png)]()

- Räpased kommetaarid (Sourour 2017)
```sh
/*This code sucks, you know it and I know it.  Move on and call me an idiot later.*/ 
```
Üheks huvitavaks näiteks on ka 80-datel kirjutatud Microsofti tarkvara koodi peidetud roppused (Eadicicco 2014).

- Huumor (Sourour 2017)

```sh
/*
 * Dear Maintainer
 *
 * Once you are done trying to ‘optimize’ this routine,
 * and you have realized what a terrible mistake that was,
 * please increment the following counter as a warning
 * to the next guy.
 *
 * total_hours_wasted_here = 73
 *
 * undeclared variable, error on line 0
 *
 */
```

```sh
// I dedicate all this code, all my work, to my wife, Darlene, who will 
// have to support me and our three children and the dog once it gets 
// released into the public.
```

```sh
// drunk, fix later
```

## Kokkuvõtte

Nii nagu ühte head asja liiga palju, kehtib ka siin, liiga palju kommenteerimist ning eriti inetut kommenteerimist, mis jätab koodi autorist ebaprofessionaalse mulje, tuleks kindlasti vältida. Kui kommenteerida, siis ainult tabavalt ning panna kirja hädavajalik, mida autor tunneb, et on vaja ilmtingimata edasi anda sisu mõistmiseks.Tasakaalu leidmine kommentaaride hulga ja kasutatava stiili osas võib vahel olla keeruline. Mis iganes on programmeerija eelistus - tuleb olla järjepidev.


## Viidatud allikad

Arunodi, N. (2021). Best Practices For Using Comments In JavaScript. [23.03.2023]. https://blog.bitsrc.io/best-practices-for-using-comments-in-javascript-4c4cd8619c18

Broad Institute. Coding and Comment Style. [24.03.2023]. https://mitcommlab.mit.edu/broad/commkit/coding-and-comment-style/

Ding, W. (2022). Code Readability: Good Comments vs. Bad Comments. [17.03.2023]. https://app.works/good-comments-vs-bad-comments/

Eadicicco, L. (2014). Microsoft Programmers Hid A Bunch Of Profanity In Early Software Code. [17.03.2023]. https://www.businessinsider.com/microsoft-hidden-messages-in-word-and-ms-dos-2014-3

MDN Web Docs. What is JavaScript? [22.03.2023]. https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript 

Nguyen, N. (2020). Why Good Codes Don’t Need Comments.[20.03.2023]. https://towardsdatascience.com/why-good-codes-dont-need-comments-92f58de19ad2

Sourour, B. (2017). Putting comments in code: the good, the bad, and the ugly. [23.03.2023]. https://www.freecodecamp.org/news/code-comments-the-good-the-bad-and-the-ugly-be9cc65fbf83/
