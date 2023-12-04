import pyautogui,time,os,psutil,subprocess,configparser,customtkinter,requests,sys,tkinter

config = configparser.ConfigParser()
config.read('config.ini')

directory_name = config.get('Settings', 'directory_name')

def theme(theme: str):
    customtkinter.set_default_color_theme(f"themes/{theme}.json")

def click(x, y):
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
def dclick(x, y):
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(x, y)
    pyautogui.doubleClick()

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def open_app(app):
    app_path = os.path.join(directory_name, app)
    subprocess.Popen(app_path)
    
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def write(text):
    pyautogui.typewrite(text)

def delay(seconds: float):
    time.sleep(seconds)

def check_and_close_process(process_name):
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            proc.kill()

def check_required_files(directory):
    required_files = [
        'alphares_1.2.1_x64.exe',
        'FilterKeysSetter.exe',
        'TimerResolution.exe',
        'Extreme_Performance_Utility.bat',
        'Ultimate_Cleaner_by_esty.bat'
    ]

    all_exist = all(os.path.exists(os.path.join(directory, file)) for file in required_files)
    return all_exist

def ButtonExitPressed():
    sys.exit()

def DownloadResources():
    file_urls = [
    "https://cdn.discordapp.com/attachments/1180154707382108321/1180155106080063518/alphares_1.2.1_x64.exe?ex=657c6417&is=6569ef17&hm=51f432a03d0fbefaba26089eff1faf1bea6e6a1f4d17735349e75ec91a931bcc&",
    "https://cdn.discordapp.com/attachments/1180154707382108321/1180155106608562186/Extreme_Performance_Utility.bat?ex=657c6417&is=6569ef17&hm=635c1fbabbce320ddfb83f1ec4afd5f697ca8ec40625312e4db5b6b5074d965f&",
    "https://cdn.discordapp.com/attachments/1180154707382108321/1180155106927325316/FilterKeysSetter.exe?ex=657c6417&is=6569ef17&hm=f78ec00384b137b99f33716440682ede04358aeac70cfb293c631b2f3e564115&",
    "https://cdn.discordapp.com/attachments/1180154707382108321/1180155107246080110/TimerResolution.exe?ex=657c6417&is=6569ef17&hm=932965af842ff0a3e6e3aa825672a412ba54ea690edfd60c1a1f810b1029587a&",
    "https://cdn.discordapp.com/attachments/1180154707382108321/1180274008554487969/Ultimate_Cleaner_by_esty.bat?ex=657cd2d4&is=656a5dd4&hm=a3468479219daa39d92e0f08eb072a950cd01412883b80b1136b98a87915fbfa&",
    "https://cdn.discordapp.com/attachments/1180154707382108321/1180525087921807400/FnUtils.ico?ex=657dbcaa&is=656b47aa&hm=733d9457b0f03acd1c54d1cbde1efd8e51e15406bd306d2f6cebdc380c4ce2b4&"
    ]
    for url in file_urls:
        file_name = os.path.join(directory_name, url.split('/')[-1].split('?')[0])
        with open(file_name, 'wb') as file:
            response = requests.get(url)
            file.write(response.content)
    config.set('Settings', 'downloaded_resources', 'True')
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def CustomResolution():
    app = 'alphares_1.2.1_x64.exe'
    check_and_close_process(app)
    open_app(app)
    pass

def ExmCleaner():
    app = 'Extreme_Performance_Utility.bat'
    check_and_close_process(app)
    open_app(app)
    pass

def UltimateCleaner():
    app = 'Ultimate_Cleaner_by_esty.bat'
    check_and_close_process(app)
    open_app(app)
    pass

def TimerResolution():
    app = 'TimerResolution.exe'
    check_and_close_process(app)
    open_app(app)
    original_pos = pyautogui.position()
    delay(0.2)
    click(830, 590)
    pyautogui.hotkey('win', 'down')
    pyautogui.moveTo(original_pos)
    pass

def get_filter_keys_settings():
    if 'FilterKeysSettings' in config:
        return config['FilterKeysSettings']
    else:
        return None

filter_keys_settings = get_filter_keys_settings()

if filter_keys_settings:
    ignore_under = filter_keys_settings.get('ignore_under')
    repeat_delay = filter_keys_settings.get('repeat_delay')
    repeat_rate = filter_keys_settings.get('repeat_rate')
else:
    ignore_under = '0'
    repeat_delay = '90'
    repeat_rate = '25'

def FilterKeys(filter_keys_option):
    app = 'FilterKeysSetter.exe'
    check_and_close_process(app)
    open_app(app)
    original_pos = pyautogui.position()

    selected_option = filter_keys_option.get()

    if selected_option == "on":
        click(1020, 620) 
        click(1010, 350)
        click(1010, 408)
        click(1010, 427)
        click(1010, 446)
        click(1010, 467)
        dclick(920, 400);delay(0.1)
        write(ignore_under)
        dclick(920, 428);delay(0.1)
        write(repeat_delay)
        dclick(920, 458);delay(0.1)
        write(repeat_rate)
        click(920, 720)
    elif selected_option == "off":
        click(1010, 625)
        click(920, 720)

    pyautogui.moveTo(original_pos)

def create_download_button(app):
    def download_resources_and_disable_button():
        DownloadResources()
        button_resources.configure(state=customtkinter.DISABLED)

    button_resources = customtkinter.CTkButton(app, text="Download Necessary Resources", command=download_resources_and_disable_button)
    button_resources.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    return button_resources

def create_resolution_button(app):
    button_resolution = customtkinter.CTkButton(app, text="Custom Fortnite resolution?", command=CustomResolution)
    button_resolution.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
    return button_resolution

def create_exm_cleaner_button(app):
    button_exm_cleaner = customtkinter.CTkButton(app, text="EXM Cleaner (slow, manual, more options)", command=ExmCleaner)
    button_exm_cleaner.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
    return button_exm_cleaner

def create_ultimate_cleaner_button(app):
    button_ultimate_cleaner = customtkinter.CTkButton(app, text="Ultimate cleaner (fast, automatic, no options)", command=UltimateCleaner)
    button_ultimate_cleaner.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
    return button_ultimate_cleaner

def create_timer_resolution_button(app):
    button_timer_resolution = customtkinter.CTkButton(app, text="TimerResolution", command=TimerResolution)
    button_timer_resolution.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
    return button_timer_resolution

def create_filter_keys_button(app):
    button_filter_keys = customtkinter.CTkButton(app, text="FilterKeys", command=lambda: FilterKeys(filter_keys_option))
    button_filter_keys.grid(row=5, column=0, padx=20, pady=20, sticky="ew")

    filter_keys_option = tkinter.StringVar()
    filter_keys_option = tkinter.StringVar(value="on")

    radio_on = customtkinter.CTkRadioButton(app, text="Turn Filter Keys On", variable=filter_keys_option, value="on")
    radio_on.grid(row=6, column=0, padx=20, pady=5, sticky="w")

    radio_off = customtkinter.CTkRadioButton(app, text="Turn Filter Keys Off", variable=filter_keys_option, value="off")
    radio_off.grid(row=7, column=0, padx=20, pady=5, sticky="w")

    radio_on.select()

    return button_filter_keys

def create_exit_button(app):
    button_exit = customtkinter.CTkButton(app, text="Exit", command=ButtonExitPressed, fg_color="red", hover_color="#660000")
    button_exit.grid(row=8, column=0, padx=20, pady=20, sticky="ew")
    return button_exit

def change_theme(theme_choice):
    config.set('ThemesSettings', 'active_theme', theme_choice)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    theme(theme_choice)
    restart_program()
