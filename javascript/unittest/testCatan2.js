// get the sample map definition
catanUrl="https://lamourine.homeunix.org/~mark/hexgame/data/xml/catan34.xml";

defaults = {hexrun: 15, mapurl: catanUrl};


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


function init() {
    var args = getArgs(defaults);

    // you can get XML docs using document.load() in some browsers
    // but this is more universal and it really IS an XML document.
    // AND you can request XML documents from locations outside the
    // document domain.
    try {
        var mapRequest = new window.XMLHttpRequest();
        mapRequest.open('GET', args.mapurl, false);
        mapRequest.send(null);
        var mapspec = mapRequest.responseXML;
    } catch (e) {
        error(e);
    }

    canvas = document.getElementById('catanmap');

    var mapview = new CatanMapView(canvas, args.hexrun, mapspec);

    mapview.draw();
};
