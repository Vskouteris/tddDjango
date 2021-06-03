function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getToken('csrftoken')

function deleteOffer(offer_id){
    var url = '/offers/'+offer_id
    alert("This Offer is going to be removed from Database");
    fetch(url, {
    	method:'DELETE',
    	headers:{
    		'Content-Type':'application/json',
    		'X-CSRFToken':csrftoken,
    	}, 
    })
    .then((response) => {
        location.reload()
    });
}



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
for (i = 0; i < editButtons.length; i++) {
    editButtons[i].addEventListener('click', function(){
        for(j = 0; j < myTableRows.length; j++){
            if (myTableRows[j].dataset["offer"] == this.title.split(' ')[1]){
                window.location = '/offers/' + this.title.split(' ')[1];
            }
        }
    })
}

// By clicking delete button delete this offer from database
deleteButtons = document.getElementsByClassName("delete-js");
for (i = 0; i < deleteButtons.length; i++) {
    deleteButtons[i].addEventListener('click', function(){
        for(j = 0; j < myTableRows.length; j++){
            if (myTableRows[j].dataset["offer"] == this.title.split(' ')[1]){
                deleteOffer(this.title.split(' ')[1]);
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


