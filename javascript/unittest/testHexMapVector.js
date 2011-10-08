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

// toString

// toXml

// add

// sub

// mul

// length

// distance

// hextant

// rotate

// angle

// bearing 
