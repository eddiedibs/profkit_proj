#!/home/edd1e/Desktop/stuff/studies/Programming/python_projects/profkit_project/prfkit_env/bin/python3.8


from colorama import Style as Style2



################################################

               #SETTINGS FILE

################################################





## Colors and Prompt
green = "\033[32;1m"
red = "\033[31;1m"
re1 = Style2.RESET_ALL
prompt_arrow = 'profkit>>'


## Prompt Messages ##

## Note: Make this functionality with google forms to retrieve info from your new students  



## file managers ##
nautilus_mnger = 'nautilus'
caja_mnger = 'caja'
thunar_mnger = 'Thunar'

## Command list ##

command_list = ['-o', '-a']
open_folder_cmd = command_list[0]
add_student = command_list[1]

## Database student_info fields ##

# db_student_info = {'timestamp': 'timestamp',
#                     'first_name': 'first_name',
#                     'last_name': 'last_name',
#                     'age': 'age',
#                     'numbers': 'numbers',
#                     'country': 'country',
#                     'email': 'email',
#                     'french_english': 'french_english',
#                     'was_studied': 'was_studied',
#                     'lang_exp': 'lang_exp',
#                     'desired_course': 'desired_course',
#                     'app_experience': 'app_experience'}

# c.execute(f"""CREATE TABLE students (
#                 id integer,
#                 timestamp integer,
#                 first_name text,
#                 last_name text,
#                 age integer,
#                 numbers integer,
#                 country text,
#                 email text,
#                 french_english text,
#                 was_studied text,
#                 lang_exp text,
#                 desired_course text,
#                 app_experience text
#                 )""")





db_student_info = ['timestamp',
                    'first_name',
                    'last_name',
                    'age',
                    'numbers',
                    'country',
                    'email',
                    'french_english',
                    'was_studied',
                    'lang_exp',
                    'desired_course',
                    'app_experience']




# If you wish to add more directories, you need to make sure folder_vars and folders both follow the SAME order
####### DIRECTORIES #######

MAIN_FOLDER_DIR = None
FR_FOLDER_DIR = None
ENG_FOLDER_DIR = None
MAT_DU_PROF = None
FR_A1 = None
SEC_KEYS = None



forms_link = None

folder_dirs = [MAIN_FOLDER_DIR, ENG_FOLDER_DIR, FR_FOLDER_DIR, MAT_DU_PROF, FR_A1, SEC_KEYS]
folder_vars = ['MAIN_FOLDER_DIR', 'FR_FOLDER_DIR', 'ENG_FOLDER_DIR', 'MAT_DU_PROF', 'FR_A1', 'SEC_KEYS']
folders = ['work', 'French', 'English', 'material-du-prof', 'ae+1', 'sec_keys']



msg_tarea = """Hola ! Cómo estás? Quería decirte que ya en la plataforma Discord está las asignaciones preparadas ! 😄"""
msg_homework = """Hello ! How are you? I wanted to tell you that the homework is already on Discord ! 😄🇺🇸"""
msg_devoir = """Salut ! Comment vas tu? je voulais te dire qu'on peut déjà trouver les devoirs sur discord ! 😄
🇫🇷"""
# msg_info = """Hola ! Cómo estás? Quería decirte que ya en la plataforma discord está las asignaciones preparadas ! 😄"""


homework_messages = [msg_tarea, msg_homework,msg_devoir]






phone_codes = {
    'Venezuela': '+58',
    'Mexico': '+52',
    'Argentina': '+54',
    'Colombia': '+57',
    'Chile': '+56',
    'Ecuador': '+593',
    'Perú': '+51',
    'Estados Unidos': '+1'

}



settings_file = __file__


