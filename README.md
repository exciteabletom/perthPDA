# perthPDA
Checks the Western Australia Department of Transport website for available Practical Driving Assessment (PDA) bookings.

## How to use
1. Install [Firefox](https://www.mozilla.org/firefox/new/) and Selenium (`python -m pip install selenium`)
1. Copy `config-example.py` to `config.py`
1. Fill in your personal information in `config.py`
1. Run the script with `python driving_test.py`

If there is a test available, "Driving test available at: location" will be printed to the screen.

If there is no test available the script will exit silently


## Receive an email when a test is available

This can be accomplished easily using cron.

For example, this [cron job](https://en.wikipedia.org/wiki/Cron) checks every 5 minutes for a test and emails you if one is available:
```
MAILTO=myemail@example.com

*/5 * * * * python /path/to/driving_test.py
```


## Need help?
Please do not hesitate to open an issue on Github, or send me an email at: me@tomdougiamas.com

I would love to help you get a test booked.
