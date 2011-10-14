/*
 *
 * Test the point object
 *
 */

mapurl = [ 
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/sample.xml",
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/sample_offset.xml"
];

function loadMap(mapurl) {
    var req = new window.XMLHttpRequest();
    req.open('GET', mapurl, false);
    req.send(null);
    return req.responseXML;
};

mapdocs = [
    loadMap(mapurl[0]),
    loadMap(mapurl[1])
];

maps = [ 
    new HexMap(mapdocs[0]),
    new HexMap(mapdocs[1])
];

function testHexMap() {

    assertEqual("map 0 origin.hx", 0, maps[0].origin.hx);
    assertEqual("map 0 origin.hy", 0, maps[0].origin.hy);
    assertEqual("simple error", 2, 1);
};


