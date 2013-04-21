import csv


print "Welcome to COHM"

start_lat = raw_input("Input starting LAT:")
start_long = raw_input("Input starting LONG:")
course_length = raw_input("Input total course length in metres:")

sourcecsv = raw_input("What is the name of the master (.csv) file?")
dist_needed = 0

start_lat = float(start_lat)
start_long = float(start_long)
course_length = float(course_length)
middle_sum = 0

test_total = start_lat + start_long + course_length

with open(sourcecsv , 'r') as csvfile:
    curiosity_course = csv.reader(csvfile, delimiter = ',', quotechar = '"')
    print(csvfile.closed)

    row_counter = 0
    for row in curiosity_course:
        try:
            middle_sum = middle_sum + float(row[1])
            if course_length > middle_sum:
                # take middle sum, remove current row
                # to get distance less than course_length
                # middle_sum = middle_sum - float(row[1])
                
                # how much further do we need to go?
                dist_needed = course_length - middle_sum
                print(middle_sum)
                row_counter = row_counter + 1
                pass
        except:
            pass

leg_count = row_counter
print(leg_count)

    
    #print(result[0])
    #print(result[1])




        



