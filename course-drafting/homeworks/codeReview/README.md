# *Code Review*
Code review on protsess, mille käigus vaatab koodi üle keegi, kes ei ole antud koodi autor. Väga oluline on, et tellija saaks kätte võimalikult kvaliteetse koodi – *code review*’d aitavad seda eesmärki täita, jälgides koodi kvaliteeti kogu arendamise elutsükli vältel. Jälgimise all on koodi kujundus, funktsionaalsus, keerukus, automaattestide korrektsus, kommentaarid, stiil ja dokumentatsioon.  
Kuigi parimaks koodi ülevaatajaks oleks oma ala tippspetsialist, siis ei ole ainult oma meeskonna kõige osavama arendaja rakendamine *code review*’de tegemisse mõistlik. Pikas perspektiivis on hea, kui käe saavad valgeks kõikidel tasemetel olevad arendajad.
 
## *Code review* plussid
Koodi kellegi teise poolt ülevaatamisel on palju positiivseid tulemeid: 

- **Teadmiste jagamine**: kasu ei saa mitte ainult koodi kirjutaja, vaid ka ülevaataja. Nooremarendajatele annab see võimaluse näha kuidas kirjutavad koodi vanemad arendajad. Kui koodi ülevaatamine on pidev, siis tekib tiimis kõigil ka ülevaade käimasolevatest arendustöödest ja vajadusel on lihtsam kellegi teise arendatud kood üle võtta ja edasi arendada.  
- **Bug-ide/vigade kiirem avastamine**: kaks pead on ikka kaks pead. Kui kood vaadatakse kriitilise pilguga põhjalikult üle alles peale kogu koodi valmis kirjutamist, siis võib olla raske leida vigu, mis tehti kuskil koodi kirjutamise protsessi alguses. Koodi kirjutaja ei pruugi enam ise mäletada, miks ta mingi koodijupi kirjutas. Pidevad *code review*-d aitavad *bug*’e avastada juba varakult. Nii saavad vead lahenduse juba koodi kirjutamise käigus. Pidevad koodi ülevaatused aitavad lühendada ka projekti lõpus testimisele ja parandamisele kuluvat aega.  
- **Standardite jälgimine**: kui arendajad ei suhtle üksteisega igapäevaselt või elavad lausa erinevates riikides, siis saab *code review*’ga silma peal hoida ka ühtse programmeerimisstiili rakendamisel. Kui kõik kasutavad sama koodikirjutamise standardit, siis on hiljem kergem kellegi teise kirjutatud koodi edasi arendada.  
- **Turvalisus**: sarnane *bug*’ide otsimisele, aga *bug*’ide asemel otsitakse turvanõrkuseid. Varane turvavigade leidmine ja parandamine on lihtsam, kui hilisem suure osa koodist ümber kirjutamine, et koodi algfaasis tehtud viga parandada.  
- **Koostöö-tunne**: koodi ülevaatamine sunnib arendajaid teiste arendajatega koostööd tegema. Koostöö suurendab liikmete ühtekuuluvustunnet ja lubab arendajatel tunda, et nad on millegi suure tähtis osa.  
- **Koodi kvaliteedi parandamine**: koostööd teinud meeskond oskab leida oma liikmete koodis vigu, mida automaattestid ei pruugi märgata.  

## *Code review* miinused  
Code Review’ga kaasneda võivad negatiivsed mõjud:  

- **Pikem projektile kuluv aeg**: pidev koodi analüüs arendaja ja ülevaataja vahel kulutab mõlema väärtuslikku aega. Lahenduseks oleks siin automaattestimise tööriistad, mis saavad ise hakkama väiksemate koodi ebakõlade leidmise ja isegi parandamisega.  
- **Teiste tööde pealt tähelepanu ära võtmine**: arendajatel on tihti suur töökoormus, *code review* sunnib neid oma töö pooleli jätma ja keskenduma täiesti uuele teemale. Nii võivad projektid venima hakata, sest arendaja ei saa keskenduda enda arendustööle.  
- **Pikad ülevaatuse ajad**: suuremate koodimuutuste puhul kulub ka *code review* peale rohkem aega. Pikad ülevaatuse ajad suurendavad riski, et ülevaataja muutub hooletuks ja ei pane kõiki vigu tähele.
 
## Code Review kasutamise näiteid:
### Paaris programmeerimine:
Kaks koos töötavat inimest – üks kirjutab koodi ja teine tegeleb koodi reaalajas ülevaatamisega.  

Plussid:
- Teadmiste jagamine
- Üks inimene ei oma kogu informatsiooni
- Aitab keerulisi probleeme kiiremini lahendada
- Tõstab moraali
- Vead leitakse kiiremini üles
- Arendaja ja ülevaataja ei pea tingimata samas asukohas viibima (*remote review*)  

Miinused:  
- Ajamahukas  
- Palju tühja tööd  
- Keeruline efektiivsust mõõta  

