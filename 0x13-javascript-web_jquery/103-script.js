$(document).ready(function () {
  const url = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&format=json';

  $('INPUT#city_search').keypress(function (event) {
    if (event.keyCode === 13) {
      $('INPUT#btn_search').click();
    }
  });

  $('INPUT#btn_search').on('click', function () {
    let city_name = $('INPUT#city_search').val();
    // city_name = city_name.replace(' ', '%20');
    const new_url = url.replace('city_name', city_name);
    console.log(new_url);
    $.getJSON(new_url,
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
