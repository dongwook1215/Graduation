//chart1=>
var chart1_year_values = [];
var chart1_country_values = [];
var chart1_num_of_export_values = [];
var chart1_amount_of_export_values = [];

for(var i=0; i<data1.length; i++) {
	chart1_year_values.push(parseInt(data1[i]['기간']))
	chart1_country_values.push(data1[i]['국가명'])
	chart1_num_of_export_values.push(parseInt(data1[i]['수출건수']))
	chart1_amount_of_export_values.push(parseInt(data1[i]['수출금액']))
}

var chart1_config = {
	type: 'bar',
	data: {
		labels: chart1_country_values,
		datasets: [{
			label: '수출건수',
			borderColor: "rgb(54, 162, 235)",
 			backgroundColor: "rgba(54, 162, 235, 0.5)",
			data: chart1_num_of_export_values,
			fill: false,
			borderWidth: 2
		}, {
			label: '수출금액',
			borderColor: "rgb(255, 99, 132)",
			backgroundColor: "rgba(255, 99, 132, 0.5)",
			data: chart1_amount_of_export_values,
			fill: false,
			borderWidth: 2
		}]
	},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Chart No.1'
			},
			tooltips: {
				mode: 'index',
				intersect: false,
			},
			hover: {
				mode: 'nearest',
				intersect: true
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'x'
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'y'
					}
				}]
			}
	 	}
	}
//<=chart1

//chart2=>
var chart2_year_values = [];
var chart2_country_values = [];
var chart2_num_of_export_values = [];
var chart2_amount_of_export_values = [];

for(var i=0; i<data2.length; i++) {
	chart2_year_values.push(parseInt(data2[i]['기간']))
	chart2_country_values.push(data2[i]['국가명'])
	chart2_num_of_export_values.push(parseInt(data2[i]['수출건수']))
	chart2_amount_of_export_values.push(parseInt(data2[i]['수출금액']))
}

var chart2_config = {
	type: 'bar',
	data: {
		labels: chart2_country_values,
		datasets: [{
			label: '수출건수',
			borderColor: "rgb(54, 162, 235)",
 			backgroundColor: "rgba(54, 162, 235, 0.5)",
			data: chart2_num_of_export_values,
			fill: false,
			borderWidth: 2
		}, {
			label: '수출금액',
			borderColor: "rgb(255, 99, 132)",
			backgroundColor: "rgba(255, 99, 132, 0.5)",
			data: chart2_amount_of_export_values,
			fill: false,
			borderWidth: 2
		}]
	},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Chart No.2'
			},
			tooltips: {
				mode: 'index',
				intersect: false,
			},
			hover: {
				mode: 'nearest',
				intersect: true
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'x'
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'y'
					}
				}]
			}
	 	}
	}
//<=chart2

//chart3=>
var chart3_year_values = [];
var chart3_country_values = [];
var chart3_num_of_export_values = [];
var chart3_amount_of_export_values = [];

for(var i=0; i<data3.length; i++) {
	chart3_year_values.push(parseInt(data3[i]['기간']))
	chart3_country_values.push(data3[i]['국가명'])
	chart3_num_of_export_values.push(parseInt(data3[i]['수출건수']))
	chart3_amount_of_export_values.push(parseInt(data3[i]['수출금액']))
}

var chart3_config = {
	type: 'bar',
	data: {
		labels: chart3_country_values,
		datasets: [{
			label: '수출건수',
			borderColor: "rgb(54, 162, 235)",
 			backgroundColor: "rgba(54, 162, 235, 0.5)",
			data: chart3_num_of_export_values,
			fill: false,
			borderWidth: 2
		}, {
			label: '수출금액',
			borderColor: "rgb(255, 99, 132)",
			backgroundColor: "rgba(255, 99, 132, 0.5)",
			data: chart3_amount_of_export_values,
			fill: false,
			borderWidth: 2
		}]
	},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Chart No.3'
			},
			tooltips: {
				mode: 'index',
				intersect: false,
			},
			hover: {
				mode: 'nearest',
				intersect: true
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'x'
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'y'
					}
				}]
			}
	 	}
	}
//<=chart3

//chart4=>
var chart4_year_values = [];
var chart4_country_values = [];
var chart4_num_of_export_values = [];
var chart4_amount_of_export_values = [];

for(var i=0; i<data4.length; i++) {
	chart4_year_values.push(parseInt(data4[i]['기간']))
	chart4_country_values.push(data4[i]['국가명'])
	chart4_num_of_export_values.push(parseInt(data4[i]['수출건수']))
	chart4_amount_of_export_values.push(parseInt(data4[i]['수출금액']))
}

var chart4_config = {
	type: 'bar',
	data: {
		labels: chart4_country_values,
		datasets: [{
			label: '수출건수',
			borderColor: "rgb(54, 162, 235)",
 			backgroundColor: "rgba(54, 162, 235, 0.5)",
			data: chart4_num_of_export_values,
			fill: false,
			borderWidth: 2
		}, {
			label: '수출금액',
			borderColor: "rgb(255, 99, 132)",
			backgroundColor: "rgba(255, 99, 132, 0.5)",
			data: chart4_amount_of_export_values,
			fill: false,
			borderWidth: 2
		}]
	},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Chart No.4'
			},
			tooltips: {
				mode: 'index',
				intersect: false,
			},
			hover: {
				mode: 'nearest',
				intersect: true
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'x'
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'y'
					}
				}]
			}
	 	}
	}
//<=chart4



window.onload = function() {
	var chart_canvas1 = document.getElementById("chart1").getContext("2d");
    var chart = new Chart(chart_canvas1, chart1_config);

    var chart_canvas2 = document.getElementById("chart2").getContext("2d");
	var chart2 = new Chart(chart_canvas2, chart2_config);

    var chart_canvas3 = document.getElementById("chart3").getContext("2d");
    var chart3 = new Chart(chart_canvas3, chart3_config);

    var chart_canvas4 = document.getElementById("chart4").getContext("2d");
    var chart4 = new Chart(chart_canvas4, chart4_config);
};
