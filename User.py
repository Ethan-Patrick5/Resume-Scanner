import Scanner
#This class will be the main method that will prompt the users and recieve
#their data
class User:

    def __init__(fname, lname, resume):
        User.fname = fname
        User.lname = lname
        User.resume = resume
    # This method is to prompt the user to attach their resume
    def getpdf():
        application = True
        print("Welcome to the resume scanner!\n" +
        "The purpose of this scanner is to analyze your skills\n" +
        "and return job postings that match your skills.")
        while application == True:
            answer = input("If you would like to use the scanner please enter yes\n" +
            "If you would like to quit the program please enter no:")
            if answer[0] == "y" or answer[0] == "Y":
                User.fname = input("Please enter your first name:")
                User.lname = input("Please enter last name:")
                User.resume = input("Please enter the link to your resume: ")
            elif answer[0] == "n" or answer[0] == "N":
                print("Thank you for using my program!")
                application = False
            else:
                answer = input("Please enter yes or no.")

if __name__ == "__main__":
    User.getpdf()
            