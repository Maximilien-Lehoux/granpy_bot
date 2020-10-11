$( document ).ready(function()
{
    var geocode = {latitude : "0", longitude : "0"};
    counter = 0
    var map = null;

    var butt = $("#button_send");
    function initMap()
    {
        map_paris = new google.maps.Map(document.getElementById("google_map_box"),
        {
            center: new google.maps.LatLng(geocode.latitude, geocode.longitude),
            zoom: 11,
        });
        var marker = new google.maps.Marker(
        {
        position : new google.maps.LatLng(geocode.latitude, geocode.longitude),
        map: map_paris,
        title: ""
        });
    }

    butt.on("click", function()
    {
        var value = $("#address").val();
        if (value == "")
        {
            value = "Salut GrandPy ! Est-ce que tu connais l'adresse de la gare de Périgueux ?";
        }
        console.log(value);

        $.ajax(
        {
            url : '/latitude_ajax',
            type : "POST",
            data : {'data':value},
            // Work with the response
            success: function( response )
            {
                geocode.latitude = ( response);
                counter += 1;
                if (counter >= 2)
                {
                    initMap();
                }

            }
        });

        $.ajax(
        {
            url : '/longitude_ajax',
            type : "POST",
            data : {'data':value},
            // Work with the response
            success: function( response )
            {
                geocode.longitude = ( response);
                counter += 1;
                if (counter >= 2)
                {
                    initMap();
                }

            }
        });
    });
});



