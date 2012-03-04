/**
 * @fileoverview
 * @version 0.1
 * @author Mark Lamourine <markllama@gmail.com>
 * @extends HexMapView
 */

/**
 *
 * @class
 * @extends HexMapView
 * @constructor
 */
CatanMapView = function(canvas, hexrun, size, origin) {

    // call the superclass constructor on the new object
    HexMapView.apply(this, arguments);

};

CatanMapView.prototype = new HexMapView();

CatanMapView.prototype.setParent = function(parent) {
    this.parent = parent
    this.parent.appendChild(this.canvas);
};

CatanMapView.prototype.toString = function() {
    return "[object CatanMapView]";
};

// define terrain classes
CatanMapView.Terrain = function() {
    HexMapView.Terrain.apply(this, arguments);
};

/**
 * @private
 * @type CatanMapView.Terrain
 */
CatanMapView.Terrain.prototype = new HexMapView.Terrain();


// subclass code....
CatanMapView.Terrain.Sea = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);    
    this.fillStyle = "lightblue";
}

CatanMapView.Terrain.Sea.prototype = new HexMapView.Terrain.SuperBorder() ;


// subclass code....
CatanMapView.Terrain.Mountain = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);    
    this.fillStyle = "grey";
}

CatanMapView.Terrain.Mountain.prototype = new HexMapView.Terrain.SuperBorder() ;


// subclass code....
CatanMapView.Terrain.Hills = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);    
    this.fillStyle = "brown";
}

CatanMapView.Terrain.Hills.prototype = new HexMapView.Terrain.SuperBorder() ;


// subclass code....
CatanMapView.Terrain.Pasture = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);    
    this.fillStyle = "olive";
}

CatanMapView.Terrain.Pasture.prototype = new HexMapView.Terrain.SuperBorder() ;


// subclass code....
CatanMapView.Terrain.Fields = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);
    this.fillStyle = "tan";
}
CatanMapView.Terrain.Fields.prototype = new HexMapView.Terrain.SuperBorder() ;

// subclass code....
CatanMapView.Terrain.Forest = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);
    this.fillStyle = "green";
}

CatanMapView.Terrain.Forest.prototype = new HexMapView.Terrain.SuperBorder() ;

// subclass code....
CatanMapView.Terrain.Desert = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);
    this.fillStyle = "yellow";
}

CatanMapView.Terrain.Desert.prototype = new HexMapView.Terrain.SuperBorder() ;


/*************************************************************************
 *
 * Tokens
 *
 *************************************************************************
 */

// generic
CatanMapView.Token = function () {
    HexMapView.Token.apply(this, arguments);
};

/**
 * @private
 * @type CatanMapView.Terrain
 */
CatanMapView.Token.prototype = new HexMapView.Token();

CatanMapView.Token.prototype.size = function() {
    if (this.map) {
	return new Point(this.map.hexheight, this.map.hexheight);
    } else {
	return null;
    }
}

// robber
CatanMapView.Token.Robber = function () {
    CatanMapView.Token.apply(this, arguments);
};

CatanMapView.Token.Robber.prototype = new CatanMapView.Token();

CatanMapView.Token.Robber.prototype.draw = function () {
    var ctx = this.map.canvas.getContext('2d');
    var center = this.center();
    var corners = this.corners();

    ctx.fillStyle = "black";

    // draw the robber token shape
    ctx.beginPath();
    
    ctx.moveTo(center.x-this.map.hexrun, center.y+this.map.hexrise);
    ctx.lineTo(center.x+this.map.hexrun, center.y+this.map.hexrise);
    ctx.quadraticCurveTo(
        center.x, center.y-this.map.hexrise*3,
        center.x-this.map.hexrun, center.y+this.map.hexrise
    );
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
}

