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

CatanMapView.prototype.terrain_types['terrain'] = CatanMapView.Terrain;

// subclass code....
CatanMapView.Terrain.Sea = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);    
    this.fillStyle = "lightblue";
}

CatanMapView.Terrain.Sea.prototype = new HexMapView.Terrain.SuperBorder() ;

CatanMapView.prototype.terrain_types['sea'] = CatanMapView.Terrain.Sea;

// subclass code....
CatanMapView.Terrain.Mountain = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);    
    this.fillStyle = "grey";
}

CatanMapView.Terrain.Mountain.prototype = new HexMapView.Terrain.SuperBorder() ;

CatanMapView.prototype.terrain_types['mountain'] = CatanMapView.Terrain.Mountain;


// subclass code....
CatanMapView.Terrain.Hills = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);    
    this.fillStyle = "brown";
}

CatanMapView.Terrain.Hills.prototype = new HexMapView.Terrain.SuperBorder() ;

CatanMapView.prototype.terrain_types['hills'] = CatanMapView.Terrain.Hills;

// subclass code....
CatanMapView.Terrain.Pasture = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);    
    this.fillStyle = "olive";
}

CatanMapView.Terrain.Pasture.prototype = new HexMapView.Terrain.SuperBorder() ;

CatanMapView.prototype.terrain_types['pasture'] = CatanMapView.Terrain.Pasture;


// subclass code....
CatanMapView.Terrain.Fields = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);
    this.fillStyle = "tan";
}
CatanMapView.Terrain.Fields.prototype = new HexMapView.Terrain.SuperBorder() ;

CatanMapView.prototype.terrain_types['fields'] = CatanMapView.Terrain.Fields;

// subclass code....
CatanMapView.Terrain.Forest = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);
    this.fillStyle = "green";
}

CatanMapView.Terrain.Forest.prototype = new HexMapView.Terrain.SuperBorder() ;

CatanMapView.prototype.terrain_types['forest'] = CatanMapView.Terrain.Forest;


// subclass code....
CatanMapView.Terrain.Desert = function () {
    // call the superclass constructor
    HexMapView.Terrain.SuperBorder.apply(this, arguments);
    this.fillStyle = "yellow";
}

CatanMapView.Terrain.Desert.prototype = new HexMapView.Terrain.SuperBorder() ;

CatanMapView.prototype.terrain_types['desert'] = CatanMapView.Terrain.Desert;


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
    
    ctx.moveTo(center.x+this.map.hexrun, center.y+this.map.hexrise);
    ctx.quadraticCurveTo(
        center.x, center.y-this.map.hexrise*3,
        center.x-this.map.hexrun, center.y+this.map.hexrise
    );
    ctx.closePath();
    ctx.fill();
    //ctx.stroke();
}


// Resource Token

// robber
CatanMapView.Token.Resource = function () {
    CatanMapView.Token.apply(this, arguments);

    // get the roll value from the element attributes
};

CatanMapView.Token.Resource.prototype = new CatanMapView.Token();

CatanMapView.Token.Resource.prototype.initDOM = function (element) {
    HexMap.Token.prototype.initDOM.call(this, element);
    if (element instanceof Element) {
        if (element.hasAttribute("roll")) {
            this.roll = element.getAttribute('roll');
        } 
    }
};

CatanMapView.Token.Resource.prototype.draw = function () {
    var ctx = this.map.canvas.getContext('2d');
    var hexcenter = this.center();

    var resource_center = new Point(hexcenter.x, hexcenter.y+this.map.hexrise);

    ctx.fillStyle = "white";
    ctx.strokeStyle = "black";
    ctx.lineWidth = 1;

    ctx.beginPath();
    ctx.arc(resource_center.x, resource_center.y, 
            this.map.hexrise/2, 0, Math.PI*2, false);
    ctx.closePath();
    ctx.stroke();
    ctx.fill();

    // print the roll number that gets the resource in the center
    if (this.roll == 6 || this.roll == 8) {
        ctx.fillStyle = "red";
    } else {
        ctx.fillStyle = "black";
    }
    ctx.textBaseline = "middle";
    ctx.textAlign = "center";
    ctx.fillText(this.roll, resource_center.x, resource_center.y);
};

// Settlement
CatanMapView.Token.Settlement = function () {
    CatanMapView.Token.apply(this, arguments);

    // get the roll value from the element attributes
};

CatanMapView.Token.Settlement.prototype = new CatanMapView.Token();

CatanMapView.Token.Settlement.prototype.initDOM = function (element) {
    HexMap.Token.prototype.initDOM.call(this, element);
    if (element instanceof Element) {
        if (element.hasAttribute("player")) {
            this.player = element.getAttribute('player');
        } 
    }
};

CatanMapView.Token.Settlement.prototype.draw = function () {
    var ctx = this.map.canvas.getContext('2d');
    var hexcenter = this.center();

    ctx.fillStyle = this.player;
    ctx.strokeStyle = "black";
    ctx.lineWidth = 2;
    
    var boxwidth = this.map.hexrun / 2;

    ctx.beginPath();
    ctx.moveTo(hexcenter.x - boxwidth, hexcenter.y - boxwidth);
    ctx.lineTo(hexcenter.x - boxwidth, hexcenter.y + boxwidth);
    ctx.lineTo(hexcenter.x + boxwidth, hexcenter.y + boxwidth);
    ctx.lineTo(hexcenter.x + boxwidth, hexcenter.y - boxwidth);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
}

// City
CatanMapView.Token.City = function () {
    CatanMapView.Token.apply(this, arguments);

    // get the roll value from the element attributes
};

CatanMapView.Token.City.prototype = new CatanMapView.Token();

CatanMapView.Token.City.prototype.initDOM = function (element) {
    HexMap.Token.prototype.initDOM.call(this, element);
    if (element instanceof Element) {
        if (element.hasAttribute("player")) {
            this.player = element.getAttribute('player');
        } 
    }
};

CatanMapView.Token.City.prototype.draw = function () {
    var ctx = this.map.canvas.getContext('2d');
    var hexcenter = this.center();

    ctx.fillStyle = this.player;
    ctx.strokeStyle = "black";
    ctx.lineWidth = 2;
    
    var boxwidth = this.map.hexrun;

    ctx.beginPath();
    ctx.moveTo(hexcenter.x - boxwidth, hexcenter.y - boxwidth);
    ctx.lineTo(hexcenter.x - boxwidth, hexcenter.y + boxwidth);
    ctx.lineTo(hexcenter.x + boxwidth, hexcenter.y + boxwidth);
    ctx.lineTo(hexcenter.x + boxwidth, hexcenter.y - boxwidth);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
}

// roads
CatanMapView.Token.Road = function () {
    CatanMapView.Token.apply(this, arguments);

    // get the roll value from the element attributes
};

CatanMapView.Token.Road.prototype = new CatanMapView.Token();

CatanMapView.Token.Road.prototype.initDOM = function (element) {
    HexMap.Token.prototype.initDOM.call(this, element);
    if (element instanceof Element) {
        if (element.hasAttribute("player")) {
            this.player = element.getAttribute('player');
        } 
    }
};

CatanMapView.Token.Road.prototype.draw = function () {
    var ctx = this.map.canvas.getContext('2d');

    // roads belong in two adjacent hexes
    var start = this.center(this.locations[0]);
    var end = this.center(this.locations[1]);

    ctx.strokeStyle = this.player;
    ctx.lineWidth = 7;

    ctx.beginPath();
    ctx.moveTo(start.x, start.y);
    ctx.lineTo(end.x, end.y);
    ctx.stroke();

}
