for anaconda use miniforge3: https://github.com/conda-forge/miniforge



    6  conda install numpy
    9  cpnda install pyserial
   10  conda install pyserial
   11  conda install networkx
   14  sudo apt-get install libasound-dev
   21  sudo apt-get remove libportaudio2
   22  git clone -b alsapatch https://github.com/gglockner/portaudio
   23  cd portaudio
   24  ls
   25  ./configure && make
   26  sudo make install
   27  sudo ldconfig
   30  sudo apt-get install libsndfile
   31  sudo apt-get install libsndfile1
   32  sudo apt-get install libsndfile2
   33  sudo apt-get install libsndfile1-dev
   37  sudo apt-get install libportmidi-dev
   39  sudo apt-get install liblo-dev
   40  sudo apt-get install liblo-tools
   64  sudo apt-get install libjack-dev 
   65  sudo /home/marco/miniforge3/bin/python setup.py install --use-double --use-jack
   
jack audio troubleshooting: https://jackaudio.org/faq/linux_rt_config.html
https://manpages.ubuntu.com/manpages/xenial/man1/jackd.1.html

pyo from source: http://ajaxsoundstudio.com/pyodoc/compiling.html

resources for starting program on boot:
https://raspberrypi.stackexchange.com/questions/12730/start-a-lxterminal-on-startup
https://forums.raspberrypi.com/viewtopic.php?t=294014

alsa audio: http://cagewebdev.com/raspberry-pi-getting-audio-working/
set sample=1024

arduino serial port ttyUSB0

start jackd server before starting the score: in .bashrc:
   /usr/bin/jackd -dalsa -dhw:USB -r48000 -p1024 -n2
   sleep 10
   /home/marco/miniforge3/bin/python /home/marco/Musica/SCORE/score.py
   
------------------------------------------------------------------------
   
Direct installation of pyo as from http://ajaxsoundstudio.com/pyodoc/compiling.html#debian-ubuntu-apt-get
that installs also portmidi, jack and liblo

sudo apt-get install libjack-jackd2-dev libportmidi-dev portaudio19-dev liblo-dev libsndfile-dev
sudo apt-get install python3-dev python3-tk python3-pil.imagetk python3-pip
git clone https://github.com/belangeo/pyo.git
cd pyo
sudo python3 setup.py install --use-jack --use-double
cd
sudo apt-get qjackctl
