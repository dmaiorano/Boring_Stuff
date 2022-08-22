import os
folder_list_=[
    "Chapter_0-Introduction"
    ,"Chapter_1-Python_Basics"
    ,"Chapter_2-Flow_Control"
    ,"Chapter_3-Functions"
    ,"Chapter_4-Lists"
    ,"Chapter_5-Dictionaries_and_Structuring_Data"
    ,"Chapter_6-Manipulating_Strings"
    ,"Chapter_7-Pattern_Matching_with_Regular_Expressions"
    ,"Chapter_8-Input_Validation"
    ,"Chapter_9-Reading_and_Writing_Files"
    ,"Chapter_10-Organizing_Files"
    ,"Chapter_11-Debugging"
    ,"Chapter_12-Web_Scraping"
    ,"Chapter_13-Working_with_Excel_Spreadsheets"
    ,"Chapter_14-Working_with_Google_Spreadsheets"
    ,"Chapter_15-Working_with_PDF_and_Word_Documents"
    ,"Chapter_16-Working_with_CSV_Files_and_JSON_Data"
    ,"Chapter_17-Keeping_Time,_Scheduling_Tasks,_and_Launching_Programs"
    ,"Chapter_18-Sending_Email_and_Text_Messages"
    ,"Chapter_19-Manipulating_Images"
    ,"Chapter_20-Controlling_the_Keyboard_and_Mouse_with_GUI_Automation"
]

for folder in folder_list_:
    os.mkdir("C:\\Users\\320172397\\OneDrive - Philips\\Documents\\Training\\PersonalTraining\\Git\\Automate-Boring-Stuff\\Boring_Stuff\\"+folder)
