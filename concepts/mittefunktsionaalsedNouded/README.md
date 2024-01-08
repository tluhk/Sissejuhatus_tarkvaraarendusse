# Mittefunktsionaalsed nõuded

**Mittefunktsionaalsed nõuded** (ka kvaliteedi atribuudid või -omadused) on tarkvaraarenduse projekti või organisatsiooni jaoks olulised kriteeriumid, mis määravad süsteemi kvaliteedi, toimivuse ja töökindluse, kuid ei ole seotud süsteemi konkreetsete funktsionaalsete omadustega.

Erinevalt **funktsionaalsetest nõuetest**, mis kirjeldavad, mida tarkvara peaks tegema (näiteks, milliseid toiminguid kasutajad saavad teha), **keskenduvad mittefunktsionaalsed** nõuded tarkvara üldistele omadustele, mis mõjutavad süsteemi kasutatavust, efektiivsust ja hooldatavust.

## Mõned levinumad mittefunktsionaalsed nõuded hõlmavad järgmist:

- **Jõudlus:** Kui kiiresti süsteem töötab ja kui suur on süsteemi ressursikasutus. Näiteks võib nõuda, et veebisait laadiks alla 3 sekundi jooksul või et andmebaasipäringud vastaksid 100 ms jooksul.

- **Skaleeritavus:** Kui hästi süsteem suudab kohaneda kasvava koormusega, olgu see kasutajate arv, andmebaasi suurus või tehingute maht.

- **Turvalisus:** Kui hästi süsteem kaitseb end kasutajate, andmete ja ressursside vastu suunatud ohtude eest, nagu häkkimine, andmete vargus, ebaseaduslik juurdepääs jne.

- **Usaldusväärsus:** Kui stabiilne on süsteem ja kui hästi see suudab taluda erinevaid tõrkeid ja vigu, tagades pideva töö ja teenuste kättesaadavuse.

- **Hooldatavus:** Kui lihtne on süsteemi muuta, parandada ja laiendada, et vastata uutele nõuetele või tehnoloogilistele arengutele. See hõlmab ka koodi loetavust, modulaarsust ja dokumenteerimist.

- **Kasutatavus:** Kui lihtne on süsteemi kasutajatel õppida, kasutada ja tõhusalt töötada. See hõlmab kasutajaliidese disaini, kasutajate abistamist ning süsteemi intuitiivsust ja kasutajamugavust.

- **Ühilduvus:** Kui hästi süsteem töötab erinevates keskkondades, nagu erinevad operatsioonisüsteemid, brauserid, riistvara jne.

## Lisaks võivad kehtida mittefunktsionaalsed nõuded ka kirjutatavale koodile, näiteks:

- **Koodi loetavus:** Kood peaks olema lihtne lugeda ja mõista. Hea koodi loetavus hõlmab korralikku indentatsiooni, selget muutujate ja funktsioonide nimetamist ning piisavat kommenteerimist.

- **Koodi struktuur ja modulaarsus:** Kood peaks olema organiseeritud ja struktureeritud viisil, mis toetab modulaarsust, komponentide taaskasutatavust ja lihtsustab hooldust. See hõlmab näiteks objektorienteeritud programmeerimise põhimõtete järgimist, kapseldamist ja disainimustreid.

- **Dokumentatsioon:** Kood peaks olema hästi dokumenteeritud, mis aitab teistel arendajatel mõista koodi eesmärki, struktuuri ja funktsionaalsust. See hõlmab nii koodi siseseid kommentaare kui ka väliseid dokumente, nagu API dokumentatsioon, tehnilised kirjeldused ja kasutusjuhendid.

- **Testitavus:** Kood peaks olema kirjutatud nii, et seda oleks lihtne testida ja veenduda, et see töötab oodatult. See hõlmab tavaliselt ühiktestide kirjutamist, testide katvuse jälgimist ja koodi struktureerimist viisil, mis toetab eraldiseisvaid ja isoleeritud teste.

- **Versioonihaldus:** Koodi arendamise käigus tuleks kasutada versioonihaldussüsteemi (nagu Git), mis võimaldab jälgida muudatusi, teha koostööd teiste arendajatega ja hallata koodibaasi erinevaid versioone.

- **Koodi optimeerimine:** Kood peaks olema optimeeritud nii, et see töötab efektiivselt ja kasutab süsteemi ressursse mõistlikult. See hõlmab ressursikasutuse optimeerimist, algoritmiliste lahenduste valimist ja vajadusel riistvaral põhinevate lahenduste kasutamist.

- **Turvalisus:** Koodis tuleks jälgida turvalisuse parimaid tavasid, vältides turvariske ja haavatavusi. See hõlmab näiteks andmete valideerimist, krüpteerimist, turvaliste protokollide kasutamist ja turvaauditite läbiviimist.

- **Koodi ühilduvus:** Kood peaks olema kirjutatud selliselt, et see oleks ühilduv erinevate platvormide, süsteemide, raamistike ja tehnoloogiatega. See võib hõlmata erinevate programmeerimiskeelte, raamistike, andmebaaside, kolmandate osapoolte teenuste ja muude komponentidega töötamist.

- **Koodi läbipaistvus ja lähtekoodi avatus:** Kui projekt nõuab avatud lähtekoodiga lahendust, peaks kood olema kirjutatud selliselt, et see oleks lihtne üle vaadata, hinnata ja kaasata teisi arendajaid. See võib hõlmata koodi avaldamist avalikes repositooriumites, litsentside kasutamist, mis võimaldavad teistel arendajatel koodi kasutada, muuta ja levitada ning kogukonna kaasamist projekti arendusprotsessi.

- **Arendusstandardite ja kodeerimisstiilide järgimine:** Koodi kirjutamisel peaks järgima organisatsiooni või projekti kehtestatud arendusstandardeid ja kodeerimisstiile. See aitab tagada koodi ühtlust ja lihtsustada koostööd teiste arendajatega.

