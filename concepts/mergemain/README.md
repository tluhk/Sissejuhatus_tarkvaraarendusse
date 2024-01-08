# main haru 'merge' oma harusse

Enne kodutöö esitamist, peab oma kodutööde harusse tegema `merge`, et vahepeal lisatud automaattestid saaksid ka Sinu kodutööde harusse lisatud.

Selleks tuleb `Github Desktop` rakenduses valida `Current branch` nupu alt (veendu, et linnuke oleks Sinu nimega haru ees) all servas olev nupp `Choose a branch to merge into Sinu_Nimega_Haru`.

![Merge 1](../../docs/kodusedtood/files/merge_1.png)

Seejärel vali `main` haru ja vajuta nuppu `Create a merge commit`.

![Merge 2](../../docs/kodusedtood/files/merge_2.png)

Seejärel võid juba oma harus tehtud muudatused Github-i `push`-ida.

Diagrammi peal näeb protsess välja selline:

```mermaid
gitGraph
    commit id: "RIF kodutööd"
    commit id: "Add README.md"
    branch Eesnimi_Perekonnanimi
    commit id: "Kaustade struktuur"
    checkout main
    commit id: "Esimese kodutöö testid"
    checkout Eesnimi_Perekonnanimi
    merge main
    commit id: "Esimene kodutöö"
    checkout main
    commit id: "Teise kodutöö testid"
    checkout Eesnimi_Perekonnanimi
    merge main
    commit id: "Teine kodutöö"
```