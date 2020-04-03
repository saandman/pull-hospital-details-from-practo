import requests
import bs4

# feel free to change the url to your location also can add any number of pages, just add them to the list.

list_of_webpages = []
# first 3 pages of Practo Bangalore
for i in range(1, 4):
    list_of_webpages.append(requests.get('https://www.practo.com/bangalore/hospitals?page='+str(i)).text)

for hospital in range(len(list_of_webpages)):
    soup = bs4.BeautifulSoup(list_of_webpages[hospital], 'lxml')
    div = soup.find_all('div', class_='c-card')

    for i in div:
        if float(i.find('span', class_='common__star-rating__value').text) < 4.0:
            continue
        else:
            hospital_name = i.find('h2', class_='u-title-font u-c-pointer u-bold')
            print(hospital_name.text + " ("+i.find('span', class_='common__star-rating__value').text+")")

            # try & except blocks are used here because some data of some hospitals is not available on website or is in different form
            try:
                hospital_specialization = i.find('div', class_='c-card-info__item u-t-capitalize')
                print(hospital_specialization.span.text)
            except:
                pass

            try:
                working_days = i.find('span', class_='u-color--green')
                print(working_days.span.text)
            except:
                temp_working_days = i.find('span', class_='u-d-block u-bold')
                temp = temp_working_days.span.span
                working_days = temp.find_all('span')
                for w in working_days:
                    print(w.text, end=' ')
                print()

            try:
                temp_time = i.find('span', class_='u-smallest-font')
                time = temp_time.find_all('span')
                for t in time:
                    print(t.text, end=' ')
                print()
            except:
                pass

            try:
                locality_name = i.find('h3', class_='u-d-inlineblock c-locality__name')
                print(locality_name.text)
            except:
                pass
            print('-----------------------------------------------------')
