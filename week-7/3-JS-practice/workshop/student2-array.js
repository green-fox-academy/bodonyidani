'use strict';

function Student() {
  this.grades = [];
  this.addGrade = function(subject, grade) {
    this.grades.push({subject: subject, grade: grade});
  };
  this.getCount = function() {
    var output = {};
    this.grades.forEach(function(grade) {
      if (!(grade.subject in output)) {
        output[grade.subject] = 0;
      }
      output[grade.subject]++;
    });
    return output;
  }
}

var dezso = new Student();

dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);
dezso.addGrade('magyar', 4);

console.log(dezso.grades)
console.log(dezso.getCount())


//dezso.getCount() // {'rajz': 2, 'matek': 3}
//dezso.getAverage() // 3.4
// szorgalmi
//dezso.getAverageBySubject() // {'matek': 4.33, 'rajz': 2}
