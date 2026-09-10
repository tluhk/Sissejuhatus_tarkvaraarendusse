# Kodutöö 1: minu arenduskeskkond

## Ülesanne lühidalt

Täienda oma olemasolevat `SJTA` repositooriumi failiga, milles kirjeldad enda arenduskeskkonda ja näitad, et seminaris seadistatud põhilised töövahendid töötavad. Salvesta muudatus commit'iga ja saada see GitHubi.

See ülesanne ei korda varem tehtud õpikeskkonnaga tutvumise ülesannet. Uut repositooriumi ega GitHubi organisatsiooni pole vaja luua.

## Eesmärk

Kodutöö järel oskad:

- luua kausta ja Markdown-faili;
- kirjeldada erinevate arendustööriistade ülesandeid;
- kontrollida terminalis Giti olemasolu ja enda asukohta;
- vaadata muudatuse enne salvestamist üle;
- teha terminalis commit'i ja push'i;
- kontrollida tulemust GitHubis.

## Ülesanne

### 1. Ava olemasolev repositoorium

Kasuta oma olemasolevat `SJTA` repositooriumi. Ava selle kohalik kaust VS Code'is. Kui repositoorium pole veel sinu arvutis, klooni see GitHubist seminaris kasutatud HTTPS-töövooga. SSH-d pole selle ülesande jaoks vaja seadistada.

Kloonimiseks kopeeri enda repo **Code → HTTPS** aadress. Ava terminal kaustas, kuhu soovid koolitööd paigutada, ning kirjuta `git clone`, tühik ja kopeeritud aadress. Seejärel ava loodud repo kaust VS Code'is. Juba kloonitud repot pole vaja uuesti kloonida.

Ava repo kaustal **Open in Integrated Terminal**. Kontrolli käsuga `pwd`, kus asud, ning käsuga `git status`, kas Git tunneb repo ära. Windowsis kasuta Git Bashi.

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
```

## Töövahendite rollid

| Töövahend | Milleks seda kasutatakse? | Kas minu arvutis töötab? |
|---|---|---|
| VS Code või alternatiiv | ... | jah/ei |
| Git | ... | jah/ei |
| GitHub | ... | jah/ei |

## Minu terminalispikker

Selgita oma sõnadega, mida teevad `pwd`, `ls`, `cd`, `git status`, `git add`, `git commit` ja `git push`. Lisa üks näide, millal mõnda neist vajad.

## Mida õppisin?

Kirjuta 5–8 lauset: mis oli uus, mis oli keeruline, mille poolest erinevad faili salvestamine, commit ja push ning miks on tarkvaraarendus meeskonnatöö ka siis, kui osa tööst teeb AI.
````

Kopeeri Giti versioon terminalist, kuid ära lisa faili paroole, võtmeid ega muud tundlikku teavet. Node.js-i, npm-i, Dockerit ja GitHub CLI-d ei pea selle kodutöö jaoks paigaldama ega kontrollima. Soovi korral võid nende kohta lisada eraldi valikulise osa.

GitHub CLI on valikuline. Kui see on paigaldatud, võid lisada ka `gh --version` tulemuse ja proovida käske `gh auth status`, `gh repo view` ning `gh issue list`.

### 4. Vaata muudatus üle

1. Salvesta fail: **Ctrl+S** või macOS-is **Cmd+S**.
2. Ava käsupaletist **Markdown: Open Preview to the Side** ning kontrolli vormindust.
3. Käivita repo kausta terminalis `git status`. Uus fail või kaust võib olla märgitud kui **untracked** — see tähendab, et Git ei jälgi seda veel.
4. Loe faili sisu üle ja paranda vead.

### 5. Tee commit ja push

Käivita käsud repo kausta terminalis ükshaaval:

```bash
git add seminar-01/arenduskeskkond.md
git diff --cached
git commit -m "Add development environment notes"
git push
```

- `git add` valib selle faili järgmisesse commit'i ehk lisab selle ettevalmistusalasse (*staging area*).
- `git diff --cached` näitab valitud muudatusi. Kontrolli, et kaasas on soovitud sisu. Kui avaneb keritav vaade, väljud klahviga `q`.
- `git commit` salvestab valitud muudatused kohalikku Giti ajalukku. Sõnum on tunnis kokku lepitud inglise keeles ja ütleb, mida muudatus teeb.
- `git push` saadab kohalikud commit'id GitHubi.

Faili salvestamine üksi ei loo commit'i. Commit üksi ei saada midagi GitHubi. Piisab ühest sisulisest commit'ist; kunstlikult muudatusi juurde tekitama ei pea.

Kui käsk annab vea, peatu selle sammu juures. Kui Git küsib autori nime või e-posti, kasuta [seminarimaterjali seadistusjuhist](seminar.md#esimene-commit-küsib-kasutaja-nime-ja-e-posti). Kui push ei õnnestu, ära kasuta sunnitud saatmist (*force push*); kirjelda takistust allpool toodud viisil. Juba tuttav Source Controli graafiline töövoog on samuti lubatud.

### 6. Kontrolli tulemust GitHubis

Kontrolli, et fail `seminar-01/arenduskeskkond.md` on GitHubis nähtav, Markdown on korrektselt vormindatud ja commit'i ajaloos on commit `Add development environment notes`.

## Esitamine

Ülesanne saadetakse sulle GitHub Issue'na. Lisa issue kommentaari link failile `seminar-01/arenduskeskkond.md` ning kasuta juba tutvustatud esitamise töövoogu.

```text
Valmis töö: https://github.com/ORGANISATSIOON/SJTA/blob/master/seminar-01/arenduskeskkond.md
```

Kui sinu vaikimisi haru nimi on `main`, kasuta lingis `master` asemel `main`.

### Kui töö jäi tehnilise takistuse taha

Lisa sama Issue kommentaari, millise sammuni jõudsid, milline käsk ebaõnnestus, täpne veateade ja mida juba proovisid. Vajaduse korral lisa sinna ka valmis Markdown-tekst. Eemalda veateatest või kuvatõmmiselt saladused. Märgi selgelt, et push jäi pooleli: see on abipalve ja vahetulemus, mitte kinnitus edukast saatmisest. Nii saab õppejõud abi kavandada enne järgmist seminari.

## Valmis töö kontrollnimekiri

- [ ] Kasutasin olemasolevat `SJTA` repositooriumi.
- [ ] Lõin faili `seminar-01/arenduskeskkond.md`.
- [ ] Lisasin operatsioonisüsteemi, redaktori ning terminali või käsukesta.
- [ ] Lisasin Giti versiooni.
- [ ] Koostasin seitsme käsu terminalispikri.
- [ ] Selgitasin töövahendite rolle oma sõnadega.
- [ ] Kirjutasin 5–8-lauselise refleksiooni, sealhulgas salvestamise, commit'i ja push'i erinevuse.
- [ ] Vaatasin muudatuse enne commit'i üle.
- [ ] Tegin commit'i ja push'i.
- [ ] Kontrollisin faili ja commit'i GitHubis.
- [ ] Lisasin issue kommentaari lingi valmis failile.

Kui mõni samm jäi tegemata, jäta selle kontrollkast märkimata ning kirjelda Issue kommentaaris takistust.
