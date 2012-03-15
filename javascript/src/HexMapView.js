/**
 * @fileoverview
 *
 * @version 0.1
 * @author Mark Lamourine <markllama@gmail.com>
 * @extends HexMap
 */


// throw an exception if HexMap is not defined
// throw an exception if Point is not defined.

/**
 *
 * @class
 * @extends HexMap
 * @constructor
 */
HexMapView = function(canvas, hexrun, size, origin) {

    // the default hex is a standard HexMapView.Hex
    this.hex = HexMapView.Hex;

    /**
     * The base pixel size of a hex
     * @type Number
     */
    this.setHexSize(hexrun);

    // a place to collect images for preload.
    this.images = [];

    // if size is a Document and origin is null, this still works
    HexMap.apply( this, Array.prototype.slice.call( arguments, 2 ) );
    
    /**
     * The parent element of the new canvas
     * @type Element
     */
    //this.parent = parent;


    // TODO - figure out how this adjusts with changes in the 
    // hex origin

    // place the location of the hex in the upper left corner
    this.porigin = new Point(this.hexradius, this.hexheight);

    // offset this to the location of the hex origin
    this.porigin = this.hexcenter(this.origin);

    // Create a new canvas element and add it to the parent
    if (canvas == undefined) {
        this.canvas = document.createElement('canvas');
    } else {
        this.canvas = canvas;
    }
    this.canvas.setAttribute('id', 'hexmap');

    var csize = this.canvasSize();
    // set the size of the canvas space
    this.canvas.setAttribute('width', csize.x);
    this.canvas.setAttribute('height', csize.y);
};

/**
 * @private
 * @type HexMap
 */
// don't populate the prototype hexes
HexMapView.prototype = new HexMap();

HexMapView.prototype.setParent = function(parent) {
    this.parent = parent;
    this.parent.appendChild(this.canvas);
};

HexMapView.prototype.toString = function() {
    return "[object HexMapView]";
};

/**
 * set the dimensions of a single hex within the map.
 * @param {Number} hexrun 1/4 of the width of a hex in pixels
 */
HexMapView.prototype.setHexSize = function(hexrun) {
    /**
     * 1/4 the width of a hex.  The length of the base of the triangle
     * formed by one diagonal side of a hex.
     * @type Number
     */
    this.hexrun = hexrun;

    /**
     * The distance from one vertex of a hex to it's center. Also the length
     * of one side.
     * @type Number
     */
    this.hexradius = hexrun * 2;

    /**
     * The length drawn from one vertex of a hex to the one opposite it through
     * the center.
     * @type Number
     */
    this.hexwidth = hexrun * 4;

    /**
     * The length of a line dropped from one vertex of a hex to a line
     * bisecting the hex.  Half the distance between two opposed sides.
     * @type Number
     */
    this.hexrise = Math.floor(this.hexradius * 0.866);

    /**
     * The distance from one side of a hex to the opposite side.
     * @type Number
     */
    this.hexheight = this.hexrise * 2;
};


/**
 * Calculate the size of the canvas needed to contain the HexMap
 * @return {Point} the size of the canvas element in pixels
 */
HexMapView.prototype.canvasSize = function() {
    var x = (this.hexrun * 3 * this.size.hx) + this.hexrun;
    var y = (this.hexheight * this.size.hy) + this.hexrise;
    return new Point(x, y);
};

/**
 * @param {HexMap.Vector} vector
 * return Point
 */
HexMapView.prototype.hexcenter = function(vector) {
    // 0,0 is at map.hexwidth, map.hexheight
    // (fx, fy)
    var normal = vector.add(this.origin.invert());
    var ybias = Math.floor(normal.hx / 2);
    var px = ((normal.hx * 3) * this.hexrun) + this.porigin.x;
    var py = ((((normal.hy) * 2) - normal.hx) * this.hexrise) + this.porigin.y;
    return new Point(px, py);
};

HexMapView.prototype.tokencenter = function(vector) {
    return this.hexcenter(vector);
};

/**
 * The radius of the click circle around the center of the given vector
 * @param {HexMap.Vector} 
 * @return int
 */
HexMapView.prototype.clickrange = function(vector) {
    return this.hexradius;
};

/**
 * Find the pixel distance from a given point to the center of a hexvector
 *
 */
