#define MyAppName "FnUtils"
#define MyAppVersion "2"
#define MyAppPublisher "esty"
#define MyAppURL "https://github.com/esteban-cz/FnUtilsV2"
#define MyAppExeName "FnUtils.exe"

[Setup]
AppId={{79854D41-82CB-41C7-B548-6E344B915B9D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=C:\{#MyAppName}
DisableDirPage=yes
DisableProgramGroupPage=yes
LicenseFile=C:\Users\tomec\VSCodeProjects\FnUtilsV2\LICENSE
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\Users\tomec\VSCodeProjects\FnUtilsV2\output
OutputBaseFilename=FnUtils_setup
SetupIconFile=C:\FnUtils\FnUtils.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "czech"; MessagesFile: "compiler:Languages\Czech.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\tomec\VSCodeProjects\FnUtilsV2\output\__main__\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\tomec\VSCodeProjects\FnUtilsV2\output\__main__\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

