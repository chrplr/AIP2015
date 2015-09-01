**Course 00: Software Installation** Wednesday September 2 2015
============================================================

Objectives
----------

Each student should end up with a bundle of softwares which are needed in the
mandatory courses of the Cogmaster.

You migh skip the last one if and only if you are already used to an advanced
text editor as wim, emacs, sublimetext. Microsoft Office Word, LibreOffice and
other document formatting software are
**not** text editors.

Important notes
---------------

The **only** slot in the schedule dedicated to installation of softwares is on
Wednesday 2 September from 9:00 to 12:00. We will **not** answer installation
questions during the following AIP lectures. We will not try to solve your
problems if you were not attending on Wednesday morning. If you don't have a
computer yet, tell us after the AIP presentation on Monday 31 August.

Backup your computer on monday evening.

Installation procedures are currently being tested on Windows (7 64bits), MacOS
(10.9 Maverick), and debian-based linux. We have have few years of experience with installations on various Operating System versions, but there is always some computers on which the usual procedures and fixes fail. We will try our best, if it happens to you, please be patient.

Some installations will require an internet access, thus don't forget to
bring your login and password for the ENS wifi on wednesday morning.

Installation procedures will be put online on Tuesday. Links will be provided to download the installation files from the internet. Try much as possible to downloaded on your computer Tuesday evening: it will save us some time on Wednesday morning because the network at the ENS is usually slow and we will have only few USB sticks with the softwares.

If you are using a debian-based Linux such as Ubuntu, most of the installations will be made with apt, it is way safer to try the installation at your home if you have a decent internet connection than Wednesday at the ENS.

20:30
The instruction to install python on Windows and Mac will be posted a bit later this evening


