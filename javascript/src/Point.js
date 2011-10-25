/**
 * @class
 * A point in a cartesian plane
 * @constructor
 * @param {int} x
 * @param {int} y
 */
function Point(x, y) {
    this.x = x;
    this.y = y;
};

/**
 * Test equality of two points
 * @return boolean
 */
Point.prototype.equals = function(other) {
    return ((this.x == other.x) && (this.y == other.y));
};

/**
 * The string representation of this point.
 * @return string
 */
Point.prototype.toString = function() {
    return "(" + this.x.toString() + ", " + this.y.toString() + ")";
    
};

/**
 * The XML representation of this point
 * @return string
 */
Point.prototype.toXml = function() {
    return "<point x=\"" + this.x + "\" y=\"" + this.y + "\" />";
};

/**
 * length of a vector (the distance of the point from the origin)
 * @return int
 */
Point.prototype.len = function() {
    return Math.round(Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2)));
};

/**
 * The sum of two vectors 
 * @return Point
 */
Point.prototype.add = function(other) {
    return new Point(this.x + other.x, this.y + other.y);
};

/**
 * The difference between two vectors
 * @param {Point} other
 * @return Point
 */
Point.prototype.sub = function(other) {
    return new Point(this.x - other.x, this.y - other.y);
};

/**
 * The dot product of a vector and an integer
 * @param {int} i
 * @return Point
 */
Point.prototype.mul = function(i) {
    return new Point(this.x * i, this.y * i);
};

/**
 * A vector which is a fraction of the original
 * @param {int} i
 * @return Point
 */
Point.prototype.div = function(i) {
    return new Point(Math.round(this.x / i), Math.round(this.y / i));
};
