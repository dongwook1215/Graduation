function createLineChartConfig(json_file) {
	var labels = Object.keys(json_file);
	var import_values = [];
	var export_values = [];
	for(var i=0; i<labels.length; i++) {
		import_values.push(parseInt(json_file[labels[i]]["수입금액"].replace(/,/g, '')));
		export_values.push(parseInt(json_file[labels[i]]["수출금액"].replace(/,/g, '')));
	}
	var config = {
		type: "line",
		data: {
			labels: labels,
			datasets: [{
				label: "수입금액",
				data: import_values,
				borderColor: "rgb(54, 162, 235)",
				pointBackgroundColor: "rgb(54, 162, 235)",
				fill: false,
				borderWidth: 2,
			}, {
				label: "수출금액",
				data: export_values,
				borderColor: "rgb(255, 99, 132)",
				pointBackgroundColor: "rgb(255, 99, 132)",
				fill: false,
				borderWidth: 2,
			}]
		},
		options: {
			responsive: false,
			tooltips: {
				mode: "index",
				intersect: false,
				callbacks: {
					label: function(tooltipItem, data) {
						return '$' + tooltipItem.yLabel.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
					}
				},
			},
			hover: {
				mode: "nearest",
				intersect: true,
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: "연도",
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: "금액",
					},
					ticks: {
						beginAtZero: true,
						callback: function(value, index, values) {
							if(parseInt(value) >= 1000){
								return '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
							} else {
								return '$' + value;
							}
						}
					}
				}]
			}
		}
	}

	return config;
}

function loadLineJson() {
	json = {
   		"2000": {
      		"수출건수": "3,605,801",
      		"수출금액": "172,267,510",
      		"수입건수": "3,302,214",
      		"수입금액": "160,481,018",
      		"무역수지": "11,786,492"
   		},
   		"2001": {
      		"수출건수": "3,603,806",
      		"수출금액": "150,439,144",
      		"수입건수": "3,285,286",
      		"수입금액": "141,097,821",
      		"무역수지": "9,341,323"
   		},
   		"2002": {
      		"수출건수": "4,021,165",
      		"수출금액": "162,470,528",
      		"수입건수": "3,801,904",
      		"수입금액": "152,126,153",
      		"무역수지": "10,344,375"
   		},
   		"2003": {
      		"수출건수": "4,318,330",
      		"수출금액": "193,817,443",
      		"수입건수": "4,037,458",
      		"수입금액": "178,826,657",
      		"무역수지": "14,990,786"
   		},
   		"2004": {
      		"수출건수": "4,634,711",
      		"수출금액": "253,844,672",
      		"수입건수": "4,337,168",
      		"수입금액": "224,462,687",
      		"무역수지": "29,381,985"
   		},
   		"2005": {
      		"수출건수": "4,720,283",
      		"수출금액": "284,418,743",
      		"수입건수": "4,781,811",
      		"수입금액": "261,238,264",
      		"무역수지": "23,180,479"
   		},
   		"2006": {
      		"수출건수": "4,843,800",
      		"수출금액": "325,464,848",
      		"수입건수": "5,216,317",
      		"수입금액": "309,382,632",
      		"무역수지": "16,082,216"
   		},
   		"2007": {
      		"수출건수": "5,030,768",
      		"수출금액": "371,489,086",
      		"수입건수": "5,667,966",
      		"수입금액": "356,845,733",
      		"무역수지": "14,643,352"
   		},
   		"2008": {
      		"수출건수": "5,234,178",
      		"수출금액": "422,007,328",
      		"수입건수": "5,850,875",
      		"수입금액": "435,274,737",
      		"무역수지": "-13,267,409"
   		},
   		"2009": {
      		"수출건수": "5,399,939",
      		"수출금액": "363,533,561",
      		"수입건수": "6,699,545",
      		"수입금액": "323,084,521",
      		"무역수지": "40,449,040"
   		},
   		"2010": {
      		"수출건수": "6,237,860",
      		"수출금액": "466,383,762",
      		"수입건수": "9,143,039",
      		"수입금액": "425,212,160",
      		"무역수지": "41,171,601"
   		},
   		"2011": {
      		"수출건수": "6,305,365",
      		"수출금액": "555,213,656",
      		"수입건수": "10,611,272",
      		"수입금액": "524,413,090",
      		"무역수지": "30,800,566"
   		},
   		"2012": {
      		"수출건수": "6,533,596",
      		"수출금액": "547,869,792",
      		"수입건수": "11,842,076",
      		"수입금액": "519,584,473",
      		"무역수지": "28,285,319"
   		},
   		"2013": {
      		"수출건수": "6,887,279",
      		"수출금액": "559,632,434",
      		"수입건수": "14,344,341",
      		"수입금액": "515,585,515",
      		"무역수지": "44,046,919"
   		},
   		"2014": {
      		"수출건수": "7,083,325",
      		"수출금액": "572,664,607",
      		"수입건수": "16,302,570",
      		"수입금액": "525,514,506",
      		"무역수지": "47,150,101"
   		},
   		"2015": {
      		"수출건수": "7,438,562",
      		"수출금액": "526,756,503",
      		"수입건수": "14,459,780",
      		"수입금액": "436,498,973",
      		"무역수지": "90,257,531"
   		},
   		"2016": {
      		"수출건수": "8,273,729",
      		"수출금액": "495,425,940",
      		"수입건수": "15,517,151",
      		"수입금액": "406,192,887",
      		"무역수지": "89,233,053"
   		},
   		"2017": {
      		"수출건수": "8,423,120",
      		"수출금액": "573,694,421",
      		"수입건수": "18,691,086",
      		"수입금액": "478,478,296",
      		"무역수지": "95,216,125"
   		},
   		"2018": {
      		"수출건수": "8,950,209",
      		"수출금액": "604,859,657",
      		"수입건수": "21,559,704",
      		"수입금액": "535,202,428",
      		"무역수지": "69,657,228"
   		},
   		"2019": {
      		"수출건수": "9,907,139",
      		"수출금액": "542,232,610",
      		"수입건수": "25,889,882",
      		"수입금액": "503,342,947",
      		"무역수지": "38,889,663"
   		},
   		"2020": {
      		"수출건수": "3,216,643",
      		"수출금액": "166,917,993",
      		"수입건수": "9,670,534",
      		"수입금액": "159,994,478",
      		"무역수지": "6,923,516"
   		}
	};

	return json;
}

