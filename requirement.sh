echo "installing in progress.."
timeout 3
echo "please hold on.."
timeout 3

apt-get update
apt-get upgrade -y
apt-get install python -y
apt-get install python2 -y
apt-get install python-pip -y
apt-get install python3 -y
pip install requests
pip install pythonping
pip install beautifulsoup4
pip install colorama

echo "all programs is installed.."
echo "now start the scanner.py"
echo "Good Work.."
echo "programmer Sh4d0wE4"