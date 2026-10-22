# Release v0.1.0

## Kuidas release luua?

**Tag** tähistab üht kindlat commit'i. **GitHub Release** lisab sellele versioonile avaldatud kirjelduse. Nii saab hiljem vaadata, milline oli dokumentatsioon just selle etapi lõpus.

Kursusel tähistame projektietappe versioonidega: seminar 2 `v0.1.0`, seminar 3 `v0.2.0`, seminar 4 `v0.3.0`, seminar 5 `v0.4.0` ja eksam `v1.0.0`. Kõigil tiimiliikmetel on ühine etapi versioon. See on kursuse kokkulepe; üksik PR ei vaja uut tag'i.

Release manager:

1. Kontrollib, et etapi PR-id on üle vaadatud ja ühendatud ning `main` sisaldab otsust, refleksioone ja release'i kirjeldust.
2. Avab repo **Releases → Draft a new release**.
3. Valib uue tag'i nimeks `v0.1.0` ja sihiks etapi lõppseisu sisaldava `main`-i commit'i. Tag märgib ka faile, mitte üksnes pealkirja.
4. Paneb pealkirjaks `Probleem sõnastatud`, lisab kokkuvõtte ning lingi faili `releases/v0.1.0.md` juurde.
5. Valib **Publish release**. Pelgalt mustandi salvestamine versiooni ei avalda.
6. Avab avaldatud release'i ja selle tag'i failivaate. Kontrollib, et vajalikud failid ja lingid on olemas.

Avaldatud tag'i ei tõsteta järgmise töö juurde: see peab säilitama etapi ajaloo. Edasine töö käib uutes harudes ning järgmine etapp saab uue versiooni. Pärast `v0.1.0` uuendab igaüks kohalikku `main`-i; seminaris 3 algab uus Issue nõuete, tööviisi või süsteemi kontseptsiooni täpsustamiseks. Release manageri vastutus vahetub.
