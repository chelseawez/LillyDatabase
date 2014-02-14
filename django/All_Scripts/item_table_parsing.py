import csv
with open('Lilly DVD Assets.csv', 'rb') as f:
    reader = csv.DictReader(f)
    
    delim = '|'
    for row in reader:
        processStatus = row["Process Status Desc"]
        material = row["Material Type Desc"]
        itemID = row["Barcode"]
        if ((itemID[:1] == "D") and (processStatus != "Withdrawn" and processStatus != "Suppressed" and processStatus != "Canceled") and (material == "Video Cassette" or material == "DVD" or material == "A-V")):
            mediaID = row["Bib Doc Number"]
            callNumber = (row["Primary Call No Desc"] + ' ' + row["Description"]).strip()
            if callNumber == "" or callNumber == None:
                callNumber = "NONE"
            loanType = row["Collection ID"]
            numLoans = row["No of Current Loans"]
            availability = ""
            if (processStatus == "Not in process" and numLoans == "0"):
                availability = "Available"
            elif (processStatus == "LSC" and numLoans == "0"):
                availability = "Available Upon Request"
            elif (numLoans == "1"):
                availability = "Checked Out"
            else:
                availability = "On Order"
            if (processStatus == "Lost" or processStatus == "Missing"):
                availability = "Lost/Missing"
            newRow = itemID + delim + mediaID + delim + callNumber + delim + loanType + delim + availability
            print newRow.encode('utf-8')
        
