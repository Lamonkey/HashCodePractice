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
                        libraries.append([int(numberOfbooks),int(signUpDay),int(shiprate)])
                    else:
                        tmp = [int(x) for x in line.split()]
                        librarie_books.append(tmp)
                line_index = line_index + 1
        scores_int = [int(x) for x in scores]
        return numberOfLibrary,int(totalBooks),libraries,librarie_books,scores_int,int(scanningDay)

    
    #output new scores, new scanningDay, selected library, selected books
    #libraries = [number of books, signup process, ship rate]
    def calculateScore(self,numberOfLibrary,totalBooks,libraries,librarie_books,scores,scanningDay):
        selectedLib = 0
        tmp_scores = []
        maxScore = 0
        #iterate every library
        for x in range(len(libraries)):
            #list of tmp score
            #calculate how many books it can ship
            booksShip = (scanningDay - libraries[x][1] - 1)*libraries[x][2]
            #rank book by its score 
            if(booksShip > 0):
                book_with_score = []
                tmp_score = scores.copy()
                for book in librarie_books[x]:
                    book_with_score.append(tmp_score[book])
                    tmp_score[book] = 0
                book_with_score = sorted(book_with_score,reverse=True)
                #calculate score
                if(booksShip >= len(book_with_score)):
                    sumScore = sum(book_with_score)
                else:
                    sumScore = sum(book_with_score[0:(booksShip)])
                tmp_scores.append(tmp_score.copy())
                #compare with maxscore
                if(sumScore > maxScore):
                #if is new maxscore, currLib = this library, books = select books
                    maxScore = sumScore
                    selectedLib = x
            else:
                tmp_scores.append(scores.copy())
                sumScore = 0
        if (maxScore == 0):
            scanningDay = 0
        else:
            scanningDay = scanningDay-libraries[selectedLib][1]
        #return selected library as an int and selected books as list and new socre as list, new scanning day
        return selectedLib, [maxScore],tmp_scores[selectedLib],scanningDay

    #output which books shipped from which library adn the order of libraries signed up
    def findShippingOrder(self,fileName):  
        numberOfLibrary,totalBooks,libraries,librarie_books,scores,scanningDay = self.importFile(fileName)
        shippingPlan = []
        while scanningDay > 1:
            selectedLibrary,selectBooks,scores,scanningDay = self.calculateScore(numberOfLibrary,totalBooks,libraries,librarie_books,scores,scanningDay)
            if(len(selectBooks)>0):
                shippingPlan.append([selectedLibrary,selectBooks])
        return shippingPlan

driver = solution()
print(driver.findShippingOrder("b_read_on.txt"))