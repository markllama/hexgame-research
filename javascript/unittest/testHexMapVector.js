/*
 *
 * Test the point object
 *
 */

function testHexMapVector() {

    hv0 = new HexMap.Vector(14,22);

    assertEquals(14, hv0.hx);
    assertEquals(22, hv0.hy);
    assertEquals(8, hv0.hz);
};

/* Constants */


// HexMap.Vector.ORIGIN
function testHexMapVectorORIGIN() {
    assertEquals(0, HexMap.Vector.ORIGIN.hx);
    assertEquals(0, HexMap.Vector.ORIGIN.hy);
};

// HexMap.Vector.UNIT
function testHexMapVectorUNIT() {
    assertEquals(0, HexMap.Vector.UNIT[0].hx);
    assertEquals(-1, HexMap.Vector.UNIT[0].hy);

    assertEquals(1, HexMap.Vector.UNIT[1].hx);
    assertEquals(0, HexMap.Vector.UNIT[1].hy);

    assertEquals(1, HexMap.Vector.UNIT[2].hx);
    assertEquals(1, HexMap.Vector.UNIT[2].hy);

    assertEquals(0, HexMap.Vector.UNIT[3].hx);
    assertEquals(1, HexMap.Vector.UNIT[3].hy);

    assertEquals(-1, HexMap.Vector.UNIT[4].hx);
    assertEquals(0, HexMap.Vector.UNIT[4].hy);

    assertEquals(-1, HexMap.Vector.UNIT[5].hx);
    assertEquals(-1, HexMap.Vector.UNIT[5].hy);
};

// Methods
// fromDOM

// equals
function testHexMapVectorEquals() {
    hv0 = new HexMap.Vector(3, 4);
    hv1 = new HexMap.Vector(3, 4);
    hv2 = new HexMap.Vector(-5, 12);

    assertTrue(hv0.equals(hv1));
    assertFalse(hv0.equals(hv2));
};

// toString

function testHexMapVectorToString() {
    hv0 = new HexMap.Vector(3, 4);
    assertEquals("HexMap.Vector(3, 4)", hv0.toString());    
};

// toXml
function testHexMapVectorToXml() {
    hv0 = new HexMap.Vector(-5, 12);
    hv0Xml = "<hexvector hx=\"-5\" hy=\"12\" />"
    assertEquals(hv0Xml, hv0.toXml());
};

// add
function testHexMapVectorAdd() {
    hv0 = new HexMap.Vector(2, 5);
    hv1 = new HexMap.Vector(-4, 6);
    hv2 = hv0.add(hv1);
    hv3 = new HexMap.Vector(-2, 11);

    assertTrue(hv3.equals(hv2));

};

// sub
function testHexMapVectorSub() {
    hv0 = new HexMap.Vector(2, 5);
    hv1 = new HexMap.Vector(-4, 6);
    hv2 = hv0.sub(hv1);
    hv3 = new HexMap.Vector(6, -1);

    assertTrue(hv3.equals(hv2));
};

// mul
function testHexMapVectorMul() {
    hv0 = new HexMap.Vector(-6, 7);
    hv1 = hv0.mul(3);
    hv2 = new HexMap.Vector(-18, 21);
    assertTrue(hv2.equals(hv1));

};

// length
function testHexMapVectorLength() {

    // check origin
    assertEquals(0, HexMap.Vector.ORIGIN.length());
    
    // check unit
    assertEquals(1, HexMap.Vector.UNIT[0].length());
    assertEquals(1, HexMap.Vector.UNIT[1].length());
    assertEquals(1, HexMap.Vector.UNIT[2].length());
    assertEquals(1, HexMap.Vector.UNIT[3].length());
    assertEquals(1, HexMap.Vector.UNIT[4].length());
    assertEquals(1, HexMap.Vector.UNIT[5].length());

    // check a circle
    assertEquals("0, -3", 3, new HexMap.Vector(0, -3).length());
    assertEquals("1, -2", 3, new HexMap.Vector(1, -2).length());
    assertEquals("2, -1", 3, new HexMap.Vector(2, -1).length());

    assertEquals("3, 0", 3, new HexMap.Vector(3, 0).length());
    assertEquals("3, 1", 3, new HexMap.Vector(3, 1).length());
    assertEquals("3, 2", 3, new HexMap.Vector(3, 2).length());

    assertEquals("3, 3", 3, new HexMap.Vector(3, 3).length());
    assertEquals("2, 3", 3, new HexMap.Vector(2, 3).length());
    assertEquals("1, 3", 3, new HexMap.Vector(1, 3).length());

    assertEquals("0, 3", 3, new HexMap.Vector(0, 3).length());
    assertEquals("-1, 3", 3, new HexMap.Vector(-1, 2).length());
    assertEquals("-2, 3", 3, new HexMap.Vector(-2, 1).length());

    assertEquals("-3, 3", 3, new HexMap.Vector(-3, 0).length());
    assertEquals("-3, 2", 3, new HexMap.Vector(-3, -1).length());
    assertEquals("-3, 1", 3, new HexMap.Vector(-3, -2).length());

    assertEquals("-3, 0", 3, new HexMap.Vector(-3, -3).length());
    assertEquals("-2, -1", 3, new HexMap.Vector(-2, -3).length());
    assertEquals("-1, -2", 3, new HexMap.Vector(-1, -3).length());

};

// distance
function testHexMapVectorDistance() {

    // check distance from origin
    // check origin
    assertEquals(0, HexMap.Vector.ORIGIN.distance(HexMap.Vector.ORIGIN));

    // check unit
    assertEquals(1, HexMap.Vector.UNIT[0].distance(HexMap.Vector.ORIGIN));
    assertEquals(1, HexMap.Vector.UNIT[1].distance(HexMap.Vector.ORIGIN));
    assertEquals(1, HexMap.Vector.UNIT[2].distance(HexMap.Vector.ORIGIN));
    assertEquals(1, HexMap.Vector.UNIT[3].distance(HexMap.Vector.ORIGIN));
    assertEquals(1, HexMap.Vector.UNIT[4].distance(HexMap.Vector.ORIGIN));
    assertEquals(1, HexMap.Vector.UNIT[5].distance(HexMap.Vector.ORIGIN));

    hv0 = new HexMap.Vector(6, -2);
    assertEquals("UNIT 0 to (6, -2)", 6, HexMap.Vector.UNIT[0].distance(hv0));
    assertEquals("UNIT 1 to (6, -2)", 6, HexMap.Vector.UNIT[0].distance(hv0));
    assertEquals("UNIT 2 to (6, -2)", 6, HexMap.Vector.UNIT[0].distance(hv0));
    assertEquals("UNIT 3 to (6, -2)", 6, HexMap.Vector.UNIT[0].distance(hv0));
    assertEquals("UNIT 4 to (6, -2)", 6, HexMap.Vector.UNIT[0].distance(hv0));
    assertEquals("UNIT 5 to (6, -2)", 6, HexMap.Vector.UNIT[0].distance(hv0));

    
};

// hextant
function testHexMapVectorHextant() {
    assert(false);

};

// rotate
function testHexMapVectorRotate() {
    assert(false);

};

// angle
function testHexMapVectorAngle() {
    assert(false);

};

// bearing 
function testHexMapVectorBearing() {
    assert(false);

};
