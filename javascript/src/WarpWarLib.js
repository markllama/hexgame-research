/**
 *
 *
 */

WarpWarMapView = function (canvas, hexrun, size, origin) {
    HexMapView.apply(this, arguments);
};

WarpWarMapView.prototype = new HexMapView();

WarpWarMapView.prototype.toString = function() {
    return "[object WarpWarMapView]";
};

// Generic Warp War Terrain
WarpWarMapView.Terrain = function() {
    HexMapView.Terrain.apply(this, arguments);
};

WarpWarMapView.Terrain.prototype = new HexMapView.Terrain();

WarpWarMapView.prototype.terrain_types['terrain'] = WarpWarMapView.Terrain;

// Generic Warp War Token
WarpWarMapView.Token = function() {
    HexMapView.Token.apply(this, arguments);
};

WarpWarMapView.Token.prototype = new HexMapView.Token();

/**
 * Terrains
 */

// base star
WarpWarMapView.Terrain.BaseStar = function() {
    WarpWarMapView.Terrain.apply(this, arguments);
};

WarpWarMapView.Terrain.BaseStar.prototype = new WarpWarMapView.Terrain();

WarpWarMapView.prototype.terrain_types['basestar'] = WarpWarMapView.Terrain.BaseStar;

WarpWarMapView.Terrain.BaseStar.prototype.drawHex = function(hex) {
    var ctx = this.map.canvas.getContext("2d");
    var center = hex.center();

    ctx.fillStyle = "black";
    ctx.lineWidth = 2;

    var r = this.map.hexrun / 2 ;
    
    ctx.beginPath();
    ctx.moveTo(center.x, center.y + r);
    ctx.lineTo(center.x, center.y - r);
    ctx.moveTo(center.x - r, center.y);
    ctx.lineTo(center.x + r , center.y);
               
    ctx.closePath();

    ctx.stroke();

    ctx.textBaseline = "middle";
    ctx.textAlign = "center";
    ctx.fillText(this.name, center.x, center.y - this.map.hexrun);

    //ctx.
};

// star
WarpWarMapView.Terrain.Star = function() {
    WarpWarMapView.Terrain.apply(this, arguments);
};

WarpWarMapView.Terrain.Star.prototype = new WarpWarMapView.Terrain();

WarpWarMapView.prototype.terrain_types['star'] = WarpWarMapView.Terrain.Star;

WarpWarMapView.Terrain.Star.prototype.drawHex = function(hex) {
    var ctx = this.map.canvas.getContext("2d");
    var center = hex.center();

    ctx.fillStyle = "black";
    ctx.lineWidth = 2;

    var r = this.map.hexrun / 3 ;
    
    ctx.beginPath();
    ctx.moveTo(center.x, center.y + r);
    ctx.lineTo(center.x, center.y - r);
    ctx.moveTo(center.x - r, center.y);
    ctx.lineTo(center.x + r , center.y);
               
    ctx.closePath();

    ctx.stroke();

    ctx.textBaseline = "middle";
    ctx.textAlign = "center";
    ctx.fillText(this.name, center.x, center.y - this.map.hexrun);

    //ctx.
};

// warpline
WarpWarMapView.Terrain.WarpLine = function() {
    WarpWarMapView.Terrain.apply(this, arguments);
};

WarpWarMapView.Terrain.WarpLine.prototype = new WarpWarMapView.Terrain();

WarpWarMapView.prototype.terrain_types['warpline'] = WarpWarMapView.Terrain.WarpLine;

WarpWarMapView.Terrain.WarpLine.prototype.draw = function() {
    var ctx = this.map.canvas.getContext("2d");
    var c0 = this.map.getHex(this.locations[0]).center();
    var c1 = this.map.getHex(this.locations[1]).center();

    ctx.fillStyle = "black";
    ctx.lineWidth = 2;

    ctx.beginPath();
    ctx.moveTo(c0.x, c0.y);
    ctx.lineTo(c1.x, c1.y);
    ctx.closePath();
    ctx.stroke();    
};
