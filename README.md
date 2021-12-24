# GachaPet
GachaPet on hauska virtuaalilemmikkipeli, jossa pelaaja voi hankkia lemmikilleen tavaroita gacha-automaateista.

## Releaset
[Release viikko 5](https://github.com/oonarauhala/ot-harjoitustyo/releases/tag/viikko5)  
[Release viikko 6](https://github.com/oonarauhala/ot-harjoitustyo/releases/tag/viikko6)
[Loppupalautus](https://github.com/oonarauhala/ot-harjoitustyo/releases/tag/loppupalautus)

## Dokumentaatio
* [Vaatimusmäärittely](https://github.com/oonarauhala/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/oonarauhala/ot-harjoitustyo/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)
* [Arkkitehtuuri](https://github.com/oonarauhala/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [Käyttöohje](https://github.com/oonarauhala/ot-harjoitustyo/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

## Asennus
* Asenna riippuvuudet: poetry install
* Käynnistä sovellus: poetry run invoke start

## Testaus
* Aja testit: poetry run invoke test
* Luo testikattavuusraportti: poetry run invoke coverage-report
    * Visuaalisen raportin voi katsoa htmlcov/index.html -tiedostosta
* Aja pylint -testi: poetry run pylint src