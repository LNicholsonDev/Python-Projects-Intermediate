# Program to help user manage contacts information
# Supports
#   listing all contacts,
#   viewing/adding/deleting a contact,
#   printing a given field for all contacts.
# Program uses dictionary of dictionaries to hold the contacts information.
def main():

    contacts = {
        "Joel":
            {"address": "1500 Anystreet, San Francisco, 94110", "company":"A startup",
             "mobile": "555-555-1111"},
        "Anne":
            {"address": "1000 Somestreet, Fresno, CA 93704",
             "state": "California",
             "landline": "125-555-2222", "company": "Some Great Company"},
        "Sally":
            {"state": "Illinois", "landline":"217-555-1222", "company": "Illinois Technologies",
             "mobile": "217-333-2353"},
        "Ben":
            {"address": "1400 Another Street, Fresno CA 93704",
             "state": "California", "mobile": "125-555-4444"}             
    }

    print("Welcome to contacts manager program")

    print("Good bye")

if (__name__ == "__main__"):
    main()
    