function createBarChartConfig(json_file) {
	var labels = Object.keys(json_file);
	var import_values = [];
	var export_values = [];
	for(var i=0; i<labels.length; i++) {
		import_values.push(parseInt(json_file[labels[i]]["수입금액"].replace(/,/g, '')));
		export_values.push(parseInt(json_file[labels[i]]["수출금액"].replace(/,/g, '')));
	}
	var config = {
		type: "bar",
		data: {
			labels: labels,
			datasets: [{
				label: "수입금액",
				data: import_values,
				borderColor: "rgb(54, 162, 235)",
				backgroundColor: "rgba(54, 162, 235, 0.5)",
				fill: false,
				borderWidth: 2,
			}, {
				label: "수출금액",
				data: export_values,
				fill: false,
				borderColor: "rgb(255, 99, 132)",
				backgroundColor: "rgba(255, 99, 132, 0.5)",
				borderWidth: 2,
			}]
		},
		options: {
			responsive: false,
			tooltips: {
				mode: "index",
				intersect: false,
				callbacks: {
					label: function(tooltipItem, data) {
						return tooltipItem.yLabel.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
					}
				},
			},
			hover: {
				mode: "nearest",
				intersect: true,
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: "연도",
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: "금액",
					},
					ticks: {
						beginAtZero: true,
						callback: function(value, index, values) {
							if(parseInt(value) >= 1000){
								return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
							} else {
								return value;
							}
						}
					}
				}]
			}
		}
	}

	return config;
}

function loadBarJson() {
	var json = {
   		"2016": {
      		"품목명": "액정 디바이스",
      		"품목코드": 9013,
      		"수출중량": "200,738.1",
      		"수입중량": "51,451.9",
      		"수출금액": "16,128,656",
      		"수입금액": "2,773,259",
      		"무역수지": "13,355,397"
   		},
   		"2017": {
      		"품목명": "액정 디바이스",
      		"품목코드": 9013,
      		"수출중량": "175,008.1",
      		"수입중량": "60,932.8",
      		"수출금액": "15,454,659",
      		"수입금액": "4,009,622",
      		"무역수지": "11,445,037"
   		},
   		"2018": {
      		"품목명": "액정 디바이스",
      		"품목코드": 9013,
      		"수출중량": "165,523.3",
      		"수입중량": "63,833.6",
      		"수출금액": "13,452,494",
      		"수입금액": "4,103,684",
      		"무역수지": "9,348,810"
   		},
   		"2019": {
      		"품목명": "액정 디바이스",
      		"품목코드": 9013,
      		"수출중량": "87,752.0",
      		"수입중량": "13,087.5",
      		"수출금액": "6,915,920",
      		"수입금액": "1,293,491",
      		"무역수지": "5,622,429"
   		},
   		"2020": {
      		"품목명": "액정 디바이스",
      		"품목코드": 9013,
      		"수출중량": "21,118.2",
      		"수입중량": "1,006.9",
      		"수출금액": "1,921,174",
      		"수입금액": "348,694",
      		"무역수지": "1,572,480"
   		}
	}

	return json;
}
