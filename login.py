from time import sleep


id = "admin"
mdp = "admin"
error = 0

enter_id = input("\nEntrez un votre identifiant: \n")
enter_mdp = input("\nEntrez un votre mot de passe: \n")

   
if enter_id != id or enter_mdp != mdp :
    print("\nVotre identifiant ou votre mot de passe est incorrect\n")
    error = 1
    print("BYE\n") 
    sleep(2)


else :
    print("\nWelcome "+ str(id) +"\n")

        
        


