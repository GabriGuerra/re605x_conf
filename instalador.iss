[Setup]
AppName=Configurar RE605X
AppVersion=1.0
DefaultDirName={pf}\RE605X
DefaultGroupName=RE605X
OutputDir=dist
OutputBaseFilename=Instalador_RE605X
SetupIconFile=icone.ico
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icone.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Configurar RE605X"; Filename: "{app}\main.exe"; IconFilename: "{app}\icone.ico"
Name: "{commondesktop}\Configurar RE605X"; Filename: "{app}\main.exe"; IconFilename: "{app}\icone.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na área de trabalho"; GroupDescription: "Opções adicionais:"; Flags: unchecked

[Run]
Filename: "{app}\main.exe"; Description: "Executar Configurar RE605X"; Flags: nowait postinstall skipifsilent