#!c:/python33/python.exe
import sys
import math


from decimal import *
from tkinter import *
from tkinter import ttk

getcontext().prec = 3

def calculate(*args):
    try:
        mode = (calculate_mode.get())
        
        powerloss = result_output_var_objects['powerloss'].get()
        speedloss_gesamt  = result_output_var_objects['speedloss_gesamt'].get()

        windspeed = weather_input_var_objects['windspeed'].get()
        direction = weather_input_var_objects['direction'].get()
      
        beaufort = weather_output_var_objects['beaufort'].get()

        lpp 	     = ship_input_var_objects['lpp'].get()
        breite 	 	 = ship_input_var_objects['breite'].get()
        tiefgang 	 = ship_input_var_objects['tiefgang'].get()
        verdraengung = ship_input_var_objects['verdraengung'].get()
        power 		 = ship_input_var_objects['power'].get()
        speed 		 = ship_input_var_objects['speed'].get() * 0.5144 ### Umrechung kn in m/s ###
       
        cb 			 = ship_output_var_objects['cb'].get()
        froude 		 = ship_output_var_objects['froude'].get()


        if mode != 'Tanker beladen' and mode != 'Tanker mit Ballastwasser' and mode != 'Containerschiff':
            log.set("Fehler! Bitte einen Schiffstyp auswählen!")
            return

        if (lpp>0):
            if(breite>0):
                if(tiefgang>0):
                    if(verdraengung>0):
                        cb = (verdraengung/(lpp*breite*tiefgang))
                        ship_output_var_objects['cb'].set(cb)
                    else:
                        log.set("Verdraengung muss größer 0 sein!")
                        return
                else:
                    log.set("Tiefgang muss größer 0 sein!")
                    return
            else:
                log.set("Breite muss größer 0 sein!")
                return
        else:
            log.set("Lpp muss größer 0 sein!")
            return
        
        
        if (cb>=0.55):
            if(cb>0.70 and mode != 'Containerschiff'):
                if(cb>0.85):
                    log.set('Bitte Parameter anpassen! \n\
                        Der berechnete cd ist > 0.85 ! \n\
                        Der cb Wert liegt damit außerhalb\n\
                        eines sinnvollen Wertebreichs\n für ein ' + str(mode))
                    return

                elif (cb <= 0.75 and mode != 'Containerschiff'):
                    log.set('Bitte Parameter anpassen! \n\
                        Der berechnete cd ist < 0.75 ! \n\
                        Der cb Wert liegt damit außerhalb\n\
                        eines sinnvollen Wertebreichs\n für ein ' + str(mode))
                    return
            else:
                pass
        else:
            log.set('Bitte Parameter anpassen! \n\
                Der berechnete cd ist < 0.55 ! \n\
                Der cb Wert liegt damit außerhalb\n\
                eines sinnvollen Wertebreichs\n für ein ' + str(mode))
            return

    #### Berechnung Parameter ######

        if speed > 0:
            froude = (speed)/((9.81*lpp)**0.5)
            ship_output_var_objects['froude'].set(froude)
        else:
            log.set("Geschwindigkeit muss größer 0 sein!")
            return

        if windspeed > 0:
            beaufort = (windspeed/0.836)**(2/3)
            weather_output_var_objects['beaufort'].set(beaufort)
        else:
            log.set("Windgeschwindigkeit muss größer 0 sein!")
            return

    #### Geschwindigkeitsverlust durch Wind von vorne ###############

        if speed > 0:
            if (cb >= 0.55) and (cb <= 0.7):
                if mode == 'Containerschiff':
                    speedloss = (0.7*beaufort+((beaufort**(6.5))/(22*(verdraengung**(2/3)))))                  
                else:
                    log.set("Fehler! cb darf nur beim Containerschiff zwischen 0.55 und 0.70 liegen")
                    return
            elif (cb >= 0.75) and (cb <= 0.85):
                if mode == 'Tanker beladen':
                    speedloss = (0.5*beaufort+((beaufort**(6.5))/(2.7*(verdraengung**(2/3)))))
                    
                elif mode == 'Tanker mit Ballastwasser':
                    speedloss = (0.7*beaufort+((beaufort**(6.5))/(2.7*(verdraengung**(2/3)))))
                    
                elif mode == 'Containerschiff':
                    log.set("Fehler! cb darf nur beim Containerschiff zwischen 0.55 und 0.70  liegen")
                    return
            else:
                log.set("Warnung! Der Berechnete cb ist kleiner < 0,75 oder größer > 0.85 cb: "+str(cb))
                return
        else:
            log.set("Fehler! Geschwindigkeit muss größer 0 sein")
            return

        #print ("Test speed= " +str(speed))
                   
    ###### Berechnung n ###########

        n=0 

        if mode == 'Tanker beladen':
            n = 1.91

        elif mode == 'Tanker mit Ballastwasser':
            n = 2.40
            
        elif mode == 'Containerschiff':
            n = 2.16
            
        else:
            log.set("Fehler! Bitte Schiffstyp auswählen")
            return

    ####### Berechnung alpha #################

        alpha = 0
        if (cb >= 0.55) and (cb < 0.6):
            alpha = 1.7 - 1.4 * froude - 7.4 * froude**2
        elif (cb >= 0.6) and (cb < 0.65):
            alpha = 2.2 - 2.5 * froude - 9.7 * froude**2
        elif (cb >= 0.65) and (cb < 0.7):
            alpha = 2.6 - 3.7 * froude - 11.6 * froude**2
        elif (cb >= 0.7) and (cb < 0.75):
            alpha = 3.1 - 5.3 * froude - 12.4 * froude**2
        elif (cb >= 0.75) and (cb < 0.8) and mode == 'Tanker mit Ballastwasser':
            alpha = 2.6 - 12.5 * froude - 13.5 * froude**2    
        elif (cb >= 0.8) and (cb < 0.85) and mode == 'Tanker mit Ballastwasser':
            alpha = 3.0 - 16.3 * froude - 21.6 * froude**2
        elif (cb >= 0.75) and (cb < 0.8):
            alpha = 2.4 - 10.6 * froude - 9.5 * froude**2
        elif (cb >= 0.8) and (cb < 0.85):
            alpha = 2.6 - 13.1 * froude - 15.1 * froude**2
        elif (cb >= 0.85) and mode == 'Tanker mit Ballastwasser':
            alpha = 3.4 - 20.9 * froude + 31.8 * froude**2
        elif (cb >= 0.85):
            alpha = 3.1 - 18.7 * froude + 28 * froude**2
        else:
            log.set("Fehler! bei dem Korrekturwert alpha")

        #print ("Test alpha = " +str(alpha))

        if (alpha<=0):
            log.set("Fehler! bei dem Korrekturwert alpha. Bitte Froudezahl überprüfen!")
            return

    ####### Berechnung my ####################

        my = 0
        
        if (direction >= 30) and (direction <= 60):
            my = (1.7 - 0.03 * (beaufort - 4)**2)/2
            speedloss_gesamt = alpha * my * speedloss
        elif (direction >= 60) and (direction <= 150):
            my = (0.9 - 0.06 * (beaufort - 6)**2)/2
            speedloss_gesamt = alpha * my * speedloss
        elif (direction >= 150) and (direction <= 180):
            my = (0.4 - 0.03 * (beaufort - 8)**2)/2
            speedloss_gesamt = alpha * my * speedloss
        elif (direction >= 180):
            log.set("Info! Windrichtung bitte zwischen 0 und 180 eingeben")
            return
        else:
            speedloss_gesamt = alpha * speedloss
            log.set("Info! Wind kommt von Vorn")
            

        #print ("Test my = " +str(my))
        #print ("Test speedloss = " +str(speedloss))
        #print ("Test speedloss_gesamt = " +str(speedloss_gesamt))


    ####### Berechung wirklicher Geschwindigkeitsverlust ########
        
        result_output_var_objects['speedloss_gesamt'].set(speedloss_gesamt)


    ####### Berechnung Leistungsverlust ##########

        powerloss = 0

        if (power>0):
            powerloss = ((n+1)*(speedloss_gesamt))
            powerloss = (powerloss)
            result_output_var_objects['powerloss'].set(powerloss)
            
        else:
            log.set("Fehler! die Leistung muss größer 0 sein")
            return

        print ("Test powerloss= " +str(powerloss))
        

    ############### Berechnung ENDE ################################

        log.set("Die berechneten Parameter für " +str(mode))

    except ValueError:
        log.set("Fehler! Bitte Eingabe überprüfen")


       


