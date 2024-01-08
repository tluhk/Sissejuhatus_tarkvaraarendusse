# Pull Request

Pull Request (PR) on GitHubis, GitLabis ja teistes Git-põhistes versioonihaldussüsteemides kasutatav mehhanism, mis võimaldab arendajatel teavitada teisi arendajaid oma muudatustest, mis on tehtud koodi baasis, ning paluda neil üle vaadata ja lisada need muudatused peamisse koodi harusse (tavaliselt `master` või `main` haru).

Pull Requesti loomine algab tavaliselt koodi muudatuste tegemisega uues harus. Kui arendaja on oma muudatustega rahul, pushib ta selle haru repositooriumi ja loob Pull Requesti, mis sisaldab teavet muudatuste kohta, sealhulgas:
- Millised muudatused on tehtud (st, millised failid on muudetud ja millised on nende muudatuste sisu)
- Millist probleemi või funktsiooni need muudatused lahendavad või täiendavad
- Kellele tuleks see Pull Request suunata ülevaatamiseks (tavaliselt mõni teine arendaja või meeskonnaliige)

Ülevaatajad saavad seejärel Pull Requesti vaadata, kommenteerida, esitada küsimusi, soovitada muudatusi või nõustuda muudatustega ja lisada need peamisse harusse. Pull Requestide kasutamine aitab tagada, et koodi muudatused on läbipaistvad, arutatavad ja läbivaadatavad, enne kui need lisatakse peamisse koodibaasi. See protsess aitab parandada koodi kvaliteeti, vähendada vigu ja tagada, et kõik meeskonnaliikmed on kursis projekti arenguga.

Vaata ka: [Pull Requesti kodutöö](../../homeworks/pullRequest/README.md)

## Harude nimetamine

Harude nimetamine võib olla projektipõhine ja erinevates organisatsioonides võib olla erinevaid konventsioone. Siin on mõned levinud harunimede tüübid ja nende otstarve:

- **Feature branches:** Need harud loovad uue funktsionaalsuse arendamiseks ja nimetatakse tavaliselt `feature/` prefiksiga, millele järgneb funktsiooni nimi või lühike kirjeldus. Näiteks `feature/user-authentication` või `feature/payment-gateway-integration`.

- **Bugfix branches:** Need harud parandavad olemasolevat koodi, mis sisaldab vigu. Tavaliselt nimetatakse neid `bugfix/` või `fix/` prefiksiga, millele järgneb viga kirjeldav nimi või veanumber. Näiteks `bugfix/missing-data-validation` või `fix/issue-123`.

- **Hotfix branches:** Need harud on ette nähtud kriitiliste probleemide lahendamiseks, mis nõuavad kiiret lahendust. Nimetatakse tavaliselt `hotfix/` prefiksiga, millele järgneb probleemi kirjeldus või veanumber. Näiteks `hotfix/security-vulnerability` või `hotfix/issue-456`.

- **Release branches:** Need harud on mõeldud tarkvara versioonide ettevalmistamiseks ja haldamiseks. Tavaliselt nimetatakse `release/` prefiksiga, millele järgneb versiooninumber. Näiteks `release/1.0.0` või `release/v2.3.1`.

- **Development branches:** Need harud on mõeldud kogu meeskonna igapäevaseks arendustegevuseks ja nimetatakse tavaliselt `dev` või `development`.

- **Peaharud:** Need harud sisaldavad kogu projekti põhikoodi ja neid kasutatakse tavaliselt peamise tarkvara versiooni haldamiseks. Nimega `main` või `master` (kuigi "main" on muutumas tavapärasemaks).

Lisaks nendele levinud harunimede tüüpidele võivad organisatsioonid kasutada ka muid nimekonventsioone, mis põhinevad projekti eripäradel, arendusprotsessidel või meeskonna eelistustel.