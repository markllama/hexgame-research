function setUp() {
    m = HexMapView();
}

function testHexMapView() {
    assertTrue("Just a sample", false)
}


// 
defaults = {hx: 14, hy: 22, hexrun: 15};

// get the sample map definition
sampleUrl="https://lamourine.homeunix.org/~mark/hexgame/xml/sample.xml";
      
// you can get XML docs using document.load() in some browsers
// but this is more universal and it really IS an XML document.
// AND you can request XML documents from locations outside the
// document domain.
try {
    sampleRequest = new window.XMLHttpRequest();
    sampleRequest.open('GET', sampleUrl, false);
    sampleRequest.send(null);
    sample = sampleRequest.responseXML;
} catch (e) {
    error(e);
}


size = sample.evaluate('map/@size', sample, null, 
		       XPathResult.STRING_TYPE, null).stringValue;

coords = size.split(',');

mapsize = new HexMap.Vector(Number(coords[0]), Number(coords[1]));

//
terrainspecs = sample.evaluate('map/terrain', sample, null,
			       XPathResult.UNORDERED_NODE_ITERATOR_TYPE, null);

//
function getArgs(defaults) {
    var args = defaults || new Object();
    var query = location.search.substring(1);
    var pairs = query.split("&");
    for (var i = 0; i < pairs.length; i++) {
	var pos = pairs[i].indexOf("=");
	var argname = pairs[i].substring(0,pos);
	var value = pairs[i].substring(pos+1);
	value = decodeURIComponent(value);
	args[argname] = value;
    }
    return args;
}
			  

function createTerrain(spec) {
    var type = spec.getAttribute('type');
    var id = spec.getAttribute('id');
    var name = spec.getAttribute('name');
    
    var tclass = eval(type);
    return new tclass(id, name);
};

function terrainVectors(map, spec) {
    var vlist = [];

    //loc = spec.document.evaluate();
    spec = spec.childNodes[1];

    // get the locations

    // check if it's "all"

    if (spec.getAttribute('all') == 'true') {
	var i = map.iterator();
	for (var hex = i.next() ; hex != null ; hex = i.next()) {
	    vlist.push(hex.location);
	}
    } else if (spec.getAttribute('not') == 'true') {
	// get the list of hexes to be excluded
	var exlist = [];
	for (var i = 0 ; i < spec.childNodes.length ; i++) {
	    var vspec = spec.childNodes[i];
	    if (vspec.nodeType == Node.ELEMENT_NODE && vspec.tagName == "vector") {
		var vector = new HexMap.Vector(Number(vspec.getAttribute('hx')),
					       Number(vspec.getAttribute('hy')));
		exlist.push(vector);
	    }
	}

	// loop through the whole list
	var i = map.iterator();
	for (var hex = i.next() ; hex != null ; hex = i.next()) {
	    // if this hex is in the exclude list, pass over it
	    var include = true;
	    for (var i = 0 ; i < exlist.length ; i++) {
		if (hex.location.equals(exlist[i])) {
		    include = false;
		}
	    }
	    if (include) {
		vlist.push(hex.location);
	    }
	}
    } else {
	for (var i = 0 ; i < spec.childNodes.length ; i++) {
	    var vspec = spec.childNodes[i];
	    if (vspec.nodeType == Node.ELEMENT_NODE && vspec.tagName == "vector") {
		var vector = new HexMap.Vector(Number(vspec.getAttribute('hx')),
					       Number(vspec.getAttribute('hy')));		
		vlist.push(vector);
	    }
	}
    }
    return vlist;
};

//
function createMap(mapid) {
    var args = getArgs(defaults);
    
    map = new HexMapView(Number(args.hexrun), sample.childNodes[0]);

    //map.canvas.addEventListener('click', canvasclick, false);
    map.canvas.onmousemove=canvasclick;
    //map.draw();

    // create a blue and a red center terrain
    var blue = new HexMapView.Terrain.Center(map);
    blue.name = "bluecenter";
    blue.color = "blue";

    // create a blue and a red center terrain
    var red = new HexMapView.Terrain.Center(map);
    red.name = "redcenter";
    red.color = "red";

    var circle = new HexMapView.Terrain.CenterCircle(map);
    circle.name = "circle";
    circle.color = "green";

    map.addTerrain(red);
    map.addTerrain(blue);
    map.addTerrain(circle);
};


function canvasclick(event) {
    // get the mouse (x,y) from the event

    var clickpoint = new Point(event.clientX, event.clientY);
    var clicktext = document.getElementById('clickpoint');  
    clicktext.innerHTML = clickpoint.toString();
    
    var canvascorner = new Point(map.canvas.offsetLeft, map.canvas.offsetTop);
    var canvastext = document.getElementById('canvascorner');
    canvastext.innerHTML = canvascorner.toString();

    var scrollcorner = new Point(window.scrollX, window.scrollY);
    var scrolltext = document.getElementById('scrollcorner');
    scrolltext.innerHTML = scrollcorner.toString();

    var canvaspoint = map.canvasPoint(clickpoint);
    var canvastext = document.getElementById('canvaspoint');
    canvastext.innerHTML = canvaspoint.toString();

    var refhex = map.refloc(canvaspoint);

    var reftext = document.getElementById('refhex');
    reftext.innerHTML = refhex.toString();
	
    var refbox = map.refbox(canvaspoint);
    var refboxtext = document.getElementById('reftriangle');
    refboxtext.innerHTML = refbox.toString();
	
    var clickhex = map.point2vector(canvaspoint);
    var hextext = document.getElementById('clickhex');
    hextext.innerHTML = clickhex.toString();

    if (refhex && map.contains(refhex) && (!map.refhex || (!refhex.equals(map.refhex || !clickhex.equals(map.clickhex))))) {
	var r = map.terrains.redcenter;
	if (map.refboxlist) {
	    for (var i in map.refboxlist) {
		var l = map.refboxlist[i];
		r.removeLocation(l);		
	    }
	}

	map.refboxlist = [];
	// now make the hex triangle color red
	for (var i in refbox) {
	    var l = refbox[i];
	    if (map.contains(l)) { r.addLocation(l); map.refboxlist.push(l); }
	}

	var b = map.terrains.bluecenter;
	map.refhex && b.removeLocation(map.refhex);
	
	if (map.contains(refhex)) {
	    b.addLocation(refhex);
	    // save the ref hex so we know to redraw
	    map.refhex = refhex;
	}

	var c = map.terrains.circle;
	map.clickhex && c.removeLocation(map.clickhex);

	if (map.contains(clickhex)) {
	    c.addLocation(clickhex);
	    map.clickhex = clickhex;
	}

	map.draw();
    }
};