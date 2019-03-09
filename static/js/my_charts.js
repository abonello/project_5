$.ajax({
    type: "GET",
    url: "get_chart_data",
    dataType: "json",
    astnc: true,
    // data: { csrfmiddlewaretoken: '{#{ csrf_token }#}' },
    success: function(data) {
        $('#output').html(data.message);
        console.log(data.message);
        // data(data.message);

        var countries = [];
        var temperature = [];
        $.each(data.message, function (key, val) {
            // console.log("Country: "+key+"  Temperature: "+val);
            countries.push(key);
            temperature.push(val);
        });
        console.log(countries);
        console.log(temperature);
        let myCtx2 = $('#myChart')[0].getContext('2d');

        let myBarChart = new Chart(myCtx2, {
            type: 'bar', // bar, horizontalBar, pie, line, doughnat, radar, polarArea
            data: {
                labels: countries,
                datasets: [{
                    label: 'Temperature',
                    data: temperature,
                    backgroundColor: [
                        'rgba(153, 204, 255, 0.6)',
                        'rgba(153, 255, 51, 0.6)',
                        'rgba(255, 204, 153, 0.6)',
                        'rgba(255, 102, 255, 0.6)',
                        'rgba(204, 204, 0, 0.6)',
                        'rgba(255, 152, 204, 0.6)',
                        'rgba(51, 255, 255, 0.6)',
                        'rgba(0, 0, 153, 0.6)',
                        'rgba(255, 0, 127, 0.6)',
                        'rgba(204, 102, 0, 0.6)'
                    ],
                    borderWidth: 1,
                    borderColor: [
                        'rgba(153, 204, 255, 0.8)',
                        'rgba(153, 255, 51, 0.8)',
                        'rgba(255, 204, 153, 0.8)',
                        'rgba(255, 102, 255, 0.8)',
                        'rgba(204, 204, 0, 0.8)',
                        'rgba(255, 152, 204, 0.8)',
                        'rgba(51, 255, 255, 0.8)',
                        'rgba(0, 0, 153, 0.8)',
                        'rgba(255, 0, 127, 0.8)',
                        'rgba(204, 102, 0, 0.8)'
                    ],
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000',
                },
                ]
            },
            options: {
                // responsive: false,
                title: {
                    display: true,
                    text: 'Temperatures of various countries',
                    fontSize: 25,
                },
                legend: {
                    display: false,
                    position: 'bottom',
                    labels: {
                        fontColor: '#000'
                    }
                },
                layout: {
                    // padding: 50,
                    padding: {
                        left: 50,
                        right: 0,
                        bottom: 50,
                        top: 0
                    }
                },
                tooltips: {
                    enabled: true, // true, false
                },
                scales: {
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'temp',
                        },
                        ticks: {
                            beginAtZero: true,
                            callback: function (value, index, values) {
                                return value + '°';
                            }
                        }
                    }]
                }
            }
        });

        let myCtx = $('#barChart')[0].getContext('2d');

        // Global Options
        Chart.defaults.global.defaultFontFamily = 'Lato';
        Chart.defaults.global.defaultFontSize = 18;
        Chart.defaults.global.defaultFontColor = '#777';

        let myBarChart1 = new Chart(myCtx, {
            type: 'horizontalBar', // bar, horizontalBar, pie, line, doughnat, radar, polarArea
            data: {
                // labels: ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford', 'Brockton', 'Quincy', 'Lynn', 'Fall River'],
                labels: countries,
                datasets: [{
                    label: 'Population',
                    label: 'Temperature',
                    data: temperature,
                    // backgroundColor: 'green'
                    backgroundColor: [
                        'rgba(153, 204, 255, 0.6)',
                        'rgba(153, 255, 51, 0.6)',
                        'rgba(255, 204, 153, 0.6)',
                        'rgba(255, 102, 255, 0.6)',
                        'rgba(204, 204, 0, 0.6)',
                        'rgba(255, 152, 204, 0.6)',
                        'rgba(51, 255, 255, 0.6)',
                        'rgba(0, 0, 153, 0.6)',
                        'rgba(255, 0, 127, 0.6)',
                        'rgba(204, 102, 0, 0.6)'
                    ],
                    borderWidth: 1,
                    // borderColor: '#777',
                    borderColor: [
                        'rgba(153, 204, 255, 0.8)',
                        'rgba(153, 255, 51, 0.8)',
                        'rgba(255, 204, 153, 0.8)',
                        'rgba(255, 102, 255, 0.8)',
                        'rgba(204, 204, 0, 0.8)',
                        'rgba(255, 152, 204, 0.8)',
                        'rgba(51, 255, 255, 0.8)',
                        'rgba(0, 0, 153, 0.8)',
                        'rgba(255, 0, 127, 0.8)',
                        'rgba(204, 102, 0, 0.8)'
                    ],
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000',

                },

                ]
            },
            options: {
                // responsive: false,
                title: {
                    display: true,
                    text: 'Temperatures in various countries',
                    fontSize: 25,
                },
                legend: {
                    display: true,
                    position: 'bottom',
                    labels: {
                        fontColor: '#000'
                    }
                },
                layout: {
                    // padding: 50,
                    padding: {
                        left: 50,
                        right: 0,
                        bottom: 0,
                        top: 0
                    }
                },
                tooltips: {
                    enabled: true, // true, false
                },
                scales: {
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'temp',
                        }
                        // ticks: {
                        //     beginAtZero: true,
                        //     callback: function (value, index, values) {
                        //         return value + '°';
                        //     }
                        // }
                    }],
                    xAxes: [{
                        // type: 'Temp',
                        ticks: {
                            min: 20,
                            // max: moment(1473853353000)
                        }
                    }]
                }
            }
        });





    }
    // context: data
});
// .done(function (response) {
//     // $(this).addClass("done");
//     // console.log(data);
//     alert(response);
//     console.log(response);
// });