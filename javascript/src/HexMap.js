/**
 * @fileoverview
 * Hex Game classes:
 * <br>
 * This module provides a set of classes used to model the mechanics of Hex
 * based games.
 *
 * @version 0.1
 * @author Mark Lamourine <markllama@gmail.com>
 * 
 */

// throw an exception if Iterator is not defined

/**
 * @class
 * @constructor
 * @param {HexMap.Vector} size the size of the array in hexes
 * @param {HexMap.Vector} origin the origin of the array in hexes
 * @param {Boolean} fill populate the array with hexes on creation? (default: true)
 * @param {HexMap.Hex} hex a sample hex object (default HexMap.Hex}
 * @param {Array of HexMap.Terrain} a set of terrains to be included by default
 */
HexMap = function(size, origin) {

    // don't replace this if it's been provided by a superclass
    if (! this.hex) {
	this.hex = HexMap.Hex;
    }

    /*
     * signature: 
     *    HexMap() # 0     
     *    HexMap(Document d) # 1
     *    HexMap(Element e)  # 1
     *    HexMap(String url) # 1
     *    HexMap(String xml) # 1
     *    HexMap(HexMap.Vector size, HexMap.Vector origin=HexMap.Vector.ORIGIN) # 1 or 2
     *    HexMap(int sx, int sy, int ox=0, int oy=0) # 2 or 4
     */
    
    if (arguments.length == 0) {
        this.initVectors(HexMap.DEFAULT_SIZE, HexMap.Vector.ORIGIN);
    } else if (arguments.length == 1) {
        // string?
        if (typeof arguments[0] == "string") {
            // check for URL pattern match
            var re = new RegExp("^\(http\s?\://\(\\S\)+)");
            if (re.test(arguments[0])) {
                req = new window.XMLHttpRequest();
                req.open('GET', arguments[0], false);
                req.send();
                this.initDOM(req.responseXML.documentElement);
            } else {
                // could try parsing and check for error, put this first?
                // XML document string
                var parser = new DOMParser();
                var mapdoc = parser.parseFromString(arguments[0], 'text/xml');
                this.initDOM(mapdoc);
            }
        } else if (arguments[0] instanceof Document) {
            // XML document
            this.initDOM(arguments[0]);
        } else if (arguments[0] instanceof Element) {
            // XML element
            this.initDOM(arguments[0]);
        } else if (arguments[0] instanceof HexMap.Vector) { 
            this.initVectors(arguments[0], HexMap.Vector.ORIGIN);
        } else {
            throw 'invalid single argument signature: ' + arguments[0];
        }
    } else if (arguments.length == 2) {
        if (typeof arguments[0] == "number") {
            var s = new HexMap.Vector(arguments[0], arguments[1]);
            var o = HexMap.Vector.ORIGIN;
        } else {
            // two vectors
            var s = arguments[0];
            var o = arguments[1];
        }
        this.initVectors(s, o);
    } else if (arguments.length == 4) {
        // four ints, size and origin
        var s = new HexMap.Vector(arguments[0], arguments[1]);
        var o = new HexMap.Vector(arguments[2], arguments[3]);
        this.initVectors(s, o);
    } else {
        throw "invalid HexMap constructor signature" + arguments;
        //alert("No matching signature for HexMap");
    }
    this.listeners = [];
};

HexMap.prototype.terrain_types = {};
HexMap.prototype.token_types = {};

HexMap.prototype.terrains = {};
HexMap.prototype.tokens = {} ;

/**
 * @class
 * A point in a hexagonal plane
 *
 * @constructor
 * Create a new HexMap.Vector
 * @param {Number} hx the hx coordinate of a HexMap.Vector tuple
 * @param {Number} hy the hy coordinate of a Hexgame.Vector tuple
 */
