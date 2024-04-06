const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
fetch(url).then(async (response) => {
     const data = await response.json();
     const movies = data.results;
     movies.forEach((item) => {
     	$('UL#list_movies').append('<li>' + item.title + '</li>');
     });
})