// 엑셀파일 불러오기
let excelFile;
let newData = [];
(function () {
  excelFile = document.getElementById("file_input");
  if (excelFile) {
    excelFile.addEventListener("change", filePicked, false);
  }
})();
function filePicked(excelEvent) {
  const newFile = excelEvent.target.files[0];
  const reader = new FileReader();
  reader.onload = function (e) {
    const data = e.target.result;
    const excel = XLSX.read(data, { type: "binary" });
    excel.SheetNames.forEach(function (sheetName) {
      const sCSV = XLS.utils.make_csv(excel.Sheets[sheetName]);
      const excelJS = XLS.utils.sheet_to_json(excel.Sheets[sheetName]);

      newData = Array.from(excelJS)
        .slice(3)
        .map((cur) => {
          const tempArr = Object.values(cur).map((num_data) => {
            return num_data;
          });
          let ret = [];
          ret.push(tempArr[0]);
          for (let i = 1; i < 6; ++i) {
            ret.push(parseInt(tempArr[i].split(",").join("")));
          }
          return ret;
        });
 
      const 레이블 = newData.map((data) => data[0]);
      const 수출건수 = newData.map((data) => data[1]);
      const 수출금액 = newData.map((data) => data[2]);
      const 수입건수 = newData.map((data) => data[3]);
      const 수입금액 = newData.map((data) => data[4]);
      const 무역수지 = newData.map((data) => data[5]);
      if (newData) {
        const excel = document.getElementById("차트입니다").getContext("2d");
        const config = {
          type: "line",
          data: {
            labels: 레이블,
            datasets: [
              {
                label: "수출금액",
                data: 수출금액,
                borderColor: "rgb(255, 051, 102)",
				        backgroundColor: "rgb(255, 051, 102)",
				        fill: false,
				        borderWidth: 2,
              },
              {
                label: "수입금액",
                data: 수입금액,
                borderColor: "rgba(0, 153, 255)",
				        backgroundColor: "rgba(0, 153, 255)",
				        fill: false,
				        borderWidth: 2,
              },
              {
                label: "무역수지",
                data: 무역수지,
                backgroundColor: "rgb(0, 153, 051)",
                borderColor: "rgb(0, 153, 051)",
                fill: false,
                borderWidth: 2,
              },
              {
                label: "수출건수",
                data: 수출건수,
                borderColor: "rgb(251, 216, 28)",
				        backgroundColor: "rgb(251, 216, 28)",
                fill: false,
                borderWidth: 2,
              },
              {
                label: "수입건수",
                data: 수입건수,
                borderColor: "rgb(68, 39, 2)",
				        backgroundColor: "rgb(68, 39, 2)",
                fill: false,
                borderWidth: 2,
              },
            ],
          },
          options: {
              responsive: true,
            
            hover: {
              mode: "nearest",
              intersect: true,
            },
          },
        };

        
        new Chart(excel, config);
      }
    });
  };
  reader.readAsBinaryString(newFile);
}
