# Näiteid hea ja halva Javascripti koodi kohta koos põhjendustega
## Javascript tee ja ära tee

JavaScript on populaarne ja võimas programmeerimiskeel, mis võimaldab arendajatel luua dünaamilisi ja interaktiivseid veebilehti. Siiski on nagu igasugusel muul programmeerimiskeelel, on olemas teatud parimad praktikad ja tüüpilised vead, mida tuleks vältida. Siin on mõned JavaScripti "tee seda" ja "ära tee" soovitused:

### Tee seda:

1. Kasuta tähenduslikke ja kirjeldavaid muutujanimesi. See muudab sinu koodi lugemise ja mõistmise lihtsamaks.
2. Kasuta kommentaare oma koodi selgitamiseks. See aitab teistel arendajatel, kes tulevikus võivad sinu koodiga töötada.
3. Kasuta semikooloneid oma lausete lõpetamiseks. Kuigi JavaScript võimaldab semikoolonite vahelejätmist, on hea tava need lisada, et vältida ootamatut käitumist.
4. Deklareeri muutujad alati enne nende kasutamist. See takistab vigu ja tagab, et sinu kood töötab ootuspäraselt.
5. Kasuta funktsioone, et kapseldada korduvkasutatavat koodi. See muudab sinu koodi modulaarsemaks ja kergemini hooldatavaks.
6. Kasuta JavaScripti viimast versiooni. See tagab, et sul on juurdepääs uusimatele funktsioonidele ja täiustustele.

### Ära tee:

1. Ära kasuta globaalseid muutujaid, välja arvatud juhul, kui see on hädavajalik. Globaalsed muutujad võivad põhjustada konflikte ja muuta sinu koodi raskemini hooldatavaks.
2. Ära kasuta eval() funktsiooni. See funktsioon võib täita suvalist koodi ja esitada turvariski.
3. Ära ignoreeri vigu. Käitle vigu alati sobivalt, et vältida ootamatut käitumist.
4. Ära kasuta alert() funktsiooni silumisel. Kasuta selle asemel console.log() funktsiooni, mis annab rohkem teavet ega häiri kasutajakogemust.
5. Ära kasuta "with" avaldust. See avaldus võib põhjustada ootamatut käitumist ja tuleks vältida.
6. Ära kasuta document.write() funktsiooni. See funktsioon võib kirjutada üle kogu sinu HTML-dokumendi.
7. Ära looda brauseripõhiste funktsioonide peale. Testi alati oma koodi mitmes brauseris, et tagada ühilduvus.

## Näited heast ja halvast koodi kasutamisest
### Funktsioonide nimetamine

HALB: 
// funktsiooni nimetamisel ei kirjeldata funktsiooni sisuliselt, vaid lihtsalt seda, mida see teeb


function nullistSuurem(temperature) {
  return temperature >= 0;
}

HEA:
// funktsiooni nimetamisel kirjeldatakse funktsiooni sisuliselt, st et mida see funktsioon teeb


function soojakraadid(temperature) {
  return temperature >= 0;
}


### “Else” kasutamine

HALB: 
// Kasutad “else”-i 

if( lumisulab === true ){
  return temperature >= 0;
} else {
  return temperature <= 0;
}

HEA:
// Ei kasuta else’i, vaid kahte if-i 

if( lumisulab === true ){
  return temperature >= 0;
} 

if( lumisulab === true ){
  return temperature <= 0;
}

### Massiivide kirjeldamine
HEA: 
var loomad = [‘elevant', 'karu', 'kaelkirjak'];

EBASOOVITATAV: 
var loomad = new Array();
loomaaed[0]='elevant';
loomaaed[1]=’karu';
loomaaed[2]='kaelkirjak';

### Muutujate nimetused

HALB: 
// liiga lühikesed, ei anna sisulist infot muutuja kohta
var x56;
var yolo1;

// liiga pikad, tüütu koodi kirjutada ja lugeda 
var kuuliLennuTeeTunneliLuuk;

HEA: 
//nimi kirjeldab muutuja sisulist tähendust/funktsiooni programmis 

var soojakraadid //(mitte var ylenulli)
var miinuskraadid //(mitte var allanulli)
var t2isealine //(mitte var yle18) 



Dave Talimaa, Jarita Maaria Rintamäki	