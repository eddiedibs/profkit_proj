#!/home/edd1e/Desktop/stuff/studies/Programming/python_projects/profkit_project/prfkit_env/bin/python3.8


import sqlite3
import settings as s
import subprocess
import re
import sys
import platform
import os
import gspread
import pywhatkit

class mainFunctions:
    def __init__(self):
        pass




    ## Function that checks whether or not work directory variables are in settings.py
    @classmethod
    def check_folders(cls):
        try:
            with open(f'{s.settings_file}', 'r') as read_file:
                data = read_file.readlines()
                ## Check folder dirs by using the os module
                for folder_index, folder in enumerate(s.folders, start=0):
                    ## if it's equal to None, then it is not registered
                    if s.folder_dirs[folder_index] == None:
                        ## It is going to look for every directory path, name and files that are in the HOME directory
                        for dirpath, dirnames, _ in os.walk(os.environ.get('HOME')):
                            for dirname in dirnames:
                                ## and for every directory name that matches settings.folders[] list, it will write it to the Settings.py file
                                if dirname == s.folders[folder_index]:
                                    dirpath = os.path.join(f'{dirpath}', f'{dirname}')
                                    print(f"{s.green}[ DIRECTORY FOUND ] {s.re1} {dirpath}\n")
                                    ## Now for every line in the data of settings.py, you are going to split it, so that we are left with the left
                                    ## part of the output (Which are all the names of the variables)
                                    for index, line in enumerate(data, start=0):
                                        settings_line = line.split(' ')
                                        ## and if one of those split lines is equal to any of the folder_vars in settings.py, you are going to
                                        ## Rewrite the directories as string variables on settings.py
                                        if settings_line[0] == s.folder_vars[folder_index]:
                                            data[index] = f"{s.folder_vars[folder_index]} = '{dirpath.strip()}'\n"
                                       
                                        else:
                                            pass
                                    with open(f'{s.settings_file}', 'w') as write_file:
                                        write_file.writelines(data)
                                        print(f'{s.green}[ OUTPUT SAVED ]{s.re1}\n') 
                        
                                    if folder == s.folders[-1]:
                                        print(f'{s.green}[ SUCCESS ]{s.re1} Directories have been registered successfully!')
                                        read_file.close()
                                        write_file.close()

                                    else:
                                        pass

                                ## Else it was not found
                                else:
                                    pass

                    else:
                        print(f"{s.green}[ INFO ] Directory '{folder}' already registered!{s.re1}\n")


            


        except KeyboardInterrupt:
            print(f'{s.red}[ACTION ABORTED] You have exited profkit{s.re1}\n')
        




    # Function that gets all of student info from a google spreadsheet with the help of its API and the gspread module 
    @classmethod
    def get_all_student_info(cls):
        try:
            
            # first we specify the path for credentials 
            gc = gspread.service_account(filename=os.path.join(f'{s.SEC_KEYS}', 'c.json'))
            # Then we open the file which contains the key for the url
            with open(os.path.join(f'{s.SEC_KEYS}', 'key.txt')) as sec_file:
                sec_file = sec_file.readline().strip()
            # Then we process the file through gspread
            sh = gc.open_by_key(sec_file) 
            
            # And we specify the sheet
            worksheet = sh.sheet1

            # Then we retrieve all the info from the sheet
            res = worksheet.get_all_records()
            student_info = res
            student_info_list = []

            # And now we connect to the local database 
            db = sqlite3.connect('student.db')
            c = db.cursor()
            
            # Now we query all of the student info so that we can compare it with the spreadsheet,
            # and if there is new data on the spreadsheet, it will insert it to the database. 
            c.execute("SELECT * FROM students")
            all_db_data = c.fetchall()

    
            for id, item in enumerate(student_info):
                list_of_values = list(item.values())
                # And we are also going to remove the empty space at the end
                list_of_values[1] = list_of_values[1].strip()
                list_of_values[2] = list_of_values[2].strip()
                # If there is actually db data and not just an empty list
                if all_db_data:

                    try:
                        # If the tuple of the values of the google form data (student_info) is not equal to its index
                        # It's going to pass
                        if tuple(list_of_values) != all_db_data[id][1:]:
                            pass

                        # and if it's equal to it, then we are going to print that it's already in the system
                        else:
                            print('[EQUAL] Row already in system\n')

                    # if we get an IndexError, that means it wasn't found, so that student is new, so we append the info to the list
                    except IndexError:
                        print(f'{s.green}[NOT FOUND]{s.re1} NEW STUDENT \'{list_of_values[1]}\' HAS BEEN ASSIGNED!\n')
                        list_of_values.insert(0, id)
                        student_info_list.append(list_of_values)


                #Else, you are going to append it to student_info_list
                else:
                    list_of_values.insert(0, id)
                    student_info_list.append(list_of_values)
                    print('NEW VALUES HAVE BEEN APPENDED\n')
                    

            db_student_info_values = []

            # Now we convert the lists in the list student_info_list to tuples 
            # (because they need to be in tuples when we register them through sqlite3)
            # and after that we append them to db_student_info_values list
            for id, item in enumerate(student_info_list):
                item = tuple(student_info_list[id])
                db_student_info_values.append(item)

            # Then we return the value
            return db_student_info_values
            

        except KeyboardInterrupt:
            print(f'{s.red}[ACTION ABORTED] You have exited profkit{s.re1}\n')
        
        except FileNotFoundError as fileErrMsg:
            print(f'{s.red}[ERROR MESSAGE]{s.re1} {fileErrMsg}\n')
            print(f'{s.green}[INFO]{s.re1} Searching for file directories...\n')
            mainFunctions.check_folders()

    @classmethod
    def print_student_form_link(cls):
        try:
            print(s.forms_link + '\n')

        except Exception as ex:
            print(ex)


    @classmethod
    def send_std_msg(cls, type='', param:str=''):
        try:
            std_list = student_logic.student_db_check(type, param)
            number = std_list[0][5]
            country = std_list[0][6]
            course_lang = std_list[0][8]
            if course_lang == 'Inglés':
                msg_lang = s.msg_homework

            else:
                msg_lang = s.msg_devoir

            for phone_code_country in s.phone_codes.keys():
                if phone_code_country == country:
                    phone_code = s.phone_codes.get(country)
                    phone_number = f'{phone_code}{number}'
                    print(f"{s.green}[INFO]{s.re1} Message will be sent to {type}: {param}")
                    pywhatkit.sendwhatmsg_instantly(phone_number, msg_lang)


                else:
                    pass



        except KeyboardInterrupt:
            pass


