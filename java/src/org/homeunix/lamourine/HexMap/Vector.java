/**
 *
 */
package org.homeunix.lamourine.HexMap;

/**
 * The HexMap.Vector represent a location on a hex map.
 *
 * A hex map has 3 coordinate axes instead of the regular two in a Cartesian
 * coordinate system.  Because only two coordinates are needed to define a 
 * point uniquely on a plane, the third axis is redundent and can be derived
 * from the other two.  
 * 
 * The axes are noted as hx, hy and hz to distinguish them from the Cartisian
 * x and y.  hz is always equal to hy - hx for any point.
 *
 * @author Mark Lamourine &lt;markllama@gmail.comt&gt;
 * @version 0.0
 */
public class Vector {
    
    final int hx;
    final int hy;
    final int hz;
    /**
     * The hex map origin
     */
    public static final Vector ORIGIN = new Vector(0, 0);

    /**
     * Unit vectors in each of the 6 directions
     */
    public static final Vector[] UNIT = {
	new Vector(0, -1),
	new Vector(1, 0),
	new Vector(1, 1),
	new Vector(0, 1),
	new Vector(-1, 0),
	new Vector(-1, -1)
    };

    /**
     * Define the characteristics of the hexes in each hextant.
     * The sign of each element reflects the signs of the hexes in each
     * hextant.
     * @private
     */
    private static final int HEXTANT[][] = {
	{  1, -1, -1},
	{  1,  1, -1},
	{  1,  1,  1},
	{ -1,  1,  1},
	{ -1, -1,  1},
	{ -1, -1, -1}
    };

    /**
     * Default constructor
     */
    Vector() {
	this.hx = 0;
	this.hy = 0;
	this.hz = 0;
    }

    /**
     * Constructor for two ints.
     */
    Vector(int hx, int hy) {
	this.hx = hx;
	this.hy = hy;
	this.hz = hy - hx;
    }

    /**
     * Cloning constructor
     */
    Vector(Vector hv) {
	this.hx = hv.hx;
	this.hy = hv.hy;
	this.hz = hv.hz;
    }

    /**
     * 
     */
    public String toString() {
	return "(" + this.hx + ", " + this.hy + ", " + this.hz + ")";
    }

    /**
     * The hx coordinate
     * @return the hx coordinate
     */
    public int getHx() {
	return this.hx;
    }

    /**
     * The hy coordinate
     * @return the hy coordinate
     */
    public int getHy() {
	return this.hy;
    }

    /**
     * The hx coordinate
     * @return the hx coordinate
     */
    public int getHz() {
	return this.hz;
    }

    /**
     * Compare two hex vectors
     *
     * @return true if the vectors are equivalant.
     */
    @Override public boolean equals(Object othat) {
	if (this == othat) {
	    return true;
	}

	if (!(othat instanceof Vector)) {
	    return false;
	}
	
	Vector that = (Vector)othat;

	return (this.hx == that.hx && this.hy == that.hy);
    }

    /**
     *
     */
    @Override public int hashCode() {
	return ((23 + this.hx) * 37) + this.hy; 
    }

    /**
     * The length of a hex vector.
     *
     * @return the length of the Vector in hexes
     */
    public int length() {
	// the length of a hex vector is the max of the absolute values of the
	// coordinates.
	return Math.max(Math.abs(this.hx), Math.max(Math.abs(this.hy), Math.abs(this.hz)));
    }

    /**
     * Add two vectors
     * @param other the second addend
     * @return the sum of the two vectors
     */
    public Vector add(Vector other) {
	return new Vector(this.hx + other.hx, this.hy + other.hy);
    }

    /**
     * Subtract two vectors
     * @param other the second addend
     * @return the difference of the two vectors
     */
    public Vector sub(Vector other) {
	return new Vector(this.hx - other.hx, this.hy - other.hy);
    }

    /**
     * The dot product of two vectors
     * @param other the second multiplicand
     * @return the product of the two vectors
     */
    public Vector mul(int m) {
	return new Vector(this.hx * m, this.hy * m);
    }

    // division doesn't really make sense.

    /**
     * Find the distance between between two points
     * @param other the other vector
     * @return the distance between two points
     */
    public int distance(Vector other) {
	return this.sub(other).length();
    }

    /**
     * What hextant does the vector reside
     * @return the hextant containing this vector
     */
    public int hextant() {

	int i;

	int ux = this.hx < 0 ? -1 : (this.hx > 0 ? 1 : 0);
	int uy = this.hy < 0 ? -1 : (this.hy > 0 ? 1 : 0);
	int uz = this.hz < 0 ? -1 : (this.hz > 0 ? 1 : 0);

	Vector hunit = new Vector(ux, uy);

	for (i = 0 ; i < 6 ; i++) {
	    // check if the vector is on axis
	    if (hunit.equals(Vector.UNIT[i])) {
		return i;
	    } 
	}

 	// not on axis
	for (i = 0 ; i < 6 ; i++) {
	    int c[] = Vector.HEXTANT[i];
	    if (ux == c[0] && uy == c[1] && uz == c[2]) {
		break;
	    }	    
	}
	return i;
    }

    /**
     * Rotate the vector by a multiple of 60 degrees
     * @return the vector rotated
     */
    public Vector rotate(int h) {
	// prepare the rotator
	int r[] = {this.hy, this.hx, -this.hz, -this.hy, -this.hx, this.hz, this.hy};

	// normalize the rotation value
	h %= 6;
	if (h < 0) {
	    h += 6;
	}
	return new Vector(r[h+1], r[h]);
    }
    
    /**
     * The bearing of this vector
     * @return the bearing of this vector
     */
    public float bearing() {
	int h = this.hextant();
	Vector n = this.rotate(-h);
	float f = (float) Math.abs(n.hx) / (float) this.length();
    
	return h + f;
    }

    /**
     * The angle between two vectors
     * @return the angle between two vectors
     */
    public float angle(Vector other) {
	float b = this.bearing();
	float o = other.bearing();
    
	if (o < b) {
	    o += 6;
	}
	return o - b;
    }

};