HexMapView.prototype.clickdistance = function(point, hexvector) {
    var center = this.hexcenter(hexvector);
    return center.sub(point).len();
};


/**
 * test if a click point is within the clickrange of the given vector
 * @param {Point} point
 * @param {HexMap.Vector} vector
 * @return boolean
 */
HexMapView.prototype.inrange = function(point, vector) {
    return this.clickdistance(point, vector) < this.clickrange(vector);
};

/**
 * This has to return a HexMap.Vector because the ref hex may not be on the map
 * but the other two in the triangle are.
 * @return HexMap.Vector
 */
HexMapView.prototype.refloc = function(point) {
    // determine the reference hex
    var hx = Math.floor((point.x - this.porigin.x) / (this.hexrun * 3));
    var hy = Math.floor(((point.y - this.porigin.y) + (hx * this.hexrise)) / this.hexheight);

    var absolute = new HexMap.Vector(hx, hy);

    var normal = absolute.add(this.origin);
    return normal;
};

/**
 * @returns 
 */
HexMapView.prototype.refbox = function(point) {
    var refloc = this.refloc(point);
    return [refloc,
	    refloc.add(HexMap.Vector.UNIT[2]),
	    refloc.add(HexMap.Vector.UNIT[3])
	    ];
};

/**
 * Convert a pixel location on the canvas to a hex location in the map
 *
 */
HexMapView.prototype.point2vector = function(point) {

    triangle = this.refbox(point);
    // generate a sorting function using the current point.
    // lexical scoping should make this work.
    var map = this;

    var bydistance = function(a, b) {
	return (map.clickdistance(point, a) - map.clickdistance(point, b));
    }

    triangle.sort(bydistance);
    return triangle[0];
};

/**
 * Given a click point, convert to a canvas relative point
 */
HexMapView.prototype.canvasPoint = function(eventpoint) {
    var canvascorner = new Point(this.canvas.offsetLeft, this.canvas.offsetTop);
    var scrollcorner = new Point(window.scrollX, window.scrollY);
    return eventpoint.sub(canvascorner).add(scrollcorner);
};

/**
 * Determine if all of the known images are loaded 
 */
HexMapView.prototype.imagesLoaded = function() {
    var loaded = true;
    for (var img in this.images) {
	loaded &= this.images[img].complete;
    }
    return loaded;
};

HexMapView.prototype.imagesRemaining = function() {
    var pending = 0;
    for (var img in this.images) {
	pending += !this.images[img].complete;
    }
    return pending;
};

/**
 * Draw the hex map in the canvas
 */
HexMapView.prototype.draw = function() {
    var ctx = this.canvas.getContext('2d');

    // check that all of the images have been loaded.
    if (!this.imagesLoaded()) {
	// paint a "busy" message
	var pending = this.imagesRemaining();
	var total = this.images.length;
	var message = "Waiting for " + pending +  " of " + total + " images";

	// write the message to the console in the middle
	ctx.textalign = 'center';
	//ctx.moveTo(ctx.canvas.width/2, ctx.canvas.height/2);
	ctx.fillText(message, ctx.canvas.width/2, ctx.canvas.height/2);
	
	// set a timer to try again
	// how do you get it to use an arbitrary object?
	setTimeout('mapview.draw()', 100);
    } else {
	this.canvas.width = this.canvas.width; // clears the canvas

	// for each hex, draw it's contents

	/*
	var i = this.iterator();
	for (var hex = i.next(); hex ; hex = i.next()) {
	    hex.draw();
	}
	*/

	for (var terrain in this.terrains) {
	    this.terrains[terrain].draw();
	}

	for (var token in this.tokens) {
	    this.tokens[token].draw()
	}	  
    }

};

/**
 *
 * @class
 * @extends HexMap.Hex
 * @constructor
 */
HexMapView.Hex = function(location, map) {
    HexMap.Hex.call(this, location, map);
};

HexMapView.Hex.prototype = new HexMap.Hex();

/**
 * Return a Point indicating the center pixel of this hex
 * @return {Point} The x,y coordinates of the center pixel of this hex
 */
HexMapView.Hex.prototype.center = function() {
    return this.map.hexcenter(this.location);
};

