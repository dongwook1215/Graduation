window.onload = function() {
	var line_json = loadLineJson();
	var line_chart_canvas = document.getElementById("line_chart").getContext("2d");
	var line_chart = new Chart(line_chart_canvas, createLineChartConfig(line_json));

	var bar_json = loadBarJson();
	var bar_chart_canvas= document.getElementById("bar_chart").getContext("2d");
	var bar_chart = new Chart(bar_chart_canvas, createBarChartConfig(bar_json));
}
