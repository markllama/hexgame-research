/**
 *
 *
 */

OgreMapView = function (canvas, hexrun, size, origin) {
    HexMapView.apply(this, arguments);
};

OgreMapView.prototype = new HexMapView();

OgreMapView.prototype.toString = function() {
    return "[object OgreMapView]";
};

// Generic Warp War Terrain
OgreMapView.Terrain = function() {
    HexMapView.Terrain.apply(this, arguments);
};

OgreMapView.Terrain.prototype = new HexMapView.Terrain();

// Generic Warp War Token
OgreMapView.Token = function() {
    HexMapView.Token.apply(this, arguments);
};

OgreMapView.Token.prototype = new HexMapView.Token();

/**
 * Terrains
 */

// base star
OgreMapView.Terrain.Crater = function() {
    OgreMapView.Terrain.apply(this, arguments);
};

OgreMapView.Terrain.Crater.prototype = new OgreMapView.Terrain();

OgreMapView.Terrain.Crater.prototype.drawHex = function(hex) {
    var ctx = this.map.canvas.getContext("2d");
    var center = hex.center();

    ctx.strokeStyle = "black";
    ctx.fillStyle = "brown";
    ctx.lineWidth = 4;

    var r = this.map.hexrun ;
    
    ctx.beginPath();
    ctx.arc(center.x, center.y, r, 0, Math.PI * 2, false);
    ctx.closePath();
    ctx.stroke();
    ctx.fill();
    
};

// rubble
OgreMapView.Terrain.Rubble = function() {
    OgreMapView.Terrain.apply(this, arguments);
};

OgreMapView.Terrain.Rubble.prototype = new OgreMapView.Terrain();

OgreMapView.Terrain.Rubble.prototype.initDOM = function(element) {
    HexMap.Terrain.prototype.initDOM.call(this, element);
    if (element instanceof Element) {
        if (element.hasAttribute("hexside")) {
            this.hexside = element.getAttribute('hexside');
        } 
    }
};

OgreMapView.Terrain.Rubble.prototype.drawHex = function(hex) {
    var ctx = this.map.canvas.getContext("2d");
    var center = hex.center();

    ctx.strokeStyle = "brown";
    ctx.lineWidth = 4;

    // get the border vertices
    var vertices = hex.vertices();
    var v0 = vertices[parseInt(this.hexside)];
    var v1 = vertices[parseInt(this.hexside) + 1];
    if (v1 == undefined) {
        v1 = vertices[0];
    }
        
    ctx.beginPath();

    ctx.moveTo(v0.x, v0.y);
    ctx.lineTo(v1.x, v1.y);

    ctx.closePath();

    ctx.stroke();
};
