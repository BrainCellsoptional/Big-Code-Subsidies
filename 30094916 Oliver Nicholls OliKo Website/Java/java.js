/*list of descriptions for each region for output in table of page 1*/
/*i had chat gpt write these descriptions*/
let regioninfo = [
  "Waikato is ranked number 1 in terms of CO2 emissions in New Zealand, a position primarily driven by its significant agricultural activities and industrial contributions. The region is a powerhouse for dairy farming and other primary industries, which, while vital for the economy, have a considerable environmental impact. Efforts are underway to promote sustainable practices and reduce emissions, with initiatives focusing on innovative farming techniques and renewable energy solutions, reflecting a growing awareness of the need for environmental stewardship in this rich agricultural landscape.",
  "Canterbury is ranked number 2 in terms of CO2 emissions in New Zealand, primarily attributed to its large-scale agricultural practices and industrial activities. The region is a major contributor to the country's dairy and sheep farming industries, which, while economically vital, result in significant greenhouse gas emissions. In recent years, Canterbury has begun to embrace sustainability initiatives, focusing on reducing its carbon footprint through innovative farming techniques and investment in renewable energy, reflecting a growing commitment to environmental stewardship alongside economic prosperity",
  "Auckland is ranked number 3 in terms of CO2 emissions in New Zealand, a status driven by its urbanization and high population density. As the largest city in the country, Auckland's emissions stem from transportation, construction, and energy use in residential and commercial buildings. While it plays a vital role in New Zealand’s economy, the city is increasingly prioritizing sustainability through initiatives aimed at reducing emissions, promoting public transport, and enhancing green spaces, demonstrating a commitment to creating a more environmentally friendly urban environment.",
  "Southland is ranked number 4 in terms of CO2 emissions in New Zealand, primarily due to its extensive dairy and sheep farming operations, as well as some industrial activities. The region's vast pastures and rich agricultural heritage make it a significant contributor to the national economy, but these practices also result in substantial greenhouse gas emissions. In recent years, Southland has been making strides towards sustainability by adopting innovative farming techniques, promoting renewable energy, and engaging in initiatives to enhance biodiversity, reflecting a growing commitment to reducing its carbon footprint while supporting local livelihoods.",
  "Manawatu-Whanganui is ranked number 5 in terms of CO2 emissions in New Zealand, largely due to its agricultural practices, particularly in sheep and beef farming, along with some industrial activities. This region is known for its fertile land and significant contribution to the agricultural sector, which, while essential for the economy, also leads to notable greenhouse gas emissions. In recent years, Manawatu-Whanganui has been working towards sustainability by implementing innovative farming methods and promoting renewable energy initiatives, reflecting a growing recognition of the need to balance agricultural productivity with environmental responsibility.",
  "Otago is ranked number 6 in terms of CO2 emissions in New Zealand, influenced by its diverse agricultural sector, which includes sheep farming, viticulture, and forestry, as well as industrial activities. The region's stunning landscapes and rich agricultural heritage contribute significantly to the economy, but these activities also lead to notable emissions. In response to environmental concerns, Otago is increasingly focusing on sustainable practices, such as promoting organic farming and enhancing energy efficiency, highlighting a commitment to reducing its carbon footprint while maintaining its agricultural productivity and natural beauty.",
  "Taranaki is ranked number 7 in terms of CO2 emissions in New Zealand, largely due to its robust agricultural sector, particularly dairy farming, alongside significant industrial operations, including oil and gas extraction. The region’s unique volcanic landscape supports productive farming, but these activities contribute to greenhouse gas emissions. In recent years, Taranaki has been taking steps to enhance sustainability through initiatives aimed at reducing emissions, increasing renewable energy use, and promoting environmentally friendly farming practices, reflecting a growing commitment to balancing economic development with ecological responsibility.",
  "Northland is ranked number 8 in terms of CO2 emissions in New Zealand, primarily driven by its agricultural activities, including beef and dairy farming, as well as forestry and tourism-related industries. While the region boasts a rich cultural heritage and stunning landscapes, its emissions are impacted by land use and transport. In response, Northland is increasingly adopting sustainable practices, such as regenerative agriculture and reforestation efforts, aiming to reduce its carbon footprint and enhance environmental resilience, all while supporting local economic growth and preserving its natural beauty.",
  "Hawke's Bay is ranked number 9 in terms of CO2 emissions in New Zealand, primarily due to its strong agricultural sector, which includes viticulture, horticulture, and livestock farming. The region's fertile land and favorable climate make it a hub for primary production, contributing to its emissions profile. However, Hawke's Bay is actively pursuing sustainability initiatives, focusing on innovative farming practices, water management, and renewable energy projects. These efforts reflect a commitment to reducing environmental impact while maintaining the economic vitality that agriculture brings to the region.",
  "Bay of Plenty is ranked number 10 in terms of CO2 emissions in New Zealand, largely influenced by its diverse agricultural sector, particularly kiwifruit and avocado production, alongside forestry and tourism. The region's favorable climate and rich soils support significant farming activities, which contribute to its emissions. However, Bay of Plenty is increasingly focusing on sustainability, with initiatives aimed at promoting environmentally friendly farming practices, enhancing energy efficiency, and protecting local ecosystems. This commitment underscores the region's effort to balance agricultural productivity with environmental stewardship."
];
/*list of all images for table page 1*/
let images = [
  "Images/1.jpg",
  "Images/2.jpg",
  "Images/3.jpg",
  "Images/4.jpg",
  "Images/5.jpg",
  "Images/6.jpg",
  "Images/7.jpg",
  "Images/8.jpg",
  "Images/9.jpg",
  "Images/10.jpg",
  
]
/*dictonary containing all information about NZ regions*/
/*used to store output information for page 2*/
let regiontext = {
  "NZ-AUK": {
    "city": "Auckland",
    "text": "1,715,600 ",
    "landArea": "1,086 km²",
    "co2Emissions": "9,726 ",
    "gdp": "NZD 94 Billion",
    "image": "Graphs/AUK.jpg"
  },
  "NZ-BOP": {
    "city": "Bay of Plenty",
    "text": "343,400 ",
    "landArea": "12,177 km²",
    "co2Emissions": "3,336",
    "gdp": "NZD 16 Billion",
    "image": "Graphs/BOP.jpg"
  },
  "NZ-CAN": {
    "city": "Canterbury",
    "text": "649,800 ",
    "landArea": "44,507 km²",
    "co2Emissions": "12,049",
    "gdp": "NZD 39 Billion",
    "image": "Graphs/CAB.jpg"
  },
  "NZ-CIT": {
    "city": "Chatham Islands",
    "text": "600 ",
    "landArea": "966 km²",
    "co2Emissions": "NO DATA",
    "gdp": "NO DATA",
    "image": "Graphs/CHT.jpg"
  },
  "NZ-GIS": {
    "city": "Gisborne",
    "text": "51,500 ",
    "landArea": "8,363 km²",
    "co2Emissions": "1,356",
    "gdp": "NZD 1.6 Billion",
    "image": "Graphs/GIB.jpg"
  },
  "NZ-HKB": {
    "city": "Hawke's Bay",
    "text": "181,000 ",
    "landArea": "14,111 km²",
    "co2Emissions": "3,367",
    "gdp": "NZD 5.4 Billion",
    "image": "Graphs/HKB.jpg"
  },
  "NZ-MBH": {
    "city": "Marlborough",
    "text": "51,000 ",
    "landArea": "12,484 km²",
    "co2Emissions": "806",
    "gdp": "NZD 1.5 Billion",
    "image": "Graphs/MAB.jpg"
  },
  "NZ-MWT": {
    "city": "Manawatu-Whanganui",
    "text": "256,500 ",
    "landArea": "22,224 km²",
    "co2Emissions": "5,816",
    "gdp": "NZD 9 Billion",
    "image": "Graphs/MHW.jpg"
  },
  "NZ-NSN": {
    "city": "Nelson",
    "text": "54,700 ",
    "landArea": "4,290 km²",
    "co2Emissions": "364",
    "gdp": "NZD 1.3 Billion",
    "image": "Graphs/NEL.jpg"
  },
  "NZ-NTL": {
    "city": "Northland",
    "text": "191,000 ",
    "landArea": "13,289 km²",
    "co2Emissions": "4,049",
    "gdp": "NZD 3 Billion",
    "image": "Graphs/NOR.jpg"
  },
  "NZ-OTA": {
    "city": "Otago",
    "text": "246,700 ",
    "landArea": "32,000 km²",
    "co2Emissions": "5,142",
    "gdp": "NZD 14 Billion",
    "image": "Graphs/OTG.jpg"
  },
  "NZ-STL": {
    "city": "Southland",
    "text": "102,700 ",
    "landArea": "32,400 km²",
    "co2Emissions": "6,186",
    "gdp": "NZD 3 Billion",
    "image": "Graphs/SOL.jpg"
  },
  "NZ-TAS": {
    "city": "Tasman",
    "text": "57,900 ",
    "landArea": "9,786 km²",
    "co2Emissions": "763",
    "gdp": "NZD 1.2 Billion",
    "image": "Graphs/TAS.jpg"
  },
  "NZ-TKI": {
    "city": "Taranaki",
    "text": "126,000 ",
    "landArea": "10,202 km²",
    "co2Emissions": "5,002",
    "gdp": "NZD 5 Billion",
    "image": "Graphs/TAR.jpg"
  },
  "NZ-WKO": {
    "city": "Waikato",
    "text": "485,000 ",
    "landArea": "25,000 km²",
    "co2Emissions": "16,217",
    "gdp": "NZD 20 Billion",
    "image": "Graphs/WAI.jpg"
  },
  "NZ-WGN": {
    "city": "Wellington",
    "text": "547,000 ",
    "landArea": "1,143 km²",
    "co2Emissions": "3,151",
    "gdp": "NZD 52 Billion",
    "image": "Graphs/WEL.jpg"
  },
  "NZ-WTC": {
    "city": "West Coast",
    "text": "32,000",
    "landArea": "23,000 km²",
    "co2Emissions": "1,108",
    "gdp": "NZD 1 Billion",
    "image": "Graphs/WEC.jpg"
  }
};
/*list of videos for page 3*/
let videos = [
  "Videos/vid1.mp4#t=1",
  "Videos/vid2.mp4",
  "Videos/vid3.mp4#t=1",
  "Videos/vid4.mp4#t=1",
]
/*video titles*/
let videodescriptions = [
  "This Video will Explains what Co2 is in simple terms and where it comes from",
  "New Zealands Future Carbon Neutral Plans",
  "New Zealands Emissions Trading Scheme",
  "News About NZ Carbon Traders"

]
/*function outputs region information*/
/*takes in region name and ranking number which is used to index from the list, onclick */
function updateInfo(region, ranking) {
  ranking = parseInt(ranking);
  /*changes text based on index number*/
  document.getElementById('selectedInfo').innerText = `City: ${region},\nRank: ${ranking}\n\n Desctiption: ${regioninfo[ranking-1]}`
  /*changes image based on index number*/
  const selectedImage = document.getElementById("selectedImage")
  selectedImage.src = images[ranking-1]
};

