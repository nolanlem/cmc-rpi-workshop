# cmc-rpi-workshop
Code repo for Columbia computer music center raspberry pi workshop nov 2024


# terminal commands we will use <br>
Computer has directory structure, which are just folders in folders etc. <br>
- where are you currently in your computer file/directory wise 
- 'pwd' = print working directory 
- ‘ls’ = list (all) files 
- 'ls *.wav' = list all .wav files in current working directory, '*' is wildcard
- 'ls *.pdf' = list all pdf files in current working directory
- ‘man ls’ = open manual for 'ls' command 
- ‘mkdir mydir’ = make a new directory in current directory called 'mydir'

Move around file directory: 
- ‘cd’ = change directory, ‘cd ../’ = go back, ‘cd myfolder’ = move into ‘myfolder’
- Let’s create a folder to hold our programs. 
- 'touch myfile.txt' = create a file called myfile.txt
- 'nano myfile.txt' = open myfile.txt in the nano code editor in terminal 

# adding libraries 
- (open terminal window )
```
sudo apt-get update 
sudo apt-get -y install python-rpi.gpio
sudo pip3 install pygame
```


