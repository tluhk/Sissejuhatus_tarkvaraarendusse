# 5. Pull request, ülevaatus ja merge

Ava GitHubis saadetud haru juures **Compare & pull request**. Siht on `main`. Kirjelda muutust ja lisa `Closes #12`, mis seob PR-i ülesandega ning sulgeb selle peaharusse ühendamisel. Vali ülevaatajaks tiimikaaslane ja vii kaart tahvlil olekusse `Review`.

Ülevaataja loeb vahekaardil **Files changed** muudatused läbi. Ta kontrollib, kas kõik kandidaadid on arusaadavad ning tõendid ja oletused eristatud. Seejärel valib ta **Approve** või põhjendatud **Request changes**. Pelk „korras” ei näita veel sisulist kontrolli; kasuta vajaduse korral [PR-i kontrollnimekirja](../../mallid/pull-request.md).

Autor parandab vajaduse korral sama faili samas harus, teeb uue commit'i ja push'i. PR uueneb automaatselt. Pärast kaaslase heakskiitu ühendab autor muudatuse nupuga **Merge pull request**, kustutab GitHubis haru ja märgib töö `Done`. Enda PR-i ise heaks ei kiideta.
