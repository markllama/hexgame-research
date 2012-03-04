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

