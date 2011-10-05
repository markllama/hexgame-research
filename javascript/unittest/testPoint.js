/*
 *
 * Test the point object
 *
 */

function testPoint() {
    p0 = new Point(5, 6);
    assertEquals(5, p0.x);
    assertEquals(6, p0.y);
};

function testToString() {
    p0 = new Point(4, 9);
    assertEquals("(4, 9)", p0.toString());
};

function testToXml() {
    p0 = new Point(-14, 22);
    assertEquals("<point x=\"-14\" y=\"22\" />", p0.toXml());
};

// test the whole first 3 hex circles?
function testLen() {
    p0 = new Point(0, 0);
    assertEquals(0, p0.len());
};