####################################################################
#
#
#                  STUDENT DATABASE HANDLING
#
#
####################################################################

class student_logic:
    def __init__(self):
        pass


    @classmethod
    def student_db_register(cls):
        try:
            student_info_rows = mainFunctions.get_all_student_info()
            for row in student_info_rows:

                conn = sqlite3.connect('student.db')
                c = conn.cursor()
                c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
                conn.commit()
                conn.close()


        except KeyboardInterrupt:
            print(f'{s.red}[ACTION ABORTED] You have exited profkit{s.re1}\n')
        
        except Exception as ex:
            print(ex)

    @classmethod
    def student_db_check_all(cls):
        try:
            conn = sqlite3.connect('student.db')
            c = conn.cursor()
            c.execute("SELECT * FROM students")
            data = c.fetchall()
            conn.commit()
            conn.close()
            return data

        except KeyboardInterrupt:
            print(f'{s.red}[ACTION ABORTED] You have exited profkit{s.re1}\n')


    @classmethod
    def student_db_check(cls, type='', param=''):
        try:
            conn = sqlite3.connect('student.db')
            c = conn.cursor()
            c.execute(f"SELECT * FROM students WHERE {type}='{param}'")
            data = c.fetchall()
            conn.commit()
            conn.close()
            return data

        except KeyboardInterrupt:
            print(f'{s.red}[ACTION ABORTED] You have exited profkit{s.re1}\n')




    @classmethod
    def student_db_remove_all(cls):
        try:
            conn = sqlite3.connect('student.db')
            c = conn.cursor()
            sql = "DELETE FROM students"
            c.execute(sql)
            print('ALL ROWS HAVE BEEN DELETED\n')
            conn.commit()
            conn.close()

        except KeyboardInterrupt:
            print(f'{s.red}[ACTION ABORTED] You have exited profkit{s.re1}\n')
        
    @classmethod
    def student_db_remove(cls, field, arg):
        try:
            conn = sqlite3.connect('student.db')
            c = conn.cursor()
            c.execute(f"SELECT * FROM students WHERE {field}=?", (arg,))

            print(f'{s.red}[USER \'{c.fetchall()[0][2]}\' WILL BE DELETED]{s.re1}\n')
            sqlDelete = f"DELETE FROM students WHERE {field}=?"
            c.execute(sqlDelete, (arg,))

            print(f'{s.red}[USER DELETED]{s.re1}\n')
            conn.commit()
            conn.close()

        except KeyboardInterrupt:
            print(f'{s.red}[ACTION ABORTED] You have exited profkit{s.re1}\n')
        




if __name__ == '__main__':
    mainFunctions.send_std_msg('first_name', 'Elizabeth')

