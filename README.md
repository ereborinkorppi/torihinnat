# torihinnat
* Aineopintojen harjoitustyö: Tietokantasovellus (periodi II)
* Sovellus löytyy:https://torihinnat.herokuapp.com/
* Valmiit admin -oikeudet on käyttäjällä: "testaaja1", jonka salasana on "salasana"

Sovelluksen perusajatus:
* Kaikki (kirjautumattakin) voivat selata perinteisten torituotteiden (marjat, sienet, vihannekset) hintatietoja ja myyntipaikkoja. 
* Hintojatietoja voi hakea rajatusti kaupungeittain
* Sisäänkirjautunut käyttäjä voi lisätä uuden myyntipaikan tai antaa olemassa olevalle myyntipaikalle hintatiedon (valita ennalta määrätyistä tuotteista tuotteen ja syöttää päivän hintatiedon)
* Ylläpitäjä voi lisätä/poistaa kaikkia näitä sovellukseen syötettyjä tietoja omassa admin -näkymässä, sekä lisäksi ylläpitäjä voi lisätä mistä tuotteista on mahdollista syöttää hintatietoja.

Sovelluksen tilanne 13.12.2020:
* Lisätyt myyntipaikat ja hintatiedot näkyvät etusivulla kirjautumattakin
* Kirjautuminen ja uuden käyttäjän rekisteröinti toimii toivotulla tavalla
* Admin oikeudet toimivat vain admineille, näitä voi testata käyttäjätunnuksella "testaaja1", jonka salasana on "salasana"
* Uuden myyntipaikan ja hintatiedon lisääminen toimivat kirjautuneille käyttäjille
* Admin näkymässä voi lisäksi luoda/poistaa tuotteita, poistaa hintatietoja ja poistaa myyntipaikkoja
* Sivustolle on luotu hieno ulkoasu.
* PGR mallia pyritty noudattamaan lomakkeiden käsittelyssä (paitsi admin, haetaan useita lomakkeita samalla sivulla)
* Lomakkeiden virhekäsittely toimii
* Etusivulla hintatiedot rajattu 10 tuoreimpaan hintaan ja kaikki hinnat sivulla näkyy sitten kaikki muutkin

Puutteet (eihän tämä kuitenkaan täydellinen ole): 
* Kaupungeittain tehtävät myyntipaikkarajaukset
* Kartta olisi kiva
* Taulukoissa näkyvien päivämäärien ja hintatietojen stilisointi suomalaiseen formaattiin
* Admin näkymän käytettävyys heikkenee huomattavasti jos sovellukseen kantaan tulee runsaasti rivejä
* Harkkatyöksi tässä ajassa kuitenkin ihan mukiinmenevä suorityös, eikö?