HexMap.Vector = function() {

    /** 
     * the hx coordinate of the hex vector
     * @type Number
     */
    this.hx = null;
    /**
     * the hy coordinate of the hex vector
     * @type Number
     */
    this.hy = null;

    if (arguments.length == 1 && arguments[0] instanceof Element) {
	var hx = Number(arguments[0].getAttribute('hx'));
	var hy = Number(arguments[0].getAttribute('hy'));
    } else if (arguments.length == 1 && arguments[0] instanceof HexMap.Vector) {
	// copy from a HexMap.Vector
	var hx = arguments[0].hx;
	var hy = arguments[0].hy;
    } else if (arguments.length == 2) {
	// initialize from two arguments which convert to Numbers
        var hx = Number(arguments[0]);
	var hy = Number(arguments[1]);
    }
    
    if (hx == null) {
	throw TypeError("hx cannot be null");
    }
    if (hy == null) {
	throw TypeError("hx cannot be null");
    }

    if (typeof hx != 'number') {
	throw TypeError("invalid number: " + hx.toString() + " actually " +  typeof hx);
    }

    if (typeof hy != 'number') {
	throw TypeError("invalid number: " + hy.toString() + " actually " +  typeof hy);
    }

    this.hx = hx;
    this.hy = hy;
    
    // derived attributes
    // Since these are constant on instantiation, just calculate them once
    /** 
     * the hz coordinate of the hex vector: hz = hy - hx
     * @type Number
     */
    this.hz = this.hy - this.hx ;

};

/**
 * Initialize a hexmap vector from a DOM element
 * @private
 * @param {HTMLElement} A DOM vector element
 */
HexMap.Vector.fromDOM = function(element) {
    if (!(element instanceof Element)) {
	throw TypeError("element must be a DOM element, not " + typeof element + " value: " + element.toString());
    }
    var hx = Number(element.getAttribute('hx'));
    var hy = Number(element.getAttribute('hy'));
    return new HexMap.Vector(hx, hy);
};

// Constants

/**
 * The (0,0) vector.
 * @final
 * @type HexMap.Vector
 */
HexMap.Vector.ORIGIN = new HexMap.Vector(0,0) ;

/**
 * Vectors with length 1 in all 6 directions
 * @final
 * @type Array of HexMap.Vector
 */
HexMap.Vector.UNIT = [
		       new HexMap.Vector( 0, -1),
		       new HexMap.Vector( 1,  0),
		       new HexMap.Vector( 1,  1),
		       new HexMap.Vector( 0,  1),
		       new HexMap.Vector(-1,  0),
		       new HexMap.Vector(-1, -1)
		       ];

/**
 * Define the characteristics of the hexes in each hextant.
 * The sign of each element reflects the signs of the hexes in each
 * hextant.
 * @private
 */
HexMap.Vector.HEXTANT = [
			  [ 1,  -1, -1],
			  [ 1,   1, -1],
			  [ 1,   1,  1],
			  [ -1,  1,  1],
			  [ -1, -1,  1],
			  [ -1, -1, -1]
			  ];
/**
 * Compare two hex vectors for equality
 * @param {HexMap.Vector} other a Vector to compare to this one. 
 * @return {Boolean} True if the two hex vectors are equivalent
 */
HexMap.Vector.prototype.equals = function(other) {
    return this.hx == other.hx && this.hy == other.hy;
};


/**
 * Convert a hex vector to string form.
 * @return {String} A string representation of the hex vector
 */
HexMap.Vector.prototype.toString = function() {
    return "HexMap.Vector(" + this.hx + ", " + this.hy + ")";
};

/**
 * Convert a hex vector to XML
 * @return {String} the hex vector as XML: &lt;hexvector hx="" hy="" /&gt;
 */
HexMap.Vector.prototype.toXml = function() {
    return "<hexvector hx=\"" + this.hx + "\" hy=\"" + this.hy + "\" />"; 
};

// Arithmetic Functions

/**
 * Add two hex vectors
 * @param {HexMap.Vector} other The hex vector to add to this one.
 * @return {HexMap.Vector} The sum of two hex vectors
 */
HexMap.Vector.prototype.add = function(other) {
    return new HexMap.Vector(this.hx + other.hx, this.hy + other.hy);
};

/**
 * Subtract two hex vectors
 * @param {HexMap.Vector} other The hex vector to subtract from this one.
 * @return {HexMap.Vector} The difference between the two hex vectors
 */
HexMap.Vector.prototype.sub = function(other) {
    return new HexMap.Vector(this.hx - other.hx, this.hy - other.hy);
};

/**
 * the dot product of two hex vectors
 * @param {Number} multiplier How many times to multiply this hex vector
 * @return {HexMap.Vector} a vector n times the length of the original
 */
HexMap.Vector.prototype.mul = function(multiplier) {
    return new HexMap.Vector(this.hx * multiplier, this.hy * multiplier);
};

