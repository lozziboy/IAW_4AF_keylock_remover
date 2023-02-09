# Magneti Marelli IAW 4AF keylock (immobilizer) remover
**step-by-step method to remove keylock (immobilizer) for ECU Magneti Marelli IAW 4AF by reprogramming EEPROM 95160**
      
___
* Required tools:
	   
   * a Windows pc
   
   * soldering iron
	   
   * arduino uno r3
   
      
___
* Required software:
	   
   * Arduino IDE
	   
   * Pyton and Pyserial
   
   * PonyProgV117h
   
___
* Step 1: install Arduino IDE  

     https://www.arduino.cc/en/software
   
___
* Step 2: install and configure Pyton and Pyserial  
	   
   * install pyton  

     https://www.python.org/getit/
   
   * find the folder where the installed `pyton.exe` is located, it could be in one of the two following places  
     `C:\Python311`
     
     `C:\Users\(your login user)\AppData\Local\Programs\Python\Python311`
 
   *  add pyton to the program runnable from command line, to do that:
     Control Panel -> System -> Edit system environment variables -> Press button "Environment variables"
     Select "Path" entry and click button "Edit"
     Click on "New" and paste the path of the folder where phyton.exe is located
    
    ![Example](https://github.com/lozziboy/IAW_4AF_keylock_remover/blob/main/docs/environment_variable.PNG) 
     
