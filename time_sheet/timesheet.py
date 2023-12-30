import csv
import shutil
from datetime import datetime

HEADER = [['Date','Task','Time Spend','Description']]
FILE_NAME = 'time_sheet.csv'
META_FILE = 'meta_data.csv'
TIME_LOG = []

class file_operations:

    def check_file_status(self):
        try:
            with open (FILE_NAME) as time_sheet:
                self.file_backup()
                time_sheet.close()
        except FileNotFoundError as e:
            name = input("Enter your name: ")
            date_time = self.get_time("%m.%Y ")
            HEADER.insert(0, [f"{name}'s Time Sheet. Month:{date_time}"])
            print("Creating a new file : time_sheet.csv")
            with open (FILE_NAME,'w+', newline='') as time_sheet:
                print("Done")
                csvfile = csv.writer(time_sheet)
                for data in HEADER:
                    csvfile.writerow(data)
                time_sheet.close()
                
    def file_backup(self):

        date_time = self.get_time("%m.%d.%Y ") #now.strftime("%m.%d.%Y ")
        print(":: backup existing time_sheet.csv")

        #use shutil to copy file
        try:
            source_file =  open(FILE_NAME, 'r') #open existing csv file
        except FileNotFoundError as e:
            print(e)

        destination_file = open(f'backup/{date_time}{FILE_NAME}', 'w') #create a new backup with date
        shutil.copyfileobj(source_file, destination_file)
        print(":: Done")

    def get_time(self,format):
        now = datetime.now() # get current date and time
        return now.strftime(format)

class log_time:

    def get_user_log(self):
        day = file_handller.get_time("%d ")
        total_time = 0
        task = input('Enter task : ')
        while True:
            try:
                time = int(input('Enter spend time : '))
                total_time += time
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                break 
        des = input('Enter the description : ')
        TIME_LOG.insert(0,[day,task,time,des])

        with open (FILE_NAME,'a', newline='') as time_sheet:
            csvfile = csv.writer(time_sheet)
            for data in TIME_LOG:
                csvfile.writerow(data)
            time_sheet.close()
        
        handle_metadata.store_date_totoal_hours(total_time)
    
    def get_week_day(self):
        weekday = datetime.today().weekday()
        day = int(file_handller.get_time("%d"))
        month = int(file_handller.get_time("%m"))
        print("")
        # If today is Monday (aka 0 of 6)
        if weekday == 0 : print (f"Monday {day}/{month}")
        elif  weekday == 1 :print (f"Tuesday {day}/{month}")
        elif  weekday == 2 : print (f"Wednesday {day}/{month}")
        elif  weekday == 3 : print (f"Thursday {day}/{month}")
        elif  weekday == 4 : print (f"Friday {day}/{month}")
        else :
            print ("You cannot log time for weekends") 
            exit()
        
class metadata:
    def __init__(self):
        self.TOTAL_TIME = 0

    def get_date_totoal_hours(self,day):
        
        try:
            with open (META_FILE,'r', newline='') as meta_data:
                # spamreader = csv.reader(meta_data, delimiter=',')
                row = list(csv.reader(meta_data, delimiter=','))
                if int(row[0][0]) == day:
                    print(f":: Total entered hourse : {int(row[0][1])} h")
                    self.TOTAL_TIME = int(row[0][1])
                else:
                    print("no")
                meta_data.close()
        except FileNotFoundError as e:
            print("")

    def store_date_totoal_hours(self,total_time):

        day = int(file_handller.get_time("%d"))
        TOTAL_TIME = self.TOTAL_TIME + total_time
        print(f"Total added time for today : {TOTAL_TIME}")
        with open(META_FILE, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([day,TOTAL_TIME])

if __name__ == '__main__':
    
    file_handller = file_operations()
    loging = log_time()
    handle_metadata = metadata()

    loging.get_week_day()

    day = int(file_handller.get_time("%d"))
    handle_metadata.get_date_totoal_hours(day)

    file_handller.check_file_status()

    loging.get_user_log()

    print(":: Successfully logged time")