### Üle-õla ülevaatamine (*Over-the-shoulder review*):  
Osalejateks arendaja ja ülevaataja. Arendaja ülesanne on selgitada oma järgmist suuremat uuenduste ettepanekut ja ülevaataja ülesandeks on täpsustavate ja selgitavate küsimuste küsimine. Ülevaataja annab soovitusi, kuidas edasi toimida; arendaja võib väiksemad muudatused kohe sisse viia, suuremad muudatused paneb arendaja kirja ja viib need sisse peale *Over-the-shoulder* *code review* lõppu.  

Plussid:
- Kerge kasutada
- Arendaja ja ülevaataja ei pea ühes asukohapunktis viibima
- Kiirem kui paaris programmeerimise meetod  

Miinused:
- Ülevaataja ei oma head ülevaadet koodist
- Ülevaatus sõltub arendaja tempost
- Ei ole kinnitust, et muudatused ka sisse viiakse
- Keeruline tulemuslikkust mõõta
 
### Tööriistadega ülevaatus:
Tööriistad võimaldavad automaatset koodi ülevaatust ja ka lihtsamate vigade automaatset parandamist. Erinevad keskkonnad toovad välja koodi vajakajäämised. Arendusmeeskonnal on võimalik veaga koheselt tegeleda või pakkuda välja erinevaid võimalikke lahendusi, jättes selleks veateate juurde omapoolsed kommentaarid. Kasutada on võimalik ka automaatseid turvalisuse testimise tööriistu. Tööriistade kasutamisele ei tohiks sajaprotsendiliselt lootma jääda – nendest tuleks mõelda, kui abilistest teiste arendajate kõrval.  

Plussid:
- Lihtne infot koguda
- Arendaja saab keskenduda arendamisele  

Miinused:
- Arendaja peab oskama vajalikke tööriistu kasutada
- Maksab palju
- Vaja on siiski ka päris inimese ülevaatust
 
### E-maili teel edastamine (_E-mail pass-around_): 
Kasutatakse väiksemate ja lihtsamate muudatuste ülevaatamiseks. Ülevaatust vajav kood saadetakse e-maili või mõne lähtekoodi haldussüsteemi kaudu ülevaatajatele. Koodimuudatused on tavaliselt väikesed ja ei võta palju aega, ega vaja väga spetsiifilisi oskuseid.  

Plussid:
- Kerge rakendada
- Arendaja ja ülevaataja ei pea olema ühes asukohas
- Lähtekoodi haldussüsteemid genereerivad automaatseid ülevaateid  

Miinused:
- E-mailide saatmiseks andmete kogumine ja nende edastamine on ajamahukas
- Ülevaadete jälgimine on keeruline
- Puudub kindel ülevaatamise tähtaeg
- Pole kinnitust, et muudatused sisse viiakse
- Keeruline efektiivsust kontrollida
 
## Konfliktide lahendamine:  
Parim viis on muidugi jõuda ühisele arusaamale. Kui tekivad eriarvamused ja tööd tehakse kaugtööna, siis tasub korraldada näost-näkku kohtumine. See kiirendab aruteluprotsessi ja aitab kiiremini lahenduseni jõuda.  
Kui arendaja ja ülevaataja ei suuda jõuda konsensuseni, siis tuleb kaasata arutellu keegi kolmas. Selleks võiks olla kas meeskonna juht või vaidlusaluse koodi haldaja.
 
## Ettepanekud *code review*’de paremaks läbiviimiseks:
- Koodi ülevaatamiseks kuluva aja piiramine aitab hoida ülevaatused produktiivsemad. Määrata kindlale koodi ridade arvule mingi kindel hulk aega mille jooksul ülevaatust tehtud peaks saama.
- Loo *code review* jaoks täpsed juhised koos konkreetsete sammudega.
- Määra täpsed kriteeriumid, millele kood vastama peab, et *code review*’d läbida.
- Kaasa *code review*’del osalema nii uued kui ka kogenud arendajad: nii saavad noored õppida ja kogenud arendajad ei muutu asendamatuteks info ainuvaldajateks.
- Hajuta koodi ülevaatamise kohustus ühtlaselt terve meeskonna vahel. Kui mõnele arendajale hakkab ette sattuma rohkem koodi ülevaatamise kohustusi, siis võivad venima hakata tema enda arendusprojektid.
- Küsi ja kommenteeri. Küsimused aitavad aru saada põhjustest miks on arendaja kirjutanud koodi just selliselt. Võibolla näeb ta midagi mida sina ülevaatajana ei näe?
- Ülevaatajana muudatusi pakkudes püüa ka põhjendada, miks mingit muudatust vaja on. Nii küsimused kui ka põhjendused aitavad vältida segaseid olukordi ja säästavad aega.
 
 
##### Kasutatud materjal:
https://about.gitlab.com/topics/version-control/what-is-code-review/  
https://google.github.io/eng-practices/review/  
https://google.github.io/eng-practices/review/reviewer/standard.html  
https://nl.mathworks.com/discovery/code-review.html