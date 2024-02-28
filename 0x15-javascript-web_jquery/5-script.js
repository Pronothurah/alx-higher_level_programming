$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>').text('Item');
    $('.my_list').append(newItem);
  });
});
