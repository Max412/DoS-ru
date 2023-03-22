# HCam
HCam - it's a tool for get access to camera. 👀 


# Download&Install
1) Install <a href="https://termux.dev" target="_blank">**Termux**</a>  
2) **Turn this commands in Termux:**
* `apt update`  
* `apt upgrade`  
* `pkg install git && pkg install python3`  
* `git clone https://github.com/Max412/easycamhack`  
* `cd easycamhack`  
* `pip install -r requirements.txt`  
* `python3 easycamhack.py`  


# Usage
On the first run, you will need to enter the <a href="https://account.shodan.io/login" target="_blank">Shodan API</a>:
![capture](https://github.com/Max412/DoS-ru/blob/main/cam2.png?raw=true)

# Flags
* `--api` [NEW_API]  
  Changing the API key you entered when you first started, for example: `python3 hcam.py --api 7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib65`

* `--ip` [IP]  
   Check the IP camera for vulnerability by entering the password, for example: `python3 hcam.py --ip 12.3.456.78`
   
* `--country` [COUNTRY IN Alpha-2 FORMAT]  
   Specify the country to search for vulnerable cameras: `python3 hcam.py --country US`

<h2>Donation</h2>

 * PayPal donation: [![PayPal page](https://img.shields.io/badge/donate-Paypal-fd8200.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=JCY2BGLULSWVJ&lc=US&item_name=ScreenToGif&item_number=screentogif&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted)
 * Patreon subscription: [![Patreon subscription](https://img.shields.io/badge/subscribe-Patreon-orange.svg)](https://www.patreon.com/nicke)

![capture](https://github.com/Max412/DoS-ru/blob/main/cam.png?raw=true)








<hr style="border:2px solid blue">
