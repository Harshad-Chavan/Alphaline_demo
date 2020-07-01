var settings = {
  "url": "http://192.168.0.111:8000/data/?format=json",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  for (let index = 0; index < response.length; index++) {
  const element = response[index];
  console.log(element);  
}
  
});
