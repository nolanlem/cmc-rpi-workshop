# cmc-rpi-workshop
Code repo for Columbia computer music center raspberry pi workshop nov 2024


# terminal commands we will use <br>
Computer has directory structure, which are just folders in folders etc. <br>
*where are you  currently in the file directory 
*'pwd' = print working directory 
*‘ls’ = list files 
'ls *.wav' = list all .wav files 
'ls *.pdf' = list all pdf files in 
‘man ls’ = open manual for 'ls' command 
‘mkdir mydir’ = make a new directory called 'mydir'

Move around file directory: 
‘cd’ = change directory, ‘cd ../’ = go back, ‘cd myfolder’ = move into ‘myfolder’
Let’s create a folder to hold our programs. 
'touch myfile.txt' = create a file called myfile.txt
'nano myfile.txt' = open myfile.txt in the nano code editor in terminal 

# adding libraries 
(open terminal window )
sudo apt-get update 
sudo apg-get -y install python-rpi.gpio
sudo pip3 install pygame 


