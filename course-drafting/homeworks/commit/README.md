# Commit

Git on versioonihaldustarkvara, mis võimaldab arendajatel tõhusalt jälgida ja hallata oma projekti muudatusi, sealhulgas koodi, dokumentatsiooni ja muid ressursse. Üks Git'i põhikomponente on "*commit*". 

Commit on sisuliselt unikaalse koodiga varustatud andmete või muudatuste kogum, millest tuleneb projekti seisund mingil konkreetsel ajahetkel. 

Commiti tegemine versioonihaldustarkvarasse on analoogne arvutimängu seisundi salvestamisele – mänguseisundit on ebapraktiline järjepidevalt salvestada ja seetõttu tasub seda teha mingi etapi läbimise järel. 

Nii keerulisema mängu, kui ka keerulisema projekti puhul on mõnikord kasulik minna tagasi mõne varasema salvestatud hetke juurde ja sealt oma tegevust uuesti alustada.

Commitimise protsess koosneb üldjoontes muudatuste tegemisest, salvestamisest (enda arvutis), ette valmistamisest (*git add*) ja üles laadimisest (*git commit*). Vajaminevad liigutused sõltuvad sellest, mis viisil on kasutaja enda arenduskeskkonna üles seadnud.

## Commit'i eesmärk

Commit'id võimaldavad arendajatel:

1.	Jälgida muudatusi: Commit'id aitavad mõista, mis on tehtud muudatuste sisu ning kes ja millal neid tegi.
2.	Taastada varasemad versioonid: Kui avastate vea või probleemi, saab commit'ide abil hõlpsasti taastada projekti varasema, töötava versiooni.
3.	Võrrelda muudatusi: Commit'ide abil saab võrrelda kahte erinevat versiooni, et näha, milliseid muudatusi on tehtud või mis võivad põhjustada konflikte.
4.	Töötada koos ühe projekti kallal: Git võimaldab commitida mitme kasutaja muudatusi ühte repositooriumisse, osutades seejuures konkureerivatele muudatustele (*merge conflict*).


## Commit'i head tavad
Heade commit'ide loomiseks ja parema projekti ajaloo säilitamiseks on mõned head tavad, mida tuleks järgida:

1.	**Ühe commit'i kohta üks asi.** Commitist tasub mõelda kui pakendist, millesse käivad vaid teineteisega seotud muudatused. Proovige commit'ida ainult ühe funktsiooni või paranduse korraga, et hoida oma projekti ajalugu puhas ja arusaadav. Kui teil on mitu muudatust, mis pole omavahel seotud, tuleks teha mitu commit'i.
2.	**Tehke sageli commit'e.** Commit'ige sageli, et hoida oma projekti ajalugu selge ja lihtne. See aitab ka probleemide lahendamisel, kuna saate hõlpsalt tuvastada, millal ja kus probleem tekkis.
3.	**Kirjutage selgeid ja informatiivseid commit-sõnumeid.** Hea commit-sõnum kirjeldab lühidalt ja arusaadavalt, mida muudatused endast kujutavad. See aitab hiljem mõista teie muudatusi. Hea commit-sõnumi osad on:
	1.	Lühidalt muudatuse sisu käskivas kõneviisis (nt. „Fix bug blah in Blogh“) (kuni 50 märki)
	2.	Tühi teine rida.
	3.	Pikem ülevaade muudatuse sisust ja eesmärkidest, mida commitiga püüad saavutada.
	
4.	**Lahendage konfliktid enne commit'imist.** Kui on tekkinud konflikte teiste arendajate muudatustega, püüdke need lahendada enne uue commit'i tegemist. See aitab vältida konfliktide kuhjumist ja võimaldab teil säilitada projekti ajaloo korrektsuse.

Dokumendi tegijad: Karl Erik ja Kristi