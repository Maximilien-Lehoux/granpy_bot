$( document ).ready(function()
{
    counter_wiki = 0
    var url_wikipedia = {}
    var address_complete = {}
    var article_wikipedia = {}
    var butt = $("#button_send");


    butt.on("click", function()
    {

        var value = $("#address").val();
        if (value == "")
        {
            value = "Salut GrandPy ! Est-ce que tu connais l'adresse de la gare de Périgueux ?";
        }
        console.log(value);

        $('#button_send').html("Chargement...");

            $.ajax(
            {
                url : '/wikipedia_article',
                type : "POST",
                data : {'data':value},
                // Work with the response
                success: function( response )
                {
                    article_wikipedia.data = (response);
                    counter_wiki += 1;
                    if (counter_wiki >= 3)
                    {
                        $('.dialog_box').append("Tu m'as demandé : " + value + "<br/>Bien sur mon garçon : " + address_complete.data + "<br/> et voici une anecdonte : " + '<br/>' +  article_wikipedia.data + '<br/>' + 'Et voici le lien de la page si tu veux davantage de précision : ' + '<br/>' + url_wikipedia.data + '<br/>'+ '<br/>');
                        counter_wiki = 0;
                        $('#button_send').html("Envoyer");
                    }
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
                    url_wikipedia.data = (response);
                    counter_wiki += 1;
                    if (counter_wiki >= 3)
                    {
                        $('.dialog_box').append("Tu m'as demandé : " + value + "<br/>Bien sur mon garçon : " + address_complete.data + "<br/> et voici une anecdonte : " + '<br/>' +  article_wikipedia.data + '<br/>' + 'Et voici le lien de la page si tu veux davantage de précision : ' + '<br/>' + url_wikipedia.data + '<br/>'+ '<br/>');
                        counter_wiki = 0;
                        $('#button_send').html("Envoyer");
                    }
                }

            });

            $.ajax(
            {
                url : '/address_complete',
                type : "POST",
                data : {'data':value},
                // Work with the response
                success: function( response )
                {
                   address_complete.data = (response);
                   counter_wiki += 1;
                   if (counter_wiki >= 3)
                   {
                        $('.dialog_box').append("Tu m'as demandé : " + value + "<br/>Bien sur mon garçon : " + address_complete.data + "<br/> et voici une anecdonte : " + '<br/>' +  article_wikipedia.data + '<br/>' + 'Et voici le lien de la page si tu veux davantage de précision : ' + '<br/>' + url_wikipedia.data + '<br/>'+ '<br/>');
                        counter_wiki = 0;
                        $('#button_send').html("Envoyer");
                   }
                }
            });
    });
});