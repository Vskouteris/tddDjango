// console.log("all_lists.js linked.....")
var myTableRows = document.getElementById("myTable").rows;
offers = [];
for (i = 0; i < myTableRows.length; i++) {
    if (myTableRows[i].className=="firstrow"){
        offers.push(myTableRows[i]);
        myTableRows[i].addEventListener('click', function(){
            // CHECKING THAT ALL THE OTHER <tr> ARE BEING NOT DISPLAY WHEN I CHOOSE ONE OF THEM
            for(j = 0; j < myTableRows.length; j++){
                if (this.dataset.offer != myTableRows[j].dataset["offer"]){
                    myTableRows[j].style.display = 'none';
                }else{
                    myTableRows[j+1].style.display = 'table-row';
                    console.log(myTableRows[j+1]);
                    j=j+1;
                }
                
            }
        })
        
    }
}




