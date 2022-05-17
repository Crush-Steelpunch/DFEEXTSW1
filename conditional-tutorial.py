# Set up some vars
devs_money = 100
dev_can_play_smash = False

# Conditional Statement to test vars

#     number test            bool test
#        True                   False       = False
if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament!")

# Second Test
#       False                   False       = False
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")

# else Statement
# True

else:
    print("Dev just can't play smash")

print("Done")