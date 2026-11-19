[← Tagasiside ja areng](02-feedback-and-evolution.md) | [Sisukord](../README.md) | [Järgmine: Sõnastik →](../glossary.md)

# Giti oskus: tag ja ajajoon

**Märge:** Seminaris

> [!NOTE]
> See leht on mustand. Seminari 5 sisu võib pärast selle esimest läbiviimist muutuda.

Igal projektietapil on avaldatud versioon. Kokku moodustavad need **ajajoone**: loo sellest, kuidas meeskonna arusaam probleemist ja lahendusest muutus.

## git tag

**Tag** on nimi, mis on kinnitatud ühele commit'ile (vt osa 2 [Giti oskus: pull ja release](../02-from-request-to-task/07-git-pull-and-release.md)). Tag'id tulevad GitHubist kaasa `pull`-iga.

```bash
git switch main
git pull --ff-only
git tag                                # kõik versioonid
git show v0.2.0 --stat                 # mis commit see on ja mis faile muudeti
git log --oneline v0.1.0..v0.2.0       # commit'id kahe versiooni vahel
```

`v0.1.0..v0.2.0` tähendab „commit'id, mis on versioonis `v0.2.0`, aga mida polnud versioonis `v0.1.0`”. Nii näed, mis tehti ühe etapi jooksul.

## Ajajoon

Ajajoon ei ole commit'ide nimekiri. See näitab, **mis muutis meeskonna arusaama** ja milline otsus sellest tulenes:

```text
v0.1.0  probleem sõnastatud
   ↓    uus tõend: vestlustest selgus, et ...
v0.2.0  tööviis ja süsteemi kontseptsioon
   ↓    risk või kompromiss: andmeallikas osutus ...
v0.3.0  kvaliteedi- ja riskiplaan
   ↓    kasutuselevõtu küsimused
v0.4.0  kasutuselevõtu ja arengu plaan
   ↓    kokkuvõte
v1.0.0  dokumenteeritud protsess
```

Iga versiooni juures vasta:

1. Mis oli selle etapi peamine otsus?
2. Mis tõend või risk selle põhjustas?
3. Mida teaksime nüüd teisiti?

Allikad on käepärast: release'i kirjeldused, otsuste logi ja `git log` kahe versiooni vahel. Hea commit'i sõnum ja otsuste logi teevad ajajoone koostamise lihtsaks. Halbadest sõnumitest ja puuduvatest otsustest ei saa hiljem lugu kokku panna.

## Kontrolli ennast

1. Mida näitab `git log --oneline v0.1.0..v0.2.0`?
2. Miks ei pea ajajoon näitama kõiki commit'e?
3. Vali oma projektist üks otsus ja kirjuta, mis tõend või risk selle põhjustas.

---

[← Tagasiside ja areng](02-feedback-and-evolution.md) | [Sisukord](../README.md) | [Järgmine: Sõnastik →](../glossary.md)
