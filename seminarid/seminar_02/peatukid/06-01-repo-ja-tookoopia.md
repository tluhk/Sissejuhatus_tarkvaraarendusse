# 1. Ühine repo ja töökoopia

Õppejõud loob või määrab tiimi repo organisatsioonis `TLUHK-RIF26` ning annab liikmetele ligipääsu. Iga liige võtab kutse vastu ja kloonib **sama repo** oma arvutisse. Kloonimine teeb kohaliku töökoopia; eraldi GitHubi repo ehk fork pole tiimiliikmena vajalik. Üksikuid Issue'sid ei kloonita.

Kopeeri repo lehelt **Code → HTTPS** aadress. Järgmises näites on repo nimeks `tiim-01-tunniplaan`:

```bash
git clone https://github.com/TLUHK-RIF26/tiim-01-tunniplaan.git
cd tiim-01-tunniplaan
git config user.name
git config user.email
```

Esimene rida laeb repo arvutisse, teine avab selle kausta terminalis. Kaks viimast näitavad commit'ide autoriandmeid. GitHubi konto olemasolu ei seadista kohalikku Giti automaatselt. Kui nimi või e-post on vale või puudu, paranda need selles repos:

```bash
git config user.name "Mari Tamm"
git config user.email "sinu-GitHubi-kontoga-seotud-e-post"
```

Esimene rida määrab autori nime, teine e-posti. Kasuta enda GitHubi kontol kinnitatud aadressi või seadetes näidatud `noreply` aadressi. Kui andmed olid õiged, pole neid vaja uuesti määrata. Ava kloonitud kaust VS Code'is.
