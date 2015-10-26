var _ = require('lodash');

function Position (options) {
    if (!(instanceof Position)) {
        return new Position;
    }

    this.boat_data = options.boat_data || {};

    _.bindAll(this,
        'register',
        'getAll'
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