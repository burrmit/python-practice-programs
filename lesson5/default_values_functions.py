def prompt_user(prompt, num_tries = 2):
    """This function prompts the user a certain number of times"""
    answer = input(prompt)

    while (answer != "yes" and answer != "no" and num_tries > 1):
       num_tries = num_tries - 1
       print ("Try again")
       answer = input(prompt)


#prompt_user("Enter yes or no: ")
#prompt_user("Enter yes or no: ", 4)
prompt_user(prompt="Hello")
prompt_user(num_tries=1, prompt="Hi")
