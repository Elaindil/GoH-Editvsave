import zipfile
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import re
import os
import webbrowser
root = Tk()
root.title('Save Editor')
helpLabel = Label(root,
                  text="To start editing the save choose your conquest save.\n It should be in (user\Documents\my games\gates of hell\profiles\\numbers\campaign\n or Users/USERNAME/AppData/Local/digitalmindsoft/gates of hell/campaign")
helpLabel.grid(row=1, column=1)
mainSaveFile = "./status"
secondarySaveFile = "./campaign.scn"
def openfile():
    save = filedialog.askopenfilename(initialdir=f"/", title="Select your save", filetypes=[('save files', "*.sav")])
    s = zipfile.ZipFile(save, 'r')
    s.extractall('')
    edit_window = Toplevel(root)
    edit_window.title('Editing the save')
    edit_window.minsize(700, 500)
    root.withdraw()
    global showMP
    global showSP
    global showAP
    global showRP
    showMP = StringVar()
    showSP = StringVar()
    showAP = StringVar()
    showRP = StringVar()
    resourceLabel = Label(edit_window, text='Resource editing')
    resourceLabel.grid(row=1, column=1)
    resourceLabelMP = Label(edit_window, text='Manpower')
    resourceLabelMP.grid(row=2, column=2)
    currentMP = Spinbox(edit_window, from_=1.00, to=99990.00, increment=100, textvariable=showMP)
    currentMP.grid(row=2, column=1)
    resourceLabelSP = Label(edit_window, text='Special points')
    resourceLabelSP.grid(row=3, column=2)
    currentSP = Spinbox(edit_window, from_=1.00, to=99990.00, increment=1, textvariable=showSP)
    currentSP.grid(row=3, column=1)
    resourceLabelAP = Label(edit_window, text='Ammo points')
    resourceLabelAP.grid(row=4, column=2)
    currentAP = Spinbox(edit_window, from_=1.00, to=99990.00, increment=100, textvariable=showAP)
    currentAP.grid(row=4, column=1)
    resourceLabelRP = Label(edit_window, text='Research points')
    resourceLabelRP.grid(row=5, column=2)
    currentRP = Spinbox(edit_window, from_=1.00, to=99990.00, increment=1, textvariable=showRP)
    currentRP.grid(row=5, column=1)
    global difficultyLevel
    difficultyLevel = IntVar()
    difficultyLevel.set(None)
    difficultyEasy = Radiobutton(edit_window, text='Easy', variable=difficultyLevel, value=1)
    difficultyNormal = Radiobutton(edit_window, text='Normal', variable=difficultyLevel, value=2)
    difficultyHard = Radiobutton(edit_window, text='Hard', variable=difficultyLevel, value=3)
    difficultyHeroic = Radiobutton(edit_window, text='Heroic', variable=difficultyLevel, value=4)
    difficultyLabel = Label(edit_window, text='Difficulty')
    difficultyLabel.grid(row=1, column=3)
    difficultyEasy.grid(row=2, column=3)
    difficultyNormal.grid(row=3, column=3)
    difficultyHard.grid(row=4, column=3)
    difficultyHeroic.grid(row=5, column=3)
    global fogOfWar
    fogOfWar = IntVar()
    fogOfWarOn = Radiobutton(edit_window, text='Fog of war on', variable=fogOfWar, value=1)
    fogOfWarOff = Radiobutton(edit_window, text='Fog of war off', variable=fogOfWar, value=2)
    fowLabel = Label(edit_window, text='Fog of war setting')
    fowLabel.grid(row=7, column=3)
    fogOfWarOn.grid(row=8, column=3)
    fogOfWarOff.grid(row=9, column=3)


    def remergeMain():
        root.deiconify()
        edit_window.destroy()

    def scanSave():
        newSave = open(mainSaveFile, 'r').read()
        currentDifficulty = re.findall("	{difficulty.+", newSave)
        currentDifficultyText = currentDifficulty[0].replace("	{difficulty ", "").strip()
        fogOfWarIn = re.findall("	{fogofwar .+", newSave)
        fogOfWarText = fogOfWarIn[0].replace("	{fogofwar ", "").strip()

        if "{difficulty easy}" in newSave:
            difficultyLevel.set(1)
        if '{difficulty normal}' in newSave:
            difficultyLevel.set(2)
        if "{difficulty hard}" in newSave:
            difficultyLevel.set(3)
        if "{difficulty heroic}" in newSave:
            difficultyLevel.set(4)
        if "{fogofwar fog_realistic}" in newSave:
            fogOfWar.set(1)
        if "{fogofwar fog_off}" in newSave:
            fogOfWar.set(2)

        mpInSaveInt = re.findall("\{mp \d+", newSave)
        mpInSave = mpInSaveInt[0].replace("{mp ", "").strip()
        rpInSaveInt = re.findall('\{rp+ \d+', newSave)
        rpInSave = rpInSaveInt[0].replace("{rp ", "").strip()
        apInSaveInt = re.findall('\{ap+ \d+', newSave)
        apInSave = apInSaveInt[0].replace("{ap ", "").strip()
        spInSaveInt = re.findall('\{sp+ \d+', newSave)
        spInSave = spInSaveInt[0].replace("{sp ", "").strip()

        showSP.set(spInSave)
        showAP.set(apInSave)
        showMP.set(mpInSave)
        showRP.set(rpInSave)

        modsActivated = re.findall("		\"mod_.+", newSave)

        allMods = modsActivated
        eachMod = StringVar(value=allMods)
        modsActiveLabel = Label(edit_window, text='Mods Active')
        modsActiveLabel.grid(row=18, column=1)
        modList = Listbox(edit_window, height=7, listvariable=eachMod)
        modList.grid(row=19, column=1)
        modList.config(width=40)

        def deleteMod():
            deleteThis = modList.curselection()
            modList.delete(deleteThis)

        def checkMod():
            checkThis = modList.curselection()
            checkThistoo = modList.get(checkThis)
            checkThistoo = checkThistoo.replace('\"mod_', '').strip()
            checkThistoo = checkThistoo.replace(':0"', '').strip()
            webbrowser.open_new('https://steamcommunity.com/sharedfiles/filedetails/?id=' + checkThistoo)

        checkWorkshopButton = Button(edit_window, text='Mod Steam Page', command=checkMod)
        checkWorkshopButton.grid(row=19, column=2)
        deleteModButton = Button(edit_window, text='Delete mod', command=deleteMod)
        deleteModButton.grid(row=19, column=3)


        edit_window.protocol("WM_DELETE_WINDOW", on_closing)

        def savechanges():

            newSaveFile = open(mainSaveFile, "w")

            newFile = (newSave.replace(f'mp {mpInSave}', f'mp {showMP.get()}'))
            newFile = (newFile.replace(f'sp {spInSave}', f'sp {showSP.get()}'))
            newFile = (newFile.replace(f'rp {rpInSave}', f'rp {showRP.get()}'))
            newFile = (newFile.replace(f'ap {apInSave}', f'ap {showAP.get()}'))

            if fogOfWar.get() == 1:
                newFile = newFile.replace(fogOfWarText, 'fog_realistic}')
            elif fogOfWar.get() == 2:
                newFile = newFile.replace(fogOfWarText, 'fog_off}')

            if difficultyLevel.get() == 1:
                newFile = newFile.replace(currentDifficultyText, 'easy}')
            if difficultyLevel.get() == 2:
                newFile = newFile.replace(currentDifficultyText, 'normal}')
            if difficultyLevel.get() == 3:
                newFile = newFile.replace(currentDifficultyText, 'hard}')
            if difficultyLevel.get() == 4:
                newFile = newFile.replace(currentDifficultyText, 'heroic}')

            countMods = 0

            for mod in modsActivated:
                newFile = (newFile.replace(f'{mod}', f'{modList.get(countMods)}'))


                countMods = countMods + 1

            newSaveFile.write(newFile)
            newSaveFile.close()
            new_save = zipfile.ZipFile(save, 'w')

            new_save.write(secondarySaveFile)
            new_save.write(mainSaveFile)

            messagebox.showinfo("Saved", "Save edited")

            edit_window.destroy()
            root.destroy()

        saveButton = Button(edit_window, text='Save changes', command=savechanges)
        saveButton.grid(row=20, column=2)

    scanSave()

    edit_window.protocol("WM_DELETE_WINDOW", remergeMain)

def infoText():
    messagebox.showinfo('help',
                        'MAKE A BACKUP of the save before using the programm! Disable Steam cloud (optional). Do not use it if you\'re afraid to break a save(shouldn\'t happen with a back up). Click on mod and "Mod steam page" to go to this mod workshop page.')

workButton = Button(root, text='Choose your save', command=openfile)
workButton.grid(row=2, column=1)

workButton = Button(root, text='Read this info', command=infoText)
workButton.grid(row=2, column=2)

def on_closing():
    try:
        os.remove(mainSaveFile)
        os.remove(secondarySaveFile)
        root.destroy()
    except FileNotFoundError:
        root.destroy()

root.mainloop()