var _ = require('lodash');

function Wind (options) {
    if (!(this instanceof Wind)) {
        return new Wind;
    }

    _.bindAll(this,
        'register',
        'getApparant',
        'postApparant',
        'getTrue',
        'postTrue');

}

module.exports = Wind;

Wind.register = function (options, router) {
    var wind = new Wind(options);
    wind.register(router);
}

Wind.prototype.register =  function register (router) {
    router.route('/wind')
        .get(this.getBoth);

    router.route('/wind/apparant')
        .get(this.getApparant)
        .post(this.postApparant);

    router.route('/wind/true')
        .get(this.getTrue)
        .post(this.postTrue);
}

Wind.prototype.getBoth = function getBoth (req, res, next) {
    var wind_data = {};
    wind_data.apparant.angle = this.boat_data["App Wind Angle"];
    wind_data.apparant.speed = this.boat_data["App Wind Speed"];
    wind_data.true.angle = this.boat_data["True Wind Angle"];
    wind_data.true.speed = this.boat_data["True Wind Speed"];

    res.status(200).json(wind_data);
}

Wind.prototype.getApparant = function getApparant (req, res, next) {
    var wind_data = {};
    wind_data.apparant.angle = this.boat_data["App Wind Angle"];
    wind_data.apparant.speed = this.boat_data["App Wind Speed"];

    res.status(200).json(wind_data);
}

Wind.prototype.postApparant = function postApparant (req, res, next) {
    this.boat_data = _.assign(boat_data, req.body);
    res.sendStatus(200);
}

Wind.prototype.getTrue = function getTrue (req, res, next) {
    var wind_data = {};
    wind_data.true.angle = this.boat_data["True Wind Angle"];
    wind_data.true.speed = this.boat_data["True Wind Speed"];

    res.status(200).json(wind_data);
}

Wind.prototype.postTrue = function postTrue (req, res, next) {
    this.boat_data = _.assign(boat_data, req.body);
    res.sendStatus(200);
}