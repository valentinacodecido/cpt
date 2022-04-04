
LandmarksVisited = []

x = 0

def EndProcedure(LandmarksVisited):
    ending = input ("See list of landmarks (a) or continue (b): ")
    if ending == "a":
        print ("\nYou learned about " + str(x) + " landmarks today in this order:\n ")
        print (LandmarksVisited)
        print ("\n ")
        LandmarksVisited = []

    if ending == "b":
        print ("Thank you, goodbye!")
        LandmarksVisited = []
# procedure to either show list, end, or continue depending on # of values in list 

print ("Welcome!")

while len(LandmarksVisited) < 3:
    choice = input ("Eiffel Tower(a) or Great Wall (b): ")
    if choice == "a":
        LandmarksVisited.append("Eiffel Tower")
        x = 1
        wall = input ("The Eiffel Tower was built to be one the main attractions at the Paris World's Fair in 1889. It was created by architects Stephen Sauvestre, Emile Nougier, and Maurice Koechlin. Would you like to learn about the Great Wall of China? ")
        
        if wall == "yes":
            LandmarksVisited.append("Great Wall of China")
            x = x + 1
            stat = input("The Great Wall of China was built by China's emperors to protect their territory. It took more than 400 years to complete and is about 13,000 miles long. Would you like to learn about the Statue of Liberty? ")
            
            if stat == "yes":
                LandmarksVisited.append("Statue of Liberty")
                x = x + 1
                finalinfo = input ("The Statue of Liberty was built in 1886 by a French intellectual and anti-slavery activist Edourard de Laboulaye. It was built to honor the United States' independence and friendship with France. Press space and enter to end: ")
                EndProcedure(LandmarksVisited)    
                   
            if stat == "no":
                finalinfo = input ("Space and enter to end: ")
                EndProcedure(LandmarksVisited)

            
        if wall == "no":
            piza = input ("The Eiffel Tower is 1,063 feet tall and weighs about 7,300 tons. Would you like to learn about the Leaning Tower of Pisa? ")
            
            if piza == "yes":
                LandmarksVisited.append("Leaning Tower of Pisa")
                finalinfo = input ("The Leaning Tower of Pisa is a structure in Pisa, Italy, that is famous for its foundations, which caused it to lean about 15 feet. Space and enter to end: ")
                EndProcedure(LandmarksVisited)
            if piza == "no":
                finalinfo = input ("Space and enter to end: ")
                EndProcedure(LandmarksVisited)
                
    
    if choice == "b":
        LandmarksVisited.append("Great Wall of China")
        x = 1
        eiffel = input ("The Great Wall of China was built by China's emperors to protect their territory. It took more than 400 years to complete and is about 13,000 miles long. Would you like to learn about the Eiffel Tower? ")
        
        if eiffel == "yes":
            LandmarksVisited.append("Eiffel Tower")
            x = x + 1
            stat = input ("The Eiffel Tower was built to be one the main attractions at the Paris World's Fair in 1889. It was created by architects Stephen Sauvestre, Emile Nougier, and Maurice Koechlin. Would you like to learn about the Statue of Liberty? ")
            
            if stat == "yes":
                LandmarksVisited.append("Statue of Liberty")
                x = x + 1
                finalinfo = input ("The Statue of Liberty was built in 1886 by a French intellectual and anti-slavery activist Edourard de Laboulaye. It was built to honor the United States' independence and friendship with France. Space and enter to end: ")
                EndProcedure(LandmarksVisited)
                
            if stat == "no":
                finalinfo = input ("Space and enter to end: ")
                EndProcedure(LandmarksVisited)
                      
        if eiffel == "no":
            piza = input ("The Great Wall of China is the longest manmade structure in the world, and is over 2,300 years old. Would you like to learn about the Leaning Tower of Pisa? ")
            
            if piza == "yes":
                LandmarksVisited.append("Leaning Tower of Piza")
                x = x + 1
                finalinfo = input ("The Leaning Tower of Pisa is a structure in Pisa, Italy, that is famous for its foundations, which caused it to lean about 15 feet. Space and enter to end: ")
                EndProcedure(LandmarksVisited)
            if piza == "no":
                finalinfo = input ("Space and enter to end: ")
                EndProcedure(LandmarksVisited)
                 


       





## EndProcedure(LandmarksVisited)


