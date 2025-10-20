def getpdf():
    application = True
    print("Welcome to the resume scanner!\n " +
          "The purpose of this scanner is to analyze your skills\n " +
          "and return job postings that match your skills.")
    while application == True:
        answer = input("If you would like to use the scanner please enter yes\n " +
              "If you would like to quit the program please enter no.")
        if answer[0] == "y" or answer[0] == "Y":
            resume = input("Please enter the link to your resume: ")
        elif answer[0] == "n" or answer[0] == "N":
            print("Thank you for using my program!")
            application = False
        else:
            answer = input("Please enter yes or no.")

if __name__ == "__main__":
    getpdf()
            