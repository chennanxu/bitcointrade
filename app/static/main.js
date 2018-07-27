var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    }
  })



function get_ticker(){
    var url = "/api/ticker/"

    fetch(url, {
        mode: 'no-cors'
    }).then(
        function(response){
            return response.json();
        }
    ).then(function(data){
       // console.log(data.date);
        var date = new Date(parseInt(data.date)*1000)
    
        document.getElementById('ticker1').innerHTML = date.toLocaleString();
        document.getElementById('ticker2').innerHTML = data.ticker.buy;
        document.getElementById('ticker3').innerHTML = data.ticker.last;
    });

}

