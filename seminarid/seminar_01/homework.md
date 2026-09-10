# Kodutöö 1: minu arenduskeskkond

## Ülesanne lühidalt

Täienda oma olemasolevat `SJTA` repositooriumi failiga, milles kirjeldad enda arenduskeskkonda ja näitad, et seminaris seadistatud põhilised töövahendid töötavad. Salvesta muudatus commit'iga ja saada see GitHubi.

See ülesanne ei korda varem tehtud õpikeskkonnaga tutvumise ülesannet. Uut repositooriumi ega GitHubi organisatsiooni pole vaja luua.

## Eesmärk

Kodutöö järel oskad:

- luua kausta ja Markdown-faili;
- kirjeldada erinevate arendustööriistade ülesandeid;
- kontrollida terminalis Giti, Node.js-i ja npm-i olemasolu;
- vaadata muudatuse enne salvestamist üle;
- teha VS Code'is commit'i ja push'i;
- kontrollida tulemust GitHubis.

## Ülesanne

### 1. Ava olemasolev repositoorium

Kasuta oma olemasolevat `SJTA` repositooriumi. Ava selle kohalik kaust VS Code'is. Kui repositoorium pole veel sinu arvutis, klooni see GitHubist seminaris kasutatud HTTPS-töövooga. SSH-d pole selle ülesande jaoks vaja seadistada.

### 2. Loo kodutöö fail

Loo repositooriumisse järgmine kaust ja fail:

```text
SJTA/
└── seminar-01/
    └── arenduskeskkond.md
```

### 3. Kirjelda oma arenduskeskkonda

Lisa faili vähemalt järgmine struktuur ja asenda näitetekst enda vastustega:

````markdown
# Minu arenduskeskkond

## Minu arvuti

- Operatsioonisüsteem: ...
- Koodiredaktor või IDE: ...
- Terminal ja käsukest (*shell*): ...

## Töövahendite kontroll

```text
git --version: ...
node --version: ...
npm --version: ...
```

## Töövahendite rollid

| Töövahend | Milleks seda kasutatakse? | Kas minu arvutis töötab? |
|---|---|---|
| VS Code või alternatiiv | ... | jah/ei |
| Git | ... | jah/ei |
| GitHub | ... | jah/ei |
| GitHub CLI | ... | pole paigaldatud / jah / ei |
| Node.js | ... | jah/ei |
| npm | ... | jah/ei |
| Docker | ... | pole veel vajalik / jah / ei |

## Mida õppisin?

Kirjuta 3–5 lauset sellest, mis oli uus, milline seadistamise või Giti samm oli kõige keerulisem ning miks ei tähenda tarkvaraarendus ainult koodi kirjutamist ja miks on see meeskonnatöö ka siis, kui osa tööst teeb AI.
````

Kopeeri versiooninumbrid terminalist, kuid ära lisa faili kasutajanimesid, paroole, võtmeid ega muud tundlikku teavet. Dockerit ei pea selle kodutöö jaoks paigaldama.

GitHub CLI on valikuline. Kui see on paigaldatud, võid lisada ka `gh --version` tulemuse ja proovida käske `gh auth status`, `gh repo view` ning `gh issue list`.

### 4. Vaata muudatus üle

1. Ava VS Code'is **Source Control**.
2. Ava muudetud fail ja vaata muudatuste võrdlust.
3. Kontrolli faili Markdowni eelvaates.
4. Paranda kirjavead ja veendu, et failis pole tundlikku teavet.

### 5. Tee commit ja push

Kasuta commit'i sõnumit:

```text
Lisa esimese seminari kodutöö
```

Tee seejärel **Push** või **Sync Changes**.

### 6. Kontrolli tulemust GitHubis

Kontrolli, et fail `seminar-01/arenduskeskkond.md` on GitHubis nähtav, Markdown on korrektselt vormindatud ja commit'i ajaloos on commit `Lisa esimese seminari kodutöö`.

## Esitamine

Ülesanne saadetakse sulle GitHub Issue'na. Lisa issue kommentaari link failile `seminar-01/arenduskeskkond.md` ning kasuta juba tutvustatud esitamise töövoogu.

```text
Valmis töö: https://github.com/ORGANISATSIOON/SJTA/blob/master/seminar-01/arenduskeskkond.md
```

Kui sinu vaikimisi haru nimi on `main`, kasuta lingis `master` asemel `main`.

## Valmis töö kontrollnimekiri

- [ ] Kasutasin olemasolevat `SJTA` repositooriumi.
- [ ] Lõin faili `seminar-01/arenduskeskkond.md`.
- [ ] Lisasin operatsioonisüsteemi, redaktori ning terminali või käsukesta.
- [ ] Lisasin Giti, Node.js-i ja npm-i versioonid.
- [ ] Selgitasin töövahendite rolle oma sõnadega.
- [ ] Kirjutasin 3–5-lauselise refleksiooni.
- [ ] Vaatasin muudatuse enne commit'i üle.
- [ ] Tegin commit'i ja push'i.
- [ ] Kontrollisin faili ja commit'i GitHubis.
- [ ] Lisasin issue kommentaari lingi valmis failile.