HexMapView.Hex.prototype.distance = function(pixel) {
    var center = this.center();
    var asqr =  Math.pow(center.x - pixel.x, 2);
    var bsqr =  Math.pow(center.y - pixel.y, 2);
    return Math.sqrt(asqr + bsqr);
};

/**
 * Return a list of Points indicating the vertices of this hex
 * @return{[Point]} An array of Points indicating the locations of the vertices
 */
HexMapView.Hex.prototype.vertices = function() {
    var c = this.center();
    return [
	    new Point(c.x - this.map.hexradius, c.y),
	    new Point(c.x - this.map.hexrun, c.y - this.map.hexrise),
	    new Point(c.x + this.map.hexrun, c.y - this.map.hexrise),
	    new Point(c.x + this.map.hexradius, c.y),
	    new Point(c.x + this.map.hexrun, c.y + this.map.hexrise),
	    new Point(c.x - this.map.hexrun, c.y + this.map.hexrise)
	    ];
};

/**
 * Draw the hex on the map
 */
HexMapView.Hex.prototype.draw = function() {
    // draw the terrains
    for (var terrain in this.terrains) {
	this.terrains[terrain].drawHex(this);
    }

    // draw the top token.
    if (this.tokens.length > 0) {
	this.tokens[0].draw();
    }
};

/**
 * present the hex as a string
 */
HexMapView.Hex.prototype.toString = function() {
    return "new HexMapView.Hex(" + this.location.toString() + ")";
};

/**
 *
 * @class
 * @extends HexMap.Terrain
 * @constructor
 */
HexMapView.Terrain = function() {
    this.isviewterrain = true;
    HexMap.Terrain.apply(this, arguments);

    if (arguments.length > 1 && arguments[1] instanceof Element) {
	element = arguments[1];
	this.layer = element.getAttribute('layer');
    }
};

/**
 * @private
 * @type HexMap.Terrain
 */
HexMapView.Terrain.prototype = new HexMap.Terrain();

HexMapView.prototype.terrain_types['terrain'] = HexMapView.Terrain;
/**
 * Draw the terrain in all hexes
 */
HexMapView.Terrain.prototype.draw = function() {
    for (var loc in this.locations) {
	var hex = this.map.getHex(this.locations[loc]);
	this.drawHex(hex);
    }
};

/**
 * Draw a single terrain
 */
HexMapView.Terrain.prototype.drawHex = function(location) {
    // what are we drawing into?
    
};

HexMapView.Terrain.prototype.toString = function() {
    return "[object HexMapView.Terrain]";
};

// Now the derived elements

/**
 *
 * @class
 * @extends HexMap.Token
 * @constructor
 */
HexMapView.Token = function(id, name, map, location) {
    HexMap.Token.apply(this, arguments);
};

/**
 * @private
 * @type HexMap.Token
 */
HexMapView.Token.prototype = new HexMap.Token();

/**
 *
 */
HexMapView.Token.prototype.toString = function() {
    return "[object HexMapView.Token]";
};

/**
 * A token is square and takes 1/2 the height of a hex
 */
HexMapView.Token.prototype.size = function() {
    if (this.map) {
	return new Point(this.map.hexrise, this.map.hexrise);
    } else {
	return null;
    }
};

HexMapView.Token.prototype.center = function(vector) {
    if (!vector) {
	vector = this.locations[0];
    }
    return this.map.hexcenter(vector);
};

/**
 * Locate the drawing corner of a token image
 * The corner is offset from the center by 1/2 the width and height
 * of a token.
 */
HexMapView.Token.prototype.corner = function(vector) {
    if (!vector) {
	vector = this.locations[0];
    }
    var offset = this.size().div(2);
    var center = this.center(vector);
    return center.sub(offset);
};

/*
 * Get the pixel corners of the token image on the canvas
 */
HexMapView.Token.prototype.corners = function(vector) {
    if (!vector) {
	vector = this.locations[0];
    }
    var refpoint = this.corner(vector);
    var size = this.size();
    return [
	    refpoint,
	    refpoint.add(new Point(size.x, 0)),
	    refpoint.add(size),
	    refpoint.add(new Point(0, size.y))
	    ];
};

/**
 * Draw a single token
 * Do it as a white box
 */
HexMapView.Token.prototype.draw = function() {

};


