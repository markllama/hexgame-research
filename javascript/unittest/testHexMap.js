/*
 *
 * Test the point object
 *
 */

mapurl = [ 
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/sample.xml",
    "https://lamourine.homeunix.org/~mark/hexgame/data/xml/sample_offset.xml"
];

/*
function loadMap(mapurl) {
    var req = new window.XMLHttpRequest();
    req.open('GET', mapurl, false);
    req.send(null);
    return req;
    //return req.responseXML;
};
*/

mapreqs = [
    new window.XMLHttpRequest(),
    new window.XMLHttpRequest(),
];

mapreqs[0].open('GET', mapurl[0], false);
mapreqs[0].send(null);

mapreqs[1].open('GET', mapurl[1], false);
mapreqs[1].send(null);

mapdocs = [
    //loadMap(mapreqs[0].responseXML),
    mapreqs[0].responseXML,
    //loadMap(mapreqs[1].responseXML)
    mapreqs[1].responseXML
];

maps = [ 
    new HexMap(mapdocs[0]),
    new HexMap(mapdocs[1])
];

function testHexMapConstructorNoArgs() {

    // no args: Default size, origin
    var h0 = new HexMap();

    assert(h0.size.equals(HexMap.Vector.ORIGIN));
    assert(h0.origin.equals(HexMap.Vector.ORIGIN));

};

function testHexMapConstructorXMLString() {
    // one arg, XML string
    var h0 = new HexMap(mapreqs[0].responseText);
    assert("size = 6,6" + h0.origin.toString(), h0.size.equals(new HexMap.Vector(6, 6)));
    assert("origin = ORIGIN", h0.origin.equals(HexMap.Vector.ORIGIN));
};

function testHexMapConstructorURLString() {
    // one arg, URL string
    var h0 = new HexMap(mapurl[0]);
    assert("size = 6,6" + h0.origin.toString(), h0.size.equals(new HexMap.Vector(6, 6)));
    assert("origin = ORIGIN", h0.origin.equals(HexMap.Vector.ORIGIN));
};

function testHexMapConstructorDocument() {

    var h0 = new HexMap(mapdocs[0]);
    assert("size = 6,6" + h0.origin.toString(), h0.size.equals(new HexMap.Vector(6, 6)));
    assert("origin = ORIGIN", h0.origin.equals(HexMap.Vector.ORIGIN));
};

function testHexMapConstructorElement() {
    // one arg, root Element
    var h0 = new HexMap(mapdocs[0].documentElement)
    assert("size = 6,6" + h0.origin.toString(), h0.size.equals(new HexMap.Vector(6, 6)));
    assert("origin = ORIGIN", h0.origin.equals(HexMap.Vector.ORIGIN));
};

function testHexMapConstructorVector() {
    // one arg, HexMap.Vector
    var h0 = new HexMap(new HexMap.Vector(3, 4));
    assert("size = 3,4" + h0.origin.toString(), h0.size.equals(new HexMap.Vector(3, 4)));
    assert("origin = ORIGIN", h0.origin.equals(HexMap.Vector.ORIGIN));

    // two args, HexMap.Vector, HexMap.Vector
    var h1 = new HexMap(new HexMap.Vector(5, 6), new HexMap.Vector(-2, -2));
    assert("size = 5,6", h1.size.equals(new HexMap.Vector(5, 6)));
    assert("origin = -2, -2", h1.origin.equals(new HexMap.Vector(-2, -2)));
};

function testHexMapConstructorInteger() {
    // two args, int, int,
    var h0 = new HexMap(6, 9);
    assert("size = 6,9" + h0.origin.toString(), h0.size.equals(new HexMap.Vector(6, 9)));
    assert("origin = ORIGIN", h0.origin.equals(HexMap.Vector.ORIGIN));

    // four args, int, int, int, int
    var h1 = new HexMap(5, 3, 1, -1);
    assert("h1 is a hex vector: (5,3), (1, -1)", h1 instanceof HexMap);
    assert("h1 has a size", h1.size instanceof HexMap.Vector);
    assert("size = 5,3 ", 
           h1.size.equals(new HexMap.Vector(5, 3)));
    assert("origin = 1, -1 ", h1.origin.equals(new HexMap.Vector(1, -1)));

};


