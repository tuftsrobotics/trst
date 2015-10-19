var express = require('express');
var _ = require('lodash');
var bodyParser = require('body-parser');


var app = express();


var boat_data = {};

app.use(bodyParser.urlencoded({extended: false}));

app.get('/', function(req, res) {
    res.status(200).json(boat_data);
    //return boat data
})

// req.data is the fields object of the analyzed sensor data
// may change if we want timestamp
.post('/', function(req, res) {
    //change boat data
    console.log('recieved data');
    console.log(req.body);
    boat_data = _.assign(boat_data, req.body);
    console.log(boat_data);
    res.sendStatus(200);
});



var server = app.listen(8888, function() {
    var host = server.address().address;
    var port = server.address().port;

    console.log("Listening at http://%s:%s", host, port);
});