// Length and Distance

/**
 * The distance from this this hex point to the origin
 * @return {Number} The length of this hex vector
 */
HexMap.Vector.prototype.length = function() {
    return Math.max(Math.abs(this.hx), 
		    Math.max(Math.abs(this.hy),
			     Math.abs(this.hz)));
};

/**
 * The distance between two hex points
 * @param {HexMap.Vector} other
 * @return {Number} The distance from this hex point to the other.
 */
HexMap.Vector.prototype.distance = function(other) {
    return other.sub(this).length();
};

// Direction

/**
 * Which of 6 regions (hextants) does this hex point reside 
 * @return {Number} the number of the region which contains this hex.
 */
HexMap.Vector.prototype.hextant = function() {
    
    var ux = 0;
    var uy = 0;
    var uz = 0;

    if (this.hx != 0) { ux = this.hx / Math.abs(this.hx); }
    if (this.hy != 0) { uy = this.hy / Math.abs(this.hy); }
    if (this.hz != 0) { uz = this.hz / Math.abs(this.hz); }

    var hunit = new HexMap.Vector(ux, uy);
    for (var i = 0 ; i < HexMap.Vector.UNIT.length ; i++) {
	if (hunit.equals(HexMap.Vector.UNIT[i]) && hunit.hz == uz) {
	    return i;
	}
    }

    for (var i = 0 ; i < HexMap.Vector.HEXTANT.length ; i++) {
	var c = HexMap.Vector.HEXTANT[i];
	if (ux === c[0] && uy === c[1] && uz === c[2]) {
	    return i;
	}	    
    }

    throw "Never Matched: i = " + i + " (" + ux + ", " + uy + ", " + uz + ") for hex " + this.toString(); 
};

/**
 * Invert this vector
 */
HexMap.Vector.prototype.invert = function() {
    return new HexMap.Vector(-this.hx, -this.hy);
};

/**
 * Rotate this vector around the origin by increments of 60 degrees
 * @param hextants: the number if 60 degree increments to rotate
 * @return {HexMap.Vector} The hex rotated by N * 60 degrees.
 */
HexMap.Vector.prototype.rotate = function(hextants) {
    var a = [this.hy, this.hx, -this.hz, -this.hy, -this.hx, this.hz, this.hy];
    var r = hextants % 6;
    
    // if the rotation is negative, normalize it
    if (r < 0) {
	r += 6;
    }
    return new HexMap.Vector(a[r+1], a[r]);
};

/**
 * The direction of the hex vector.  The integer part is the hextant and
 * the decimal part is a fraction of the arc between one hextant and the
 * next.
 * @return {Number} 
 */
HexMap.Vector.prototype.bearing = function() {

    var h = this.hextant();
    var n = this.rotate(-h);
    var f = Math.abs(n.hx) / this.length();
    
    return h + f;
};

/**
 * The angle between two hex vectors.  The angle is always right handed and
 * positive.
 * @param {HexMap.Vector} other The second hex vector
 * @return {Number} The angle between this hex vector and the other.
 */
HexMap.Vector.prototype.angle = function(other) {
    var b = this.bearing();
    var o = other.bearing();
    
    if (o < b) {
	o += 6;
    }
    return o - b;
};



/**
 * The default size of a hex array
 * @final
 * @type HexMap.Vector
 */
HexMap.DEFAULT_SIZE = HexMap.Vector.ORIGIN;

/**
 * The default origin of a hex array
 * @final
 * @type HexMap.Vector
 */
HexMap.DEFAULT_ORIGIN = HexMap.Vector.ORIGIN;

/**
 * Create a hexmap from HexMap.Vectors
 *
 */
HexMap.prototype.initVectors = function(size, origin) {
    // check that they are both HexMap.Vector s

    if (size) {
        this.size = size;
    } else {
        this.size = HexMap.DEFAULT_SIZE;
    }

    this.size = size;

    if (origin) { 
        this.origin = origin;
    } else {
        this.origin = HexMap.Vector.ORIGIN
    }

    this.fill();
};

/**
 * Create a hexmap from a DOM structure
 * @param {element} the map element of the document
 */
