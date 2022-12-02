import zipfile
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from zipfile import *
from tkinter import ttk  
import re
import os
import webbrowser





root = Tk()
root.title('Save Editor')
helpLabel = Label(root, text="To start editing the save choose your conquest save.\n It should be in (user\Documents\my games\gates of hell\profiles\\numbers\campaign\n or Users/USERNAME/AppData/Local/digitalmindsoft/gates of hell/campaign")


helpLabel.grid(row=1,column=1)

mainSaveFile = "./status"
secondarySaveFile = "./campaign.scn"





def openfile():
    save = filedialog.askopenfilename(initialdir="/", title="Select your save",filetypes=[('save files',"*.sav")])
    s = zipfile.ZipFile(save, 'r')
    s.extractall('')
    edit_window = Toplevel(root)
    edit_window.title('Editing the save')
    edit_window.minsize(700,500)
    root.withdraw()
    #aveZipName = re.sub('
    
    
    
    mainSaveFileTest = "./status"
    secondarySaveFileTest = "./campaign.scn"

    

    global showMP
    global showSP
    global showAP
    global showRP
    showMP= StringVar()
    showSP = StringVar()
    showAP = StringVar()
    showRP = StringVar()
    resourceLabel = Label(edit_window,text='Resource editing')
    resourceLabel.grid(row=1,column=1)

    resourceLabelMP = Label(edit_window, text='Manpower')
    resourceLabelMP.grid(row=2, column=2)

    currentMP = Spinbox(edit_window, from_=1.00, to=99990.00,increment=100, textvariable=showMP)
    currentMP.grid(row=2,column=1)

    resourceLabelSP = Label(edit_window, text='Special points')
    resourceLabelSP.grid(row=3, column=2)

    currentSP = Spinbox(edit_window, from_=1.00, to=99990.00,increment=1, textvariable=showSP)
    currentSP.grid(row=3, column=1)

    resourceLabelAP = Label(edit_window, text='Ammo points')
    resourceLabelAP.grid(row=4, column=2)

    currentAP = Spinbox(edit_window, from_=1.00, to=99990.00,increment=100, textvariable=showAP)
    currentAP.grid(row=4, column=1)

    resourceLabelRP = Label(edit_window, text='Research points')
    resourceLabelRP.grid(row=5, column=2)

    currentRP = Spinbox(edit_window, from_=1.00, to=99990.00,increment=1, textvariable=showRP)
    currentRP.grid(row=5, column=1)

    global difficultyLevel
    difficultyLevel = IntVar()
    difficultyLevel.set(None)

    difficultyEasy = Radiobutton(edit_window, text='Easy', variable=difficultyLevel, value=1)
    difficultyNormal = Radiobutton(edit_window, text='Normal', variable=difficultyLevel, value=2)
    difficultyHard = Radiobutton(edit_window, text='Hard', variable=difficultyLevel, value=3)
    difficultyHeroic = Radiobutton(edit_window, text='Heroic', variable=difficultyLevel, value=4)
    difficultyLabel = Label(edit_window,text='Difficulty')

    difficultyLabel.grid(row=1,column=3)
    difficultyEasy.grid(row=2,column=3)
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

    currentMaps = Label(edit_window, text='Next battle will happen on these maps')
    currentMaps.grid(row=10, column=1)

    changeMaps = Label(edit_window, text='Change maps')
    changeMaps.grid(row=10, column=2)
    
    
    
    def remergeMain():
        root.deiconify()
        edit_window.destroy()

    def scanSave():
        newSave = open(mainSaveFile,'r').read()
        currentDifficulty=re.findall("	{difficulty.+",newSave)
        currentDifficultyText = currentDifficulty[0].replace("	{difficulty ", "").strip()
        fogOfWarIn = re.findall("	{fogofwar .+",newSave)
        fogOfWarText = fogOfWarIn[0].replace("	{fogofwar ", "").strip()
        
        
        print(fogOfWarText)
 
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

        mpInSaveInt = re.findall("\{mp \d+",newSave)
        mpInSave = mpInSaveInt[0].replace("{mp ", "").strip()
        #test2 = test.strip('mp')
        print(mpInSave)
        rpInSaveInt = re.findall('\{rp+ \d+', newSave)
        rpInSave = rpInSaveInt[0].replace("{rp ", "").strip()
        print(rpInSave)
        apInSaveInt = re.findall('\{ap+ \d+', newSave)
        apInSave = apInSaveInt[0].replace("{ap ", "").strip()
        print(apInSave)
        spInSaveInt = re.findall('\{sp+ \d+', newSave)
        spInSave = spInSaveInt[0].replace("{sp ", "").strip()
        print(spInSave)

        showSP.set(spInSave)
        showAP.set(apInSave)
        showMP.set(mpInSave)
        showRP.set(rpInSave)

        modsActivated = re.findall("		\"mod_.+", newSave)
       
        #for mod in modsActivated:
        #    mod = mod.replace('		"mod_','')
        print(modsActivated)    
            
        allMods=modsActivated
        eachMod=StringVar(value=allMods)
        modsActiveLabel = Label(edit_window, text='Mods Active')
        modsActiveLabel.grid(row=18, column=1)
        modList=Listbox(edit_window,height=7,listvariable=eachMod)
        modList.grid(row=19,column=1)
        modList.config(width=40)
        
        def deleteMod():
            deleteThis=modList.curselection()
            modList.delete(deleteThis)
            #modsActivated.(deleteThis,'')
        def checkMod():
            checkThis=modList.curselection()
            checkThistoo=modList.get(checkThis)
            checkThistoo=checkThistoo.replace('\"mod_','').strip()
            checkThistoo=checkThistoo.replace(':0"','').strip()
            webbrowser.open_new('https://steamcommunity.com/sharedfiles/filedetails/?id='+checkThistoo)
            #checkThis=checkThis.replace('\"mod_','')
            print(checkThistoo)
            
        
        checkWorkshopButton = Button(edit_window, text='Mod Steam Page',command=checkMod)
        checkWorkshopButton.grid(row=19,column=2)
        deleteModButton = Button (edit_window,text='Delete mod',command=deleteMod)
        deleteModButton.grid(row=19,column=3)
            
        
        mapsActive = re.findall("			\{map \"multi/.+", newSave)
        print(mapsActive)
        
        
        
        maps = ('dcg_a_kalinin','dcg_a_runway','dcg_battleofhungary_f','dcg_brozha_f','dcg_courtyard_d','dcg_d_uran','dcg_d_vyazma','dcg_dubovka','dcg_f_barrikady','dcg_f_bridges_of_lysovo','dcg_f_bykovo','dcg_f_factory','dcg_f_hillswood','dcg_f_lazurnyi','dcg_f_oeadland','dcg_firearc_d','dcg_frontier_d','dcg_gelid_w','dcg_glushkovo','dcg_hanhijarvi','dcg_hanhijarvi_winter','dcg_hills','dcg_hilltop','dcg_karvola','dcg_karvola_winter','dcg_kirjavala','dcg_kirjavala_winter','dcg_kirkenes_airfield','dcg_kursk_f','dcg_kylmapuro','dcg_kylmapuro_winter','dcg_kymhi_airfield','dcg_kymhi_airfield_winter','dcg_laisniemi'
            ,'dcg_laisniemi_winter','dcg_lakhta','dcg_lakhta_winter','dcg_mannerheim','dcg_mikli','dcg_mikli_winter','dcg_narofominsk','dcg_natramala','dcg_natramala_winter','dcg_niemen','dcg_pinsk','dcg_puhoksen','dcg_puhoksen_winter','dcg_radekhiv','dcg_raseiniai','dcg_rasputitsa','dcg_ruetzen','dcg_rzhev','dcg_shiryayevo','dcg_suburbs_d','dcg_tikhvin_w','dcg_tormasenvaara','dcg_vainikalan','dcg_vainikalan_winter','dcg_velikiyeluki','dcg_vitebsk_d','dcg_warfare3','dcg_winterstorm_w','dcg_ziborovo_f','defenseonly/dcg_d_guglovo_defense','defenseonly/dcg_d_hill_defense_defense','defenseonly/dcg_d_kursk_defense','defenseonly/dcg_d_weissenberg_defense','defenseonly/dcg_f_battle_of_rschew_defense','defenseonly/dcg_f_battleofcologne_defense','defenseonly/dcg_f_endlesswardefense_needsrefining','defenseonly/dcg_f_field_defense_map_defense','defenseonly/dcg_f_gr.dubrauneedsrefiningdefense','defenseonly/dcg_f_westlands_defense',
            'defenseonly/dcg_w_citadel_defense','defenseonly/dcg_w_stalingrad_defense','defenseonly/dcg_w_easternfrontdefense_defense','defenseonly/dcg_w_field_defense_snow_defense','defenseonly/dcg_w_hill_defense_defense','noaireinforcements/dcg_d_kursk_noreinforcements','noaireinforcements/dcg_d_hill_defense_noreinforcements','noaireinforcements/dcg_d_weissenberg_noreinforcements','noaireinforcements/dcg_f_battle_of_rschew_noreinforcements','noaireinforcements/dcg_f_battleofcologne_noreinforcements','noaireinforcements/dcg_f_endlesswardefense_noreinforcements','noaireinforcements/dcg_f_field_defense_map_noreinforcements','noaireinforcements/dcg_f_gr.dubrauneedsrefiningnoreinforcements','noaireinforcements/dcg_w_citadel_noreinforcements','noaireinforcements/dcg_w_field_defense_snow_noreinforcements','noaireinforcements/dcg_w_hill_defense_noreinforcements','noaireinforcements/dcg_w_stalingrad_noreinforcements',
            'earlymaps/dcg_brozha_f_early','earlymaps/dcg_d_uran_early','earlymaps/dcg_d_vyazma_early','earlymaps/dcg_dubovka_early','earlymaps/dcg_frontier_d_early','earlymaps/dcg_narofominsk_early','earlymaps/dcg_niemen_early','earlymaps/dcg_pinsk_early','earlymaps/dcg_rasputitsa_early','earlymaps/dcg_shiryayevo_early','earlymaps/dcg_ziborovo_f_early')
        
        # mapChange1 = ttk.Combobox(edit_window,values=maps)
        # mapChange.grid(row=11,column=2) 
        # mapChange.config(width=50, height=10)
        # mapChange.state(["readonly"])
        
        # mapChange2 = ttk.Combobox(edit_window,values=maps)
        # mapChange2.grid(row=12,column=2) 
        # mapChange2.config(width=50, height=10)
        # mapChange2.state(["readonly"])
        
        # mapChange3 = ttk.Combobox(edit_window,values=maps)
        # mapChange3.grid(row=13,column=2) 
        # mapChange3.config(width=50, height=10)
        # mapChange3.state(["readonly"])
        
        # mapChange4 = ttk.Combobox(edit_window,values=maps)
        # mapChange4.grid(row=14,column=2) 
        # mapChange4.config(width=50, height=10)
        # mapChange4.state(["readonly"])
        
        # mapChange5 = ttk.Combobox(edit_window,values=maps)
        # mapChange5.grid(row=15,column=2) 
        # mapChange5.config(width=50, height=10)
        # mapChange5.state(["readonly"])
        
        mapChangeList = []
        count = 0
        for map in mapsActive:
            map = map.replace('                        {map "multi','').strip()
            map = map.replace('{map "multi/','')
            map = map.replace(':campaign_capture_the_flag:4x4"}','')
            mapShow = Label(edit_window, text=map)
            mapShow.grid(row=11+count,column=1)
            
            mapChange = ttk.Combobox(edit_window,values=maps)
            mapChange.current(maps.index(str(map)))
            mapChange.grid(row=11+count,column=2) 
            mapChange.config(width=50, height=10)
            mapChange.state(["readonly"])
            mapChangeList.append(mapChange)
            count = count+1
            print(map)
            #print(name)
            
            #print(mapChange.current())
            #print(mapChange.get(1))
        
        #print(mapChangeList[0].get())
        #print(mapChangeList[1].get())
        #print(mapChangeList[2].get())
        #print(mapChangeList[3].get())
        #print(mapChangeList[4].get())        
        #print(mapChangeList)   
         
       # print(mapChange1.current())
       # print(mapChange2.get())
       # print(mapChange3.get())
       # print(mapChange4.get())
       # print(mapChange5.get())
        edit_window.protocol("WM_DELETE_WINDOW", on_closing)
        
        def savechanges():
            #newSaveFile = open(mainSaveFile,'w')
            
            #tempFile = (newSave.replace(mpInSave,showMP.get()))
            
            #newSaveFile.write(tempFile)
            
            newSaveFile = open(mainSaveFile, "w")
            

            newFile = (newSave.replace(f'mp {mpInSave}' ,f'mp {showMP.get()}'))
            newFile = (newFile.replace(f'sp {spInSave}',f'sp {showSP.get()}'))
            newFile = (newFile.replace(f'rp {rpInSave}',f'rp {showRP.get()}'))
            newFile = (newFile.replace(f'ap {apInSave}',f'ap {showAP.get()}'))

            if fogOfWar.get() == 1:
                newFile = newFile.replace(fogOfWarText,'fog_realistic}')
            elif fogOfWar.get() == 2:
                newFile = newFile.replace(fogOfWarText,'fog_off}')
                
            if difficultyLevel.get() == 1:
                newFile = newFile.replace(currentDifficultyText,'easy}')
            if difficultyLevel.get() == 2:
                newFile = newFile.replace(currentDifficultyText,'normal}')
            if difficultyLevel.get() == 3:
                newFile = newFile.replace(currentDifficultyText,'hard}')
            if difficultyLevel.get() == 4:
                newFile = newFile.replace(currentDifficultyText,'heroic}')
            mapCount = 0    
            for mapNew in mapsActive:
                print(mapNew)
                print(mapChangeList[mapCount].get())
                
                newFile = newFile.replace(f'{mapNew}',f'			{{map "multi/{mapChangeList[mapCount].get()}:campaign_capture_the_flag:4x4"}}')
                mapCount = mapCount+1
                #newFile = newFile.replace(f'			{{map "multi/{map(0+mapCount)}:campaign_capture_the_flag:4x4"}}',f'			\{{map "multi/{mapnew}:campaign_capture_the_flag:4x4"}}')
               
                #print(mapChange.get())
                #mapCount = mapCount+1 
           # newFile =(newFile.replace(f'{modsActivated[0]}','		"mod_2888964832:0"'))
            
            #print(modsActivated)
            #for mod in modsActivated:
            #    newFile =(newFile.replace(mod,modList.get(0+count)))
            countMods = 0
                        
            #print(str(mapChange.current(0)))
            #print(mapChange.current(1))
            for mod in modsActivated:
                newFile =(newFile.replace(f'{mod}',f'{modList.get(countMods)}'))
                #print(modList.get(countMods))
                #print(modList.get(0+count))
                
                countMods = countMods + 1
            
           
            
            
            newSaveFile.write(newFile)
            newSaveFile.close()
            new_save=zipfile.ZipFile(save,'w')
            
            
            new_save.write(secondarySaveFile)
            new_save.write(mainSaveFile)
            
            
            messagebox.showinfo("Saved", "Save edited")
           
            edit_window.destroy()
            root.destroy()
           
                
           
        saveButton=Button(edit_window,text='Save changes',command=savechanges)
        saveButton.grid(row=20,column=2)

    scanSave()


    edit_window.protocol("WM_DELETE_WINDOW", remergeMain)
   
