
// Hiding and showing ergasies of one offer by clicking the expand button
var myTableRows = document.getElementById("myTable").rows;
expandButtons = document.getElementsByClassName("expand-js");
for (i = 0; i < expandButtons.length; i++) {
    expandButtons[i].addEventListener('click', function(){
        for(j = 0; j < myTableRows.length; j++){
            if (myTableRows[j].dataset["offer"] == this.title.split(' ')[1]){
                if (myTableRows[j+1].style.display=='table-row'){
                    myTableRows[j+1].style.display = 'none';
                }
                else{
                    myTableRows[j+1].style.display = 'table-row';
                }
            }
        }
    })
}
// By clicking edit button open the respective html for updating an offer
editButtons = document.getElementsByClassName("edit-js");
// console.log(editButtons)
for (i = 0; i < editButtons.length; i++) {
    editButtons[i].addEventListener('click', function(){
        for(j = 0; j < myTableRows.length; j++){
            if (myTableRows[j].dataset["offer"] == this.title.split(' ')[1]){
                console.log('/offers/' + this.title.split(' ')[1])
                window.location = '/offers/' + this.title.split(' ')[1];
            }
        }
    })
}

// creating a new offer by sales
 newOfferSign = document.getElementById("new_offer_plus");
 newOfferSign.addEventListener('click', function(){
    console.log('plus button pusheddddd');
    document.getElementById("post-offer-form").style.display = "";
 })