First, read the installation instruction for your operating system:  
[Linux](#linux-debian-based)  
[Mac OS](#mac-os)  
[windows](#windows)

Follow carefully the instructions. If something does not work as expected, stop there and ask for our help. It is much easier to prevent a misinstallation than to repare it.

Once the installation on your computer completed, you can browse the documents in [the ressource folder](../resources/)


## Windows

### Scratch
1. Download [ScratchInstaller1.4.exe](http://download.scratch.mit.edu/ScratchInstaller1.4.exe) from http://download.scratch.mit.edu/ by using the right click on the link and the option `Save target as`, and select an appropriate directory, for example the default `Downloads` folder.
2. then install as usual:
 * upon the end of the download either click on `Open the Folder` or open an explorer (windows key + e) and go to your `Downloads` folder
 * double-click on the ScratchInstaller1.4.exe file and wait
 * after a while your screen turns dark and an ominous warning pop-up window ask you if you'd like this unknown programm to modify stuff on your computer. Click on the `Yes` button.
 * The Scratch Setup Wizard window should pop-up and you can install the software clicking on the `Next` Button and accepting default parameters (note in which directory the program will be installed) until you have to click on the `Finish` button.
3. test Scratch
 * If you did not uncheck the options before clicking on `Finish`, you should see the program running and you coud reopen it using the desktop Scratch icon. Alternatively, you can open an explorer, go to the directory in which the program was installed and double click on the Scratch icon.
 * you should be able to move the little animal around

### Atom

1. Download the Atom installer by clicking on the big red `Download Windows Installer` button on [http://atom.io]

2. Install as usual

3. Enjoy!


### R and Rstudio

1. Downloads
 * [ ] Download [the lattest RStudio-0.XX.XXX.exe](https://download1.rstudio.org/RStudio-0.99.473.exe) from [https://www.rstudio.com/products/rstudio/download/]
 * [ ] Download [the lattest R package installer](https://cran.r-project.org/bin/windows/base/R-3.2.2-win.exe) from [https://cran.r-project.org/bin/windows/base/]

2. Installation

 * [ ] Install R by double-clicking on the downloaded file and following the steps on the typical Windows installer pop-up window (usually you just have to clic on the `Next` button).  
 * [ ] Then install RStudio by double-clicking on the downloaded file. It should be straight forward.

3. Verification
 * [ ] Launch RStudio from the icon on your desktop
 * [ ] in the command window, type 'demo(graphics)'


### Git

0. Set up an account on Github.com
 * [ ] Open an internet browser and go to [http://github.com]
 * [ ] fill the requested fields with appropriate username, email, and password
 * [ ] click on the `Sign up for Github` button
1. Download the application
 * [ ] Go to [http://desktop.github.com] and click on the `Download GitHub Desktop` button.
2. Installation
 * It should start automatically, otherwise go to your `Downloads` folder and double click on the "GitHubSetup.exe" file

3. configuration: you should see a window that says "Welcome"
 * [ ] fill the username and password and click on `login`, then your email and click on `Continue`
 * [ ] skip the local repository search
 * [ ] now you can just quit the "Github Desktop" application

### Python

1. Downloads
 * [ ] please download [Windows 64-Bit Python 2.7 Graphical Installer](https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-Windows-x86_64.exe) from [http://continuum.io/downloads]
 * [ ] if you have a 32 bit system (typically Windows XP), then download the [Windows 32-Bit Python 2.7 Graphical Installer](https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-Windows-x86.exe) instead.

2. Installation of the Anaconda distribution

* [ ] go to your `Downloads` folder and double click on the "Anaconda-X.X.X-Windows-" file
* [ ] confirm that you want to run the file on the security warning pop-up window
* [ ] on the Anaconda Setup Wizard, beware, you will have to change on option, so click 'Next' on the opening panel
* [ ] then 'Agree' with the licence agreement
* [ ] verify that you Install for `Just Me (recommended)`, then click on `Next`
* [ ] use default Destination folder and click on `Next`
* [ ] check that both "Add Anaconda to my PATH" and "Register Anaconda as my default Python 2.7" are ckecked and click on `Install`
* [ ] upon completion, click on 'Next', then `Finish`

3. Configuration



## Mac OS

### XQuartz

1. Download [XQuartz-2.7.7.dmg](http://xquartz.macosforge.org/downloads/SL/XQuartz-2.7.7.dmg) from [http://xquartz.macosforge.org/landing/]

2. Installation
 * [ ] double click on "XQuartz-2.7.7.dmg" in your "Downloads" folder or wherever you downloaded it.
 * [ ] double click on the "XQuartz.pkg"
 * [ ] click on `Continue` and `Agree` until you can click on `Install`

### Git

0. Set up an account on Github.com
 * [ ] Open an internet browser and go to [http://github.com]
 * [ ] fill the requested fields with appropriate username, email, and password
 * [ ] click on the `Sign up for Github` button
1. Download the application
 * [ ] Go to [http://desktop.github.com] and click on the `Download GitHub Desktop` button.
2. Installation
 * [ ] Go to your `Downloads` folder
 * [ ] decompress the `.zip` archive if needed
 * [ ] double-click on the `GitHub Desktop` icon
 * [ ] click on the `Open` button at the security pop up window
 * [ ] click on `Move to Application Folder`
3. configuration: you should see a window that says "Let's take a minute to setup your computer"
 * [ ] click on `Continue`
 * [ ] fill the username and password and click on `Sign up`, then on `Continue`
 * [ ] Click on `Install Command Line Tools`, then on the pop-up window, type down your mac account password and click on `Install Helper`
 * [ ] click on `OK` upon completion of the Helper install
 * [ ] Then click on `Continue` on the "Welcome to GitHub Desktop"
 * [ ] Don't add any repository yet, just click on `Done`
 * [ ] now you can just quit the "Github Desktop" application

 ### Atom

 1. Download the Atom installer by clicking on the big red `Download For Mac` button on [http://atom.io]

 2. Install as usual

 3. Enjoy!


### Scratch
1. Download [MacScratch1.4.dmg](http://download.scratch.mit.edu/MacScratch1.4.dmg) from http://download.scratch.mit.edu/
2. then install as usual:
 * select your `Downloads` folder from the `Dock`
 * clic on the .dmg file to mount the virtual disk that wraps the application
 * drag and drop this application to your `Applications` folder in the pop-up window
 * eject the virtual disk
3. test Scratch
 * select your `Applications` folder from the `Dock`
 * clic on the `Scratch1.4` folder
 * then clic on the `Scratch.app` icon
 * the Scratch window should appear on your screen and you should be able to drag and move the little animal around

### R

1. Downloads

 * [ ] Go to [http://cran.rstudio.com/bin/macosx/] and download either the "R-3.2.2.pkg" or the "R-3.2.1-snowleopard.pkg" depending on the version of your OS (check About this mac on the apple menu on the top left of your screen if needed).

 * [ ] download [RStudio-0.99.473.dmg](http://download1.rstudio.org/RStudio-0.99.473.dmg) from https://www.rstudio.com/products/rstudio/download/ or an appropriate older version from [https://support.rstudio.com/hc/en-us/articles/206569407-Older-Versions-of-RStudio-Desktop]


2. Installation
* [ ] In the Finder open the folder in which you downloaded the R package. Double-click on it and do as usual.
* [ ] go to the download folder then double-click on "RStudio-X.XX.XXX.dmg". In the window that pops up, slide the RStudio icon into the Applications folder.

3. Verification
 * [ ] Launch RStudio from the icon on your desktop
 * [ ] in the command window, type 'demo(graphics)


###Python

The procedure will be poster later this evening. Meanwhile, please download [Mac OS X — 64-Bit Python 2.7 Graphical Installer](https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-MacOSX-x86_64.pkg) from [http://continuum.io/downloads]


## Linux debian based

### Python

Execute the following commands:
1. Download and installation
 * [ ] `sudo apt-get install python2.7`
 * [ ] `sudo apt-get install python-numpy python-scipy python-matplotlib python-pandas`
 * [ ] `sudo apt-get install ipython ipython-notebook`

   You might as well install the documentation

 * [ ] `sudo apt-get install python2.7-doc python2.7-examples`
 * [ ] `sudo apt-get install python-numpy-doc python-matplotlib-doc`
 * [ ] `sudo apt-get install ipython-doc`

2. Check the installation
 * [ ] in a terminal, type `ipython` in order to lauch a ipython interpreter
 * [ ] in the ipython shell, type each of those lines one by one followed by enter

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
    x=np.arange(-5,5,.1)
    y=stats.norm.pdf(x)
    plt.plot(x,y)
    plt.show()
    ```
 * [ ] python /usr/share/pyshared/pygame/examples/chimp.py

3. If you want a look a the documentation you installed, use your favorite browser  
 `iceweasel /usr/share/doc/python2.7-doc/html/index.html`  
 and  
 `iceweasel /usr/share/doc/python-pygame/index.hml`


### Git
1. Download et installation
    ```bash
    sudo apt-get install git-core
    ```
2. Configuration, by typing in a terminal with the appropriate replacements
 * [ ] `git config --global user.name "your_user_name"`
 * [ ] `git config --global user.email your_email@example.com`

### Scratch
1. Installation: in a terminal, type
```bash
sudo apt-get install scratch`
```
2. Test : in the terminal of a graphic console, type
```bash
scratch
```
You should see a new window, where you should be able to grab and move the little mascot.


### R

1. Setup
 * [ ] Check which linux exactly you are using with the following command
    ```bash
    lsb_release -da
    ```
  You should see a aoutput like this one:
    ```
    Distributor ID: Debian
    Description :   Debian GNU/Linux 7.8 (wheezy)
    Release:        7.8
    Codename:       wheezy
    ```

 * [ ] add the appropriate repository to your `/etc/apt/sources.list`
    ```bash
    sudo sh -c 'echo deb http://cran.univ-paris1.fr/bin/linux/debian wheezy-cran3/ >> /etc/apt/sources.list'
    ```
    For ubuntu, you migh have to leave out the -cran3 after the version codename
    ```bash
    sudo sh -c 'echo deb http://cran.univ-paris1.fr/bin/linux/ubuntu vivid/ >> /etc/apt/sources.list'
    ```


 * [ ] update your repository list
    ```bash
    sudo apt-get update
    ```
 * [ ] go to [http://www.rstudio.com/products/rstudio/download/] and download the appropriate `.deb` installer for Debian/Ubuntu. If your system is not that recent, go to [https://support.rstudio.com/hc/en-us/articles/206569407-Older-Versions-of-RStudio-Desktop] to find the appropriate installer file.


1. Installation
 * [ ] R
    ```bash
    sudo apt-get install r-base r-base-core r-base-html
    ```
 * [ ] and, for Rstudio, replacing the XX by the version numbers
    ```bash
    sudo apt-get install libjpeg62
    sudo dpkg -i rstudio-X.XX.XXX-amd64.deb
    ```

3. Verification
 * [ ] type `rstudio` in a console to lauch the R interpreter
 * [ ] type 'demo(graphics)' and press on 'Enter' to see the graphs.

### Atom

 If you are using linux, you are most probably already using a decent text editor and thus won't need Atom.
