import urllib.request
from bs4 import BeautifulSoup
import re

url="http://www.pythonchallenge.com/pc/def/linkedlist.php"
response = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(response.content, 'html.parser') # content

paragraph_data = soup.find('body','center')
nothing = "".join(re.findall(r'[1-9]{5}',soup))
for i in range(400):
   try:   
       nextUrl = url+'?'+nothing
       response = urllib.request.urlopen(nextUrl).read().decode()
       soup = BeautifulSoup(response.content, 'html.parser')
       data = soup.find('body')
       nothing = "".join(re.findall(r'[1-9]{5}',data))
   except:
      try:
         print(response)
         nothing = int("".join(re.findall(r'[1-9]{5}',data)))
         nothing /=2
         continue
      except:
         print(response)
         break



