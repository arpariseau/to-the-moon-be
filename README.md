# To the Moon and Backend 

This is the final project at Turing School of Software and Design in Denver, CO. It is the backend portion of a service-oriented architecture. Working directly with a front end team, we were provided a detailed wireframe and a list of expected responses. We built an API that consumes multiple external APIs to gather and format that data required. 
Stack: Python3, Flask, Postgres, Heroku 

# Endpoints 

### Celestial Bodies Index Endpoint
``` GET 'https://moon-back-end.herokuapp.com/api/v1/celestial_bodies'```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies’```

```json
{
  "data": [
    {
    "celestial_body_type": "Planet",
    "gravity": 0.37,
    "id": 1,
    "image": "https://cdn.mos.cms.futurecdn.net/GA4grWEsUYUqH58cDbRBw8.jpg",
    "name": "Mercury",
    "planet_day": 58.65,
    "planet_year": 87.96,
    "travel": {
        "distance": 112788522.23136441,
        "travel_time": 4544.992030599791
      }
    },
    {
    "celestial_body_type": "Planet",
    "gravity": 0.9,
    "id": 2,
    "image": "https://astronomy.com/-/media/Images/News%20and%20Observing/News/2020/04/Venus1__1_.jpg?mw=600",
    "name": "Venus",
    "planet_day": 243.02,
    "planet_year": 224.7,
    "travel": {
        "distance": 89615403.36369385,
        "travel_time": 3611.194526261035
      }
    },
    {
    "celestial_body_type": "Planet",
    "gravity": 0.38,
    "id": 3,
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSY5oCXASYgKXI1MFGmRbgs9WmSnULsnOe_fg&usqp=CAU",
    "name": "Mars",
    "planet_day": 1.02,
    "planet_year": 686.98,
    "travel": {
        "distance": 41416978.76680374,
        "travel_time": 1668.9627162638517
      }
    },
    {
    "celestial_body_type": "Planet",
    "gravity": 2.53,
    "id": 4,
    "image": "https://3.bp.blogspot.com/-JzB2ruOjBOs/WJy8tR_tJSI/AAAAAAAABdA/26gANOQ4Y4IZyMnEGS2L8X-dvhVhGL0ZQCLcB/s1600/jupiter_HD.jpg",
    "name": "Jupiter",
    "planet_day": 0.41,
    "planet_year": 4332.59,
    "travel": {
        "distance": 431324606.1620057,
        "travel_time": 17380.90772735355
      }
    },
    {
    "celestial_body_type": "Planet",
    "gravity": 1.06,
    "id": 5,
    "image": "https://solarsystem.nasa.gov/system/resources/list_images/2490_hubblesaturn_320.png",
    "name": "Saturn",
    "planet_day": 0.44,
    "planet_year": 10759.22,
    "travel": {
        "distance": 878319056.9760253,
        "travel_time": 35393.256647970076
      }
    },
    {
    "celestial_body_type": "Planet",
    "gravity": 0.9,
    "id": 6,
    "image": "https://i2-prod.mirror.co.uk/science/article11370299.ece/ALTERNATES/s615/1_Uranus.jpg",
    "name": "Uranus",
    "planet_day": 0.72,
    "planet_year": 30685.4,
    "travel": {
        "distance": 1773240469.5898645,
        "travel_time": 71455.53149540073
      }
    },
    {
    "celestial_body_type": "Planet",
    "gravity": 1.14,
    "id": 7,
    "image": "https://media.wired.com/photos/5d04045bde1abfe4e801d054/191:100/w_2292,h_1200,c_limit/Science-Neptune-FA-PIA01492_orig.jpg",
    "name": "Neptune",
    "planet_day": 0.67,
    "planet_year": 60189,
    "travel": {
        "distance": 2686981881.527914,
        "travel_time": 108276.18800483213
      }
    },
    {
    "celestial_body_type": "Moon",
    "gravity": 0.16,
    "id": 8,
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSA0QNeR2YGmCWvRtZqsYN9Ft44WxYJEArbtw&usqp=CAU",
    "name": "Moon",
    "planet_day": 27.32,
    "planet_year": null,
    "travel": {
        "distance": 238900,
        "travel_time": 9.62685364281109
      }
    },
    {
    "celestial_body_type": "Star",
    "gravity": 27.95,
    "id": 9,
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRkKZ8nFulIMZAK8MKI8kzvsfGnaa3YlqMMRA&usqp=CAU",
    "name": "Sun",
    "planet_day": 25.38,
    "planet_year": null,
    "travel": {
        "distance": 93464107.60204296,
        "travel_time": 3766.2841554659476
      }
    }
  ]
}
```

### Celestial Bodies Show Endpoint
```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies/(id)’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies/9’```

```json
{
    "celestial_body_type": "Star",
    "gravity": 27.95,
    "id": 9,
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRkKZ8nFulIMZAK8MKI8kzvsfGnaa3YlqMMRA&usqp=CAU",
    "name": "Sun",
    "planet_day": 25.38,
    "planet_year": null,
    "travel": {
        "distance": 93464281.86764629,
        "travel_time": 3766.29117777427
    }
}
```
### Landmarks Index Endpoint 

```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies/(id)/landmarks’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies/9/landmarks’```

```json
{
  "data": [
      {
          "celestial_body_id": 9,
          "description": "Deep in the sun's core is the beating heart of the entire solar system. It's hard to believe that so much is powered by a reaction on the atomic scale. Under pressure from the gravity of the sun being so massive, hydrogen atoms fuse into helium, providing the energy that lights up the entire solar system. It produces 1.8 billion times the energy of the largest nuclear bomb detonated on Earth... every single second!",
          "id": 1,
          "image": "https://cdn.mos.cms.futurecdn.net/WtnoFrpeLL37TLcjpzK5A7-970-80.jpg",
          "landmark_type": "Structure",
          "name": "Core"
      },
      {
          "celestial_body_id": 9,
          "description": "When you look up into the sky (but hopefully not directly!) the bright ball of the photosphere is the part of the sun you're looking at. Though often depicted as being yellow, the light from the sun is white. When it hits the Earth's atmosphere, a phenomenon called Rayleigh scattering causes it to look yellow, as well as the sky blue. The same phenomenon is responsible for the brilliant colors of both sunrises and sunsets.",
          "id": 2,
          "image": "https://astronomy.swin.edu.au/cms/cpg15x/albums/scaled_cache/897b42ce97bcd409a597f1392b2dd379-280x229.png",
          "landmark_type": "Structure",
          "name": "Photosphere"
      },
      {
          "celestial_body_id": 9,
          "description": "Just like the Earth, the sun also has an atmosphere. The largest part of it is known as its corona. Though it is not usually visible thanks to the brightness of the photosphere, during eclipses - when the moon's orbit puts it in the right place to block out the majority of the sun's light - it becomes readily apparent. Particles stream out of the corona to create solar wind, which is responsible for phenomena such as the auroras, and comets having tails, among others.",
          "id": 3,
          "image": "https://media.wired.com/photos/5e62e4af2ee19f000853234b/master/w_1600%2Cc_limit/photo_space_corona_1_AFRC2017-0233-006.jpg",
          "landmark_type": "Atmosphere",
          "name": "Corona"
      },
      {
          "celestial_body_id": 9,
          "description": "Sun spots happen when fluctuations in the sun cause areas of the surface to be not as hot as their surroundings, causing that area to look darker than the rest of the sun. Despite only appearing as spots, they can grow to a size several times our own planet's! They can last anywhere from a few days to a few months, and tend to increase and decrease in frequency based off of eleven-year cycles.",
          "id": 4,
          "image": "https://upload.wikimedia.org/wikipedia/commons/6/67/Sunspots_1302_Sep_2011_by_NASA.jpg",
          "landmark_type": "Surface",
          "name": "Sunspots"
      },
      {
          "celestial_body_id": 9,
          "description": "Solar flares are bright flashes caused by increased activity from the sun, in conjunction with a coronal mass ejection - an intense wave of energized particles that erupt from the sun and fly out into the solar system. While they are relatively common, they can cause electrical problems should the Earth be in the path of a flare, thanks to the disturbances they can cause in the atmosphere.",
          "id": 5,
          "image": "https://media1.s-nbcnews.com/j/newscms/2017_23/2030061/170608-solar-flare-mn-0850_be3b4f10ba85b1f4ef86e87522e6b26a.fit-2000w.jpg",
          "landmark_type": "Atmosphere",
          "name": "Solar Flares"
      }
  ]
}
```
### Landmark Show Endpoint 

```GET ‘https://moon-back-end.herokuapp.com/api/v1/landmarks/(id)’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/landmarks/9’```

