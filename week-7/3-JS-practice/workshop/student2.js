'use strict';

function Student(name, grades) {
  this.name = name;
  this.grades = grades;
  this.addGrade = function(subject, grade) {
    this.grades.push({subject: subject, grade: grade});
  };
}

var dezso = new Student('Dezso', []);

dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);

console.log(dezso.grades)


//dezso.getCount() // {'rajz': 2, 'matek': 3}
//dezso.getAverage() // 3.4
// szorgalmi
//dezso.getAverageBySubject() // {'matek': 4.33, 'rajz': 2}
