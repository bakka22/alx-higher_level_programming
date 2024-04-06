const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
fetch(url).then(async (response) => {
     const data = await response.json();
     const name = data.name;
     $('DIV#character').text(name);
})