def infoText():
    messagebox.showinfo('help','MAKE A BACKUP of the save before using the programm! Disable Steam cloud. Do not use it if you\'re afraid to break a save(shouldn\'t happen with a back up). This programm has also DLC and Conquest Enhanced maps. DO NOT CHANGE TO DLC maps if you don\'t have DLC and to CE maps if you don\'t have CE activated and don\'t know what they do, you will break your save. Click on mod and "Mod steam page" to go to this mod workshop page.')

workButton = Button(root,text='Choose your save', command=openfile)
workButton.grid(row=2,column=1)

workButton = Button(root,text='Read this info', command=infoText)
workButton.grid(row=2,column=2)

def on_closing():
        try:
            os.remove(mainSaveFile)
            os.remove(secondarySaveFile)
            root.destroy()
        except FileNotFoundError:
            root.destroy()
            


#edit_window.protocol("WM_DELETE_WINDOW", on_closingRoot)
root.mainloop()

#save = filedialog.askopenfile(mode='r',initialdir="/", title="Select your save",filetypes=[('save files',"*.sav")])

#saved = zipfile.ZipFile(save, 'r')

#myLabel= Label(root, text=save).pack()

#d = save.namelist()
#print(d)







#import zipfile
#s = zipfile.ZipFile('test.zip', 'w')
#s.write('foods.py')