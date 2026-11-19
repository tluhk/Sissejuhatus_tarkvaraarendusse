# Seminar 4, samm 7: Backlog tootest

Iga tiim loob seminaris 2–3 Issue'd oma lugudest või riskidest, mitte kodutöö sammudest. Näiteks: „Kontrolli kalendriekspordi välju”. Ajahinnang pannakse Issue'i loomisel, tegelik aeg sulgemisel. Projectsi väljad on Estimate ja „Tegelik (h)” (lisati sammus 1). Siin selgitame WIP-piirangu ja hinnangu kalibreerimise praktilise näitega.

## Blokeerijad

**Mis see on:** blokeerija (*blocker*) on takistus, mille tõttu Issue'iga ei saa edasi minna, kuigi tegija tahaks. Tavaliselt ootab töö kellegi teise tegevust, vastust või infot. Näiteks: „Riskikaarti ei saa lõpetada, sest me ei tea veel, kas tunniplaani andmed on kalendriekspordis olemas.”

**Miks see on tähtis:** blokeeritud kaart näeb tahvlil välja nagu tavaline pooleliolev töö. Kui blokeerijat ei märgita, ei tea keegi peale tegija, et töö seisab. Projektijuht ei saa aidata ja tähtaeg tuleb üllatusena. Blokeeritud kaart võtab ka WIP-piirangust ühe koha. See on õige, sest nii on tiimil põhjus takistus kõrvaldada, mitte võtta lihtsalt uus töö.

**Kuidas märkida:**

1. Kaart jääb olekusse In progress. Eraldi veergu ei tehta, sest tahvli olekud on kogu kursuse jooksul samad.
2. Issue saab sildi `blocked`.
3. Issue'sse kirjutatakse kommentaar kolme küsimusega: mida ootame, kellelt ootame ja millal kontrollime uuesti.
4. Kui blokeerija on teine Issue, märgitakse see ka seosena. Issue'i külgribal on osa „Relationships” ja valik „Mark as blocked by”. *Õpetajale: kontrolli enne seminari GitHubi praegust kasutajaliidest.*
5. Kui takistus kaob, eemaldatakse silt ja kommentaari kirjutatakse, mis selle lahendas.

**Seminaris:** iga tiim vaatab üle sammus 6 leitud andmeallika riski. Kui mõni loodud Issue ootab infot väljastpoolt tiimi, märgib tiim selle blokeerijaks. Projektijuht vaatab kodutöö ajal sildiga `blocked` kaarte vähemalt korra päevas.

**Mõiste testiks:** blokeerija ehk *blocker*.
