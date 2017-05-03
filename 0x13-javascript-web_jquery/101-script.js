$(document).ready(function () {
  $('div#add_item').on('click', function (event) {
    $('UL.my_list').append('<LI>Item</LI>');
  });
  $('div#remove_item').on('click', function (event) {
    $('UL.my_list LI:last').remove();
  });
  $('div#clear_list').on('click', function (event) {
    $('UL.my_list LI').remove();
  });
});
