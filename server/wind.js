var _ = require('lodash');

function Wind (options) {
    if (!(instanceof Wind)) {
        return new Wind;
    }

    this.boat_data = options.boat_data || {};

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

