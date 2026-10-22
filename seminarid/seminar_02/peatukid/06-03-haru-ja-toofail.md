# 3. Haru ja tööfail

Kontrolli terminalis, et oled repo kaustas ja töökaust on puhas:

```bash
pwd
git status
git switch main
git pull --ff-only
git switch -c issue-12-map-problem-candidates
mkdir -p research
```

- `pwd` näitab praegust kausta; `git status` näitab haru ja salvestamata muudatusi. Kui sul on varasem töö pooleli, lõpeta see enne haru vahetamist.
- `git switch main` viib peaharusse.
- `git pull --ff-only` toob sinna GitHubi muudatused. Lahknenud ajaloo korral käsk peatub: küsi abi.
- `git switch -c ...` loob ja avab enda ülesande haru. Kasuta ingliskeelset kuju `issue-<number>-<short-english-description>`.
- `mkdir -p research` loob tööfailide kausta, kui seda veel pole.

Loo VS Code'is fail `research/mari-tamm-probleemikandidaadid.md`, lisa enda kandidaadid ja salvesta. Peaharu `main` muudetakse ainult PR-ide kaudu.
