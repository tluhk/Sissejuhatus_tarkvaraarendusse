---
marp: true
---
# Sissejuhatus tarkvaraarendusse

Martti Raavel
<martti.raavel@tlu.ee>

---

## Kolmas loeng

- [Meenutame eelmist loengut](../loeng_02/README.md)
- RK lehekülje kasutajalood
- Eelmiste koduste tööde seis
- Kuidas on läinud ESLint tööriistaga?
- [Tarkvaraarenduse mudelid](../../../concepts/arendusmeetodid/README.md)
- [Rollid tarkvaraarenduses](../../../concepts/rollid/README.md)
- [Dokumentatsioon](../../../concepts/dokumentatsioon/README.md)

---

## Kodustest töödest

- Kuidas läks?
- Milline on seis varasemate koduste töödega?
- ESLint

---

## Tarkvaraarenduse mudelid

Tarkvaraarenduse mudelid on struktureeritud lähenemised tarkvaraarendusele, mis määratlevad etapid ja protsessid, mida tuleb järgida tarkvara tootmisel. Need mudelid võivad olla lineaarsed, järjestikused või iteratiivsed, sõltuvalt projekti olemusest ja nõuetest.

---

## Tarkvaraarenduse mudelid - Arutelu

---

## Tarkvaraarenduse mudelid - Kose mudel (Waterfall)

- **Kirjeldus:** Lineaarne ja järjestikune lähenemine, kus iga faas tuleb lõpetada enne järgmise algust. See on varaseim SDLC lähenemine.
- **Eelised:** Selge struktuur, lihtne mõistmine, hästi määratletud etapid.
- **Puudused:** Pärast faasi lõpetamist on muudatuste tegemine keeruline, ei sobi keerukate projektide jaoks.

---

## Tarkvaraarenduse mudelid - Agiilne mudel (Agile)

- **Kirjeldus:** Iteratiivne lähenemine tarkvara tarnimisele, mis ehitab tarkvara järk-järgult, keskendudes kliendi tagasisidele ja kiiretele iteratsioonidele.
- **Eelised:** Paindlik, edendab iteratiivset tagasisidet, julgustab kliendi kaasamist.
- **Puudused:** Vähem ennustatav, võib olla raske mõista neile, kes on harjunud traditsiooniliste meetoditega.

---

## Tarkvaraarenduse mudelid - Kanban

- **Kirjeldus:** Visuaalne protsessijuhtimise lähenemine, mis võtab vihjeid lean tootmisest ja rõhutab just õigeaegset tarnimist.
- **Eelised:** Paindlikkus, pidev tarnimine, visuaalne olemus aitab tuvastada kitsaskohti.
- **Puudused:** Vähem struktureeritud, võib viia ülekoormuseni, kui seda korralikult ei hallata.

---

## Tarkvaraarenduse mudelid - Scrum

- **Kirjeldus:** Agiilse metodoloogia tüüp, mis korraldab töö tsüklitena, mida nimetatakse "Sprintideks", mis kestavad tavaliselt 2-4 nädalat.
- **Eelised:** Regulaarsed toodete tarned, läbipaistvus, kohandatavus.
- **Puudused:** Nõuab kogenud meeskonnaliikmeid, ulatus võib mõnikord olla liiga paindlik.

---

## Tarkvaraarenduse mudelid - Extreme Programming (XP)

- **Kirjeldus:** Agiilne raamistik, mis rõhutab kliendi rahulolu, pakkudes sagedasi "väljalaskeid" lühikeste arendustsüklite jooksul, eesmärgiga parandada tootlikkust ja tutvustada kontrollpunkte.
- **Eelised:** Rõhutab koodi kvaliteeti, julgustab kliendi kaasamist.
- **Puudused:** Nõuab ulatuslikku kliendi kaasamist, võib olla arendajatele väga intensiivne.

---

## Rollid tarkvaraarenduses

