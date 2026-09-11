---
marp: true
theme: default
paginate: true
header: Sissejuhatus tarkvaraarendusse
footer: Seminar 1 – Markdown
---

# Miks mitte kirjutada dokumentatsiooni ainult Wordis?

Millised omadused on arendusprojekti dokumentatsiooni puhul olulised?

<!-- Arutelu: koguge vastused enne Markdowni eeliste vaatamist. -->

---

## Markdown sobib versioonihaldusega

- fail on tavaline lihttekst;
- lähtekoodi on lihtne lugeda;
- Git näitab tekstimuudatusi selgelt;
- sama faili saab töödelda paljude programmidega;
- GitHub kuvab selle vormindatud dokumendina.

---

## Kus Markdowni kasutatakse?

- `README.md` failides;
- dokumentatsioonis;
- GitHub Issues kirjeldustes;
- pull request'ides;
- kommentaarides;
- staatiliste veebilehtede sisus.

Faililaiend on tavaliselt `.md`.

---

## Markdowni põhisüntaks

```markdown
# Pealkiri

## Alapealkiri

Tavaline tekst ja **paks tekst**.

- loendi esimene punkt
- loendi teine punkt

[Lingi tekst](https://example.com)

`failinimi.md`
```

---

# Mida Markdown kirjeldab?

- Dokumendi täpset visuaalset kujundust?
- Dokumendi struktuuri ja tähendust?

---

## Markdown kirjeldab struktuuri

Markdown ütleb näiteks:

- see on pealkiri;
- see on loend;
- see on link;
- see on kood.

Kuvav programm otsustab, kuidas need elemendid täpselt välja näevad.

---

## Vaata kahte vaadet

1. Ava `README.md` VS Code'is lähdetekstina.
2. Ava sama fail GitHubis vormindatud dokumendina.
3. Leia, kuidas `#`, `##`, `-` ja `**` tulemust muudavad.
