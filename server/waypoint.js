var _ = require('lodash');

function Waypoint (options) {
    if (!(instanceof Waypoint)) {
        return new Waypoint;
    }

    this.waypoints = options.waypoints || [];

    _.bindAll(this,
        'register',
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