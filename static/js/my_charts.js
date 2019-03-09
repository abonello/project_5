$.ajax({
    type: "GET",
    url: "get_chart_data",
    dataType: "json",
    astnc: true,
    // data: { csrfmiddlewaretoken: '{#{ csrf_token }#}' },
    success: function(data) {
        var features_title = [];
        var features_votes= [];
        var features_comments = [];
        var bugs_title = [];
        var bugs_votes= [];
        var bugs_comments = [];
        $.each(data.message.features, function(i, content) {
            features_title.push(content.title)
            features_votes.push(content.votes)
            features_comments.push(content.comments)
        });
        // console.log(features_title);
        // console.log(features_votes);
        // console.log(features_comments);

        $.each(data.message.bugs, function(i, content) {
            bugs_title.push(content.title)
            bugs_votes.push(content.votes)
            bugs_comments.push(content.comments)
        });
        // console.log(bugs_title);
        // console.log(bugs_votes);
        // console.log(bugs_comments);

        let feature_votes_Ctx = $('#feature-votes-chart')[0].getContext('2d');

        // Global Options
        // Chart.defaults.global.defaultFontFamily = 'Lato';
        // Chart.defaults.global.defaultFontSize = 18;
        // Chart.defaults.global.defaultFontColor = '#777';

        let featureVotesChart = new Chart(feature_votes_Ctx, {
            type: 'horizontalBar',
            data: {
                labels: features_title,
                datasets: [{
                    data: features_votes,
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
                    text: "Feature's Votes",
                    fontSize: 25,
                },
                legend: {
                    display: false,
                    position: 'bottom',
                    labels: {
                        fontColor: '#000'
                    }
                },
                // layout: {
                //     padding: {
                //         left: 20,
                //         right: 20,
                //         bottom: 0,
                //         top: 0
                //     }
                // },
                tooltips: {
                    enabled: true, // true, false
                },
                scales: {
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'features',
                        }
                    }],
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'votes',
                        }
                    }]
                }
            }
        });

        let feature_comments_Ctx = $('#feature-comments-chart')[0].getContext('2d');
        let featureCommentsChart = new Chart(feature_comments_Ctx, {
            type: 'horizontalBar',
            data: {
                labels: features_title,
                datasets: [{
                    data: features_comments,
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
                    text: "Feature's Comments",
                    fontSize: 25,
                },
                legend: {
                    display: false,
                    position: 'bottom',
                    labels: {
                        fontColor: '#000'
                    }
                },
                // layout: {
                //     padding: {
                //         left: 20,
                //         right: 20,
                //         bottom: 0,
                //         top: 0
                //     }
                // },
                tooltips: {
                    enabled: true, // true, false
                },
                scales: {
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'features',
                        }
                    }],
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'comments',
                        }
                    }]
                }
            }
        });

        let bug_votes_Ctx = $('#bug-votes-chart')[0].getContext('2d');
        let bugVotesChart = new Chart(bug_votes_Ctx, {
            type: 'horizontalBar',
            data: {
                labels: bugs_title,
                datasets: [{
                    data: bugs_votes,
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
                    text: "Bug's Votes",
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
                    padding: {
                        left: 20,
                        right: 20,
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
                            labelString: 'bugs',
                        }
                    }],
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'votes',
                        }
                    }]
                }
            }
        });

        let bug_comments_Ctx = $('#bug-comments-chart')[0].getContext('2d');
        let bugCommentsChart = new Chart(bug_comments_Ctx, {
            type: 'horizontalBar',
            data: {
                labels: bugs_title,
                datasets: [{
                    data: bugs_comments,
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
                    text: "Bug's Comments",
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
                    padding: {
                        left: 20,
                        right: 20,
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
                            labelString: 'bugs',
                        }
                    }],
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'comments',
                        }
                    }]
                }
            }
        });





    }
});

// function resize() {
                    // $(".canvas").outerHeight($(window).height() - $(".canvas").offset().top - Math.abs($(".canvas").outerHeight(true) - $(".canvas").outerHeight()));
//     $('.canvas').height = $('.canvas').width() * 2;

// }
// $(document).ready(function () {
//     resize();
//     $(window).on("resize", function () {
//         resize();
//     });
// });