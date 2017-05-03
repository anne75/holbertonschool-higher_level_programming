$(document).ready(function () {
  const url = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&format=json';
  $('INPUT#btn_search').on('click', function () {
    let cityName = $('INPUT#city_search').val();
    // cityName = cityName.replace(' ', '%20');
    const newUrl = url.replace('city_name', cityName);
    $.getJSON(newUrl,
      function (res) {
        if (res.query.results != null) {
          $('DIV#wind_speed').text(res.query.results.channel.wind.speed);
        } else {
          $('DIV#wind_speed').text('');
        }
      }
     );
  });
});
