from datetime import datetime
import ntplib

ntp_pool = 'id.pool.ntp.org'

def get_ntp_time():
    for item in ntp_pool:
    	call = ntplib.NTPClient()
    	response = call.request(item, version=3)
    	t = datetime.fromtimestamp(response.orig_time)
    	print(t.strftime("%a %b %d %H:%M:%S.%f"))

if __name__ == "__main__":
    get_ntp_time()
