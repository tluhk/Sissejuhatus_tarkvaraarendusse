Kes loengus ei olnud, siis kõigepealt tuleb teha koduste tööde [repositooriumisse](https://github.com/tluhk/RIF22_kodutood):

- Oma nimega branch kujul: Eesnimi_Perekonnanimi
- Kaust Eesnimi_Perekonnanimi
- Sinna alla loo fail README.md, mille sisse lisa oma nimi
- Loo kaust Programmeerimine_I
- Sinna alla loo fail README.md
- Loo kaust SJTA
- Sinna alla loo fail README.md

Esialgne kaustade struktuur peaks välja nägema sarnane:

```bash
├── Eesnimi_Perekonnanimi
│   ├── Programmeerimine_I
│   │   ├── Kodune_1
│   │   ├── Kodune_2
│   │   └── README.md
│   ├── SJTA
│   │   └── README.md
└── README.md
```

Kui tegid/teed oma haru peale loengut, siis sisaldab `main` haru juba mõningaid uusi kaustu, mis tulevad Sinu loodud harusse kaasa - need on seotud Programmeerimine I aine kodutööde automaatse testimisega, millest räägime konsultatsioonis ja järgmistes loengutes.

Tõenäoliselt paistab sellisel juhul kaustastruktuur lõpuks välja sarnane:

```bash
├── .github/workflows
|   └── homework1.yml
├── Eesnimi_Perekonnanimi
│   ├── Programmeerimine_I
│   │   ├── Kodune_1
│   │   ├── Kodune_2
│   │   └── README.md
│   ├── SJTA
│   │   └── README.md
├── test
|   └── math.test.js
├── .gitattributes
├── .gitignore
├── README.md
├── package-lock.json
└── package.json
```

Tähtajad vastavalt Programmeerimine I aine [tähtaegadele](https://github.com/tluhk/Programmeerimine_I/blob/master/lessons/loeng_02/about.md#kodune-t%C3%B6%C3%B6).

- Endanimelises kaustas README.md lühikese ülevaade oma kodutööde kohta
  - Kuidas ülesande lahendamisele lähenesid
  - Kas oli probleeme
  - Kuidas probleemid lahendasid
- Programmeerimine I ülesanded
- Oma Programmeerimine I kausta
  - Kodune_1
  - Kodune_2
  
  Issue: https://github.com/tluhk/Sissejuhatus_tarkvaraarendusse/issues/8
  
