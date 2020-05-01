'''
writing to a file. two methods: write and append, write erase and write, append append...
'''

text = "Sample text to save\nNew line!"
#teksten vi vil skrive i filen.
save_file = open("example_file for e17.txt", "w")
#åpner og lager filen vi vil bruke. Og legger inn om det er write append eller read.
save_file.write(text) 
save_file.close()
#legge inn hva som skal inne (text) og huske å lukke filen. 

'''
Under her lager vi en ny fil og skriver til denne, etter det bytter vi ut write
med append. Vi kan da legge til ny tekst uten å slette det som er der fra før. Det
skjer hvis man bruker write
'''

text2 = "Sample text to save\nNew line!"

save_file = open("example_file for e18.txt", "w")

save_file.write(text2) 
save_file.close()

text3 = "\nText to add!"

save_file = open("example_file for e18.txt", "a")
# ,(a) er altså append.
save_file.write(text3) 
save_file.close()