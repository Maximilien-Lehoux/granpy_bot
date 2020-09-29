$( document ).ready(function()
{
    counter = 0
    var url_wikipedia = {}
    var butt = $("#button_send");


    butt.on("click", function()
    {

        var value = $("#address").val();

        $('#button_send').html("Chargement...");

            $.ajax(
            {
                url : '/wikipedia_article',
                type : "POST",
                data : {'data':value},
                // Work with the response
                success: function( response )
                {
                    if (counter >= 1)
                    {
                        $('.dialog_box').append("Bien sur mon garçon, et voici une anecdonte : " + '<br/>' +  response + '<br/>' + 'Et voici le lien de la page si tu veux davantage de précision : ' + '<br/>' + url_wikipedia.data + '<br/>'+ '<br/>');
                    }
                     $('#button_send').html("Envoyer");
                }
            });

            $.ajax(
            {
                url : '/wikipedia_url',
                type : "POST",
                data : {'data':value},
                // Work with the response
                success: function( response )
                {
                   url_wikipedia.data = response.link(response);
                   counter += 1;
                }
            });
    });
});