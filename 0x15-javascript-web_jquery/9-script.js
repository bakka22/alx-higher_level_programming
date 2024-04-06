const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
fetch(url).then(async (response) => {
     const data = await response.json();
     const hello = data.hello;
     $('DIV#hello').text(hello);
})