HexMap.prototype.initDOM = function(element) {
    if (element instanceof Document) {
        element = element.documentElement;
    }

    if (!(element instanceof Element) || element.tagName.toLowerCase() != 'map') {
	throw "HexMap.initDOM: element must be a map, not" + element.toString() + " ," + element.tagName ;
    }
    this.fromdom = true;
    this.URL = element.ownerDocument.URL;

    var url = parseUri(this.URL);

    this.baseUrl = url.protocol + "://" + url.authority + url.directory;

    if (element.hasAttribute('size')) {
	// split the string
	var sizestr = element.getAttribute('size');
	var size = sizestr.split(',');
	this.size = new HexMap.Vector(Number(size[0]), Number(size[1]));
    } else {
        sizeelement = element.getElementsByTagName('size')[0];
        sizevector = sizeelement.getElementsByTagName('vector')[0];
        this.size = HexMap.Vector.fromDOM(sizevector);
    }

    if (element.hasAttribute('origin')) {
	// split the string
	var originstr = element.getAttribute('origin');
	var origin = originstr.split(',');
	this.origin = new HexMap.Vector(Number(origin[0]), Number(origin[1]));
    } else {
        originelement = element.getElementsByTagName('origin')[0];
        originvector = originelement.getElementsByTagName('vector')[0];
        this.origin = HexMap.Vector.fromDOM(originvector);

    }

    this.fill();

    if (element.hasAttribute('id')) {
	this.id = element.getAttribute('id')
    }

    if (element.hasAttribute('name')) {
	this.name = element.getAttribute('name')
    }

    // add the terrains
    var mapdoc = element.ownerDocument;
    var terrains = mapdoc.getElementsByTagName('terrain');
    for (var i = 0 ; i < terrains.length ; i++) {
	var telement = terrains[i];
	
	if (telement.hasAttribute('type')) {
            ttypestr = telement.getAttribute('type');
            var ttype = this.terrain_types[ttypestr];
            if (ttype == undefined) {
	        var ttype = eval(ttypestr);
            }
	} else {
	    ttype = HexMap.Terrain;
	}

        if (ttype) {
	    var tname = telement.getAttribute('name');
	    var terrain = new ttype(this, telement);
        } else {
            throw "No such terrain class: " + ttypestr;
        }
	
	this.terrains[tname] = terrain;
    }

    var tokens = mapdoc.getElementsByTagName('token');
    for (var i = 0 ; i < tokens.length ; i++) {
	var telement = tokens[i];

	if (telement.hasAttribute('type')) {
	    var ttype = eval(telement.getAttribute('type'));
	} else {
	    ttype = HexMap.Token;
	}
	var tname = telement.getAttribute('name');
	var token = new ttype(this, telement);
	this.tokens[tname] = token;
    }
};

/**
 * The hx value of the first column in the array
 * @return {Number} The first column.
 */
HexMap.prototype.hxfirst = function() {
    return this.origin.hx;
};

/**
 * The number of columns in the array
 * @return {Number} The number of columns in the array
 */
HexMap.prototype.hxcount = function() {
    return this.size.hx;
};

/**
 * The hy offset of the first hex in this column from the origin.hy
 * @return {Number} the hy offset of this column.
 */
HexMap.prototype.ybias = function(hx) {
    return Math.floor((hx - this.hxfirst()) / 2);
};

/**
 * The first hy value in the given column
 * @param {Number} hx a column in the array.
 * @return {Number} the first hy value in column hx.
 */
HexMap.prototype.hyfirst = function(hx) {
    var first = this.hxfirst();
    if (hx < first || hx >= first + this.hxcount()) {
	return null;
    }
    return this.origin.hy + this.ybias(hx);
};

/**
 * The number of hexes in the given column.
 * @param {Number} hx a column in the array.
 * @return {Number} The number of hexes in column hx.
 */
HexMap.prototype.hycount = function(hx) {
    var first = this.hxfirst();
    if (hx < first || hx >= first + this.hxcount()) {
	return null;
    }    
    return this.size.hy;
};


/**
 * Add the hexes to the array object directly.
 * @private
 * @return {void}
 */
HexMap.prototype.fill = function() {
    var hxmin = this.hxfirst();
    var hxlimit = hxmin + this.hxcount();
    for (var hx = hxmin ; hx < hxlimit ; hx++) {
	var column = [];
	var hymin = this.hyfirst(hx);
	var hylimit = hymin + this.hycount(hx);
	
	for (var hy = hymin ; hy < hylimit ; hy++) {
	    column[hy] = new this.hex(new HexMap.Vector(hx, hy), this)
	}  
	    
	var colnum = hx ;
	this[colnum] = column;
    }
};

