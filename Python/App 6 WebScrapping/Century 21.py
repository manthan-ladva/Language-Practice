import pandas                                   #--------------------Importing Libraries
import requests                                 #--------------------Importing Libraries
from bs4 import BeautifulSoup                   #--------------------Importing Libraries

l = []                                          #--------------------List, which is used here to import details

base_url = "https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="                      #--------------------Url is passed here to proceed work

for page in range(0, 30, 10):                                                         #--------------------This loop is used for no. of pages
    print(base_url + str(page) + ".html")                                             #--------------------increment the names in url

    r = requests.get(base_url + str(page) + ".html")                                  #--------------------Request from Url
    c = r.content                                                                     #--------------------Collect all its content
    soup = BeautifulSoup(c, "html.parser")                                            #--------------------Functionality is used here of library
    all =  soup.find_all("div", {"class":"propertyRow"})                              #--------------------Particular division of particular class is finded

    for i in all:                                                                     #--------------------This loop is used for the all the items in the particular page
        d = {}                                                                                        #--------------------Dictionary Declaration
        d["Price"] = i.find("h4", {"class": "propPrice"}).text.replace("\n", "")                      #--------------------Details collecting
        d["Address"] = i.find_all("span", {"class":"propAddressCollapse"})[0].text
        d["Locality"] = i.find_all("span", {"class":"propAddressCollapse"})[1].text

        try:                                                                                          #--------------------If available then collect the details
            d["Beds"] = i.find("span", {"class":"infoBed"}).find("b").text
        except:
            d["Beds"] = None

        try:
            d["Full Bath"] = i.find("span", {"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Bath"] = None

        try:
            d["Area"] = i.find("span", {"class":"infoSqFt"}).find("b").text
        except:
            d["Area"] = None

        try:
            d["Half Bath"] = i.find("span", {"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Bath"] = None

        for column_group in i.find_all("div", {"class":"columnGroup"}):                                #--------------------Some extra details which are rare
            for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}), column_group.find_all("span", {"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text

        l.append(d)                                                                                     #--------------------Giving details to List

df = pandas.DataFrame(l)                                                                                #--------------------Converting list to DataFrame
df.to_csv("Century 21.csv")                                                                             #--------------------Making it to a Csv file
