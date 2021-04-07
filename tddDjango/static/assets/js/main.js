console.log("linkedddd.....");
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
   
$('form').on('click',function(event) {
    console.log($(this).data);
    console.log(this.action);
    console.log(this.action.includes('details'));

    if (this.action.includes('details')){
        var url = '/details/'
        query = this.search.value       //takes value of input in form e.g altavia
    
        console.log(url);     
        
        fetch(url, {
			method:'GET',
			headers:{
				'Content-Type':'text/html',
				'X-CSRFToken':csrftoken,
			}
		})
		.then((response) => {
            console.log("o yeahhhhh");
		    return response;
		});

    }

});