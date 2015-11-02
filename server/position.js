var _ = require('lodash');

function Position (options) {
    if (!(this instanceof Position)) {
        return new Position;
    }

    _.bindAll(this,
        'register',
        'getAll',
        'getGPS',
        'postGPS',
        'getHeadingGPS',
        'postHeadingGPS',
        'getHeadingMag',
        'postHeadingMag',
        'getSpeed',
        'postSpeed');

}

module.exports = Position;

Position.register = function (options, router) {
    var position = new Position(options);
    position.register(router);
}

Position.prototype.register =  function register (router) {
    router.route('/position')
        .get(this.getAll);

    router.route('/position/gps')
        .get(this.getGPS)
        .post(this.postGPS);

    router.route('/position/heading/gps')
        .get(this.getHeadingGPS)
        .post(this.postHeadingGPS);

    router.route('/position/heading/magnetic')
        .get(this.getHeadingMag)
        .post(this.postHeadingMag);

    router.route('/position/speed')
        .get(this.getSpeed)
        .post(this.postSpeed);
}

Position.prototype.getAll = function getAll (req, res, next) {
    var pos_data = {};
    pos_data.gps.lat = this.boat_data["Latitude"];
    pos_data.gps.long = this.boat_data["Longitude"];
    pos_data.gps.heading = this.boat_data["COG"];
    pos_data.mag.heading = this.boat_data["Heading"];
    pos_data.speed = this.boat_data["SOG"];

    res.status(200).json(pos_data);
}

Position.prototype.getGPS = function getGPS (req, res, next) {
    var pos_data = {};
    pos_data.gps.lat = this.boat_data["Latitude"];
    pos_data.gps.long = this.boat_data["Longitude"];

    res.status(200).json(pos_data);
}

Position.prototype.postGPS = function postGPS (req, res, next) {
    this.boat_data = _.assign(boat_data, req.body);
    res.sendStatus(200);
}

Position.prototype.getHeadingGPS = function getHeadingGPS (req, res, next) {
    var pos_data = {};
    pos_data.gps.heading = this.boat_data["COG"];

    res.status(200).json(pos_data);
}

Position.prototype.postHeadingGPS = function postHeadingGPS (req, res, next) {
    this.boat_data = _.assign(boat_data, req.body);
    res.sendStatus(200);
}

Position.prototype.getHeadingMag = function getHeadingMag (req, res, next) {
    var pos_data = {};
    pos_data.mag.heading = this.boat_data["Heading"];

    res.status(200).json(pos_data);
}

Position.prototype.postHeadingMag = function postHeadingMag (req, res, next) {
    this.boat_data = _.assign(boat_data, req.body);
    res.sendStatus(200);
}

Position.prototype.postSpeed = function postSpeed (res, req, next) {
    var pos_data = {};
    pos_data.speed = this.boat_data["SOG"];

    res.status(200).json(pos_data);
}

Position.prototype.postSpeed = function postSpeed (req, res, next) {
    this.boat_data = _.assign(boat_data, req.body);
    res.sendStatus(200);
}