#From the webpage - https://apod.nasa.gov/apod/archivepix.html, go to the link, find the image  and download it

#how to parse webpage --- BeautifulSoup
#how to download --- urllib, urlparse
import urllib
from bs4 import BeautifulSoup
import urlparse
import os

#Open the index page
baseurl = "https://apod.nasa.gov/apod/archivepix.html" 
download_folder = "apod_images"

content = urllib.URLopener().open(baseurl).read()
soup = BeautifulSoup(content, "lxml")
atags = soup.find_all("a")
print("opened base url")

#For each link on the index page:
for tag in atags:
    href = tag["href"]

#   Open the link and download the image in it
    hrefurl = urlparse.urljoin(baseurl, href)
    try: 
        hrefcontent = urllib.URLopener().open(hrefurl).read()
    except:
        pass
    hrefsoup = BeautifulSoup(hrefcontent, "lxml")
    print("following link", hrefurl)
    imgtags = hrefsoup.find_all("img")
    
    print("value of imgtags", imgtags)
    for imgtag in imgtags:
        imageurl = urlparse.urljoin(hrefurl, imgtag["src"])
#        print("Downloading image from url", imageurl)
        imgname = imageurl.split("/")[-1]
        download_path = os.path.join(download_folder, imgname)
        print ("download path is", download_path)
        try:
            image = urllib.URLopener().retrieve(imageurl, download_path)
            print("image saved as:", download_path)
        except:
            pass

