import urllib.request
import time

webcamUrl = "http://216.208.180.174/axis-cgi/jpg/image.cgi"

count = 1

while True:
	urllib.request.urlretrieve(webcamUrl, "./imgs/" + str(count) + ".jpg")
	count += 1
	time.sleep(20)

