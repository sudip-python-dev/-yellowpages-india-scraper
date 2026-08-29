import requests
from bs4 import BeautifulSoup
import pandas as pd

html = requests.get('http://yellowpages.in/hyderabad/apparels-and-accessories/110497301').text

#with open('yellowpages.html') as f:
#    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

ui = soup.find('ul', id='MainContent_ulFList')

divs = []
if ui:
    divs = ui.find_all('div', class_='eachPopular')


titles = []
rating_stars = []
reviews = []
open_status = []
images = []
contact_numbers = []
addresses = []
locations = []
hashtags = []
emails = []


for div in divs:
    title = div.find('a', class_='eachPopularTitle')
    if title:
        title = title.text
    else:
        title = 'N/A'
    print(title)
    titles.append(title)
    
    rating_star = div.find('div', class_='eachPopularRatingBlock').contents
    if rating_star:
        rating = rating_star[0].get('class')[1][1:]
    else:
        ratung = 'N/A'
    print(rating)
    rating_stars.append(rating)
    
    review = rating_star[1]
    if review:
        review = review.text
    else:
        review = 'N/A'
    print(review)
    reviews.append(review)
    
    open_now = div.find('div', class_='openNow')
    if open_now:
        open_now = open_now.text
    else:
        open_now = 'N/A'
    print(open_now)
    open_status.append(open_now)
    
    img = div.find('img')
    if img:
        img = img.get('src')
    else:
        img = 'N/A'
    print(img)
    images.append(img)
    
    contact_number = div.find('a', class_='businessContact')
    if contact_number:
        contact_number = contact_number.text
    else:
        contact_number = 'N/A'
    print(contact_number)
    contact_numbers.append(contact_number+'\n')
    
    address = div.find('address', class_='businessArea')
    if address:
        address = address.text
    else:
        address = 'N/A'
    print(address)
    addresses.append(address)
    
    contact_email = div.find('div', class_='eachPopularLink').contents
    if contact_email:
        email = contact_email[0].get('href').split(':')[1]
    else:
        email = 'N/A'
    print(email+'\n')
    emails.append(email+'\n')
    
    location = div.find('div', class_='directionsLocationsBlock').contents
    if location:
        location = location[0].get('href')
    else:
        location = 'N/A'
    print(location)
    locations.append(location)
    
    hashtag = ', '.join([tag.text for tag in div.find_all('li')])
    print(hashtag)
    hashtags.append(hashtag)
    
    print()

file_name = 'yellow_data.xlsx'
sheet_name = 'yellow_sheet'
df = pd.DataFrame({
    'Titles':titles,
    'Rating Stars':rating_stars,
    'Reviews': reviews,
    'Open status': open_status,
    'Images': images,
    'Contact Number': contact_numbers, 
    'Emails': emails,
    'Addresses': addresses,
    'Locations': locations,
    'Purpose': hashtags
    })

print(titles)
print(rating_stars)
print(reviews)
print(open_status)
print(images)
print(contact_numbers)
print(emails)
print(addresses)
print(locations)
print(hashtags)

with open('yellow_data_emails.txt', 'w') as f:
    f.writelines(emails)
with open('yellow_data_numbers.txt', 'w') as f:
    f.writelines(contact_numbers)

df.to_excel(file_name, sheet_name=sheet_name, index=True)

#print("\n--- All Titles ---")
#print(titles)
