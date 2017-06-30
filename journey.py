import folium
map = folium.Map(location=[46.336135, 13.786698])
print(map)
map.save("Map1.html")

map = folium.Map(location=[46.336135, 13.786698],zoom_start=11)
map.save("Map1.html")

map.add_child(folium.Marker(location=[46.283288, 13.833684],popup= "sexy strand"))
map.add_child(folium.CircleMarker(location=[46.273276, 13.893348],radius = 10, popup= "sweet home", color= 'red'))
map.add_child(folium.Marker(location=[46.261760, 13.592697],popup= "Cobarid vízesés(vízesésben fürdés),(70km)"))
map.add_child(folium.Marker(location=[46.349391, 13.802744],popup= "mészköves hegytető (13km)"))
map.add_child(folium.Marker(location=[46.293537, 13.493032],popup= "Susec - canyoning (55euro, 87km), http://www.lifeadventures.si/adventures/canyoning-slovenia/canyoning-susec/"))
map.add_child(folium.Marker(location=[46.368547, 14.114110],popup= "rafting (35euro, 26km)"))
map.add_child(folium.Marker(location=[46.393776, 14.085619],popup= "Vintgar-szurdok (27km)"))

map.save("Map1.html")


