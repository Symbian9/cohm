
var x=new google.maps.LatLng(52.395715,4.888916);

mapfile = raw_input("What should the new map file (.html) be called? ")

f = open(mapfile, "a")

top = open("map_top.tpl", "r")
top_file = top.readlines()
top.close()

for info in top:
    print >> f, info.strip()
# should have just opened map_top and added it to f = mapfile




var stavanger=new google.maps.LatLng(58.983991,5.734863);
var amsterdam=new google.maps.LatLng(52.395715,4.888916);
var london=new google.maps.LatLng(51.508742,-0.120850);

var myTrip=[
];
