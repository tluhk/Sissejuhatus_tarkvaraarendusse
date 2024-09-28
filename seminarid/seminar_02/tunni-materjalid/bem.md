# BEM (Block Element Modifier) metodoloogia

BEM on CSS-i nimetamise konventsioon ja metodoloogia, mis aitab luua taaskasutatavaid ja struktureeritud koodi komponente. BEM jagab kasutajaliidese iseseisvate plokkide kogumiks, muutes CSS-i koodi lihtsamini mõistetavaks ja hooldatavaks.

## BEM-i põhimõtted:

1. **Block (Plokk)**: Iseseisvalt eksisteeriv komponendi osa.
   Näide: `.button`

2. **Element**: Ploki osa, mis ei oma iseseisvat tähendust.
   Näide: `.button__icon`, `.button__text`

3. **Modifier (Muutja)**: Ploki või elemendi variant või olek.
   Näide: `.button--primary`, `.button--secondary`

BEM-i lähenemine (`.button--primary`) on eelistatud järgmistel põhjustel:

1. Selgem hierarhia: BEM näitab selgelt, et `primary` on `button`-i modifikaator.
2. Väiksem spetsiifilisus: `.button.primary` on spetsiifilisem kui `.button--primary`, mis võib põhjustada probleeme ülekirjutamisel.
3. Parem nimeruumide eraldamine: BEM hoiab ära võimalikud konfliktid teiste komponentidega (nt kui on ka `.text` või `.icon` klassid).
4. Järjepidevus: BEM tagab ühtse lähenemise kogu projektis, mis muudab koodi loetavamaks ja hooldatavamaks.

## BEM-i eelised:

- Selge ja arusaadav struktuur
- Lihtne skaleerida ja hooldada
- Vähendab CSS-i spetsiifilisust ja konflikte
- Parandab koodi loetavust ja arendajate vahelist koostööd

BEM aitab luua modulaarse ja korduva CSS-i, mis on eriti kasulik suurtes projektides ja meeskondades.

## HTML ja CSS näide nupukomponendist, mis kasutab BEM-i

### HTML

```html
<div class="button button--primary">
  <span class="button__icon">🔍</span>
  <span class="button__text">Search</span>
</div>

<div class="button button--secondary">
  <span class="button__text">Cancel</span>
</div>
```
