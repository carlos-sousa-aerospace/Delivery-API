function httpGetAsync(theUrl, callback) {
    const xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            callback(xmlHttp.responseText);
        }
    }
    xmlHttp.open("Get", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

window.onload = function() {
    httpGetAsync("http://127.0.0.1:5000/store", function(response) {
        document.getElementById("myElement").innerHTML = response
    })
}

