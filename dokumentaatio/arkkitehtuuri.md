# Sovelluksen arkkitehtuuri

## Yleiskuva
Ohjelma koostuu pakkauksista ui, repositories ja entities. luokan App sovelluslogiikka käyttää pakkauksien tarjoamia palveluita ja luokkia.
![Arkkitehtuuri](/dokumentaatio/kuvat/uml-2.png)  


## Käyttöliittymä
Käyttöliittymäpalvelut löytyvät ui-paketista. Suuren osan käyttöliittymätoiminnoista on ulkoistettu DisplayManager -luokalle.
Sovellukseen kuuluu useita sivuja, joista tärkeimmät ovat kirjautuminen, pelin pääsivu ja gacha-sivu.
Sivujen vaihtelu tehdään ohjelman pääloopissa, joka kutsuu DisplayManagerin sopivaa metodia vaihtaekseen sivua.

## Tietojen tallenus
Sovellus käyttää Firebase -tietokantaa (noSQL) verkossa. Käyttäjän rekisteröityessä, sisäänkirjautuessa sekä uloskirjautuessa tiedot haetaan ja tarvittaessa tallennetaan tietokantaan. Tieto on json-muotoista. Sovellus käyttää toetokantaoperaatioihin python-firebase -kirjastoa.

## Päätoiminnallisuudet
### Uuden käyttäjän rekisteröinti
Käyttäjä voi rekisteröityä rekisteröintisivulla syöttämällä uniikin käyttäjänimen ja salasanan. Salasana täytyy syöttää kaksi kertaa, jotta kirjoitusvirheiltä vältyttäisiin.
UserRepository tarkistaa, että käyttäjänimeä ei vielä löydy tietokannasta.
![Rekisteröityminen](/dokumentaatio/kuvat/sekvenssi2.png)

### Lemmikin ruokinta
Käyttäjä voi ruokkia lemmikkiään klikkaamalla sitä.  

![Lemmikin ruokinta](/dokumentaatio/kuvat/sekvenssi1.png)