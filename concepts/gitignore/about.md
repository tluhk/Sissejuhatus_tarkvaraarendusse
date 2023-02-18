# .gitignore

`.gitignore` on konfiguratsioonifail, mida Git kasutab, et määrata, millised failid ja kataloogid tuleks versioonihaldussüsteemist välja jätta. Git jälgib muudatusi kõigis hoidlas olevates failides, kuid on teatud faile ja katalooge, mida me ei soovi versioonihaldussüsteemi kaasata. Need võivad hõlmata logifaile, ajutisi faile või faile, mis sisaldavad tundlikke andmeid (nt paroole või API võtmeid).

Loetledes need failid ja kataloogid hoidla juurkataloogis olevas `.gitignore`-failis, välistab Git nende jälgimise ega kuva neid jälgimata failidena, kui näiteks käitame `git status` käsku. See aitab hoida hoidla puhtana ja keskenduda olulistele failidele.

`.gitignore`-fail sisaldab tavaliselt mustrite loendit, mis kirjeldavad ignoreeritavaid faile ja katalooge. Näiteks võime kõigi .log laiendiga failide ignoreerimiseks kasutada järgmist mustrit:

```bash
*.log
```

Keerulisemate mustrite määramiseks saame kasutada ka metamärke ja katalooge. Lisateavet faili `.gitignore` kasutamise kohta leiate [Giti dokumentatsioonist](https://git-scm.com/docs/gitignore).

Näide tüüpilisest `.gitignore` failist, mis sobib NodeJS projekti jaoks:

```bash
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Dependency directories
node_modules/

# Build output
dist/
build/
out/
*.tgz

# Environment variables
.env

# Optional eslint cache
.eslintcache

# Optional Prettier cache
.prettiercache

# OS generated files
.DS_Store
Thumbs.db
```

See fail välistab järgmised failid ja kataloogid:

- Logid: logs, *.log, npm-debug.log*, yarn-debug.log*, yarn-error.log*.
- Sõltuvuskataloogid: node_modules/.
- *Build output*: dist/, build/, out/, *.tgz.
- Keskkonnamuutujad: .env.
- Valikuline eslint-vahemälu: .eslintcache.
- Valikuline *prettier* vahemälu: .prettiercache.
- OS-i loodud failid: .DS_Store, Thumbs.db.

See on vaid näide ja teil võib tekkida vajadus seda kohandada, et see vastaks teie konkreetse projekti vajadustele.

Allikad:
- https://git-scm.com/docs/gitignore