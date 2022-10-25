import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import MaxQueue
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList
import algorithms
import time
import copy



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()
        self.bestSeller = BinarySearchTree.BinarySearchTree()
        self.sortedTitleIndicesHeap = BinaryHeap.BinaryHeap()
        #self.shoppingCart = MaxQueue.MaxQueue()

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        #self.bookCatalog = ArrayList.ArrayList()
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                #print("BOOK INSERTED: ", line)
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
                self.bestSeller.add(rank, s)
                k = Book.Book(key, title, group, int(rank) * -1, similar)
                self.sortedTitleIndicesHeap.add(k)
            # The following line is used to calculate the total time
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")
            return self.bookCatalog

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByPrefix(self, s : str):
        # todo
        '''Add a method to BookStore called addBookByPrefix(prefix) that adds the book with the
            given title prefix to the shopping cart and returns True. If no title contains that prefix or if
            the prefix is an empty string, then the method must return False and add nothing to the cart.
            HINT: First search the binary search tree for the index corresponding to the title with the given
            prefix. If the index is not None, add the Book at the given index in the bookCatalogue to the
            cart.
        '''
        start_time = time.time()
        index = self.sortedTitleIndices.find(s)
        # print("S: ", index.v)
        if s != "" and s is not None:
            self.shoppingCart.add(self.bookCatalog.get(index.v))
            print(f"Added first matched title: {self.bookCatalog.get(index.v).title}")
            #elapsed_time = time.time() - start_time
            #print(f"addBookByPrefix Completed in {elapsed_time} seconds")
        else:
            print("Book was not found.")
        elapsed_time = time.time() - start_time
        print(f"addBookByPrefix Completed in {elapsed_time} seconds")

    def addBookByKey(self, s : str):
        # determine if key is inside ChainedHashTable
        # if inside ChainedHashTable then get the index
        # get the book for adding shopping cart
        # put book inside shopping cart
        # print the title
        #if not inside, print did not find
        s = self.bookIndices.find(s)
        #print(key)
        if s != None:
            start_time = time.time()
            self.shoppingCart.add(self.bookCatalog.get(s))
            print(f"Added title: {self.bookCatalog.get(s).title}")
            elapsed_time = time.time() - start_time
            print(f"addBookByKey Completed in {elapsed_time} seconds")
        else:
            start_time = time.time()
            elapsed_time = time.time() - start_time
            print("Book was not found.")
            print(f"addBookByKey Completed in {elapsed_time} seconds")

    def bestsellers_with(self, infix, structure, n=0):
        '''
        searches the book catalog for the first n books containing the given string infix,
        stores them in a data structure determined by structure, and prints them in order of
        highest ranking to lowest ranking
        '''
        print("structure:", structure)
        if infix is None or infix == "":
            print("Invalid Infix")
        else:
            if structure == 1:
                if n < 0:
                    print("Invalid number of Titles")
                else:
                    start_time = time.time()
                    # FIXME: Insert the rest of the implementation here
                    # book_tree = self.sortedTitleIndices.find(infix)
                    # print("BOOK TREE NODE: ", book_tree)
                    best_seller = None
                    # Reverse this in_order, iterate, set best_seller to the first occurance that contains the infix
                    books = self.bestSeller.in_order()
                    #print("Books:", books)
                    for i in range(len(books) - 1, -1, -1):
                        book = books[i]
                        #print(f"COMPARING: {infix} : {book.v.title} ------------------ {infix in book.v.title} ---- {book.v.rank}")
                        if infix in book.v.title:
                            print(f"Added title: {book.v}")
                    elapsed_time = time.time() - start_time
                    print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")
            elif structure == 2:
                if n < 0:
                    print("Invalid number of Titles")
                else:
                    start_time = time.time()
                    # FIXME: Insert the rest of the implementation here
                    books = self.sortedTitleIndicesHeap
                    while books.size() > 0:
                        book = books.remove()

                        #print(book)
                        if infix in book.title:
                            book.rank = book.rank*-1
                            print(f"Added title: {book}")

                    #print(f"Added title: {self.bookCatalog.get(books.find_min()).title}")
                    elapsed_time = time.time() - start_time
                    print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")
            else:
                print("Invalid Data Structure")

    def sort_catalog(self, s):
        #check which method is being chosen
        #just pass in book catalog to sort method
        start_time = time.time()
        if s == 1:
            algorithms.merge_sort(self.bookCatalog)
        elif s == 2:
            algorithms.quick_sort(self.bookCatalog, False)
        elif s == 3:
            algorithms.quick_sort(self.bookCatalog)
        elapsed_time = time.time() - start_time
        print(f"Sorted {self.bookCatalog.size()}  in {elapsed_time} seconds")

    def search_by_prefix(self, prefix, algo):
        #determine which algorithm was chosen
        #if binary search was chosen, make sure catalog is sorted first
        #search for prefix inside catalog
        #determine if it was found or not
        #if not remove from catalog so would not be found again
        #repeat until found or until max searches
        count = 0
        if algo == 1:
            start_time = time.time()
            copy_catalog = copy.deepcopy(self.bookCatalog)
            #lin_s = algorithms.linear_search(copy_catalog, Book.Book(0, prefix, "", 0, None))
            while True:
                lin_s = algorithms.linear_search(copy_catalog, Book.Book(None, prefix, None, 1, None))
                if lin_s > 0:
                    print(copy_catalog.get(lin_s))
                    copy_catalog.remove(lin_s)
                    count += 1
                else:
                    break
            elapsed_time = time.time() - start_time
            print(f"Found {count} books with given prefix in {elapsed_time} seconds")
        elif algo == 2:
            book_catalog = copy.deepcopy(self.bookCatalog)
            algorithms.quick_sort(book_catalog)
            start_time = time.time()
            bin_s = algorithms.binary_search(book_catalog, Book.Book(0, prefix, "", 0, None))
            #print(bin_s)
            while bin_s != -100:
                print(book_catalog.get(bin_s))
                book_catalog.remove(bin_s)
                bin_s = algorithms.binary_search(book_catalog, Book.Book(0, prefix, "", 0, None))
                count += 1
            elapsed_time = time.time() - start_time
            print(f"Found {count} books with given prefix in {elapsed_time} seconds")

    def display_catalog(self, n):
        #make sure to print no more than n books and make sure that n is no larger than catalog
        start_time = time.time()
        if n > len(self.bookCatalog): return ValueError
        count = 0
        for book in self.bookCatalog:
            if count == n:
                break
            else:
                print(book)
            count += 1
            print("count: ", count)
        elapsed_time = time.time() - start_time
        print(f"Displayed {n} books in {elapsed_time} seconds")

    def searchBookByInfix(self, infix : str):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        #only print a maximum of 50 books
            #find if infix in in book.title
            #print(book)
        # given a string search data base to see if there a matching title

        # if given the empty string, print the first 50 books
        '''
        for book in arrayList:
            book.title #this gives the string of the title
            if s in book.title:
                print(book)
        '''
        numBooks = 0
        for book in self.bookCatalog:
            if infix in book.title:
                numBooks += 1
                if numBooks == 50:
                    break
                else:
                    print(book)
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        #to do
        #self.shoppingCart = MaxQueue.MaxQueue()
        print(self.shoppingCart.max())
        return(self.shoppingCart.max())

