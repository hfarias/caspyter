echo "Installing Caspyter"

#________BASICS____________________________

sudo apt-get update
sudo apt-get install build-essential -y
apt-get install sudo wget vim openssh-server git automake curl -y

sudo apt-get update
sudo apt-get install libice6 libsm6 libxt6 libxrender1 libfontconfig1 libcups2 libxml2 libxslt-dev libgtk2.0-0 python-qt4 -y

#_____________USER CASPYTER_______________________

sudo userdel -r caspyter
sudo adduser --disabled-password --gecos "" caspyter
sudo bash -c 'echo "caspyter ALL = (ALL) NOPASSWD: ALL" | (EDITOR="tee -a" visudo)'
echo "caspyter:qwe123" | sudo chpasswd

su caspyter << EOF
echo "Iniciando con Caspyter"
whoami

#_____________USER CASPYTER_______________________

cd /home/caspyter

echo "Cloning files..."
git clone https://github.com/hfarias/caspyter.git


#_____________USER CASPYTER_______________________


mkdir /home/caspyter/lab
mkdir /home/caspyter/casapy

echo "Download CASA"
wget https://almascience.eso.org/arcdistribution/casa-distro/linux/release/casa-release-4.5.2-el6.tar.gz
tar zxf /home/caspyter/casa-release-4.5.2-el6.tar.gz
mv /home/caspyter/casa-release-4.5.2-el6 /home/caspyter/casapy/casa-release-4.5.2-el6

#_____________Install patchELF_______________________
echo "Install patchELF"
sudo sh /home/caspyter/caspyter/script/patchELF.sh


#_____________Install Anaconda_______________________

echo "Install Anaconda"
wget https://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh -O /home/caspyter/lab/Anaconda.sh
bash /home/caspyter/lab/Anaconda.sh -b -p /home/caspyter/anaconda2
echo 'export PATH="$HOME/anaconda2/bin:$PATH"' >> ~/.bashrc
source /home/caspyter/.bashrc

#_____________Install Casanova_______________________
echo "Install Casanova"
source /home/caspyter/caspyter/install_casanova

#_____________Download Data Test_______________________

mkdir /home/caspyter/notebook

cd /home/caspyter/notebook
wget -r -np -nH --cut-dirs=4 --reject "index.html*" https://bulk.cv.nrao.edu/synth/dred_workshops/sis14/working_data/sis14_twhya_calibrated_flagged.ms/

mv /home/caspyter/caspyter/notebook/First_Look_at_Imaging.ipynb /home/caspyter/notebook

EOF