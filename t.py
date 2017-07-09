#################################################################
                    
                 #creator : Kriti Sahu

#script to download images from uglysweatercomics

#################################################################


#Script to download images from uglysweater comics
#You can also use selenium to move to older posts

from bs4 import BeautifulSoup 
import time
import urllib
import os
from urllib import urlopen
import glob
from PIL import Image
import webbrowser
import imageio
import shutil
import mimetypes
import requests


   
#Create file in the directory where the script is
def create_dir(fname): 
    global filename 
    filename=fname
    if not os.path.isdir(filename):
        os.mkdir(filename)
    os.chdir(filename)
    
    #Create Images folder to make gif
    if not os.path.exists("Images"):
        os.makedirs("Images")  

#Scrap the page

def scrap(older_post):
    count=0

    global get_url

    get_url = "http://uglysweatercomic.com"+older_post

    #print(get_url)
   
    url = urlopen(get_url)
    content = url.read()
    soup = BeautifulSoup(content,"lxml")
    title=[]
   

    #Title of the images
    for a in soup.find_all('h1',attrs={'class':"entry-title"}):
        title.append(a.text)

    #print(title)
       
    mydiv=soup.find_all('div',attrs={'class':"body entry-content"})
     
    for d in mydiv:
        
        slide =d.find('div',attrs={'class':"sqs-block gallery-block sqs-block-gallery"})
        
        #contains slider images

        if slide!=None:
            path = "./Images/"

            os.chdir(path)  #set path to store images in Images(folder)
            images=[]
            
            imgs= slide.find_all('img')
            for img in imgs:
                print(img.get('data-image'))
                images.append(img.get('data-image'))
            
            u=0
            
            #save images in Images(folder) to create gif out out of them

            for i in images:
                urllib.urlretrieve(i, str(u)+".png")
                time.sleep(1)
                u=u+1

            #make the images of same size

            width = int(1000)
            height = int(1000)
            r=os.getcwd()
            print(r)
            print(head)

            head=retval
            #print(head)
            
            f_img=title[count].replace('/n','').strip()

            for fn in sorted(os.listdir(r)):
                #print(fn)
                myimg=Image.open(r+'/'+fn)

                img_anti=myimg.resize((width,height),Image.ANTIALIAS)

                name,ext=os.path.splitext(fn)

                new_image_file = "%s%s" % (name,ext)

                img_anti.save(r+'/'+new_image_file)

                #print("resized file saved as %s" % new_image_file)

                #webbrowser.open(new_image_file)        #to see ur resize image file
            

            #take pics from Images(folder) and make gif

            with imageio.get_writer(head+'/'+f_img+".gif", mode='I',duration = 0.8) as writer:
                for fn in sorted(os.listdir(r)):

                    image = imageio.imread(r+'/'+fn)
                    writer.append_data(image)

            #time.sleep(3) #to wait for gif to create

            count=count+1  
              
            #remove png files from folder-Images           
            
            filelist = glob.glob("*.png")
            for f in filelist:
                os.remove(f)
      
        else:
            
            #set directory         
            os.chdir(retval)
          
            print(retval)
                     
            imgs= d.find('img')
            '''response = requests.get(imgs.get('src'))
            
            content_type = response.headers['content-type']
            extension = mimetypes.guess_extension(content_type)
            print(extension)'''
            #print(imgs.get('src'))

            #download images                   
            '''urllib.urlretrieve(imgs.get('src'), str(title[count]+str(extension)))'''
            #time.sleep(2)
            count=count+1
    
    #move to older_post page
    older_post=None
    ref = soup.find('a', attrs={'class' : 'older-posts'})
    
    #check if older posts link present
    if ref !=None:
        older_post=ref['href']
        scrap(older_post)

def main():
    
    fname=str(raw_input("Enter filename : "))
    create_dir(fname)
    global retval
    #gives the  current location of the folder
    retval = os.getcwd() 
    #print(retval)
    scrap("/")
    print("downloading is completed")
    #print os.getcwd()
 
    #shutil.rmtree(r) # remove Images(folder)

main()




