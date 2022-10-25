### KSW_2022_Fall_Program

# 🚀Gesture Controlled Drone by TEAM GANGSTURE🚀

📑 *Project Title*
        
    Using deep learning vision technology to control drone dynamic motions

📅 *Project Period*

    09-05-2022(MON) ~ 12-19-2022(MON)

🧖🏻‍♀️ *Problem Statement*
    
    Unmanned Aerial Vehicles are becoming more important in various industries. 
    Controlling the drone requires professional training because of its controller 
    and it makes using the drone more challenging.
    This project aims to make controlling the drone easy without using 
    the physical hand-held remote controller. 
    Therefore, the drone does not need to use as many resources.

📖 *Considerations*

	🚁 Software
	- Develop own classifier to control the drone
	- Develop the drone code to control by classifier
	- Link between the drone and iOS application in real-time   

	🚁 Hardware
	- Change the system that we use to do deep learning

💡 *Novelty*

  	1. No extra sensors or deivces are needed to controll drone
    2. Use dataset which we made ourselves for traing model 
    3. Use iOS platform to monitor the video which drone seeing

🏛 *System Overview*
 <p align="center">
   <img src="https://user-images.githubusercontent.com/51031771/196214789-31eee8f2-81f9-43ee-b53e-b5c5d5bb4820.png" width="600" alt="Image Error"/>
</p>
    
  1. The iOS application takes a gesture video.
  2. The application changes the gesture to command signal with AI classification model and send it to the drone in real-time.
  3. When the drone gets the signal, it moves and takes a video what the drone is watching.
  4. The drone sends the streaming video to iOS application and the video is shown in the application.
  5. The drone sends the video to server to save it.

  
🖥️ *Environment Setting*
    
    ✔️Python version 3.9.7 
    
    ✔️Media Pipe  0.8.11
    
    ✔️Xcode  13.4.1
    
  
📤 *Installation*

    $ git clone [github link]
    $ cd [directory]

👨‍👩‍👧‍👧 *Collaborator*
     
    🐬Hyeongbin Park
    	- Kwangwoon Univeristy
    	- Major in Information Convergence
    	- idolphin.kr@gmail.com
    	- https://github.com/iDolphin99
       
    🐢Yujin Lee
    	- Kwangwoon University
    	- Major in Software
    	- yj587878@gmail.com
    	- https://github.com/yujinnee
      
    🧂Soeun Lee
    	- Jeju National University
    	- Major in Computer Science and Statistics
    	- so5eun.lee@gmail.com
    	-https://github.com/Lee-soeun
       
    🌊Seunghwan Kim
    	- Jeju National University
    	- Major in Big Data Convergence
    	- hwan.is.ocean@gmail.com
    	- https://github.com/oshunKim
	    
    🐰Xinning Bai
    	- Purdue University
    	- Major in CNIT
    	- xinningbai@gmail.com
    	- https://github.com/Lizwhite8
    
    🍕Jake Hazelton
    	-Purdue University
    	-Major in CNIT
    	-jake36268@gmail.com
    	-https://github.com/thehazeman
  
