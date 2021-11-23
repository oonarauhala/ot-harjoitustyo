# GachaPet
GachaPet on hauska virtuaalilemmikkipeli, jossa pelaaja voi hankkia lemmikilleen tavaroita gacha-automaateista.


## Dokumentaatio
* [Vaatimusmäärittely](https://github.com/oonarauhala/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/oonarauhala/ot-harjoitustyo/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)

## Asennus
* Asenna riippuvuudet: poetry install
* Käynnistä sovellus: poetry run invoke start

## Testaus
* Aja testit: poetry run invoke test
* Luo testikattavuusraportti: poetry run invoke coverage-report
    * Visuaalisen raportin voi katsoa htmlcov/index.html -tiedostosta