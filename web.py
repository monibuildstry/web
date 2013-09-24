#---------------------------------import---------------------------------------
import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;
 
#------------------------------------------------------------------------------
def main():
    userUrl = "http://www.bikramyoga.com/studioDetails.php?id=343";
    req = urllib2.Request(userUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    soup = BeautifulSoup(respHtml);
    address = soup.findAll(name="span",attrs={"class":"testClass6"});
    new = re.search(regular expression,address);
    if(new):
        for each in new:
            print each;
   
 
###############################################################################
if __name__=="__main__":
    main();
