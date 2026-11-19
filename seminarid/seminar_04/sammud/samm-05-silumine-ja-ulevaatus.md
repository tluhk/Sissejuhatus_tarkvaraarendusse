# Seminar 4, samm 5: Vea silumine ja koodi ülevaatus

Seminaris on 5 minutit: mis toimub arendamise etapis, mis on viga, mis on silumine (*debugging*) ja mis on koodi ülevaatus (*code review*). Harjutus tehakse kodutöös iseseisvalt, sest koodinäiteid me veel arutanud ega näidanud ei ole.

**Iseseisev harjutus** (eraldi fail, millele kodutöö viitab):

1. Õppija saab lühikese Pythoni funktsiooni, mis arvutab keskmise ja milles on viga:

   ```python
   def average(values):
       return sum(values) / (len(values) - 1)
   ```

2. Ta ennustab tulemuse sisendiga `[2, 4, 6]`, ilma koodi käivitamata. Oodatud tulemus on `4`, tegelik `6`.
3. Ta kirjutab vea kirjelduse: sisend, oodatud tulemus, tegelik tulemus ja oletatav põhjus.
4. Ta saab parandatud versiooni ja vaatab selle üle nagu PR-i. Ülevaatuse kommentaar on üks konkreetne küsimus, näiteks „Mis juhtub tühja loendiga?”.
5. Koodi käivitamine on valikuline: `python3` käsk terminalis.

Vastus kirjutatakse oma Issue'sse. Koodi kirjutama ei pea.
