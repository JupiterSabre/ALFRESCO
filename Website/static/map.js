let map;

const styleOptions = {
    strokeColor: "green",
    strokeWeight: 2,
    strokeOpacity: 1,
    fillColor: "green",
    fillOpacity: 0.3,
  };

function initMap() {
    const { Map } = google.maps.importLibrary('maps')

    var mapOptions = {
        mapId: "f6e3c418d4f6c8b",
        center: {lat: 40.753597, lng: -73.983233},
        zoom: 10
    }

    map = new google.maps.Map(document.getElementById('map-container'), mapOptions);

    datasetId = "c9dac58f-4a61-4d83-a6d0-8e44d411d530"

    const datasetLayer = map.getDatasetFeatureLayer(datasetId)

    datasetLayer.style = styleOptions

}

initMap()

    // const waterfrontKML = new google.maps.KmlLayer({
    //     url: "/static/Libraries.kml",
    //   });
    
    //   waterfrontKML.setMap(map);
    // }

   
    


    
    // var WaterfrontArray = [ ['Hunts Point Landing', 40.8018801326,-73.8718161976, "Bronx"],
    // ['Manhattan Avenue', 40.7390609761,-73.9551975777, 'Brooklyn'],
    // ['Inwood Hill Park', 40.8693041643, -73.93178676, 'Manhattan'],
    // ['Seaside Wildlife Nature Park', 40.54136335, -74.14243279, 'Saten Island'],
    // ['Barretto Point Park', 40.80503153, -73.8878624],
    // ['Canarsie Pier', 40.63038364, -73.88382452, 'Brooklyn'],
    // ['Francis Lewis Park', 40.7971669903,-73.8246332253, 'Queens'],
    // ['Jacob Riis Park', 40.5681457184, -73.8850332298, 'Queens'],
    // ['Bayside Marina', 40.7795327754, -73.7683994024, 'Queens'],
    // ['Hunters Point South', 40.7384023773, -73.960210381, 'Queens']   
    //     ];

    
    // var infoWindow = new google.maps.InfoWindow;
    
    // var marker, i;
        
    //     for (i = 0; i < WaterfrontArray.length; i++) {
    //         marker = new google.maps.Marker({
    //             position: google.maps.LatLng(WaterfrontArray[i][1], WaterfrontArray[i][2]),
    //             map:map
    //         });

    //         google.maps.event.addListener(marker, 'click', (function(marker, i) {
    //             return function() {
    //             infoWindow.setContent(WaterfrontArray[i][0] + " - " + WaterfrontArray[i][3]);
    //             infoWindow.open(map, marker);
    //             }
    //         })(marker, i));
    //     } }








    // Multiple markers
    // function addMarker(property) {
    //     const  marker = new google.maps.Marker({
    //         position:property.location,
    //         map: map,
    //         icon: property.imageIcon
    //     })

    // }

    // addMarker({location:{lat: 40.7421, lng:-74.0100}, imageIcon:'https://img.icons8.com/nolan/2x/marker.png'});
    // addMarker({location:{lat: 40.7029, lng:-74.0154}})



    // Info Window
    // const detailWindow = new google.maps.InfoWindow({
    //     content: `<h2>I AM BRYANT PARK</h2>`
    // })
    // Add listener
    // marker.addListener("mouseover", () => {
    //     detailWindow.open(map, marker);
    // })
