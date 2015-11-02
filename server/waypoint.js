var _ = require('lodash');

function Waypoint (options) {
    if (!(this instanceof Waypoint)) {
        return new Waypoint(options);
    }

    this.waypoints = options.waypoints || [];

    _.bindAll(this,
        'getWaypoint',
        'postWaypoint');

}

module.exports = Waypoint;

Waypoint.register = function (options, router) {
    var waypoint = new Waypoint(options);
    waypoint.register(router);
}

Waypoint.prototype.register =  function register (router) {
    router.route('/waypoint')
        .get(this.getWaypoint)
        .post(this.postWaypoint);
}

//TODO: Actual waypoint handling

Waypoint.prototype.getWaypoint = function getWaypoint (req, res, next) {
    res.status(200).send(this.waypoints[0]);
}

Waypoint.prototype.postWaypoint = function postWaypoint (req, res, next) {
    this.waypoints[0] = req.data;
    res.sendStatus(200);
}