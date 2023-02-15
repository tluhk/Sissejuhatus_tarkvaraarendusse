# Git

## Mis on git?

Git on hajutatud versioonihaldussüsteem, mis on loodud tarkvara arendamise käigus lähtekoodi muutuste jälgimiseks. Selle töötas välja 2005. aastal Linuxi operatsioonisüsteemi looja Linus Torvalds ja sellest ajast on saanud üks enimkasutatavaid versioonihaldussüsteeme maailmas.

Git on oma põhiolemuselt tööriist koodimuudatuste haldamiseks. See võimaldab arendajatel salvestada oma koodibaasi mitu versiooni, jälgida erinevate inimeste tehtud muudatusi ja liita muudatused tagasi koodibaasi põhiharusse. Git on loodud olema kiire, tõhus ja paindlik, mistõttu sobib see hästi paljude tarkvaraarenduse töövoogudega.

Giti üks peamisi omadusi on selle hajutatud arhitektuur. Giti puhul on igal kasutajal oma kohalik koodibaasi hoidla koos kõigi tehtud muudatuste täieliku ajalooga. See tähendab, et kasutajad saavad töötada keskserverist sõltumatult, muutes võrguühenduseta või lahtiühendatud võrkudes töötamise lihtsaks. Kui muudatused on jagamiseks valmis, saab need lükata (`push`) kesksesse hoidlasse või tõmmata (`pull`) teiste kasutajate hoidlatest (`repository`).

Git sisaldab ka võimsaid hargnemis- ja liitmisvõimalusi (`branch` ja `merge`). Hargnemine võimaldab arendajatel luua uusi sõltumatuid koodibaasi harusid, et testida uusi funktsioone või teha muudatusi ilma põhikoodibaasi häirimata. Ühendamine võimaldab arendajatel ühendada erinevates harudes tehtud muudatused tagasi põhikoodibaasi.

Üldiselt on Git võimas ja paindlik tööriist koodimuudatuste haldamiseks, millest on saanud tänapäevaste tarkvaraarenduse töövoogude oluline komponent. Selle hajutatud arhitektuur, hargnemis- ja liitmisvõimalused ning võime käsitleda suuri koodibaase muudavad selle ideaalseks valikuks igas suuruses ja keerukusega projektide jaoks.

## Git-iga seotud sõnavara

Git-i kasutuselevõtt eeldab teatud terminite tundmist ja aru saamist. Järgnevalt on välja toodud põhiline git-iga seotud sõnavara koos lühikeste selgitustega:

- **Hoidla** (`repository`): hoidla ehk repositoorium on keskne koht koodi ja sellega seotud failide salvestamiseks. Gitis võib hoidla olla kas kohalik või asuda kusagil serveris.

- **Haru** (`branch`): haru on koodibaasi eraldi versioon. Arendajad saavad luua uue haru, et töötada uue funktsiooni või veaparandusega, ilma et see mõjutaks põhikoodibaasi. Filiaalis tehtud muudatused saab liita tagasi põhikoodibaasi, kui need on valmis.

- **`Commit`**: *Commit* on koodibaasi tehtud muudatuste salvestatud komplekt. Kui arendaja teeb koodis muudatusi, saab ta need muudatused hoidlasse salvestamiseks *committida*. Igal *commitil* on kordumatu identifikaator ja sõnum, mis kirjeldab tehtud muudatusi.

- **Tõukamine** (`push`): on Giti käsk, mida kasutatakse kohalikus hoidlas tehtud muudatuste üleslaadimiseks kaughoidlasse. Kui teete kohalikus hoidlas muudatusi, saate tõukekäskluse abil need muudatused kaughoidlasse üles laadida, näiteks GitHubis või GitLabis hostitud hoidlasse.

- **Ühendamine** (`merge`): ühendamine on koodibaasi ühest harust teise tehtud muudatuste kombineerimise protsess. Tavaliselt tehakse seda funktsiooniharus tehtud muudatuste liitmiseks tagasi põhikoodibaasi.

- **Tõmbetaotlus** (`pull request`): Tõmbetaotlus on taotlus teisele arendajale harus tehtud muudatuste ülevaatamiseks ja liitmiseks. Tõmbepäringud sisaldavad tavaliselt tehtud muudatuste loendit, kommentaare ja koodi muudatuste erinevusi.

- **Kloonimine** (`clone`): Kloonimine on hoidlast kohalikku masinasse koopia tegemine. See loob hoidlast kohaliku koopia, mida saab kasutada muudatuste tegemiseks ja keskhoidlasse sidumiseks.

