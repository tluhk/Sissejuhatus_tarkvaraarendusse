# Forkimine

GitHubi repositooriumi forkimine tähendab repositooriumi koopia loomist sinu enda GitHubi kontole. See koopia on sinu isiklik repositoorium, kus saad teha muudatusi ja katsetusi ilma, et see mõjutaks originaalrepositooriumit. Forkitud repositoorium säilitab seose algse repositooriumiga, mis võimaldab sul jälgida algse repositooriumi muudatusi ja vajadusel neid ka enda forkitud repositooriumiga sünkroniseerida.

Forkimine on eriti kasulik avatud lähtekoodiga projektide puhul. See võimaldab sul teha muudatusi ja seejärel esitada need algsele projektile pull requesti kaudu. Pull requestide kaudu saavad projekti omanikud ja teised kaasautorid hinnata ja arutada sinu muudatusi, enne kui need lisatakse algsele repositooriumile.

Forkimise protsess on järgmine:

- Mine GitHubis soovitud repositooriumi lehele.
- Kliki paremas ülanurgas "Fork" nupul.
  ![Fork nupp](./files/forkButton.png)
- Vali `Create a new fork`
- Vali GitHubi konto, kuhu soovid fork'i teha.
  ![Fork Githubi konto valik](files/valiForkKonto.png)
- Pärast forkimist saad kloonida repositooriumi oma arvutisse, luua uusi harusid, teha muudatusi, commit'e ja push'e. Kui soovid oma muudatusi esitada algsele repositooriumile, tuleb sul luua pull request.

Kui oled teinud `forki`, selle oma arvutisse klooninud, teinud selles mingeid muudatusi (koos `commit`i ja `push`iga) ja soovid need muudatused esitada algsele repositooriumile, siis tuleb sul luua `pull request`. Selleks:

- Ava oma GitHubi kontol forkitud repositoorium.
- Vali `Contribute` menüüst `Open pull request`
  ![Pull request](files/pullRequest.png)
- Avanenud vaatest kontrolli üle repositooriumid (millisest millisesse `Pull request` luuakse)
- Täida `Pull request` kirjeldus ja vajadusel määra ülevaataja (`reviewer`)
  ![Pull request](files/comparingChanges.png)
- Kui kõik on korras, siis vajuta `Create pull request` nuppu.
- Määratud ülevaatajale tuleb teade uue `Pull Request`i kohta
  ![Add review](files/addReview.png)
- Vajuta `Review changes` nuppu, lisa oma kommentaarid ja vastavalt vajadusele `Approve` või `Request changes`
  ![Review changes](files/reviewChanges.png)
- Kui kõik on korras, siis vajuta `Merge pull request` nuppu
  ![Merge pull request](files/mergePullRequest.png)
- Seejärel vajuta `Confirm merge` nuppu
  ![Confirm merge](files/confirmMerge.png)


Üldiselt võiks kogu protsessi kirjeldada järgmine diagramm:

```mermaid
sequenceDiagram
    participant U as Arendaja
    participant O as Originaalrepositoorium
    participant F as ArendajaFork
    participant R as Ülevaataja
    U->>+O: Fork repositoorium
    O->>-U: Loob fork'i arendaja kontole
    U->>+F: Klooni fork'i lokaalselt
    F->>-U: Annab kloonitud repositooriumi
    U->>+F: Loo uus haru
    U->>+F: Tee muudatusi
    U->>+F: Commit muudatused
    U->>+F: Push muudatused
    F->>-U: Värskendab repositooriumit
    U->>+O: Loo Pull Request
    O->>-U: PR loodud
    U->>+R: Määra ülevaataja
    R->>+O: Vaata PR üle
    R->>+O: Jäta kommentaarid (kui vajalik)
    R->>-U: Tagasiside arendajale
    U->>+F: Tee vajalikud muudatused
    U->>+F: Commit ja push muudatused
    F->>-U: Värskendab repositooriumit
    U->>+O: Uuenda PR
    R->>+O: Vaata muudatusi üle
    R->>+O: Kinnita PR
    O->>+O: Merge PR
    O->>-U: Teavitab arendajat edukast merge'st
```