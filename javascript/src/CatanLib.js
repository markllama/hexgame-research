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


CatanMapView.Terrain.Mountain = function() {
    // call the superclass constructor
    HexMapView.Terrain.SuperHex.apply(this, arguments);
}

CatanMapView.Terrain.Mountain.prototype = HexMapView.Terrain.SuperHex ;