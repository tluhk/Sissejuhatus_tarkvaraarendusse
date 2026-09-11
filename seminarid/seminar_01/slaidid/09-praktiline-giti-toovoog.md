---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 1 – praktiline Giti töövoog
---

# Praktiline töö

## Esimene repositoorium ja muudatus

```text
Repo → clone → muuda → commit → push → kontrolli
```

---

## 1. Loo repositoorium

1. Logi GitHubi sisse.
2. Vali **New repository**.
3. Nimi: `sissejuhatus-tarkvaraarendusse`.
4. Vali nähtavus õppejõu juhise järgi.
5. Lisa `README.md`.
6. Vali **Create repository**.

Kui sulle on kursuse repo juba loodud, kasuta seda.

---

## Kontrollpunkt 1

Brauseris on avatud repositoorium, milles on:

- repositooriumi nimi;
- fail `README.md`;
- nupp **Code**;
- vähemalt üks commit.

Ära liigu edasi enne, kui see vaade on olemas.

---

## 2. Kopeeri repositooriumi aadress

1. Vajuta **Code**.
2. Vali **Local**.
3. Vali **HTTPS**.
4. Kopeeri kuvatud aadress.

Aadress lõpeb tavaliselt laiendiga `.git`.

---

## 3. Klooni repositoorium VS Code'i

1. Ava VS Code'i käsupalett:
   - Windows/Linux: `Ctrl+Shift+P`;
   - macOS: `Cmd+Shift+P`.
2. Vali **Git: Clone**.
3. Kleebi repositooriumi HTTPS-aadress.
4. Vali oma kursuse projektide kaust.
5. Ava kloonitud repositoorium.

---

## Kontrollpunkt 2

VS Code'i Exploreris on näha:

- projekti kausta nimi;
- fail `README.md`.

Source Control ei tohiks praegu näidata muutmata failide juures muudatusi.

---

## 4. Muuda README-faili

Lisa enda sisuga:

```markdown
# Sissejuhatus tarkvaraarendusse

## Minust

Minu nimi on ...
```

Salvesta fail.

---

## Lisa veel kaks osa

```markdown
## Miks ma seda kursust õpin?

Kirjuta siia paar lauset.

## Üks tarkvara, mida kasutan iga päev

- Tarkvara nimi:
- Millist probleemi see lahendab?
- Mis juhtuks, kui see ei töötaks?
```

---

# Mis muutus?

Enne commit'i tegemist vaata muudatus alati üle.

<!-- Arutelu: kirjeldage VS Code'i diff-vaate värve ja sümboleid. -->

---

## 5. Vaata muudatus üle

1. Ava **Source Control**.
2. Vali muudetud `README.md`.
3. Vaata eelmist ja uut versiooni.
4. Paranda võimalikud vead.
5. Kontrolli, et failis pole tundlikku teavet.

---

## 6. Tee commit

1. Lisa `README.md` staged changes nimekirja.
2. Kirjuta commit'i sõnum:

   ```text
   Lisa enda tutvustus
   ```

3. Vajuta **Commit**.

Commit salvestab muudatuse kohalikku repositooriumi.

---

# Kas muudatus on nüüd GitHubis?

<!-- Praktiline samm: ärge vajutage veel Sync Changes; värskendage GitHubi lehte. -->

---

## Ei – commit oli kohalik

Muudatuse saatmiseks GitHubi tuleb teha **push**.

1. Vali **Sync Changes** või **Push**.
2. Vajaduse korral logi GitHubi sisse.
3. Oota, kuni saatmine lõpeb.

---

## 7. Kontrolli tulemust GitHubis

1. Ava repositoorium brauseris.
2. Värskenda lehte.
3. Ava `README.md`.
4. Kontrolli uut sisu.
5. Ava commit'ide ajalugu.

Tulemus peab olema nähtav ka väljaspool sinu arvutit.

---

## Praktilise töö kontrollpunkt

- [ ] Repo avaneb VS Code'is kaustana.
- [ ] `README.md` sisaldab sinu teksti.
- [ ] Commit'i sõnum kirjeldab muudatust.
- [ ] Source Control ei näita saatmata muudatusi.
- [ ] Uus commit ja README on GitHubis nähtavad.
