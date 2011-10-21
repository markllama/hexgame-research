// test a HexMapView

hexrun = 15;

mapurls = [ 
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/catancenter.xml",
];

mapreqs = [
    new window.XMLHttpRequest()
];

mapreqs[0].open('GET', mapurls[0], false);
mapreqs[0].send(null);


mapdocs = [
    //loadMap(mapreqs[0].responseXML),
    mapreqs[0].responseXML
];

maps = [ 
    new HexMapView(hexrun, mapdocs[0])
];

