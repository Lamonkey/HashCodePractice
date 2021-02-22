class solution:
    #edited read file and return the following variable
    def importFile(self,fileName):
        librarys = [] #store book in each librarys
        scores = [] #score of all book
        scanningDay = 0 #how many days for scanning
        signUpDays = [] #all librarys sign up day
        shipRates = [] #all librarys ship rate
    
    #output new scores, new scanningDay, selected library, selected books
    def calculateScore(self,librarys,scores,scanningDay,signUpDays,shipRates):
        curScore = 0
        maxScore = 0
        for(x in range(len(librarys)-1):
            curScore = librarys[x].score
            maxScore = curScore
            if(librarys[x].score > librarys[x+1].score):
                break
            else:
                maxScore = libarys[x+1].score
        return None

    #output which books shipped from which library adn the order of libraries signed up
    def findShippingOrder(self,fileName):  
        return None
