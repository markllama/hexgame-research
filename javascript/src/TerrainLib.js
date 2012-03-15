/**
 * A terrain that draws the border of the hex
 * @extends 
 */
HexMapView.Terrain.Border = function() {
    this.isborder = true;
    HexMapView.Terrain.apply(this, arguments);
};

HexMapView.Terrain.Border.prototype = new HexMapView.Terrain();

HexMapView.prototype.terrain_types['border'] = HexMapView.Terrain.Border;

HexMapView.Terrain.Border.prototype.toString = function() {
    return "[object HexMapView.Terrain.Border]";
};

/**
 * Draw the border around a hex
 */
HexMapView.Terrain.Border.prototype.drawHex = function(hex) {
    // get the map graphics context
    var ctx = this.map.canvas.getContext('2d');
    var vertices = hex.vertices();
    ctx.strokeStyle = "black";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(vertices[0].x, vertices[0].y);
    ctx.lineTo(vertices[1].x, vertices[1].y);
    ctx.lineTo(vertices[2].x, vertices[2].y);
    ctx.lineTo(vertices[3].x, vertices[3].y);
    ctx.lineTo(vertices[4].x, vertices[4].y);
    ctx.lineTo(vertices[5].x, vertices[5].y);
    ctx.closePath();
    ctx.stroke();
};


/**
 * A terrain that draws a dot in the center of a hex
 * @extends 
 */
HexMapView.Terrain.Center = function() {
    HexMapView.Terrain.apply(this, arguments);
    //
    // set the color
    this.name = "center";
    this.color = "black";
};

HexMapView.Terrain.Center.prototype = new HexMapView.Terrain();

HexMapView.prototype.terrain_types['center'] = HexMapView.Terrain.Center;

HexMapView.Terrain.Center.prototype.toString = function() {
    return "[object HexMapView.Terrain.Center]";
};

/**
 * Draw a dot in the center of a hex
 */
HexMapView.Terrain.Center.prototype.drawHex = function(hex) {
    // get the map graphics context
    var ctx = this.map.canvas.getContext('2d');
    var center = hex.center();
    ctx.fillStyle = this.color;
    ctx.strokeStyle = this.color;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(center.x-3 , center.y-3);
    ctx.lineTo(center.x+3 , center.y-3);
    ctx.lineTo(center.x+3 , center.y+3);
    ctx.lineTo(center.x-3 , center.y+3);
    ctx.closePath();
    ctx.fill();
    
};

/**
 * A terrain that draws a dot in the center of a hex
 * @extends 
 */
HexMapView.Terrain.CenterCircle = function() {
    HexMapView.Terrain.apply(this, arguments);
    //
    // set the color
    this.name = "center";
    this.color = "black";
};

HexMapView.Terrain.CenterCircle.prototype = new HexMapView.Terrain();

HexMapView.prototype.terrain_types['centercircle'] = HexMapView.Terrain.CenterCircle;

HexMapView.Terrain.CenterCircle.prototype.toString = function() {
    return "[object HexMapView.Terrain.CenterCircle]";
};

/**
 * Draw a dot in the center of a hex
 */
HexMapView.Terrain.CenterCircle.prototype.drawHex = function(hex) {
    // get the map graphics context
    var ctx = this.map.canvas.getContext('2d');
    var center = hex.center();
    ctx.fillStyle = this.color;
    ctx.strokeStyle = this.color;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(center.x, center.y);
    ctx.arc(center.x, center.y, 8, 0, Math.PI * 2, false);
    ctx.closePath();
    ctx.stroke();
    
};


/**
 * A terrain that draws the border of the hex
 * @extends 
 */
HexMapView.Terrain.SuperBorder = function() {
    this.isborder = true;
    HexMapView.Terrain.apply(this, arguments);
    this.fillStyle = undefined ;
};

HexMapView.Terrain.SuperBorder.prototype = new HexMapView.Terrain();

HexMapView.prototype.terrain_types['superborder'] = HexMapView.Terrain.SuperBorder;

HexMapView.Terrain.SuperBorder.prototype.toString = function() {
    return "[object HexMapView.Terrain.SuperBorder]";
};

/**
 * Draw the border around a hex
 */
HexMapView.Terrain.SuperBorder.prototype.drawHex = function(hex) {
    // get the map graphics context
    var ctx = this.map.canvas.getContext('2d');
    //var vertices = this.vertices(hex);
    var vertices = this.vertices(hex);

    ctx.strokeStyle = "black";
    ctx.lineWidth = 1;

    if (this.fillStyle) {
        ctx.fillStyle = this.fillStyle;
    }

    this.setPath(ctx, vertices);
    ctx.stroke();

    if (this.fillStyle) {
        ctx.fill();
    }
};

