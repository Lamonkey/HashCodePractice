class solution:
#edited read file and return the following variable
    def importFile(self,fileName):
        numberOfLibrary = 0 #total number of library
        totalBooks = 0 #total number of books
        libraries = [] #propety of each library
        librarie_books = [] #store book in each librarys
        scores = [] #score of all book
        scanningDay = 0 #how many days for scanning
    
        
        with open(fileName) as reader:
            line_index = 0
            for line in reader:
                if (line != '\n'):
                    if(line_index == 0):
                        totalBooks,numberOfLibrary,scanningDay = line.split()
                    elif(line_index == 1):
                        scores = line.split()
                    elif(line_index%2 == 0):
                        numberOfbooks,signUpDay,shiprate = line.split()
                        libraries.append([numberOfbooks,signUpDay,shiprate])
                    else:
                        librarie_books.append(line.split())
                line_index = line_index + 1

        return numberOfLibrary,totalBooks,libraries,librarie_books,scores,scanningDay

    
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
        numberOfLibrary,totalBooks,libraries,librarie_books,scores,scanningDay = importFile(fileName)
        return None
