// test a HexMapView

hexrun = 15;

mapurls = [ 
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/sample.xml",
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/small.xml",
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/sample_offset.xml",
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/catancenter.xml"
];

mapreqs = [
    new window.XMLHttpRequest(),
    new window.XMLHttpRequest(),
    new window.XMLHttpRequest(),
    new window.XMLHttpRequest()
];

mapreqs[0].open('GET', mapurls[0], false);
mapreqs[0].send(null);
mapreqs[1].open('GET', mapurls[1], false);
mapreqs[1].send(null);
mapreqs[2].open('GET', mapurls[2], false);
mapreqs[2].send(null);
mapreqs[3].open('GET', mapurls[3], false);
mapreqs[3].send(null);


mapdocs = [
    //loadMap(mapreqs[0].responseXML),
    mapreqs[0].responseXML,
    mapreqs[1].responseXML,
    mapreqs[2].responseXML,
    mapreqs[3].responseXML
];

maps = [ 
    new HexMapView(hexrun, mapdocs[0]),
    new HexMapView(hexrun, mapdocs[1]),
    new HexMapView(hexrun, mapdocs[2]),
    new HexMapView(hexrun, mapdocs[3])
];

// a collection of HexMap.Vectors and the Points they translate to
points = [
    //{'vector': null, 'center': null}
    //{'vector': new HexMap.Vector(), 'center': new Point()},
    {'vector': HexMap.Vector.ORIGIN, 'center': new Point(30, 50)},
    {'vector': new HexMap.Vector(0,1), 'center': new Point(30, 100)},
    {'vector': new HexMap.Vector(0,2), 'center': new Point(30, 150)},

    {'vector': new HexMap.Vector(1,0), 'center': new Point(75, 25)},
    {'vector': new HexMap.Vector(1,1), 'center': new Point(75, 75)},
    {'vector': new HexMap.Vector(1,2), 'center': new Point(75, 125)},

    {'vector': new HexMap.Vector(2,1), 'center': new Point(120, 50)},
    {'vector': new HexMap.Vector(2,2), 'center': new Point(120, 100)},
    {'vector': new HexMap.Vector(2,3), 'center': new Point(120, 150)},

    {'vector': new HexMap.Vector(3,1), 'center': new Point(165, 25)},
    {'vector': new HexMap.Vector(3,2), 'center': new Point(165, 75)},
    {'vector': new HexMap.Vector(3,3), 'center': new Point(165, 125)},
    
    // now for map 1 origin = (-3, -3)
    {'vector': new HexMap.Vector(-3, -3), 'center': new Point(30, 50)},
    {'vector': new HexMap.Vector(-3, -2), 'center': new Point(30, 100)},
    {'vector': new HexMap.Vector(-3 ,-1), 'center': new Point(30, 150)},

    {'vector': new HexMap.Vector(-2, -3), 'center': new Point(75, 25)},
    {'vector': new HexMap.Vector(-2, -2), 'center': new Point(75, 75)},
    {'vector': new HexMap.Vector(-2, -2), 'center': new Point(75, 125)},

    {'vector': new HexMap.Vector(-1, -2), 'center': new Point(120, 50)},
    {'vector': new HexMap.Vector(-1, -1), 'center': new Point(120, 100)},
    {'vector': new HexMap.Vector(-1, 0), 'center': new Point(120, 150)},

    {'vector': new HexMap.Vector(0, -2), 'center': new Point(165, 25)},
    {'vector': new HexMap.Vector(0, -1), 'center': new Point(165, 75)},
    {'vector': new HexMap.Vector(0, 0), 'center': new Point(165, 125)},

];

function testHexCenterZeroOrigin() {
    var map = maps[0];

    var p = points[0];
    assert("test hex 0", p['center'].equals(map.hexcenter(p['vector'])));

    var p = points[1];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    var p = points[2];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    var p = points[3];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    var p = points[4];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    var p = points[5];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    // now try it with the next map
};

function testHexCenterOffset() {
    map = maps[1];

    var p = points[6];
    assert("test hex 0", p['center'].equals(map.hexcenter(p['vector'])));

    var p = points[7];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    var p = points[8];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    var p = points[9];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    var p = points[10];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));

    var p = points[11];
    var mc = map.hexcenter(p['vector']);
    assert("test hex 1:" + mc.toString(), p['center'].equals(mc));
};

// now check the the inverse
// given a point, find the vector

function testPointToVectorZero() {
    map = maps[0];

    var p = points[0];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[1];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[2];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[3];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[4];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[5];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));
    
};

function testPointToVectorOffset() {
    map = maps[2];

    var p = points[6];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[7];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[8];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[9];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[10];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));

    var p = points[11];
    var v = map.point2vector(p['center']);
    assert("test hex 0: " + v.toString(), p['vector'].equals(v));
    
};