/**
 * Return the location of the origin of this array
 * @return {HexMap.Vector} The origin of the array
 */
HexMap.prototype.getOrigin = function() {
    return this.origin;
};

/**
 * Return the dimensions of this array
 * @return {HexMap.Vector} The size of the array (hx, hy)
 */
HexMap.prototype.getSize = function() {
    return this.size;
};

/**
 * The array as XML
 * @return {String} the array as XML
 */
HexMap.prototype.toXml = function() {
     var s = "<map  >\n";
     s += "</map>";
     return s;
 };

 /**
  * Does the array contain the given hex vector?
  * @param {HexMap.Vector} hv A hex location
  * @return {Boolean} true if the hex location is in the array
  */
 HexMap.prototype.contains = function(hv) {
     // acount for origin

     normal = hv;

     /* This could be more elegent */
     if (normal.hx < this.hxfirst() ||
 	  normal.hx >= this.hxfirst() + this.hxcount()) {
 	return false;
     }

     if (normal.hy < this.hyfirst(normal.hx) || 
 	normal.hy >= this.hyfirst(normal.hx) + this.hycount(normal.hx)) {
 	return false;
     }

     return true;
 };

 /**
  * Return a hex at the location of the hex vector given
  * @param {HexMap.Vector} location The ocation the location of the desired hex.
  * @return {HexMap.Hex} The hex at the given location.
  */
 HexMap.prototype.getHex = function(location) {

     if (! location instanceof HexMap.Vector) {
 	throw "getHex: location must be a HexMap.Vector";
     }
     // check if the requested hex exists
     // should we throw an exception instead?
     if (!this.contains(location)) {	
 	return null;
     }

     //normal = location.add(this.origin.invert());
     normal = location;
     if (!this[normal.hx]) {
	 throw "getHex: hx is not a valid column: " + location.toString();
     }
     // unbias hy MAL FIX
     return this[normal.hx][normal.hy];

 };

 /**
  * An iterator for this array
  * @return {Iterator &lt;HexMap
 &gt;} An iterator for this array
 */
HexMap.prototype.iterator = function() {
    return new Iterator(this);
};

/**
 * Return the first hex in the array sequence
 * @private
 * @return {HexMap.Hex} The first hex in the array
 */
HexMap.prototype.first = function() {
    var firsthex = this.getHex(this.origin);
    return firsthex;
};

/**
 * Return the hex after the one given in the array sequence
 * @private
 * @return {HexMap} The next hex (or null)
 */
HexMap.prototype.next = function(current) {
    if (!current) { return null; }

    try {
	var nextvec = current.location.add(HexMap.Vector.UNIT[3]);
	var next = this.getHex(nextvec);
    } catch(err) {
	alert("couldnt get next hex: current = " + current.toString() + " next: " + nextvec.toString());
    }

    if (!next) {
	// we were at the end of the column
	// switch to the beginning of the next
	var hx = current.location.hx + 1;
	var hy = this.hyfirst(hx);

	next = this.getHex(new HexMap.Vector(hx, hy));
    }

    return next;    
};

/**
 *
 */
HexMap.prototype.toString = function() {
    return '[object HexMap]';
};

/**
 * @param {HexMap.Terrain} terrain the terrain to add to the map
 */
HexMap.prototype.addTerrain = function (terrain) {
    if (!(terrain && terrain instanceof HexMap.Terrain)) {
	throw(new Error("must be a terrain"));
    }
    // should check if it's already there.
    terrain.setMap(this);
    this.terrains[terrain.name] = terrain;
};

/**
 *
 */
HexMap.prototype.removeTerrain = function (terrain) {

};

/**
 *
 */
HexMap.prototype.getTerrains = function () {

};


HexMap.prototype.addToken = function(token) {
    if (!(token && token instanceof HexMap.Token)) {
	throw(new Error("must be a token"));
    }
    // should check if it's already there.
    token.setMap(this);
    this.tokens[token.name] = token;
};

// HexMap.prototype.removeToken = function (token) {} ;
// HexMap.prototype.getTokens = function () {} ;

