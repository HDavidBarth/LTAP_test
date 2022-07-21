# Henry Barth
# Start Date: 7.17.2022
# Project: Split Date

def splitDate(date):
    """the first parameter is a string with a date and then a time separated by a space
    eg: MM/DD/YYYY 12:00:00
    it will return a string like: MM/DD/YYYY
    """
    return date.split(" ")[0]  #the split method returns a list object, and we only want to access the first element