Tarkvaraarenduse valdkonnas võivad isikud täita erinevaid rolle, millest igaühel on oma eripärad ja panused üldprojekti.

---

## Rollid tarkvaraarenduses - Arutelu

---

## Rollid arenduses

- Tarkvaraarhitekt (_software architect_)
- Süsteemianalüütik (_system analyst_)
- Programmeerija (_programmer_)
- Arendaja (_developer_)
- Tarkvarainsener (_software engineer_)
- Testija (_quality assurance tester_)
- Süsteemiadministraator (_system administrator_)
- Andmebaasi administraator (_database administrator_)
- Kasutajatugi (_helpdesk_)
- Koolitaja (_training_)
- Projektijuht (_project manager_)
- Arenduse juht (_development manager_)

---

## Tarkvaraarhitekt (_software architect_)

Tarkvaraarhitekt planeerib tarkvara ülesehituse: millistest osadest tarkvara koosneb, kuidase need omavahel ja välismaailmaga suhtlevad.

---

## Süsteemianalüütik (_system analyst_)

Süsteemianalüütik aitab 'tõlkida' ärisoovid arendajatele sobivateks juhisteks.

Tarkvaraarhitekti ja süsteemianalüütiku plaanide järgi saab tarkvara loomisega alustada. Tarkvara kirjutamise ehk programmeerimisega on seotud mitmed ametinimetused. Tasub märkida, et neid nimetusi kasutatakse paindlikult, erinevalt ja teineteisega vahetatavalt, mistõttu ei ole need alati siintoodud tähendusega.

---

## Programmeerija (_programmer_)

Programmeerija on keegi, kes kirjutab programmi. Kõige lihtsamalt võib see olla keegi, kes instruktsioonide järgi programmi kirjutab, ise programmi ehitusele vähe mõeldes.

Üldnimetusena võib see tähistada ükskõik millist programmi kirjutamisega seotud ametit.

---

## Arendaja (_developer_)

Arendaja on üldmõiste töötaja kohta, kes tarkvara loob. Arendustööks on vaja arusaamist programmeerimiskeelest ja nõuetest, kuid keerukamate ülesannete jaoks võib olla tarvis laialdasemaid teadmisi. Oskuste, kogemuste ning vastutuse põhjal eristatakse vahel nooremarendajat (_junior developer_), kellele usaldatakse enamasti kergemad ülesanded, ja vanemarendajat (_senior developer_), kes saab hakkama nõudlikumate töödega.

---

## Tarkvarainsener (_software engineer_)

Tarkvarainsener tunneb programmeerimisega seotud infotehnoloogilisi võimalusi (raamistikke, malle, arhitektuure, protsesse, tehnikaid jne.) ning oskab neid otstarbekohaselt rakendada. Tihti võib see kattuda arendaja või vanemarendaja töökirjeldusega.

---

## Testija (_quality assurance tester_)

Testija kontrollib, et tarkvara teeks seda, mida ta peab tegema, ehk et ärisoovid oleksid täidetud ning tarkvaras ei oleks vigu. Seda rolli saab võrrelda järelevalveametniku rolliga ehituses.

---

## Süsteemiadministraator (_system administrator_)

Süsteemiadministraator vastutab arvutisüsteemide eest; hangib, paigaldab ja uuendab tarkvara ja riistvarakomponendid, ehk kannab hoolt, et kõik süsteemid oleksid töökorras.

---

## Andmebaasi administraator (_database administrator_)

Andmebaasi administraator haldab andmebaasi, vastutab andmete säilitamise, rakenduse töötamise eest.

---

## Kasutajatugi (_helpdesk_)

Kasutajatugi aitab kasutajatel tarkvara kasutada.

---

## Koolitaja (_training_)

Koolitaja õpetab lõppkasutajat tarkvara kasutama, vajadusel vastutab kasutamiseks vajalike dokumentide loomise eest. Ka maja ehitamisel saab omanik palju “koolitajatega” kokku.

---

## Projektijuht (_project manager_)

