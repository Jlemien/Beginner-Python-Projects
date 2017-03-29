import webbrowser
import requests
from bs4 import BeautifulSoup
from GoodreadsBooks import ListOfBooksTest
from GoodreadsBooks import ISBN_List1

ItemsToBeSearched = ListOfBooksTest

def AudioBookFinder(listofbooks):
    for item in listofbooks:
        exampleURL = "http://audiobookbay.me/?s=" + item
        r = requests.get(exampleURL)
        soup = BeautifulSoup(r.content, "lxml")
        prettysoup = soup.prettify()
        negative_test_phrase = "try again with another query or use our navigation"
        positive_test_phrase = "<div class=\"postTitle\"><h2><a href="
        if negative_test_phrase in prettysoup:
            print("No ", item, "here.")
        elif positive_test_phrase not in prettysoup:
            print("They have", item, "available for download!")
            webbrowser.open_new_tab(exampleURL + item)
    print("This is end of the AudioBookFinder function.")

def SearchTaoBaoforBooks(inputlist):
    TaobaoBaseURLpart1 = "https://s.taobao.com/search?q="
    TaobaoBaseURLpart2 = "&cps=yes&cat=33"
    for bookname in inputlist:
        webbrowser.open_new_tab(TaobaoBaseURLpart1 + bookname + TaobaoBaseURLpart2)
    print("This is end of the SearchTaoBaoforBooks function.")

def SearchBookFinder4U(inputlist):
    ISBNFinderBaseURL = "http://www.bookfinder4u.com/compare.aspx?isbn="
    for ISBN in inputlist:
        webbrowser.open_new_tab(ISBNFinderBaseURL + ISBN)
    print("This is end of the ISBNFinder function.")

# def ExportBestPricetoSpreadsheet(inputlist):
#     r = requests.get(baseURL + ISBN)
#     soup = BeautifulSoup(r.content, "lxml")
#     prettysoup = soup.prettify()
#     #I need to figure out a pay to print the "Best Price" amount from that page

def ActuallyFindABook():
    TargetBook = str(input("Type the book you want to find: "))
    WhichSearch = input("Do you want to search AudioBookBay, TaoBao, or BookFinder4U? Please type 1, 2, or 3: ")
    if WhichSearch == "1":
        exampleURL = "http://audiobookbay.me/?s=" + TargetBook
        r = requests.get(exampleURL)
        soup = BeautifulSoup(r.content, "lxml")
        prettysoup = soup.prettify()
        negative_test_phrase = "try again with another query or use our navigation"
        positive_test_phrase = "<div class=\"postTitle\"><h2><a href="
        if negative_test_phrase in prettysoup:
            print("No ", TargetBook, "here.")
        elif positive_test_phrase not in prettysoup:
            print("They have", TargetBook, "available for download!")
            webbrowser.open_new_tab(exampleURL + TargetBook)
    print("This is end of the AudioBookFinder function.")
    if WhichSearch == "2":
        TaobaoBaseURLpart1 = "https://s.taobao.com/search?q="
        TaobaoBaseURLpart2 = "&cps=yes&cat=33"
        webbrowser.open_new_tab(TaobaoBaseURLpart1 + TargetBook + TaobaoBaseURLpart2)
        print("This is end of the SearchTaoBaoforBooks function.")
    if WhichSearch == "3":
        BookFinder4UURL1, BookFinder4UURL2 = "http://www.bookfinder4u.com/search_title/", ".html"
        webbrowser.open_new_tab(BookFinder4UURL1 + TargetBook + BookFinder4UURL2)
        print("This is end of the BookFinder4U function.")


SearchBookFinder4U(ISBN_List1)