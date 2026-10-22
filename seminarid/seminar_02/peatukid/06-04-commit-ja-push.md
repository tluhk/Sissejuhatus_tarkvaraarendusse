# 4. Commit ja push

```bash
git status
git add research/mari-tamm-probleemikandidaadid.md
git diff --cached
git commit -m "Add timetable problem candidates"
git push -u origin issue-12-map-problem-candidates
```

- `status` näitab muutunud faile.
- `add` valib nimetatud faili järgmise commit'i jaoks.
- `diff --cached` näitab valitud muudatusi. Kontrolli sisu enne jätkamist.
- `commit` salvestab valiku kohalikku ajalukku.
- `push` saadab haru GitHubi; `-u` seob kohaliku haru kaugemas repos oleva haruga. Hiljem piisab samas harus käsust `git push`.

Üks commit olgu üks loogiline muudatus. Ingliskeelne sõnum algab tegusõnaga ja ütleb, mida muudeti. Näiteks `Clarify problem impact` annab rohkem infot kui `update`. Põhjenduse saab vajaduse korral lisada pikemasse sõnumisse. Lisalugemine: [commit'i sõnumite head tavad](../../../concepts/commit/README.md).
