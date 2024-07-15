from nada_dsl import *

def nada_main():
    # Define the parties involved
    voter1 = Party(name="Voter1")
    voter2 = Party(name="Voter2")
    tally_party = Party(name="TallyParty")

    
    vote1 = SecretInteger(Input(name="vote1", party=voter1))
    vote2 = SecretInteger(Input(name="vote2", party=voter2))

    
    mask1 = SecretInteger(Input(name="mask1", party=voter1))
    mask2 = SecretInteger(Input(name="mask2", party=voter2))

    masked_vote1 = vote1 + mask1
    masked_vote2 = vote2 + mask2

    
    tally_masked_votes = masked_vote1 + masked_vote2

    sum_masks = mask1 + mask2
    final_tally = tally_masked_votes - sum_masks

    return [Output(final_tally, "final_tally", tally_party)]


nada_main()
