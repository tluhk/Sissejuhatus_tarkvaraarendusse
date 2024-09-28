# Ülesanne testida eslinti

ESLint on populaarne staatilise koodianalüüsi tööriist JavaScripti jaoks. See aitab arendajatel tuvastada ja parandada probleeme oma koodis, järgides eelnevalt määratletud koodistiile ja parimaid praktikaid. ESLint võimaldab:

1. Tuvastada süntaksivigu
2. Leida potentsiaalseid probleeme (nt kasutamata muutujad)
3. Jõustada koodistiili reegleid (nt taanded, tühikud)
4. Parandada koodibaasi ühtlust mitme arendaja vahel
5. Tõsta koodi kvaliteeti ja hooldatavust

ESLint on konfigureeritav, mis tähendab, et meeskonnad saavad kohandada reegleid vastavalt oma vajadustele ja eelistustele. See integreeritakse sageli arenduskeskkondadesse ja pideva integratsiooni (CI) protsessidesse, et tagada kõrge koodi kvaliteet kogu arendusprotsessi vältel.

## Ülesanne
1. Luua uus projektikaust
2. Loo node projekt `npm init -y`
3. Installi ESLint `npm install eslint` või globaalselt `npm install -g eslint`
4. Insatlli VSCode extensioni ESLint
5. Installi Error Lens plugin (see pole nõutav, kuid see näitab vigu koodis)
6. Loo ESLinti configuratsioon `npx eslint --init` võid kasutada vaikimis valikuid, kuid mitte Reacti ja Vued hetkel.

(7. Vajadusel äivita ESLint koodi kontrollimiseks `npx eslint .`)

## Näide
```javascript
// Example 1: Unused variables and inconsistent spacing
var unusedVar = 5;
let x=10;

// Example 2: Missing semicolons and using single quotes inconsistently
const greeting = "Hello"
const name = 'World'
console.log(greeting + ' ' + name)

// Example 3: Using var instead of let/const
for (var i = 0; i < 5; i++) {
  console.log(i);
}
console.log(i);  // i is accessible outside the loop

// Example 4: Inconsistent indentation
function badlyIndentedFunction() {
    const a = 1;
  const b = 2;
      return a + b;
}

// Example 5: Unused function parameters and function declarations after return
function unusedParam(a, b) {
    return a;
}

function earlyReturn() {
    return;
    console.log("This will never be reached");
}

// Example 6: Comparison with type coercion
if (5 == "5") {
    console.log("This is true with ==, but not with ===");
}


// Example 7: Multiple empty lines
function someFunction() {
    const a = 1;


    const b = 2;


    return a + b;
}



// Example 8: Line too long (depending on max-len rule)
const veryLongLine = "This is a very long line that exceeds the typical maximum line length that is often set in ESLint configurations";

// Example 9: Declaring variables that shadow outer scope variables
let count = 1;
if (true) {
    let count = 2;
    console.log(count);
}

// Example 10: Using console.log (if no-console rule is enabled)
console.log("This might be flagged depending on ESLint configuration");
```

These examples include various issues that ESLint commonly checks for:
1. Unused variables
2. Inconsistent spacing and indentation
3. Missing semicolons
4. Mixing quote styles
5. Using var instead of let/const
6. Unused function parameters
7. Unreachable code
8. Loose equality comparisons
9. Multiple empty lines
10. Overly long lines
11. Shadowing variables
12. Use of console.log (which might be disallowed in production code)
When you run ESLint on this file, it should flag these issues, helping beginners understand common pitfalls and best practices in JavaScript coding. The exact warnings and errors will depend on your specific ESLint configuration.