var express = require('express');
var _ = require('lodash');
var bodyParser = require('body-parser');
var Wind = require('./wind');
var Position = require('./position')
var Waypoint = require('./waypoint')


function Application (options) {
    if (!(this instanceof Application)) {
        return new Aplication(options);
    }

    this.boat_data = options.boat_data || {};
    // TODO: check for boat data in all modules
    this.Wind = options.Wind || Wind;
    this.Position = options.Position || Position;
    this.Waypoint = options.Waypoint || Waypoint;

    this.app = options.app || express();
    app.use(bodyParser.urlencoded({extended: false}));

    var api = app.Router();

    this.app.use(api);
    this.registerAll(options, api);

    _.bindAll(this,
        'register',
        'registerAll',
        'get',
        'post',
        'listen');
}

module.exports = Application;

Application.prototype.registerAll = function registerAll (options, router) {
    this.register(router);
    this.Wind.register(options, router);
    this.Position.register(options, router);
    this.Waypoint.register(options, router);
}

Application.prototype.register = function register (router) {
    router.route('/')
        .get(this.get);
        .post(this.post);
}

Application.prototype.get = function get (req, res, next) {
    res.status(200).json(this.boat_data);
    next();
}

Application.prototype.post = function post (req, res, next) {
    this.boat_data = _.assign(boat_data, req.body);
    res.sendStatus(200);
}


Application.prototype.listen = function listen () {
    var _this = this;
    this.server = this.app.listen(8888, function() {
        var host = _this.server.address().address;
        var port = _this.server.address().port;

        console.log("Listening at http://%s:%s", host, port);
    });    
}


