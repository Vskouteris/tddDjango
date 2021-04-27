// console.log("all_lists.js linked.....")
var myTable = document.getElementById("myTable");
offers = [];
for (i = 0; i < myTable.rows.length; i++) {
    thisRow=myTable.rows[i]
    if (thisRow.className=="firstrow"){
        thisRow.addEventListener('click', function(){
            console.log('clicking',thisRow)
        })
        offers.push(thisRow)
    }
}