Projektijuht juhib projekti töökorraldust, hoolitseb lõpptulemuse saavutamise eest, jälgib eelarve täitmist.

---

## Arenduse juht (_development manager_)

Arenduse juht koordineerib koostööd projektide vahel, saab projekti katkestada

---

## Dokumentatsioon

Tarkvaraarenduse dokumentatsioon viitab kirjalike või visuaalsete materjalide loomise ja korrastamise protsessile, mis kirjeldavad tarkvaratoote või -süsteemi disaini, arendust ja kasutamist.

---

## Tehnilised kirjeldused

Dokumendid, mis kirjeldavad tarkvarasüsteemi, sealhulgas andmestruktuuride, algoritmide ja liideste kavandamist ja rakendamist.

---

## Kasutusjuhendid

Dokumendid, mis kirjeldavad tarkvaratoote kasutamist, sealhulgas installi-, konfiguratsiooni- ja kasutusjuhiseid.

---

## Väljalaskemärkmed

Dokumendid, mis kirjeldavad tarkvaratoote iga versiooni muudatusi ja täiustusi.

---

## Koodikommentaarid

Kommentaarid, mis lisatakse tarkvaratoote lähtekoodile, et kirjeldada, kuidas koodi erinevad osad töötavad ja kuidas need on kasutamiseks mõeldud.

---

## API dokumentatsioon

Dokumendid, mis kirjeldavad tarkvarasüsteemi poolt avaldatavaid liideseid, sealhulgas iga liidese sisendeid, väljundeid ja käitumist.

---

## Dokumentatsiooni loomine

Tarkvaraarenduse dokumentatsiooni koostamine võib olla keeruline protsess, kuna olenevalt projekti vajadustest võib olla vaja koostada palju erinevat tüüpi dokumentatsiooni. Siin on aga mõned üldised sammud, mida saab tõhusa tarkvaraarenduse dokumentatsiooni loomiseks järgida

---

## Tehke kindlaks dokumentatsiooni eesmärk ja ulatus

Enne dokumentatsiooni loomise alustamist on oluline kindlaks teha, millist tüüpi dokumentatsiooni on vaja, kes on sihtrühm ja millised on dokumentatsiooni eesmärgid.

---

## Dokumentatsiooni kavandamine

See samm hõlmab dokumentatsiooni struktuuri, vormingu ja sisu määratlemist. Peaksite kaaluma dokumentatsiooni (nt tekst, diagrammid või videod) parimat vormingut ja otsustama, milline sisu tuleb kaasata.

---

## Dokumentatsiooni kirjutamine

Kui planeerimine on lõpetatud, võite alustada dokumentatsiooni kirjutamist. Kasutage selget ja ülevaatlikku keelt ning veenduge, et dokumentatsioon oleks kergesti loetav ja arusaadav. Peaksite lisama ka kõik asjakohased diagrammid, pildid ja viited, mis aitavad sisu selgitada.

---

## Dokumentatsiooni testimine ja ülevaatamine

Oluline on dokumentatsiooni testida, et olla kindel, et see on täpne ja hõlpsasti jälgitav. See võib hõlmata seda, et teised arendajad, sidusrühmad või lõppkasutajad vaatavad tagasiside andmiseks dokumentatsiooni üle.

---

## Dokumentatsiooni värskendamine ja hooldamine

Tarkvaraarendus on pidev protsess, mistõttu on oluline dokumentatsiooni projekti edenedes uuendada ja säilitada. See võib hõlmata uue teabe lisamist, olemasoleva teabe värskendamist ja aegunud teabe eemaldamist.

---

## Näpunäiteid

- Kasutage kogu dokumentatsioonis ühtset vormingut ja stiili
- Keeruliste mõistete selgitamiseks kasutage diagramme ja pilte
- Hoidke dokumentatsioon ajakohasena
- Kasutage selget ja kokkuvõtlikku keelt
- Kaaluge sihtrühma vajadusi ja vaatenurki

---

## Kodune töö