function testHexMap0Origin() {
    var map = maps[0];
    assertEquals("map 0 origin.hx", 0, map.origin.hx);
    assertEquals("map 0 origin.hy", 0, map.origin.hy);
};


function testHexMapHxFirst() {
    var map0 = new HexMap(new HexMap.Vector(7, 7), new HexMap.Vector(0, 0));
    var map1 = new HexMap(new HexMap.Vector(7, 7), new HexMap.Vector(-3, -3));
    assertEquals("map 0 hxfirst = 0", 0, map0.hxfirst());
    assertEquals("map 1 hxfirst = -3", -3, map1.hxfirst());
};

function testHexMapHxCount() {
    var map0 = new HexMap(new HexMap.Vector(6, 6), new HexMap.Vector(0, 0));
    var map1 = new HexMap(new HexMap.Vector(7, 7), new HexMap.Vector(-3, -3));
    assertEquals("map 0 hxcount = 6", 6, map0.hxcount());
    assertEquals("map 1 hxcount = 7", 7, map1.hxcount());
};

function testHexMapHyFirst() {
    var map0 = new HexMap(new HexMap.Vector(6, 6), new HexMap.Vector(0, 0));
    var map1 = new HexMap(new HexMap.Vector(7, 7), new HexMap.Vector(-3, -3));

    assertEquals("map 0 hyfirst(-1) = null", null, map0.hyfirst(-1));
    assertEquals("map 0 hyfirst(0) = 0", 0, map0.hyfirst(0));
    assertEquals("map 0 hyfirst(1) = 0", 0, map0.hyfirst(1));
    assertEquals("map 0 hyfirst(2) = 1", 1, map0.hyfirst(2));
    assertEquals("map 0 hyfirst(3) = 1", 1, map0.hyfirst(3));
    assertEquals("map 0 hyfirst(4) = 2", 2, map0.hyfirst(4));
    assertEquals("map 0 hyfirst(5) = 2", 2, map0.hyfirst(5));
    assertEquals("map 0 hyfirst(6) = null", null, map0.hyfirst(6));

    assertEquals("map 1 hyfirst(-4) = null", null, map1.hyfirst(-4));
    assertEquals("map 1 hyfirst(-3) = -3", -3, map1.hyfirst(-3));
    assertEquals("map 1 hyfirst(-2) = -3", -3, map1.hyfirst(-2));
    assertEquals("map 1 hyfirst(-1) = -2", -2, map1.hyfirst(-1));
    assertEquals("map 1 hyfirst(0) = -2", -2, map1.hyfirst(0));
    assertEquals("map 1 hyfirst(1) = -1", -1, map1.hyfirst(1));
    assertEquals("map 1 hyfirst(2) = -1", -1, map1.hyfirst(2));
    assertEquals("map 1 hyfirst(3) = 0", 0, map1.hyfirst(3));
    assertEquals("map 1 hyfirst(4) = null", null, map1.hyfirst(4));
};

function testHexMapYBias() {
    map0 = new HexMap(new HexMap.Vector(6, 6), new HexMap.Vector(0, 0));
    map1 = new HexMap(new HexMap.Vector(7, 7), new HexMap.Vector(-3, -3));

    assertEquals("map 0 bias -1 = -1", -1, map0.ybias(-1));
    assertEquals("map 0 bias 0 = 0", 0, map0.ybias(0));
    assertEquals("map 0 bias 1 = 0", 0, map0.ybias(1));
    assertEquals("map 0 bias 2 = 1", 1, map0.ybias(2));
    assertEquals("map 0 bias 3 = 1", 1, map0.ybias(3));
    assertEquals("map 0 bias 4 = 2", 2, map0.ybias(4));
    assertEquals("map 0 bias 5 = 2", 2, map0.ybias(5));
    assertEquals("map 0 bias 6 = 3", 3, map0.ybias(6));

    assertEquals("map 1 bias -4 = -1", -1, map1.ybias(-4));
    assertEquals("map 1 bias -3 = 0", 0, map1.ybias(-3));
    assertEquals("map 1 bias -2 = 0", 0, map1.ybias(-2));
    assertEquals("map 1 bias -1 = 1", 1, map1.ybias(-1));
    assertEquals("map 1 bias 0 = 1", 1, map1.ybias(0));
    assertEquals("map 1 bias 1 = 2", 2, map1.ybias(1));
    assertEquals("map 1 bias 2 = 2", 2, map1.ybias(2));
    assertEquals("map 1 bias 3 = 3", 3, map1.ybias(3));
    assertEquals("map 1 bias 4 = 3", 3, map1.ybias(4));

};

