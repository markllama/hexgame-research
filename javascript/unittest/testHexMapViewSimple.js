// get the sample map definition
sampleUrl="https://lamourine.homeunix.org/~mark/hexgame/data/xml/sample.xml";
      
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

// extract the map size from the map document.
sizeVectorElement = sample.evaluate(
    'map/size', 
    sample, 
    null, 
    XPathResult.FIRST_ORDERED_NODE_TYPE, 
    null
).singleNodeValue;

// really should check that the size has a single vectorl
mapsize = HexMap.Vector.fromDOM(sizeVectorElement.firstChild)

terrainnodes = sample.evaluate(
    'map/terrains/terrain', 
    sample, 
    null,
    XPathResult.UNORDERED_NODE_LIST_TYPE, 
    null
);

// iterate over terrainnodes

