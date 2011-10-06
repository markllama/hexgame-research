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

function testEquals() {
    p0 = new Point(2, 3);
    p1 = new Point(2, 3);
    p2 = new Point(3, 5);

    assertTrue(p0.eq(p1));
    assertFalse(p0.eq(p2));
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

    p1 = new Point(14, -22);
    assertEquals(26.0, p1.len());
};

function testAdd() {
    p0 = new Point(-4, -2);
    p1 = new Point(3, 5);

    p2 = p0.add(p1);

    assertTrue(p2.eq(new Point(-1, 3)));
};

function testSub() {
    p0 = new Point(-4, -2);
    p1 = new Point(3, 5);

    p2 = p0.sub(p1);

    assertTrue(p2.eq(new Point(-7, -7)));
};

function testMul() {
    p0 = new Point(-4, 5);
    p1 = p0.mul(5);
    assertTrue(p1.eq(new Point(-20, 25)));
};

function testDiv() {
    p0 = new Point(10, 15);
    p1 = p0.div(5);
    assertTrue(p1.eq(new Point(2, 3)));
};