function testHexMap0Contains() {
    var map = maps[0];

    // check the internal corners
    assert("map 0 contains origin", map.contains(HexMap.Vector.ORIGIN));
    assert("map 0 contains 0, 5", map.contains(new HexMap.Vector(0, 5)));
    assert("map 0 contains 5, 2", map.contains(new HexMap.Vector(5, 2)));
    assert("map 0 contains 5, 7", map.contains(new HexMap.Vector(5, 7)));

    // check the external corners
    assertFalse("map 0 not -1, -1", map.contains(new HexMap.Vector(-1, -1)));
    assertFalse("map 0 not -1, 0", map.contains(new HexMap.Vector(-1, 0)));
    assertFalse("map 0 not 0, -1", map.contains(new HexMap.Vector(0, -1)));

    // check the external corners
    assertFalse("map 0 not -1, 5", map.contains(new HexMap.Vector(-1, 5)));
    assertFalse("map 0 not -1, 6", map.contains(new HexMap.Vector(-1, 6)));
    assertFalse("map 0 not 0, 6", map.contains(new HexMap.Vector(0, 6)));

    assertFalse("map 0 not 5, 1", map.contains(new HexMap.Vector(5, 1)));
    assertFalse("map 0 not 6, 2", map.contains(new HexMap.Vector(6, 2)));
    assertFalse("map 0 not 6, 3", map.contains(new HexMap.Vector(6, 3)));

    assertFalse("map 0 not 5, 8", map.contains(new HexMap.Vector(5, 8)));
    assertFalse("map 0 not 6, 7", map.contains(new HexMap.Vector(6, 7)));
    assertFalse("map 0 not 6, 8", map.contains(new HexMap.Vector(6, 8)));

};

function testHexMap1Origin() {
    assertEquals("map 1 origin.hx", -3, maps[1].origin.hx);
    assertEquals("map 1 origin.hy", -3, maps[1].origin.hy);
};


function testHexMap1Contains() {
    var map = maps[1];

    // check the internal corners
    assertTrue(("map 1 contains origin: " + map.origin.toString()), map.contains(HexMap.Vector.ORIGIN));

    assertFalse("map 1 contains -4,-3", map.contains(new HexMap.Vector(-4,-3)));
    assertFalse("map 1 contains -3,-4", map.contains(new HexMap.Vector(-3,-4)));
    assertTrue("map 1 contains -3,-3", map.contains(new HexMap.Vector(-3,-3)));

    assertFalse("map 1 contains -4,3", map.contains(new HexMap.Vector(-4,3))); 
    assertFalse("map 1 contains -3,4", map.contains(new HexMap.Vector(-3,4)));
    assertTrue("map 1 contains -3,3", map.contains(new HexMap.Vector(-3,3)));

    assertFalse("map 1 contains 4,0", map.contains(new HexMap.Vector(4,0))); 
    assertFalse("map 1 contains 3,-1", map.contains(new HexMap.Vector(3,-1)));
    assertTrue("map 1 contains 3,0", map.contains(new HexMap.Vector(3,0)));

    assertFalse("map 1 contains 4,6", map.contains(new HexMap.Vector(4,6))); 
    assertFalse("map 1 contains 3,7", map.contains(new HexMap.Vector(3,7)));
    assertTrue("map 1 contains 3,6", map.contains(new HexMap.Vector(3,6)));
};

function testHexMap0GetHex() {
    var map = maps[0];

    assert("map 0 hex 0,0 is correct", 
           map[0][0].location.equals(HexMap.Vector.ORIGIN));

    assert("map 0 hex -3,-3 is correct", 
           map[-3][-3].location.equals(new HexMap.Vector(-3, -3)));
};