def generateLabels(labels_dict, start_row=1, colum_in=3):
	count = start_row
	for l in labels_dict:
		ttk.Label(mainframe, text=l).grid(column=colum_in, row=count, sticky=W)
		count=count+1

def generateFeet_Input(labels_dict, var_objects, result, start_row=1, in_column=4):
	count = start_row
	for l in labels_dict:
		result[l] = ttk.Entry(mainframe, width=7, textvariable=var_objects[l])
		result[l].grid(column=in_column, row=count, sticky=(W, E))
		count=count+1

def generateFeet_Output(labels_dict, result):
	count = 1
	for l in labels_dict:
		result[l] = ttk.Entry(mainframe, width=5, textvariable=l)
		#result[l].grid(column=2, row=count, sticky=(W, E))
	return result

def generateVar(var_labels, var_container):
	for l in var_labels:
		var_container[l] = DoubleVar()

def switch_mode(val):
	calculate_mode = val
	print (val)


############ Generate labes and input felds ##############################

calculate_mode = None

ship_input_labels = ['Lpp in [m]:', 'Breite in [m]:', 'Tiefgang in [m]:', 'Verdrängung in [m³]:', 'Leistung in [kW]:', 'Geschwindigkeit in [kn]:'] 
ship_output_labels = ['Cb:', 'Froude:']

