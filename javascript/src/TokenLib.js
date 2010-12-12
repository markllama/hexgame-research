/**
 *
 */
HexMapView.Token.Box = function(map) {
    HexMapView.Token.apply(this, arguments);
};

HexMapView.Token.Box.prototype = new HexMapView.Token();

HexMapView.Token.Box.draw = function() {

};

/**
 *
 */
HexMapView.Token.Image = function() {
    HexMapView.Token.apply(this, arguments);

    this.images = {};
    if (arguments[1] && arguments[1] instanceof Element) {
	this.img = new Image();
	this.images = {};

	var telement = arguments[1];
	var doc = telement.ownerDocument;
	var imglist = doc.evaluate('images/img', telement, null,
				   XPathResult.ORDERED_LIST_ITERATOR_TYPE,
				   null);
	for (var i = imglist.iterateNext() ; i ; i = imglist.iterateNext()) {
	    var imgname = i.getAttribute('name');
	    var imgpath = i.getAttribute('src');

	    var imgurl = this.map.baseUrl + imgpath;

	    // the first image is the initial state
	    if (!this.state) {
		this.state = imgname;
	    }

	    this.images[imgname] = imgurl;
	    // prefetch each image file
	    // and wait while it comes.
	    var img = new Image();
	    img.src = imgurl;
	    this.map.images.push(img);
	}

	this.img.src = this.images[this.state];
    }

};

HexMapView.Token.Image.prototype = new HexMapView.Token();

HexMapView.Token.Image.prototype.toString = function() {
    return "[object HexMapView.Token.Image]";
};

/**
 * Draw a single token
 */
HexMapView.Token.Image.prototype.draw = function() {
    
    var map = this.map;
    var ctx = map.canvas.getContext('2d');
    var size = this.size();
    var corner = this.corner();

    this.img.src = this.images[this.state];
    
    ctx.drawImage(this.img, corner.x, corner.y, size.x, size.y);
};

