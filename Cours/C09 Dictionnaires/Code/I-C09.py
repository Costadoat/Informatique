import json
import folium
import webbrowser


# Opening JSON file
f = open('lieux-de-tournage-a-paris.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

tournage=data[0]
print(tournage)
print(tournage['fields']['nom_tournage'])

coords=[]
for tournage in data:
    if tournage['fields']['type_tournage']=='Série TV':
#    if tournage['fields']['type_tournage']=='Série Web':
#        if tournage['fields']['nom_tournage'][:4]=='SKAM' :
        if tournage['fields']['nom_tournage'][:10]=='ENGRENAGES' :
#        if tournage['fields']['nom_tournage'][:6].replace('è','e').upper()=='ARSENE' :
            print(tournage['fields']['adresse_lieu'])
            coords.append(tournage['fields']['geo_point_2d'])

f.close()
print(coords[0])

my_map = folium.Map(location = [48.856614, 2.3522219], zoom_start = 13)

# Plot coordinates using comprehension list
for i in range(len(coords)):
    folium.CircleMarker(coords[i], radius=3, color='#f20c54', fill_color='#f20c54',fill_opacity=1).add_to(my_map) 

#Display the map
my_map.save("map.html")
webbrowser.open("map.html")
