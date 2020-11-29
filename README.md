# torihinnat
* Aineopintojen harjoitustyö: Tietokantasovellus (periodi II)
* Sovellus löytyy:https://torihinnat.herokuapp.com/
* Valmiit admin -oikeudet on käyttäjällä: "testaaja1", jonka salasana on "salasana"

Tarkoitus on luoda sovellus jossa:
* Käyttäjät voivat selata ja  lisätä perinteisten torituotteiden (marjat, sienet, vihannekset) myyntipaikkoja ja hintatietoja. 
* Käyttäjä voi lisätä uuden myyntipaikan tai antaa olemassa olevalle myyntipaikalle hintatiedon (valita tuote ja hinta)
* Ylläpitäjä voi lisätä/poistaa näitä tietoja, sekä lisätä mistä tuotteista on mahdollista lisätä hintatietoja.
* Myyntipaikkoja ja hintojatietoja voi hakea kaupungeittain ja ehkä nähdä jopa kartalla.

Tällä hetkellä 29.11.2020:
* Lisätyt myyntipaikat ja hintatiedot näkyvät etusivulla kirjautumattakin
* Kirjautuminen ja uuden käyttäjän rekisteröinti toimii
* Admin oikeudet toimii, näitä voi testata käyttäjätunnuksella "testaaja1", jonka salasana on "salasana"
* Uuden myyntipaikan ja hintatiedon lisääminen toimivat kirjautuneille käyttäjille
* Admin näkymässä voi lisäksi luoda/poistaa tuotteita, poistaa hintatietoja ja poistaa myyntipaikkoja
* Sivustolle on luotu ulkoasu.
* Edellisestä kerrasta on lisäksi korjattu lomakkeiden virhekäsittelyä ja mitä syötettä ne ottavat vastaan
* PGR mallia pyritty noudattamaan lomakkeiden käsittelyssä (paitsi admin, haetaan useita lomakkeita samalla sivulla)

Vielä puuttuu 29.11.2020: 
* Kaupungeittain tehtävät hintatieto/myyntipaikka rajaukset
* Mahdollinen kartta
* Näytettävien hintatietojen määrän rajaus etusivulla
* Taulukoissa näkyvien päivämäärien ja hintatietojen stilisointi
* Ulkoasun hionta ja mahdolliset bugikorjaukset palautteen mukaan