/*waits for click event then retrives key from SVG region */
/*uses key to index dictonary for correct information*/
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('.region').forEach(region => {
      region.addEventListener('click', () => {
          const regionId = region.id
          const info = regiontext[regionId]
          /*updates text*/
          document.getElementById("regioninfo").innerText = `${info.city}'s \n Co2 Emissions Throught the years\n\n Population 2021: ${info.text} \n Total Land Area: ${info.landArea} \n Co2 Emissions in 2021: ${info.co2Emissions} Kiliotonnes \n GDP: ${info.gdp} Dollars\n\n\n`
          /*updates graph*/
          const regionimage = document.getElementById("regionimage");
          regionimage.src = info.image
      });
  });
});

/*sets video index to 0 and incrementes by + 1 or - 1 when button is clicked*/
let vidcount = 0
next.addEventListener('click', ()=> {
  if (vidcount == 3) {
    vidcount = -1
  }
  vidcount = (vidcount + 1);
  vid.src = videos[vidcount];
  vidtext.innerText = videodescriptions[vidcount]
})
back.addEventListener('click', ()=> {
  if (vidcount == 0) {
    vidcount = 4
  }
  vidcount = (vidcount - 1);
  vid.src = videos[vidcount];
  vidtext.innerText = videodescriptions[vidcount]
})