// HexMap.prototype.addListener = function (listener) {} ;
// HexMap.prototype.removeListener = function (listener) {} ;
// HexMap.prototype.updateListeners = function (message) {};



/**
 * @class
 * This represents a single element of a hex array.  It will contain
 * hex modifiers (HexMap.Terrain) and game tokens (HexMap.Token).
 * @constructor
 * @param {HexMap.Vector} location
 * @param {HexMap} map
 * @param {Array of HexMap.Token} tokens
 * @param {Array if HexMap.Terrain} terrains
 */
HexMap.Hex = function(location, map) {
    // check that the location is a Vector or null 
    this.location = location;
    // check that the map is a HexMap or null
    this.map = map;

    // initialize the token and terrains lists
    this.terrains = [];
    this.tokens = [];
};

/**
 * @method HexMap.Hex
 * @return string representation of the hex
 * @type String
 */
HexMap.Hex.prototype.toString = function() {
    // print the map ID, location, token ids and terrain ids

    return "new HexMap.Hex(" + this.location.toString() + ")";
};

/**
 * @method HexMap.Hex
 * @return XML representation of the hex
 * @type String
 */
HexMap.Hex.prototype.toXml = function() {
    var xml =  "<hex>" + this.location.toXml();
    for (token in this.tokens) {
	// only indicate the id
	xml += token.toXml(true);
    }
    for (terrain in this.terrains) {
	// only indicate the id
	xml += terrain.toXml(true);
    }
    xml += "</hex>";

    return xml;
};

/**
 * @method HexMap.Hex
 * @return true if the hex has no terrains or tokens
 * @type Boolean
 */
HexMap.Hex.prototype.empty = function() {
    return this.tokens.length === 0 && this.terrains.length === 0;
};

/**
 * @method HexMap.Hex
 */
HexMap.Hex.prototype.addToken = function(token) {
    this.tokens.push(token);
};

/**
 * @method HexMap.Hex
 * @param {HexMap.Token} token
 * @return the token removed or null
 * @type HexMap.Token
 */
HexMap.Hex.prototype.removeToken = function(token) {
    for (var i = 0 ; i < this.tokens.length ; i++) {
	if (this.tokens[i] === token) {
	    return this.tokens.splice(i, 1);
	}
    }
};

/**
 * @method HexMap.Hex
 * @param {HexMap.Token} token
 * @param {Integer} count how many layers to raise the token (default: 1)
 */
HexMap.Hex.prototype.raiseToken = function(token, count) {

};

/**
 * @method HexMap.Hex
 * @param {HexMap.Token} token 
 * @param {Integer} count how many layers to lower the token (default: 1)
 */
HexMap.Hex.prototype.lowerToken = function(token, count) {

};

/**
 * @method HexMap.Hex
 * @param {HexMap.Terrain} terrain
 */
HexMap.Hex.prototype.addTerrain = function(terrain) {
    this.terrains.push(terrain);
};

/**
 * @method HexMap.Hex
 * @param {HexMap.Terrain} terrain
 * @return the terrain which was removed or null
 * @type HexMap.Terrain
 */
HexMap.Hex.prototype.removeTerrain = function(terrain) {
    for (var i = 0 ; i < this.terrains.length ; i++) {
	if (this.terrains[i] === terrain) {
	    return this.terrains.splice(i, 1);
	}
    }
};

/**
 * @class
 * @constructor
 */
HexMap.Terrain = function(map) {

    this.map = map;
    this.locations = [];

    if (arguments.length > 1 && arguments[1] instanceof Element) {
	this.terraindom = true;
	this.initDOM(arguments[1]);
    }
};

// register with the map
HexMap.prototype.terrain_types['terrain'] = HexMap.Terrain;

/**
 *
 * @private
 * @param {HTMLElement} element
 */
