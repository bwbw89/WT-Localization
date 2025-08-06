# War Thunder Custom Localization (units.csv)
The purpose of this localization pack in War Thunder is to provide the player with extra information about enemy (and friendly) units in-game that the base localization does not provide. This is especially useful in any gamemode and even custom battles that utilize similar settings to Realistic Battles (RB) in terms of vehicle markers. For example, the base game might show a label of F-4, but will not tell you exactly what model, limiting your ability to judge threats and properly adapt in playstyle. This localization fixes these issues by specifying what exact vehicle is present, such as the Israeli F-4E Kurnass.
## First-time Instructions
1. Click "Download raw file" on units.csv from Github.
2. Access the War Thunder files on your device's File Explorer.
3. Find the "config.blk" file and open in a text editor such as Notepad.
4. Add this line to the debug section: ```testLocalization:b=yes```
   Your debug section could look like the following:
```
  debug{
    netLogerr:b=yes
    testLocalization:b=yes
    screenshotHiRes:b=no
    screenshotAsJpeg:b=yes
  }
```
5. Save your changes (using Ctrl+S or any other method).
6. Launch War Thunder.
7. A "lang" folder should appear in your War Thunder files.
8. Go into the "lang" folder and copy the **NEW** units.csv file and replace the base one.
Your localization should now be updated.
## Updating Localization
Localizations need to be updated everytime new vehicles are added to War Thunder, or else the text will break. Assuming you already have the custom localizaton, the following instructions will help you update the localization to the newest update, or fix any broken text you might face when certain updates occur, such as events, even when there are no new vehicles.
1. Delete the "lang" folder from your War Thunder files.
2. Go into War Thunder and change your language from English to Russian, which should regenerate a new "lang" folder.
3. Copy the **NEW** units.csv file into the newly generated "lang" folder.
4. Change language back to English.
## Auto Parser
The purpose of the auto parser file is to automatically do most of the localization process, thus making new localization updates easier. This file should be ignored for the most part, as the only file necessary to update your localization is the units.csv file.
To use auto_parser.py, the user needs to create an input.txt and output.txt in the auto_parser folder. Then, the user should copy and paste the new units from the default Gaijin units.csv into the input.txt. Then, the auto_parser.py file should be run, creating a parsed and localized version in output.txt, which can be copy and pasted into your local (localized) units.csv file where custom changes may be made if necessary.
