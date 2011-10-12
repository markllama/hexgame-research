// get the sample map definition
sampleUrl="https://lamourine.homeunix.org/~mark/hexgame/data/xml/sample.xml";

defaults = {hexrun: 15, mapurl: sampleUrl};

      

// now create the map view
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

function canvasclick(event) {
    // get the mouse (x,y) from the event

    var clickpoint = new Point(event.clientX, event.clientY);
    var clicktext = document.getElementById('clickpoint');  
    clicktext.innerHTML = clickpoint.toString();
    
    var canvascorner = new Point(mapview.canvas.offsetLeft, mapview.canvas.offsetTop);
    var canvastext = document.getElementById('canvascorner');
    canvastext.innerHTML = canvascorner.toString();

    var scrollcorner = new Point(window.scrollX, window.scrollY);
    var scrolltext = document.getElementById('scrollcorner');
    scrolltext.innerHTML = scrollcorner.toString();

    var canvaspoint = mapview.canvasPoint(clickpoint);
    var canvastext = document.getElementById('canvaspoint');
    canvastext.innerHTML = canvaspoint.toString();

    var refhex = mapview.refloc(canvaspoint);

    var reftext = document.getElementById('refhex');
    reftext.innerHTML = refhex.toString();
	
    var refbox = mapview.refbox(canvaspoint);
    var refboxtext = document.getElementById('reftriangle');
    refboxtext.innerHTML = refbox.toString();
	
    var clickhex = mapview.point2vector(canvaspoint);
    var hextext = document.getElementById('clickhex');
    hextext.innerHTML = clickhex.toString();

    if (refhex && mapview.contains(refhex) && (!mapview.refhex || (!refhex.equals(mapview.refhex || !clickhex.equals(mapview.clickhex))))) {
	var r = mapview.terrains.redcenter;
	if (mapview.refboxlist) {
	    for (var i in mapview.refboxlist) {
		var l = mapview.refboxlist[i];
		r.removeLocation(l);		
	    }
	}

	mapview.refboxlist = [];
	// now make the hex triangle color red
	for (var i in refbox) {
	    var l = refbox[i];
	    if (mapview.contains(l)) { r.addLocation(l); mapview.refboxlist.push(l); }
	}

	var b = mapview.terrains.bluecenter;
	mapview.refhex && b.removeLocation(mapview.refhex);
	
	if (mapview.contains(refhex)) {
	    b.addLocation(refhex);
	    // save the ref hex so we know to redraw
	    mapview.refhex = refhex;
	}

	var c = mapview.terrains.circle;
	mapview.clickhex && c.removeLocation(mapview.clickhex);

	if (mapview.contains(clickhex)) {
	    c.addLocation(clickhex);
	    mapview.clickhex = clickhex;
	}

	mapview.draw();
    }
};


args = getArgs(defaults);

// you can get XML docs using document.load() in some browsers
// but this is more universal and it really IS an XML document.
// AND you can request XML documents from locations outside the
// document domain.
try {
    sampleRequest = new window.XMLHttpRequest();
    sampleRequest.open('GET', args.mapurl, false);
    sampleRequest.send(null);
    sample = sampleRequest.responseXML;
} catch (e) {
    error(e);
}

mapelement = sample.getElementsByTagName("map")[0];

mapview = new HexMapView(args.hexrun, mapelement);
mapview.canvas.onmousemove=canvasclick;

// create and add the standard terrains


// create a blue and a red center terrain
var blue = new HexMapView.Terrain.Center(mapview);
blue.name = "bluecenter";
blue.color = "blue";

// create a blue and a red center terrain
var red = new HexMapView.Terrain.Center(mapview);
red.name = "redcenter";
red.color = "red";

var circle = new HexMapView.Terrain.CenterCircle(mapview);
circle.name = "circle";
circle.color = "green";

mapview.addTerrain(red);
mapview.addTerrain(blue);
mapview.addTerrain(circle);
