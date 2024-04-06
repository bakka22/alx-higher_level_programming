$(document).ready(() => {
  $('INPUT#btn_translate').on('click', getLang);
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      getLang();
    }
  });
  async function getLang () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val();
    response = await fetch(url);
    data = await response.json();
    hello = data.hello;
    $('DIV#hello').text(hello);
  }
});