```json
{
  "celestial_body_id": 1,
  "description": "Named after the French composer, this crater, along with a similar one named Hakusai, are prominent enough to be detected from Earth using radio telescopes. It has a very noticeable ray pattern stretching out from the impact center, which indicates that it's relatively new. It was one of the first things photographed by the MESSENGER probe, sent to orbit the planet from 2011 to 2015.",
  "id": 9,
  "image": "https://live.staticflickr.com/6170/6176086738_3a98b804a4_b.jpg",
  "landmark_type": "Crater",
  "name": "Debussy"
}
```

### Most Recent Space News Endpoint
```GET ‘https://moon-back-end.herokuapp.com/api/v1/news’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/news’```

```json
{
"docs": [
  {
      "_id": "5f60e35096c53b1fb52b980e",
      "categories": [],
      "date_added": 1599983562,
      "date_published": 1600184411,
      "events": [],
      "featured": false,
      "featured_image": "https://cdn.arstechnica.net/wp-content/uploads/2020/09/tropics-800x505.jpg",
      "id": "",
      "imported_date": "2020-09-13T07:52:42.498Z",
      "launches": [],
      "ll": [],
      "news_site": "arstechnica",
      "news_site_long": "Arstechnica",
      "published_date": "2020-09-15T15:40:11.000Z",
      "tags": [],
      "title": "Hurricane Sally will bring devastating floods to the Southern United States",
      "url": "https://arstechnica.com/science/2020/09/hurricane-sally-will-bring-devastating-floods-to-the-southern-united-states/"
  },

```