HexMapView.Terrain.SuperBorder.prototype.setPath = function(ctx, vertices) {
    ctx.beginPath();
    ctx.moveTo(vertices[0].x, vertices[0].y);
    ctx.lineTo(vertices[1].x, vertices[1].y);
    ctx.lineTo(vertices[2].x, vertices[2].y);
    ctx.lineTo(vertices[3].x, vertices[3].y);
    ctx.lineTo(vertices[4].x, vertices[4].y);
    ctx.lineTo(vertices[5].x, vertices[5].y);
    ctx.closePath();
}

HexMapView.Terrain.SuperBorder.prototype.vertices = function(hex) {
    var vlist = [];
    for (var vu in HexMap.Vector.UNIT) {
        var vh = hex.location.add(HexMap.Vector.UNIT[vu]);
        var vp = this.map.hexcenter(vh);
        vlist.push(vp);
    };

    return vlist;
}

/**
 *
 */
HexMapView.Terrain.Image = function() {
    HexMapView.Terrain.apply(this, arguments);

    if (arguments[1] && arguments[1] instanceof Element) {
	this.img = new Image();
	this.imgsrc = {};

	var telement = arguments[1];
	var doc = telement.ownerDocument;
	var imglist = doc.evaluate('images/img', telement, null,
				   XPathResult.ORDERED_LIST_ITERATOR_TYPE,
				   null);
	for (var i = imglist.iterateNext() ; i ; i = imglist.iterateNext()) {
	    var imgname = i.getAttribute('name');
	    var imgpath = i.getAttribute('src');

	    var imgurl = this.map.baseUrl + imgpath
	    if (!this.firsturl) {
		this.firsturl = imgurl
	    }

	    this.imgsrc[imgname] = imgurl;
	    // prefetch each image file
	    // and wait while it comes.
	    var img = new Image();
	    img.src = imgurl;
	    this.map.images.push(img);
	}

	this.img.src = this.firsturl;
    }


};

HexMapView.Terrain.Image.prototype = new HexMapView.Terrain();

HexMapView.prototype.terrain_types['image'] = HexMapView.Terrain.Image;

HexMapView.Terrain.Image.prototype.toString = function() {
    return "[object HexMapView.Terrain.Image]";
};

/**
 * determine the size of a terrain image
 * @type Point
 * @return the dimensions of a hex terrain image in pixels
 */
HexMapView.Terrain.Image.prototype.imageSize = function() {
    return new Point(this.map.hexwidth, this.map.hexheight);
};

/**
 * determine the location of the image corner for a Terrain image
 * @param {Hex} the hex location
 * @type Point
 * @return the location of an image for the terrain
 */
HexMapView.Terrain.Image.prototype.imageCorner = function(hex) {
    //var c = this.map.hexcenter(hex.location);
    return new Point(- this.map.hexradius, -this.map.hexrise);
};

HexMapView.Terrain.Image.setMap = function(map) {
    this.map = map;
    
    var imagesize = this.imageSize();
    this.image = new Image(imagesize.x, imagesize.y);
};

HexMapView.Terrain.Image.setSrc = function(src) {
    this.image.src = src;
};

/**
 * draw the terrain image in a hex
 * @param {Hex} hex where to place the image
 */
HexMapView.Terrain.Image.drawHex = function(hex, facing) {
    // 
    var ctx = this.map.canvas.getContext('2d');
    var center = this.map.hexcenter(hex.location);
    var corner = this.imageCorner(hex);
    var imgSize = this.imageSize();
    var img = this.img;

    // make sure the image has loaded
    if (this.img.src) {
	if (!this.img.complete) {
	    var src = this.img.src;
	    this.img.onload = function() {
		ctx.save();
		ctx.translate(center.x, center.y);
		if (facing) {
		    ctx.rotate(Math.PI / 3 * (facing));
		}
		ctx.drawImage(img, corner.x, corner.y, imgSize.x, imgSize.y);
		ctx.restore();
	    }
	    this.img.src = src;
	} else { 
	    ctx.save();
	    ctx.translate(center.x, center.y);
	    if (facing) {
		ctx.rotate(Math.PI / 3 * (facing));
	    }
	    ctx.drawImage(img, corner.x, corner.y, imgSize.x, imgSize.y);
	    ctx.restore();
	}
    }
};
