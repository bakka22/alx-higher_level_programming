$(document).ready(() => {
  $('INPUT#btn_translate').on('click', async function () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val();
    response = await fetch(url);
    data = await response.json();
    hello = data.hello;
    $('DIV#hello').text(hello);
  });
});
