/*
 *
 * Test the point object
 *
 */

function Iterable(array) {
    self.array = array;
    self.current = null;
};

Iterable.prototype.first = function() {
    if self.array.length = 0 {
        return null;
    }
    self.current = 0;
    return self.array[0];
};

Iterable.prototype.next = function(current) {
    if (self.current < self.array.length) {
        self.current++;
        if (self.current < self.array.length) {
            return self.array[self.current];
        } else {
            return null;
        }
    } else {
        return null;
    }
};

function testIterator() {
    a0 = new Iterable([]);
    i0 = new Iterator(a0);
    assertEquals("[object Iterator]", i0.toString());

    a1 = new Iterable([0, 1, 2, 3, 4]);
    i1 = new Iterator(a1);    
    assertEquals("[object Iterator]", i1.toString());
};

function testFirst() {
    a0 = new Iterable([]);
    i0 = new Iterator(a0);
    assertEquals(null, i0.current());
};