HexMap.Terrain.prototype.initDOM = function(element) {
    this.fromdom = true;

    if (element.hasAttribute('id')) {
	this.id = element.getAttribute('id');
    }

    if (element.hasAttribute('name')) {
	this.name = element.getAttribute('name');
    }
    
    if (this.map) {
	// add yourself to the map
	this.map.addTerrain(this);

	var doc = element.ownerDocument;
	loc = doc.evaluate('locations', element, null,
			   XPathResult.FIRST_ORDERED_NODE_TYPE,
			   null).singleNodeValue;

	if (!(loc instanceof Element)) {
	    alert("no locations found");
	}

	if (loc.hasAttribute('all')) {
	    var i = this.map.iterator();
	    for (var h = i.next() ; h != null ; h = i.next()) {
		this.addLocation(h.location);
	    }
	    // add it to all
	} else {
	    this.doc = doc;
	    this.loc = loc;

	    var vlist = doc.evaluate('vector', loc, null,
				     XPathResult.ORDERED_NODE_ITERATOR_TYPE,
				     null);

	    for (var vn = vlist.iterateNext() ; vn != null ; vn = vlist.iterateNext()) {		
		var hv = new HexMap.Vector(vn);
		this.addLocation(hv);
	    }
	    
	    this.vlistafter = vlist;
	}
    }
};

HexMap.Terrain.prototype.toString = function() {
    return "[object HexMap.Terrain]";
};

HexMap.Terrain.prototype.toXml = function() {

};

HexMap.Terrain.prototype.setMap = function(map) {
    if (!(map == null || map instanceof HexMap)) {
	throw(new Error("Must be a HexMap"));
    }
    this.map = map;
};

/**
 *
 */
HexMap.Terrain.prototype.addLocation = function(location) {
    
    if (!(this.map.contains(location))) {
	throw "adding a location to the terrain thats not in the map: " + location.toString();
    }

    this.locations.push(location);
    
    try {
	this.map.getHex(location).addTerrain(this);
    } catch(err) {
	alert("map does not contain hexvector " + location.toString());
	throw(err);
    }
    
};


HexMap.Terrain.prototype.removeLocation = function(location) {
    // check that the location is in the map
    
    if (!(this.map.contains(location))) {
	throw "removing a location from the terrain thats not in the map: " + location.toString();
    }

    for (var i in this.locations) {
	var l = this.locations[i];
	if (l.equals(location)) {
	    var h = this.map.getHex(location);
	    h.removeTerrain(this);
	    this.locations.splice(i, 1);
	    break;
	}
    }
};


/**
 * moveto(HexMap.Vector)
 * move(direction)
 */

/**
 * @class
 * 
 * @constructor
 */
HexMap.Token = function(map) {
    this.map = map || null;
    this.locations = [];

    if (arguments.length > 1 && arguments[1] instanceof Element) {
	this.initDOM(arguments[1]);
    } else {
	this.id = 'unset';
	this.name = 'unset';
	this.location = null;
    }
};

HexMap.prototype.token_types['token'] = HexMap.Token;

HexMap.Token.prototype.initDOM = function(element) {
    this.fromdom = true;

    if (element.hasAttribute('id')) {
	this.id = element.getAttribute('id');
    }

    if (element.hasAttribute('name')) {
	this.name = element.getAttribute('name');
    }
    
    if (this.map) {
	// add yourself to the map
	this.map.addToken(this);

	var doc = element.ownerDocument;
	loc = doc.evaluate('locations', element, null,
			   XPathResult.FIRST_ORDERED_NODE_TYPE,
			   null).singleNodeValue;

	this.doc = doc;
	this.loc = loc;

	var vlist = doc.evaluate('vector', loc, null,
				 XPathResult.ORDERED_NODE_ITERATOR_TYPE,
				 null);

	for (var vn = vlist.iterateNext() ; vn != null ; vn = vlist.iterateNext()) {		
	    var hv = new HexMap.Vector(vn);
	    this.addLocation(hv);
	}
	
	this.vlistafter = vlist;
    }
};

HexMap.Token.prototype.toString = function() {
    return "[object HexMap.Token]";
};

HexMap.Token.prototype.toXml = function() {
    return "<token id=\"" + this.id + "\" name=\"" + this.name + "\">"; 
};

HexMap.Token.prototype.setMap = function(map) {
    if (!(map == null || map instanceof HexMap)) {
	throw(new Error("Must be a HexMap"));
    }
    this.map = map;
};

/**
 *
 */
HexMap.Token.prototype.addLocation = function(location) {
    
    if (!(this.map.contains(location))) {
	throw "adding a location to the terrain thats not in the map: " + location.toString();
    }

    this.locations.push(location);
    
    try {
	this.map.getHex(location).addToken(this);
    } catch(err) {
	alert("map does not contain hexvector " + location.toString());
	throw(err);
    }
    
};


