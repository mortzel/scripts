# Random Linux Scripts
In this repo you can find some random scripts I use to make the world a little bit better.

## genpass
_genpass_ is a bash script to generate a random password with a default length of 18 or a other length.

##### Usage
genpass [lentgh]

## genmac
_genmac_ is a basch script to generate a random mac address.  

## goping
_goping_ is a payhton script to check the time which a ping needs to reach google.com and puts the result to a influxdb to view it in grafana.

## locking
_locking_ is a bash script which looks the screen with i3lock and suspends the system if wanted. If you want to suspend, it checks if the screen is already locked and if it is already locked it will not suspend your system.

##### Usage
locking -l | -as | -us

## screenshot
The bash script _screenshot_ creates a screenshot from your actual window.

## Speedflux
_speedflux_ is a python script which uses _speedtest-cli_ to test the internet connection und puts the result to a influxdb to view it in grafana.

## uptor
_uptor_ is a Python script to create torrent files for all files and folders in a folder, or for all folder in a folder in a folder ;)
It create the torrent files, uploads them to transmission and to a bittracker site

##### Usage
uptor -u uploadfolder -c categorie [-r]

## wallpaper
_wallpaper_ is a bash script which sets a random wallpaper from the folder _.wallpaper_ with feh and changes it every 15 minutes. With the parameter _-c_ you can change the actual wallpaper.

##### Usage
wallpaper [-c]
