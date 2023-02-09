# Magneti Marelli IAW 4AF keylock (immobilizer) remover
**step-by-step method to remove keylock (immobilizer) for ECU Magneti Marelli IAW 4AF by reprogramming EEPROM 95160**
      
___
* Required tools:
	   
   * a Windows pc
 
   * Arduino uno r3, or its chinese clone
   <img src="https://github.com/lozziboy/IAW_4AF_keylock_remover/blob/main/images/arduino_china.png" width="250">
   
   * SOP8 clamp
   <img src="https://github.com/lozziboy/IAW_4AF_keylock_remover/blob/main/images/sop8%20clamp.png" width="400">

   
      
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
 
   *  add pyton to the program runnable from command line:  
     `Control Panel -> System -> Edit system environment variables -> Press button "Environment variables"`  
     `Select "Path" entry and click button "Edit"`  
     `Click on "New" and paste the path of the folder where phyton.exe is located`  
    
    ![Example](https://github.com/lozziboy/IAW_4AF_keylock_remover/blob/main/images/environment_variable.png)
    
   * install 7zip   
     https://www.7-zip.org/download.html
     
   * download pyserial.tar.gz and uncompress it locally using 7zip   
     https://pypi.org/project/pyserial/
     
   * install pyserial using windows terminal  
     `cd C:\Users\(your login user)\Downloads\pyserial-3.5.tar\dist\pyserial-3.5`   
     `python setup.py install`
     
___
* Step 3: prepare arduino for eeprom 95160 programming
	   
   * download arduino sketch (EEPROG.ino) to dump/write/erase eeprom 95160   
    https://github.com/cedricp/Arduino-95160
    
    * connect Arduino uno3 to the serial usb of the pc and use software Arduino IDE upload EEPROG.ino to an Arduino uno r3   

___
* Step 4: wire eeprom 95160 to Arduino
	   
   * open ECU IAW 4AF, locate eeprom 95160 and hook it with the SOP8 clamp   
	   <img src="https://github.com/lozziboy/IAW_4AF_keylock_remover/blob/main/images/SPI95160_pos.png" width="300">
	   
   * wire eeprom 95160 to Arduino, accordingly with the following connections   
     `chip select (s) = 9`    
     `serial data input (d) = 10`        
     `serial data output (q) = 11`        
     `serial clock (c) = 12`       
     `write protect (w) = 13`       
     `hold (h) = 8`        
     `Vcc = 3.3v`       
     `Vss = GND`       
 	   <img src="https://github.com/lozziboy/IAW_4AF_keylock_remover/blob/main/images/wiring%2095160.png" width="600">    
	   	   
___
* Step 5: download pyton scripts to manage eeprom 95160   
   https://github.com/cedricp/Arduino-95160/tree/master/tools

___
* Step 6: dump the eeprom 95160 content
	   
   * open Windows terminal   
   * locate to pyton scripts folder    
     `cd C:\Users\(your login user)\......\pyton scripts\`
   * use pyton script `dump_eeprom.py` to dump the eeprom content in a local file   
     `dump_eeprom.py [comport] [filename]`	   	   

___
* Step 7: edit the local file to remove immobilizer
   
   * install PonyProgV117h    
   http://www.lancos.com/ppwin95.html    
   
   * open PonyProgV117h and set the following options    
     `chip 2402-16`    
     `Edit->Edit buffer enabled`    
   
   * open the file with the eeprom data dump and edit the following bytes    
	   <img src="https://github.com/lozziboy/IAW_4AF_keylock_remover/blob/main/images/immo off.png" width="800">
	   
   * save the file
___
* Step 8: write the 95160 eeprom
   
   * open Windows terminal   
   * locate to pyton scripts folder    
     `cd C:\Users\(your login user)\......\pyton scripts\`
   * use pyton script `write_eeprom.py` to write the eeprom with the content in the modified local file   
     `write_eeprom.py [comport] [filename]`	

