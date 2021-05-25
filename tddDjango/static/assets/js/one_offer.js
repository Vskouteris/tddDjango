console.log('linkedddddd -yo')
function addOneLine() {
    var table = document.getElementById("ergasies");
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    cell1.innerHTML = "ΚΑΛΟΥΠΙ";
    cell2.innerHTML = '<input type="search" value="" />';
    cell3.innerHTML = '<input type="search" value="" />';
    cell4.innerHTML = '<input type="search" value="" />';
  }

newErgasiaLIne = document.getElementById("new_line");
newErgasiaLIne.addEventListener('click', function(){
    console.log('plus button pusheddddd');
    addOneLine();
 })