- **Kahvel** (`fork`): kahveldamine (`forking`) on hoidlast koopia tegemine uude eraldi hoidlasse. Seda kasutatakse sageli siis, kui arendajad soovivad luua projektist oma versiooni või teha muudatusi projektis, millele neil pole kirjutamisõigust.

- **Remote**: *remote* on link kaughoidlale, mida tavaliselt hostitakse koodijagamisplatvormil, nagu GitHub või GitLab. Arendajad saavad muudatusi lükata kaughoidlasse või sealt muudatusi tõmmata, et hoida oma kohalik hoidla ajakohasena.

Need on vaid mõned peamised Gitiga seotud sõnavaraterminid. Terminite ja nende tähendustega tutvumine on oluline esimene samm Giti tõhusa kasutamise õppimisel.

## Giti töövoog

Giti töövoog on parimate tavade ja juhiste kogum Giti kasutamiseks koodimuudatuste haldamiseks. Giti töövooge on palju, kuid kõige levinumat neist nimetatakse **funktsioonide haru töövoogudeks**, mida kirjeldatakse allpool:

- **Looge uus haru (branch):** alustage koodibaasi uue haru loomisega uue funktsiooni või veaparanduse jaoks, millega töötate. See hoiab muudatused peamisest koodibaasist eraldatuna, kuni need on ühendamiseks valmis.

- **Muudatuste tegemine:** muutke koodi uues harus, järgides oma organisatsiooni koodikirjutamise- ja testimisstandardeid.

- **Testige muudatusi:** testige muudatusi uues harus, et tagada nende ootuspärane toimimine.

- **Committige muudatused (commit):** kui muudatused toimivad ootuspäraselt, *committige* need uue haru kohalikku hoidlasse. Soovitatav on teha muudatusi sageli koos kirjeldavate kinnitussõnumitega, mis selgitavad, mida ja miks muudeti.

- **Muudatuste tõukamine (push):** lükake muudatused kesksesse hoidlasse, tehes need teistele arendajatele kättesaadavaks. See toimib ka koodimuudatuste varukoopiana.

- **Tõmbetaotluse avamine (pull request):** kui teete koostööd teiste arendajatega, avage tõmbetaotlus, et taotleda oma muudatuste ülevaatamist. See võimaldab teistel arendajatel teie koodi üle vaadata ja tagasisidet anda.

- **Muudatuste ühendamine (merge):** kui muudatused on üle vaadatud ja kinnitatud, ühendage uus haru koodibaasi põhiharuga. See lisab muudatused põhikoodibaasi, muutes need kättesaadavaks kõigile arendajatele.

- **Haru kustutamine**: pärast muudatuste ühendamist kustutage uus haru. See aitab hoida koodibaasi korrastatuna ja hoiab ära segiajamise dubleerivate harudega.

Funktsioonide haru töövoog on vaid üks paljudest võimalikest Giti töövoogudest, kuid see on hea lähtepunkt enamikule arendusmeeskondadele. Selle töövoo peamised eelised hõlmavad paremat koostööd, koodi ülevaatamist ja võimalust töötada uute funktsioonide või veaparandustega ilma peamist koodibaasi häirimata.

## Git-i paigaldamine arvutisse

Giti kasutamiseks arvutis tuleb kõigepealt paigaldada oma arvutisse Giti tarkvara ja see seadistada. 

1. Laadige alla ja installige Git: Giti tarkvara saate alla laadida ametlikult veebisaidilt (https://git-scm.com/downloads). Kui olete installiprogrammi alla laadinud, käivitage see ja järgige installimisprotsessi lõpuleviimiseks installiviisardi juhiseid.

2. Giti konfigureerimine: pärast Giti installimist peate selle konfigureerima oma giti kasutajanime ja e-posti aadressiga. Seda teavet kasutatakse teie tuvastamiseks, kui teete koodis muudatusi. Kasutajanime ja e-posti konfigureerimiseks tuleb käsurealt sisestada järgmised käsud:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Soovi korral on võimalik giti kasutamiseks paigaldada arvutisse ka graafilise kasutajaliidesega tööriist, mis võimaldab paremat kasutajakogemust eriti algajatele kasutajatele, kes ei tunne ennast käsurea kasutamisel väga kindalt.

Graafilisi kasutajaliidesega tööriistu on mitmeid, kuid üks variant on näiteks tasuta tööriist Github Desktop, mille saab alla laadida siit: https://desktop.github.com/
