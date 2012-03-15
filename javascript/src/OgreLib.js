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

/*
OgreMapView.prototype.terrain_types = {
    'plain': HexMapView.Terrain.Border,
    'crater': OgreMapView.Terrain.Crater,
    'rubble': OgreMapView.Terrain.Rubble
};
*/

// Generic Ogre Terrain
OgreMapView.Terrain = function() {
    HexMapView.Terrain.apply(this, arguments);
};

OgreMapView.Terrain.prototype = new HexMapView.Terrain();

OgreMapView.prototype.terrain_types['terrain'] = OgreMapView.Terrain;

// Generic Warp War Token
OgreMapView.Token = function() {
    HexMapView.Token.apply(this, arguments);
};

OgreMapView.Token.prototype = new HexMapView.Token();

/**
 * Terrains
 */

OgreMapView.prototype.terrain_types['plain'] = HexMapView.Terrain.Border;


// base star
OgreMapView.Terrain.Crater = function() {
    OgreMapView.Terrain.apply(this, arguments);
};

OgreMapView.prototype.terrain_types['crater'] = OgreMapView.Terrain.Crater;

OgreMapView.Terrain.Crater.prototype = new OgreMapView.Terrain();

OgreMapView.Terrain.Crater.prototype.drawHex = function(hex) {
    var ctx = this.map.canvas.getContext("2d");
    var center = hex.center();

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

OgreMapView.prototype.terrain_types['rubble'] = OgreMapView.Terrain.Rubble;

OgreMapView.Terrain.Rubble.prototype = new OgreMapView.Terrain();

OgreMapView.Terrain.Rubble.prototype.initDOM = function(element) {
    HexMap.Terrain.prototype.initDOM.call(this, element);
    if (element instanceof Element) {
        if (element.hasAttribute("hexside")) {
            this.hexside = element.getAttribute('hexside');
        } 
    }
};

OgreMapView.Terrain.Rubble.prototype.draw = function() {
    var ctx = this.map.canvas.getContext("2d");
    ctx.strokeStyle = "brown";
    ctx.lineWidth = 6;

    var vertices0 = this.map.getHex(this.locations[0]).vertices();
    var vertices1 = this.map.getHex(this.locations[1]).vertices();

    var common = [];

    for (var i = 0 ; i < vertices0.length ; i++) {
        var p0 = vertices0[i];
        for (var j = 0 ; j < vertices1.length ; j++) {
            var p1 = vertices1[j];
            if (p0.equals(p1)) {
                common.push(p0);
            }
        }
    }

    if (common.length == 2) {
        ctx.beginPath();
        ctx.moveTo(common[0].x, common[0].y);
        ctx.lineTo(common[1].x, common[1].y);
        ctx.closePath();
        ctx.stroke();
    }

};

OgreMapView.Terrain.Rubble.prototype.drawHex = function(hex) {
    var ctx = this.map.canvas.getContext("2d");
    var center = hex.center();

    var facing = parseInt(this.hexside);
    var colors = ['red', 'green', 'yellow', 'blue', 'orange', 'purple'];
    var dec = [
        [new Point(4, 0), new Point(0, 4)],
        [new Point(4, 2), new Point(-4, 2)],
        [new Point(0, 4), new Point(-4, 0)],

        [new Point(-4, 4), new Point(-2, -4)],
        [new Point(-4, -2), new Point(4, -2)],
        [new Point(2, -2), new Point(2, 0)],
    ];

    ctx.strokeStyle = colors[facing];

    //ctx.strokeStyle = "brown";
    ctx.lineWidth = 4;

    // get the border vertices
    var vertices = hex.vertices();
    var v0 = vertices[facing];
    var v1 = vertices[facing + 1];
    if (v1 == undefined) {
        v1 = vertices[0];
    }
        
    ctx.beginPath();

    ctx.moveTo(v0.x + dec[facing][0].x, v0.y + dec[facing][0].y);
    ctx.lineTo(v1.x + dec[facing][1].x, v1.y + dec[facing][1].y);

    ctx.closePath();

    ctx.stroke();
};
