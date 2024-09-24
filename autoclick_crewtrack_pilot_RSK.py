import os
import pyautogui as py
import time
import pyscreeze


## Pilots


# Define the command to execute
command = 'cmd.exe /c "cd /d C:\\Users\\025883\\OneDrive - Hawaiian Airlines, Inc\\Documents\\My Tableau Prep Repository\\Flows && start "" "RSK_REPORT_UPDATE_FLOW.tfl""'

# Execute the command
exit_code = os.system(command)
if exit_code != 0:
    print(f"Command failed with exit code {exit_code}")
    
time.sleep(80)
    
    # Get the current working directory
directory = 'C:\\Users\\025883\\OneDrive - Hawaiian Airlines, Inc\\Documents\\R Scripts\\python_autoclick_prep'


# file path to images
file_path_images = os.path.join(directory, 'buttons_click')

# file path to full size
fullsize_path = os.path.join(file_path_images, 'full_size_prep.png')

# Locate the image on the screen
fullsize_emblem_click = py.locateOnScreen(fullsize_path, confidence = 0.9)

# click database emblem
py.click(fullsize_emblem_click)

# file path to db emblem
db_emblem_path = os.path.join(file_path_images, 'database_emblem.png')

# Locate the image on the screen
database_emblem_click = py.locateOnScreen(db_emblem_path, confidence = 0.6)

# click database emblem
py.click(database_emblem_click)

time.sleep(5)

# locate sign in button
sign_in_path = os.path.join(file_path_images, 'sign_in.png')

# locate on screen
sign_in_emblem = py.locateOnScreen(sign_in_path, confidence = 0.8)

#click sign in emblem
py.click(sign_in_emblem)

time.sleep(25)

# locate AO in button
single_AO_path = os.path.join(file_path_images, 'single_AO.png')

# locate AO screen
single_AO_path_emblem = py.locateOnScreen(single_AO_path, confidence = 0.8)

#click AO emblem
py.click(single_AO_path_emblem)

time.sleep(10)

# locate allow in button
allow_path = os.path.join(file_path_images, 'allow.png')

# locate allow screen
allow_path_emblem = py.locateOnScreen(allow_path, confidence = 0.8)

#click allow emblem
py.click(allow_path_emblem)

time.sleep(10)

# locate prep in button
prep_path = os.path.join(file_path_images, 'prep.png')

# locate allow screen
allow_prep_emblem = py.locateOnScreen(prep_path, confidence = 0.8)

#click allow emblem
py.click(allow_prep_emblem)

time.sleep(10)

# locate play in button
play_path = os.path.join(file_path_images, 'play.png')

# locate AO screen
allow_play_emblem = py.locateOnScreen(play_path, confidence = 0.8)

#click AO emblem
py.click(allow_play_emblem)

time.sleep(5)


# locate replace in button
replace_path = os.path.join(file_path_images, 'replace.png')

# locate AO screen
allow_replace_emblem = py.locateOnScreen(replace_path, confidence = 0.8)

#click AO emblem
py.click(allow_replace_emblem)


time.sleep(60)

# locate exit in button
exit_path = os.path.join(file_path_images, 'exit.png')

# locate AO screen
allow_exit_emblem = py.locateOnScreen(exit_path, confidence = 0.8)

#click AO emblem
py.click(allow_exit_emblem)



