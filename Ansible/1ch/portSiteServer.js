var http = require('http');
     fs  = require('fs');

fs.readFile('./scribbler/index.html', function (err, html) {
    if (err) {
        throw err; 
    }                                     
        //var server = http.createServer(function(req, res) {
           http.createServer(function(req, res) { 
                res.writeHead(200, {"Content-Type": "text/html"});
                res.write(html);
                res.end();
        }).listen(8080);
});