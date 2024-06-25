from bs4 import BeautifulSoup
import requests
 
html_text = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text 
 
souped_html = BeautifulSoup(html_text, 'lxml')
 
films = souped_html.find_all('h3')
 
film_list = [] 
 
for film in films: 
    film_titles = film.text.strip().replace('"', '') 
    if film_titles.startswith("12:"):
        film_titles = film.text.replace(':', ')') 
    film_list.append(film_titles) 
 
film_list.reverse() 
 
print(*film_list, sep="\n") 
 
with open("Top-100-Films.txt", "w", encoding="latin-1") as txtfile:
    txtfile.write("Top 100 Films\n\n")
    for film in film_list:
        txtfile.write(f"{film}\n")
 

#! line1-2= These are our imported libraries we will be using.
#*line4= dot notation used to grab just the text we want from the request we made from the website. The get method is used as a request to a specific URL.
#*line6=  we use the BeautifulSoup library to analyse the web page we requested.
#*line8= inspected the elements on the website to find the element that was holding the film titles and then used the .find_all method to find all the h3's within the webpage.
#*line10= created a new list to store the films in.
#?line12= for loop used to iterate through our films
#?line13= To mitigate some issues in our code, i used to .replace() method to remove the speech marks and replace them with nothing.
#?line14-15= To remove the ':' from the Godfather II title, I used an if statement and the replace method to change it to a ')'.
#?line16= used a for loop to iterate through our films and appended the list so we could store the films in that list.
#*line18= we then used the .reverse() method to change the order of the films so it was ordered starting from 1 to 100.
#todoline20= we then printed the film list and used the sep= parameter and passed the value "\n" so that each film is placed onto a new line.
#?line22-24= with open used to export the results into a txtfile, called Top-100-Films.txt.
#? The "w" means that the file has been opened in write mode.
#? encoding="latin-1" allows the program to convert special characters in our txt file instad of utf-8 as that wouldn't work.
#? as txtfile assgins the variable name.
#? Instructed the writer to make a new row with the heading Top 100 Films.
#?line25= The for loop allows us to iterate through the list.


# #! was to outline BeautifulSoup class, Import requests
# #* was to outline the variable names and lists created
# #todo was to outline the print statement
# #? was to outline the for loops and with open def




