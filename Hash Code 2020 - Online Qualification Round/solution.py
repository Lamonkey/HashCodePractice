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
    #libraries = [number of books, signup process, ship rate]
    def calculateScore(self,numberOfLibrary,totalBooks,libraries,librarie_books,scores,scanningDay):
        selectedLib = 0
        tmp_scores = []
        #iterate every library
        for x in range(len(libraries)):
            #list of tmp score
            maxScore = 0
            #calcuate how many days a library needs to ship out all its books
            numOfShippingDays = libraries[x][0]/libraries[x][2]
            #calculate how many books it can ship
            booksShip = (scanningDay - libraries[x][1] - 1)*libraries[x][2]
            #rank book by its score 
            book_with_score = []
            tmp_score = scores.copy()
            for books in librarie_books[x]:
                for book in books:
                    book_with_score.append(tmp_score[book])
                    tmp_score[book] = 0
                sorted(book_with_score,reverse=True)
                #calculate score
                sumScore = sum(book_with_score[0:(booksShip-1)])
                tmp_scores.append(tmp_score.copy())
                #compare with maxscore
                if(sumScore > maxScore):
            #if is new maxscore, currLib = this library, books = select books
                    maxScore = sumScore
                    selectedLib = x

        #return selected library as an int and selected books as list and new socre as list, new scanning day
        return selectedLib, [],tmp_scores[selectedLib],scanningDay - libraries[selectedLib][1]

    #output which books shipped from which library adn the order of libraries signed up
    def findShippingOrder(self,fileName):  
        numberOfLibrary,totalBooks,libraries,librarie_books,scores,scanningDay = self.importFile(fileName)
        shippingPlan = []
        while scanningDay > 1:
            scores,scanningDay,selectedLibrary,selectBooks = self.calculateScore(numberOfLibrary,totalBooks,libraries,librarie_books,scores,scanningDay)
            shippingPlan.append([selectedLibrary,selectBooks])
        return shippingPlan
