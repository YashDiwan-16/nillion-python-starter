from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    
    rating1 = SecretInteger(Input(name="Rating1", party=party1))
    rating2 = SecretInteger(Input(name="Rating2", party=party2))
    rating3 = SecretInteger(Input(name="Rating3", party=party3))
    rating4 = SecretInteger(Input(name="Rating4", party=party4))

    total_ratings = rating1 + rating2 + rating3 + rating4
    average_rating = total_ratings / Integer(4)

    return [Output(average_rating, "AverageRating", party1)]

nada_main()
