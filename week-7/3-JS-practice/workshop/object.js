'use strict';

/*

var humwee = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 20000
};

function ride(car, km) {
  car.km += km;
}

ride(humwee, 200);

console.log(humwee.km);

*/

var humwee = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 20000,
  ride: function(km) {
    this.km += km;
  }
};

humwee.ride(200)

console.log(humwee.km);