weather_input_labels = ['Windgeschwindigkeit in [m/s]:', 'Windrichtung zum Schiff in [Grad]:']
weather_output_labels = ['Beaufort-Skala:']

result_output_labels = ['gesamter Geschw.verlust [%]:','Verlust an Leistung in [%]:']

############ definition of input and output variable ######################

ship_input_variables =['lpp','breite','tiefgang','verdraengung','power','speed']
ship_output_variables =['cb', 'froude']

weather_input_variables =['windspeed','direction']
weather_output_variables = ['beaufort']

result_output_variables = ['speedloss_gesamt','powerloss']

############ object container for input and outputs #######################



### Feld Objekte unwichtig
weather_input_objects = {}
weather_output_objects = {}
ship_input_objects = {}
ship_output_objects = {}
result_output_objects = {}


### Variablen der felder input ist rechts und output links
weather_input_var_objects = {}
weather_output_var_objects = {}

ship_input_var_objects = {}
ship_output_var_objects = {}

### output ergebnisse links
result_output_var_objects = {}

############ Build App ####################

root = Tk()
root.title("Widerstandsberechnung")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


###### Define Dropdown
calculate_mode = StringVar(mainframe)
# initial value
choices = ['Bitte Schiffstyp wählen:', 'Tanker mit Ballastwasser', 'Tanker beladen', 'Containerschiff']

ttk.Label(mainframe, text='Eingabeparameter:').grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text='Ausgabeparameter:').grid(column=5, row=1, sticky=W)
ttk.Label(mainframe, text='Schiff Parameter:').grid(column=3, row=2, sticky=W)
ttk.OptionMenu(mainframe, calculate_mode, *choices).grid(column=3, row=3, sticky=W)


generateVar(ship_input_variables, ship_input_var_objects)
generateLabels(ship_input_labels, 4)
generateFeet_Input(ship_input_variables,ship_input_var_objects,ship_input_objects, 4)

generateVar(ship_output_variables, ship_output_var_objects)
generateLabels(ship_output_labels, 4 , 5)
generateFeet_Input(ship_output_variables,ship_output_var_objects,ship_output_objects, 4, 6)

ttk.Label(mainframe, text='Parameter Wetter:').grid(column=3, row=10, sticky=W)

generateVar(weather_input_variables, weather_input_var_objects)
generateLabels(weather_input_labels, 11)
generateFeet_Input(weather_input_variables,weather_input_var_objects,weather_input_objects, 11)

generateVar(weather_output_variables, weather_output_var_objects)
generateLabels(weather_output_labels, 11, 5)
generateFeet_Input(weather_output_variables,weather_output_var_objects,weather_output_objects, 11 , 6)

ttk.Label(mainframe, text='Ergebnis:').grid(column=3, row=13, sticky=W)

generateVar(result_output_variables, result_output_var_objects)
generateLabels(result_output_labels, 14)
generateFeet_Input(result_output_variables,result_output_var_objects,result_output_objects, 14)

#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

log = StringVar(mainframe)
ttk.Label(mainframe, textvariable=log).grid(column=3, row=16, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=17, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
