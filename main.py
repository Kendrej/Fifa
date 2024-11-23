from database import Database
from models.cards import Cards


def main():
    database = Database("test.db")
    
    user_id = int(1)
    imie = "Cristiano"
    nazwisko = "Ronaldo"
    kraj = "Portugal"
    Liga = "LALIGA EA SPORTS"
    klub = "Real Madrid"
    playstyle = "Rapid"
    isPlus = True #czy playstyle jest plus(1) czy nie (0)

    if database.check_if_id_card_exists(user_id) :
        #database.addPlayersPrice()
        print("Id karty jest juz w bazie danych")
    else:
        database.addCard(user_id,imie,nazwisko)

        database.addStatistics(user_id,87,76,88,76,67,33,73)

        database.addOtherStatistics(user_id,57,168,3,4,"right","Mostly Explosive","Short & Normal")

        if not database.check_if_nationality_exists(kraj):
            database.addNationality(kraj)
            print("dodana narodowosc")
        database.connectNationalityIDWithCardID(database.getNationalityID(kraj),user_id)

        if not database.check_if_id_league_exists(Liga):
            database.addLeague(Liga)
            print("dodana liga")

        if not database.check_if_club_exists(klub):
            database.addClub(klub)
            print("Dodany klub")
            database.connectLeagueIDWithClubID(database.getLeagueID(Liga),database.getClubID(klub))
        database.connectClubIDWithCardID(database.getClubID(klub),user_id)

        if not database.check_if_id_playstyle_exists(playstyle):
            database.addPlaystyle(playstyle)
            print("Playstyle Dodany")
        database.assign_playstyle_to_Card(database.getPlaystyleId(playstyle),user_id,isPlus)


        print("Zawodnik dodany")
        
    database.close()

    print("Database updated.")

main()
