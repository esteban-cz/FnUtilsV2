import customtkinter,configparser,defs

config = configparser.ConfigParser()
config.read('config.ini')

active_theme = config.get('ThemesSettings', 'active_theme', fallback='Blue')

directory_name = config.get('Settings', 'directory_name')

defs.create_directory(directory_name)

apps_to_close = [
    'alphares_1.2.1_x64.exe',
    'FilterKeysSetter.exe',
    'TimerResolution.exe',
    'Extreme_Performance_Utility.bat',
    'Ultimate_Cleaner_by_esty.bat'
]

for app in apps_to_close:
    defs.check_and_close_process(app)

app = customtkinter.CTk()
app.title("FnUtils by esty")
defs.set_icon(app)
app.geometry("400x520")

theme_var = customtkinter.StringVar(value=active_theme)
defs.theme(active_theme)
themes = ["Blue", "Anthracite", "DaynNight", "GhostTrain", "Greengage", "GreyGhost", "Hades", "Harleyquin", "MoonlitSky", "NeonBanana", "NightTrain", "Oceanix", "Sweetkind", "TestCard", "TrojanBlue"]
theme_dropdown = customtkinter.CTkComboBox(
    master=app,
    values=themes,
    command=lambda choice: defs.change_theme(choice),
    variable=theme_var,
    state="readonly"
)
theme_dropdown.grid(row=0, column=0, padx=20, pady=10, sticky="e")

directory_name = config.get('Settings', 'directory_name', fallback='C:\\FnUtils')
all_files_exist = defs.check_required_files(directory_name)

if all_files_exist:
    config.set('Settings', 'downloaded_resources', 'True')
else:
    config.set('Settings', 'downloaded_resources', 'False')

with open('config.ini', 'w') as configfile:
    config.write(configfile)

app.grid_columnconfigure(0, weight=1)

downloaded_resources = config.getboolean('Settings', 'downloaded_resources', fallback=False)

if not downloaded_resources:
    button_resources = defs.create_download_button(app)

button_resolution = defs.create_resolution_button(app)
button_exm_cleaner = defs.create_exm_cleaner_button(app)
button_ultimate_cleaner = defs.create_ultimate_cleaner_button(app)
button_timer_resolution = defs.create_timer_resolution_button(app)
button_filter_keys = defs.create_filter_keys_button(app)
ButtonExit = defs.create_exit_button(app)

app.mainloop()
