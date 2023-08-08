#dictionaries allows us to store information in key value pairs
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "Decmber",

}



print(monthConversions["May"])
print(monthConversions.get("Mar", "Not a valid key"))