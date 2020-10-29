var config = {
	type: 'line',
	data: {
		labels: labels,
		datasets: [{
			label: 'dataset',
			borderColor: "rgb(54, 162, 235)",
 			backgroundColor: "rgba(54, 162, 235, 0.5)",
			data: data[0],
			fill: false,
		}, {
			label: 'dataset',
			borderColor: "rgb(255, 99, 132)",
			backgroundColor: "rgba(255, 99, 132, 0.5)",
			data: data[1],
			fill: false
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
					labelString: 'Month'
				}
			}],
			yAxes: [{
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'Value'
				}
			}]
		}
	}
};

window.onload = function() {
	var chart_canvas = document.getElementById("chart_1").getContext("2d");
    var chart = new Chart(chart_canvas, config);

    var chart_canvas_2 = document.getElementById("chart_2").getContext("2d");
    var chart_2 = new Chart(chart_canvas_2, config);

    var chart_canvas_3 = document.getElementById("chart_3").getContext("2d");
    var chart_3 = new Chart(chart_canvas_3, config);

    var chart_canvas_4 = document.getElementById("chart_4").getContext("2d");
    var chart_4 = new Chart(chart_canvas_4, config);
};
