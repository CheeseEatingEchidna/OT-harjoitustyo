#Vaatimusmäärittely

###Sovelluksen tarkoitus

Sovellus mahdollistaa teksti tiedostojen muokkaamisen androidilla. Sovellus backuppaa näitä tiedostoja (gittiä käyttäen) napin painalluksesta/automaattisesti. Tiedostot jota sovellus manipuloi tulee toimia hyvin myös vimissä, jotta näitä tiedostoja on mahdollista manipuloida muilla laitteilla vimiä käyttäen.

###Käyttöliittymä

Käyttöliittymä koostuu pelkistetystä kirjoitus alustasta (eli miltein tyhjästä ruudusta), Kansio näkymästä jossa näkyy sovelluksen käytössä olevat kansiot ja niiden sisältö (ikään kuin windowsin file browserin vasemmassa laidassa). Sovelluksella on myös alustus ikkuna johon täytetään tiedot siitä missä kansiossa haluat aloittaa/jatkaa, miten siihen saadaan yhteys (esim miten palvelimeen otetaan yhteyttä) ja vielä login ruutu josta pääsee kirjautumaan ns työtilaan.

##Perusversion tarjoama toiminnallisuus

##Ennen kirjautumista
- Käyttäjä voi alustaa ohjelman haluamaansa kansioon
- Ohjelma sitoo kansioon käyttäjä tunnuksen ja salasanan jota ilman käyttäjä ei pääse sisältöön sovelluksen kautta käsiksi

##Kirjautumisen jälkeen

- Käyttäjä näkee listan kansioista sisältöineen
- Valitsemalla teksitiedoston, käyttäjä siiretään tekstin kääntäjään
- Näiden näkymien välillä liikkuminen on helppoa

## Jatkokehitysideoita

Tämän sovelluksen olisi tarkoitus olla jonkin lainen alpha tekstinkäsittely ohjelmasta joka toimisi ikään kuin jonkin asteinen Onenote tai Evernote. Mutta käsittelemällä vain yksinkertaisia tekstitiedostoja joita on helppo siirrellä ohjelmalta ja käyttöjärjestelmästä toiselle. On erittäin tärkeää että nämä tiedostot näyttävät ja toimivat hyvin Vimissä sillä tulen näitä tiedostoja tietokoneella käsittelemään Vimin kautta.

- Pidemmän päälle olisi kiva piillottaa softan taakse joku linuxin user/pw manageri ja pitää tiedostoja enkryptoidussa tiedostossa.
