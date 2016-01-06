
function triangle(num) {
  output = '';
  for (var i = 1; i < num; i++) {
    output += ' ';
  }
  output += '#';
  for (var i = 1; i <= num; i++) {
    console.log(output);
    output += '##';
  }
}




triangle(3);
/*
  #
 ###
#####
*/

triangle(5);
/*
    #
   ###
  #####
 #######
#########
*/
