'use strict';

function Student(name, grades) {
  this.name = name;
  this.grades = grades;
  this.addGrade = function(grade) {
    this.grades.push(grade);
    }
}

var jozsi = new Student('Jozsi', []);

jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);

console.log(jozsi.grades);


function getAverage(student) {
  var sum = student.grades.reduce(function(acc, i) {
    return acc + i;
    }, 0);
    return sum / student.grades.length;
  }

console.log(getAverage(jozsi));
